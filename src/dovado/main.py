import dovado.user_input as user_input
import dovado.tcl_parsing as tcl
import dovado.report_parsing as report
import dovado.vivado_interaction as vivado
import yaml
from pathlib import Path


def main():
    # Starting Vivado in the background
    vivado.start()

    CONFIG = yaml.safe_load(Path("config.yaml").open())

    SRC_FOLDER = user_input.request_code_dir()
    TOP_MODULE = user_input.request_top_module(SRC_FOLDER)

    SYNTHESIS_PART = user_input.request_part()

    # STOP_STEP can take the following values:
    #  "synthesis", "implementation"
    STOP_STEP = user_input.request_stop_step()

    # INCREMENTAL_MODE has the following structure:
    # {"is synthesis incremental" : boolean,
    #  "is implementation incremental" : boolean}
    # if STOP_STEP == "synthesis" the second key is absent
    INCREMENTAL_MODE = user_input.request_incremental_mode(STOP_STEP)

    # Directives to give to the -directive switch in
    # synth_design and eventually in place_design and route_design
    # some directives are forbidden in incremental mode
    # for place_design and route_design
    (
        SYNTHESIS_DIRECTIVES,
        PLACE_DIRECTIVES,
        ROUTE_DIRECTIVES,
    ) = user_input.request_directives(STOP_STEP, INCREMENTAL_MODE)

    CLOCK = user_input.request_clock()

    # Swapping out placeholder in constraint file
    tcl.fill_frame(
        CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT_FRAME"],
        [str(1000 / CLOCK)],
        CONFIG["PLACEHOLDER"],
        CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT"],
    )

    # Swapping out placeholders in TCL scripts
    # TODO start debugging from here, above still needs much testing, maybe start writing tests
    # here how to mock user input https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
    # use pytest for tests
    tcl.fill_frame(
        CONFIG["TCL_DIR"] + CONFIG[STOP_STEP.upper() + "_FRAME"],
        [
            CONFIG["VIVADO_OUTPUT_DIR"],
            SRC_FOLDER,
            CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT"],
            TOP_MODULE,
            SYNTHESIS_PART,
            CONFIG[STOP_STEP.upper() + "_TIMING"],
            CONFIG[STOP_STEP.upper() + "_UTILISATION"],
        ],
        CONFIG["PLACEHOLDER"],
        CONFIG[STOP_STEP.upper()],
    )

    # Calling vivado to evaluate the script
    vivado.execute_command("source " + CONFIG[STOP_STEP.upper()])

    utilization_metrics = {
        i: report.get_utilisation(
            CONFIG["UTILIZATION METRICS"],
            CONFIG["UTILIZATION_SECTION_TITLES"],
            CONFIG["VIVADO_OUTPUT_DIR"]
            + CONFIG[STOP_STEP.upper() + "UTILISATION"],
            "Util%",
            i,
        )
        for i in user_input.request_utilization_metrics()
    }

    max_frequency = report.get_wns(
        CONFIG["VIVADO_OUTPUT_DIR"] + CONFIG["VIVADO_TIMING_SETUP_REPORT_NAME"]
    )
    print("Utilization metrics: " + str(utilization_metrics))
    print("Max frequency: " + str(max_frequency))
