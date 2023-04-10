from dovado_rtl.generators.vitis.generator import VitisGenerator
from dovado_rtl.parsers.cpp.parse import parse
from pathlib import Path
from dovado_rtl.explorers.manual_explorer import ManualExplorer
from dovado_rtl.explorers.utilities.tasks import ManualExplorationProject
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy
from typing import cast


def test_vitis():
    manual_explorer = ManualExplorer()
    input_project = Input.make_from_file(Path("resources/configs/test_cpp_config.toml"))

    copied_input_project = project_copy(input_project)
    manual_exploration_project = cast(
        ManualExplorationProject, parse(copied_input_project)
    )

    design_point = manual_explorer.explore(task=manual_exploration_project)
    generator = VitisGenerator()
    generator.generate(design_point)
    assert Path(
        design_point.work_directory, "hls_generated", "solution1", "syn"
    ).is_dir()
    print()
