import re
from pathlib import Path
import dovado_rtl.src_parsing as parsing
from dovado_rtl.config import get_config


def fill(frame_path, replacements, placeholder, out_path):
    out = re.sub(
        placeholder,
        lambda m, r=iter(replacements): next(r),
        Path(frame_path).open("r").read(),
    )
    Path(out_path).write_text(out)


def fill_tcl(
    src_folder,
    top_src,
    top_module,
    is_boxed,
    synthesis_part,
    synthesis_directive,
    incremental_mode,
    stop_step,
    top_lang,
    target_clock,
    place_directive="",
    route_directive="",
):
    print("TOP LANG: " + str(top_lang))
    SYNTHESIS_REPLACEMENTS = [
        get_config("VIVADO_OUTPUT_DIR"),
        src_folder,
        get_config("XDC_DIR") + get_config("CONSTRAINT"),
        (
            "read_vhdl -library bftLib "
            + get_config("VHDL_DIR")
            + get_config("VHDL_BOX")
        )
        if top_lang is parsing.RTL.VHDL
        else (
            "read_verilog "
            + get_config("VERILOG_DIR")
            + get_config("VERILOG_BOX")
        ),
        ("set_property IS_ENABLED 0 [get_files " + top_src + "]")
        if top_lang is parsing.RTL.VHDL
        else "# no disabling needed",
        top_module if not is_boxed else "box",
        synthesis_part,
        synthesis_directive,
        "-incremental_synth" if incremental_mode.synthesis else "",
    ]
    print("SYNTHESIS REPLACEMENTS: " + str(SYNTHESIS_REPLACEMENTS))

    IMPLEMENTATION_REPLACEMENTS = (
        []
        if stop_step is parsing.StopStep.SYNTHESIS
        else (
            [
                "",
                "-directive " + place_directive,
                "",
                "-directive " + route_directive,
            ]
            if not incremental_mode.implementation
            else [
                "-directive " + place_directive,
                " ",
                "-directive " + route_directive,
                " ",
            ]
        )
    )

    REPLACEMENT = (
        SYNTHESIS_REPLACEMENTS
        if stop_step is parsing.StopStep.SYNTHESIS
        else SYNTHESIS_REPLACEMENTS[:3]
        + [
            (
                "read_vhdl -library bftLib "
                + get_config("VHDL_DIR")
                + get_config("VHDL_BOX")
            )
            if top_lang is parsing.RTL.VHDL
            else (
                "read_verilog "
                + get_config("VERILOG_DIR")
                + get_config("VERILOG_BOX")
            )
        ]
        + SYNTHESIS_REPLACEMENTS[5:]
        + IMPLEMENTATION_REPLACEMENTS
    )

    print("REPLACEMENTS: " + str(REPLACEMENT))
    fill(
        get_config("TCL_DIR") + get_config(stop_step.name + "_FRAME"),
        REPLACEMENT
        + [
            get_config(stop_step.name + "_TIMING"),
            get_config(stop_step.name + "_UTILISATION"),
        ],
        get_config("PLACEHOLDER"),
        get_config("TCL_DIR") + get_config(stop_step.name),
    )


def fill_box(
    frame_path,
    top_src,
    top_module,
    parameters,
    clock_port,
    placeholder,
    out_path,
):
    full_parameters = []
    for param in parameters:
        full_parameters.append(
            parsing.get_parameter_on_name(Path(top_src), top_module, param)
        )

    top_suffix = Path(top_src).suffix
    if top_suffix == ".vhd":
        _vhdl_fill_box(
            frame_path,
            top_src,
            top_module,
            full_parameters,
            clock_port,
            placeholder,
            out_path,
        )
    elif top_suffix == ".sv" or top_suffix == ".v":
        _verilog_fill_box(
            frame_path,
            top_src,
            top_module,
            full_parameters,
            clock_port,
            placeholder,
            out_path,
        )
    else:
        raise ValueError(
            "Suffix of both Source and Frame is invalid: " + top_suffix
        )


def _vhdl_parameter_map(parameters):
    parameter_section = "generic map(\n"
    for parameter in parameters[:-1]:
        if not parameter.value:
            raise Exception(
                "Please provide default values for all parameters, "
                + str(parameter.name)
                + " does not have one."
            )
        try:
            parameter_section += (
                parameter.name
                + " => "
                + (
                    str(parameter.value)
                    if not parameter.value.base
                    else str(
                        int(parameter.value.val[1:], parameter.value.base,)
                    )
                ).strip()
                + ",\n"
            )
        except Exception:
            print("Skipping unsupported parameter: " + str(parameter))
            continue
    try:
        parameter_section += (
            parameters[-1].name
            + " => "
            + (
                str(parameters[-1].value)
                if not parameters[-1].value.base
                else str(
                    int(
                        parameters[-1].value.val[1:],
                        parameters[-1].value.base,
                    )
                )
            )
            + ")"
        )
    except Exception:
        print("Skipping unsupported parameter: " + str(parameter))
        parameter_section += ")"
    return parameter_section


def _vhdl_fill_box(
    frame_path,
    top_src,
    top_module,
    parameters,
    clock_port,
    placeholder,
    out_path,
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
        _vhdl_parameter_map(parameters),
        parsing.get_port_id(clock_port),
        "".join(input_mapping),
    ]
    fill(frame_path, replacements, placeholder, out_path)


def _verilog_parameter_map(parameters):
    parameter_section = "#(\n"
    for parameter in parameters[:-1]:
        parameter_section += (
            "."
            + parameter.name
            + "("
            + str(int(str(parameter.value.val), parameter.value.base))
            + "),\n"
        )
    parameter_section += (
        "."
        + parameters[-1].name
        + "("
        + str(int(str(parameters[-1].value.val), parameters[-1].value.base,))
        + ")\n)\n"
    )
    return parameter_section


def _verilog_fill_box(
    frame_path,
    top_src,
    top_module,
    parameters,
    clock_port,
    placeholder,
    out_path,
):
    input_mapping = [
        "." + parsing.get_port_id(port) + " ('1),\n"
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
        _verilog_parameter_map(parameters),
        parsing.get_port_id(clock_port),
        "".join(input_mapping),
    ]

    fill(frame_path, replacements, placeholder, out_path)


def setup_incremental(is_incremental: parsing.IsIncremental):
    if not is_incremental.synthesis and not is_incremental.implementation:
        return
    if is_incremental.synthesis:
        path = get_config("TCL_DIR") + get_config("SYNTHESIS")
        synthesis = Path(path).read_text()
        synthesis = synthesis.replace("#! ", "")
        Path(path).write_text(synthesis)
    if is_incremental.implementation:
        path = get_config("TCL_DIR") + get_config("IMPLEMENTATION")
        implementation = Path(path).read_text()
        implementation = implementation.replace("#! ", "")
        Path(path).write_text(implementation)
