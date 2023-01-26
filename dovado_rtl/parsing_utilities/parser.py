from pathlib import Path
from typing import Protocol
from dovado_rtl.parsing_utilities.parsed import Parsed


class Parser(Protocol):
    def parse(self, to_parse: Path) -> Parsed:
        ...
