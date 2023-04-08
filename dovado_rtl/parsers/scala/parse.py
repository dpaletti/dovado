from typing import Union

from dovado_rtl.explorers.utilities.tasks import ParsedProject
from dovado_rtl.input import Input
from dovado_rtl.parsers.parse import parse as general_parse
from dovado_rtl.parsers.scala.scala_parser import ScalaParser


def parse(
    input_project: Input,
) -> ParsedProject:
    return general_parse(input_project, ScalaParser)
