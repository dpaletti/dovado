from dovado_rtl.explorers.manual_explorer import ManualExplorer
from dovado_rtl.explorers.utilities.tasks import ManualExplorationProject
from dovado_rtl.input import Input
from dovado_rtl.parsers.verilog.parse import parse
from dovado_rtl.boxers.verilog.boxer import VerilogBoxer
from pathlib import Path
from typing import cast


def test_verilog_box():

    manual_explorer = ManualExplorer()
    input_project = Input.make_from_file(
        Path("resources/configs/test_verilog_config.toml")
    )
    manual_exploration_project = cast(ManualExplorationProject, parse(input_project))

    design_point = manual_explorer.explore(task=manual_exploration_project)
    boxer = VerilogBoxer()
    boxer.box(design_point)
    assert Path("dovado_work/box.sv").read_text().replace(" ", "").replace(
        "\n", ""
    ) == Path("resources/corundum_box.sv").read_text().replace(" ", "").replace(
        "\n", ""
    )

    assert boxer.boxed
