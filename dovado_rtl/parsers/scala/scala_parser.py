from pathlib import Path
from dovado_rtl.parsers.scala.scala_visitor import ScalaVisitor
from dovado_rtl.parsers.scala.scala_parsed import ScalaParsed
from dovado_rtl.parsers.utilities.antlr.antlr_parser import AntlrParser
import antlr4
from dovado_rtl.parsers.scala.generated.ScalaParser import (
    ScalaParser as GeneratedScalaParser,
)
from dovado_rtl.parsers.scala.generated.ScalaLexer import (
    ScalaLexer as GeneratedScalaLexer,
)


class ScalaParser(AntlrParser):
    __grammar_top_rule: str = "compilationUnit"

    def parse(self, to_parse: Path) -> ScalaParsed:
        token_stream, classes = self._parse(to_parse)
        return ScalaParsed(token_stream, classes)

    @property
    def _grammar_top_rule(self) -> str:
        return self.__grammar_top_rule

    @property
    def _lexer_type(self) -> type[antlr4.Lexer]:
        return GeneratedScalaLexer

    @property
    def _parser_type(self) -> type[antlr4.Parser]:
        return GeneratedScalaParser

    @property
    def _visitor_type(self) -> type[antlr4.ParseTreeVisitor]:
        return ScalaVisitor
