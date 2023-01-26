from antlr4 import TokenStream
from dovado_rtl.parsing_utilities import HdlAntlrParsed, HdlAntlrModule


class VerilogParsed(HdlAntlrParsed):
    def __init__(self, token_stream: TokenStream, modules: list[HdlAntlrModule]):
        super().__init__(token_stream=token_stream, modules=modules)

    @property
    def _parameter_initialization_prefix(self) -> str:
        raise Exception("Parameters in Verilog must be initialized")
