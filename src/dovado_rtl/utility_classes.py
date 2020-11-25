from enum import Enum, auto


class RTL(Enum):
    VHDL = auto()
    VERILOG = auto()
    SYSTEM_VERILOG = auto()


class StopStep(Enum):
    SYNTHESIS = auto()
    IMPLEMENTATION = auto()


class ImplementationStep(Enum):
    PLACE = auto()
    ROUTE = auto()


class IsIncremental:
    def __init__(self, synthesis: bool, implementation: bool = False):
        self.synthesis: bool = synthesis
        self.implementation: bool = implementation
