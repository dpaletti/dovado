from pathlib import Path
from nacolla.parsing import parse_implementation_map
import toml
from dovado_rtl.explorers.utilities.tasks import ManualExplorationProject

from dovado_rtl.input import Input


def test_nacolla_parsers():
    path_prefix = "resources"

    to_parse = Path(path_prefix + "/configs/test_config.toml")
    input_project = Input(**toml.load(to_parse))

    implementation_map = parse_implementation_map(
        Path(path_prefix + "/flow_files/implementation_file.json")
    )
    parsed = implementation_map["vhdl_parser"](input_project)
    assert isinstance(parsed, ManualExplorationProject)
    assert parsed.project_root == Path("resources/neorv32/rtl")
