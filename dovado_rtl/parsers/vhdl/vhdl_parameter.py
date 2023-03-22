from dataclasses import dataclass
from dovado_rtl.parsers.utilities.antlr.antlr_parameter import AntlrParameter


@dataclass
class VhdlParameter(AntlrParameter):
    is_boolean: bool
