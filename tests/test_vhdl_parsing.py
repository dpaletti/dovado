import dovado.vhdl_parsing as v
import pytest


def test_list_files():
    assert v.list_files("examples/vhdl_fifo_memory") == [
        "examples/vhdl_fifo_memory/fifo.vhd"
    ]


def test_list_modules():
    assert v.list_modules("examples/vhdl_fifo_memory/fifo.vhd") == [
        "fifo_mem",
        "status_signal",
        "memory_array",
        "read_pointer",
        "write_pointer",
    ]
