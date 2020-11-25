from typing import List, Optional, Tuple
import numpy as np
import dovado_rtl.user_input as user_input
import dovado_rtl.report_parsing as report_utilities
from dovado_rtl.config import Configuration
import dovado_rtl.vivado_interaction as vivado
from dovado_rtl.frame_handling import (
    TclFrameHandler,
    HdlBoxFrameHandler,
    XdcFrameHandler,
)
from dovado_rtl.utility_classes import StopStep, IsIncremental, RTL
from dovado_rtl.src_parsing import SourceFile
from dovado_rtl.point_evaluation import DesignPointEvaluator
from dovado_rtl.estimation import Estimator
from dovado_rtl.fitness import FitnessEvaluator
from dovado_rtl.genetic_algorithm import optimize


def main():
    vivado.start()
    config: Configuration = Configuration()

    src_folder: str = user_input.ask_code_dir()
    top_module: str
    top_src: str
    top_module, top_src = user_input.ask_top_module(src_folder, config)
    parsed_source: SourceFile = SourceFile(src_folder + top_src)
    synthesis_part: str = user_input.ask_part()

    stop_step: StopStep = user_input.ask_stop_step()

    free_parameters: List[str] = user_input.ask_parameters(parsed_source)

    clock_port: str = user_input.ask_identifiers(parsed_source)

    incremental_mode: IsIncremental = user_input.ask_incremental_mode(
        stop_step
    )

    synthesis_directive: str
    place_directive: Optional[str]
    route_directive: Optional[str]
    (
        synthesis_directive,
        place_directive,
        route_directive,
    ) = user_input.ask_directives(stop_step, incremental_mode)

    # Clock given in Mhz
    target_clock: float = user_input.ask_clock()

    XdcFrameHandler(
        config.get_config("PLACEHOLDER"),
        config.get_config("XDC_DIR") + config.get_config("CONSTRAINT_FRAME"),
        1000 / target_clock,
        config.get_config("XDC_DIR") + config.get_config("CONSTRAINT"),
    ).fill_xdc()

    tcl_handler = TclFrameHandler(
        config,
        parsed_source,
        True,
        synthesis_part,
        synthesis_directive,
        incremental_mode,
        stop_step,
        place_directive,
        route_directive,
    ).fill_tcl()

    box_handler: HdlBoxFrameHandler = HdlBoxFrameHandler(
        config.get_config("PLACEHOLDER"),
        config.get_config("VHDL_DIR") + config.get_config("VHDL_BOX_FRAME")
        if parsed_source.get_hdl() is RTL.VHDL
        else config.get_config("VERILOG_DIR")
        + config.get_config("VERILOG_BOX_FRAME"),
        top_module,
        parsed_source.get_ports(),
        parsed_source.get_port(clock_port),
        config.get_config("VHDL_DIR") + config.get_config("VHDL_BOX")
        if parsed_source.get_hdl() is RTL.VHDL
        else config.get_config("VERILOG_DIR")
        + config.get_config("VERILOG_BOX"),
        parsed_source.get_hdl(),
        parsed_source.get_top_level()
        if parsed_source.get_hdl() is RTL.VHDL
        else None,
    )

    metrics: List[Tuple[str, str]] = user_input.ask_utilization_metrics(
        report_utilities.get_available_indices(
            config.get_config("VIVADO_OUTPUT_DIR")
            + config.get_config(stop_step.name + "_UTILISATION")
        )
    )

    point_evaluator = DesignPointEvaluator(
        config,
        parsed_source,
        box_handler,
        tcl_handler,
        True,
        target_clock,
        user_input.ask_incremental_mode(stop_step),
        stop_step,
        free_parameters,
        metrics,
    )
    if user_input.ask_is_point_evaluation():
        print(
            "Point Evaluation result\n"
            + str(
                point_evaluator.evaluate(
                    tuple(user_input.ask_parameters_value(free_parameters))
                )
            )
        )
        return

    # OrderedDict from typing is available only from python 3.7 (we support python 3.6)
    # OrderedDict[str, Tuple[int, int]]
    free_parameters_range = user_input.ask_parameters_range(
        free_parameters, config
    )

    estimator: Estimator = Estimator(
        point_evaluator,
        free_parameters_range,
        config.get_config("INITIAL_SAMPLES"),
    )
    fitness_evaluator: FitnessEvaluator = FitnessEvaluator(
        estimator, point_evaluator, config
    )

    result: np.ndarray = optimize(
        fitness_evaluator,
        free_parameters_range,
        metrics,
        config.get_config("GENETIC_RUN_TIME"),
    )
    print("Optimization Result: " + str(result))


main()
