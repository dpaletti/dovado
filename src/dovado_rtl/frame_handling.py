from pathlib import Path
from typing import List, Optional
from dovado_rtl.src_parsing import SourceParser
from dovado_rtl.config import Configuration
from dovado_rtl.antlr.hdl_representation import (
    Parameter,
    Port,
    PortDirectionEnum,
    PortTypeEnum,
)
from dovado_rtl.enums import RTL, StopStep
from dovado_rtl.simple_types import IsIncremental
from dovado_rtl.fill_handler import FillHandler


class XdcFrameHandler(FillHandler):
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
        FillHandler.__init__(self, placeholder, frame_path, out_path)

    def fill(self) -> bool:
        self.replacements = [str(self.target_clock)]
        return super().fill()


class TclFrameHandler(FillHandler):
    def __init__(
        self,
        config: Configuration,
        parsed_source: SourceParser,
        base_folder: str,
        synthesis_part: str,
        synthesis_directive: str,
        incremental_mode: IsIncremental,
        stop_step: StopStep,
        place_directive: Optional[str] = None,
        route_directive: Optional[str] = None,
    ):
        self.parsed_source: SourceParser = parsed_source
        self.base_folder: str = base_folder
        self.synthesis_part: str = synthesis_part
        self.synthesis_directive: str = synthesis_directive
        self.incremental_mode: IsIncremental = incremental_mode
        self.stop_step: StopStep = stop_step
        self.place_directive: Optional[str] = place_directive
        self.route_directive: Optional[str] = route_directive
        self.config: Configuration = config

        FillHandler.__init__(
            self,
            str(config.get_config("PLACEHOLDER")),
            str(self.config.get_config("TCL_DIR"))
            + str(self.config.get_config(self.stop_step.name + "_FRAME")),
            str(self.config.get_config("WORK_DIR"))
            + str(self.config.get_config(self.stop_step.name)),
        )

    def fill(self) -> bool:
        top_lang: RTL = self.parsed_source.get_hdl()
        is_library = self.parsed_source.is_library_project()
        user_libs = "{"
        folder = ""
        if is_library:
            for lib in self.parsed_source.get_user_defined_libs():
                user_libs += " " + lib
        else:
            folder = self.parsed_source.get_folder()
            user_libs += " " + folder
        user_libs += " }"

        synthesis_replacements: List[str] = [
            str(self.config.get_config("WORK_DIR")),
            self.base_folder,
            str(self.config.get_config("WORK_DIR"))
            + str(self.config.get_config("CONSTRAINT")),
            user_libs,
            (
                "read_vhdl -library "
                + ("dovado " if is_library else (folder + " "))
                + str(self.config.get_config("WORK_DIR"))
                + str(self.config.get_config("VHDL_BOX"))
            )
            if top_lang is RTL.VHDL
            else (
                "read_verilog -sv -library "
                + ("dovado " if is_library else (folder + " "))
                + str(self.config.get_config("WORK_DIR"))
                + str(self.config.get_config("VERILOG_BOX"))
            ),
            "box",
            self.synthesis_part,
            self.synthesis_directive,
            "-incremental_synth" if self.incremental_mode.synthesis else "",
        ]

        implementation_replacements: Optional[List[str]] = (
            []
            if self.stop_step is StopStep.SYNTHESIS
            else (
                [
                    "",
                    "-directive " + str(self.place_directive),
                    "",
                    "-directive " + str(self.route_directive),
                ]
                if not self.incremental_mode.implementation
                else [
                    "-directive " + str(self.place_directive),
                    " ",
                    "-directive " + str(self.route_directive),
                    " ",
                ]
            )
        )

        self.replacements = (
            synthesis_replacements
            if self.stop_step is StopStep.SYNTHESIS
            else synthesis_replacements[:4]
            + [
                (
                    "read_vhdl -library "
                    + ("dovado " if is_library else (folder + " "))
                    + str(self.config.get_config("WORK_DIR"))
                    + str(self.config.get_config("VHDL_BOX"))
                )
                if top_lang is RTL.VHDL
                else (
                    "read_verilog -sv -library "
                    + ("dovado " if is_library else (folder + " "))
                    + str(self.config.get_config("WORK_DIR"))
                    + str(self.config.get_config("VERILOG_BOX"))
                )
            ]
            + synthesis_replacements[5:]
            + implementation_replacements
        )
        self.replacements += [
            str(self.config.get_config(self.stop_step.name + "_TIMING")),
            str(self.config.get_config(self.stop_step.name + "_UTILISATION")),
        ]
        return super().fill()

    def setup_incremental(self, is_incremental: IsIncremental):
        if not is_incremental.synthesis and not is_incremental.implementation:
            return
        path = str(self.config.get_config("WORK_DIR"))
        if is_incremental.synthesis:
            path += str(self.config.get_config("SYNTHESIS"))
        if is_incremental.implementation:
            path += str(self.config.get_config("IMPLEMENTATION"))
        text = Path(path).read_text()
        text = text.replace("#! ", "")
        Path(path).write_text(text)


