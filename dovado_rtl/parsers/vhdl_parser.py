from pathlib import Path
from antlr4 import CommonTokenStream

from antlr4.tree.Tree import ParseTree
from dovado_rtl.parsers.antlr.generated.vhdl.vhdlParser import (
    vhdlParser as AntlrGeneratedParser,
)
from dovado_rtl.parsers.antlr.generated.vhdl.vhdlLexer import (
    vhdlLexer as AntlrGeneratedLexer,
)
from dovado_rtl.parsers.antlr.vhdl_entity_visitor import VhdlEntityVisitor
from dovado_rtl.parsers.hdl_antlr_parser import HdlAntlrParser

from dovado_rtl.parsers.vhdl_parsed import VhdlParsed


class VhdlParser(HdlAntlrParser):
    __grammar_top_rule: str = "design_file"

    def parse(self, to_parse: Path) -> VhdlParsed:
        parse_tree: ParseTree
        token_stream: CommonTokenStream

        parse_tree, token_stream = self._antlr_parse(
            to_parse, AntlrGeneratedLexer, AntlrGeneratedParser, self.__grammar_top_rule
        )
        entities, _ = self._hdl_visit(VhdlEntityVisitor, parse_tree)
        return VhdlParsed(token_stream, entities)
