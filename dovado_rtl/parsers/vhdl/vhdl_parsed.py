from dovado_rtl.parsing_utilities.antlr.hdl.hdl_antlr_parsed import HdlAntlrParsed


class VhdlParsed(HdlAntlrParsed):
    parameter_intialization_prefix: str = ":="

    @property
    def _parameter_initialization_prefix(self) -> str:
        return self.parameter_intialization_prefix
