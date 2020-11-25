import re
from pathlib import Path
from typing import List, Optional
from dovado_rtl.src_parsing import SourceFile
from dovado_rtl.config import Configuration
from dovado_rtl.antlr.HdlRepresentation import (
    Parameter,
    Port,
    TopLevel,
)
from dovado_rtl.utility_classes import RTL, StopStep, IsIncremental


class FrameHandler:
    def __init__(self, placeholder: str):
        self.placeholder = placeholder

    def fill(self, frame_path, replacements, out_path):
        out = re.sub(
            self.placeholder,
            lambda m, r=iter(replacements): next(r),
            Path(frame_path).open("r").read(),
        )
        Path(out_path).write_text(out)


class XdcFrameHandler(FrameHandler):
    def __init__(
        self,
        placeholder: str,
        frame_path: str,
        target_clock: float,
        out_path: str,
    ):
        self.frame_path: str = frame_path
        self.target_clock: float = target_clock
        self.out_path: str = out_path
        FrameHandler.__init__(self, placeholder)

    def fill_xdc(self):
        self.fill(self.frame_path, [str(self.target_clock)], self.out_path)


class TclFrameHandler(FrameHandler):
    def __init__(
        self,
        config: Configuration,
        parsed_source: SourceFile,
        is_boxed: bool,
        synthesis_part: str,
        synthesis_directive: str,
        incremental_mode: IsIncremental,
        stop_step: StopStep,
        place_directive=None,
        route_directive=None,
    ):
        self.parsed_source: SourceFile = parsed_source
        self.is_boxed: bool = is_boxed
        self.synthesis_part: str = synthesis_part
        self.synthesis_directive: str = synthesis_directive
        self.incremental_mode: IsIncremental = incremental_mode
        self.stop_step: StopStep = stop_step
        self.place_directive: Optional[str] = place_directive
        self.route_directive: Optional[str] = route_directive
        self.config: Configuration = config

        FrameHandler.__init__(self, config.get_config("PLACEHOLDER"))

    def fill_tcl(self):
        top_lang: RTL = self.parsed_source.get_hdl()
        print("TOP LANG: " + str(top_lang))
        synthesis_replacements = [
            self.config.get_config("VIVADO_OUTPUT_DIR"),
            self.parsed_source.get_folder(),
            self.config.get_config("XDC_DIR")
            + self.config.get_config("CONSTRAINT"),
            (
                "read_vhdl -library bftLib "
                + self.config.get_config("VHDL_DIR")
                + self.config.get_config("VHDL_BOX")
            )
            if top_lang is RTL.VHDL
            else (
                "read_verilog "
                + self.config.get_config("VERILOG_DIR")
                + self.config.get_config("VERILOG_BOX")
            ),
            (
                "set_property IS_ENABLED 0 [get_files "
                + self.parsed_source.get_path()
                + "]"
            )
            if top_lang is RTL.VHDL
            else "# no disabling needed",
            self.parsed_source.get_path() if not self.is_boxed else "box",
            self.synthesis_part,
            self.synthesis_directive,
            "-incremental_synth" if self.incremental_mode.synthesis else "",
        ]
        print("SYNTHESIS REPLACEMENTS: " + str(synthesis_replacements))

        implementation_replacements = (
            []
            if self.stop_step is StopStep.SYNTHESIS
            else (
                [
                    "",
                    "-directive " + self.place_directive,
                    "",
                    "-directive " + self.route_directive,
                ]
                if not self.incremental_mode.implementation
                else [
                    "-directive " + self.place_directive,
                    " ",
                    "-directive " + self.route_directive,
                    " ",
                ]
            )
        )

        replacements = (
            synthesis_replacements
            if self.stop_step is StopStep.SYNTHESIS
            else synthesis_replacements[:3]
            + [
                (
                    "read_vhdl -library bftLib "
                    + self.config.get_config("VHDL_DIR")
                    + self.config.get_config("VHDL_BOX")
                )
                if top_lang is RTL.VHDL
                else (
                    "read_verilog "
                    + self.config.get_config("VERILOG_DIR")
                    + self.config.get_config("VERILOG_BOX")
                )
            ]
            + synthesis_replacements[5:]
            + implementation_replacements
        )

        print("REPLACEMENTS: " + str(replacements))
        self.fill(
            self.config.get_config("TCL_DIR")
            + self.config.get_config(self.stop_step.name + "_FRAME"),
            replacements
            + [
                self.config.get_config(self.stop_step.name + "_TIMING"),
                self.config.get_config(self.stop_step.name + "_UTILISATION"),
            ],
            self.config.get_config("TCL_DIR")
            + self.config.get_config(self.stop_step.name),
        )

    def setup_incremental(self, is_incremental: IsIncremental):
        if not is_incremental.synthesis and not is_incremental.implementation:
            return
        if is_incremental.synthesis:
            path = self.config.get_config("TCL_DIR") + self.config.get_config(
                "SYNTHESIS"
            )
            synthesis = Path(path).read_text()
            synthesis = synthesis.replace("#! ", "")
            Path(path).write_text(synthesis)
        if is_incremental.implementation:
            path = self.config.get_config("TCL_DIR") + self.config.get_config(
                "IMPLEMENTATION"
            )
            implementation = Path(path).read_text()
            implementation = implementation.replace("#! ", "")
            Path(path).write_text(implementation)


