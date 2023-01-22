import os
from pathlib import Path
from dovado_rtl.parsers.antlr.hdl.hdl_antlr_parameter import ParameterTypeEnum
from dovado_rtl.parsers.antlr.hdl.hdl_representation import (
    PortDirectionEnum,
    PortTypeEnum,
)
from dovado_rtl.parsers.verilog2001.verilog_parsed import VerilogParsed

from dovado_rtl.parsers.verilog2001.verilog_parser import VerilogParser


def test_corundum_queue_manager_parsing():
    path_prexif: str = "../" + os.curdir + "/resources"
    to_parse = Path(path_prexif + "/corundum/fpga/common/rtl/cpl_queue_manager.v")
    parser = VerilogParser()
    parsed: VerilogParsed = parser.parse(Path(to_parse))

    assert len(parsed.entities) == 1
    entity = parsed.entities[0]

    assert (len(parsed.top_level.libraries)) == 0
    assert (len(parsed.top_level.use_clauses)) == 0

    assert (len(entity.parameters)) == 13
    assert (len(entity.ports)) == 43

    parameter = entity.parameters[0]
    assert parameter.value == "64"
    assert parameter.name == "ADDR_WIDTH"
    assert parameter.has_default == True
    assert parameter.type is not None
    assert parameter.type.type == ParameterTypeEnum.INTEGER
    assert parameter.type.descriptor == "integer"

    assert (
        parsed.replace({"ADDR_WIDTH": "32"})
        == Path(path_prexif + "/replaced_corundum_queue_manager.v").read_text()
    )

    port = entity.ports[0]
    assert port.name == "clk"
    assert port.type is not None
    assert port.type.type == PortTypeEnum.VECTOR
    assert port.type.descriptor == ""
    assert port.direction is not None
    assert port.direction.direction == PortDirectionEnum.INPUT
    assert port.direction.descriptor == "input"
