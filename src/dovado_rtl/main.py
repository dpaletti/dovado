import dovado_rtl.user_input as user_input
from dovado_rtl.config import get_config
import dovado_rtl.vivado_interaction as vivado
import dovado_rtl.frame_handling as frame
from dovado_rtl.genetic_algorithm import optimize
from dovado_rtl.src_parsing import is_to_box, RTL
import dovado_rtl.global_user_selections as gus
import dovado_rtl.point_evaluation as pe
import dovado_rtl.estimation as es
import dovado_rtl.fitness as fit
import yaml
from pathlib import Path


def main():
    # Starting Vivado in the background
    vivado.start()

    SRC_FOLDER = user_input.ask_code_dir()
    TOP_MODULE, TOP_SRC = user_input.ask_top_module(SRC_FOLDER)
    TOP_SUFFIX = Path(SRC_FOLDER + TOP_SRC).suffix
    if TOP_SUFFIX == ".vhd" or TOP_SUFFIX == ".vhdl":
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
    print("Current Language: " + str(TOP_LANG))
    SYNTHESIS_PART = user_input.ask_part()

    # STOP_STEP can take the following values:
    #  "synthesis", "implementation"
    STOP_STEP = user_input.ask_stop_step()

    TO_BOX = is_to_box(Path(TOP_SRC), STOP_STEP)

    gus.set_free_parameters(user_input.ask_parameters(TOP_SRC, TOP_MODULE))

    # A local copy of the top module source file is needed
    # in order to update the parameters in place
    if not TO_BOX:
        with Path(
            SRC_FOLDER + get_config("VHDL_LOCAL_SRC")
            if TOP_SUFFIX == ".vhd"
            else SRC_FOLDER + get_config("VERILOG_LOCAL_SRC")
        ).open("w+") as f:
            f.write(Path(TOP_SRC).read_text())

    # Clock and out are needed for boxing the component
    # to avoid overflowing pins
    # And to deal with incorrect reverse parsing from the HDLConv library
    # when dealing with (System)Verilog source code or some VHDL source code
    else:
        CLOCK_PORT = user_input.ask_identifiers(TOP_SRC, TOP_MODULE)
        frame.fill_box(
            get_config("VHDL_DIR") + get_config("VHDL_BOX_FRAME")
            if TOP_SUFFIX == ".vhd"
            else get_config("VERILOG_DIR") + get_config("VERILOG_BOX_FRAME"),
            TOP_SRC,
            TOP_MODULE,
            gus.FREE_PARAMETERS,
            CLOCK_PORT,
            get_config("PLACEHOLDER"),
            get_config("VHDL_DIR") + get_config("VHDL_BOX")
            if TOP_SUFFIX == ".vhd"
            else get_config("VERILOG_DIR") + get_config("VERILOG_BOX"),
        )

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
        get_config("XDC_DIR") + get_config("CONSTRAINT_FRAME"),
        [str(1000 / TARGET_CLOCK)],
        get_config("PLACEHOLDER"),
        get_config("XDC_DIR") + get_config("CONSTRAINT"),
    )
    frame.fill_tcl(
        SRC_FOLDER,
        TOP_SRC,
        TOP_MODULE,
        TO_BOX,
        SYNTHESIS_PART,
        SYNTHESIS_DIRECTIVE,
        INCREMENTAL_MODE,
        STOP_STEP,
        TOP_LANG,
        TARGET_CLOCK,
        PLACE_DIRECTIVE,
        ROUTE_DIRECTIVE,
    )

    pe.setup_evaluation(
        STOP_STEP,
        TOP_LANG,
        TO_BOX,
        TOP_MODULE,
        SRC_FOLDER,
        TOP_SRC,
        TARGET_CLOCK,
        INCREMENTAL_MODE,
    )
    if user_input.ask_is_point_evaluation():
        print(
            pe.evaluate(
                tuple(user_input.ask_parameters_value(gus.FREE_PARAMETERS))
            )
        )

    else:
        gus.set_free_parameters_range(
            user_input.ask_parameters_range(gus.FREE_PARAMETERS)
        )
        es.generate_dataset(
            get_config("INITIAL_SAMPLES"),
            gus.FREE_PARAMETERS_RANGE,
            gus.FREE_PARAMETERS,
        )
        fit.set_threshold(es.examples)

        result = optimize(get_config("GENETIC_RUN_TIME"))
        print("Optimization Result: " + str(result))
