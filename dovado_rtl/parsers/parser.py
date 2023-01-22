from pathlib import Path
from typing import Protocol
from dovado_rtl.parsers.parsed import Parsed


class Parser(Protocol):
    @staticmethod
    def _detect_hdl():
        # TODO: add a supported languages as an enum
        # and add a static method to get the language as an enum field
        ...

    def parse(self, to_parse: Path) -> Parsed:
        ...
