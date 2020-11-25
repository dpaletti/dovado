from typing import List, Any, Optional


class Port:
    def __init__(
        self, name: str, direction: Optional[str], port_type: Optional[str]
    ):
        self.__name: str = name
        self.__direction: str = direction
        self.__type: str = port_type

    def get_name(self) -> str:
        return self.__name

    def get_direction(self) -> str:
        return self.__direction

    def get_type(self) -> str:
        return self.__type

    def set_direction(self, direction: str) -> None:
        self.__direction = direction

    def set_type(self, s_type: str) -> None:
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

    def __eq__(self, other: Any):
        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any):
        return not self == other


class Parameter:
    def __init__(self, name: str, generic_type: Optional[str]):
        self.__name: str = name
        self.__type: str = generic_type
        self.__value: Optional[int] = None

    def get_name(self) -> str:
        return self.__name

    def get_type(self) -> str:
        return self.__type

    def get_value(self) -> int:
        return self.__value

    def set_value(self, value) -> None:
        self.__value = value

    def __repr__(self):
        return (
            "Parameter: {"
            + "name: '"
            + str(self.__name)
            + "', "
            + "type: '"
            + str(self.__type)
            + "'}"
        )

    def __eq__(self, other: Any):
        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any):
        return not self == other


class Entity:
    def __init__(self, name: str):
        self.__name: str = name
        self.__ports: List[Port] = []
        self.__parameters: List[Parameter] = []

    def add_port(self, port_to_add: Port) -> None:
        # verilog parser may traverse ports more than once
        for p in self.__ports:
            if p.get_name() == port_to_add.get_name():
                if not p.get_direction() and port_to_add.get_direction():
                    p.set_direction(port_to_add.get_direction())
                if p.get_direction() != port_to_add.get_direction():
                    raise Exception(
                        "Error during parsing, double "
                        + "contrasting port definition (direction mismatch)"
                    )
                if not p.get_type() and port_to_add.get_type():
                    p.set_type(port_to_add.get_type())
                if p.get_type() != port_to_add.get_type():
                    raise Exception(
                        "Error during parsing, double "
                        + "contrasting port definition (type mismatch) "
                        + "old type= "
                        + p.get_type()
                        + " new_type= "
                        + port_to_add.get_type()
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
    def __init__(self, libraries, used):
        self.__libraries: List[str] = libraries
        self.__use_clauses: List[str] = used

    def add_library(self, library):
        self.__libraries.append(library)

    def add_used(self, used):
        self.__libraries.append(used)

    def get_libraries(self):
        return self.__libraries

    def get_use_clauses(self):
        return self.__use_clauses
