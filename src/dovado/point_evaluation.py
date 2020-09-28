import yaml
from functools import lru_cache
from pathlib import Path
from dataclasses import dataclass
import dovado.vivado_interaction as vivado
import dovado.report_parsing as report
import dovado.user_input as user_input
import dovado.src_parsing as src

CONFIG = yaml.safe_load(Path("config.yaml").open())


@dataclass
class EvaluationSetup:
    stop_step: str
    top_suffix: str
    top_module: str
    src_folder: str
    target_clock: float


@dataclass
class DesignValue:
    utilisation: dict
    max_frequency: float


evaluation_setup = None
is_evaluation_setup = False


def setup_evaluation(
    stop_step, top_suffix, top_module, src_folder, target_clock
):
    global is_evaluation_setup
    if is_evaluation_setup:
        return
    global evaluation_setup
    evaluation_setup = EvaluationSetup(
        stop_step, top_suffix, top_module, src_folder, target_clock
    )
    is_evaluation_setup = True


@lru_cache
def evaluate(design_point):
    if evaluation_setup.stop_step == "synthesis" and not (
        evaluation_setup.top_suffix == ".sv"
        or evaluation_setup.top_suffix == ".v"
    ):
        for parameter, value in design_point.items():
            src.set_parameter(
                Path(evaluation_setup.src_folder + CONFIG["VHDL_LOCAL_SRC"]),
                evaluation_setup.top_module,
                parameter,
                value,
            )
    else:
        for parameter, value in design_point.items():
            src.map_parameter(
                Path(CONFIG["VHDL_DIR"] + CONFIG["VHDL_BOX"])
                if evaluation_setup.top_suffix == ".vhd"
                else Path(CONFIG["VERILOG_DIR"] + CONFIG["VERILOG_BOX"]),
                evaluation_setup.top_module,
                parameter,
                value,
            )
    vivado_out, success = vivado.source(
        CONFIG["TCL_DIR"] + CONFIG[evaluation_setup.stop_step.upper()]
    )
    print(vivado_out)
    return (
        None
        if not success
        else DesignValue(
            utilisation={
                i: report.get_utilisation(
                    CONFIG["VIVADO_OUTPUT_DIR"]
                    + CONFIG[
                        evaluation_setup.stop_step.upper() + "_UTILISATION"
                    ],
                    i[0],
                    i[1],
                )
                for i in user_input.ask_utilization_metrics(
                    report.get_available_indices(
                        CONFIG["VIVADO_OUTPUT_DIR"]
                        + CONFIG[
                            evaluation_setup.stop_step.upper() + "_UTILISATION"
                        ]
                    )
                )
            },
            max_frequency=get_max_frequency(
                report.get_wns(
                    CONFIG["VIVADO_OUTPUT_DIR"]
                    + CONFIG[evaluation_setup.stop_step.upper() + "_TIMING"]
                )
            ),
        )
    )


def get_max_frequency(wns):

    return (1000 / ((1 / 1000 * evaluation_setup.target_clock) - wns),)
