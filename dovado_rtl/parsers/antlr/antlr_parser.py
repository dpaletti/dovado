from pathlib import Path

import antlr4
from antlr4.tree.Tree import ParseTree
from dovado_rtl.parsers.antlr.antlr_parsed import AntlrParsed
from abc import ABC, abstractmethod


class AntlrParser(ABC):
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

    def _antlr_parse(
        self,
        to_parse: Path,
    ) -> tuple[ParseTree, antlr4.CommonTokenStream]:
        file_stream = antlr4.FileStream(str(to_parse))
        lexer = self._lexer_type(file_stream)
        token_stream = antlr4.CommonTokenStream(lexer)
        parser = self._parser_type(token_stream)
        parse_tree: ParseTree = getattr(parser, self._grammar_top_rule)()
        return parse_tree, token_stream
