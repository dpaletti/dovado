from abc import ABC, abstractmethod
from pathlib import Path

from antlr4.tree.Tree import ParseTree
from dovado_rtl.parsers.antlr.hdl.hdl_representation import Entity, HDLVisitor, TopLevel
from dovado_rtl.parsers.antlr.antlr_parser import AntlrParser
import antlr4


class HdlAntlrParser(AntlrParser, ABC):
    @property
    @abstractmethod
    def _visitor_type(self) -> type[HDLVisitor]:
        ...

    def __hdl_visit(self, parse_tree: ParseTree) -> tuple[list[Entity], TopLevel]:
        visitor = self._visitor_type()
        visitor.visit(parse_tree)
        return visitor.entities, visitor.top_level

    def _hdl_parse(
        self,
        to_parse: Path,
    ):
        parse_tree: ParseTree
        token_stream: antlr4.CommonTokenStream

        parse_tree, token_stream = self._antlr_parse(to_parse)
        entities, top_level = self.__hdl_visit(parse_tree)
        return token_stream, entities, top_level
