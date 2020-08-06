import dovado.user_input as user_input
import dovado.tcl_parsing as tcl
import dovado.report_parser as report
import dovado.vivado_interaction as vivado
import yaml
from pathlib import Path
import sys


def main():
    # Starting Vivado in the background
    vivado.start()

    CONFIG = yaml.safe_load(Path("config.yaml").open())

    SRC_FOLDER = user_input.request_code_dir()
    TOP_MODULE = user_input.request_top_module(SRC_FOLDER)

    if vivado.expect("Vivado%") != 0:
        sys.exit("Could not start Vivado")

    SYNTH_PART = user_input.request_part()

    # either "synthesis" or "implementation"
    STOP_STEP = user_input.request_synth_step()

    # {"is synthesis incremental" : boolean,
    #  "is implementation incremental" : boolean}
    # if STOP_SETP = "synthesis" the second key is absent
    INCREMENTAL_MODE = user_input.request_incremental_mode()
    # Swapping out placeholders in TCL scripts
    tcl.fill_frame(
        CONFIG["SYNTHESIS_FRAME_SCRIPT_PATH"][
            CONFIG["VIVADO_OUTPUT_DIR"],
            SRC_FOLDER,
            CONFIG["CONSTRAINTS_FILE_PATH"],
            TOP_MODULE,
            SYNTH_PART,
            CONFIG["VIVADO_TIMING_SETUP_REPORT_NAME"],
            CONFIG["VIVADO_UTILISATION_REPORT_NAME"],
        ],
        CONFIG["PLACEHOLDER"],
        CONFIG["SYNTHESIS_SCRIPT_PATH"],
    )

    # Calling vivado to evaluate the script
    vivado.communicate("source " + CONFIG["SYNTHESIS_SCRIPT_PATH"])
    utilization_metrics = {
        i: report.get_utilisation(
            CONFIG["UTILIZATION METRICS"],
            CONFIG["UTILIZATION_SECTION_TITLES"],
            CONFIG["VIVADO_OUTPUT_DIR"]
            + CONFIG["VIVADO_UTILISATION" + "_REPORT_NAME"],
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
