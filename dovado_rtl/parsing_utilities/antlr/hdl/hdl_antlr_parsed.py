from abc import ABC

from antlr4 import TokenStream
from dovado_rtl.parsing_utilities import HdlAntlrModule, AntlrParsed, AntlrParameter


class HdlAntlrParsed(AntlrParsed, ABC):
    def __init__(self, token_stream: TokenStream, modules: list[HdlAntlrModule]):
        super().__init__(token_stream)
        self.modules = modules

    def _get_parameter(self, name: str) -> AntlrParameter:
        for module in self.modules:
            for parameter in module.parameters:
                if parameter.name == name:
                    return parameter
        raise ValueError("Parameter with name " + str(name) + " does not exists.")
