from typing import Protocol


class Parsed(Protocol):
    def replace(self, parameter_to_value: dict[str, str]) -> None:
        ...
