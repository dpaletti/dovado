from abc import abstractmethod
from pathlib import Path
from typing import Protocol
from dovado_rtl.parsers.utilities.parsed import Parsed
from typing_extensions import runtime_checkable
from typing import Optional


@runtime_checkable
class Parser(Protocol):
    @abstractmethod
    def parse(self, to_parse: Path, target_module: Optional[str] = None) -> Parsed:
        ...
