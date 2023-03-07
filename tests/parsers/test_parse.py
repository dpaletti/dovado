from pathlib import Path
import os
import toml

from dovado_rtl.input import Input
from dovado_rtl.parsers.parse import parse
from dovado_rtl.parsers.vhdl.vhdl_parser import VhdlParser


def test_parse():

    path_prefix: str = "resources"
    to_parse = Path(path_prefix + "/configs/test_config.toml")
    input_project = Input(**toml.load(to_parse))
    parse(input_project, VhdlParser)
