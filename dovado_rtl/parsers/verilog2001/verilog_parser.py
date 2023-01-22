#!/usr/bin/env python3

from pathlib import Path
from antlr4 import CommonTokenStream

from antlr4.tree.Tree import ParseTree
from dovado_rtl.parsers.antlr.hdl.hdl_antlr_parser import HdlAntlrParser
from dovado_rtl.parsers.antlr.hdl.hdl_representation import HDLVisitor
from dovado_rtl.parsers.verilog2001.verilog_parsed import VerilogParsed
from dovado_rtl.parsers.verilog2001.generated.VerilogLexer import (
    VerilogLexer as GeneratedVerilog2001Lexer,
)
from dovado_rtl.parsers.verilog2001.generated.VerilogParser import (
    VerilogParser as GeneratedVerilog2001Parser,
)
from dovado_rtl.parsers.verilog2001.verilog2001_entity_visitor import (
    Verilog2001EntityVisitor,
)

import antlr4


class VerilogParser(HdlAntlrParser):
    __grammar_top_rule: str = "source_text"

    def parse(self, to_parse: Path) -> VerilogParsed:
        token_stream, entities, top_level = self._hdl_parse(to_parse)
        return VerilogParsed(token_stream, entities, top_level)

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
    def _visitor_type(self) -> type[HDLVisitor]:
        return Verilog2001EntityVisitor
