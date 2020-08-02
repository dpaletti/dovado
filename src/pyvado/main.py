import pyvado.tcl_completion_and_execution as tcae
import pyvado.report_parser as rp
import yaml
from pathlib import Path


def main():
    # Importing config
    config = yaml.safe_load(Path("config.yaml").open())

    # Asking user for input
    RTL_FILE_PATH = tcae.request_file("RTL", ".*\\.vhl|.*\\.v", ".vhl or .v")
    CONSTRAINTS_FILE_PATH = tcae.request_file("Constraint", ".*\\.xdc", ".xdc")
    TOP_MODULE = tcae.request_identifier("top module", config["MAXIMUM_TOP_MODULE_LENGTH"])
    SYNTH_PART = tcae.request_identifier("part", config["MAXIMUM_PART_IDENTIFIER_LENGTH"])

    # Inferring chosen RTL language from file extension
    SRC_LANG = tcae.get_src_lang(RTL_FILE_PATH)

    # Swapping out placeholders in TCL scripts
    tcae.write_tcl_evaluation_script([config["VIVADO_OUTPUT_DIR"],
                                      RTL_FILE_PATH,
                                      CONSTRAINTS_FILE_PATH, TOP_MODULE,
                                      SYNTH_PART,
                                      config["VIVADO_TIMING_SETUP_REPORT_NAME"],
                                      config["VIVADO_UTILISATION_REPORT_NAME"]],
                                     SRC_LANG,
                                     config["TCL_VHDL_EVALUATE_SCRIPT_PATH"],
                                     config["TCL_VERILOG_EVALUATE_SCRIPT_PATH"],
                                     config["PLACEHOLDER"],
                                     config["TCL_OUTPUT_SCRIPT_PATH"])


    # Calling vivado to evaluate the script
    tcae.evaluate_tcl_script(config["TCL_OUTPUT_SCRIPT_PATH"])

    # Reading utilisation and timing from reports
    slice_lut_perc_util = rp.get_utilisation(config["VIVADO_OUTPUT_DIR"] +
                                             config[
                                                 "VIVADO_UTILISATION_REPORT_NAME"],
                                             "Slice Logic",
                                             "Util%",
                                             "Slice LUTs*")
    wns = rp.get_wns_whs(config["VIVADO_OUTPUT_DIR"]
                         + config["VIVADO_TIMING_SETUP_REPORT_NAME"])
    print("\nWNS: " + str(wns) + "ns" + "\nPercentual Utilisation of LUTs: "
          + str(slice_lut_perc_util) + "%")
