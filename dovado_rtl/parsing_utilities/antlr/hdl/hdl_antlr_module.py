from dataclasses import dataclass
from typing import Optional
from dovado_rtl.parsing_utilities.antlr.antlr_parameter import AntlrParameter

from dovado_rtl.parsing_utilities.port import Port


@dataclass
class HdlAntlrModule:
    name: str
    parameters: list[AntlrParameter]
    ports: list[Port]
    submodules: Optional[list["HdlAntlrModule"]] = None
