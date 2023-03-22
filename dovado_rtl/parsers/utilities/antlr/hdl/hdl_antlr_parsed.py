#!/usr/bin/env python3
from typing import Sequence, cast

from antlr4 import TokenStream
from dovado_rtl.parsers.utilities.antlr.antlr_parsed import AntlrParsed
from dovado_rtl.parsers.utilities.antlr.hdl.hdl_antlr_module import HdlAntlrModule


class HdlAntlrParsed(AntlrParsed):
    def __init__(
        self, token_stream: TokenStream, modules: Sequence[HdlAntlrModule]
    ) -> None:
        super().__init__(token_stream, modules)
        self._modules = modules

    @property
    def modules(self) -> Sequence[HdlAntlrModule]:
        return self._modules

    def get_module(self, name: str) -> HdlAntlrModule:
        return cast(HdlAntlrModule, super().get_module(name))
