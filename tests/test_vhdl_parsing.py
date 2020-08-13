import dovado.vhdl_parsing as test
import tests.test_parsing_data as data
import pytest
from pathlib import Path


def test_list_files():
    for dir in [x for x in Path("examples").iterdir()]:
        test_out = test.list_files(dir)
        if dir.is_dir():
            for file in [x for x in dir.iterdir()]:
                assert file in test_out if file.suffix == "vhd" else True
    assert test.list_files("") == []


def test_list_modules():
    assert test.list_modules(
        Path("examples/vhdl_fifo_memory/fifo.vhd").read_text()
    ) == [
        "fifo_mem",
        "status_signal",
        "memory_array",
        "read_pointer",
        "write_pointer",
    ]


def test_strip_comments():
    assert test.strip_comments("--test comment\n") == "\n"


def test_get_entity():
    assert (
        test.get_entity(
            Path("./examples/vhdl_fifo_memory/fifo.vhd").read_text(),
            "status_signal",
        )
        == data.fifo_mem_entity_status_signal.strip()
    )
    assert not test.get_entity("", "ignored")


def test_is_entity():
    assert test.is_entity(
        test.get_entity(
            Path("./examples/vhdl_fifo_memory/fifo.vhd").read_text(),
            "status_signal",
        )
    )

    assert test.is_entity(
        test.get_entity(
            Path(
                "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd"
            ).read_text(),
            "rbs",
        )
    )


def test_strip_parameters():
    assert test.strip_parameters(
        test.get_entity(
            Path(
                "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd"
            ).read_text(),
            "rbs",
        )
    )[1] == ["Nbit_rbs : integer"]
    assert test.strip_parameters("entity generic") == ("entity generic", None)

    with pytest.raises(ValueError):
        test.strip_parameters("")


def test_list_declarations():
    assert test.list_declarations(
        test.get_entity(
            Path("./examples/vhdl_fifo_memory/fifo.vhd").read_text(),
            "fifo_mem",
        )
    ) == [
        "data_out : out std_logic_vector(7 downto 0)",
        "fifo_full, fifo_empty, fifo_threshold, fifo_overflow, fifo_underflow: out std_logic",
        "clk :in std_logic",
        "rst_n: in std_logic",
        "wr :in std_logic",
        "rd: in std_logic",
        "data_in: in std_logic_vector(7 downto 0)",
    ]
    assert test.list_declarations(
        test.get_entity(
            Path(
                "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd"
            ).read_text(),
            "rbs",
        )
    ) == [
        "minN : in std_logic_vector(Nbit_rbs - 1 downto 0)",
        "subN : in std_logic_vector(Nbit_rbs - 1 downto 0)",
        "binN : in std_logic",
        "boutN: out std_logic",
        "diffN: out std_logic_vector(Nbit_rbs - 1 downto 0)",
    ]

    with pytest.raises(ValueError):
        test.list_declarations("")


def test_declaration_exists():
    assert (
        test.declaration_exists(
            [
                "minN : in std_logic_vector(Nbit_rbs - 1 downto 0)",
                "subN : in std_logic_vector(Nbit_rbs - 1 downto 0)",
                "binN : in std_logic",
                "boutN: out std_logic",
                "diffN: out std_logic_vector(Nbit_rbs - 1 downto 0)",
            ],
            "minN",
        )
        == "minN : in std_logic_vector(Nbit_rbs - 1 downto 0)"
    )

    assert not (
        test.declaration_exists(
            [
                "minN : in std_logic_vector(Nbit_rbs - 1 downto 0)",
                "subN : in std_logic_vector(Nbit_rbs - 1 downto 0)",
                "binN : in std_logic",
                "boutN: out std_logic",
                "diffN: out std_logic_vector(Nbit_rbs - 1 downto 0)",
            ],
            "gianni minà",
        )
    )


def test_get_direction():
    assert (
        test.get_direction("minN : in std_logic_vector(Nbit_rbs - 1 downto 0)")
        == "in"
    )
    with pytest.raises(ValueError):
        test.get_direction(
            "minN : incà std_logic_vector(Nbit_rbs - 1 downto 0)"
        ) == "incà"


def test_get_type():
    assert (
        test.get_type("minN : in std_logic_vector(Nbit_rbs - 1 downto 0)")
        == "std_logic_vector"
    )

    assert test.get_type("binN : in std_logic") == "std_logic"


def test_sub_declaration_identifier():
    assert (
        test.sub_declaration_identifier(
            "fifo_full, fifo_empty, fifo_threshold, fifo_overflow,"
            + "fifo_underflow: out std_logic",
            "fifo_empty",
        )
        == "fifo_empty: out std_logic"
    )
    with pytest.raises(ValueError):
        test.sub_declaration_identifier(
            "fifo_full, fifo_empty, fifo_threshold, fifo_overflow,"
            + "fifo_underflow out std_logic",
            "fifo_empty",
        )
