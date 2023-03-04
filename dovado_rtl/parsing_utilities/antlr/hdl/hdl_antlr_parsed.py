#!/usr/bin/env python3
from typing import Sequence, cast

from antlr4 import TokenStream
from dovado_rtl.parsing_utilities.antlr.antlr_parsed import AntlrParsed
from dovado_rtl.parsing_utilities.antlr.hdl.hdl_antlr_module import HdlAntlrModule


class HdlAntlrParsed(AntlrParsed):
    def __init__(
        self, token_stream: TokenStream, modules: Sequence[HdlAntlrModule]
    ) -> None:
        super().__init__(token_stream, modules)
        self._modules = modules

    @property
    def modules(self) -> Sequence[HdlAntlrModule]:
        return self._modules

    def _get_module(self, name: str) -> HdlAntlrModule:
        return cast(HdlAntlrModule, super()._get_module(name))
