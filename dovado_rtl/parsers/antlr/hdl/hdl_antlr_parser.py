from abc import ABC

from antlr4.tree.Tree import ParseTree
from dovado_rtl.parsers.antlr.hdl.hdl_representation import Entity, HDLVisitor, TopLevel
from dovado_rtl.parsers.antlr.antlr_parser import AntlrParser


class HdlAntlrParser(AntlrParser, ABC):
    @staticmethod
    def _hdl_visit(
        visitor_type: type[HDLVisitor], parse_tree: ParseTree
    ) -> tuple[list[Entity], TopLevel]:
        visitor = visitor_type()
        visitor.visit(parse_tree)
        return visitor.entities, visitor.top_level
