from pathlib import Path

from dovado_rtl.parsers.utilities import HdlAntlrParser
from dovado_rtl.parsers.system_verilog.system_verilog_parsed import SystemVerilogParsed
from dovado_rtl.parsers.system_verilog.generated.SystemVerilogLexer import (
    SystemVerilogLexer as GeneratedSystemVerilogLexer,
)
from dovado_rtl.parsers.system_verilog.generated.SystemVerilogParser import (
    SystemVerilogParser as GeneratedSystemVerilogParser,
)
from dovado_rtl.parsers.system_verilog.system_verilog_visitor import (
    SystemVerilogVisitor,
)

import antlr4


class SystemVerilogParser(HdlAntlrParser):
    __grammar_top_rule: str = "source_text"

    def parse(self, to_parse: Path) -> SystemVerilogParsed:
        token_stream, modules = self._parse(to_parse)
        return SystemVerilogParsed(token_stream, modules)

    @property
    def _grammar_top_rule(self) -> str:
        return self.__grammar_top_rule

    @property
    def _lexer_type(self) -> type[antlr4.Lexer]:
        return GeneratedSystemVerilogLexer

    @property
    def _parser_type(self) -> type[antlr4.Parser]:
        return GeneratedSystemVerilogParser

    @property
    def _visitor_type(self) -> type[antlr4.ParseTreeVisitor]:
        return SystemVerilogVisitor
