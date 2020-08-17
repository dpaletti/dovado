import re
from pathvalidate import is_valid_filepath
from os import path
from pathlib import Path
import dovado.vivado_interaction as vivado
import dovado.doc_parsing as doc
import dovado.src_parsing as parsing


def list_rtl_files(src_path):
    rtl_extensions = ["vhd", "v", "sv"]
    files = []
    for extension in rtl_extensions:
        files += [
            str(pth) for pth in src_path.rglob("*." + extension) if pth.is_file
        ]
    return set(files)


def ask_code_dir():
    while True:
        default = "./"
        user_input = input(
            "Enter path to code folder" + " [default = " + "./" + "]: "
        )
        if (
            is_valid_filepath(user_input)
            and path.exists(user_input)
            and path.isdir(user_input)
            and (list_rtl_files(Path(user_input)))
        ) or user_input == "":
            return default if user_input == "" else user_input

        print("Invalid path, ensure there are no typos\n")


def top_module_exists(src_folder, module):

    for src in list_rtl_files(Path(src_folder)):
        if module in parsing.get_modules(Path(src)):
            return src
    return None


def default_top_module(src_folder):
    for src in list_rtl_files(Path(src_folder)):
        modules = parsing.get_modules(Path(src))
        if modules:
            return modules[0], src
    print("No module found in the given source files")
    raise ValueError(
        "No module found in "
        + str(src_folder)
        + " at default_top_module(src_folder)"
    )


def ask_top_module(src_folder):
    default, def_src = default_top_module(src_folder)
    while True:
        user_input = input(
            "Enter top module identifier [default = " + default + "]: "
        )
        mod_src = top_module_exists(src_folder, user_input)
        if mod_src or user_input == "":
            return (
                (default, def_src)
                if user_input == ""
                else (user_input, mod_src)
            )
        print("Module does not exist among the files in the code folder\n")


def ask_part():
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


def ask_stop_step():
    default = "synthesis"
    while True:
        user_input = input(
            "Would you like to get utilization and frequency after logical"
            + " synthesis or after implementation?"
            + "(allowed answers = synthesis/implementation)"
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


def ask_incremental_mode(stop_step):
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


def _ask_implementation_directives(to_request, incremental_mode):
    if to_request not in {"place", "route"}:
        raise ValueError(
            "_request_incremental_directives called with " + to_request
        )

    default = "Default"
    directives_paragraph = doc.get_directives_paragraph(to_request)
    directives = doc.get_directives(directives_paragraph)
    incremental_directives = doc.get_directives(
        doc.get_directives_paragraph("read checkpoint")
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
                    + " with read_checkpoint thus: "
                    + str(incremental_directives)
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


def ask_directives(stop_step, incremental_mode):
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
            _ask_implementation_directives("place", incremental_mode),
            _ask_implementation_directives("route", incremental_mode),
        )


def ask_clock():
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
    return [
        i
        for i in [
            parsing.get_port_id(j)
            for j in parsing.get_ports(Path(src), module)
        ]
        if re.match(".*(clk|clock),*", i)
    ]


def is_valid_clock(src, module, identifier):
    port = parsing.get_port_from_id(
        identifier, parsing.get_ports(Path(src), module)
    )
    if not port:
        return None, None, None
    port_direction = parsing.get_port_direction(port)
    port_type = parsing.get_port_type(port)
    if (
        port_direction == "IN" and port_type == "std_logic"
        if Path(src).suffix == ".vhd"
        else port_type == "wire"
    ):
        return (
            port,
            port_direction,
            port_type,
        )
    return None, port_direction, port_type


def ask_identifiers(src, module):
    while True:
        user_input = input("Enter clock identifier: ")
        clock, clock_direction, clock_port_type = is_valid_clock(
            src, module, user_input
        )
        if clock:
            return clock
        print(
            "Invalid clock identifier: port direction = "
            + str(clock_direction)
            + " (must be an input port) port type = "
            + str(clock_port_type)
            + " (must be binary)\n"
        )


def parse_comma_separated_list(regexp_element, to_parse):
    return (
        None
        if not re.fullmatch(
            "^("
            + regexp_element
            + ")"
            + "(([ \t]*,[ \t]*)("
            + regexp_element
            + "))*$",
            to_parse,
        )
        else [i for i in re.sub(r"[ \t]*", "", to_parse).split(",")]
    )


def ask_utilization_metrics(available_metrics):
    util_indices = dict(
        zip(range(1, len(available_metrics) + 1), iter(available_metrics))
    )

    info_prompt = "Percentage Utilisation indices available:\n"
    for (k, v) in util_indices.items():
        info_prompt += "(" + str(k) + ") " + v + "\n"

    print(info_prompt)
    default = "1, 4, 9"
    while True:
        user_input = input(
            "Enter a comma-separated list of percentage "
            + "utilisation indices [default = "
            + default
            + "]: "
        )
        if user_input == "":
            user_input = default
        parsed_list = parse_comma_separated_list("[1-9]|1[0-2]", user_input)
        if parsed_list:
            return [util_indices[int(i)] for i in set(parsed_list)]

        print(
            "Invalid input, please enter"
            + " a comma separated list of numbers between 1 and 12"
        )
