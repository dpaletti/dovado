from pathlib import Path
import os
import toml

from dovado_rtl.input import Input
from dovado_rtl.parsers.parse import parse
from dovado_rtl.parsers.vhdl.parse import parse as vhdl_parser
from dovado_rtl.parsers.vhdl.vhdl_parser import VhdlParser


def test_parse():

    path_prefix: str = "../" + os.curdir + "/resources/configs"
    to_parse = Path(path_prefix + "/test_config.toml")
    input_project = Input(**toml.load(to_parse))
    manual_exploration = parse(input_project, VhdlParser)