class HdlBoxFrameHandler(FrameHandler):
    def __init__(
        self,
        placeholder: str,
        frame_path: str,
        top_module: str,
        ports: List[Port],
        clock_port: Port,
        out_path: str,
        hdl: RTL,
        top_level: TopLevel = None,
    ):
        self.frame_path: str = frame_path
        self.top_module: str = top_module
        self.ports: List[Port] = ports
        self.clock_port: Port = clock_port
        self.out_path: str = out_path
        self.top_level: TopLevel = top_level
        self.hdl: RTL = hdl

        FrameHandler.__init__(self, placeholder)

    def fill_box(
        self, parameters: List[Parameter],
    ):
        libraries = self.top_level.get_libraries()
        imports = self.top_level.get_use_clauses()

        if self.hdl is RTL.VHDL:
            self.__vhdl_fill_box(parameters, libraries, imports)
        else:
            self.__verilog_fill_box(parameters)

    @staticmethod
    def __vhdl_parameter_map(parameters):
        parameter_section = "generic map(\n"
        for parameter in parameters[:-1]:
            if not parameter.value:
                raise Exception(
                    "Please provide default values for all parameters, "
                    + str(parameter.name)
                    + " does not have one."
                )
            parameter_section += (
                parameter.name
                + " => "
                + (
                    str(parameter.value)
                    if not parameter.value.base
                    else str(
                        int(parameter.value.val[1:], parameter.value.base,)
                    )
                ).strip()
                + ",\n"
            )
        parameter_section += (
            parameters[-1].name
            + " => "
            + (
                str(parameters[-1].value)
                if not parameters[-1].value.base
                else str(
                    int(
                        parameters[-1].value.val[1:],
                        parameters[-1].value.base,
                    )
                )
            )
            + ")"
        )
        return parameter_section

    def __vhdl_fill_box(
        self,
        parameters: List[Parameter],
        libraries: List[str],
        imports: List[str],
    ):
        input_mapping = [
            port.get_name()
            + (
                " => '1',\n"
                if port.get_type() == "std_logic"
                else " => " + port.get_type() + "'((others => '1')),\n"
            )
            for port in self.ports
            if (
                port.get_direction().upper() == "IN"
                and port.get_name() != self.clock_port.get_name()
            )
        ]
        input_mapping[len(input_mapping) - 1] = input_mapping[
            len(input_mapping) - 1
        ].replace(",", "")
        replacements = [
            "".join(
                ["library " + lib + ";\n" for lib in libraries]
                + ["use " + imp + ";\n" for imp in imports]
            ),
            "Work." + self.top_module,
            self.__vhdl_parameter_map(parameters),
            self.clock_port.get_name(),
            "".join(input_mapping),
        ]
        self.fill(self.frame_path, replacements, self.out_path)

    @staticmethod
    def __verilog_parameter_map(parameters):
        parameter_section = "#(\n"
        for parameter in parameters[:-1]:
            parameter_section += (
                "."
                + parameter.name
                + "("
                + str(int(str(parameter.value.val), parameter.value.base))
                + "),\n"
            )
        parameter_section += (
            "."
            + parameters[-1].name
            + "("
            + str(
                int(str(parameters[-1].value.val), parameters[-1].value.base,)
            )
            + ")\n)\n"
        )
        return parameter_section

    def __verilog_fill_box(
        self, parameters,
    ):
        input_mapping = [
            "." + port.get_name() + " ('1),\n"
            for port in self.ports
            if (
                port.get_direction() == "input"
                and port.get_name() != self.clock_port.get_name()
            )
        ]

        input_mapping[len(input_mapping) - 1] = input_mapping[
            len(input_mapping) - 1
        ].replace(",", "")

        replacements = [
            self.top_module,
            self.__verilog_parameter_map(parameters),
            self.clock_port.get_name(),
            "".join(input_mapping),
        ]

        self.fill(self.frame_path, replacements, self.out_path)
