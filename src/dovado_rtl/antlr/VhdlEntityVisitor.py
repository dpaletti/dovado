from dovado_rtl.antlr.HdlRepresentation import (
    Entity,
    TopLevel,
    Port,
    Parameter,
)
from dovado_rtl.antlr.generated.vhdl.vhdlVisitor import vhdlVisitor
from dovado_rtl.antlr.generated.vhdl.vhdlParser import vhdlParser
from typing import List


class VhdlEntityVisitor(vhdlVisitor):
    def __init__(self):
        self.top_level: TopLevel = TopLevel([], [])
        self.entities: List[Entity] = []

    def visitDesign_file(self, ctx: vhdlParser.Design_fileContext) -> None:
        for d in ctx.design_unit():
            self.visitDesign_unit(d)

    def visitDesign_unit(self, ctx: vhdlParser.Design_unitContext) -> None:
        self.visitContext_clause(ctx.context_clause())
        self.visitLibrary_unit(ctx.library_unit())

    def visitContext_clause(
        self, ctx: vhdlParser.Context_clauseContext
    ) -> None:
        for c in ctx.context_item():
            self.visitContext_item(c)

    def visitLibrary_unit(self, ctx: vhdlParser.Library_unitContext) -> None:
        if ctx.secondary_unit():
            self.visitSecondary_unit(ctx.secondary_unit())
        if ctx.primary_unit():
            self.visitPrimary_unit(ctx.primary_unit())

    def visitContext_item(self, ctx: vhdlParser.Context_itemContext) -> None:
        if ctx.library_clause():
            self.visitLibrary_clause(ctx.library_clause())
        if ctx.use_clause():
            self.visitUse_clause(ctx.use_clause())

    def visitSecondary_unit(
        self, ctx: vhdlParser.Secondary_unitContext
    ) -> None:
        if ctx.architecture_body():
            pass
        if ctx.package_body():
            pass

    def visitPrimary_unit(self, ctx: vhdlParser.Primary_unitContext) -> None:
        if ctx.entity_declaration():
            self.visitEntity_declaration(ctx.entity_declaration())
        if ctx.configuration_declaration():
            pass
        if ctx.package_declaration():
            pass

    def visitLibrary_clause(
        self, ctx: vhdlParser.Library_clauseContext
    ) -> None:
        self.visitLogical_name_list(ctx.logical_name_list())

    def visitUse_clause(self, ctx: vhdlParser.Use_clauseContext) -> None:
        for s in ctx.selected_name():
            self.top_level.add_used(self.visitSelected_name(s))

    def visitLogical_name(self, ctx: vhdlParser.Logical_nameContext) -> None:
        self.top_level.add_library(self.visitIdentifier(ctx.identifier()))

    def visitEntity_declaration(
        self, ctx: vhdlParser.Entity_declarationContext
    ) -> None:
        self.entities.append(Entity(self.visitIdentifier(ctx.identifier()[0])))
        self.visitEntity_header(ctx.entity_header())

    def visitEntity_header(self, ctx: vhdlParser.Entity_headerContext) -> None:
        if ctx.generic_clause():
            self.visitGeneric_clause(ctx.generic_clause())
        if ctx.port_clause():
            self.visitPort_clause(ctx.port_clause())

    def visitGeneric_clause(
        self, ctx: vhdlParser.Generic_clauseContext
    ) -> None:
        self.visitGeneric_list(ctx.generic_list())

    def visitPort_clause(self, ctx: vhdlParser.Port_clauseContext) -> None:
        self.visitPort_list(ctx.port_list())

    def visitGeneric_list(self, ctx: vhdlParser.Generic_listContext) -> None:
        for declaration in ctx.interface_constant_declaration():
            self.visitInterface_constant_declaration(declaration)

    def visitPort_list(self, ctx: vhdlParser.Port_listContext) -> None:
        self.visitInterface_port_list(ctx.interface_port_list())

    def visitInterface_constant_declaration(
        self, ctx: vhdlParser.Interface_constant_declarationContext
    ) -> None:
        id_list = self.visit(ctx.identifier_list())
        generic_type = self.visit(ctx.subtype_indication())
        for generic_id in id_list:
            self.entities[-1].add_parameter(
                Parameter(generic_id, generic_type)
            )

    def visitInterface_port_list(
        self, ctx: vhdlParser.Interface_port_listContext
    ) -> None:
        for d in ctx.interface_port_declaration():
            self.visitInterface_port_declaration(d)

    def visitInterface_port_declaration(
        self, ctx: vhdlParser.Interface_port_declarationContext
    ) -> None:
        id_list = self.visitIdentifier_list(ctx.identifier_list())
        if ctx.signal_mode():
            direction = self.visitSignal_mode(ctx.signal_mode())
            port_type = self.visitSubtype_indication(ctx.subtype_indication())

            for port_id in id_list:
                self.entities[-1].add_port(Port(port_id, direction, port_type))
        else:
            raise Exception(
                "Parsing ports "
                + str(id_list)
                + " without direction, please specify it "
                + "(signal mode) in interface_port_declaration"
            )

    def visitSignal_mode(self, ctx: vhdlParser.Signal_modeContext) -> str:
        if ctx.IN():
            return "in"
        if ctx.OUT():
            return "out"
        if ctx.INOUT():
            return "inout"
        if ctx.BUFFER():
            return "buffer"
        if ctx.LINKAGE():
            return "linkage"

    def visitIdentifier_list(
        self, ctx: vhdlParser.Identifier_listContext
    ) -> List[str]:
        identifiers = []
        for i in ctx.identifier():
            identifiers.append(self.visitIdentifier(i))
        return identifiers

    def visitIdentifier(self, ctx: vhdlParser.IdentifierContext) -> str:
        if ctx.BASIC_IDENTIFIER():
            return ctx.BASIC_IDENTIFIER().getText()
        return ctx.EXTENDED_IDENTIFIER().getText()

    def visitSubtype_indication(
        self, ctx: vhdlParser.Subtype_indicationContext
    ) -> str:
        subtype = "".join(
            [
                self.visitSelected_name(sel_name)
                for sel_name in ctx.selected_name()
            ]
        )

        if ctx.constraint():
            # vector range is ignored
            pass
        if ctx.tolerance_aspect():
            # tolerance is ignored
            pass
        return subtype

    def visitSelected_name(self, ctx: vhdlParser.Selected_nameContext) -> str:
        return self.visitIdentifier(ctx.identifier())

    def visitName_part(self, ctx: vhdlParser.Name_partContext) -> str:
        if ctx.selected_name_part():
            return self.visitSelected_name_part(ctx.selected_name_part())
        if ctx.function_call_or_indexed_name_part():
            return self.visitFunction_call_or_indexed_name_part(
                ctx.function_call_or_indexed_name_part()
            )
        if ctx.slice_name_part():
            return self.visitSlice_name_part(ctx.slice_name_part())
        if ctx.attribute_name_part():
            return self.visitAttribute_name_part(ctx.attribute_name_part())

    def visitDirection(self, ctx: vhdlParser.DirectionContext) -> str:
        if ctx.TO():
            return ctx.TO().getText()
        if ctx.DOWNTO():
            return ctx.DOWNTO().getText()

    def visitSelected_name_part(
        self, ctx: vhdlParser.Selected_name_partContext
    ) -> str:
        name = ""
        if ctx.DOT():
            for d, s in zip(ctx.DOT(), ctx.suffix()):
                name += d.getText() + self.visitSuffix(s)
        return name

    def visitFunction_call_or_indexed_name_part(
        self, ctx: vhdlParser.Function_call_or_indexed_name_partContext
    ) -> str:
        return (
            ctx.LPAREN().getText()
            + self.visitActual_parameter_part(ctx.actual_parameter_part())
            + ctx.RPAREN().getText()
        )

    def visitActual_parameter_part(
        self, ctx: vhdlParser.Actual_parameter_partContext
    ) -> str:
        return self.visitAssociation_list(ctx.association_list())

    def visitAssociation_list(
        self, ctx: vhdlParser.Association_listContext
    ) -> str:
        association_list = self.visitAssociation_element(
            ctx.association_element()[0]
        )
        for c, a in zip(ctx.COMMA, ctx.association_element()[1:]):
            association_list += c.getText() + self.visitAssociation_element(a)
        return association_list

    def visitAssociation_element(
        self, ctx: vhdlParser.Association_elementContext
    ) -> str:
        association_element = ""
        if ctx.formal_part():
            association_element += (
                self.visitFormal_part(ctx.formal_part())
                + ctx.ARROW().getText()
            )
        association_element += self.visitActual_part(ctx.actual_part())
        return association_element

    def visitFormal_part(self, ctx: vhdlParser.Formal_partContext) -> str:
        formal_part = ""
        formal_part += self.visitIdentifier(ctx.identifier()[0])
        if ctx.LPAREN():
            formal_part += (
                ctx.LPAREN().getText()
                + self.visitExplicit_range(ctx.explicit_range())
                + ctx.RPAREN()
            )
        return formal_part

    def visitActual_part(self, ctx: vhdlParser.Actual_partContext) -> str:
        if ctx.name():
            return (
                self.visitName(ctx.name())
                + ctx.LPAREN().getText()
                + self.visitActual_designator(ctx.actual_designator())
                + ctx.RPAREN().getText()
            )
        return self.visitActual_designator(ctx.actual_designator())

    def visitActual_designator(
        self, ctx: vhdlParser.Actual_designatorContext
    ) -> str:
        return self.visitExpression(ctx.expression()) + ctx.OPEN().getText()

    def visitSlice_name_part(
        self, ctx: vhdlParser.Slice_name_partContext
    ) -> str:
        return (
            ctx.LPAREN().getText()
            + self.visitDiscrete_range(ctx.discrete_range())
            + ctx.RPAREN().getText()
        )

    def visitAttribute_name_part(
        self, ctx: vhdlParser.Attribute_name_partContext
    ) -> str:
        name = ""
        if ctx.signature():
            name += self.visitSignature(ctx.signature())
        name += ctx.APOSTROPHE().getText() + self.visitAttribute_designator(
            ctx.attribute_designator()
        )
        if ctx.expression():
            name += (
                ctx.LPAREN().getText()
                + self.visitExpression(ctx.expression())
                + ctx.RPAREN().getText()
            )
        return name