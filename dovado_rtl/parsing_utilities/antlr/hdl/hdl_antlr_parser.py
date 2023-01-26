from abc import ABC, abstractmethod
from pathlib import Path

from antlr4.tree.Tree import ParseTree
from dovado_rtl.parsing_utilities import AntlrParser
import antlr4

from dovado_rtl.parsing_utilities.antlr.hdl.hdl_antlr_module import HdlAntlrModule


class HdlAntlrParser(AntlrParser, ABC):
    @property
    @abstractmethod
    def _visitor_type(self) -> type[antlr4.ParseTreeVisitor]:
        ...

    def __hdl_visit(self, parse_tree: ParseTree) -> list[HdlAntlrModule]:
        visitor = self._visitor_type()
        modules: list[HdlAntlrModule] = visitor.visit(parse_tree)
        return modules

    def _hdl_parse(
        self,
        to_parse: Path,
    ) -> tuple[antlr4.CommonTokenStream, list[HdlAntlrModule]]:
        parse_tree: ParseTree
        token_stream: antlr4.CommonTokenStream
        modules: list[HdlAntlrModule]

        parse_tree, token_stream = self._antlr_parse(to_parse)
        modules = self.__hdl_visit(parse_tree)
        return token_stream, modules
