from typing import Protocol

MODULE_NAME_STR = str
PARAMETER_NAME_STR = str
VALUE_STR = str

from typing_extensions import runtime_checkable


@runtime_checkable
class Parsed(Protocol):
    def replace(
        self,
        parameter_to_value: dict[MODULE_NAME_STR, dict[PARAMETER_NAME_STR, VALUE_STR]],
    ) -> str:
        ...
