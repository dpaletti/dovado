#!/usr/bin/env python3
from typing import cast

from antlr4 import TokenStream
from dovado_rtl.parsing_utilities.antlr.antlr_parsed import AntlrParsed
from dovado_rtl.parsing_utilities.antlr.hdl.hdl_antlr_module import HdlAntlrModule


class HdlAntlrParsed(AntlrParsed):
    def __init__(
        self, token_stream: TokenStream, modules: tuple[HdlAntlrModule]
    ) -> None:
        super().__init__(token_stream, modules)
        self._modules = modules

    @property
    def modules(self) -> tuple[HdlAntlrModule]:
        return self._modules
