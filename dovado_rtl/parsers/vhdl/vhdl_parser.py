from pathlib import Path
from antlr4 import CommonTokenStream

from antlr4.tree.Tree import ParseTree
from dovado_rtl.parsers.antlr.hdl.hdl_representation import HDLVisitor
from dovado_rtl.parsers.vhdl.generated.vhdlParser import (
    vhdlParser as GeneratedVhdlParser,
)
from dovado_rtl.parsers.vhdl.generated.vhdlLexer import (
    vhdlLexer as GeneratedVhdlLexer,
)
from dovado_rtl.parsers.vhdl.vhdl_entity_visitor import VhdlEntityVisitor
from dovado_rtl.parsers.antlr.hdl.hdl_antlr_parser import HdlAntlrParser

from dovado_rtl.parsers.vhdl.vhdl_parsed import VhdlParsed
import antlr4


class VhdlParser(HdlAntlrParser):
    __grammar_top_rule: str = "design_file"

    def parse(self, to_parse: Path) -> VhdlParsed:
        token_stream, entities, _ = self._hdl_parse(to_parse)
        return VhdlParsed(token_stream, entities)

    @property
    def _grammar_top_rule(self) -> str:
        return self.__grammar_top_rule

    @property
    def _lexer_type(self) -> type[antlr4.Lexer]:
        return GeneratedVhdlLexer

    @property
    def _parser_type(self) -> type[antlr4.Parser]:
        return GeneratedVhdlParser

    @property
    def _visitor_type(self) -> type[HDLVisitor]:
        return VhdlEntityVisitor
