import tcl_completion_and_execution as tcae
import report_parser as rp

# TCL script with blank fields to be filled
# with user input in order to evaluate vhdl source
TCL_VHDL_EVALUATE_SCRIPT_PATH = "./tcl/vhdl_evaluate_point_frame.tcl"

# TCL script with blank fields to be filled
# with user input in order to evaluate verilog source
TCL_VERILOG_EVALUATE_SCRIPT_PATH = "./tcl/verilog_evaluate_point_frame.tcl"

# Placeholder inside the two above files
# to be swapped with user input
PLACEHOLDER = "____"

# TCL script with all fields filled with user input
TCL_OUTPUT_SCRIPT_PATH = "./tcl/full_evalutate_point_frame.tcl"

# Output of vivado call (reports and checkpoints)
VIVADO_OUTPUT_DIR = "./vivado_out/"

# Utilisation Report Name
# add this to VIVADO_OUTPUT_DIR to get its path
VIVADO_UTILISATION_REPORT_NAME = "post_synth_util.xml"

# Timing (setup) Report Name
# add this to VIVADO_OUTPUT_DIR to get its path
VIVADO_TIMING_SETUP_REPORT_NAME = "post_synth_setup_timing.rpt"

# Security measures against buffer overflows
MAXIMUM_TOP_MODULE_LENGTH = 100
MAXIMUM_PART_IDENTIFIER_LENGTH = 100

# Asking user for input
RTL_FILE_PATH = tcae.request_file("RTL", ".*\\.vhl|.*\\.v", ".vhl or .v")
CONSTRAINTS_FILE_PATH = tcae.request_file("Constraint", ".*\\.xdc", ".xdc")
TOP_MODULE = tcae.request_identifier("top module", MAXIMUM_TOP_MODULE_LENGTH)
SYNTH_PART = tcae.request_identifier("part", MAXIMUM_PART_IDENTIFIER_LENGTH)

# Inferring chosen RTL language from file extension
SRC_LANG = tcae.get_src_lang(RTL_FILE_PATH)

# Swapping out placeholders in TCL scripts
tcae.write_tcl_evaluation_script([VIVADO_OUTPUT_DIR, RTL_FILE_PATH,
                                  CONSTRAINTS_FILE_PATH, TOP_MODULE,
                                  SYNTH_PART, VIVADO_TIMING_SETUP_REPORT_NAME,
                                  VIVADO_UTILISATION_REPORT_NAME],
                                 SRC_LANG,
                                 TCL_VHDL_EVALUATE_SCRIPT_PATH,
                                 TCL_VERILOG_EVALUATE_SCRIPT_PATH,
                                 PLACEHOLDER, TCL_OUTPUT_SCRIPT_PATH)

# Calling vivado to evaluate the script
tcae.evaluate_tcl_script(TCL_OUTPUT_SCRIPT_PATH)

# Reading utilisation and timing from reports
slice_lut_perc_util = rp.get_utilisation(VIVADO_OUTPUT_DIR +
                                         VIVADO_UTILISATION_REPORT_NAME,
                                         "Slice Logic",
                                         "Util%",
                                         "Slice LUTs*")
wns = rp.get_wns_whs(VIVADO_OUTPUT_DIR + VIVADO_TIMING_SETUP_REPORT_NAME)
print("\nWNS: " + str(wns) + "ns" + "\nPercentual Utilisation of LUTs: "
      + str(slice_lut_perc_util) + "%")
