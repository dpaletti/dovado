from pathlib import Path
from dovado_rtl.parsers.verilog.verilog_parsed import VerilogParsed
from dovado_rtl.parsers.verilog.verilog_parser import VerilogParser
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy


def test_corundum_queue_manager_parsing():
    project = Input.make_from_file(Path("resources/configs/test_verilog_config.toml"))
    copied_project = project_copy(project)
    parser = VerilogParser()
    parsed: VerilogParsed = parser.parse(
        Path(copied_project.project_root, copied_project.target_file)
    )

    assert len(parsed.modules) == 1
    module = parsed.modules[0]

    assert (len(module.parameters)) == 19
    assert (len(module.ports)) == 42

    parameter = module.parameters[0]
    assert parameter.value == "64"
    assert parameter.name == "ADDR_WIDTH"
    assert parameter.has_default == True

    assert (
        parsed.replace({"queue_manager": {"ADDR_WIDTH": "32"}})
        == Path("resources/replaced_corundum_queue_manager.v").read_text()
    )

    assert module.ports[0].name == "clk"
    assert module.ports[0].direction == "input"
    assert module.ports[5].name == "s_axis_dequeue_req_ready"
    assert module.ports[5].direction == "output"
