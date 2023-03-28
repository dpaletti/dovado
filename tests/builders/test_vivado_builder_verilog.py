from dovado_rtl.explorers.manual_explorer import ManualExplorer
from dovado_rtl.explorers.utilities.tasks import ManualExplorationProject
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy
from dovado_rtl.parsers.verilog.parse import parse
from dovado_rtl.builders.vivado.builder import VivadoBuilder
from dovado_rtl.boxers.verilog.boxer import VerilogBoxer
from pathlib import Path
from typing import cast


def test_vivado_builder_verilog():
    manual_explorer = ManualExplorer()
    input_project = Input.make_from_file(
        Path("resources/configs/test_verilog_config.toml")
    )
    copied_input_project = project_copy(input_project)
    manual_exploration_project = cast(
        ManualExplorationProject, parse(copied_input_project)
    )

    design_point = manual_explorer.explore(task=manual_exploration_project)

    boxer = VerilogBoxer()
    boxer.box(design_point)

    builder = VivadoBuilder()
    evaluated_design_point = builder.build(design_point)

    assert evaluated_design_point.design_value == {
        "frequency": 193.98642095053344,
        "Slice LUTs*": 1.15,
        "test_metric": 1193.9864209505336,
        "another_test_metric": 1.0,
    }
