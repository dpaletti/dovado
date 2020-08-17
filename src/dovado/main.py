import dovado.user_input as user_input
import dovado.report_parsing as report
import dovado.vivado_interaction as vivado
import dovado.frame_handling as frame
import yaml
from pathlib import Path


def main():
    # Starting Vivado in the background
    vivado.start()

    CONFIG = yaml.safe_load(Path("config.yaml").open())

    SRC_FOLDER = user_input.ask_code_dir()
    TOP_MODULE, TOP_SRC = user_input.ask_top_module(SRC_FOLDER)
    TOP_SUFFIX = Path(SRC_FOLDER + TOP_SRC).suffix
    if TOP_SUFFIX != ".vhd" and TOP_SUFFIX != ".v" and TOP_SUFFIX != ".sv":
        raise ValueError(
            "Parsed files must have .v or .vhd or .sv as a suffix not "
            + TOP_SUFFIX
        )

    SYNTHESIS_PART = user_input.ask_part()

    # STOP_STEP can take the following values:
    #  "synthesis", "implementation"
    STOP_STEP = user_input.ask_stop_step()

    # Clock and out are needed for boxing the component
    # to avoid overflowing pins
    if STOP_STEP == "implementation":
        CLOCK_PORT = user_input.ask_identifiers(TOP_SRC, TOP_MODULE)
        frame.fill_box(
            CONFIG["VHDL_DIR"] + CONFIG["VHDL_BOX_FRAME"]
            if TOP_SUFFIX == ".vhd"
            else CONFIG["VERILOG_DIR"] + CONFIG["VERILOG_BOX_FRAME"],
            TOP_SRC,
            TOP_MODULE,
            CLOCK_PORT,
            CONFIG["PLACEHOLDER"],
            CONFIG["VHDL_DIR"] + CONFIG["VHDL_BOX"]
            if TOP_SUFFIX == ".vhd"
            else CONFIG["VERILOG_DIR"] + CONFIG["VERILOG_BOX"],
        )
        TOP_MODULE = "box"

    # INCREMENTAL_MODE has the following structure:
    # {"is synthesis incremental" : boolean,
    #  "is implementation incremental" : boolean}
    # if STOP_STEP == "synthesis" the second key is absent
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
    CLOCK = user_input.ask_clock()

    # Swapping out placeholder in constraint file
    frame.fill(
        CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT_FRAME"],
        [str(1000 / CLOCK)],
        CONFIG["PLACEHOLDER"],
        CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT"],
    )

    SYNTHESIS_REPLACEMENTS = [
        CONFIG["VIVADO_OUTPUT_DIR"],
        SRC_FOLDER,
        CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT"],
        TOP_MODULE,
        SYNTHESIS_PART,
        SYNTHESIS_DIRECTIVE,
        "-incremental_synth"
        if INCREMENTAL_MODE["is synthesis incremental"]
        else "",
    ]

    IMPLEMENTATION_REPLACEMENTS = (
        []
        if STOP_STEP == "synthesis"
        else (
            [
                "",
                "-directive " + PLACE_DIRECTIVE,
                "",
                "-directive " + ROUTE_DIRECTIVE,
            ]
            if not INCREMENTAL_MODE["is implementation incremental"]
            else [
                "-directive " + PLACE_DIRECTIVE,
                " ",
                "-directive " + ROUTE_DIRECTIVE,
                " ",
            ]
        )
    )

    REPLACEMENT = (
        SYNTHESIS_REPLACEMENTS
        if STOP_STEP == "synthesis"
        else SYNTHESIS_REPLACEMENTS[:3]
        + [
            "read_vhdl -library bftLib vhdl/box.vhd"
            if TOP_SUFFIX == ".vhd"
            else "read_verilog verilog/box.vs"
        ]
        + SYNTHESIS_REPLACEMENTS[3:]
        + IMPLEMENTATION_REPLACEMENTS
    )

    # Swapping out placeholders in TCL scripts
    frame.fill(
        CONFIG["TCL_DIR"] + CONFIG[STOP_STEP.upper() + "_FRAME"],
        REPLACEMENT
        + [
            CONFIG[STOP_STEP.upper() + "_TIMING"],
            CONFIG[STOP_STEP.upper() + "_UTILISATION"],
        ],
        CONFIG["PLACEHOLDER"],
        CONFIG["TCL_DIR"] + CONFIG[STOP_STEP.upper()],
    )

    # Calling vivado to evaluate the script
    # Output of the command is ignored, it is in the return value
    vivado_out = vivado.execute_command(
        "source " + CONFIG["TCL_DIR"] + CONFIG[STOP_STEP.upper()]
    )
    print(vivado_out)

    utilization_metrics = {
        i: report.get_utilisation(
            CONFIG["UTILIZATION_METRICS"],
            CONFIG["UTILIZATION_SECTION_TITLES"],
            CONFIG["VIVADO_OUTPUT_DIR"]
            + CONFIG[STOP_STEP.upper() + "_UTILISATION"],
            "Util%",
            i,
        )
        for i in user_input.ask_utilization_metrics(
            CONFIG["UTILIZATION_METRICS"]
        )
    }

    max_frequency = 1000 / (
        (1 / 1000 * CLOCK)
        - report.get_wns(
            CONFIG["VIVADO_OUTPUT_DIR"] + CONFIG[STOP_STEP.upper() + "_TIMING"]
        )
    )

    print("Utilization metrics: " + str(utilization_metrics))
    print("Max frequency: " + str(max_frequency) + " Mhz")
