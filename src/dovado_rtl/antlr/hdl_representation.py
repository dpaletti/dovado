from typing import List, Optional
from enum import Enum, auto
from dataclasses import dataclass


class PortDirectionEnum(Enum):
    INPUT = auto()
    OUTPUT = auto()
    OTHER = auto()


class PortTypeEnum(Enum):
    SCALAR = auto()
    VECTOR = auto()
    REG = auto()


class ParameterTypeEnum(Enum):
    INTEGER = auto()
    BOOL = auto()
    OTHER = auto()


@dataclass
class PortDirection:
    direction: PortDirectionEnum
    descriptor: str


@dataclass
class PortType:
    type: PortTypeEnum
    descriptor: str


@dataclass
class ParameterType:
    type: ParameterTypeEnum
    descriptor: Optional[str]


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

    def get_name(self) -> str:
        return self.__name

    def get_direction(self) -> Optional[PortDirection]:
        return self.__direction

    def get_type(self) -> Optional[PortType]:
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


class Parameter:
    def __init__(self, name: str, generic_type: Optional[ParameterType]):
        self.__name: str = name
        self.__type: Optional[ParameterType] = generic_type
        self.__value: Optional[int] = None

    def get_name(self) -> str:
        return self.__name

    def get_type(self) -> Optional[ParameterType]:
        return self.__type

    def get_value(self) -> Optional[int]:
        return self.__value

    def set_value(self, value: int) -> None:
        self.__value = value

    def __repr__(self):
        return (
            "Parameter: {"
            + "name: '"
            + str(self.__name)
            + "', "
            + "type: '"
            + str(self.__type)
            + "', value: '"
            + str(self.__value)
            + "'}"
        )


class Entity:
    def __init__(self, name: str):
        self.__name: str = name
        self.__ports: List[Port] = []
        self.__parameters: List[Parameter] = []

    def add_port(self, port_to_add: Port) -> None:
        # verilog parser may traverse ports more than once
        for p in self.__ports:
            if p.get_name() == port_to_add.get_name():
                direction_to_add = port_to_add.get_direction()
                if not p.get_direction() and direction_to_add:
                    p.set_direction(direction_to_add)
                if p.get_direction() != direction_to_add:
                    raise Exception(
                        "Error during parsing, double "
                        + "contrasting port definition (direction mismatch)"
                    )
                type_to_add = port_to_add.get_type()
                if not p.get_type() and type_to_add:
                    p.set_type(type_to_add)
                if p.get_type() != port_to_add.get_type():
                    raise Exception(
                        "Error during parsing, double "
                        + "contrasting port definition (type mismatch) "
                        + "old type= "
                        + str(p.get_type())
                        + " new_type= "
                        + str(port_to_add.get_type())
                    )
                return
        self.__ports.append(port_to_add)

    def get_ports(self) -> List[Port]:
        return self.__ports

    def add_parameter(self, parameter: Parameter) -> None:
        self.__parameters.append(parameter)

    def get_parameters(self) -> List[Parameter]:
        return self.__parameters

    def get_name(self):
        return self.__name


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
