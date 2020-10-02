import dovado.src_parsing as test
import pytest
from pathlib import Path


def test_parse():
    test.parse(Path("./examples/vhdl_ripple_borrow_subtractor/rbs.vhd"))
    assert test.parsed
    assert test.parsed_src_path
    test.parse(Path("./examples/verilog_unsigned_adder/unsigned_adder.sv"))
    assert test.parsed
    assert test.parsed_src_path
    with pytest.raises(ValueError):
        test.parse(Path("./tests/resources/vhdl_wrong.vhd"))

    with pytest.raises(ValueError):
        test.parse(Path("./tests/resources/verilog_wrong.v"))


def test_get_modules():
    assert test.get_modules(
        Path("./examples/vhdl_ripple_borrow_subtractor/rbs.vhd")
    ) == ["rbs"]
    assert test.get_modules(
        Path("./examples/verilog_unsigned_adder/unsigned_adder.sv")
    ) == ["krnl_vadd_rtl_adder"]
    assert test.get_modules(
        Path("./examples/verilog_unsigned_adder/unsigned_adder.sv")
    ) == ["krnl_vadd_rtl_adder"]


def test_get_parameters():
    test.parsed = None
    assert (
        test.get_parameters(
            Path("./examples/vhdl_ripple_borrow_subtractor/rbs.vhd"), "rbs"
        )[0].name
        == "Nbit_rbs"
    )
    assert [
        i.name
        for i in test.get_parameters(
            Path("./examples/verilog_unsigned_adder/unsigned_adder.sv"),
            "krnl_vadd_rtl_adder",
        )
    ] == ["C_DATA_WIDTH", "C_NUM_CHANNELS"]
    assert (
        test.get_parameters(
            Path("./examples/vhdl_fifo_memory/fifo.vhd"), "fifo_mem"
        )[0].name
        == "fake"
    )
