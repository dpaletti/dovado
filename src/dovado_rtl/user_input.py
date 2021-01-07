import re
from pathvalidate import is_valid_filepath
from os import path
from pathlib import Path
from collections import OrderedDict
from typing import Tuple, Optional, Set, List, Dict
import dovado_rtl.vivado_interaction as vivado
import dovado_rtl.doc_parsing as doc
from dovado_rtl.config import Configuration
from dovado_rtl.simple_types import IsIncremental, Metric
from dovado_rtl.enums import RTL, StopStep, ImplementationStep
from dovado_rtl.src_parsing import SourceParser
from dovado_rtl.antlr.hdl_representation import (
    Entity,
    Parameter,
    Port,
    PortDirection,
    PortDirectionEnum,
    PortType,
    PortTypeEnum,
)


def list_rtl_files(src_path: Path) -> Set[Path]:
    rtl_extensions = ["vhd", "vhdl", "v", "sv"]
    files = []
    for extension in rtl_extensions:
        files += [
            pth for pth in src_path.rglob("*." + extension) if pth.is_file
        ]
    return set(files)


def ask_code_dir() -> str:
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


def get_top_module(
    src_folder: str, module_file: str, config: Configuration
) -> Tuple[Entity, str, SourceParser]:
    for src in list_rtl_files(Path(src_folder)):
        if src.name == module_file:
            sp = SourceParser(src_folder, str(src))
            entities = sp.get_entities()
            if len(entities) > 1:
                print(
                    "Discarding all entities except the first from "
                    + str(src)
                    + " please refactor your code for a more consistent behaviour."
                    + " Put your target module in a file by itself"
                )
            return entities[0], str(src), sp
    raise ValueError("Could not find " + module_file + " in " + src_folder)


def ask_top_module(
    src_folder: str, config: Configuration
) -> Tuple[Entity, str, SourceParser]:
    while True:
        user_input = input("Enter top file (including suffix): ")
        try:
            return get_top_module(src_folder, user_input, config,)
        except ValueError as e:
            print(e)
            continue


def ask_part() -> str:
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


def ask_stop_step() -> StopStep:
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
                StopStep.SYNTHESIS
                if stop_step == "synthesis"
                else StopStep.IMPLEMENTATION
            )


