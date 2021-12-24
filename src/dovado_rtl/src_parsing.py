from pathlib import Path
from typing import List, Tuple, Optional, Dict, Iterator
from antlr4 import CommonTokenStream, FileStream
from dovado_rtl.antlr.generated.vhdl.vhdlLexer import vhdlLexer
from dovado_rtl.antlr.generated.vhdl.vhdlParser import vhdlParser
from dovado_rtl.antlr.vhdl_entity_visitor import VhdlEntityVisitor
from dovado_rtl.antlr.generated.Verilog2001.VerilogParser import VerilogParser
from dovado_rtl.antlr.generated.Verilog2001.VerilogLexer import VerilogLexer
from dovado_rtl.antlr.verilog2001_entity_visitor import (
    Verilog2001EntityVisitor,
)
from dovado_rtl.antlr.generated.SystemVerilog.SystemVerilogParser import (
    SystemVerilogParser,
)
from dovado_rtl.antlr.generated.SystemVerilog.SystemVerilogLexer import (
    SystemVerilogLexer,
)
from dovado_rtl.antlr.sysverilog_entity_visitor import (
    SysVerilogHDLEntityVisitor,
)
from dovado_rtl.antlr.hdl_representation import (
    Entity,
    PortDirection,
    PortType,
    TopLevel,
    Parameter,
    Port,
    ParameterTypeEnum,
)
from dovado_rtl.abstract_classes import AbstractSourceParser
from dovado_rtl.enums import RTL
from dovado_rtl.fill_handler import FillHandler


class SourceParser(AbstractSourceParser):
    def __init__(
        self, root_folder: str, src_path: str, entity: Optional[Entity] = None
    ):
        self.__root_folder: Path = Path(root_folder)
        self.__posix_path: Path = Path(src_path)
        supported_extensions = [".vhd", ".vhdl", ".v", ".sv"]
        if self.__posix_path.suffix not in supported_extensions:
            raise Exception(
                "Supported extensions are: "
                + str(supported_extensions)
                + ", input extension "
                + self.__posix_path.suffix
                + " not supported"
            )

        self.__input_stream = FileStream(str(self.__posix_path))
        self.__RTL = (
            RTL.VHDL
            if (
                self.__posix_path.suffix == ".vhd"
                or self.__posix_path.suffix == ".vhdl"
            )
            else RTL.VERILOG
            if self.__posix_path.suffix == ".v"
            else RTL.SYSTEM_VERILOG
        )
        self.__entities, self.__top_level = self.parse()
        self.__selected_entity: Optional[Entity] = entity

    def parse(self) -> Tuple[List[Entity], Optional[TopLevel]]:
        if self.__RTL is RTL.VHDL:
            lexer = vhdlLexer(self.__input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = vhdlParser(token_stream)
            visitor = VhdlEntityVisitor()
            tree = parser.design_file()
        elif self.__RTL is RTL.VERILOG:
            lexer = VerilogLexer(self.__input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = VerilogParser(token_stream)
            visitor = Verilog2001EntityVisitor()
            tree = parser.source_text()
        else:
            lexer = SystemVerilogLexer(self.__input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = SystemVerilogParser(token_stream)
            visitor = SysVerilogHDLEntityVisitor()
            tree = parser.source_text()

        visitor.visit(tree)
        return visitor.entities, visitor.top_level

    @staticmethod
    def get_project_path(file_path: Path) -> Path:
        # this only supports files which are at project's root
        # TODO support files in project's subdir

        return file_path.parent.absolute()

    def get_selected_entity(self) -> Entity:
        if self.__selected_entity:
            return self.__selected_entity
        raise Exception(
            "Trying to retrieve selected entity when it is not yet set"
        )

    def get_entity(self, entity: str) -> Entity:
        for e in self.__entities:
            if e.get_name() == entity:
                return e
        raise Exception(
            "Entity "
            + entity
            + " has not been found among parsed entities "
            + str(self.__entities)
        )

    def set_entity(self, entity: str) -> None:
        self.__selected_entity = self.get_entity(entity)

    def get_top_entity(self) -> Entity:
        if self.__selected_entity:
            return self.__selected_entity
        raise ValueError(
            "Trying to access selected entity when it is not yet set"
        )

    def get_path(self) -> str:
        return str(self.__posix_path)

    def get_folder(self) -> str:
        return str(self.__root_folder.name)

    def get_hdl(self) -> RTL:
        return self.__RTL

    def get_entities(self) -> List[Entity]:
        return self.__entities

    def get_parameters(self) -> List[Parameter]:
        return self.get_top_entity().get_parameters()

    def get_parameter(self, parameter: str) -> Parameter:
        for p in self.get_top_entity().get_parameters():
            if p.get_name() == parameter:
                return p
        raise Exception(
            "Parameter "
            + parameter
            + "has not been found among parsed parameters"
            + str(self.get_top_entity().get_parameters())
            + " in entity "
            + self.get_top_entity().get_name()
        )

    def get_top_level(self):
        return self.__top_level

    def get_parameter_value(self, parameter: str) -> Optional[int]:
        return self.get_parameter(parameter).get_value()

    def __set_parameter_value(self, parameter: str, value: int) -> None:
        self.get_parameter(parameter).set_value(value)

    def write_parameter_values(
        self, hdl_handler: FillHandler, values: Dict[str, int],
    ):
        # FrameHandler is too broad, should use HdlBoxHandler but in python 3.6 is not
        # possible to solve the circular dependency

        for p, v in values.items():
            if p in [
                full_param.get_name()
                for full_param in self.__selected_entity.get_parameters()
                if full_param.get_type().type is ParameterTypeEnum.BOOL
            ] and v not in {"false", "true"}:
                v = "false" if v == 0 else "true"
            self.__set_parameter_value(p, v)

        hdl_handler.replacements = [
            p.get_name()
            for p in self.get_top_entity().get_parameters()
            if p in values.keys()
        ]
        hdl_handler.set_parameters(
            [self.get_parameter(p) for p in values.keys()]
        )
        hdl_handler.fill()

    def get_ports(self) -> List[Port]:
        return self.get_top_entity().get_ports()

    def get_port(self, port: str) -> Port:
        for p in self.get_top_entity().get_ports():
            if p.get_name() == port:
                return p
        raise Exception(
            "Port "
            + port
            + "has not been found among parsed ports"
            + str(self.get_top_entity().get_ports())
            + " in entity "
            + self.get_top_entity().get_name()
        )

    def check_port(self, port: str) -> Optional[Port]:
        for p in self.get_top_entity().get_ports():
            if p.get_name() == port:
                return p
        return None

    def get_port_direction(self, port: str) -> Optional[PortDirection]:
        return self.get_port(port).get_direction()

    def get_port_type(self, port: str) -> Optional[PortType]:
        return self.get_port(port).get_type()

    def get_imports(self) -> Tuple[List[str], List[str]]:
        return (
            self.__top_level.get_libraries(),
            self.__top_level.get_use_clauses(),
        )

    def is_library_project(self) -> bool:
        return any(p.is_dir() for p in self.__root_folder.iterdir())

    def get_user_defined_libs(self) -> Iterator[str]:
        if self.__RTL is not RTL.VHDL:
            yield from ()
        for p in self.__root_folder.iterdir():
            if p.is_dir():
                yield p.name

    def get_root_folder(self) -> Path:
        return self.__root_folder
