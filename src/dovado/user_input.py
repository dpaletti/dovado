import re
from pathvalidate import is_valid_filepath
from os import path
from pathlib import Path
import dovado.vhdl_parsing as vhdl
import dovado.verilog_parsing as verilog
import dovado.vivado_interaction as vivado
import dovado.doc_parsing as doc


def request_code_dir():
    while True:
        default = "./"
        user_input = input(
            "Enter path to code folder" + " [default = " + "./" + "]: "
        )
        print("User input: " + user_input)
        if (
            is_valid_filepath(user_input)
            and path.exists(user_input)
            and path.isdir(user_input)
            and (
                vhdl.list_files(Path(user_input))
                or verilog.list_files(Path(user_input))
            )
        ) or user_input == "":
            return default if user_input == "" else user_input

        print("Invalid path, ensure there are no typos\n")


def top_module_exists(src_folder, module):

    for src in vhdl.list_files(Path(src_folder)):
        if module in vhdl.list_modules(Path(src).read_text()):
            return True, src

    for src in verilog.list_files(Path(src_folder)):
        if module in verilog.list_modules(Path(src).read_text()):
            return True, src
    return False, None


def default_top_module(src_folder):
    for src in vhdl.list_files(Path(src_folder)):
        modules = vhdl.list_modules(Path(src).read_text())
        if modules:
            return modules[0], src
    for src in verilog.list_files(Path(src_folder)):
        modules = verilog.list_modules(Path(src).read_text())
        if modules:
            return modules[0], src
    print("No module found in the given source files")
    raise ValueError(
        "No module found in "
        + str(src_folder)
        + " at default_top_module(src_folder)"
    )


def request_top_module(src_folder):
    default, def_src = default_top_module(src_folder)
    while True:
        user_input = input(
            "Enter top module identifier [default = " + default + "]: "
        )
        exists, mod_src = top_module_exists(src_folder, user_input)
        if exists or user_input == "":
            return (
                (default, def_src)
                if user_input == ""
                else (user_input, mod_src)
            )
        print("Module does not exist among the files in the code folder\n")


def request_part():
    parts = vivado.get_parts()
    default = parts[0]
    while True:
        user_input = input(
            "Enter part (input ? to have a list of available parts)"
            + "[default = "
            + default
            + "]: "
        )
        if user_input in parts or user_input == "":
            return default if user_input == "" else user_input
        if user_input == "?":
            print("Available parts\n" + str(parts))
            continue
        print("Part not available.")


def request_stop_step():
    default = "synthesis"
    while True:
        user_input = input(
            "Would you like to get utilization and frequency after logical"
            + " synthesis or after place and route?"
            + "(allowed answers = synthesis/place and route)"
            + "[default = "
            + default
            + "]: "
        )
        if (
            user_input == "synthesis"
            or user_input == "implementation"
            or user_input == ""
        ):
            return default if user_input == "" else user_input


def request_incremental_mode(stop_step):
    default = "yes"
    default_second = "yes"
    while True:
        user_input = input(
            "Do you want to run synthesis in incremental mode?"
            + "(options = yes/no) [default = yes]: "
        )
        if user_input == "yes" or user_input == "no" or user_input == "":
            user_input = default if user_input == "" else user_input
            break
    if stop_step == "synthesis":
        return {
            "is synthesis incremental": True if user_input == "yes" else False,
        }
    while True:
        user_second_input = input(
            "Do you want to run implementation in incremental mode?"
            + "(options = yes/no) [default = yes]:"
        )
        if (
            user_second_input == "yes"
            or user_second_input == "no"
            or user_second_input == ""
        ):
            user_second_input = (
                default_second
                if user_second_input == ""
                else user_second_input
            )
            return {
                "is synthesis incremental": True
                if user_input == "yes"
                else False,
                "is implementation incremental": True
                if user_second_input == "yes"
                else False,
            }


def parse_comma_separated_list(regexp_element, to_parse):
    return (
        (False, None)
        if not re.fullmatch(
            "^("
            + regexp_element
            + ")"
            + "(([ \t]*,[ \t]*)("
            + regexp_element
            + "))*$",
            to_parse,
        )
        else (True, [i for i in re.sub(r"[ \t]*", "", to_parse).split(",")],)
    )


def _request_implementation_directives(to_request, incremental_mode):
    if to_request not in {"place", "route"}:
        raise ValueError(
            "_request_incremental_directives called with " + to_request
        )

    default = "Default"
    directives_paragraph = doc.get_directives_paragraph(to_request)
    directives = doc.get_directives(directives_paragraph)
    incremental_directives = doc.get_incremental_directives(
        directives_paragraph
    )
    while True:
        user_input = input(
            "What directive do you want to give to the "
            + to_request
            + ' step? Input"?"'
            + " to get help on available directives."
            + " [default = "
            + default
            + "]: "
        )
        if user_input == "?":
            if incremental_mode["is implementation incremental"]:
                print(
                    "Available directives are only the ones compatible"
                    + " with incremental mode thus: "
                    + str(incremental_directives)
                    + "\n here a recap of all the available directives "
                    + directives_paragraph
                )
            else:
                print("Available directives: " + directives_paragraph)
            continue
        if (
            user_input
            in (
                incremental_directives
                if incremental_mode["is implementation incremental"]
                else directives
            )
            or user_input == ""
        ):
            return default if user_input == "" else user_input


