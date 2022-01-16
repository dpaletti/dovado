from pathlib import Path
from typing import Tuple, List, Optional
from collections import OrderedDict
from random import randrange

from dovado_rtl.antlr.hdl_representation import ParameterTypeEnum
from dovado_rtl.config import Configuration
import dovado_rtl.vivado_interaction as vivado
from dovado_rtl.frame_handling import (
    TclFrameHandler,
    HdlBoxFrameHandler,
    XdcFrameHandler,
)
from dovado_rtl.enums import RTL, StopStep
from dovado_rtl.simple_types import IsIncremental
from dovado_rtl.point_evaluation import DesignPointEvaluator
from dovado_rtl.fitness import FitnessEvaluator
from dovado_rtl.genetic_algorithm import optimize
from dovado_rtl.cli_utility import (
    validate_board,
    validate_parameters,
    validate_clock_port,
    validate_directives,
    validate_target_clock,
    validate_estimator,
    validate_int_metrics,
    validate_controller,
)
import typer

from dovado_rtl.src_parsing import SourceParser

app = typer.Typer(help="Dovado RTL design automation and space exploration")
vivado.start()


def main():
    app()


@app.callback()
def dovado(
    ctx: typer.Context,
    # Arguments
    # file_path is used through the context in cli_utility during parameters validation
    # and is then passed through context
    # until it reaches this method where it is extracted and used as parsed_src
    file_path: Path = typer.Option(  # pylint: disable=unused-argument
        ...,
        exists=True,
        file_okay=True,
        readable=True,
        resolve_path=True,
        help=(
            "path of the rtl file containing the top level entity, please check the documentation"
            + " for the directory structure your RTL project should comply with"
        ),
    ),
    # Required Cli options
    board: str = typer.Option(
        ...,
        callback=validate_board,
        help="Part name for synthesis/implementation, inserting the wrong one"
        + " will get an error message with all the parts available with your Vivado installation",
    ),
    parameters: List[str] = typer.Option(
        ...,
        callback=validate_parameters,
        help="parameters to use for point/space exploration, only integer (subtypes) and booleans are supported",
    ),
    clock_port: str = typer.Option(
        ...,
        callback=validate_clock_port,
        help="clock port name of the top module/entity",
    ),
    # Optional Cli options
    implementation: bool = typer.Option(
        False,
        help="flag to set point/space exploration to stop at implementation instead of synthesis",
    ),
    incremental: bool = typer.Option(
        False,
        help="flag to choose whether to choose incrementaly synthesis/implementation",
    ),
    directives: Tuple[str, str, str] = typer.Option(
        default=(
            "runtimeoptimized",
            "RuntimeOptimized",
            "RuntimeOptimized",
        ),  # capitalization is necessary to comply with vivado directives specification
        callback=validate_directives,
        help="directives to pass respectively to synthesis, place and route",
    ),
    target_clock: float = typer.Option(
        default=1000,
        callback=validate_target_clock,
        help="target clock (Mhz) on which the worst negative slack is computed,"
        + "make sure this is sufficiently large to never be reached by your design",
    ),
    metrics: Optional[List[int]] = typer.Option(
        None,
        callback=validate_int_metrics,
        help="list of integers representing selected metrics, "
        + "wait for first synthesis/implementation if you do not know the mapping",
    ),
):  # pylint: disable=too-many-arguments
    # pylint: disable=too-many-locals
    config = Configuration()
    Path(str(config.get_config("WORK_DIR"))).mkdir(parents=True, exist_ok=True)

    parsed_src = ctx.obj
    project_path = parsed_src.get_root_folder()

    if implementation:
        stop_step = StopStep.IMPLEMENTATION
    else:
        stop_step = StopStep.SYNTHESIS
    if incremental:
        incremental_mode = IsIncremental(True, True)
    else:
        incremental_mode = IsIncremental(False, False)

    XdcFrameHandler(
        str(config.get_config("PLACEHOLDER")),
        str(config.get_config("XDC_DIR"))
        + str(config.get_config("CONSTRAINT_FRAME")),
        1000 / target_clock,
        str(config.get_config("WORK_DIR"))
        + str(config.get_config("CONSTRAINT")),
    ).fill()

    tcl_handler = TclFrameHandler(
        config,
        parsed_src,
        str(project_path),
        board,
        directives[0],
        incremental_mode,
        stop_step,
        directives[1],
        directives[2],
    )
    tcl_handler.fill()

    box_handler = HdlBoxFrameHandler(
        str(config.get_config("PLACEHOLDER")),
        str(config.get_config("VHDL_DIR"))
        + str(config.get_config("VHDL_BOX_FRAME"))
        if parsed_src.get_hdl() is RTL.VHDL
        else str(config.get_config("VERILOG_DIR"))
        + str(config.get_config("VERILOG_BOX_FRAME")),
        parsed_src.get_selected_entity().get_name(),
        parsed_src.get_ports(),
        parsed_src.get_port(clock_port),
        str(config.get_config("WORK_DIR")) + str(config.get_config("VHDL_BOX"))
        if parsed_src.get_hdl() is RTL.VHDL
        else str(config.get_config("WORK_DIR"))
        + str(config.get_config("VERILOG_BOX")),
        parsed_src.get_hdl(),
        parsed_src.get_folder(),
    )

    point_evaluator = DesignPointEvaluator(
        config,
        parsed_src,
        box_handler,
        tcl_handler,
        target_clock,
        incremental_mode,
        stop_step,
        list(parameters),
        metrics,
    )
    ctx.obj = {
        "parameters": parameters,
        "point_evaluator": point_evaluator,
        "config": config,
    }


