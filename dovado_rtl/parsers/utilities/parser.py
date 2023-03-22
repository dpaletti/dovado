from abc import ABC, abstractmethod
from pathlib import Path
from typing import Protocol
from dovado_rtl.parsers.utilities.parsed import Parsed


from typing_extensions import runtime_checkable


@runtime_checkable
class Parser(Protocol):
    @abstractmethod
    def parse(self, to_parse: Path) -> Parsed:
        ...
