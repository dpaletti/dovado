from dovado_rtl.parsers.utilities.antlr.hdl.hdl_antlr_parsed import HdlAntlrParsed


class VerilogParsed(HdlAntlrParsed):
    @property
    def _parameter_initialization_prefix(self) -> str:
        raise Exception("Parameters in Verilog must be initialized")
