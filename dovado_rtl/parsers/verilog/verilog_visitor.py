from typing import Optional, Sequence, Union, cast
from antlr4 import IllegalStateException
from dovado_rtl.parsers.utilities import (
    AntlrParameter,
    Port,
)
from dovado_rtl.parsers.verilog.generated.VerilogParserVisitor import (
    VerilogParserVisitor,
)
from dovado_rtl.parsers.verilog.generated.VerilogParser import VerilogParser
from dovado_rtl.parsers.utilities.antlr.hdl.hdl_antlr_module import HdlAntlrModule


class VerilogVisitor(VerilogParserVisitor):
    def visitSource_text(
        self, ctx: VerilogParser.Source_textContext
    ) -> Sequence[HdlAntlrModule]:
        modules: list[HdlAntlrModule]
        parsed_description: Optional[HdlAntlrModule]

        descriptions = ctx.description()
        modules = []
        if descriptions:
            for description in descriptions:
                parsed_description = self.visitDescription(description)
                if parsed_description:
                    modules.append(parsed_description)
        return modules

    def visitDescription(
        self, ctx: VerilogParser.DescriptionContext
    ) -> Optional[HdlAntlrModule]:
        module_declaration = ctx.module_declaration()

        if module_declaration:
            return self.visitModule_declaration(module_declaration)
        return None

    def visitModule_declaration(
        self, ctx: VerilogParser.Module_declarationContext
    ) -> HdlAntlrModule:
        parameters: list[AntlrParameter]
        ports: list[Port]
        parsed_module_item: Optional[Union[list[AntlrParameter], list[Port]]]

        module_identifier = ctx.module_identifier()
        module_parameter_port_list = ctx.module_parameter_port_list()
        list_of_port_declarations = ctx.list_of_port_declarations()
        module_items = ctx.module_item()

        ports = []
        parameters = []

        if module_parameter_port_list:
            parameters = self.visitModule_parameter_port_list(
                module_parameter_port_list
            )
        if list_of_port_declarations:
            ports = self.visitList_of_port_declarations(list_of_port_declarations)
        if module_items:
            for module_item in module_items:
                parsed_module_item = self.visitModule_item(module_item)
                if parsed_module_item:
                    if isinstance(parsed_module_item[0], Port):
                        parsed_module_item = cast(list[Port], parsed_module_item)
                        ports += parsed_module_item

                    if isinstance(parsed_module_item[0], AntlrParameter):
                        parsed_module_item = cast(
                            list[AntlrParameter], parsed_module_item
                        )
                        parameters += parsed_module_item

        if module_identifier:
            return HdlAntlrModule(
                name=module_identifier.getText(), parameters=parameters, ports=ports
            )
        raise IllegalStateException("A module must have a valid identifier")

    def visitModule_item(
        self, ctx: VerilogParser.Module_itemContext
    ) -> Optional[Union[list[Port], list[AntlrParameter]]]:
        # we ignore generate and specify block

        port_declaration = ctx.port_declaration()
        module_or_generate_item = ctx.module_or_generate_item()
        parameter_declaration = ctx.parameter_declaration()
        specparam_declaration = ctx.specparam_declaration()

        if port_declaration:
            # list[Port]
            return self.visitPort_declaration(port_declaration)
        if module_or_generate_item:
            # list[AntlrParameter]
            return self.visitModule_or_generate_item(module_or_generate_item)
        if parameter_declaration:
            # list[AntlrParameter]
            return self.visitParameter_declaration(parameter_declaration)
        if specparam_declaration:
            # list[AntlrParameter]
            return self.visitSpecparam_declaration(specparam_declaration)
        return None

    def visitModule_or_generate_item(
        self, ctx: VerilogParser.Module_or_generate_itemContext
    ) -> list[AntlrParameter]:
        local_parameter_declaration = ctx.local_parameter_declaration()

        if local_parameter_declaration:
            # list[AntlrParameter]
            return self.visitLocal_parameter_declaration(local_parameter_declaration)
        return []

    def visitLocal_parameter_declaration(
        self, ctx: VerilogParser.Local_parameter_declarationContext
    ) -> list[AntlrParameter]:
        list_of_param_assignments = ctx.list_of_param_assignments()

        if list_of_param_assignments:
            return self.visitList_of_param_assignments(list_of_param_assignments)
        return []

    def visitList_of_port_declarations(
        self, ctx: VerilogParser.List_of_port_declarationsContext
    ) -> list[Port]:
        # We ignore port, port_implicit and port_explicit
        # as they deal with port connection and not declaration

        parsed_ports: list[Port]

        port_declarations = ctx.port_declaration()

        if port_declarations:
            parsed_ports = []
            for port_declaration in port_declarations:
                parsed_ports += self.visitPort_declaration(port_declaration)
            return parsed_ports
        return []

    def visitPort_declaration(
        self, ctx: VerilogParser.Port_declarationContext
    ) -> list[Port]:
        inout_declaration = ctx.inout_declaration()
        input_declaration = ctx.input_declaration()
        output_declaration = ctx.output_declaration()

        if inout_declaration:
            return self.visitInout_declaration(inout_declaration)

        if input_declaration:
            return self.visitInput_declaration(input_declaration)

        if output_declaration:
            return self.visitOutput_declaration(output_declaration)

        return []

    def visitOutput_declaration(
        self, ctx: VerilogParser.Output_declarationContext
    ) -> list[Port]:
        identifiers: list[str]

        list_of_port_identifiers = ctx.list_of_port_identifiers()

        if list_of_port_identifiers:
            identifiers = self.visitList_of_port_identifiers(list_of_port_identifiers)
            return [
                Port(
                    name=identifier,
                    direction="output",
                    dimension="vectorial" if ctx.range_() else "scalar",
                    has_default=False,
                )
                for identifier in identifiers
            ]
        return []

    def visitInput_declaration(
        self, ctx: VerilogParser.Input_declarationContext
    ) -> list[Port]:
        identifiers: list[str]

        list_of_port_identifiers = ctx.list_of_port_identifiers()

        if list_of_port_identifiers:
            identifiers = self.visitList_of_port_identifiers(list_of_port_identifiers)
            return [
                Port(
                    name=identifier,
                    direction="input",
                    dimension="vectorial" if ctx.range_() else "scalar",
                    has_default=False,
                )
                for identifier in identifiers
            ]
        return []

    def visitInout_declaration(
        self, ctx: VerilogParser.Inout_declarationContext
    ) -> list[Port]:
        identifiers: list[str]

        list_of_port_identifiers = ctx.list_of_port_identifiers()

        if list_of_port_identifiers:
            identifiers = self.visitList_of_port_identifiers(list_of_port_identifiers)
            return [
                Port(
                    name=identifier,
                    direction="inout",
                    dimension="vectorial" if ctx.range_() else "scalar",
                    has_default=False,
                )
                for identifier in identifiers
            ]
        return []

    def visitList_of_port_identifiers(
        self, ctx: VerilogParser.List_of_port_identifiersContext
    ) -> list[str]:
        port_identifiers = ctx.port_identifier()

        if port_identifiers:
            return [port_identifier.getText() for port_identifier in port_identifiers]

        return []

    def visitModule_parameter_port_list(
        self, ctx: VerilogParser.Module_parameter_port_listContext
    ) -> list[AntlrParameter]:
        parameters: list[AntlrParameter]

        parameter_declarations = ctx.parameter_declaration()

        parameters = []
        if parameter_declarations:
            for parameter_declaration in parameter_declarations:
                parameters += self.visitParameter_declaration(parameter_declaration)
        return parameters

    def visitParameter_declaration(
        self, ctx: VerilogParser.Parameter_declarationContext
    ) -> list[AntlrParameter]:
        list_of_param_assignments = ctx.list_of_param_assignments()

        if list_of_param_assignments:
            return self.visitList_of_param_assignments(list_of_param_assignments)
        return []

    def visitList_of_param_assignments(
        self, ctx: VerilogParser.List_of_param_assignmentsContext
    ) -> list[AntlrParameter]:
        parameters: list[AntlrParameter]

        param_assignments = ctx.param_assignment()
        parameters = []
        if param_assignments:
            for param_assignment in param_assignments:
                parameters.append(self.visitParam_assignment(param_assignment))
        return parameters

    def visitParam_assignment(
        self, ctx: VerilogParser.Param_assignmentContext
    ) -> AntlrParameter:
        parameter_identifier = ctx.parameter_identifier()
        constant_mintypmax_expression = ctx.constant_mintypmax_expression()

        if parameter_identifier and constant_mintypmax_expression:
            return AntlrParameter(
                name=parameter_identifier.getText(),
                value=constant_mintypmax_expression.getText(),
                rule=constant_mintypmax_expression,
                has_default=True,
            )
        raise IllegalStateException(
            "Verilog parameters must have identifier and initialization"
        )
