from dovado_rtl.parsers.utilities.antlr.antlr_parsed import AntlrParsed


class CppParsed(AntlrParsed):
    @property
    def _parameter_initialization_prefix(self) -> str:
        raise ValueError(
            "In c++ we work only on defines, no concept of initialization exists"
        )
