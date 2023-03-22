import csv
from pathlib import Path
from typing import cast
from dovado_rtl.explorers.automatic_explorer import AutomaticExplorer, EndResult
from dovado_rtl.explorers.utilities.design_points import EvaluatedDesignPoint
from dovado_rtl.explorers.utilities.tasks import AutomaticExplorationProject
from dovado_rtl.input import Input
from dovado_rtl.parsers.vhdl.parse import parse
from tests.explorers.test_manual_explorer import get_exploration_file


def test_automatic_explorer():
    automatic_explorer = AutomaticExplorer()
    input_project = Input.make_from_file(
        Path("resources/configs/test_range_config.toml")
    )
    automatic_exploration_project = cast(
        AutomaticExplorationProject, parse(input_project)
    )

    design_point = automatic_explorer.explore(task=automatic_exploration_project)
    while not isinstance(design_point, EndResult):
        evaluated_design_point = EvaluatedDesignPoint(
            **dict(design_point),
            design_value=dict(
                zip(
                    design_point.default_metrics
                    + list(design_point.custom_metrics.keys()),
                    [0] * 4,
                )
            )
        )
        design_point = automatic_explorer.update(evaluated_design_point)
    print(design_point.result)

    parameters_file = get_exploration_file(
        Path(automatic_exploration_project.work_directory), name="parameters"
    )
    metrics_file = get_exploration_file(
        Path(automatic_exploration_project.work_directory), name="metrics"
    )

    parameters_csv = csv.DictReader(parameters_file.open())
    metrics_csv = csv.DictReader(metrics_file.open())
    parameters_csv_rows = [row for row in parameters_csv]
    metrics_csv_rows = [row for row in metrics_csv]
    power_of_two_rows = [row["MEM_INT_IMEM_SIZE"] for row in parameters_csv_rows]
    step_rows = [row["HPM_CNT_WIDTH"] for row in parameters_csv_rows]
    step = cast(
        int,
        automatic_exploration_project.space.get_range(
            list(automatic_exploration_project.parameter_sources.keys())[0],
            "neorv32_top",
            "HPM_CNT_WIDTH",
        ).step,
    )

    assert design_point.result.X is not None
    assert design_point.result.F is not None
    assert len(parameters_csv_rows) == len(design_point.result.X)
    assert len(metrics_csv_rows) == len(design_point.result.F)
    assert len(parameters_csv_rows) == len(metrics_csv_rows)

    for step_row_value in step_rows:
        assert int(step_row_value) % step == 0

    for power_row_value in power_of_two_rows:
        assert is_power_of_two(int(power_row_value))

    # Revert file to original values
    restored = automatic_exploration_project.replace(
        Path("core/neorv32_top.vhd"),
        {
            "neorv32_top": {
                "MEM_INT_IMEM_SIZE": "16*1024",
                "CPU_EXTENSION_RISCV_B": "0",
                "PMP_NUM_REGIONS": "0",
                "HPM_CNT_WIDTH": "40",
            }
        },
    )

    Path(automatic_exploration_project.project_root, "core/neorv32_top.vhd").write_text(
        restored
    )


def is_power_of_two(x: int) -> bool:
    return (x != 0) and ((x & (x - 1)) == 0)
