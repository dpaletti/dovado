from pathlib import Path

import antlr4
from antlr4.tree.Tree import ParseTree
from dovado_rtl.parsers.antlr_parsed import AntlrParsed
from abc import ABC, abstractmethod


class AntlrParser(ABC):
    @abstractmethod
    def parse(self, to_parse: Path) -> AntlrParsed:
        ...

    @staticmethod
    def _antlr_parse(
        to_parse: Path,
        lexer_type: type[antlr4.Lexer],
        parser_type: type[antlr4.Parser],
        grammar_top_rule: str,
    ) -> tuple[ParseTree, antlr4.CommonTokenStream]:
        file_stream = antlr4.FileStream(str(to_parse))
        lexer = lexer_type(file_stream)
        token_stream = antlr4.CommonTokenStream(lexer)
        parser = parser_type(token_stream)
        parse_tree: ParseTree = getattr(parser, grammar_top_rule)()
        return parse_tree, token_stream