@app.command("points")
def points(
    ctx: typer.Context,
    param_values_path: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        readable=True,
        resolve_path=True,
        help="path to a csv file containing on each line values for each parameter previously selected"
        + " (values won't be recorded until the first valid design point, e.g. the first set"
        + " of values which won't make synthesis/implementation fail)",
    ),
):
    """
    RTL Design automation
    """
    out_file = Path(ctx.obj["config"].get_config("WORK_DIR")).joinpath(
        "point_evaluation.csv"
    )
    out_file.open("w").close()
    first_evaluation = True
    for input_line in Path(param_values_path).read_text().splitlines():
        design_point = input_line.split(",")
        design_value = ctx.obj["point_evaluator"].evaluate(tuple(design_point))
        if design_value and first_evaluation:
            output_line = "Design Point,"
            for k in design_value.value.keys():
                if k.utilisation:
                    output_line += k.utilisation[0] + "-" + k.utilisation[1]
                elif k.is_frequency:
                    output_line += "Frequency"
                elif k.custom_metric:
                    output_line += k.custom_metric[0]
                output_line += ","
            out_file.open("a").writelines([output_line[:-1] + "\n"])
            first_evaluation = False
        if design_value and not first_evaluation:
            output_line = ""
            output_line += "("
            for point_value in design_point:
                output_line += point_value + "-"
            output_line = output_line[:-1]
            output_line += "),"
            for v in design_value.value.values():
                output_line += str(v) + ","
            out_file.open("a").writelines([output_line[:-1] + "\n"])


@app.command(
    "space",
    context_settings={
        "allow_extra_args": True,
        "ignore_unknown_options": True,
    },
)
def space(
    ctx: typer.Context,
    param_ranges: List[int] = typer.Argument(
        ...,
        help="list of integers in which each odd indexed element starts"
        + " a range and the consecutive closes it (start counting from 1)",
    ),
    power_of_2: Optional[List[str]] = typer.Option(
        None,
        help="list of 'y'/'n' where y indicates that the corresponding, in order, parameter must be a power of 2",
    ),
    param_initial_values: Optional[List[int]] = typer.Option(
        None,
        help="state initial values for parameters which are guaranteed to synthesize/implement",
    ),
    optimization_runtime: Optional[str] = typer.Option(
        None, help="optimization timeout as hh:mm:ss"
    ),
    disable_approximate: Optional[bool] = typer.Option(
        False, help="disable approximations for fitness function"
    ),
    estimation_model: Optional[str] = typer.Option(
        "HoeffdingAdaptiveTree",
        callback=validate_estimator,
        help="estimator to use for fitness function approximation (see movado docs for more information),"
        + "'HoeffdingAdaptiveTree' is default. 'KernelRidge' selects a kernel regression",
    ),
    controller_model: Optional[str] = typer.Option(
        "Mab",
        callback=validate_controller,
        help="controller to use for fitness function approximation (see movado docs for more information),"
        + "'Distance' is default. 'Mab' selects a pure multi-armed bandit controller, ",
    ),
    disable_controller_mab_weight: Optional[bool] = typer.Option(
        False, help="disable loss weighting in Distance Controller"
    ),
    n_controllers: Optional[int] = typer.Option(
        1, help="set the number of controllers for movado (voters)"
    ),
    many_objective: Optional[bool] = typer.Option(
        False,
        help="use AGE-MOEA instead of NSGA-II as genetic algorithm,"
        + " in case of many objectives (e.g. > 4) it may give better performance",
    ),
):
    """
    RTL design space exploration
    """
    for idx, param in enumerate(ctx.obj["parameters"]):
        parsed_src: SourceParser = ctx.obj["point_evaluator"].get_parsed_src()
        full_param = parsed_src.get_parameter(param)
        if full_param.get_type().type is ParameterTypeEnum.BOOL:
            param_ranges = (
                list(param_ranges[: idx * 2])
                + [0, 1]
                + (
                    list(param_ranges[idx * 2 :])
                    if (idx * 2) < len(param_ranges)
                    else []
                )
            )

    it = iter(param_ranges)
    ranges_dict = OrderedDict(zip(ctx.obj["parameters"], zip(it, it)))
    if param_initial_values:
        design_value = ctx.obj["point_evaluator"].evaluate(
            tuple(param_initial_values)
        )
        if not design_value:
            raise Exception(
                "Could not synthesize/implement " + str(param_initial_values)
            )
    else:
        print(
            "Trying random parameter values in the range given to get first synthesis/implementation"
        )
        design_value = ctx.obj["point_evaluator"].evaluate(
            tuple([randrange(i, j) for i, j in ranges_dict.values()])
        )
        while not design_value:
            print(
                "Trying random parameter values in the range given to get first synthesis/implementation"
            )
            design_value = ctx.obj["point_evaluator"].evaluate(
                tuple([randrange(i, j) for i, j in ranges_dict.values()])
            )
        print("First synthesis succeeded")

    metrics = ctx.obj["point_evaluator"].get_metrics()
    fitness_evaluator = FitnessEvaluator(
        ctx.obj["point_evaluator"],
        disable=disable_approximate,
        controller=controller_model,
        estimator=estimation_model,
        controller_mab_weight=not disable_controller_mab_weight,
        voters=n_controllers,
    )

    execution_time = optimize(
        fitness_evaluator,
        ranges_dict,
        metrics,
        optimization_runtime,
        power_of_2,
        many_objective,
    )
    print("\n\nExecution Time: " + str(execution_time) + "\n\n")


main()
