import dovado.user_input as test
import io
import tests.vivado_2019_2_mock_data as version_dependent
from pathlib import Path
from unittest.mock import patch
import pytest


def test_ask_code_dir():
    for dir in [x for x in Path("examples").iterdir() if x.is_dir()]:
        with patch("sys.stdin", io.StringIO(str(dir))):
            assert test.ask_code_dir() == str(dir)

    with patch("sys.stdin", io.StringIO("\n")):
        assert test.ask_code_dir() == "./"

    with patch("sys.stdin", io.StringIO("invalid_path\n\n")):
        assert test.ask_code_dir() == "./"


def test_top_module_exists():
    assert (
        test.top_module_exists("examples/vhdl_fifo_memory", "fifo_mem")
        == "examples/vhdl_fifo_memory/fifo.vhd"
    )
    assert (
        test.top_module_exists("examples/vhdl_fifo_memory", "memory_array")
        == "examples/vhdl_fifo_memory/fifo.vhd"
    )
    assert (
        test.top_module_exists("examples/vhdl_fifo_memory", "invalid") == None
    )
    assert test.top_module_exists("invalid", "") == None
    assert test.top_module_exists("invalid", "fifo_mem") == None
    # Verilog 2001
    assert (
        test.top_module_exists(
            "examples/verilog_unsigned_adder", "krnl_vadd_rtl_adder"
        )
        == "examples/verilog_unsigned_adder/unsigned_adder.v"
    )


def test_default_top_module():
    assert test.default_top_module("examples/vhdl_fifo_memory") == (
        "fifo_mem",
        "examples/vhdl_fifo_memory/fifo.vhd",
    )
    assert test.default_top_module("examples/verilog_unsigned_adder") == (
        "krnl_vadd_rtl_adder",
        "examples/verilog_unsigned_adder/unsigned_adder.v",
    )
    with pytest.raises(ValueError):
        test.default_top_module("invalid")


def test_ask_top_module():
    src_folder = "examples/vhdl_fifo_memory"
    module = "fifo_mem"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.ask_top_module(src_folder) == (
            module,
            test.top_module_exists(src_folder, module),
        )
    src_folder = "examples/verilog_unsigned_adder"
    module = "krnl_vadd_rtl_adder"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.ask_top_module(src_folder) == (
            module,
            test.top_module_exists(src_folder, module),
        )
    src_folder = "examples/verilog_unsigned_adder"
    module = "\n"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.ask_top_module(src_folder) == test.default_top_module(
            src_folder
        )
    src_folder = "examples/verilog_unsigned_adder"
    module = "invalid\n\n"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.ask_top_module(src_folder) == test.default_top_module(
            src_folder
        )


def test_ask_part():
    for answer in version_dependent.parts:
        with patch(
            "dovado.vivado_interaction.get_parts",
            lambda: version_dependent.parts,
        ):
            with patch(
                "dovado.vivado_interaction.get_parts",
                lambda: version_dependent.parts,
            ):
                with patch(
                    "sys.stdin", io.StringIO("wrong part\n?\n" + answer + "\n")
                ):
                    assert test.ask_part() == answer


def test_ask_stop_step():
    for answer in {"synthesis\n", "implementation\n", "\n"}:
        with patch(
            "sys.stdin", io.StringIO("wrong stop step\n" + answer),
        ):
            assert (
                test.ask_stop_step() == answer.strip()
                if answer != "\n"
                else test.ask_stop_step() == "synthesis"
            )


def test_ask_incremental_mode():
    for stop_step in {"synthesis", "implementation"}:
        for answers in {
            ("yes\n", "yes\n"),
            ("no\n", "no\n"),
            ("yes\n", "no\n"),
            ("no\n", "yes\n"),
            ("\n", "\n"),
        }:
            if stop_step == "synthesis":
                with patch(
                    "sys.stdin",
                    io.StringIO("wrong stop step\n" + answers[0] + ""),
                ):
                    assert test.ask_incremental_mode(stop_step) == {
                        "is synthesis incremental": True
                        if answers[0].strip() == "yes" or answers[0] == "\n"
                        else False,
                    }
            elif stop_step == "implementation":
                with patch(
                    "sys.stdin",
                    io.StringIO(
                        "wrong stop step\n" + answers[0] + answers[1] + ""
                    ),
                ):
                    assert test.ask_incremental_mode(stop_step) == {
                        "is synthesis incremental": True
                        if answers[0].strip() == "yes" or answers[0] == "\n"
                        else False,
                        "is implementation incremental": True
                        if answers[1].strip() == "yes" or answers[1] == "\n"
                        else False,
                    }


def test_parse_comma_separated_list():
    assert test.parse_comma_separated_list(
        "[1-9]|1[0-1]", "1, 2, 3, 4, 11"
    ) == (True, ["1", "2", "3", "4", "11"],)
    assert test.parse_comma_separated_list(
        "[1-9]|1[0-1]", "1, 2, 3, 4, 12"
    ) == (False, None,)


