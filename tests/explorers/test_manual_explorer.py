from pathlib import Path
from typing import cast
from dovado_rtl.explorers.explorer import EndExploration
from dovado_rtl.explorers.manual_explorer import ManualExplorer
from dovado_rtl.explorers.utilities.design_points import EvaluatedDesignPoint
from dovado_rtl.explorers.utilities.tasks import ManualExplorationProject
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy
from dovado_rtl.parsers.vhdl.parse import parse
import csv


def test_manual_explorer():
    manual_explorer = ManualExplorer()
    input_project = Input.make_from_file(Path("resources/configs/test_config.toml"))
    copied_input_project = project_copy(input_project)
    manual_exploration_project = cast(
        ManualExplorationProject, parse(copied_input_project)
    )

    design_point = manual_explorer.explore(task=manual_exploration_project)

    assert design_point.points[Path("neorv32_top.vhd")] == {
        "neorv32_top": {
            "CLOCK_FREQUENCY": "1000000",
            "CPU_EXTENSION_RISCV_B": "false",
            "MEM_INT_IMEM_SIZE": "1024",
            "PMP_NUM_REGIONS": "0",
        }
    }

    while not isinstance(design_point, EndExploration):
        evaluated_design_point = EvaluatedDesignPoint(
            **dict(design_point),
            design_value=dict(
                zip(
                    design_point.default_metrics
                    + list(design_point.custom_metrics.keys()),
                    [0] * 5,
                )
            )
        )
        design_point = manual_explorer.update(evaluated_design_point)
        assert_exploration_file(Path(manual_exploration_project.work_directory))


def assert_exploration_file(work_directory: Path):

    last_exploration_file = get_exploration_file(work_directory, name="exploration")

    csv_dict = csv.DictReader(last_exploration_file.open())
    rows = [row for row in csv_dict]
    assert list(rows[0].keys()) == [
        "Slice LUTs",
        "DSPs",
        "frequency",
        "test_metric",
        "another_test_metric",
    ]
    assert len(rows) == 1
    assert rows[1] == {
        "Slice LUTs": "0.0",
        "DSPs": "0.0",
        "frequency": "0.0",
        "test_metric": "0.0",
        "another_test_metric": "0.0",
    }


def get_exploration_file(path: Path, name: str) -> Path:
    files = [file for file in path.iterdir() if name in str(file)]
    if len(files) == 1:
        return files[0]
    else:
        versions = [
            int(str(file.parts[-1]).replace(name, "").replace(file.suffix, ""))
            for file in files
            if str(file.parts[-1]).replace(name, "").replace(file.suffix, "") != ""
        ]
        files.remove(Path(path, name + files[0].suffix))
        return files[versions.index(max(versions))]
