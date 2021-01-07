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


class RegressionModel(Enum):
    KERNEL_RIDGE = auto()
    STREAM_LEARNING_ISOUP = auto()
    STREAM_LEARNING_STACKED = auto()

