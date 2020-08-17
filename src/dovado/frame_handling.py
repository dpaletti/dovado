import re
from pathlib import Path
import dovado.src_parsing as parsing


def fill(frame_path, replacements, placeholder, out_path):
    out = re.sub(
        placeholder,
        lambda m, r=iter(replacements): next(r),
        Path(frame_path).open("r").read(),
    )
    Path(out_path).write_text(out)


def fill_box(
    frame_path, top_src, top_module, clock_port, placeholder, out_path,
):
    top_suffix = Path(top_src).suffix
    frame_suffix = Path(frame_path).suffix
    if top_suffix != frame_suffix:
        raise ValueError(
            "Source and Frame must have same extension "
            + " Source suffix: "
            + top_suffix
            + " Frame suffix: "
            + frame_suffix
        )
    if top_suffix == ".vhd":
        _vhdl_fill_box(
            frame_path, top_src, top_module, clock_port, placeholder, out_path,
        )
    elif top_suffix == ".sv" or top_suffix == ".v":
        _verilog_fill_box(
            frame_path, top_src, top_module, clock_port, placeholder, out_path,
        )
    else:
        raise ValueError(
            "Suffix of both Source and Frame is invalid: " + top_suffix
        )


def _vhdl_fill_box(
    frame_path, top_src, top_module, clock_port, placeholder, out_path,
):
    libraries, imports = parsing.get_imports(Path(top_src))
    input_mapping = [
        parsing.get_port_id(port)
        + (
            " => '1',\n"
            if parsing.get_port_type(port) == "std_logic"
            else " => " + parsing.get_port_type(port) + "'((others => '1')),\n"
        )
        for port in parsing.get_ports(Path(top_src), top_module)
        if (
            parsing.get_port_direction(port) == "IN"
            and parsing.get_port_id(port) != parsing.get_port_id(clock_port)
        )
    ]
    input_mapping[len(input_mapping) - 1] = input_mapping[
        len(input_mapping) - 1
    ].replace(",", "")
    replacements = [
        "".join(
            ["library " + lib + ";\n" for lib in libraries]
            + ["use " + imp + ";\n" for imp in imports]
        ),
        "Work." + top_module,
        parsing.get_port_id(clock_port),
        "".join(input_mapping),
    ]
    fill(frame_path, replacements, placeholder, out_path)


def _verilog_fill_box(
    frame_path, top_src, top_module, clock_port, placeholder, out_path,
):
    input_mapping = [
        parsing.get_port_id(port) + " ('1),\n"
        for port in parsing.get_ports(Path(top_src), top_module)
        if (
            parsing.get_port_direction(port) == "IN"
            and parsing.get_port_id(port) != parsing.get_port_id(clock_port)
        )
    ]

    input_mapping[len(input_mapping) - 1] = input_mapping[
        len(input_mapping) - 1
    ].replace(",", "")

    replacements = [
        top_module,
        parsing.get_port_id(clock_port),
        "".join(input_mapping),
    ]

    fill(frame_path, replacements, placeholder, out_path)
