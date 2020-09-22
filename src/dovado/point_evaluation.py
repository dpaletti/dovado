import yaml
from pathlib import Path
from dataclasses import dataclass
import dovado.vivado_interaction as vivado
import dovado.report_parsing as report
import dovado.user_input as user_input
import dovado.src_parsing as src

CONFIG = yaml.safe_load(Path("config.yaml").open())


@dataclass
class DesignPoint:
    utilisation: dict
    wns: float


def evaluate(parameters, stop_step, top_suffix, top_module, src_folder):
    if stop_step == "synthesis" and not (
        top_suffix == ".sv" or top_suffix == ".v"
    ):
        for parameter, value in parameters.items():
            src.set_parameter(
                Path(src_folder + CONFIG["VHDL_LOCAL_SRC"]),
                top_module,
                parameter,
                value,
            )
    else:
        for parameter, value in parameters.items():
            src.map_parameter(
                Path(CONFIG["VHDL_DIR"] + CONFIG["VHDL_BOX"])
                if top_suffix == ".vhd"
                else Path(CONFIG["VERILOG_DIR"] + CONFIG["VERILOG_BOX"]),
                top_module,
                parameter,
                value,
            )
    vivado_out, success = vivado.source(
        CONFIG["TCL_DIR"] + CONFIG[stop_step.upper()]
    )
    print(vivado_out)
    return (
        None
        if not success
        else DesignPoint(
            utilisation={
                i: report.get_utilisation(
                    CONFIG["VIVADO_OUTPUT_DIR"]
                    + CONFIG[stop_step.upper() + "_UTILISATION"],
                    i[0],
                    i[1],
                )
                for i in user_input.ask_utilization_metrics(
                    report.get_available_indices(
                        CONFIG["VIVADO_OUTPUT_DIR"]
                        + CONFIG[stop_step.upper() + "_UTILISATION"]
                    )
                )
            },
            wns=report.get_wns(
                CONFIG["VIVADO_OUTPUT_DIR"]
                + CONFIG[stop_step.upper() + "_TIMING"]
            ),
        )
    )


def get_max_frequency(wns, target_clock):

    return (1000 / ((1 / 1000 * target_clock) - wns),)
