from pathlib import Path
from dovado_rtl.parsers.vhdl_parsed import VhdlParsed
from dovado_rtl.parsers.vhdl_parser import VhdlParser
import os


def test_neorv_top_parsing():
    to_parse = Path("../" + os.curdir + "/resources/neorv32/rtl/core/neorv32_top.vhd")
    parser = VhdlParser()
    parsed: VhdlParsed = parser.parse(Path(to_parse))
    assert len(parsed.entities) == 1
    # Only scalar parameters are supported
    assert len(parsed.entities[0].parameters) == 65
    assert len(parsed.entities[0].ports) == 0
    # TODO: finish test
    # TODO: test some parameters and some ports
    print(parsed.entities)
