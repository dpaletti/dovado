from pathlib import Path

from antlr4.tree.Tree import ParseTree
from dovado_rtl.parsers.utilities import HdlAntlrParser
from dovado_rtl.parsers.verilog.verilog_parsed import VerilogParsed
from dovado_rtl.parsers.verilog.generated.VerilogLexer import (
    VerilogLexer as GeneratedVerilog2001Lexer,
)
from dovado_rtl.parsers.verilog.generated.VerilogParser import (
    VerilogParser as GeneratedVerilog2001Parser,
)
from dovado_rtl.parsers.verilog.verilog_visitor import (
    VerilogVisitor,
)

import antlr4


class VerilogParser(HdlAntlrParser):
    __grammar_top_rule: str = "source_text"

    def parse(self, to_parse: Path) -> VerilogParsed:
        token_stream, modules = self._parse(to_parse)
        return VerilogParsed(token_stream, modules)

    @property
    def _grammar_top_rule(self) -> str:
        return self.__grammar_top_rule

    @property
    def _lexer_type(self) -> type[antlr4.Lexer]:
        return GeneratedVerilog2001Lexer

    @property
    def _parser_type(self) -> type[antlr4.Parser]:
        return GeneratedVerilog2001Parser

    @property
    def _visitor_type(self) -> type[ParseTree]:
        return VerilogVisitor
