from dovado_rtl.antlr.hdl_representation import (
    Entity,
    ParameterTypeEnum,
    PortDirectionEnum,
    PortTypeEnum,
    TopLevel,
    Port,
    Parameter,
    PortDirection,
    PortType,
    ParameterType,
)
from dovado_rtl.antlr.generated.vhdl.vhdlParserVisitor import vhdlParserVisitor
from dovado_rtl.antlr.generated.vhdl.vhdlParser import vhdlParser
from typing import List, Iterator, Optional, Union, Tuple
from itertools import repeat


class VhdlEntityVisitor(vhdlParserVisitor):
    def __init__(self):
        self.top_level: TopLevel = TopLevel([], [])
        self.entities: List[Entity] = []

    def visitDesign_file(self, ctx: vhdlParser.Design_fileContext):
        for d in ctx.design_unit():
            self.visitDesign_unit(d)

    def visitDesign_unit(self, ctx: vhdlParser.Design_unitContext):
        self.visitContext_clause(ctx.context_clause())
        self.visitLibrary_unit(ctx.library_unit())

    def visitContext_clause(self, ctx: vhdlParser.Context_clauseContext):
        for i in ctx.context_item():
            self.visitContext_item(i)

    def visitContext_item(self, ctx: vhdlParser.Context_itemContext):
        if ctx.library_clause():
            self.visitLibrary_clause(ctx.library_clause())
        if ctx.use_clause():
            self.visitUse_clause(ctx.use_clause())
        if ctx.context_reference():
            pass

    def visitLibrary_clause(self, ctx: vhdlParser.Library_clauseContext):
        for ln in self.visitLogical_name_list(ctx.logical_name_list()):
            self.top_level.add_library(ln)

    def visitUse_clause(self, ctx: vhdlParser.Use_clauseContext):
        for n in ctx.selected_name():
            self.top_level.add_used(self.visitSelected_name(n))

    def visitLogical_name_list(
        self, ctx: vhdlParser.Logical_name_listContext
    ) -> Iterator[str]:
        return self.visitIdentifier_list(ctx.identifier_list())

    def visitIdentifier_list(
        self, ctx: vhdlParser.Identifier_listContext
    ) -> Iterator[str]:
        for i in ctx.identifier():
            yield self.visitIdentifier(i)

    def visitSelected_name(self, ctx: vhdlParser.Selected_nameContext) -> str:
        out = self.visitIdentifier(ctx.identifier())
        for s in ctx.suffix():
            suff = self.visitSuffix(s)
            if suff:
                out += "." + suff
        return out

    def visitSuffix(self, ctx: vhdlParser.SuffixContext) -> Optional[str]:
        if ctx.name_literal():
            return self.visitName_literal(ctx.name_literal())
        if ctx.KW_ALL():
            return ctx.KW_ALL().getText()

    def visitIdentifier(self, ctx: vhdlParser.IdentifierContext):
        return (
            ctx.BASIC_IDENTIFIER().getText()
            if ctx.BASIC_IDENTIFIER()
            else ctx.EXTENDED_IDENTIFIER()
        )

    def visitLibrary_unit(self, ctx: vhdlParser.Library_unitContext):
        if ctx.primary_unit():
            self.visitPrimary_unit(ctx.primary_unit())
        if ctx.secondary_unit():
            # architecture body and package body ignored
            pass

    def visitPrimary_unit(self, ctx: vhdlParser.Primary_unitContext):
        if ctx.entity_declaration():
            self.visitEntity_declaration(ctx.entity_declaration())
        else:
            pass

    def visitEntity_declaration(
        self, ctx: vhdlParser.Entity_declarationContext
    ):
        self.entities.append(Entity(self.visitIdentifier(ctx.identifier()[0])))
        if ctx.generic_clause():
            self.visitGeneric_clause(ctx.generic_clause())
        if ctx.port_clause():
            self.visitPort_clause(ctx.port_clause())

    def visitGeneric_clause(self, ctx: vhdlParser.Generic_clauseContext):
        self.visitGeneric_list(ctx.generic_list())

    def visitPort_clause(self, ctx: vhdlParser.Port_clauseContext):
        self.visitPort_list(ctx.port_list())

    def visitGeneric_list(self, ctx: vhdlParser.Generic_listContext):
        for i in self.visitInterface_list(ctx.interface_list()):
            p_type = i[1]
            if isinstance(p_type, ParameterType):
                self.entities[-1].add_parameter(Parameter(i[0], p_type))

    def visitPort_list(self, ctx: vhdlParser.Port_listContext):
        for i in self.visitInterface_list(ctx.interface_list()):
            p_dir = i[1]
            p_type = i[2]
            if (
                len(i) == 3
                and isinstance(p_dir, PortDirection)
                and isinstance(p_type, PortType)
            ):
                self.entities[-1].add_port(Port(i[0], p_dir, p_type))
            else:
                pass

    def visitInterface_list(
        self, ctx: vhdlParser.Interface_listContext
    ) -> Union[
        List[Tuple[str, ParameterType]],
        List[Tuple[str, PortDirection, PortType]],
    ]:
        out = []
        for i in ctx.interface_element():
            for e in self.visitInterface_element(i):
                out.append(e)
        return out

    def visitInterface_element(
        self, ctx: vhdlParser.Interface_elementContext
    ) -> Union[
        Union[
            Iterator[Tuple[str, ParameterType]],
            Union[
                List[Tuple[str, ParameterType]],
                List[Tuple[str, PortDirection, PortType]],
            ],
        ],
        None,
    ]:
        return self.visitInterface_declaration(ctx.interface_declaration())

    def visitInterface_declaration(
        self, ctx: vhdlParser.Interface_declarationContext
    ) -> Union[
        Union[
            Iterator[Tuple[str, ParameterType]],
            Union[
                List[Tuple[str, ParameterType]],
                List[Tuple[str, PortDirection, PortType]],
            ],
        ],
        None,
    ]:
        if ctx.interface_object_declaration():
            return self.visitInterface_object_declaration(
                ctx.interface_object_declaration()
            )
        else:
            return []

    def visitInterface_object_declaration(
        self, ctx: vhdlParser.Interface_object_declarationContext
    ) -> Union[
        Union[
            Iterator[Tuple[str, ParameterType]],
            Union[
                List[Tuple[str, ParameterType]],
                List[Tuple[str, PortDirection, PortType]],
            ],
        ],
        None,
    ]:
        if ctx.interface_constant_declaration():
            return self.visitInterface_constant_declaration(
                ctx.interface_constant_declaration()
            )
        if ctx.interface_signal_declaration():
            return self.visitInterface_signal_declaration(
                ctx.interface_signal_declaration()
            )

    def visitInterface_constant_declaration(
        self, ctx: vhdlParser.Interface_constant_declarationContext
    ) -> Iterator[Tuple[str, ParameterType]]:
        for i, t in zip(
            self.visitIdentifier_list(ctx.identifier_list()),
            repeat(self.visitSubtype_indication(ctx.subtype_indication())),
        ):
            if isinstance(t, ParameterType):
                yield i, t
            else:
                pass

    def visitInterface_signal_declaration(
        self, ctx: vhdlParser.Interface_signal_declarationContext
    ) -> Union[
        List[Tuple[str, ParameterType]],
        List[Tuple[str, PortDirection, PortType]],
    ]:
        out = []
        if not ctx.signal_mode():
            for i, t in zip(
                self.visitIdentifier_list(ctx.identifier_list()),
                repeat(self.visitSubtype_indication(ctx.subtype_indication())),
            ):
                if isinstance(t, ParameterType):
                    out.append((i, t))
                else:
                    pass
            return out
        else:
            for i, s, t in zip(
                self.visitIdentifier_list(ctx.identifier_list()),
                repeat(self.visitSignal_mode(ctx.signal_mode())),
                repeat(self.visitSubtype_indication(ctx.subtype_indication())),
            ):
                if isinstance(t, PortType):
                    out.append((i, s, t))
                else:
                    pass
            return out

    def visitSignal_mode(
        self, ctx: vhdlParser.Signal_modeContext
    ) -> PortDirection:
        return (
            PortDirection(PortDirectionEnum.INPUT, "input")
            if ctx.KW_IN()
            else PortDirection(PortDirectionEnum.OUTPUT, "output")
            if ctx.KW_OUT()
            else PortDirection(PortDirectionEnum.OTHER, "buffer")
            if ctx.KW_BUFFER()
            else PortDirection(PortDirectionEnum.OTHER, "inout")
            if ctx.KW_INOUT()
            else PortDirection(PortDirectionEnum.OTHER, "linkage")
        )

    def visitSubtype_indication(
        self, ctx: vhdlParser.Subtype_indicationContext
    ) -> Union[PortType, ParameterType, None]:
        type = self.visitType_mark(ctx.type_mark())
        if type == "std_logic":
            return PortType(PortTypeEnum.SCALAR, "std_logic")
        if type == "std_ulogic":
            return PortType(PortTypeEnum.SCALAR, "std_ulogic")
        if type == "std_ulogic_vector":
            return PortType(PortTypeEnum.VECTOR, "std_ulogic_vector")
        elif type == "std_logic_vector":
            return PortType(PortTypeEnum.VECTOR, "std_logic_vector")
        elif type == "integer":
            return ParameterType(ParameterTypeEnum.INTEGER, "integer")
        elif type == "natural":
            return ParameterType(ParameterTypeEnum.INTEGER, "natural")
        elif type == "positive":
            return ParameterType(ParameterTypeEnum.INTEGER, "positive")
        elif type == "signed":
            return ParameterType(ParameterTypeEnum.INTEGER, "signed")
        elif type == "unsigned":
            return ParameterType(ParameterTypeEnum.INTEGER, "unsigned")
        elif type == "boolean":
            return ParameterType(ParameterTypeEnum.BOOL, "boolean")
        else:
            pass

    def visitType_mark(
        self, ctx: vhdlParser.Type_markContext
    ) -> Optional[str]:
        return self.visitName(ctx.name())

    def visitName(self, ctx: vhdlParser.NameContext) -> Optional[str]:
        if ctx.name_literal():
            return self.visitName_literal(ctx.name_literal())
        if ctx.external_name():
            return self.visitExternal_name(ctx.external_name())
        else:
            return self.visitName(ctx.name())
            # skipping range in e.g. std_logic_vector

    def visitName_literal(
        self, ctx: vhdlParser.Name_literalContext
    ) -> Optional[str]:
        if ctx.identifier():
            return self.visitIdentifier(ctx.identifier())
        if ctx.operator_symbol():
            return self.visitOperator_symbol(ctx.operator_symbol())
        if ctx.CHARACTER_LITERAL():
            return ctx.CHARACTER_LITERAL().getText()

    def visitOperator_symbol(
        self, ctx: vhdlParser.Operator_symbolContext
    ) -> str:
        return ctx.STRING_LITERAL().getText()

    def visitExternal_name(self, ctx: vhdlParser.External_nameContext) -> str:
        return (
            ctx.SHIFT_LEFT().getText() + ctx.KW_VARIABLE().getText()
            if ctx.KW_VARIABLE()
            else ctx.KW_CONSTANT().getText()
            if ctx.KW_CONSTANT
            else ctx.KW_SIGNAL().getText()
            + self.visitExternal_pathname(ctx.external_pathname())
            + ctx.COLON().getText()
            + self.visitSubtype_indication(ctx.subtype_indication())
            + ctx.SHIFT_RIGHT().getText()
        )

    def visitExternal_pathname(
        self, ctx: vhdlParser.External_pathnameContext
    ) -> Optional[str]:
        if ctx.package_pathname():
            return self.visitPackage_pathname(ctx.package_pathname())
        if ctx.absolute_pathname():
            return self.visitAbsolute_pathname(ctx.absolute_pathname())
        if ctx.relative_pathname():
            return self.visitRelative_pathname(ctx.relative_pathname())

    def visitPackage_pathname(
        self, ctx: vhdlParser.Package_pathnameContext
    ) -> str:
        out = ctx.AT().getText()
        for i in ctx.identifier()[:-1]:
            out += self.visitIdentifier(i) + "."
        return out + self.visitIdentifier(ctx.identifier()[-1])

    def visitAbsolute_pathname(
        self, ctx: vhdlParser.Absolute_pathnameContext
    ) -> str:
        return "." + self.visitPartial_pathname(ctx.partial_pathname())

    def visitRelative_pathname(
        self, ctx: vhdlParser.Relative_pathnameContext
    ) -> str:
        return (
            (ctx.UP().getText() + ".")
            if ctx.UP()
            else "" + self.visitPartial_pathname(ctx.partial_pathname())
        )

    def visitPartial_pathname(
        self, ctx: vhdlParser.Partial_pathnameContext
    ) -> str:
        out = ""
        for p in ctx.pathname_element():
            out += self.visitPathname_element(p) + "."
        return out + self.visitIdentifier(ctx.identifier())

    def visitPathname_element(
        self, ctx: vhdlParser.Pathname_elementContext
    ) -> str:
        if ctx.expression():
            print("Expression in pathname are not supported, skipping")
        return self.visitLabel(ctx.label())

    def visitLabel(self, ctx: vhdlParser.LabelContext) -> str:
        return self.visitIdentifier(ctx.identifier())
