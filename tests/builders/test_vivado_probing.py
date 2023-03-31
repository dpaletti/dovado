from dovado_rtl.explorers.manual_explorer import ManualExplorer
from dovado_rtl.explorers.utilities.tasks import (
    ManualExplorationProject,
    EndExploration,
)
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy
from dovado_rtl.parsers.vhdl.parse import parse
from dovado_rtl.builders.vivado.builder import VivadoBuilder
from dovado_rtl.boxers.vhdl.boxer import VhdlBoxer
from pathlib import Path
from typing import cast


def test_vivado_probing():
    manual_explorer = ManualExplorer()
    input_project = Input.make_from_file(
        Path("resources/configs/test_probe_config.toml")
    )
    copied_input_project = project_copy(input_project)
    manual_exploration_project = cast(
        ManualExplorationProject, parse(copied_input_project)
    )

    design_point = manual_explorer.explore(task=manual_exploration_project)
    boxer = VhdlBoxer()
    boxer.box(design_point)

    builder = VivadoBuilder()
    evaluated_design_point = builder.build(design_point)
    assert isinstance(evaluated_design_point, EndExploration)
