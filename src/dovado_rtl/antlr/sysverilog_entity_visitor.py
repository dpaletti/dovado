from dovado_rtl.antlr.hdl_representation import (
    Entity,
    ParameterType,
    ParameterTypeEnum,
    Port,
    Parameter,
    PortDirection,
    PortDirectionEnum,
    PortType,
    PortTypeEnum,
)
from itertools import chain
from typing import List, Tuple, Iterator, Union
from dovado_rtl.antlr.generated.SystemVerilog.SystemVerilogParserVisitor import (
    SystemVerilogParserVisitor,
)
from dovado_rtl.antlr.generated.SystemVerilog.SystemVerilogParser import (
    SystemVerilogParser,
)


class SysVerilogHDLEntityVisitor(SystemVerilogParserVisitor):
    def __init__(self):
        self.entities: List[Entity] = []
        self.top_level = None

    def visitSource_text(
        self, ctx: SystemVerilogParser.Source_textContext
    ) -> None:
        for d in ctx.description():
            self.visitDescription(d)

    def visitDescription(
        self, ctx: SystemVerilogParser.DescriptionContext
    ) -> None:
        if ctx.module_declaration():
            self.visitModule_declaration(ctx.module_declaration())
        else:
            pass

    def visitModule_declaration(
        self, ctx: SystemVerilogParser.Module_declarationContext
    ) -> None:
        if ctx.module_nonansi_header():
            self.visitModule_nonansi_header(ctx.module_nonansi_header())
        elif ctx.module_ansi_header():
            self.visitModule_ansi_header(ctx.module_ansi_header())
        else:
            self.entities.append(
                Entity(self.visitModule_identifier(ctx.module_identifier()[0]))
            )

    def visitModule_nonansi_header(
        self, ctx: SystemVerilogParser.Module_nonansi_headerContext
    ):
        self.entities.append(
            Entity(self.visitModule_identifier(ctx.module_identifier()))
        )
        if ctx.parameter_port_list():
            self.visitParameter_port_list(ctx.parameter_port_list())
        print("Non-Ansi ports found, skipping...")
        # self.visitList_of_ports(ctx.list_of_ports())

    def visitList_of_ports(
        self, ctx: SystemVerilogParser.List_of_portsContext
    ):
        for i in ctx.port():
            self.visitPort(i)

    def visitList_of_port_declarations(
        self, ctx: SystemVerilogParser.List_of_port_declarationsContext
    ):
        for i in ctx.ansi_port_declaration():
            self.visitAnsi_port_declaration(i)

    def visitAnsi_port_declaration(
        self, ctx: SystemVerilogParser.Ansi_port_declarationContext
    ):
        direction = None
        if ctx.net_port_header():
            direction = self.visitNet_port_header(ctx.net_port_header())
        if ctx.variable_port_header():
            direction = self.visitVariable_port_header(
                ctx.variable_port_header()
            )
        if ctx.port_direction():
            direction = self.visitPort_direction()
        if direction:
            ident = self.visitPort_identifier(ctx.port_identifier())

            self.entities[-1].add_port(Port(ident, direction, None))

    def visitNet_port_header(
        self, ctx: SystemVerilogParser.Net_port_headerContext
    ):
        if ctx.port_direction():
            return self.visitPort_direction(ctx.port_direction())
        return None

    def visitVariable_port_header(
        self, ctx: SystemVerilogParser.Variable_port_headerContext
    ):
        if ctx.port_direction():
            return self.visitPort_direction(ctx.port_direction())
        return None

    def visitPort_direction(
        self, ctx: SystemVerilogParser.Port_directionContext
    ):
        if ctx.KINPUT():
            return PortDirection(PortDirectionEnum.INPUT, descriptor="input")
        if ctx.KOUTPUT():
            return PortDirection(PortDirectionEnum.OUTPUT, descriptor="output")
        if ctx.KINOUT():
            return PortDirection(PortDirectionEnum.OTHER, descriptor="inout")
        return None

    def visitModule_ansi_header(
        self, ctx: SystemVerilogParser.Module_ansi_headerContext
    ):
        self.entities.append(
            Entity(self.visitModule_identifier(ctx.module_identifier()))
        )
        if ctx.parameter_port_list():
            self.visitParameter_port_list(ctx.parameter_port_list())
        if ctx.list_of_port_declarations():
            self.visitList_of_port_declarations(
                ctx.list_of_port_declarations()
            )

    def visitParameter_port_list(
        self, ctx: SystemVerilogParser.Parameter_port_listContext
    ):
        for i in ctx.parameter_port_declaration():
            self.visitParameter_port_declaration(i)
        if ctx.list_of_param_assignments():
            self.visitList_of_param_assignments(
                ctx.list_of_param_assignments()
            )

    def visitList_of_param_assignments(
        self, ctx: SystemVerilogParser.List_of_param_assignmentsContext
    ):
        for i in ctx.param_assignment():
            yield self.visitParam_assignment(i)

    def visitParam_assignment(
        self, ctx: SystemVerilogParser.Param_assignmentContext
    ):

        return self.visitParameter_identifier(ctx.parameter_identifier())

    def visitParameter_identifier(
        self, ctx: SystemVerilogParser.Parameter_identifierContext
    ):
        return self.visitIdentifier(ctx.identifier())

    def visitParameter_port_declaration(
        self, ctx: SystemVerilogParser.Parameter_port_declarationContext
    ):
        if ctx.parameter_declaration():
            self.visitParameter_declaration(ctx.parameter_declaration())

    def visitList_of_port_declarations(
        self, ctx: SystemVerilogParser.List_of_port_declarationsContext
    ) -> None:
        for p in ctx.ansi_port_declaration():
            self.visitAnsi_port_declaration(p)

    def visitList_of_port_declarations_comma(self, ctx) -> None:
        self.visitAttr_port_declaration(ctx.attr_port_declaration())
        self.visitComma_attr_port_declaration_star(
            ctx.comma_attr_port_declaration_star()
        )

    def visitComma_attr_port_declaration_star(self, ctx) -> None:
        if not ctx.comma_attr_port_declaration():
            return
        for a in ctx.comma_attr_port_declaration():
            self.visitComma_attr_port_declaration(a)

    def visitComma_attr_port_declaration(self, ctx) -> None:
        self.visitAttr_port_declaration(ctx.attr_port_declaration())

    def visitList_of_port_declarations_semicolon(self, ctx) -> None:
        self.visitAttr_port_declaration_semicolon_plus(
            ctx.attr_port_declaration_semicolon_plus()
        )

    def visitAttr_port_declaration_semicolon_plus(self, ctx) -> None:
        for a in ctx.attr_port_declaration_semicolon():
            self.visitAttr_port_declaration_semicolon(a)

    def visitAttr_port_declaration_semicolon(self, ctx) -> None:
        self.visitAttr_port_declaration(ctx.attr_port_declaration())

    def visitAttr_port_declaration(self, ctx) -> None:
        self.visitPort_declaration(ctx.port_declaration())

    def visitPort_declaration(
        self, ctx: SystemVerilogParser.Port_declarationContext
    ) -> None:
        if ctx.inout_declaration():
            self.visitInout_declaration(ctx.inout_declaration())
        if ctx.input_declaration():
            self.visitInput_declaration(ctx.input_declaration())
        if ctx.output_declaration():
            self.visitOutput_declaration(ctx.output_declaration())
        if ctx.ref_declaration():
            print("Ref ports not supported, skipping")

    def visitInout_declaration(
        self, ctx: SystemVerilogParser.Inout_declarationContext
    ) -> None:
        for ident in self.visitList_of_port_identifiers(
            ctx.list_of_port_identifiers()
        ):
            self.entities[-1].add_port(
                Port(
                    ident,
                    PortDirection(PortDirectionEnum.OTHER, "inout"),
                    None,
                )
            )

    def visitInput_declaration(
        self, ctx: SystemVerilogParser.Input_declarationContext
    ) -> None:
        for ident in self.visitList_of_port_identifiers(
            ctx.list_of_port_identifiers()
        ):
            self.entities[-1].add_port(
                Port(
                    ident,
                    PortDirection(PortDirectionEnum.INPUT, "input"),
                    None,
                )
            )

    def visitOutput_declaration(
        self, ctx: SystemVerilogParser.Output_declarationContext
    ) -> None:
        for ident in self.visitList_of_port_identifiers(
            ctx.list_of_port_identifiers()
        ):
            self.entities[-1].add_port(
                Port(
                    ident,
                    PortDirection(PortDirectionEnum.OUTPUT, "output"),
                    None,
                )
            )

    def visitList_of_port_identifiers(
        self, ctx: SystemVerilogParser.List_of_port_identifiersContext
    ) -> None:
        for i in self.visitPort_identifier(ctx.port_identifier()):
            yield self.visitPort_identifier(i)

    def visitPort_identifier(
        self, ctx: SystemVerilogParser.Port_identifierContext
    ) -> str:
        return self.visitIdentifier(ctx.identifier())

    def visitList_of_interface_parameters(self, ctx) -> None:
        if ctx.list_of_parameter_declarations():
            self.visitList_of_parameter_declarations(
                ctx.list_of_parameter_declarations()
            )
        if ctx.list_of_parameter_descriptions():
            self.visitList_of_parameter_descriptions(
                ctx.list_of_parameter_descriptions()
            )

    def visitList_of_parameter_declarations(self, ctx) -> None:
        self.visitParameter_declaration(ctx.parameter_declaration())
        self.visitComma_parameter_declaration_star(
            ctx.comma_parameter_declaration_star()
        )

    def visitComma_parameter_declaration_star(self, ctx) -> None:
        if not ctx.comma_parameter_declaration():
            return
        for p in ctx.comma_parameter_declaration():
            self.visitComma_parameter_declaration(p)

    def visitComma_parameter_declaration(self, ctx) -> None:
        self.visitParameter_declaration(ctx.parameter_declaration())

    def visitParameter_declaration(
        self, ctx: SystemVerilogParser.Parameter_declarationContext
    ) -> None:
        param_type = self.visitData_type_or_implicit(
            ctx.data_type_or_implicit()
        )
        if param_type:
            for param in self.visitList_of_param_assignments(
                ctx.list_of_param_assignments()
            ):
                self.entities[-1].add_parameter(
                    Parameter(str(param), param_type)
                )

    def visitData_type(self, ctx: SystemVerilogParser.Data_typeContext):
        if ctx.integer_atom_type():
            return self.visitInteger_atom_type(ctx.integer_atom_type())
        else:
            return None

    def visitInteger_atom_type(
        self, ctx: SystemVerilogParser.Integer_atom_typeContext
    ):
        if ctx.KBYTE():
            return ParameterType(ParameterTypeEnum.INTEGER, "byte")
        if ctx.KSHORTINT():
            return ParameterType(ParameterTypeEnum.INTEGER, "shortint")
        if ctx.KINT():
            return ParameterType(ParameterTypeEnum.INTEGER, "int")
        if ctx.KLONGINT():
            return ParameterType(ParameterTypeEnum.INTEGER, "longint")
        if ctx.KINTEGER():
            return ParameterType(ParameterTypeEnum.INTEGER, "integer")
        if ctx.KTIME():
            return ParameterType(ParameterTypeEnum.INTEGER, "time")

    def visitParam_description(self, ctx) -> None:
        if ctx.param_declaration():
            for v in self.visitParam_declaration(ctx.param_declaration()):
                self.entities[-1].add_parameter(Parameter(v[0], v[1]))

        for d in chain(
            self.visitLogic_declaration(ctx.logic_declaration())
            if ctx.logic_declaration()
            else iter(()),
            self.visitInteger_declaration(ctx.integer_declaration())
            if ctx.integer_declaration()
            else iter(()),
            self.visitInt_declaration(ctx.int_declaration())
            if ctx.int_declaration()
            else iter(()),
            self.visitTime_declaration(ctx.time_declaration())
            if ctx.time_declaration()
            else iter(()),
        ):
            self.entities[-1].add_parameter(Parameter(d[0], d[1]))
        if ctx.usertype_variable_declaration():
            print("UserType parameters are not supported, skipping")
        else:
            # non numeric or non synthesizable types skipped
            pass

    def visitParam_declaration(self, ctx) -> List[Tuple[str, ParameterType]]:
        out = []
        if ctx.Signed():
            for v in self.visitList_of_hierarchical_variable_descriptions(
                ctx.list_of_hierarchical_variable_descriptions()
            ):
                out.append(
                    (v, ParameterType(ParameterTypeEnum.INTEGER, "Signed"))
                )
        if ctx.Unsigned():
            for v in self.visitList_of_hierarchical_variable_descriptions(
                ctx.list_of_hierarchical_variable_descriptions()
            ):
                out.append(
                    (v, ParameterType(ParameterTypeEnum.INTEGER, "Unsigned"))
                )
        else:
            for v in self.visitList_of_hierarchical_variable_descriptions(
                ctx.list_of_hierarchical_variable_descriptions()
            ):
                out.append((v, ParameterType(ParameterTypeEnum.INTEGER, "")))
        return out

    def visitBits_declaration(
        self, ctx
    ) -> Iterator[Tuple[str, ParameterType]]:
        for v in self.visitList_of_variable_descriptions(
            ctx.list_of_variable_descriptions()
        ):
            b_type = self.visitBits_type(ctx.bits_type())
            b_type += "signed" if ctx.Signed() else ""
            b_type += "unsigned" if ctx.Unsigned() else ""
            yield v, ParameterType(ParameterTypeEnum.INTEGER, b_type)

    def visitBits_type(self, ctx) -> str:
        if ctx.Bit():
            return ctx.Bit().getText()
        else:
            return ctx.Byte().getText()

    def visitNet_declaration(
        self, ctx: SystemVerilogParser.Net_declarationContext
    ) -> Iterator[Tuple[str, PortType]]:
        for v in self.visitList_of_variable_descriptions(
            ctx.list_of_variable_descriptions()
        ):
            net: PortType = self.visitNet_type(ctx.net_type())
            p_type = net.descriptor
            p_type += "vectored" if ctx.Vectored() else ""
            p_type += "scalared" if ctx.Scalared() else ""
            p_type += "signed" if ctx.Signed() else ""
            p_type += "unsigned" if ctx.Unsigned() else ""
            yield v, PortType(net.type, p_type)

    def visitNet_type(
        self, ctx: SystemVerilogParser.Net_typeContext
    ) -> PortType:
        if ctx.Supply0():
            return PortType(PortTypeEnum.VECTOR, ctx.Supply0().getText())
        if ctx.Supply1():
            return PortType(PortTypeEnum.VECTOR, ctx.Supply1().getText())
        if ctx.Tri():
            return PortType(PortTypeEnum.VECTOR, ctx.Tri().getText())
        if ctx.Tri_and():
            return PortType(PortTypeEnum.VECTOR, ctx.Tri_and().getText())
        if ctx.Tri_or():
            return PortType(PortTypeEnum.VECTOR, ctx.Tri_or().getText())
        if ctx.Tri_reg():
            return PortType(PortTypeEnum.VECTOR, ctx.Tri_reg().getText())
        if ctx.Tri0():
            return PortType(PortTypeEnum.VECTOR, ctx.Tri0().getText())
        if ctx.Tri1():
            return PortType(PortTypeEnum.VECTOR, ctx.Tri1().getText())
        if ctx.Uwire():
            return PortType(PortTypeEnum.VECTOR, ctx.Uwire().getText())
        if ctx.Wire():
            return PortType(PortTypeEnum.VECTOR, ctx.Wire().getText())
        if ctx.Wand():
            return PortType(PortTypeEnum.VECTOR, ctx.Wand().getText())
        if ctx.Wor():
            return PortType(PortTypeEnum.VECTOR, ctx.Wor().getText())
        return PortType(PortTypeEnum.VECTOR, ctx.NONE().getText())

    def visitLogic_declaration(
        self, ctx
    ) -> Union[
        Iterator[Tuple[str, ParameterType]], Iterator[Tuple[str, PortType]]
    ]:
        for v in self.visitList_of_variable_descriptions(
            ctx.list_of_variable_descriptions()
        ):
            if isinstance(
                ctx.parentCtx.parentCtx.parentCtx,
                SystemVerilogParser.Port_declarationContext,
            ):
                yield v, PortType(PortTypeEnum.SCALAR, "Logic")

            else:
                yield v, ParameterType(ParameterTypeEnum.INTEGER, "Logic")

    def visitInteger_declaration(
        self, ctx
    ) -> Union[
        Iterator[Tuple[str, ParameterType]], Iterator[Tuple[str, PortType]]
    ]:
        for v in self.visitList_of_variable_descriptions(
            ctx.list_of_variable_descriptions()
        ):
            p_type = "automatic" if ctx.Automatic() else ""
            p_type += "integer"
            p_type += "signed" if ctx.Signed() else ""
            p_type += "unsigned" if ctx.Unsigned() else ""
            if isinstance(
                ctx.parentCtx.parentCtx.parentCtx,
                SystemVerilogParser.Port_declarationContext,
            ):
                yield v, PortType(PortTypeEnum.SCALAR, p_type)
            else:
                yield v, ParameterType(ParameterTypeEnum.INTEGER, p_type)

    def visitInt_declaration(
        self, ctx
    ) -> Union[
        Iterator[Tuple[str, ParameterType]], Iterator[Tuple[str, PortType]]
    ]:
        for v in self.visitList_of_variable_descriptions(
            ctx.list_of_variable_descriptions()
        ):

            p_type = "automatic" if ctx.Automatic() else ""
            p_type += "static" if ctx.Static() else ""
            p_type += "const" if ctx.Const() else ""
            p_type += "integer"
            p_type += "signed" if ctx.Signed() else ""
            p_type += "unsigned" if ctx.Unsigned() else ""
            if isinstance(
                ctx.parentCtx.parentCtx.parentCtx,
                SystemVerilogParser.Port_declarationContext,
            ):
                yield v, PortType(PortTypeEnum.SCALAR, p_type)
            else:
                yield v, ParameterType(ParameterTypeEnum.INTEGER, p_type)

    def visitTime_declaration(
        self, ctx
    ) -> Union[
        Iterator[Tuple[str, ParameterType]], Iterator[Tuple[str, PortType]]
    ]:

        for v in self.visitList_of_variable_descriptions(
            ctx.list_of_variable_descriptions()
        ):
            if isinstance(
                ctx.parentCtx.parentCtx.parentCtx,
                SystemVerilogParser.Port_declarationContext,
            ):
                yield v, PortType(PortTypeEnum.SCALAR, "Time")
            else:
                yield v, ParameterType(ParameterTypeEnum.INTEGER, "Time")

    def visitList_of_hierarchical_variable_descriptions(
        self, ctx
    ) -> List[str]:
        vds = self.visitHierarchical_variable_description(
            ctx.hierarchical_variable_description()
        )

        vds.extend(
            self.visitComma_hierarchical_variable_description_star(
                ctx.comma_hierarchical_variable_description_star()
            )
        )
        return vds

    def visitComma_hierarchical_variable_description_star(
        self, ctx
    ) -> List[str]:
        out = []
        for h in ctx.comma_hierarchical_variable_description():
            out.extend(self.visitComma_hierarchical_variable_description(h))
        return out

    def visitComma_hierarchical_variable_description(self, ctx) -> List[str]:
        return self.visitHierarchical_variable_description(
            ctx.hierarchical_variable_description()
        )

    def visitHierarchical_variable_description(self, ctx) -> List[str]:
        return self.visitHierarchical_variable_identifier(
            ctx.hierarchical_variable_identifier()
        )

    def visitHierarchical_variable_identifier(
        self, ctx: SystemVerilogParser.Hierarchical_variable_identifierContext
    ) -> List[str]:
        return self.visitHierarchical_identifier(ctx.hierarchical_identifier())

    def visitHierarchical_identifier(
        self, ctx: SystemVerilogParser.Hierarchical_identifierContext
    ) -> List[str]:
        out = [
            self.visitHierarchical_identifier_branch_item(
                ctx.hierarchical_identifier_branch_item()
            )
        ]
        out.extend(
            self.visitDot_hierarchical_identifier_branch_item_star(
                ctx.dot_hierarchical_identifier_branch_item_star()
            )
        )
        return out

    def visitDot_hierarchical_identifier_branch_item_star(
        self, ctx
    ) -> List[str]:
        out = []
        for h in ctx.dot_hierarchical_identifier_branch_item():
            out.append(self.visitDot_hierarchical_identifier_branch_item(h))
        return out

    def visitDot_hierarchical_identifier_branch_item(self, ctx) -> str:
        return self.visitHierarchical_identifier_branch_item(
            ctx.hierarchical_identifier_branch_item()
        )

    def visitHierarchical_identifier_branch_item(self, ctx):
        return self.visitIdentifier(ctx.identifier())

    def visitList_of_variable_descriptions(
        self, ctx: SystemVerilogParser
    ) -> List[str]:
        vds = [self.visitVariable_description(ctx.variable_description())]
        vds.extend(
            self.visitComma_variable_description_star(
                ctx.comma_variable_description_star()
            )
        )
        return vds

    def visitComma_variable_description_star(
        self, ctx: SystemVerilogParser
    ) -> List[str]:
        vds = []
        for v in ctx.comma_variable_description():
            vds.append(self.visitComma_variable_description(v))
        return vds

    def visitComma_variable_description(self, ctx: SystemVerilogParser) -> str:
        return self.visitVariable_description(ctx.variable_description())

    def visitVariable_description(self, ctx: SystemVerilogParser) -> str:
        return self.visitVariable_identifier(ctx.variable_identifier())

    def visitVariable_identifier(
        self, ctx: SystemVerilogParser.Variable_identifierContext
    ) -> str:
        return self.visitIdentifier(ctx.identifier())

    def visitModule_identifier(
        self, ctx: SystemVerilogParser.Module_identifierContext
    ) -> str:
        return self.visitIdentifier(ctx.identifier())

    def visitIdentifier(
        self, ctx: SystemVerilogParser.IdentifierContext
    ) -> str:
        return ctx.SIMPLE_IDENTIFIER().getText()
