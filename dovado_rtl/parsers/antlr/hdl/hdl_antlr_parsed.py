#!/usr/bin/env python3

from abc import ABC

from antlr4 import TokenStream
from dovado_rtl.parsers.antlr.antlr_parameter import AntlrParameter
from dovado_rtl.parsers.antlr.antlr_parsed import AntlrParsed
from dovado_rtl.parsers.antlr.hdl.hdl_representation import Entity


class HdlAntlrParsed(AntlrParsed, ABC):
    def __init__(self, token_stream: TokenStream, entities: list[Entity]):
        super().__init__(token_stream)
        self.entities = entities

    def _get_parameter(self, name: str) -> AntlrParameter:
        for entity in self.entities:
            for parameter in entity.parameters:
                if parameter.name == name:
                    return parameter
        raise ValueError("Parameter with name " + str(name) + " does not exists.")
