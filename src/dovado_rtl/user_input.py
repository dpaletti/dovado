import re
from pathvalidate import is_valid_filepath
from os import path
from pathlib import Path
import dovado_rtl.vivado_interaction as vivado
import dovado_rtl.doc_parsing as doc
import dovado_rtl.src_parsing as parsing
from dovado_rtl.config import get_config


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
        if module in parsing.get_modules(
            Path(src)
        ) and src != src_folder + get_config("VHDL_LOCAL_SRC"):
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
    default = list(parts.keys())[0]
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


def ask_stop_step() -> parsing.StopStep:
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
            stop_step = default if user_input == "" else user_input
            return (
                parsing.StopStep.SYNTHESIS
                if stop_step == "synthesis"
                else parsing.StopStep.IMPLEMENTATION
            )


def ask_incremental_mode(stop_step) -> parsing.IsIncremental:
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
    if stop_step is parsing.StopStep.SYNTHESIS:
        return parsing.IsIncremental(
            synthesis=True if user_input == "yes" else False
        )
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
            return parsing.IsIncremental(
                synthesis=True if user_input == "yes" else False,
                implementation=True if user_second_input == "yes" else False,
            )


def _ask_implementation_directives(
    to_request: parsing.ImplementationStep,
    incremental_mode: parsing.IsIncremental,
):
    if not isinstance(to_request, parsing.ImplementationStep):
        raise ValueError(
            "_request_incremental_directives called with " + str(to_request)
        )

    default = "Default"
    directives_paragraph = doc.get_directives_paragraph(
        to_request.name.lower()
    )
    directives = doc.get_directives(directives_paragraph)
    incremental_directives = doc.get_directives(
        doc.get_directives_paragraph("read checkpoint")
    )
    while True:
        user_input = input(
            "What directive do you want to give to the "
            + str(to_request)
            + ' step? Input"?"'
            + " to get help on available directives."
            + " [default = "
            + default
            + "]: "
        )
        if user_input == "?":
            if incremental_mode.implementation:
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
                if incremental_mode.implementation
                else directives
            )
            or user_input == ""
        ):
            return default if user_input == "" else user_input


def ask_directives(stop_step, incremental_mode: parsing.IsIncremental):
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
    if stop_step is parsing.StopStep.SYNTHESIS:
        return input_synth_directives, None, None
    else:
        return (
            input_synth_directives,
            _ask_implementation_directives(
                parsing.ImplementationStep.PLACE, incremental_mode
            ),
            _ask_implementation_directives(
                parsing.ImplementationStep.ROUTE, incremental_mode
            ),
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


def ask_parameters_range(param_list):
    shortcut = "_"
    print(
        "For each parameter specify a range e.g.'0 100' ,\n"
        + "a shorthand for the maximum integer value is int_high so "
        + "'-int_high int_high' specifies the whole integer range while "
        + "'0 int_high' specifies a natural for example. \n"
        + "Enter "
        + shortcut
        + " at any point to fix all unspecified ranges to "
        + "'-int_high int_high'"
    )
    param_range_accumulator = []
    i = 0
    while i < len(param_list):
        user_input = input("Enter range for " + param_list[i] + ": ")
        if user_input == shortcut:
            return dict(
                zip(
                    param_list,
                    param_range_accumulator
                    + (
                        [
                            (
                                -get_config("INTEGER_HIGH"),
                                get_config("INTEGER_HIGH"),
                            )
                        ]
                        * (len(param_list) - len(param_range_accumulator))
                    ),
                )
            )
        splitted_input = user_input.strip().split()
        if len(splitted_input) > 2:
            print("Please input only two integers separated by a whitespace")
            continue
        try:
            param_range_accumulator.append(
                (int(splitted_input[0]), int(splitted_input[1]))
            )
            i = i + 1
        except Exception:
            print("Could not parse input as a pair of integers ")

    return dict(zip(param_list, param_range_accumulator))


def ask_parameters(src, module):
    while True:
        user_input = input(
            "Enter a comma separated list "
            + "of parameters to optimize [example: firstParam, N, width]: "
        )
        param_list = parse_comma_separated_list(r"\w+", user_input)
        available_param_list = [
            i.name for i in parsing.get_parameters(Path(src), module)
        ]
        if param_list and all(i in available_param_list for i in param_list):
            return [
                i for i in available_param_list if i in param_list
            ]  # return ordered list
        if not param_list:
            print("Malformed list: " + user_input + "\ntry again\n")
        else:
            print(
                "The following parameters could not be found among "
                + "the ones declared in "
                + src
                + " at module "
                + module
                + ": "
                + str([i for i in param_list if i not in available_param_list])
                + "\nAvailable parameters are "
                + str(available_param_list)
                + "\n"
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


def ask_utilization_metrics(util_indices):

    info_prompt = "Percentage Utilisation indices available:\n"
    i = 0
    counter_dict = {}
    for section in util_indices.keys():
        info_prompt += section + "\n"
        for metric in util_indices[section]:
            i = i + 1
            counter_dict[i] = (section, metric)
            info_prompt += "\t(" + str(i) + ") " + metric + "\n"

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
        parsed_list = parse_comma_separated_list(r"\d+", user_input)
        try:
            if parsed_list and max([int(i) for i in parsed_list]) < len(
                counter_dict
            ):
                return [counter_dict[int(i)] for i in set(parsed_list)]
        except Exception:
            print(
                "Invalid input, please enter"
                + " a comma separated list of integer numbers"
            )


def ask_is_point_evaluation():
    default = "p"
    while True:
        user_input = input(
            "Would you like to run single point evaluation "
            + "or design space evaluation?\n"
            + "Please input 'p' for point evaluation "
            + "or 'd' for design space evaluation "
            "[default = " + default + "]"
        )
        user_input = user_input.strip()
        if not (user_input == "p" or user_input == "d"):
            print(
                user_input
                + " is an in invalid input, please input either 'p' or 'd'"
            )
            continue
        return True if user_input == "p" else False


def ask_parameters_value(param_list):
    parameter_value_accumulator = []
    i = 0
    while i < len(param_list):
        user_input = input("Enter value for parameter " + param_list[i] + ":")
        try:
            parameter_value_accumulator.append(int(user_input))
            i = i + 1
        except Exception:
            print("Please input an integer value")
            continue
    return parameter_value_accumulator
