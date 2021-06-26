from pathlib import Path
from typing import Dict, Union
import yaml


class Configuration:
    __config_dict = {
        # Dovado Working Dir
        # This directory will be created in the same directory
        # in which the "dovado" command is executed
        "WORK_DIR": "dovado_work/",
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
        # Vhdl file with fields to be filled for boxing
        "VHDL_BOX_FRAME": "box_frame.vhd",
        # Vhdl file with all fields filled
        "VHDL_BOX": "box.vhd",
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
        # Run time set as a constraint for the genetic algorithm, format "hh:mm:ss"
        "GENETIC_RUN_TIME": "04:00:00",
    }

    def __init__(self):
        config_path = Path("dovado.yaml")
        self.config: Dict[str, Union[str, int]] = yaml.safe_load(
            config_path.open()
        ) if config_path.is_file() else self.__config_dict

    def get_config(self, config_name: str):
        if config_name in self.config:
            return self.config[config_name]
        else:
            return self.__config_dict[config_name]
