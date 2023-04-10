from dovado_rtl.generators.bash_generator import BashGenerator
from dovado_rtl.parsers.scala.parse import parse
from pathlib import Path
from dovado_rtl.explorers.manual_explorer import ManualExplorer
from dovado_rtl.explorers.utilities.tasks import ManualExplorationProject
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy
from typing import cast


def test_bash():
    manual_explorer = ManualExplorer()
    input_project = Input.make_from_file(
        Path("resources/configs/test_scala_config.toml")
    )

    copied_input_project = project_copy(input_project)
    manual_exploration_project = cast(
        ManualExplorationProject, parse(copied_input_project)
    )

    design_point = manual_explorer.explore(task=manual_exploration_project)
    generator = BashGenerator()
    generator.generate(design_point)
    assert Path("resources/rocket-chip/vsim/generated-src").is_dir()
