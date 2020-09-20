import yaml
from pathlib import Path
from dataclasses import dataclass
import dovado.frame_handling as frame
import dovado.vivado_interaction as vivado
import dovado.report_parsing as report
import dovado.user_input as user_input

CONFIG = yaml.safe_load(Path("config.yaml").open())


@dataclass
class DesignPoint:
    utilisation: dict
    max_frequency: float


def evaluate(design_point, evaluation_setup):

    SYNTHESIS_REPLACEMENTS = [
        CONFIG["VIVADO_OUTPUT_DIR"],
        evaluation_setup.src_folder,
        CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT"],
        evaluation_setup.top_module,
        evaluation_setup.synthesis_part,
        evaluation_setup.synthesis_directive,
        "-incremental_synth"
        if evaluation_setup.incremental_mode["is synthesis incremental"]
        else "",
    ]

    IMPLEMENTATION_REPLACEMENTS = (
        []
        if evaluation_setup.stop_step == "synthesis"
        else (
            [
                "",
                "-directive " + evaluation_setup.place_directive,
                "",
                "-directive " + evaluation_setup.route_directive,
            ]
            if not evaluation_setup.incremental_mode[
                "is implementation incremental"
            ]
            else [
                "-directive " + evaluation_setup.place_directive,
                " ",
                "-directive " + evaluation_setup.route_directive,
                " ",
            ]
        )
    )

    REPLACEMENT = (
        SYNTHESIS_REPLACEMENTS
        if evaluation_setup.stop_step == "synthesis"
        else SYNTHESIS_REPLACEMENTS[:3]
        + [
            "read_vhdl -library bftLib vhdl/box.vhd"
            if evaluation_setup.top_suffix == ".vhd"
            else "read_verilog verilog/box.vs"
        ]
        + SYNTHESIS_REPLACEMENTS[3:]
        + IMPLEMENTATION_REPLACEMENTS
    )

    frame.fill(
        CONFIG["TCL_DIR"]
        + CONFIG[evaluation_setup.stop_step.upper() + "_FRAME"],
        REPLACEMENT
        + [
            CONFIG[evaluation_setup.stop_step.upper() + "_TIMING"],
            CONFIG[evaluation_setup.stop_step.upper() + "_UTILISATION"],
        ],
        CONFIG["PLACEHOLDER"],
        CONFIG["TCL_DIR"] + CONFIG[evaluation_setup.stop_step.upper()],
    )

    # Calling vivado to evaluate the script
    # Output of the command is ignored, it is in the return value
    vivado_out, success = vivado.source(
        CONFIG["TCL_DIR"] + CONFIG[evaluation_setup.stop_step.upper()]
    )
    print(vivado_out)
    return (
        None
        if not success
        else DesignPoint(
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
            max_frequency=1000
            / (
                (1 / 1000 * evaluation_setup.target_clock)
                - report.get_wns(
                    CONFIG["VIVADO_OUTPUT_DIR"]
                    + CONFIG[evaluation_setup.stop_step.upper() + "_TIMING"]
                )
            ),
        )
    )
