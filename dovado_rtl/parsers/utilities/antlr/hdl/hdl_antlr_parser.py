#!/usr/bin/env python3
from pathlib import Path
from typing import cast
from dovado_rtl.parsers.utilities.antlr.antlr_parser import AntlrParser
from dovado_rtl.parsers.utilities.antlr.hdl.hdl_antlr_module import HdlAntlrModule
import antlr4


class HdlAntlrParser(AntlrParser):
    def _parse(
        self, to_parse: Path
    ) -> tuple[antlr4.CommonTokenStream, tuple[HdlAntlrModule]]:
        return cast(
            tuple[antlr4.CommonTokenStream, tuple[HdlAntlrModule]],
            super()._parse(to_parse),
        )
