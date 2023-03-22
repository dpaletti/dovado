from pathlib import Path
import antlr4
from dovado_rtl.parsers.cpp.cpp_parsed import CppParsed
from dovado_rtl.parsers.utilities.antlr.antlr_parser import AntlrParser
from dovado_rtl.parsers.cpp.generated.CPP14Lexer import (
    CPP14Lexer as GeneratedCppLexer,
)
from dovado_rtl.parsers.cpp.generated.CPP14Parser import (
    CPP14Parser as GeneratedCppParser,
)
from dovado_rtl.parsers.cpp.cpp_visitor import CppVisitor


class CppParser(AntlrParser):
    __grammar_top_rule: str = "translationUnit"

    def parse(self, to_parse: Path) -> CppParsed:
        token_stream, classes = self._parse(to_parse)
        return CppParsed(token_stream, classes)

    @property
    def _grammar_top_rule(self) -> str:
        return self.__grammar_top_rule

    @property
    def _lexer_type(self) -> type[antlr4.Lexer]:
        return GeneratedCppLexer

    @property
    def _parser_type(self) -> type[antlr4.Parser]:
        return GeneratedCppParser

    @property
    def _visitor_type(self) -> type[antlr4.ParseTreeVisitor]:
        return CppVisitor
