from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional
from dovado_rtl.parsers.antlr.antlr_parameter import AntlrParameter


class ParameterTypeEnum(Enum):
    INTEGER = auto()
    BOOL = auto()
    OTHER = auto()
    UNKNOWN = auto()


@dataclass
class ParameterType:
    type: ParameterTypeEnum
    descriptor: Optional[str] = None


@dataclass
class HdlAntlrParameter(AntlrParameter):
    type: ParameterType
