from abc import ABC
from typing import List, Optional
from enum import Enum, auto
from dataclasses import dataclass
from dovado_rtl.parsers.antlr.hdl.hdl_antlr_parameter import HdlAntlrParameter

from antlr4 import ParseTreeVisitor


class PortDirectionEnum(Enum):
    INPUT = auto()
    OUTPUT = auto()
    OTHER = auto()


class PortTypeEnum(Enum):
    SCALAR = auto()
    VECTOR = auto()
    REG = auto()


@dataclass
class PortDirection:
    direction: PortDirectionEnum
    descriptor: str


@dataclass
class PortType:
    type: PortTypeEnum
    descriptor: str


class Port:
    def __init__(
        self,
        name: str,
        direction: Optional[PortDirection],
        port_type: Optional[PortType],
    ):
        self.__name = name
        self.__direction = direction
        self.__type = port_type

    @property
    def name(self) -> str:
        return self.__name

    @property
    def direction(self) -> Optional[PortDirection]:
        return self.__direction

    @property
    def type(self) -> Optional[PortType]:
        return self.__type

    def set_direction(self, direction: PortDirection) -> None:
        self.__direction = direction

    def set_type(self, s_type: PortType) -> None:
        self.__type = s_type

    def __repr__(self):
        return (
            "Port: {"
            + "name: '"
            + str(self.__name)
            + "', "
            + "type: '"
            + str(self.__type)
            + "', "
            + "direction: '"
            + str(self.__direction)
            + "'}"
        )


class Entity:
    def __init__(self, name: str):
        self.__name: str = name
        self.__ports: List[Port] = []
        self.__parameters: List[HdlAntlrParameter] = []

    @property
    def name(self):
        return self.__name

    @property
    def parameters(self) -> List[HdlAntlrParameter]:
        return self.__parameters

    @property
    def ports(self) -> List[Port]:
        return self.__ports

    def asdict(self):
        return

    def add_port(self, port_to_add: Port) -> None:
        # verilog parser may traverse ports more than once
        for p in self.__ports:
            if p.name == port_to_add.name:
                direction_to_add = port_to_add.direction
                if not p.direction and direction_to_add:
                    p.set_direction(direction_to_add)
                if p.direction != direction_to_add:
                    raise Exception(
                        "Error during parsing, double "
                        + "contrasting port definition (direction mismatch)"
                    )
                type_to_add = port_to_add.type
                if not p.type and type_to_add:
                    p.set_type(type_to_add)
                if p.type != port_to_add.type:
                    raise Exception(
                        "Error during parsing, double "
                        + "contrasting port definition (type mismatch) "
                        + "old type= "
                        + str(p.type)
                        + " new_type= "
                        + str(port_to_add.type)
                    )
                return
        self.__ports.append(port_to_add)

    def add_parameter(self, parameter: HdlAntlrParameter) -> None:
        self.__parameters.append(parameter)


class TopLevel:
    def __init__(self, libraries: List[str], used: List[str]):
        self.__libraries: List[str] = libraries
        self.__use_clauses: List[str] = used

    def add_library(self, library: str):
        self.__libraries.append(library)

    def add_used(self, used: str):
        self.__use_clauses.append(used)

    def get_libraries(self):
        return self.__libraries

    def get_use_clauses(self):
        return self.__use_clauses


class HDLVisitor(ABC, ParseTreeVisitor):
    def __init__(self):
        self.entities: List[Entity] = []
        self.top_level: TopLevel = TopLevel([], [])
