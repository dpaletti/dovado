from abc import ABC, abstractmethod
from antlr4 import TokenStream
from antlr4.TokenStreamRewriter import TokenStreamRewriter

from dovado_rtl.parsers.antlr_parameter import AntlrParameter


class AntlrParsed(ABC):
    def __init__(self, token_stream: TokenStream) -> None:
        self.__rewriter = TokenStreamRewriter(token_stream)

    @abstractmethod
    def _get_parameter(self, name: str) -> AntlrParameter:
        ...

    @property
    @abstractmethod
    def _parameter_initialization_prefix(self) -> str:
        ...

    def _lazy_replace(self, parameter: AntlrParameter, value: str) -> None:
        parameter.value = value

        to_write = value
        if not parameter.has_default:
            to_write = (
                parameter.rule.getText() + self._parameter_initialization_prefix + value
            )

        self.__rewriter.replaceRangeTokens(
            parameter.rule.start, parameter.rule.stop, to_write
        )

    def replace(self, parameter_to_value: dict[str, str]):
        for parameter_name, value in parameter_to_value.items():
            self._lazy_replace(self._get_parameter(parameter_name), value)
        return self.rewriter.getDefaultText()
