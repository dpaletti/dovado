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
from dovado_rtl.antlr.generated.SysVerilogHDL.SysVerilogHDLVisitor import (
    SysVerilogHDLVisitor,
)
from dovado_rtl.antlr.generated.SysVerilogHDL.SysVerilogHDLParser import (
    SysVerilogHDLParser,
)


class SysVerilogHDLEntityVisitor(SysVerilogHDLVisitor):
    def __init__(self):
        self.entities: List[Entity] = []
        self.top_level = None

    def visitSource_text(
        self, ctx: SysVerilogHDLParser.Source_textContext
    ) -> None:
        self.visitDescription_star(ctx.description_star())

    def visitDescription_star(
        self, ctx: SysVerilogHDLParser.Description_starContext
    ) -> None:
        if not ctx.description():
            return
        for d in ctx.description():
            self.visitDescription(d)

    def visitDescription(
        self, ctx: SysVerilogHDLParser.DescriptionContext
    ) -> None:
        if ctx.module_declaration():
            self.visitModule_declaration(ctx.module_declaration())
        else:
            pass

    def visitModule_declaration(
        self, ctx: SysVerilogHDLParser.Module_declarationContext
    ) -> None:
        self.entities.append(
            Entity(self.visitModule_identifier(ctx.module_identifier()))
        )
        self.visitModule_interface(ctx.module_interface())
        self.visitModule_item_star(ctx.module_item_star())

    def visitModule_interface(
        self, ctx: SysVerilogHDLParser.Module_interfaceContext
    ) -> None:
        if ctx.module_parameter_interface():
            self.visitModule_parameter_interface(
                ctx.module_parameter_interface()
            )
        if ctx.module_port_interface():
            self.visitModule_port_interface(ctx.module_port_interface())

    def visitModule_parameter_interface(
        self, ctx: SysVerilogHDLParser.Module_parameter_interfaceContext
    ) -> None:
        if ctx.list_of_interface_parameters():
            self.visitList_of_interface_parameters(
                ctx.list_of_interface_parameters()
            )

    def visitModule_port_interface(
        self, ctx: SysVerilogHDLParser.Module_port_interfaceContext
    ) -> None:
        if ctx.list_of_interface_ports():
            self.visitList_of_interface_ports(ctx.list_of_interface_ports())

    def visitList_of_interface_ports(
        self, ctx: SysVerilogHDLParser.List_of_interface_portsContext
    ) -> None:
        if ctx.list_of_port_identifiers():
            self.visitList_of_port_identifiers(ctx.list_of_port_identifiers())
        if ctx.list_of_port_declarations():
            self.visitList_of_port_declarations(
                ctx.list_of_port_declarations()
            )

    def visitList_of_port_declarations(
        self, ctx: SysVerilogHDLParser.List_of_port_declarationsContext
    ) -> None:
        if ctx.list_of_port_declarations_comma():
            self.visitList_of_port_declarations_comma(
                ctx.list_of_port_declarations_comma()
            )
        if ctx.list_of_port_declarations_semicolon():
            self.visitList_of_port_declarations_semicolon(
                ctx.list_of_port_declarations_semicolon()
            )

    def visitList_of_port_declarations_comma(
        self, ctx: SysVerilogHDLParser.List_of_port_declarations_commaContext
    ) -> None:
        self.visitAttr_port_declaration(ctx.attr_port_declaration())
        self.visitComma_attr_port_declaration_star(
            ctx.comma_attr_port_declaration_star()
        )

    def visitComma_attr_port_declaration_star(
        self, ctx: SysVerilogHDLParser.Comma_attr_port_declaration_starContext
    ) -> None:
        if not ctx.comma_attr_port_declaration():
            return
        for a in ctx.comma_attr_port_declaration():
            self.visitComma_attr_port_declaration(a)

    def visitComma_attr_port_declaration(
        self, ctx: SysVerilogHDLParser.Comma_attr_port_declarationContext
    ) -> None:
        self.visitAttr_port_declaration(ctx.attr_port_declaration())

    def visitList_of_port_declarations_semicolon(
        self,
        ctx: SysVerilogHDLParser.List_of_port_declarations_semicolonContext,
    ) -> None:
        self.visitAttr_port_declaration_semicolon_plus(
            ctx.attr_port_declaration_semicolon_plus()
        )

    def visitAttr_port_declaration_semicolon_plus(
        self,
        ctx: SysVerilogHDLParser.Attr_port_declaration_semicolon_plusContext,
    ) -> None:
        for a in ctx.attr_port_declaration_semicolon():
            self.visitAttr_port_declaration_semicolon(a)

    def visitAttr_port_declaration_semicolon(
        self, ctx: SysVerilogHDLParser.Attr_port_declaration_semicolonContext
    ) -> None:
        self.visitAttr_port_declaration(ctx.attr_port_declaration())

    def visitAttr_port_declaration(
        self, ctx: SysVerilogHDLParser.Attr_port_declarationContext
    ) -> None:
        self.visitPort_declaration(ctx.port_declaration())

    def visitPort_declaration(
        self, ctx: SysVerilogHDLParser.Port_declarationContext
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
        self, ctx: SysVerilogHDLParser.Inout_declarationContext
    ) -> None:
        self.visitInout_description(ctx.inout_description())

    def visitInput_declaration(
        self, ctx: SysVerilogHDLParser.Input_declarationContext
    ) -> None:
        self.visitInput_description(ctx.input_description())

    def visitOutput_declaration(
        self, ctx: SysVerilogHDLParser.Output_declarationContext
    ) -> None:
        self.visitOutput_description(ctx.output_description())

    def visitInout_description(
        self, ctx: SysVerilogHDLParser.Inout_descriptionContext
    ) -> None:
        for p in self.visitPort_description(ctx.port_description()):
            self.entities[-1].add_port(
                Port(
                    p[0], PortDirection(PortDirectionEnum.OTHER, "inout"), p[1]
                )
            )

    def visitInput_description(
        self, ctx: SysVerilogHDLParser.Input_descriptionContext
    ):
        if ctx.port_description():
            self.visitPort_description(ctx.port_description())
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
            self.visitNet_declaration(ctx.net_declaration())
            if ctx.net_declaration()
            else iter(()),
            self.visitBits_declaration(ctx.bits_declaration())
            if ctx.bits_declaration()
            else iter(()),
        ):
            p_type = d[1]
            if isinstance(p_type, PortType):
                self.entities[-1].add_port(
                    Port(
                        d[0],
                        PortDirection(PortDirectionEnum.INPUT, "input"),
                        p_type,
                    )
                )

    def visitOutput_description(
        self, ctx: SysVerilogHDLParser.Output_descriptionContext
    ):
        if ctx.port_description():
            for p in self.visitPort_description(ctx.port_description()):
                self.entities[-1].add_port(
                    Port(
                        p[0],
                        PortDirection(PortDirectionEnum.OUTPUT, "output"),
                        p[1],
                    )
                )

        for d in chain(
            self.visitLogic_declaration(ctx.logic_declaration())
            if ctx.logic_declaration()
            else iter(()),
            self.visitInteger_declaration(ctx.integer_declaration())
            if ctx.integer_declaration()
            else iter(()),
            self.visitTime_declaration(ctx.time_declaration())
            if ctx.time_declaration()
            else iter(()),
            self.visitNet_declaration(ctx.net_declaration())
            if ctx.net_declaration()
            else iter(()),
        ):
            p_type = d[1]
            if isinstance(p_type, PortType):
                self.entities[-1].add_port(
                    Port(
                        d[0],
                        PortDirection(PortDirectionEnum.OUTPUT, "output"),
                        p_type,
                    )
                )
            else:
                pass

    def visitPort_description(
        self, ctx: SysVerilogHDLParser.Port_descriptionContext
    ) -> Iterator[Tuple[str, PortType]]:
        if ctx.Signed():
            for v in ctx.list_of_variable_descriptions():
                yield v, PortType(PortTypeEnum.VECTOR, "Signed")
        if ctx.Unsigned():
            for v in ctx.list_of_variable_descriptions():
                yield v, PortType(PortTypeEnum.VECTOR, "Unsigned")
        else:
            for v in ctx.list_of_variable_descriptions():
                yield v, PortType(PortTypeEnum.VECTOR, "")

    def visitList_of_port_identifiers(
        self, ctx: SysVerilogHDLParser.List_of_port_identifiersContext
    ) -> None:
        self.visitPort_identifier(ctx.port_identifier())
        self.visitComma_port_identifier_star(ctx.comma_port_identifier_star())

    def visitComma_port_identifier_star(
        self, ctx: SysVerilogHDLParser.Comma_port_identifier_starContext
    ) -> None:
        if not ctx.comma_port_identifier():
            return
        for i in ctx.comma_port_identifier():
            self.visitComma_port_identifier(i)

    def visitComma_port_identifier(
        self, ctx: SysVerilogHDLParser.Comma_port_identifierContext
    ) -> None:
        self.visitPort_identifier(ctx.port_identifier())

    def visitPort_identifier(
        self, ctx: SysVerilogHDLParser.Port_identifierContext
    ) -> None:
        self.entities[-1].add_port(
            Port(self.visitIdentifier(ctx.identifier()), None, None)
        )

    def visitList_of_interface_parameters(
        self, ctx: SysVerilogHDLParser.List_of_interface_parametersContext
    ) -> None:
        if ctx.list_of_parameter_declarations():
            self.visitList_of_parameter_declarations(
                ctx.list_of_parameter_declarations()
            )
        if ctx.list_of_parameter_descriptions():
            self.visitList_of_parameter_descriptions(
                ctx.list_of_parameter_descriptions()
            )

    def visitList_of_parameter_declarations(
        self, ctx: SysVerilogHDLParser.List_of_parameter_declarationsContext
    ) -> None:
        self.visitParameter_declaration(ctx.parameter_declaration())
        self.visitComma_parameter_declaration_star(
            ctx.comma_parameter_declaration_star()
        )

    def visitComma_parameter_declaration_star(
        self, ctx: SysVerilogHDLParser.Comma_parameter_declaration_starContext
    ) -> None:
        if not ctx.comma_parameter_declaration():
            return
        for p in ctx.comma_parameter_declaration():
            self.visitComma_parameter_declaration(p)

    def visitComma_parameter_declaration(
        self, ctx: SysVerilogHDLParser.Comma_parameter_declarationContext
    ) -> None:
        self.visitParameter_declaration(ctx.parameter_declaration())

    def visitParameter_declaration(
        self, ctx: SysVerilogHDLParser.Parameter_declarationContext
    ) -> None:
        self.visitParam_description(ctx.param_description())

    def visitParam_description(
        self, ctx: SysVerilogHDLParser.Param_descriptionContext
    ) -> None:
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

    def visitParam_declaration(
        self, ctx: SysVerilogHDLParser.Param_declarationContext
    ) -> List[Tuple[str, ParameterType]]:
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
        self, ctx: SysVerilogHDLParser.Bits_declarationContext
    ) -> Iterator[Tuple[str, ParameterType]]:
        for v in self.visitList_of_variable_descriptions(
            ctx.list_of_variable_descriptions()
        ):
            b_type = self.visitBits_type(ctx.bits_type())
            b_type += "signed" if ctx.Signed() else ""
            b_type += "unsigned" if ctx.Unsigned() else ""
            yield v, ParameterType(ParameterTypeEnum.INTEGER, b_type)

    def visitBits_type(self, ctx: SysVerilogHDLParser.Bits_typeContext) -> str:
        if ctx.Bit():
            return ctx.Bit().getText()
        else:
            return ctx.Byte().getText()

    def visitNet_declaration(
        self, ctx: SysVerilogHDLParser.Net_declarationContext
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
        self, ctx: SysVerilogHDLParser.Net_typeContext
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
        self, ctx: SysVerilogHDLParser.Logic_declarationContext
    ) -> Union[
        Iterator[Tuple[str, ParameterType]], Iterator[Tuple[str, PortType]]
    ]:
        for v in self.visitList_of_variable_descriptions(
            ctx.list_of_variable_descriptions()
        ):
            if isinstance(
                ctx.parentCtx.parentCtx.parentCtx,
                SysVerilogHDLParser.Port_declarationContext,
            ):
                yield v, PortType(PortTypeEnum.SCALAR, "Logic")

            else:
                yield v, ParameterType(ParameterTypeEnum.INTEGER, "Logic")

    def visitInteger_declaration(
        self, ctx: SysVerilogHDLParser.Integer_declarationContext
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
                SysVerilogHDLParser.Port_declarationContext,
            ):
                yield v, PortType(PortTypeEnum.SCALAR, p_type)
            else:
                yield v, ParameterType(ParameterTypeEnum.INTEGER, p_type)

    def visitInt_declaration(
        self, ctx: SysVerilogHDLParser.Int_declarationContext
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
                SysVerilogHDLParser.Port_declarationContext,
            ):
                yield v, PortType(PortTypeEnum.SCALAR, p_type)
            else:
                yield v, ParameterType(ParameterTypeEnum.INTEGER, p_type)

    def visitTime_declaration(
        self, ctx: SysVerilogHDLParser.Time_declarationContext
    ) -> Union[
        Iterator[Tuple[str, ParameterType]], Iterator[Tuple[str, PortType]]
    ]:

        for v in self.visitList_of_variable_descriptions(
            ctx.list_of_variable_descriptions()
        ):
            if isinstance(
                ctx.parentCtx.parentCtx.parentCtx,
                SysVerilogHDLParser.Port_declarationContext,
            ):
                yield v, PortType(PortTypeEnum.SCALAR, "Time")
            else:
                yield v, ParameterType(ParameterTypeEnum.INTEGER, "Time")

    def visitList_of_hierarchical_variable_descriptions(
        self,
        ctx: SysVerilogHDLParser.List_of_hierarchical_variable_descriptionsContext,
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
        self,
        ctx: SysVerilogHDLParser.Comma_hierarchical_variable_description_starContext,
    ) -> List[str]:
        out = []
        for h in ctx.comma_hierarchical_variable_description():
            out.extend(self.visitComma_hierarchical_variable_description(h))
        return out

    def visitComma_hierarchical_variable_description(
        self,
        ctx: SysVerilogHDLParser.Comma_hierarchical_variable_descriptionContext,
    ) -> List[str]:
        return self.visitHierarchical_variable_description(
            ctx.hierarchical_variable_description()
        )

    def visitHierarchical_variable_description(
        self, ctx: SysVerilogHDLParser.Hierarchical_variable_descriptionContext
    ) -> List[str]:
        return self.visitHierarchical_variable_identifier(
            ctx.hierarchical_variable_identifier()
        )

    def visitHierarchical_variable_identifier(
        self, ctx: SysVerilogHDLParser.Hierarchical_variable_identifierContext
    ) -> List[str]:
        return self.visitHierarchical_identifier(ctx.hierarchical_identifier())

    def visitHierarchical_identifier(
        self, ctx: SysVerilogHDLParser.Hierarchical_identifierContext
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
        self,
        ctx: SysVerilogHDLParser.Dot_hierarchical_identifier_branch_item_starContext,
    ) -> List[str]:
        out = []
        for h in ctx.dot_hierarchical_identifier_branch_item():
            out.append(self.visitDot_hierarchical_identifier_branch_item(h))
        return out

    def visitDot_hierarchical_identifier_branch_item(
        self,
        ctx: SysVerilogHDLParser.Dot_hierarchical_identifier_branch_itemContext,
    ) -> str:
        return self.visitHierarchical_identifier_branch_item(
            ctx.hierarchical_identifier_branch_item()
        )

    def visitHierarchical_identifier_branch_item(
        self,
        ctx: SysVerilogHDLParser.Hierarchical_identifier_branch_itemContext,
    ):
        return self.visitIdentifier(ctx.identifier())

    def visitList_of_variable_descriptions(
        self, ctx: SysVerilogHDLParser.List_of_variable_descriptionsContext
    ) -> List[str]:
        vds = [self.visitVariable_description(ctx.variable_description())]
        vds.extend(
            self.visitComma_variable_description_star(
                ctx.comma_variable_description_star()
            )
        )
        return vds

    def visitComma_variable_description_star(
        self, ctx: SysVerilogHDLParser.Comma_variable_description_starContext
    ) -> List[str]:
        vds = []
        for v in ctx.comma_variable_description():
            vds.append(self.visitComma_variable_description(v))
        return vds

    def visitComma_variable_description(
        self, ctx: SysVerilogHDLParser.Comma_variable_descriptionContext
    ) -> str:
        return self.visitVariable_description(ctx.variable_description())

    def visitVariable_description(
        self, ctx: SysVerilogHDLParser.Variable_descriptionContext
    ) -> str:
        return self.visitVariable_identifier(ctx.variable_identifier())

    def visitVariable_identifier(
        self, ctx: SysVerilogHDLParser.Variable_identifierContext
    ) -> str:
        return self.visitIdentifier(ctx.identifier())

    def visitModule_identifier(
        self, ctx: SysVerilogHDLParser.Module_identifierContext
    ) -> str:
        return self.visitIdentifier(ctx.identifier())

    def visitIdentifier(
        self, ctx: SysVerilogHDLParser.IdentifierContext
    ) -> str:
        if ctx.Simple_identifier():
            return ctx.Simple_identifier().getText()
        else:
            return ctx.Escaped_identifier().getText()
