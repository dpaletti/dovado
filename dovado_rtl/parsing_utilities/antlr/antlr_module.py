from dataclasses import dataclass
from typing import Generic, Optional, TypeVar
from dovado_rtl.parsing_utilities.antlr.antlr_parameter import AntlrParameter

_T = TypeVar("_T")


@dataclass
class SimpleModule:
    name: str
    parameters: list[AntlrParameter]


@dataclass
class RecursiveModule(Generic[_T]):
    submodules: Optional[list[_T]] = None


@dataclass
class AntlrModule(RecursiveModule["AntlrModule"], SimpleModule):
    ...
