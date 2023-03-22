from dovado_rtl.parsers.utilities.antlr.hdl.hdl_antlr_parsed import HdlAntlrParsed


class SystemVerilogParsed(HdlAntlrParsed):
    __parameter_initialization_prefix = "="

    @property
    def _parameter_initialization_prefix(self) -> str:
        return self.__parameter_initialization_prefix