def ask_incremental_mode(stop_step: StopStep) -> IsIncremental:
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
    if stop_step is StopStep.SYNTHESIS:
        return IsIncremental(
            synthesis=True if user_input == "yes" else False,
            implementation=True,
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
            return IsIncremental(
                synthesis=True if user_input == "yes" else False,
                implementation=True if user_second_input == "yes" else False,
            )


def _ask_implementation_directives(
    to_request: ImplementationStep, incremental_mode: IsIncremental,
) -> str:
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


def ask_directives(
    stop_step: StopStep, incremental_mode: IsIncremental
) -> Tuple[str, Optional[str], Optional[str]]:
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
    if stop_step is StopStep.SYNTHESIS:
        return input_synth_directives, None, None
    else:
        return (
            input_synth_directives,
            _ask_implementation_directives(
                ImplementationStep.PLACE, incremental_mode
            ),
            _ask_implementation_directives(
                ImplementationStep.ROUTE, incremental_mode
            ),
        )


def ask_clock() -> int:
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


def is_valid_clock(
    parsed_src: SourceParser, port: Optional[Port]
) -> Tuple[Optional[Port], Optional[PortDirection], Optional[PortType]]:
    if not port:
        return None, None, None
    port_direction = port.get_direction()
    port_type = port.get_type()
    if (
        port_direction.direction is PortDirectionEnum.INPUT
        and port_type.type is PortTypeEnum.SCALAR
        if parsed_src.get_hdl() is RTL.VHDL
        else port_type.type is PortTypeEnum.VECTOR
    ):
        return (
            port,
            port_direction,
            port_type,
        )
    return None, port_direction, port_type


def ask_identifiers(parsed_src: SourceParser) -> Port:
    while True:
        user_input = input("Enter clock identifier: ")
        clock, clock_direction, clock_port_type = is_valid_clock(
            parsed_src, parsed_src.check_port(user_input)
        )
        if clock:
            return clock
        print(
            "Invalid clock identifier: port direction = "
            + str(clock_direction)
            + " (must be an input port) port type = "
            + str(clock_port_type)
            + " (must be binary)\n"
            + "available ports: "
            + str(parsed_src.get_ports())
        )


def ask_parameters_range(
    param_list: List[Parameter], config: Configuration
) -> "OrderedDict[str, Tuple[int, int]]":
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
        user_input = input(
            "Enter range for " + str(param_list[i].get_name()) + ": "
        )
        if user_input == shortcut:
            return OrderedDict(
                zip(
                    [p.get_name() for p in param_list],
                    param_range_accumulator
                    + (
                        [
                            (
                                -int(config.get_config("INTEGER_HIGH")),
                                config.get_config("INTEGER_HIGH"),
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

    return OrderedDict(
        zip([p.get_name() for p in param_list], param_range_accumulator)
    )


def ask_parameters(parsed_src: SourceParser) -> List[Parameter]:
    while True:
        user_input = input(
            "Enter a comma separated list "
            + "of parameters to optimize [example: firstParam, N, width]: "
        )
        param_list = parse_comma_separated_list(r"\w+", user_input)
        available_param_list = [i for i in parsed_src.get_parameters()]
        if param_list and all(
            i in [p.get_name() for p in available_param_list]
            for i in param_list
        ):
            return [
                parsed_src.get_parameter(i)
                for i in [p.get_name() for p in available_param_list]
                if i in param_list
            ]  # return ordered list
        if not param_list:
            print("Malformed list: " + user_input + "\ntry again\n")
        else:
            print(
                "The following parameters could not be found among "
                + "the ones declared in "
                + parsed_src.get_path()
                + " at module "
                + parsed_src.get_top_entity().get_name()
                + ": "
                + str([i for i in param_list if i not in available_param_list])
                + "\nAvailable parameters are "
                + str(available_param_list)
                + "\n"
            )


def ask_utilization_metrics(
    util_indices: Dict[str, List[str]]
) -> List[Metric]:

    info_prompt = "Percentage Utilisation indices available:\n"
    i = 0
    counter_dict = {}
    for section in util_indices.keys():
        info_prompt += section + "\n"
        for util_metric in util_indices[section]:
            i = i + 1
            counter_dict[i] = Metric(
                utilisation=(section, util_metric), is_frequency=False
            )
            info_prompt += "\t(" + str(i) + ") " + util_metric + "\n"

    print(info_prompt)
    default = "-1, 1, 4, 9"
    while True:
        user_input = input(
            "Enter a comma-separated list of percentage "
            + "indices to optimize, input -1 to select frequency [default = "
            + default
            + "]: "
        )
        if user_input == "":
            user_input = default
        try:
            parsed_list = [
                int(i)
                for i in parse_comma_separated_list(r"[-+]?\d+", user_input)
            ]
            if parsed_list and max([i for i in parsed_list if i > 0]) < len(
                counter_dict
            ):
                out: List[Metric] = [
                    counter_dict[i]
                    for i in set([i for i in parsed_list if i >= 0])
                ]
                return (
                    (out + [Metric(None, True)])
                    if (-1 in parsed_list)
                    else out
                )
        except Exception as e:
            print(e)
            print(
                "Invalid input, please enter"
                + " a comma separated list of integer numbers"
            )


def ask_is_point_evaluation() -> bool:
    default = "p"
    while True:
        user_input = input(
            "Would you like to run single point evaluation "
            + "or design space evaluation?\n"
            + "Please input 'p' for point evaluation "
            + "or 'd' for design space evaluation "
            "[default = " + default + "]: "
        )
        user_input = user_input.strip()
        if not (user_input == "p" or user_input == "d"):
            print(
                user_input
                + " is an in invalid input, please input either 'p' or 'd'"
            )
            continue
        return True if user_input == "p" else False


def ask_parameters_value(param_list: List[Parameter]) -> List[int]:
    if len(param_list) == 0:
        raise Exception(
            "No params passed to ask_parameters_value, at least one must be selected"
        )
    parameter_value_accumulator = []
    i = 0
    while i < len(param_list):
        user_input = input(
            "Enter value for parameter " + param_list[i].get_name() + ": "
        )
        try:
            parameter_value_accumulator.append(int(user_input))
            i = i + 1
        except Exception:
            print("Please input an integer value")
            continue
    return parameter_value_accumulator
