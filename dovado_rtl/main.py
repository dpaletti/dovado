from pathlib import Path
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy
import toml
import sys


def main() -> None:
    input_project = Input(**toml.load(parse_config_path()))

    if not input_project.in_place:
        input_project = project_copy(input_project)


def parse_config_path() -> Path:
    if len(sys.argv) == 1:
        raise ValueError("Missing the path to the configuration file")
    return Path(sys.argv[1])
