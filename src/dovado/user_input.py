import re
from pathvalidate import is_valid_filepath
from os import path
import dovado.vhdl_parsing as vhdl
import dovado.verilog_parsing as verilog
import dovado.vivado_interaction as vivado
import dovado.report_parsing as report
import dovado.doc_parsing as doc


def request_code_dir():
    while True:
        default = "./"
        user_input = input(
            "Enter path to code folder" + " [default = " + "./" + "]: "
        )
        try:
            if (
                is_valid_filepath(user_input)
                and path.exists(user_input)
                and (
                    vhdl.list_files(user_input)
                    or verilog.list_files(user_input)
                )
            ) or user_input == "":
                return default if user_input == "" else user_input

            print("Invalid path, ensure there are no typos\n")

        except NotADirectoryError:
            print("Not a directory, do not input a file")
            continue


def top_module_exists(src_folder, module):

    for src in vhdl.list_files(src_folder):
        if module in vhdl.list_modules(src):
            return True

    for src in verilog.list_files(src_folder):
        if module in verilog.list_modules(src):
            return True
    return False


def default_top_module(src_folder):
    for src in vhdl.list_files(src_folder):
        modules = vhdl.list_modules(src)
        if modules:
            return modules[0]
    for src in verilog.list_files(src_folder):
        modules = verilog.list_modules(src)
        if modules:
            return modules[0]
    print("No module found in the given source files")
    raise ValueError(
        "No module found in "
        + str(src_folder)
        + " at default_top_module(src_folder)"
    )


def request_top_module(src_folder):
    default = default_top_module(src_folder)
    while True:
        user_input = input(
            "Enter top module identifier [default = " + default + "]: "
        )
        if top_module_exists(src_folder, user_input) or user_input == "":
            return default if user_input == "" else user_input
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
                    + incremental_directives
                    + "\n here a recap of all the available directives "
                    + directives_paragraph
                )
            else:
                print("Available directives: " + directives_paragraph)
            continue
        if (
            user_input in incremental_directives
            if incremental_directives
            else user_input in directives
        ) or user_input == "":
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
            return [util_indices[int(i)] for i in parsed_list]
