from typing import List, Any, Optional


class Port:
    def __init__(
        self, name: str, direction: Optional[str], port_type: Optional[str]
    ):
        self._name = name
        self._direction = direction
        self._type = port_type

    def get_name(self):
        return self._name

    def get_direction(self):
        return self._direction

    def get_type(self):
        return self._type

    def set_direction(self, direction: str):
        self._direction = direction

    def set_type(self, s_type: str):
        self._type = s_type

    def __repr__(self):
        return (
            "Port: {"
            + "name: '"
            + str(self._name)
            + "', "
            + "type: '"
            + str(self._type)
            + "', "
            + "direction: '"
            + str(self._direction)
            + "'}"
        )

    def __eq__(self, other: Any):
        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any):
        return not self == other


class Parameter:
    def __init__(self, name: str, generic_type: Optional[str]):
        self._name = name
        self._type = generic_type

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def __repr__(self):
        return (
            "Parameter: {"
            + "name: '"
            + str(self._name)
            + "', "
            + "type: '"
            + str(self._type)
            + "'}"
        )

    def __eq__(self, other: Any):
        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any):
        return not self == other


class Entity:
    def __init__(self, name: str):
        self._name: str = name
        self._ports: List[Port] = []
        self._parameters: List[Parameter] = []
        self._port_updates = []

    def add_port(self, port_to_add: Port):
        # verilog parser may traverse ports more than once
        for p in self._ports:
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
        self._ports.append(port_to_add)

    def get_ports(self):
        return self._ports

    def add_parameter(self, parameter: Parameter):
        self._parameters.append(parameter)

    def get_parameters(self):
        return self._parameters

    def get_name(self):
        return self._name


class TopLevel:
    def __init__(self, libraries, used):
        self._libraries: List[str] = libraries
        self._used: List[str] = used

    def add_library(self, library):
        self._libraries.append(library)

    def add_used(self, used):
        self._libraries.append(used)

    def get_libraries(self):
        return self._libraries

    def get_used(self):
        return self._used
