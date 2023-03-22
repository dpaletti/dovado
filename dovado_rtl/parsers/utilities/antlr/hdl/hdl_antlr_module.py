from dataclasses import dataclass
from dovado_rtl.parsers.utilities.antlr.antlr_module import AntlrModule
from dovado_rtl.parsers.utilities.port import Port


@dataclass
class ModuleWithPorts:
    ports: list[Port]


@dataclass
class HdlAntlrModule(AntlrModule, ModuleWithPorts):
    ...
