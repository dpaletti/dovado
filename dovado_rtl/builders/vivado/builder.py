from dovado_rtl.builders.builder import Builder
from dovado_rtl.builders.vivado.vivado import Vivado
from dovado_rtl.explorers.utilities.design_points import (
    DesignPoint,
    EvaluatedDesignPoint,
)
from pathlib import Path
import re
from typing import Dict, Any, List, Optional
from bs4 import BeautifulSoup
from bs4.element import PageElement, ResultSet
import numpy as np
from typing import Union
from dovado_rtl.explorers.utilities.tasks import EndExploration


class VivadoBuilder(Builder):
    _output_directory = "vivado_out"
    _constraint_package = "constraint_files"
    _constraint_frame = "constraint_frame.xdc"
    _constraint_file = "constraint.xdc"
    _tcl_package = "tcl_scripts"
    _synthesis_frame = "synthesis_frame.tcl"
    _synthesis_filled = "synthesis.tcl"
    _implementation_frame = "implementation_frame.tcl"
    _implementation_filled = "implementation.tcl"
    _package = "dovado_rtl.builders.vivado"
    _box = "box"
    _post_synth_timing = "post_synth_setup_timing.rpt"
    _post_synth_util = "post_synth_util.xml"
    _post_impl_timing = "post_impl_setup_timing.rpt"
    _post_impl_util = "post_impl_util.xml"
    _metrics_file = "metrics.txt"

    def __init__(self) -> None:
        super().__init__()
        self._vivado = Vivado()
        self._tcl_script: Optional[Path] = None

    def build(
        self, design_point: DesignPoint
    ) -> Union[EvaluatedDesignPoint, EndExploration]:
        if not self._vivado.is_board_valid(design_point.board):
            raise ValueError(
                "Board '"
                + str(design_point.board)
                + "' is invalid. Please pick one among:\n"
                + str(set(self._vivado.get_boards().keys()))
            )

        if not self._tcl_script:
            self._tcl_script = self._make_tcl_file(design_point)

        vivado_out, success = self._vivado.execute_script(str(self._tcl_script))
        if design_point.verbose:
            print(vivado_out)

        if not design_point.custom_metrics and not design_point.default_metrics:
            self._write_all_metrics(design_point)
            return EndExploration()

        design_value = VivadoBuilder._compute_metrics(success, design_point)

        return EvaluatedDesignPoint(**dict(design_point), design_value=design_value)

    @staticmethod
    def _write_all_metrics(design_point: DesignPoint):
        utilisation_report = (
            VivadoBuilder._post_impl_util
            if design_point.implementation
            else VivadoBuilder._post_synth_util
        )

        report_directory = Path(
            design_point.work_directory, VivadoBuilder._output_directory
        )
        metrics = VivadoBuilder._get_all_metrics(
            Path(report_directory, utilisation_report)
        )
        Path(report_directory, VivadoBuilder._metrics_file).write_text(
            "\n".join(metrics)
        )

    @staticmethod
    def _get_all_metrics(report_path: Path):
        report = BeautifulSoup(report_path.open(), "lxml-xml")
        report_structure = VivadoBuilder._get_available_indices(report)
        out = []
        for metrics in report_structure.values():
            for metric in metrics:
                out.append(metric)
        return out

    @staticmethod
    def _compute_metrics(success: bool, design_point: DesignPoint) -> dict[str, float]:
        custom_metrics = design_point.custom_metrics
        default_metrics = design_point.default_metrics
        if not success:
            return {
                metric: 0
                if (metric in custom_metrics) or (metric == "frequency")
                else 100
                for metric in list(custom_metrics.keys()) + default_metrics
            }

        utilisation_report = (
            VivadoBuilder._post_impl_util
            if design_point.implementation
            else VivadoBuilder._post_synth_util
        )
        timing_report = (
            VivadoBuilder._post_impl_timing
            if design_point.implementation
            else VivadoBuilder._post_synth_timing
        )
        report_directory = Path(
            design_point.work_directory, VivadoBuilder._output_directory
        )

        evaluation = {}
        if "frequency" in default_metrics:
            evaluation["frequency"] = VivadoBuilder._get_frequency(
                Path(report_directory, timing_report),
                target_clock=design_point.target_clock,
            )

        if default_metrics:
            evaluation = evaluation | VivadoBuilder._get_utilisation_values(
                Path(report_directory, utilisation_report),
                [metric for metric in default_metrics if metric != "frequency"],
            )

        if custom_metrics:
            custom_metric_input = (
                VivadoBuilder._get_utilisation_values(
                    Path(report_directory, utilisation_report)
                )
                | {
                    str(path): module_to_params
                    for path, module_to_params in design_point.points.items()
                }
                | {
                    "frequency": VivadoBuilder._get_frequency(
                        Path(report_directory, timing_report),
                        target_clock=design_point.target_clock,
                    )
                }
            )

            for custom_metric_name, custom_metric_function in custom_metrics.items():
                evaluation[custom_metric_name] = custom_metric_function(
                    **custom_metric_input
                )

        return evaluation

    def _make_tcl_file(self, design_point: DesignPoint) -> Path:
        output_directory = str(
            Path(design_point.work_directory, VivadoBuilder._output_directory)
        )
        source_file = str(design_point.project_root)
        constraint_file_path = Path(
            design_point.work_directory, VivadoBuilder._constraint_file
        )
        constraint_file = str(constraint_file_path)
        self._fill(
            [str(1000 / design_point.target_clock)],
            VivadoBuilder._package + "." + VivadoBuilder._constraint_package,
            VivadoBuilder._constraint_frame,
            constraint_file_path,
        )
        libraries = self._get_libraries(design_point.project_root)
        libraries = ("{ " + " ".join(libraries) + " }") if libraries else "[list]"
        extension = design_point.target_file.suffix
        read_box: str
        if extension == ".vhd":
            read_box = "read_vhdl -vhdl2008 -library root " + str(
                Path(design_point.work_directory, VivadoBuilder._box + ".vhd")
            )
        elif extension == ".v" or extension == ".sv":
            read_box = "read_verilog -sv -library root " + str(
                Path(design_point.work_directory, VivadoBuilder._box + ".sv")
            )
        else:
            raise ValueError(
                "Could not recognize extension '"
                + str(extension)
                + "' in target file '"
                + str(design_point.target_file)
                + "'"
            )
        top = VivadoBuilder._box
        board = design_point.board
        synthesis_directive = design_point.synthesis_directive
        checkpoint_directive = "-incremental_synth" if design_point.incremental else ""
        timing_report = VivadoBuilder._post_synth_timing
        utilization_report = VivadoBuilder._post_synth_util
        replacements: list[str] = [
            output_directory,
            source_file,
            constraint_file,
            libraries,
            read_box,
            top,
            board,
            synthesis_directive,
            checkpoint_directive,
            timing_report,
            utilization_report,
        ]

        filled_file_path: Path
        full_tcl_package: str = (
            VivadoBuilder._package + "." + VivadoBuilder._tcl_package
        )
        if design_point.implementation:
            place_directive = design_point.place_directive
            route_directive = design_point.route_directive
            replacements.insert(-2, place_directive)
            replacements.insert(-2, route_directive)
            filled_file_path = Path(
                design_point.work_directory, VivadoBuilder._implementation_filled
            )
            self._fill(
                replacements,
                full_tcl_package,
                VivadoBuilder._implementation_frame,
                filled_file_path,
            )
        else:
            filled_file_path = Path(
                design_point.work_directory, VivadoBuilder._synthesis_filled
            )
            self._fill(
                replacements,
                full_tcl_package,
                VivadoBuilder._synthesis_frame,
                filled_file_path,
            )

        if design_point.incremental:
            filled_file_path.write_text(filled_file_path.read_text().replace("#!", ""))

        return filled_file_path

    @staticmethod
    def _get_libraries(project_root: Path) -> list[str]:
        libraries = [
            str(directory.parts[-1])
            for directory in project_root.rglob("*")
            if directory.is_dir()
        ]
        libraries.insert(0, project_root.parts[-1])
        return libraries

    @staticmethod
    def _represents_float(s: Any):
        try:
            float(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def _get_percentage_util(columns: ResultSet, row: PageElement) -> str:
        column_number = 0
        column: PageElement
        for column in columns:
            if str(column.get("contents")) == "Util%":
                column_number: int = int(columns.index(column))
                break
        siebling = row
        if column_number > 0:
            for _ in range(0, column_number - 1):
                siebling: Any = siebling.findNext("tablecell")
        return siebling.findNext("tablecell").get("contents")

    @staticmethod
    def _get_utilisation_values(
        report_path: Path, utilisation_metrics: Optional[list[str]] = None
    ) -> dict[str, float]:
        report = BeautifulSoup(report_path.open(), "lxml-xml")
        report_structure = VivadoBuilder._get_available_indices(report)
        values = {}
        if utilisation_metrics is None:
            for section, metrics in report_structure.items():
                for metric in metrics:
                    values[metric] = VivadoBuilder._get_utilisation(
                        report, section, metric
                    )
            return values

        for utilisation_metric in utilisation_metrics:
            section = VivadoBuilder._get_section(report_structure, utilisation_metric)
            values[utilisation_metric] = VivadoBuilder._get_utilisation(
                report, section, utilisation_metric
            )
        return values

    @staticmethod
    def _get_section(report_structure: dict[str, list[str]], utilisation_metric: str):
        for section, metrics in report_structure.items():
            if utilisation_metric.lower() in [metric.lower() for metric in metrics]:
                return section
        raise ValueError(
            "Could not find "
            + str(utilisation_metric)
            + " in utilisation report:\n"
            + str(report_structure)
        )

    @staticmethod
    def _get_available_indices(report: BeautifulSoup) -> Dict[str, List[str]]:
        indices = {}
        sections_partial: ResultSet = report.find_all("section")
        sections = []
        sections.extend(sections_partial)
        for section in sections:

            for nested_section in section.find_all("section"):
                nested_section.decompose()

            columns = []
            rows = []

            for column in (
                section.find("tablerow").find_all("tableheader")
                if section.find("tablerow")
                else []
            ):
                columns.append(column.get("contents").strip())
            if "Util%" in columns:
                for row in section.find_all("tablerow"):
                    if row.find("tablecell") and VivadoBuilder._represents_float(
                        VivadoBuilder._get_percentage_util(
                            section.find_all("tableheader"), row
                        )
                    ):
                        rows.append(row.find("tablecell").get("contents").strip())
                indices[section.get("title")] = rows

        return indices

    @staticmethod
    def _get_utilisation(report: BeautifulSoup, section_name: str, row_name: str):
        section: PageElement = report.find("section", {"title": section_name})
        columns: ResultSet = section.find_all("tableheader")
        row: PageElement = section.find(
            "tablecell",
            {"contents": re.compile("[ \t\r\n]*" + row_name + r"(\*)?[ \t\r\n]*")},
        )
        try:
            return float(VivadoBuilder._get_percentage_util(columns, row))
        except Exception:
            return 0

    @staticmethod
    def _get_frequency(report_path: Path, target_clock: float) -> float:
        return VivadoBuilder._get_max_frequency(
            target_clock, VivadoBuilder._get_wns(report_path)
        )

    @staticmethod
    def _get_max_frequency(target_clock: float, wns: float) -> float:

        return 1000 / (1 / (1 / 1000 * target_clock) - wns)

    @staticmethod
    def _get_wns(report_path: Path) -> float:
        try:
            first_line = report_path.open().readline()
            try:
                return float(re.findall(r"([-+]?(\d*\.\d*|inf))", first_line)[0][0])
            except Exception:
                return float(np.inf)

        except FileNotFoundError as f:
            raise FileNotFoundError(
                "Wrong path: "
                + str(report_path)
                + "\n"
                + "FileNotFoundError: "
                + str(f)
            )
