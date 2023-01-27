from dovado_rtl.parsing_utilities import HdlAntlrParsed


class VhdlParsed(HdlAntlrParsed):
    parameter_intialization_prefix: str = ":="

    @property
    def entities(self):
        return self.modules

    @property
    def _parameter_initialization_prefix(self) -> str:
        return self.parameter_intialization_prefix
