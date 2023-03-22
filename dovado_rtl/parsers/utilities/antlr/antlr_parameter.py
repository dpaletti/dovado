#!/usr/bin/env python3
from dataclasses import dataclass

from antlr4 import ParserRuleContext

from dovado_rtl.parsers.utilities.parameter import Parameter


@dataclass
class AntlrParameter(Parameter):
    rule: ParserRuleContext
    has_default: bool