def request_directives(stop_step, incremental_mode):
    synth_directives_paragraph = doc.get_directives_paragraph("synthesis")
    synth_directives = doc.get_directives(synth_directives_paragraph)
    or_directives = ""
    default = "default"
    for i in synth_directives:
        or_directives += i + "|"
    or_directives = or_directives[: len(or_directives) - 1]
    while True:
        user_input = input(
            "What directives do you want to give to the"
            + ' synthesis step? Input "?" to get help on'
            + " available directives."
            + " [default = "
            + default
            + "]: "
        )
        if user_input == "?":
            print(synth_directives_paragraph)
            continue
        if user_input == "":
            user_input = default
        if user_input in synth_directives:
            input_synth_directives = user_input
            break
    if stop_step == "synthesis":
        return input_synth_directives, None, None
    else:
        return (
            input_synth_directives,
            _request_implementation_directives("place", incremental_mode),
            _request_implementation_directives("route", incremental_mode),
        )


def request_clock():
    default = "250"
    while True:
        user_input = input(
            "Input target clock as an integer value (in Mhz) [default: "
            + default
            + "]: "
        )
        if user_input == "":
            user_input = default
        try:
            return int(user_input)
        except ValueError:
            print("Invalid, input\n")
            continue


def get_default_clock_identifier(src, module):
    print("Suffix: " + Path(src).suffix)
    if Path(src).suffix == ".vhd":
        declarations = vhdl.list_declarations(
            vhdl.get_entity(Path(src).read_text(), module)
        )
    elif Path(src).suffix == ".v":
        declarations = verilog.list_declarations(
            verilog.get_module(Path(src).read_text(), module)
        )
    else:
        raise ValueError(
            "Source file: "
            + str(src)
            + " passed to get_default_clock_identifier "
            + " has unknown extension "
            + " allowed extensions are .vhd and .v"
        )
    return [i for i in declarations if re.match(".*(clk|clock),*", i)]


def is_valid_clock(src, module, identifier):
    if Path(src).suffix == ".vhd":
        declaration = vhdl.declaration_exists(
            vhdl.list_declarations(vhdl.get_entity(src, module)), identifier
        )
        if not declaration:
            return None, None, None
        direction = vhdl.get_direction(declaration)
        port_type = vhdl.get_type(declaration)
        if direction == "in" and port_type == "std_logic":
            return (
                vhdl.sub_declaration_identifier(declaration, identifier),
                direction,
                port_type,
            )
        return None, direction, port_type
    if Path(src).suffix == ".v":
        declaration = verilog.declaration_exists(
            verilog.list_declarations(
                verilog.get_module(Path(src).read_text(), module)
            ),
            identifier,
        )
        if not declaration:
            return None
        direction = verilog.get_direction(declaration)
        port_type = verilog.get_type(declaration)
        if direction == "input" and port_type == "wire":
            return (
                verilog.sub_declaration_identifier(declaration, identifier),
                direction,
                port_type,
            )
        return None, direction, port_type


def is_valid_out(src, module, identifier):
    if Path(src).suffix == ".vhd":
        declaration = vhdl.declaration_exists(
            vhdl.list_declarations(
                vhdl.get_entity(Path(src).read_text(), module), identifier
            )
        )
        if not declaration:
            return None, None, None
        direction = vhdl.get_direction(declaration)
        port_type = vhdl.get_type(declaration)
        if direction == "out":
            return declaration, direction, port_type
        return None, direction, port_type
    if Path(src).suffix == ".v":
        declaration = verilog.declaration_exists(
            verilog.list_declarations(
                verilog.get_module(Path(src).read_text(), module)
            ),
            identifier,
        )
        if not declaration:
            return None
        direction = verilog.get_direction(declaration)
        port_type = verilog.get_type(declaration)
        if direction == "output":
            return declaration, direction, port_type
        return None, direction, port_type


def request_identifiers(src, module):
    while True:
        user_input = input("Enter clock identifier: ")
        clock, clock_direction, clock_port_type = is_valid_clock(
            src, module, user_input
        )
        if clock:
            break
        print(
            "Invalid clock identifier: port direction = "
            + clock_direction
            + " (must be an input port) port type = "
            + clock_port_type
            + " (must be binary)\n"
        )
    while True:
        user_input = input("Enter out port identifier: ")
        out, out_direction, out_port_type = is_valid_out(
            src, module, user_input
        )
        if out:
            return clock, out
        print(
            "Invalid out port identifier: port direction = "
            + out_direction
            + " (must be an output port)"
        )


def request_utilization_metrics(available_metrics):
    util_indices = dict(
        zip(range(1, len(available_metrics) + 1), iter(available_metrics))
    )

    info_prompt = "Percentage Utilisation indices available:\n"
    for (k, v) in util_indices.items():
        info_prompt += "(" + str(k) + ") " + v + "\n"

    print("Percentage Utilisation indices available:\n" + info_prompt)
    default = "1, 4, 9"
    while True:
        user_input = input(
            "Enter a comma-separated list of percentage "
            + "utilisation indices [default = +"
            + default
            + "]: "
        )
        if user_input == "":
            user_input = default
        is_compliant, parsed_list = parse_comma_separated_list(
            "[1-9]|1[0-1]", user_input
        )
        if is_compliant:
            return [util_indices[int(i)] for i in set(parsed_list)]

        print(
            "Invalid input, please enter a comma separated list of numbers between 1 and 11"
        )
