from pathlib import Path

import antlr4
from antlr4.tree.Tree import ParseTree
from dovado_rtl.parsers.utilities.antlr.antlr_module import AntlrModule
from dovado_rtl.parsers.utilities.antlr.antlr_parsed import AntlrParsed
from abc import ABC, abstractmethod

from dovado_rtl.parsers.utilities.parser import Parser


class AntlrParser(ABC, Parser):
    @abstractmethod
    def parse(self, to_parse: Path) -> AntlrParsed:
        ...

    @property
    @abstractmethod
    def _lexer_type(self) -> type[antlr4.Lexer]:
        ...

    @property
    @abstractmethod
    def _parser_type(self) -> type[antlr4.Parser]:
        ...

    @property
    @abstractmethod
    def _visitor_type(self) -> type[antlr4.ParseTreeVisitor]:
        ...

    @property
    @abstractmethod
    def _grammar_top_rule(self) -> str:
        ...

    def _make_parser(
        self,
        to_parse: Path,
    ) -> tuple[ParseTree, antlr4.CommonTokenStream]:
        file_stream = antlr4.FileStream(str(to_parse))
        lexer = self._lexer_type(file_stream)
        token_stream = antlr4.CommonTokenStream(lexer)
        parser = self._parser_type(token_stream)
        parse_tree: ParseTree = getattr(parser, self._grammar_top_rule)()
        return parse_tree, token_stream

    def _visit(self, parse_tree: ParseTree) -> tuple[AntlrModule]:
        visitor = self._visitor_type()
        modules: tuple[AntlrModule] = visitor.visit(parse_tree)
        return modules

    def _parse(
        self,
        to_parse: Path,
    ) -> tuple[antlr4.CommonTokenStream, tuple[AntlrModule]]:
        parse_tree: ParseTree
        token_stream: antlr4.CommonTokenStream
        modules: tuple[AntlrModule]

        parse_tree, token_stream = self._make_parser(to_parse)
        modules = self._visit(parse_tree)
        return token_stream, modules
