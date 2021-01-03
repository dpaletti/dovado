from click import BadParameter
import typer
from typing import Tuple, List
from pathlib import Path
from dovado_rtl.doc_parsing import get_directives, get_directives_paragraph
from dovado_rtl.src_parsing import SourceParser
from dovado_rtl.vivado_interaction import get_parts
from dovado_rtl.antlr.hdl_representation import PortDirectionEnum
from dovado_rtl.enums import RegressionModel


def validate_estimator(value: str) -> str:
    if value.upper() not in RegressionModel.__members__.keys():
        raise typer.BadParameter(
            "Invalid estimator "
            + value
            + " available estimators are "
            + str(set(RegressionModel.__members__.keys()))
        )
    return value


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
