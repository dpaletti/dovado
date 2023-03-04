from dataclasses import dataclass
from dovado_rtl.parsing_utilities.antlr.antlr_parameter import AntlrParameter


@dataclass
class VhdlParameter(AntlrParameter):
    is_boolean: bool
