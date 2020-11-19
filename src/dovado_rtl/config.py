from pathlib import Path
import yaml

_config_dict = {
    # Directory holding tcl scripts
    "TCL_DIR": "tcl/",
    # Directory holding xdc files
    "XDC_DIR": "xdc/",
    # Directory holding vhdl files
    "VHDL_DIR": "vhdl/",
    # Directory holding verilog files
    "VERILOG_DIR": "verilog/",
    # Constraint file for setting master clock frequency
    # with blank clock to be filled
    "CONSTRAINT_FRAME": "constraint_frame.xdc",
    # Constraint file with clock filled
    "CONSTRAINT": "constraint.xdc",
    # TCL script with blank fields to be filled
    # with user input in order to evaluate vhdl source until synthesis
    "SYNTHESIS_FRAME": "synthesis_frame.tcl",
    # TCL script with all fields filled with user input until synthesis
    "SYNTHESIS": "synthesis.tcl",
    # TCL script with blank fields to be filled
    # with user input in order to evaluate vhdl source
    "IMPLEMENTATION_FRAME": "implementation_frame.tcl",
    # TCL script with all fields filled with user input
    "IMPLEMENTATION": "implementation.tcl",
    # Local copy of VHDL top module source where parameters are changed in place.
    # This is used if stop step is synthesis
    # Reverse parsing does not work for (System)Verilog so no such file
    # exists for the (System)Verilog case which is instead always boxed
    "VHDL_LOCAL_SRC": "dovado_work_file.vhd",
    # Vhdl file with fields to be filled for boxing
    "VHDL_BOX_FRAME": "box_frame.vhd",
    # Vhdl file with all fields filled
    "VHDL_BOX": "box.vhd",
    # TODO remove this or understand its possible role
    # Verilog local source
    "VERILOG_LOCAL_SRC": "dovado_work_file.sv",
    # Verilog file with fields to be filled for boxing
    "VERILOG_BOX_FRAME": "box_frame.sv",
    # Verilog file with all fields filled
    "VERILOG_BOX": "box.sv",
    # Placeholder inside the two above files
    # to be swapped with user input
    "PLACEHOLDER": "____",
    # Output of vivado call (reports and checkpoints)
    "VIVADO_OUTPUT_DIR": "vivado_out/",
    # After Synthesis Utilisation Report Name
    "SYNTHESIS_UTILISATION": "post_synth_util.xml",
    # After Implementation Utilisation Report Name
    "IMPLEMENTATION_UTILISATION": "post_impl_util.xml",
    # After Synthesis Timing (setup) Report Name
    "SYNTHESIS_TIMING": "post_synth_setup_timing.rpt",
    # After Implementation Timing (setup) Report Name
    "IMPLEMENTATION_TIMING": "post_impl_setup_timing.rpt",
    # Maximum integer value considered for RTL parameters
    "INTEGER_HIGH": 2147483647,
    # Initial sample size for the estimator
    "INITIAL_SAMPLES": 100,
    # N-parameter to choose which example to calculate the distance from
    "N": 3,
    # Run time set as a constraint for the genetic algorithm, format "hh:mm:ss"
    "GENETIC_RUN_TIME": "00:30:00",
}

custom_configuration_checked = False
configuration_exists = False


def get_config(config_name: str):
    global custom_configuration_checked
    global configuration_exists
    if not custom_configuration_checked:
        custom_configuration_checked = True
        try:
            CONFIG = yaml.safe_load(Path("config.yaml").open())
            configuration_exists = True
        except:
            configuration_exists = False
    if configuration_exists:
        try:
            return CONFIG[config_name]
        except:
            return _config_dict[config_name]
    else:
        return _config_dict[config_name]
