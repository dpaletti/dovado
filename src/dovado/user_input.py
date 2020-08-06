import re
from pathvalidate import is_valid_filepath
from os import path
import dovado.vhdl_parsing as vhdl
import dovado.verilog_parsing as verilog
import dovado.vivado_interaction as vivado


def request_code_dir():
    while True:
        default = "./"
        user_input = input(
            "Enter path to code folder" + " [default = " + "./" + "]: "
        )
        if (
            is_valid_filepath(user_input)
            and path.exists(user_input)
            and (vhdl.list_files(user_input) or verilog.list_files(user_input))
        ) or user_input == "":
            return default if user_input == "" else user_input

        print("Invalid path, ensure there are no typos\n")


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
    for src in verilog.list_files():
        modules = verilog.list_modules(src)
        if modules:
            return modules[0]
    print("No module found in the given source files")
    exit(1)


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
            "Enter part (input ? to have a list of available parts) [default ="
            + default
            + "]: "
        )
        if user_input in parts or user_input == "":
            return default if user_input == "" else user_input
        if user_input == "?":
            print("Available parts\n" + str(parts))
        print("Part not available.")


def request_stop_step():
    default = "synthesis"
    while True:
        user_input = input(
            "Would you like to get utilization and frequency after logical"
            + "synthesis or after place and route?"
            + "(allowed answers = synthesis/place and route)"
            + "[default ="
            + default
            + "]: "
        )
        if (
            user_input == "synthesis"
            or user_input == "place and route"
            or user_input == ""
        ):
            return default if user_input == "" else user_input


def request_incremental_mode(stop_step):
    default = "yes"
    default_second = "yes"
    while True:
        user_input = input(
            "Do you want to run synthesis in incremental mode?"
            + "(options = yes/no) [default = yes]:"
        )
        if user_input == "yes" or user_input == "no" or user_input == "":
            user_input = default if user_input == "" else user_input
            break
    if stop_step == "implementation":
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
    return {
        "is synthesis incremental": True if user_input == "yes" else False,
    }


def request_directives(stop_step, incremental_mode):
    while True:
        user_input = input(
            "What directives do you want to give to the"
            + ' synthesis step? input "?" to get help for'
            + " synth_design and look at -directive for"
            + " all the available directives"
            + " (input must be a comma separeted list)"
            + " [default = runtimeoptimized]"
        )


def request_utilization_metrics(available_metrics):
    util_indices = dict(
        zip(range(1, len(available_metrics) + 1), iter(available_metrics))
    )

    info_prompt = "Percentage Utilisation indices available:\n"
    for (k, v) in util_indices.items():
        info_prompt += "(" + str(k) + ") " + v + "\n"

    print(
        "Percentage Utilisation indices available:\n"
        + info_prompt
        + "Recap of interdependences among above indices:\n"
        + "(1) = (2) + (3)\n"
        + "(4) = (5) + (6)\n"
        + "(9) = (10) + (11)\n"
        + "Naming follows names found in the Vivado utilisation report\n"
    )
    default = "1, 4, 9"
    while True:
        user_input = input(
            "Enter a comma-separated list of percentage "
            + "utilisation indices [default = +"
            + default
            + "]: "
        )
        if (
            re.fullmatch(
                r"^([1-9]|1[0-1])(([ \t]*,[ \t]*)([1-9]|1[0-2]))*$", user_input
            )
            or user_input == ""
        ):
            if user_input == "":
                user_input = default
            return [
                util_indices[int(i)]
                for i in re.sub(re.compile("[ \t]*"), "", user_input).split(
                    ","
                )
            ]
