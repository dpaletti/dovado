import dovado.verilog_parsing as test
from pathlib import Path


def test_list_files():
    for dir in [x for x in Path("examples").iterdir()]:
        test_out = test.list_files(dir)
        if dir.is_dir():
            for file in [x for x in dir.iterdir()]:
                assert file in test_out if file.suffix == "v" else True
    assert test.list_files("") == []


def test_list_modules():
    assert test.list_modules(
        Path("./examples/verilog_unsigned_adder/unsigned_adder.v").read_text()
    ) == ["krnl_vadd_rtl_adder"]
    assert test.list_modules(b"") == []


def test_strip_comments():
    assert (
        test.strip_comments(
            "///*block comment inside line comment*/\n/********\n****/"
        )
        == ""
    )
