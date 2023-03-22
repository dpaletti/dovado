from typing import Sequence

from dovado_rtl.parsers.vhdl.vhdl_parameter import VhdlParameter
from dovado_rtl.parsers.utilities.antlr.hdl.hdl_antlr_module import HdlAntlrModule
from dovado_rtl.parsers.utilities.antlr.hdl.hdl_antlr_parsed import HdlAntlrParsed
from dovado_rtl.parsers.utilities.parsed import (
    MODULE_NAME_STR,
    PARAMETER_NAME_STR,
    VALUE_STR,
)


class VhdlParsed(HdlAntlrParsed):
    parameter_intialization_prefix: str = ":="

    def replace(
        self,
        module_parameter_to_value: dict[
            MODULE_NAME_STR, dict[PARAMETER_NAME_STR, VALUE_STR]
        ],
    ) -> str:
        parameter_to_value_with_boolean_replaced = module_parameter_to_value.copy()
        for module_name, parameter_to_value in module_parameter_to_value.items():
            for parameter_name, parameter_value in parameter_to_value.items():
                parameter = self._get_parameter(parameter_name, module_name)
                if parameter.is_boolean:
                    lowercase_parameter_value = parameter_value.lower()
                    if lowercase_parameter_value not in ["0", "1", "false", "true"]:
                        raise ValueError(
                            "Parameter '"
                            + parameter_name
                            + "' is a boolean parameter, value "
                            + str(parameter_value)
                            + " is not allowed. Allowed values are (case-insensitive): '0', '1', 'false', 'true'"
                        )
                    parameter_to_value_with_boolean_replaced[module_name][
                        parameter_name
                    ] = (
                        "false"
                        if (
                            lowercase_parameter_value == "0"
                            or lowercase_parameter_value == "false"
                        )
                        else "true"
                    )
        return super().replace(parameter_to_value_with_boolean_replaced)

    def _get_parameter(self, parameter_name: str, module_name: str) -> VhdlParameter:
        parameter = super()._get_parameter(parameter_name, module_name)
        if isinstance(parameter, VhdlParameter):
            return parameter
        raise ValueError(
            "Parameter '"
            + str(parameter)
            + "' must be a VhdlParameter not a '"
            + str(type(parameter))
            + "'"
        )

    @property
    def entities(self) -> Sequence[HdlAntlrModule]:
        return self.modules

    @property
    def _parameter_initialization_prefix(self) -> str:
        return self.parameter_intialization_prefix
