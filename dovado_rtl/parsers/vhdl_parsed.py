from antlr4 import TokenStream
from dovado_rtl.parsers.antlr.hdl_representation import Entity
from dovado_rtl.parsers.antlr_parameter import AntlrParameter
from dovado_rtl.parsers.antlr_parsed import AntlrParsed


class VhdlParsed(AntlrParsed):
    parameter_intialization_prefix: str = ":="

    def __init__(self, token_stream: TokenStream, entities: list[Entity]):
        super().__init__(token_stream)
        self.entities = entities

    @property
    def _parameter_initialization_prefix(self) -> str:
        return self.parameter_intialization_prefix

    def _get_parameter(self, name: str) -> AntlrParameter:
        for entity in self.entities:
            for parameter in entity.parameters:
                if parameter.name == name:
                    return parameter
        raise ValueError("Parameter with name " + str(name) + " does not exists.")
