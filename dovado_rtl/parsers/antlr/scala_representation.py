from enum import Enum, auto
from typing import List
from dataclasses import dataclass


class ClassSpecification(Enum):
    CLASS = auto()  # a general OO class
    OBJECT = auto()  # a singleton
    TRAIT = auto()  # an interface


@dataclass
class Position:
    line: int
    column: int


@dataclass
class ScalaParameter:
    # SCALA statements are terminated either by a newline or by a semi-colon
    name: str
    expr_start: Position
    expr_end: Position
    value: str  # intended, right value may be any expression
    is_between_parenthesis: bool = False


class ScalaObject:
    def __init__(self, class_spec: ClassSpecification, name: str) -> None:
        self._class_spec: ClassSpecification = class_spec
        self._name: str = name
        self._parameters: List[ScalaParameter] = []

    def __str__(self) -> str:
        out = str(self._class_spec.name)
        out += " " + self._name + "\n"
        for param in self._parameters:
            out += str(param) + "\n"
        return out

    def __is_hex(self, possible_hex: str):
        try:
            int(possible_hex, 16)
            return True
        except:
            return False

    def __is_int(self, possible_int: str):
        try:
            int(possible_int)
            return True
        except:
            return False

    def addParameter(self, parameter: ScalaParameter) -> None:
        if parameter.value == "true" or parameter.value == "false":
            # Parser has wrong end of statement for true and false
            parameter.expr_end.column = parameter.expr_end.column + 4

        elif (
            (
                (self.__is_int(parameter.value))
                or ("x" in parameter.value and self.__is_hex(parameter.value))
                or ("." in parameter.value)
            )
            and parameter.expr_start.line == parameter.expr_end.line
            and parameter.expr_end.column - parameter.expr_start.column
            <= len(str(parameter.value).replace(" ", "")) - 2
        ):
            if self.__is_int(parameter.value) or (
                "x" in parameter.value and self.__is_hex(parameter.value)
            ):
                parameter.expr_end.column = (
                    parameter.expr_start.column + len(parameter.value) - 1
                )
            elif "." in parameter.value:
                # Parser may misinterpret expression length in case of assignments such as object.something
                parameter.expr_end.column = (
                    parameter.expr_start.column
                    + len(str(parameter.value).replace(" ", ""))
                    - 1
                )

        elif (
            parameter.expr_start.line == parameter.expr_end.line
            and parameter.expr_end.column - parameter.expr_start.column
            <= len(str(parameter.value).replace(" ", "")) - 2
        ):
            print("\n----------------------------------------")
            print("Ignoring parameter: " + parameter.name)
            print(
                "Parsed Length: "
                + str(parameter.expr_end.column - parameter.expr_start.column)
            )
            print(
                "Parsed Position: ("
                + str(parameter.expr_start)
                + ", "
                + str(parameter.expr_end)
                + ")"
            )
            print("Parsed Value: " + str(parameter.value))
            print("Cannot handle it currently")
            print("------------------------------------------")
            return
        if parameter.expr_start.line != parameter.expr_end.line:
            print("Ignoring parameter: " + parameter.name)
            print("Multiline assignments are not supported yet")
            return
        self._parameters.append(parameter)

    def getName(self) -> str:
        return self._name

    def getParameter(self, name: str) -> ScalaParameter:
        for parameter in self._parameters:
            if parameter.name == name:
                return parameter
        raise Exception(
            "Parameter " + str(name) + " does not exist, please fix your json"
        )


class ScalaFile:
    def __init__(self, path: str) -> None:
        self.path = path
        self.objects: List[ScalaObject] = []

    def __str__(self) -> str:
        out = "File path: " + self.path
        out += "\n"
        for ob in self.objects:
            out += str(ob) + "\n"
        return out

    def addObject(self, obj: ScalaObject) -> None:
        self.objects.append(obj)

    def addParameterToObject(
        self, parameter: ScalaParameter, object_name: str
    ) -> None:
        for obj in self.objects:
            if obj.getName() == object_name:
                obj.addParameter(parameter)
                return

    def getObject(self, name: str) -> ScalaObject:
        for obj in self.objects:
            if obj.getName() == name:
                return obj
        raise Exception(
            "Class " + str(name) + " does not exist, please fix the input json"
        )
