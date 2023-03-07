import os
from pathlib import Path
from dovado_rtl.parsers.verilog.verilog_parsed import VerilogParsed
from dovado_rtl.parsers.verilog.verilog_parser import VerilogParser


def test_corundum_queue_manager_parsing():
    path_prexif: str = "resources"
    to_parse = Path(path_prexif + "/corundum/fpga/common/rtl/cpl_queue_manager.v")
    parser = VerilogParser()
    parsed: VerilogParsed = parser.parse(Path(to_parse))

    assert len(parsed.modules) == 1
    module = parsed.modules[0]

    assert (len(module.parameters)) == 18
    assert (len(module.ports)) == 43

    parameter = module.parameters[0]
    assert parameter.value == "64"
    assert parameter.name == "ADDR_WIDTH"
    assert parameter.has_default == True

    assert (
        parsed.replace({"cpl_queue_manager": {"ADDR_WIDTH": "32"}})
        == Path(path_prexif + "/replaced_corundum_queue_manager.v").read_text()
    )

    assert module.ports[0].name == "clk"
    assert module.ports[0].direction == "input"
    assert module.ports[5].name == "s_axis_enqueue_req_ready"
    assert module.ports[5].direction == "output"
