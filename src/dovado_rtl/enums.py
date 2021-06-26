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