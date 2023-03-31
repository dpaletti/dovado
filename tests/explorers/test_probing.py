from pathlib import Path
from typing import cast
from dovado_rtl.explorers.manual_explorer import ManualExplorer
from dovado_rtl.explorers.automatic_explorer import AutomaticExplorer
from dovado_rtl.explorers.utilities.tasks import (
    ManualExplorationProject,
    AutomaticExplorationProject,
)
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy
from dovado_rtl.parsers.vhdl.parse import parse
from dovado_rtl.explorers.explorer import EndExploration


def test_manual_probe():
    manual_explorer = ManualExplorer()
    input_project = Input.make_from_file(
        Path("resources/configs/test_probe_config.toml")
    )
    copied_input_project = project_copy(input_project)
    manual_exploration_project = cast(
        ManualExplorationProject, parse(copied_input_project)
    )

    design_point = manual_explorer.explore(task=manual_exploration_project)
    evaluated_design_point = EndExploration()
    out = manual_explorer.update(evaluated_design_point)
    assert isinstance(out, EndExploration)


def test_automatic_probe():
    automatic_explorer = AutomaticExplorer()
    input_project = Input.make_from_file(
        Path("resources/configs/test_probe_range_config.toml")
    )
    copied_input_project = project_copy(input_project)
    manual_exploration_project = cast(
        AutomaticExplorationProject, parse(copied_input_project)
    )

    design_point = automatic_explorer.explore(task=manual_exploration_project)
    evaluated_design_point = EndExploration()
    out = automatic_explorer.update(evaluated_design_point)
    assert isinstance(out, EndExploration)
