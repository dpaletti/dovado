from typing import Union

from dovado_rtl.explorers.utilities.tasks import (
    AutomaticExplorationProject,
    ManualExplorationProject,
)
from dovado_rtl.input import Input
from dovado_rtl.parsers.parse import parse as general_parse
from dovado_rtl.parsers.verilog.verilog_parser import VerilogParser


def parse(
    input_project: Input,
) -> Union[AutomaticExplorationProject, ManualExplorationProject]:
    return general_parse(input_project, VerilogParser)
