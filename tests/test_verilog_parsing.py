import dovado.verilog_parsing as v
import pytest


def test_list_files():
    assert v.list_files("examples/verilog_unsigned_adder") == [
        "examples/verilog_unsigned_adder/unsigned_adder.v"
    ]


def test_list_modules():
    print(v.list_modules("examples/verilog_fifo_memory/fifo.v"))
    assert v.list_modules("examples/verilog_fifo_memory/fifo.v") == [
        "fifo_mem",
        "memory_array",
        "read_pointer",
        "status_signal",
        "write_pointer",
    ]