class HdlBoxFrameHandler(FillHandler):
    def __init__(
        self,
        placeholder: str,
        frame_path: str,
        top_module: str,
        ports: List[Port],
        clock_port: Port,
        out_path: str,
        hdl: RTL,
        lib: Optional[str],
    ):
        self.__top_module: str = top_module
        self.__ports: List[Port] = ports
        self.__clock_port: Port = clock_port
        self.__parameters: Optional[List[Parameter]] = None
        self.__hdl: RTL = hdl
        self.__lib: Optional[str] = lib

        FillHandler.__init__(self, placeholder, frame_path, out_path)

    def get_parameters(self) -> List[Parameter]:
        if self.__parameters:
            return self.__parameters
        raise Exception(
            "Trying to access parameters in HdlBoxFrameHandler before setting them"
        )

    def set_parameters(self, parameters: List[Parameter]) -> None:
        self.__parameters = parameters

    def fill(self) -> bool:
        if not self.__parameters:
            raise Exception(
                "Cannot fill box without setting parameters beforehand"
            )

        if self.__hdl is RTL.VHDL:
            if self.__lib:
                return self.__vhdl_fill_box(self.__lib)
            raise ValueError(
                "Cannot retrieve lib in which the top level resides"
            )
        return self.__verilog_fill_box()

    def __vhdl_parameter_map(self) -> str:
        parameter_section: str = "generic map(\n"
        for parameter in self.get_parameters()[:-1]:
            if not parameter.get_value():
                raise Exception(
                    "Please provide default values for all parameters, "
                    + str(parameter.get_name())
                    + " does not have one."
                )
            parameter_section += (
                parameter.get_name()
                + " => "
                + (str(parameter.get_value())).strip()
                + ",\n"
            )
        parameter_section += (
            self.get_parameters()[-1].get_name()
            + " => "
            + (str(self.get_parameters()[-1].get_value())).strip()
            + ")"
        )
        return parameter_section

    def __vhdl_fill_box(self, lib: str) -> bool:
        input_mapping = [
            port.get_name()
            + (
                " => " + port.get_type().descriptor + "'('1'),\n"
                if port.get_type().type is PortTypeEnum.SCALAR
                else " => "
                + port.get_type().descriptor
                + "'((others => std_logic'('1'))),\n"
            )
            for port in self.__ports
            if (
                port.get_direction().direction is PortDirectionEnum.INPUT
                and port.get_name() != self.__clock_port.get_name()
            )
        ]
        input_mapping[len(input_mapping) - 1] = input_mapping[
            len(input_mapping) - 1
        ].replace(",", "")
        self.replacements = [
            "library " + lib + ";",
            lib + "." + self.__top_module,
            self.__vhdl_parameter_map(),
            self.__clock_port.get_name(),
            "".join(input_mapping),
        ]
        return super().fill()

    def __verilog_parameter_map(self) -> str:
        parameter_section: str = "#(\n"
        for parameter in self.get_parameters()[:-1]:
            parameter_section += (
                "."
                + parameter.get_name()
                + "("
                + str(parameter.get_value())
                + "),\n"
            )
        parameter_section += (
            "."
            + self.get_parameters()[-1].get_name()
            + "("
            + str(self.get_parameters()[-1].get_value())
            + ")\n)\n"
        )
        return parameter_section

    def __verilog_fill_box(self) -> bool:
        input_mapping = [
            "." + port.get_name() + " ('1),\n"
            for port in self.__ports
            if (
                port.get_direction().direction is PortDirectionEnum.INPUT
                and port.get_name() != self.__clock_port.get_name()
            )
        ]

        input_mapping[len(input_mapping) - 1] = input_mapping[
            len(input_mapping) - 1
        ].replace(",", "")

        self.replacements = [
            self.__top_module,
            self.__verilog_parameter_map(),
            self.__clock_port.get_name(),
            "".join(input_mapping),
        ]
        return super().fill()
