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

    def addParameter(self, parameter: ScalaParameter) -> None:
        self._parameters.append(parameter)

    def getName(self) -> str:
        return self._name


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
