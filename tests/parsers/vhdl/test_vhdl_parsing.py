from pathlib import Path
from dovado_rtl.parsers.vhdl.vhdl_parsed import VhdlParsed
from dovado_rtl.parsers.vhdl.vhdl_parser import VhdlParser
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy


def test_neorv_top_parsing():
    project = Input.make_from_file(Path("resources/configs/test_config.toml"))
    copied_project = project_copy(project)

    parser = VhdlParser()
    parsed: VhdlParsed = parser.parse(
        Path(copied_project.project_root, "neorv32_top.vhd")
    )

    # Only scalar parameters are supported
    assert len(parsed.entities) == 1
    entity = parsed.entities[0]

    assert len(entity.parameters) == 69
    assert len(entity.ports) == 55

    non_default_parameter = entity.parameters[0]
    default_parameter = entity.parameters[1]

    assert non_default_parameter.name == "CLOCK_FREQUENCY"
    assert non_default_parameter.value == ""
    assert non_default_parameter.rule.getText() == "natural"

    assert default_parameter.name == "HART_ID"
    assert default_parameter.value == 'x"00000000"'
    assert default_parameter.rule.getText() == 'x"00000000"'

    clk_port = entity.ports[0]

    assert clk_port.name == "clk_i"
    assert clk_port.dimension == "scalar"
    assert clk_port.direction == "input"

    wb_tag_o = entity.ports[7]
    assert wb_tag_o.name == "wb_tag_o"
    assert wb_tag_o.dimension == "vectorial"
    assert wb_tag_o.direction == "output"

    assert (
        parsed.replace(
            {
                "neorv32_top": {
                    "CLOCK_FREQUENCY": "10",
                    "HART_ID": "11",
                    "INT_BOOTLOADER_EN": "1",
                }
            }
        )
        == Path("resources/replaced_neorv_top.vhd").read_text()
    )
