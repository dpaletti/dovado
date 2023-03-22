from collections.abc import Sequence
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar
from dovado_rtl.parsers.utilities.antlr.antlr_parameter import AntlrParameter

_T = TypeVar("_T")


@dataclass
class SimpleModule:
    name: str
    parameters: Sequence[AntlrParameter]


@dataclass
class RecursiveModule(Generic[_T]):
    submodules: Optional[Sequence[_T]] = None


@dataclass
class AntlrModule(RecursiveModule["AntlrModule"], SimpleModule):
    ...
