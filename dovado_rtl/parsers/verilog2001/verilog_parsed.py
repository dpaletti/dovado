#!/usr/bin/env python3
from antlr4 import TokenStream
from dovado_rtl.parsers.antlr.hdl.hdl_antlr_parsed import HdlAntlrParsed
from dovado_rtl.parsers.antlr.hdl.hdl_representation import Entity, TopLevel


class VerilogParsed(HdlAntlrParsed):
    def __init__(
        self, token_stream: TokenStream, entities: list[Entity], top_level: TopLevel
    ):
        super().__init__(token_stream=token_stream, entities=entities)
        self.top_level = top_level

    @property
    def _parameter_initialization_prefix(self) -> str:
        raise Exception("Parameters in Verilog must be initialized")
