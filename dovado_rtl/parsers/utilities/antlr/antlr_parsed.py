from abc import ABC, abstractmethod
from typing import Sequence
from antlr4 import TokenStream
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from dovado_rtl.parsers.utilities.antlr.antlr_module import AntlrModule
from dovado_rtl.parsers.utilities.antlr.antlr_parameter import AntlrParameter
from dovado_rtl.parsers.utilities.parsed import (
    MODULE_NAME_STR,
    PARAMETER_NAME_STR,
    VALUE_STR,
    Parsed,
)


class AntlrParsed(ABC, Parsed):
    def __init__(
        self, token_stream: TokenStream, modules: Sequence[AntlrModule]
    ) -> None:
        self._modules = modules
        self.__rewriter = TokenStreamRewriter(token_stream)

    @property
    def modules(self) -> Sequence[AntlrModule]:
        return self._modules

    @property
    @abstractmethod
    def _parameter_initialization_prefix(self) -> str:
        ...

    def get_module(self, name: str) -> AntlrModule:
        if "/" in name:
            raise ValueError(
                "Module identifiers containing '/' are not supported.\n"
                + "In the future a module name containing '/' will represent a path to a submodule.\n"
                + " Submodules are not supported for now."
            )

        for module in self.modules:
            if name == module.name:
                return module
        raise ValueError(
            "Module '"
            + str(name)
            + "' does not exist.\n"
            + "WARNING: module identifiers containing '/' are not supported."
        )

    def _get_parameter(self, parameter_name: str, module_name: str) -> AntlrParameter:
        module = self.get_module(module_name)
        for parameter in module.parameters:
            if parameter.name == parameter_name:
                return parameter
        raise ValueError(
            "Parameter '"
            + str(parameter_name)
            + "' does not exist in module '"
            + str(module_name)
            + "'"
        )

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

    def replace(
        self,
        module_parameter_to_value: dict[
            MODULE_NAME_STR, dict[PARAMETER_NAME_STR, VALUE_STR]
        ],
    ) -> str:
        for module_name, parameter_to_value in module_parameter_to_value.items():
            for parameter_name, value in parameter_to_value.items():
                self._lazy_replace(
                    self._get_parameter(parameter_name, module_name), value
                )
        return self.__rewriter.getDefaultText()
