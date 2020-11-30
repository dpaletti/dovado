import dovado_rtl.user_input as user_input
import dovado_rtl.report_parsing as report_utilities
from dovado_rtl.config import Configuration
import dovado_rtl.vivado_interaction as vivado
from dovado_rtl.concrete_frame_handling import (
    TclFrameHandler,
    HdlBoxFrameHandler,
    XdcFrameHandler,
)
from dovado_rtl.utility_classes import RTL
from dovado_rtl.src_parsing import SourceFile
from dovado_rtl.point_evaluation import DesignPointEvaluator
from dovado_rtl.estimation import Estimator
from dovado_rtl.fitness import FitnessEvaluator
from dovado_rtl.genetic_algorithm import optimize


def main():
    vivado.start()
    config = Configuration()

    src_folder = user_input.ask_code_dir()
    top_module, top_src = user_input.ask_top_module(src_folder, config)
    parsed_source = SourceFile(top_src, top_module)
    synthesis_part = user_input.ask_part()

    stop_step = user_input.ask_stop_step()

    free_parameters = user_input.ask_parameters(parsed_source)

    clock_port = user_input.ask_identifiers(parsed_source)

    incremental_mode = user_input.ask_incremental_mode(stop_step)

    (
        synthesis_directive,
        place_directive,
        route_directive,
    ) = user_input.ask_directives(stop_step, incremental_mode)

    # Clock given in Mhz
    target_clock = user_input.ask_clock()

    XdcFrameHandler(
        str(config.get_config("PLACEHOLDER")),
        str(config.get_config("XDC_DIR"))
        + str(config.get_config("CONSTRAINT_FRAME")),
        1000 / target_clock,
        str(config.get_config("XDC_DIR"))
        + str(config.get_config("CONSTRAINT")),
    ).fill()

    tcl_handler = TclFrameHandler(
        config,
        parsed_source,
        synthesis_part,
        synthesis_directive,
        incremental_mode,
        stop_step,
        place_directive,
        route_directive,
    )
    tcl_handler.fill()

    box_handler = HdlBoxFrameHandler(
        str(config.get_config("PLACEHOLDER")),
        str(config.get_config("VHDL_DIR"))
        + str(config.get_config("VHDL_BOX_FRAME"))
        if parsed_source.get_hdl() is RTL.VHDL
        else str(config.get_config("VERILOG_DIR"))
        + str(config.get_config("VERILOG_BOX_FRAME")),
        top_module.get_name(),
        parsed_source.get_ports(),
        parsed_source.get_port(clock_port.get_name()),
        str(config.get_config("VHDL_DIR")) + str(config.get_config("VHDL_BOX"))
        if parsed_source.get_hdl() is RTL.VHDL
        else str(config.get_config("VERILOG_DIR"))
        + str(config.get_config("VERILOG_BOX")),
        parsed_source.get_hdl(),
        parsed_source.get_top_level()
        if parsed_source.get_hdl() is RTL.VHDL
        else None,
    )

    metrics = user_input.ask_utilization_metrics(
        report_utilities.get_available_indices(
            str(config.get_config("VIVADO_OUTPUT_DIR"))
            + str(config.get_config(stop_step.name + "_UTILISATION"))
        )
    )

    point_evaluator = DesignPointEvaluator(
        config,
        parsed_source,
        box_handler,
        tcl_handler,
        target_clock,
        incremental_mode,
        stop_step,
        [p.get_name() for p in free_parameters],
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

    free_parameters_range = user_input.ask_parameters_range(
        free_parameters, config
    )

    estimator = Estimator(
        point_evaluator,
        free_parameters_range,
        int(config.get_config("INITIAL_SAMPLES")),
    )
    fitness_evaluator = FitnessEvaluator(estimator, point_evaluator, config)

    result = optimize(
        fitness_evaluator,
        free_parameters_range,
        metrics,
        str(config.get_config("GENETIC_RUN_TIME")),
    )
    print("Optimization Result: " + str(result))


main()