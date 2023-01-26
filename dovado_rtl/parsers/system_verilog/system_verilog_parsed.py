from antlr4 import TokenStream
from dovado_rtl.parsing_utilities.antlr.hdl.hdl_antlr_module import HdlAntlrModule
from dovado_rtl.parsing_utilities.antlr.hdl.hdl_antlr_parsed import HdlAntlrParsed


class SystemVerilogParsed(HdlAntlrParsed):
    __parameter_initialization_prefix = "="

    def __init__(self, token_stream: TokenStream, modules: list[HdlAntlrModule]):
        super().__init__(token_stream=token_stream, modules=modules)

    @property
    def _parameter_initialization_prefix(self) -> str:
        return self.__parameter_initialization_prefix
