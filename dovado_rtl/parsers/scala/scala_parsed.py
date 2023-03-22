from dovado_rtl.parsers.utilities.antlr.antlr_parsed import AntlrParsed


class ScalaParsed(AntlrParsed):
    parameter_intialization_prefix: str = "="

    @property
    def _parameter_initialization_prefix(self) -> str:
        return self.parameter_intialization_prefix
