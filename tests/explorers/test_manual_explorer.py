from pathlib import Path
from typing import cast
from dovado_rtl.explorers.manual_explorer import ManualExplorer
from dovado_rtl.explorers.tasks import ManualExplorationProject
from dovado_rtl.input import Input
from dovado_rtl.parsers.vhdl.parse import parse


def test_manual_explorer():
    manual_explorer = ManualExplorer()
    input_project = Input.make_from_file(Path("resources/configs/test_config.toml"))
    manual_exploration_project = cast(ManualExplorationProject, parse(input_project))

    design_point = manual_explorer.explore(task=manual_exploration_project)

    assert design_point.points[Path("core/neorv32_top.vhd")] == {
        "neorv32_top": {
            "CPU_EXTENSION_RISCV_B": "false",
            "PMP_NUM_REGIONS": "0",
            "MEM_INT_IMEM_SIZE": "1024",
        }
    }
