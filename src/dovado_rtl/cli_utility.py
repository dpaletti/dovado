from click import BadParameter
import re
import typer
from typing import Tuple, List, Dict, Optional
from pathlib import Path
from dovado_rtl.doc_parsing import get_directives, get_directives_paragraph
from dovado_rtl.src_parsing import SourceParser
from dovado_rtl.vivado_interaction import get_parts
from dovado_rtl.antlr.hdl_representation import PortDirectionEnum
from dovado_rtl.simple_types import Metric
from movado import models, controllers


def validate_power_of_2(value: List[str], ctx: typer.Context):
    if len(ctx.params["parameters"]) != len(value):
        raise BadParameter(
            "power of 2 constraint must be specified for each parameter, mismatching list lengths"
            + ", parameter list lenght:"
            + str(len(ctx.params["parameters"]))
            + ", constraint list length: "
            + str(len(value))
        )
    for i in value:
        if i not in {"y", "n"}:
            raise BadParameter("Accepted input are only y/n")
    return value


def validate_int_metrics(value: List[int]):
    for i in value:
        if i < 0:
            raise BadParameter(
                "Invalid metric '" + str(i) + ", all parameters must be >= 0"
            )
    return value


def parse_comma_separated_list(
    regexp_element: str,
    to_parse: str,
) -> Optional[List[str]]:
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


def ask_utilization_metrics(
    util_indices: Dict[str, List[str]],
    pre_selected_metrics: Optional[List[int]] = None,
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

    while True:
        if not pre_selected_metrics:
            typer.echo(info_prompt)
            user_input = typer.prompt(
                "Enter a comma-separated list of percentage "
                + "indices to optimize, input 0 to select frequency"
            )
        try:
            if not pre_selected_metrics:
                parsed_list = [
                    int(i)
                    for i in parse_comma_separated_list(r"[+]?\d+", user_input)
                ]
            else:
                parsed_list = pre_selected_metrics
                pre_selected_metrics = None
            if parsed_list and (
                parsed_list == []
                or max([i for i in parsed_list if i > 0]) < len(counter_dict)
            ):
                out: List[Metric] = [
                    counter_dict[i] for i in {i for i in parsed_list if i > 0}
                ]
                return (
                    (out + [Metric(None, True)]) if (0 in parsed_list) else out
                )
        except Exception as e:
            print(e)
            print(
                "Invalid input, please enter"
                + " a comma separated list of integer numbers"
            )


def validate_nearest_distance(value: int) -> int:
    if value < 0:
        raise typer.BadParameter(
            "Invalid distance value: "
            + str(value)
            + " non-negative integer expected"
        )
    return value


def validate_estimator(value: str) -> str:
    if value in models:
        return value
    raise typer.BadParameter(
        "Invalid estimation model "
        + value
        + " available models are: "
        + str(models)
    )


def validate_controller(value: str) -> str:
    if value in controllers:
        return value
    raise typer.BadParameter(
        "Invalid controller "
        + value
        + " available controllers are: "
        + str(controllers)
    )


def validate_board(value: str) -> str:
    parts = get_parts()
    if value in set(parts.keys()):
        return value
    raise typer.BadParameter(
        "Invalid board " + value + " available boards are: " + str(parts)
    )


def validate_parameters(ctx: typer.Context, value: List[str]) -> List[str]:

    file_path = Path(ctx.params["file_path"]).absolute()
    if not ctx.obj:
        parsed_src = SourceParser(
            str(SourceParser.get_project_path(file_path)), str(file_path)
        )
        parsed_src.set_entity(str(parsed_src.get_entities()[0].get_name()))
        ctx.obj = parsed_src
    else:
        parsed_src: SourceParser = ctx.obj
    parameter_name_list = [p.get_name() for p in parsed_src.get_parameters()]
    for chosen_parameter in value:
        if chosen_parameter not in parameter_name_list:
            raise typer.BadParameter(
                "Chosen parameter: "
                + chosen_parameter
                + " is not among available parameters "
                + str(parameter_name_list)
            )
    return value


def validate_clock_port(ctx: typer.Context, value: str) -> str:
    parsed_src: SourceParser = ctx.obj
    for port in parsed_src.get_ports():
        if (
            port.get_name() == value
            and port.get_direction().direction is PortDirectionEnum.INPUT
        ):
            return value
    raise typer.BadParameter(
        "Chosen clock port: "
        + value
        + " is not among available input ports "
        + str(
            [
                p.get_name()
                for p in parsed_src.get_ports()
                if p.get_direction().direction is PortDirectionEnum.INPUT
            ]
        )
    )


def validate_directives(value: Tuple[str, str, str]):
    commands = ["synthesis", "place", "route"]
    for c in commands:
        directive = value[commands.index(c)]
        directives = get_directives((get_directives_paragraph(c)))
        if directive not in directives:
            raise typer.BadParameter(
                "Chosen directive for "
                + c
                + ": "
                + directive
                + " is not among available directives for "
                + c
                + " "
                + str(directives)
            )
    return value


def validate_target_clock(value: float) -> float:
    if value > 0:
        return value
    raise BadParameter(
        "Target clock must be positive, invalid target clock input: "
        + str(value)
    )


def validate_param_ranges(value: List[int]) -> List[int]:
    if len(value) % 2 == 0:
        return value
    raise typer.BadParameter(
        "Parameter ranges list must be of even length, "
        + "each odd element is the start of the range and the next one is the end of the range"
    )
