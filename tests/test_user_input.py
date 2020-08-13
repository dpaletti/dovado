import dovado.user_input as test
import io
import tests.vivado_2019_2_mock_data as version_dependent
from pathlib import Path
from unittest.mock import patch
import pytest


def test_request_code_dir():
    for dir in [x for x in Path("examples").iterdir() if x.is_dir()]:
        with patch("sys.stdin", io.StringIO(str(dir))):
            assert test.request_code_dir() == str(dir)

    with patch("sys.stdin", io.StringIO("\n")):
        assert test.request_code_dir() == "./"

    with patch("sys.stdin", io.StringIO("invalid_path\n\n")):
        assert test.request_code_dir() == "./"


def test_top_module_exists():
    assert test.top_module_exists("examples/vhdl_fifo_memory", "fifo_mem") == (
        True,
        "examples/vhdl_fifo_memory/fifo.vhd",
    )
    assert test.top_module_exists(
        "examples/vhdl_fifo_memory", "memory_array"
    ) == (True, "examples/vhdl_fifo_memory/fifo.vhd",)
    assert test.top_module_exists("examples/vhdl_fifo_memory", "invalid") == (
        False,
        None,
    )
    assert test.top_module_exists("invalid", "") == (False, None)
    assert test.top_module_exists("invalid", "fifo_mem") == (False, None)
    # Verilog 2001
    assert test.top_module_exists(
        "examples/verilog_unsigned_adder", "krnl_vadd_rtl_adder"
    ) == (True, "examples/verilog_unsigned_adder/unsigned_adder.v",)


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


def test_request_top_module():
    src_folder = "examples/vhdl_fifo_memory"
    module = "fifo_mem"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.request_top_module(src_folder) == (
            module,
            test.top_module_exists(src_folder, module)[1],
        )
    src_folder = "examples/verilog_unsigned_adder"
    module = "krnl_vadd_rtl_adder"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.request_top_module(src_folder) == (
            module,
            test.top_module_exists(src_folder, module)[1],
        )
    src_folder = "examples/verilog_unsigned_adder"
    module = "\n"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.request_top_module(src_folder) == test.default_top_module(
            src_folder
        )
    src_folder = "examples/verilog_unsigned_adder"
    module = "invalid\n\n"
    with patch("sys.stdin", io.StringIO(module)):
        assert test.request_top_module(src_folder) == test.default_top_module(
            src_folder
        )


def test_request_part():
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
                    assert test.request_part() == answer


def test_request_stop_step():
    for answer in {"synthesis\n", "implementation\n", "\n"}:
        with patch(
            "sys.stdin", io.StringIO("wrong stop step\n" + answer),
        ):
            assert (
                test.request_stop_step() == answer.strip()
                if answer != "\n"
                else test.request_stop_step() == "synthesis"
            )


def test_request_incremental_mode():
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
                    assert test.request_incremental_mode(stop_step) == {
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
                    assert test.request_incremental_mode(stop_step) == {
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


def test__request_implementation_directives():
    for to_request in {"place\n", "route\n"}:
        if to_request == "place\n":
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
        if to_request == "route\n":
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
                                    test._request_implementation_directives(
                                        to_request.strip(), incremental_mode
                                    )
                                    == answer
                                )
    with pytest.raises(ValueError):
        test._request_implementation_directives("invalid", "ignored")


@patch(
    "dovado.doc_parsing.get_directives_paragraph",
    lambda x: version_dependent.synth_directives_paragraph,
)
@patch(
    "dovado.doc_parsing.get_directives",
    lambda x: version_dependent.synth_directives,
)
@patch(
    "dovado.user_input._request_implementation_directives",
    lambda x, y: "default",
)
def test_request_directives():
    with patch("sys.stdin", io.StringIO("runtimeoptimized")):
        assert test.request_directives(
            "synthesis", {"ignored": "ignored"}
        ) == ("runtimeoptimized", None, None)
    with patch("sys.stdin", io.StringIO("invalid\n\n")):
        assert test.request_directives(
            "synthesis", {"ignored": "ignored"}
        ) == ("default", None, None)
    with patch("sys.stdin", io.StringIO("invalid\n?\n\n")):
        incremental_mode = {"is implementation incremental": True}
        assert test.request_directives("implementation", incremental_mode) == (
            "default",
            test._request_implementation_directives("place", incremental_mode),
            test._request_implementation_directives("route", incremental_mode),
        )


def test_request_clock():
    with patch("sys.stdin", io.StringIO("40.0\n\n")):
        assert test.request_clock() == 250

    with patch("sys.stdin", io.StringIO("400\n")):
        assert test.request_clock() == 400


def test_request_utilization_metrics():
    with patch("sys.stdin", io.StringIO("1, 2, 3, 3, 1")):
        assert set(
            test.request_utilization_metrics(
                version_dependent.available_utilization_metrics
            )
        ) == set(["Slice LUTs", "LUT as Logic", "LUT as Memory"])

    with patch("sys.stdin", io.StringIO("1, 12\n\n")):
        assert set(
            test.request_utilization_metrics(
                version_dependent.available_utilization_metrics
            )
        ) == set(["Slice LUTs", "Slice Registers", "Block RAM Tile"])
