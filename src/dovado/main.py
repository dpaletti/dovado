import dovado.user_input as user_input
import dovado.vivado_interaction as vivado
import dovado.frame_handling as frame

# from dovado.point_evaluation import evaluate, setup_evaluation
from dovado.genetic_algorithm import optimize
from dovado.src_parsing import (
    get_parameters,
    get_parameter_range,
    is_to_box,
    RTL,
)
import dovado.global_user_selections as gus
import dovado.report_parsing as report
import dovado.point_evaluation as pe
import yaml
from pathlib import Path


def main():
    # Starting Vivado in the background
    vivado.start()

    CONFIG = yaml.safe_load(Path("config.yaml").open())

    SRC_FOLDER = user_input.ask_code_dir()
    TOP_MODULE, TOP_SRC = user_input.ask_top_module(SRC_FOLDER)
    TOP_SUFFIX = Path(SRC_FOLDER + TOP_SRC).suffix
    if TOP_SUFFIX == ".vhd" or ".vhdl":
        TOP_LANG = RTL.VHDL
    elif TOP_SUFFIX == ".v":
        TOP_LANG = RTL.VERILOG
    elif TOP_SUFFIX == ".sv":
        TOP_LANG = RTL.SYSTEM_VERILOG
    else:
        raise ValueError(
            "Parsed files must have .v, .vhd, .vhdl or .sv as a suffix not "
            + TOP_SUFFIX
        )

    SYNTHESIS_PART = user_input.ask_part()

    # STOP_STEP can take the following values:
    #  "synthesis", "implementation"
    STOP_STEP = user_input.ask_stop_step()

    TO_BOX = is_to_box(Path(TOP_SRC), STOP_STEP)

    # A local copy of the top module source file is needed
    # in order to update the parameters in place
    if not TO_BOX:
        with Path(
            SRC_FOLDER + CONFIG["VHDL_LOCAL_SRC"]
            if TOP_SUFFIX == ".vhd"
            else SRC_FOLDER + CONFIG["VERILOG_LOCAL_SRC"]
        ).open("w+") as f:
            f.write(Path(TOP_SRC).read_text())

    # Clock and out are needed for boxing the component
    # to avoid overflowing pins
    # And to deal with incorrect reverse parsing from the HDLConv library
    # when dealing with (System)Verilog source code or some VHDL source code
    else:
        CLOCK_PORT = user_input.ask_identifiers(TOP_SRC, TOP_MODULE)
        frame.fill_box(
            CONFIG["VHDL_DIR"] + CONFIG["VHDL_BOX_FRAME"]
            if TOP_SUFFIX == ".vhd"
            else CONFIG["VERILOG_DIR"] + CONFIG["VERILOG_BOX_FRAME"],
            TOP_SRC,
            TOP_MODULE,
            get_parameters(Path(TOP_SRC), TOP_MODULE),
            CLOCK_PORT,
            CONFIG["PLACEHOLDER"],
            CONFIG["VHDL_DIR"] + CONFIG["VHDL_BOX"]
            if TOP_SUFFIX == ".vhd"
            else CONFIG["VERILOG_DIR"] + CONFIG["VERILOG_BOX"],
        )
        TOP_MODULE = "box"

    INCREMENTAL_MODE = user_input.ask_incremental_mode(STOP_STEP)

    # Directives to give to the -directive switch in
    # synth_design and eventually in place_design and route_design
    # some directives are forbidden in incremental mode
    # for place_design and route_design
    (
        SYNTHESIS_DIRECTIVE,
        PLACE_DIRECTIVE,
        ROUTE_DIRECTIVE,
    ) = user_input.ask_directives(STOP_STEP, INCREMENTAL_MODE)

    # Clock given in Mhz
    TARGET_CLOCK = user_input.ask_clock()

    # Swapping out placeholder in constraint file
    frame.fill(
        CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT_FRAME"],
        [str(1000 / TARGET_CLOCK)],
        CONFIG["PLACEHOLDER"],
        CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT"],
    )
    frame.fill_tcl(
        SRC_FOLDER,
        TOP_SRC,
        TOP_MODULE,
        SYNTHESIS_PART,
        SYNTHESIS_DIRECTIVE,
        INCREMENTAL_MODE,
        STOP_STEP,
        TOP_LANG,
        TARGET_CLOCK,
        PLACE_DIRECTIVE,
        ROUTE_DIRECTIVE,
    )
    gus.set_free_parameters(user_input.ask_parameters(TOP_SRC, TOP_MODULE))
    if TOP_LANG is RTL.VERILOG or TOP_LANG is RTL.SYSTEM_VERILOG:
        gus.set_free_parameters_range(
            user_input.ask_parameters_range(gus.FREE_PARAMETERS)
        )
    else:
        gus.set_free_parameters_range(
            dict(
                zip(
                    gus.FREE_PARAMETERS,
                    [
                        get_parameter_range(param)
                        for param in gus.FREE_PARAMETERS
                    ],
                )
            )
        )
    gus.set_metrics(
        user_input.ask_utilization_metrics(
            report.get_available_indices(
                CONFIG["VIVADO_OUTPUT_DIR"]
                + CONFIG[STOP_STEP.name + "_UTILISATION"]
            )
        )
    )
    pe.setup_evaluation(
        STOP_STEP,
        TOP_LANG,
        TO_BOX,
        TOP_MODULE,
        SRC_FOLDER,
        TOP_SRC,
        TARGET_CLOCK,
    )

    result = optimize("00:00:10")
    print("Optimization Result: " + result)

    # parameters = get_parameters(
    #     Path(TOP_SRC), SRC_MODULE if TOP_MODULE == "box" else TOP_MODULE
    # )
    # parameters = {parameter: int(parameter.value) for parameter in parameters}

    # setup_evaluation(
    #     STOP_STEP, TOP_SUFFIX, TOP_MODULE, SRC_FOLDER, TARGET_CLOCK
    # )
    # design_value = evaluate(parameters, METRICS)

    # if design_value:
    #     print("Utilization metrics: " + str(design_value.utilisation))
    #     print(
    #         "Max frequency: "
    #         + str(-design_value.negative_max_frequency)
    #         + " Mhz"
    #     )
    # else:
    #     print("Failed sourcing tcl script")
