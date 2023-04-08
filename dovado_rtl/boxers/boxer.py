from pathlib import Path

from dovado_rtl.explorers.utilities.design_points import DesignPoint
from dovado_rtl.parsers.utilities.antlr.hdl.hdl_antlr_module import HdlAntlrModule
from dovado_rtl.parsers.utilities.antlr.hdl.hdl_antlr_parsed import HdlAntlrParsed
from pathlib import Path
from typing import Sequence
from dovado_rtl.parsers.utilities.port import Port
from abc import ABC, abstractmethod
from dovado_rtl.fill import fill
from nacolla.stateful_callable import StatefulCallable


class Boxer(StatefulCallable, ABC):
    _placeholder = "____"

    def __init__(self) -> None:
        super().__init__()
        self.boxed = False

    @abstractmethod
    def box(self, design_point: DesignPoint) -> DesignPoint:
        ...

    def _fill(
        self,
        replacements: list[str],
        package: str,
        resource: str,
        out_path: Path,
    ) -> None:
        fill(replacements, package, resource, out_path, self._placeholder)

    def _box_hdl_antlr(
        self,
        design_point: DesignPoint,
        package: str,
        frame_file_name: str,
        box_file_name: str,
        add_library: bool = False,
    ) -> DesignPoint:
        if self.boxed:
            return design_point

        target_source = design_point.target_source
        target_module = design_point.target_module

        if not isinstance(target_source, HdlAntlrParsed):
            raise ValueError("target source must be a HdlAntlrModule")

        parsed_module: HdlAntlrModule
        modules: Sequence[HdlAntlrModule] = target_source.modules
        if target_module is None:
            if len(target_source.modules) > 1:
                print(
                    "Target source "
                    + str(design_point.target_file)
                    + " contains more than 1 module, please specify 'target module'"
                )
            parsed_module = modules[0]
        else:
            parsed_module = target_source.get_module(target_module)

        port_replacements = self._get_port_replacements(
            parsed_module.ports, design_point.clock_port
        )

        target_module_library = str(design_point.target_file.parent)
        target_module_library = (
            target_module_library
            if str(target_module_library) != "."
            else design_point.project_root.parts[-1]
        )
        replacements = [
            (target_module_library + "." + parsed_module.name)
            if add_library
            else parsed_module.name,
            " ".join(port_replacements),
        ]
        if add_library:
            replacements.insert(0, "library " + target_module_library)
        self._fill(
            replacements=replacements,
            package=package,
            resource=frame_file_name,
            out_path=Path(design_point.work_directory, box_file_name),
        )
        self.boxed = True
        return design_point

    @staticmethod
    @abstractmethod
    def _get_port_replacements(ports: list[Port], clock_port_name: str) -> list[str]:
        ...
