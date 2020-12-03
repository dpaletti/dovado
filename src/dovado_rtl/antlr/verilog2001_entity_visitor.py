from dovado_rtl.antlr.hdl_representation import (
    ParameterType,
    ParameterTypeEnum,
    PortDirection,
    Entity,
    Port,
    Parameter,
    PortDirectionEnum,
    PortType,
    PortTypeEnum,
)
from dovado_rtl.antlr.generated.Verilog2001.Verilog2001Visitor import (
    Verilog2001Visitor,
)
from dovado_rtl.antlr.generated.Verilog2001.Verilog2001Parser import (
    Verilog2001Parser,
)
from typing import List, Optional


class Verilog2001EntityVisitor(Verilog2001Visitor):
    def __init__(self):
        self.entities: List[Entity] = []
        self.top_level = None

    def visitSource_text(
        self, ctx: Verilog2001Parser.Source_textContext
    ) -> None:
        if ctx.timing_spec():
            pass
        for d in ctx.description():
            self.visitDescription(d)

    def visitDescription(
        self, ctx: Verilog2001Parser.DescriptionContext
    ) -> None:
        self.visitModule_declaration(ctx.module_declaration())

    def visitModule_declaration(
        self, ctx: Verilog2001Parser.Module_declarationContext
    ) -> None:
        self.entities.append(
            Entity(self.visitModule_identifier(ctx.module_identifier()))
        )
        if ctx.module_parameter_port_list():
            self.visitModule_parameter_port_list(
                ctx.module_parameter_port_list()
            )
        if ctx.list_of_ports():
            self.visitList_of_ports(ctx.list_of_ports())
        if ctx.list_of_port_declarations():
            self.visitList_of_port_declarations(
                ctx.list_of_port_declarations()
            )
        for m in ctx.module_item():
            self.visitModule_item(m)
        for nm in ctx.non_port_module_item():
            self.visitNon_port_module_item(nm)

    def visitNon_port_module_item(
        self, ctx: Verilog2001Parser.Non_port_module_itemContext
    ):
        if ctx.local_parameter_declaration():
            self.visitLocal_parameter_declaration(
                ctx.local_parameter_declaration()
            )
        if ctx.module_or_generate_item():
            self.visitModule_or_generate_item(ctx.module_or_generate_item())
        if ctx.parameter_declaration():
            self.visitParameter_declaration(ctx.parameter_declaration())
        if ctx.specify_block():
            self.visitSpecify_block(ctx.specify_block())
        if ctx.specparam_declaration():
            self.visitSpecparam_declaration(ctx.specparam_declaration())
        if ctx.generated_instantiation():
            pass
        pass

    def visitModule_item(
        self, ctx: Verilog2001Parser.Module_itemContext
    ) -> None:
        if ctx.module_or_generate_item():
            self.visitModule_or_generate_item(ctx.module_or_generate_item())
        if ctx.port_declaration():
            self.visitPort_declaration(ctx.port_declaration())
        if ctx.generated_instantiation():
            pass
        if ctx.local_parameter_declaration():
            self.visitLocal_parameter_declaration(
                ctx.local_parameter_declaration()
            )
        if ctx.parameter_declaration():
            self.visitParameter_declaration(ctx.parameter_declaration())
        if ctx.specify_block():
            self.visitSpecify_block(ctx.specify_block())
        if ctx.specparam_declaration():
            self.visitSpecparam_declaration(ctx.specparam_declaration())

    def visitSpecify_block(
        self, ctx: Verilog2001Parser.Specify_blockContext
    ) -> None:
        for i in ctx.specify_item():
            self.visitSpecify_item(i)

    def visitSpecify_item(
        self, ctx: Verilog2001Parser.Specify_itemContext
    ) -> None:
        if ctx.specparam_declaration():
            self.visitSpecparam_declaration(ctx.specparam_declaration())
        else:
            pass

    def visitSpecparam_declaration(
        self, ctx: Verilog2001Parser.Specparam_declarationContext
    ) -> None:
        for p in self.visitList_of_specparam_assignments(
            ctx.list_of_specparam_assignments()
        ):
            self.entities[-1].add_parameter(
                Parameter(
                    p, ParameterType(ParameterTypeEnum.INTEGER, "specparam")
                )
            )

    def visitList_of_specparam_assignments(
        self, ctx: Verilog2001Parser.List_of_specparam_assignmentsContext
    ) -> List[str]:
        specparams = []
        for s in ctx.specparam_assignment():
            specparams.append(self.visitSpecparam_assignment(s))
        return specparams

    def visitSpecparam_assignment(
        self, ctx: Verilog2001Parser.Specparam_assignmentContext
    ) -> Optional[str]:
        if ctx.specparam_identifier():
            return self.visitSpecparam_identifier(ctx.specparam_identifier())
        else:
            pass

    def visitSpecparam_identifier(
        self, ctx: Verilog2001Parser.Specparam_identifierContext
    ) -> str:
        return self.visitIdentifier(ctx.identifier())

    def visitModule_or_generate_item(
        self, ctx: Verilog2001Parser.Module_or_generate_itemContext
    ):
        if ctx.parameter_override():
            self.visitParameter_override(ctx.parameter_override())
        else:
            pass

    def visitParameter_override(
        self, ctx: Verilog2001Parser.Parameter_overrideContext
    ) -> None:
        for p in self.visitList_of_parameter_assignments(
            ctx.list_of_param_assignments()
        ):
            self.entities[-1].add_parameter(Parameter(p, None))

    def visitLocal_parameter_declaration(
        self, ctx: Verilog2001Parser.Local_parameter_declarationContext
    ):
        if ctx.range_():
            for p in self.visitList_of_param_assignments(
                ctx.list_of_param_assignments()
            ):
                self.entities[-1].add_parameter(Parameter(p, None))
        else:
            for p in self.visitList_of_param_assignments(
                ctx.list_of_param_assignments()
            ):
                self.entities[-1].add_parameter(
                    Parameter(p, ctx.getText().split()[1])
                )

    def visitList_of_port_declarations(
        self, ctx: Verilog2001Parser.List_of_port_declarationsContext
    ) -> None:
        for pd in ctx.port_declaration():
            self.visitPort_declaration(pd)

    def visitPort_declaration(
        self, ctx: Verilog2001Parser.Port_declarationContext
    ) -> None:
        if ctx.attribute_instance():
            pass
        if ctx.inout_declaration():
            self.visitInout_declaration(ctx.inout_declaration())
        if ctx.input_declaration():
            self.visitInput_declaration(ctx.input_declaration())
        if ctx.output_declaration():
            self.visitOutput_declaration(ctx.output_declaration())

    def visitInout_declaration(
        self, ctx: Verilog2001Parser.Inout_declarationContext
    ) -> None:
        for p in ctx.list_of_port_identifiers():
            self.entities[-1].add_port(
                Port(
                    p,
                    PortDirection(PortDirectionEnum.OTHER, "inout"),
                    PortType(PortTypeEnum.VECTOR, "wire/reg")
                    if not ctx.net_type()
                    else self.visitNet_type(ctx.net_type()),
                )
            )

    def visitInput_declaration(
        self, ctx: Verilog2001Parser.Input_declarationContext
    ) -> None:
        for p in self.visitList_of_port_identifiers(
            ctx.list_of_port_identifiers()
        ):
            self.entities[-1].add_port(
                Port(
                    p,
                    PortDirection(PortDirectionEnum.INPUT, "input"),
                    PortType(PortTypeEnum.VECTOR, "wire/reg")
                    if not ctx.net_type()
                    else self.visitNet_type(ctx.net_type()),
                )
            )

    def visitOutput_declaration(
        self, ctx: Verilog2001Parser.Output_declarationContext
    ) -> None:
        if ctx.list_of_port_identifiers():
            for p in self.visitList_of_port_identifiers(
                ctx.list_of_port_identifiers()
            ):
                self.entities[-1].add_port(
                    Port(
                        p,
                        PortDirection(PortDirectionEnum.OUTPUT, "output"),
                        (
                            PortType(PortTypeEnum.VECTOR, "wire/reg")
                            if not ctx.net_type()
                            else self.visitNet_type(ctx.net_type())
                        )
                        if not ctx.output_variable_type()
                        else ctx.output_variable_type(),
                    )
                )

        if ctx.list_of_variable_port_identifiers():
            for vp in self.visitList_of_variable_port_identifiers(
                ctx.list_of_variable_port_identifiers()
            ):
                Port(
                    vp,
                    PortDirection(PortDirectionEnum.OUTPUT, "output"),
                    (
                        PortType(PortTypeEnum.VECTOR, "wire/reg")
                        if not ctx.net_type()
                        else self.visitNet_type(ctx.net_type())
                    )
                    if not ctx.output_variable_type()
                    else ctx.output_variable_type(),
                )

    def visitList_of_variable_port_identifiers(
        self, ctx: Verilog2001Parser.List_of_variable_port_identifiersContext
    ) -> List[str]:
        ids = []
        for p in ctx.port_identifier():
            ids.append(self.visitPort_identifier(p))

        if ctx.constant_expression():
            pass
        return ids

    def visitList_of_port_identifiers(
        self, ctx: Verilog2001Parser.List_of_port_identifiersContext
    ) -> List[str]:
        ids = []
        for pi in ctx.port_identifier():
            ids.append(self.visitPort_identifier(pi))
        return ids

    def visitNet_type(
        self, ctx: Verilog2001Parser.Net_typeContext
    ) -> PortType:
        return PortType(PortTypeEnum.VECTOR, "")

    def visitOutput_variable_type(
        self, ctx: Verilog2001Parser.Output_variable_typeContext
    ) -> PortType:
        return PortType(PortTypeEnum.VECTOR, "")

    def visitList_of_ports(
        self, ctx: Verilog2001Parser.List_of_portsContext
    ) -> None:
        for p in ctx.port():
            self.visitPort(p)

    def visitPort(self, ctx: Verilog2001Parser.PortContext) -> None:
        if ctx.port_identifier():
            self.entities[-1].add_port(
                Port(
                    self.visitPort_identifier(ctx.port_identifier()),
                    None,
                    None,
                )
            )
        else:
            for p in self.visitPort_expression(ctx.port_expression()):
                self.entities[-1].add_port(Port(p, None, None))

    def visitPort_identifier(
        self, ctx: Verilog2001Parser.Port_identifierContext
    ) -> str:
        return self.visitIdentifier(ctx.identifier())

    def visitPort_expression(
        self, ctx: Verilog2001Parser.Port_expressionContext
    ) -> List[str]:
        refs = []
        for pr in ctx.port_reference():
            refs.append(self.visitPort_reference(pr))
        return refs

    def visitPort_reference(
        self, ctx: Verilog2001Parser.Port_referenceContext
    ) -> str:
        if ctx.constant_expression():
            pass
        if ctx.range_expression():
            pass

        return self.visitPort_identifier(ctx.port_identifier())

    def visitModule_parameter_port_list(
        self, ctx: Verilog2001Parser.Module_parameter_port_listContext
    ) -> None:
        for p in ctx.parameter_declaration_():
            self.visitParameter_declaration_(p)

    def visitParameter_declaration(
        self, ctx: Verilog2001Parser.Parameter_declarationContext
    ) -> None:
        self.visitParameter_declaration_(ctx.parameter_declaration_())

    def visitParameter_declaration_(
        self, ctx: Verilog2001Parser.Parameter_declaration_Context
    ) -> None:
        for pa in self.visitList_of_param_assignments(
            ctx.list_of_param_assignments()
        ):
            if "integer" in ctx.getText()[9 : 9 + len("integer")]:
                self.entities[-1].add_parameter(
                    Parameter(
                        pa,
                        ParameterType(ParameterTypeEnum.INTEGER, "integer"),
                    )
                )
            if "time" in ctx.getText()[9 : 9 + len("time")]:
                self.entities[-1].add_parameter(
                    Parameter(
                        pa, ParameterType(ParameterTypeEnum.INTEGER, "time"),
                    )
                )
            else:
                self.entities[-1].add_parameter(
                    Parameter(
                        pa,
                        ParameterType(ParameterTypeEnum.INTEGER, "integer"),
                    )
                )

                pass

    def visitList_of_param_assignments(
        self, ctx: Verilog2001Parser.List_of_param_assignmentsContext
    ) -> List[str]:
        params = []
        for p in ctx.param_assignment():
            params.append(self.visitParam_assignment(p))
        return params

    def visitParam_assignment(
        self, ctx: Verilog2001Parser.Param_assignmentContext
    ) -> str:
        return self.visitParameter_identifier(ctx.parameter_identifier())

    def visitParameter_identifier(
        self, ctx: Verilog2001Parser.Parameter_identifierContext
    ) -> str:
        return self.visitIdentifier(ctx.identifier())

    def visitModule_identifier(
        self, ctx: Verilog2001Parser.Module_identifierContext
    ) -> str:
        return self.visitIdentifier(ctx.identifier())

    def visitIdentifier(self, ctx: Verilog2001Parser.IdentifierContext) -> str:
        if ctx.Simple_identifier():
            return ctx.Simple_identifier().getText()
        else:
            return ctx.Escaped_identifier().getText()

