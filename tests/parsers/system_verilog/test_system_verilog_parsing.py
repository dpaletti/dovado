import os
from pathlib import Path
from dovado_rtl.parsers.system_verilog.system_verilog_parsed import SystemVerilogParsed
from dovado_rtl.parsers.system_verilog.system_verilog_parser import SystemVerilogParser


def test_cv32e40p_core_parsing():
    path_prexif: str = "resources"
    to_parse = Path(path_prexif + "/cv32e40p/rtl/cv32e40p_core.sv")
    parser = SystemVerilogParser()
    parsed: SystemVerilogParsed = parser.parse(Path(to_parse))
    assert len(parsed.modules) == 1
    module = parsed.modules[0]
    assert module.name == "cv32e40p_core"

    assert len(module.parameters) == 5
    assert module.parameters[0].name == "PULP_XPULP"
    assert module.parameters[-1].name == "NUM_MHPMCOUNTERS"

    assert len(module.ports) == 39
    assert module.ports[0].name == "clk_i"
    assert module.ports[0].dimension == "scalar"
    assert module.ports[0].direction == "input"
    assert module.ports[4].name == "boot_addr_i"
    assert module.ports[4].dimension == "vectorial"
    assert module.ports[4].direction == "input"
    assert module.ports[-1].name == "core_sleep_o"
    assert module.ports[-1].dimension == "scalar"
    assert module.ports[-1].direction == "output"

    assert (
        parsed.replace({"cv32e40p_core": {"PULP_XPULP": "1"}})
        == Path(path_prexif + "/replaced_cv32e40p_core.sv").read_text()
    )
