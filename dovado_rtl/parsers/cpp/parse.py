from typing import Union
from dovado_rtl.explorers.utilities.tasks import (
    AutomaticExplorationProject,
    ManualExplorationProject,
)
from dovado_rtl.input import Input
from dovado_rtl.parsers.parse import parse as general_parse
from dovado_rtl.parsers.cpp.cpp_parser import CppParser


def parse(
    input_project: Input,
) -> Union[AutomaticExplorationProject, ManualExplorationProject]:
    return general_parse(input_project, CppParser)
