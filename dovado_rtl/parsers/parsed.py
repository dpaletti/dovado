from typing import Protocol

FILE_ROW = int
FILE_COLUMN = int
POSITION = tuple[FILE_ROW, FILE_COLUMN]


class Parsed(Protocol):
    def replace(self, parameter_to_value: dict[str, str]) -> None:
        ...