def test__ask_implementation_directives():
    for to_ask in {"place\n", "route\n"}:
        if to_ask == "place\n":
            patch_dir_par = (
                "dovado.doc_parsing.get_directives_paragraph",
                lambda x: version_dependent.place_directives_paragraph,
            )
            patch_dir = (
                "dovado.doc_parsing.get_directives",
                lambda x: version_dependent.place_directives,
            )
            patch_inc_dir = (
                "dovado.doc_parsing.get_incremental_directives",
                lambda x: version_dependent.incremental_place_directives,
            )
            directives = version_dependent.place_directives
            incremental_directives = (
                version_dependent.incremental_place_directives
            )
        if to_ask == "route\n":
            patch_dir_par = (
                "dovado.doc_parsing.get_directives_paragraph",
                lambda x: version_dependent.route_directives_paragraph,
            )
            patch_dir = (
                "dovado.doc_parsing.get_directives",
                lambda x: version_dependent.route_directives,
            )
            patch_inc_dir = (
                "dovado.doc_parsing.get_incremental_directives",
                lambda x: version_dependent.incremental_route_directives,
            )
            directives = version_dependent.route_directives
            incremental_directives = (
                version_dependent.incremental_route_directives
            )
        with patch(*patch_dir_par):
            with patch(*patch_dir):
                with patch(*patch_inc_dir):
                    for incremental_mode in [
                        {"is implementation incremental": True},
                        {"is implementation incremental": False},
                    ]:
                        for answer in (
                            incremental_directives
                            if incremental_mode[
                                "is implementation incremental"
                            ]
                            else directives
                        ):
                            with patch(
                                "sys.stdin", io.StringIO("?\n" + str(answer)),
                            ):
                                assert (
                                    test._ask_implementation_directives(
                                        to_ask.strip(), incremental_mode
                                    )
                                    == answer
                                )
    with pytest.raises(ValueError):
        test._ask_implementation_directives("invalid", "ignored")


@patch(
    "dovado.doc_parsing.get_directives_paragraph",
    lambda x: version_dependent.synth_directives_paragraph,
)
@patch(
    "dovado.doc_parsing.get_directives",
    lambda x: version_dependent.synth_directives,
)
@patch(
    "dovado.user_input._ask_implementation_directives", lambda x, y: "default",
)
def test_ask_directives():
    with patch("sys.stdin", io.StringIO("runtimeoptimized")):
        assert test.ask_directives("synthesis", {"ignored": "ignored"}) == (
            "runtimeoptimized",
            None,
            None,
        )
    with patch("sys.stdin", io.StringIO("invalid\n\n")):
        assert test.ask_directives("synthesis", {"ignored": "ignored"}) == (
            "default",
            None,
            None,
        )
    with patch("sys.stdin", io.StringIO("invalid\n?\n\n")):
        incremental_mode = {"is implementation incremental": True}
        assert test.ask_directives("implementation", incremental_mode) == (
            "default",
            test._ask_implementation_directives("place", incremental_mode),
            test._ask_implementation_directives("route", incremental_mode),
        )


def test_ask_clock():
    with patch("sys.stdin", io.StringIO("40.0\n\n")):
        assert test.ask_clock() == 250

    with patch("sys.stdin", io.StringIO("400\n")):
        assert test.ask_clock() == 400


def test_get_default_clock_identifier():
    assert test.get_default_clock_identifier(
        "./examples/vhdl_fifo_memory/fifo.vhd", "fifo_mem"
    ) == ["clk"]


def test_is_valid_clock():
    assert test.is_valid_clock(
        "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd",
        "rbs",
        "invalid port",
    ) == (None, None, None)

    assert set(("IN", "std_logic",)).issubset(
        set(
            test.is_valid_clock(
                "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd",
                "rbs",
                "binN",
            )
        )
    )
    assert test.is_valid_clock(
        "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd", "rbs", "diffN",
    ) == (None, "OUT", "std_logic_vector")


def test_is_valid_out():
    assert test.is_valid_out(
        "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd",
        "rbs",
        "invalid port",
    ) == (None, None, None)

    assert set(("OUT", "std_logic_vector",)).issubset(
        set(
            test.is_valid_out(
                "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd",
                "rbs",
                "diffN",
            )
        )
    )

    assert test.is_valid_out(
        "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd", "rbs", "binN",
    ) == (None, "IN", "std_logic")


def test_ask_identifiers():
    with patch("sys.stdin", io.StringIO("invalid\nbinN\ninvalid\ndiffN\n")):
        test_call = test.ask_identifiers(
            "./examples/vhdl_ripple_borrow_subtractor/rbs.vhd", "rbs"
        )
        assert (
            str(test_call[0].name) == "binN"
            and str(test_call[1].name) == "diffN"
        )
    with patch("sys.stdin", io.StringIO("invalid\naclk\ninvalid\nm_tdata\n")):
        test_call = test.ask_identifiers(
            "./examples/verilog_unsigned_adder/unsigned_adder.v",
            "krnl_vadd_rtl_adder",
        )
        assert (
            str(test_call[0].name) == "aclk"
            and str(test_call[1].name) == "m_tdata"
        )


def test_ask_utilization_metrics():
    with patch("sys.stdin", io.StringIO("1, 2, 3, 3, 1")):
        assert set(
            test.ask_utilization_metrics(
                version_dependent.available_utilization_metrics
            )
        ) == set(["Slice LUTs", "LUT as Logic", "LUT as Memory"])

    with patch("sys.stdin", io.StringIO("1, 12\n\n")):
        assert set(
            test.ask_utilization_metrics(
                version_dependent.available_utilization_metrics
            )
        ) == set(["Slice LUTs", "Slice Registers", "Block RAM Tile"])
