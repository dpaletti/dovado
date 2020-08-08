import dovado.user_input as u
import io
import tests.vivado_2019_2_mock_data as version_dependent
import dovado.doc_parsing as doc
from pathlib import Path
import random

# TODO further generalise tests
vhdl_src_folder = "examples/vhdl_fifo_memory"
verilog_src_folder = "examples/verilog_fifo_memory"
verilog_module = "memory_array"
vhdl_module = "memory_array"
verilog_default_module = "fifo_mem"
vhdl_default_module = "fifo_mem"
chosen_module = "status_signal"


def test_request_code_dir(monkeypatch):
    with monkeypatch.context() as m:
        for dir in [x for x in Path("examples").iterdir() if x.is_dir()]:
            m.setattr(
                "sys.stdin", io.StringIO(str(dir)),
            )
            assert u.request_code_dir() == str(dir)


def test_top_module_exists_vhdl():
    src_folder = vhdl_src_folder
    module = vhdl_module

    assert u.top_module_exists(src_folder, module) == True


def test_top_module_exists_verilog():
    src_folder = verilog_src_folder
    module = verilog_module

    assert u.top_module_exists(src_folder, module) == True


def test_default_top_module_vhdl():
    src_folder = vhdl_src_folder
    assert u.default_top_module(src_folder) == vhdl_default_module


def test_default_top_module_verilog():
    src_folder = verilog_src_folder
    assert u.default_top_module(src_folder) == verilog_default_module


def test_request_top_module_default(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(
            "sys.stdin", io.StringIO("wrong module\n\n"),
        )
        out = u.request_top_module(vhdl_src_folder)
        assert out == vhdl_default_module


def test_request_top_module(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(
            "sys.stdin", io.StringIO("wrong module\n" + chosen_module + "\n"),
        )
        out = u.request_top_module(vhdl_src_folder)
        assert out == chosen_module


def test_request_part(monkeypatch):
    for answer in version_dependent.parts:
        with monkeypatch.context() as m:
            m.setattr(
                "dovado.vivado_interaction.get_parts",
                lambda: version_dependent.parts,
            ),
            m.setattr(
                "sys.stdin", io.StringIO("wrong part\n?\n" + answer + "\n"),
            )
            assert u.request_part() == answer


def test_request_stop_step(monkeypatch):
    with monkeypatch.context() as m:
        for answer in {"synthesis\n", "implementation\n", "\n"}:
            m.setattr(
                "sys.stdin", io.StringIO("wrong stop step\n" + answer),
            )
            assert (
                u.request_stop_step() == answer.strip()
                if answer != "\n"
                else u.request_stop_step() == "synthesis"
            )


def test_request_incremental_mode(monkeypatch):
    with monkeypatch.context() as m:
        for stop_step in {"synthesis", "incremental"}:
            for answers in {
                ("yes\n", "yes\n"),
                ("no\n", "no\n"),
                ("yes\n", "no\n"),
                ("no\n", "yes\n"),
                ("\n", "\n"),
            }:
                if stop_step == "synthesis":
                    m.setattr(
                        "sys.stdin",
                        io.StringIO("wrong stop step\n" + answers[0] + ""),
                    )
                    assert u.request_incremental_mode(stop_step) == {
                        "is synthesis incremental": True
                        if answers[0].strip() == "yes" or answers[0] == "\n"
                        else False,
                    }
                elif stop_step == "implementation":
                    m.setattr(
                        "sys.stdin",
                        io.StringIO(
                            "wrong stop step\n" + answers[0] + answers[1] + ""
                        ),
                    )
                    assert u.request_incremental_mode(stop_step) == {
                        "is synthesis incremental": True
                        if answers[0].strip() == "yes" or answers[0] == "\n"
                        else False,
                        "is implementation incremental": True
                        if answers[1].strip() == "yes" or answers[1] == "\n"
                        else False,
                    }


def test_parse_comma_separated_list():
    assert u.parse_comma_separated_list("[1-9]|1[0-1]", "1, 2, 3, 4, 11") == (
        True,
        ["1", "2", "3", "4", "11"],
    )
    assert u.parse_comma_separated_list("[1-9]|1[0-1]", "1, 2, 3, 4, 12") == (
        False,
        None,
    )


def test__request_implementation_directives(monkeypatch):
    to_request = random.choice(["place\n", "route\n"])
    print("TO_REQUEST: " + to_request)
    with monkeypatch.context() as m:
        if to_request == "place\n":
            m.setattr(
                "dovado.doc_parsing.get_directives_paragraph",
                lambda x: version_dependent.place_directives_paragraph,
            )
            m.setattr(
                "dovado.doc_parsing.get_directives",
                lambda x: version_dependent.place_directives,
            )
            m.setattr(
                "dovado.doc_parsing.get_incremental_directives",
                lambda x: version_dependent.incremental_place_directives,
            )
            directives = version_dependent.place_directives
        if to_request == "route\n":
            m.setattr(
                "dovado.doc_parsing.get_directives_paragraph",
                lambda x: version_dependent.route_directives_paragraph,
            )
            m.setattr(
                "dovado.doc_parsing.get_directives",
                lambda x: version_dependent.route_directives,
            )
            m.setattr(
                "dovado.doc_parsing.get_incremental_directives",
                lambda x: version_dependent.incremental_route_directives,
            )
            directives = version_dependent.route_directives
        incremental_mode = random.choice(
            [
                {"is implementation incremental": True},
                {"is implementation incremental": False},
            ]
        )
        answer = random.choice(directives)
        print("INCREMENTAL_MODE: " + str(incremental_mode))
        print("ANSWER: " + str(answer))
        m.setattr(
            "sys.stdin", io.StringIO(answer),
        )
        assert (
            u._request_implementation_directives(
                to_request.strip(), incremental_mode
            )
            == answer
        )


# TODO request directives and above tests extension and generalisation
