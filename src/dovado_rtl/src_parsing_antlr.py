from enum import Enum, auto
from dataclasses import dataclass
from antlr4 import CommonTokenStream, FileStream
from dovado_rtl.antlr.generated.vhdl.vhdlLexer import vhdlLexer
from dovado_rtl.antlr.generated.vhdl.vhdlParser import vhdlParser
from dovado_rtl.antlr.VhdlEntityVisitor import VhdlEntityVisitor
from dovado_rtl.antlr.generated.Verilog2001.Verilog2001Parser import (
    Verilog2001Parser,
)
from dovado_rtl.antlr.generated.Verilog2001.Verilog2001Lexer import (
    Verilog2001Lexer,
)
from dovado_rtl.antlr.Verilog2001EntityVisitor import Verilog2001EntityVisitor
from dovado_rtl.antlr.generated.SysVerilogHDL.SysVerilogHDLParser import (
    SysVerilogHDLParser,
)
from dovado_rtl.antlr.generated.SysVerilogHDL.SysVerilogHDLLexer import (
    SysVerilogHDLLexer,
)
from dovado_rtl.antlr.SysVerilogHDLEntityVisitor import (
    SysVerilogHDLEntityVisitor,
)


class RTL(Enum):
    VHDL = auto()
    VERILOG = auto()
    SYSTEM_VERILOG = auto()


class StopStep(Enum):
    SYNTHESIS = auto()
    IMPLEMENTATION = auto()


class ImplementationStep(Enum):
    PLACE = auto()
    ROUTE = auto()


@dataclass
class IsIncremental:
    synthesis: bool = True
    implementation: bool = True


def parse(src):
    input_stream = FileStream(src)
    vhdl = True
    if vhdl is True:
        lexer = vhdlLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = vhdlParser(token_stream)
        tree = parser.design_file()
        visitor = VhdlEntityVisitor()
        visitor.visit(tree)
        print(visitor.entities[0].get_name())
        print(visitor.entities[0].get_ports())
        print(visitor.entities[0].get_parameters())
    verilog2001 = False
    if verilog2001 is True:
        lexer = Verilog2001Lexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = Verilog2001Parser(token_stream)
        tree = parser.source_text()
        visitor = Verilog2001EntityVisitor()
        visitor.visit(tree)
        print(visitor.entities[0].get_name())
        print(visitor.entities[0].get_ports())
        print(visitor.entities[0].get_parameters())

    system_verilog = False
    if system_verilog is True:
        lexer = SysVerilogHDLLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SysVerilogHDLParser(token_stream)
        tree = parser.source_text()
        visitor = SysVerilogHDLEntityVisitor()
        visitor.visit(tree)
        print(visitor.entities[0].get_name())
        print(visitor.entities[0].get_ports())
        print(visitor.entities[0].get_parameters())

