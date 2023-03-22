from typing import Optional, Sequence, Union

from antlr4 import IllegalStateException
from dovado_rtl.parsers.vhdl.vhdl_parameter import VhdlParameter
from dovado_rtl.parsers.utilities import Port, HdlAntlrModule
from dovado_rtl.parsers.vhdl.generated.vhdlVisitor import vhdlVisitor
from dovado_rtl.parsers.vhdl.generated.vhdlParser import vhdlParser
from dovado_rtl.parsers.utilities.port import PORT_DIMENSION, PORT_DIRECTION


class VhdlVisitor(vhdlVisitor):
    def visitDesign_file(
        self, ctx: vhdlParser.Design_fileContext
    ) -> Sequence[HdlAntlrModule]:
        modules: list[HdlAntlrModule]

        design_units = ctx.design_unit()

        modules = []
        if design_units:
            for design_unit in design_units:
                module = self.visitDesign_unit(design_unit)
                if module is not None:
                    modules.append(module)

        return modules

    def visitDesign_unit(
        self, ctx: vhdlParser.Design_unitContext
    ) -> Optional[HdlAntlrModule]:
        # context clause is ignored
        library_unit = ctx.library_unit()

        if library_unit:
            return self.visitLibrary_unit(library_unit)
        return None

    def visitLibrary_unit(
        self, ctx: vhdlParser.Library_unitContext
    ) -> Optional[HdlAntlrModule]:
        primary_unit = ctx.primary_unit()

        if primary_unit:
            return self.visitPrimary_unit(primary_unit)
        return None

    def visitPrimary_unit(
        self, ctx: vhdlParser.Primary_unitContext
    ) -> Optional[HdlAntlrModule]:
        # packages and configurations are ignored
        entity_declaration = ctx.entity_declaration()

        if entity_declaration:
            return self.visitEntity_declaration(entity_declaration)
        return None

    def visitEntity_declaration(self, ctx: vhdlParser.Entity_declarationContext):
        parsed_identifier: str
        parameters: list[VhdlParameter]
        ports: list[Port]

        identifiers = ctx.identifier()
        entity_header = ctx.entity_header()

        if identifiers:
            # skipping the second name declaration
            parsed_identifier = identifiers[0].getText()
            if entity_header:
                parameters, ports = self.visitEntity_header(entity_header)
                return HdlAntlrModule(
                    name=parsed_identifier, parameters=parameters, ports=ports
                )
            else:
                raise IllegalStateException("Entity must have a header section")

        else:
            raise IllegalStateException("Identifier is mandatory for an entity")

    def visitEntity_header(
        self, ctx: vhdlParser.Entity_headerContext
    ) -> tuple[list[VhdlParameter], list[Port]]:
        ports: list[Port]
        parameters: list[VhdlParameter]

        generic_clause = ctx.generic_clause()
        port_clause = ctx.port_clause()

        ports = []
        parameters = []
        if generic_clause:
            parameters = self.visitGeneric_clause(generic_clause)
        if port_clause:
            ports = self.visitPort_clause(port_clause)
        return parameters, ports

    def visitGeneric_clause(
        self, ctx: vhdlParser.Generic_clauseContext
    ) -> list[VhdlParameter]:
        generic_list = ctx.generic_list()

        if generic_list:
            return self.visitGeneric_list(generic_list)
        return []

    def visitPort_clause(self, ctx: vhdlParser.Port_clauseContext) -> list[Port]:
        port_list = ctx.port_list()
        if port_list:
            return self.visitPort_list(port_list)
        return []

    def visitPort_list(self, ctx: vhdlParser.Port_listContext) -> list[Port]:
        interface_port_list = ctx.interface_port_list()

        if interface_port_list:
            return self.visitInterface_port_list(interface_port_list)
        return []

    def visitInterface_port_list(
        self, ctx: vhdlParser.Interface_port_listContext
    ) -> list[Port]:
        ports: list[Port]

        interface_port_declarations = ctx.interface_port_declaration()

        ports = []
        if interface_port_declarations:
            for interface_port_declaration in interface_port_declarations:
                ports += self.visitInterface_port_declaration(
                    interface_port_declaration
                )
        return ports

    def visitInterface_port_declaration(
        self, ctx: vhdlParser.Interface_port_declarationContext
    ) -> list[Port]:
        identifiers: list[str]
        port_direction: PORT_DIRECTION
        port_dimension: PORT_DIMENSION

        identifier_list = ctx.identifier_list()
        signal_mode = ctx.signal_mode()
        subtype_indication = ctx.subtype_indication()
        expression = ctx.expression()

        if identifier_list:
            identifiers = self.visitIdentifier_list(identifier_list)
            if signal_mode:
                port_direction = self.visitSignal_mode(signal_mode)
            else:
                # if no direction is specified
                # the standard assumes input
                port_direction = "input"

            if subtype_indication:
                _, port_dimension = self.visitSubtype_indication(subtype_indication)
            else:
                raise IllegalStateException("Type is mandatory in port declaration")

            return [
                Port(
                    name=identifier,
                    direction=port_direction,
                    dimension=port_dimension,
                    has_default=expression is not None,
                )
                for identifier in identifiers
            ]
        return []

    @staticmethod
    def is_subtype_scalar_boolean(selected_names: list[str]) -> bool:
        if len(selected_names) > 1:
            return False
        return selected_names[0] == "boolean"

    def visitSubtype_indication(
        self, ctx: vhdlParser.Subtype_indicationContext
    ) -> tuple[bool, PORT_DIMENSION]:
        parsed_selected_names: list[str]

        selected_names = ctx.selected_name()
        if selected_names:
            parsed_selected_names = [
                self.visitSelected_name(selected_name)
                for selected_name in selected_names
            ]
        else:
            raise IllegalStateException(
                "A subtype indication must contain at least one type"
            )

        if ctx.constraint():
            return False, "vectorial"
        else:
            return self.is_subtype_scalar_boolean(parsed_selected_names), "scalar"

    def visitSelected_name(self, ctx: vhdlParser.Selected_nameContext) -> str:
        identifier = ctx.identifier()
        if identifier:
            return self.visitIdentifier(identifier)
        raise IllegalStateException("A selected name must contain an identifier")

    def visitIdentifier(self, ctx: vhdlParser.IdentifierContext) -> str:
        basic_identifier = ctx.BASIC_IDENTIFIER()
        extended_identifier = ctx.EXTENDED_IDENTIFIER()
        if basic_identifier:
            return str(basic_identifier)
        if extended_identifier:
            return str(extended_identifier)
        raise IllegalStateException(
            "An identifier must contain either a base identifier or an extended identifier"
        )

    def visitSignal_mode(self, ctx: vhdlParser.Signal_modeContext) -> PORT_DIRECTION:
        if ctx.IN():
            return "input"
        if ctx.OUT():
            return "output"
        if ctx.INOUT():
            return "inout"
        if ctx.BUFFER():
            return "input"
        if ctx.LINKAGE():
            return "input"
        raise IllegalStateException("Found illegal signal mode")

    def visitGeneric_list(self, ctx: vhdlParser.Generic_listContext):
        parameters: list[VhdlParameter]
        interface_constant_declarations = ctx.interface_constant_declaration()

        parameters = []
        if interface_constant_declarations:
            for interface_constant_declaration in interface_constant_declarations:
                parameters += self.visitInterface_constant_declaration(
                    interface_constant_declaration
                )

        return parameters

    def visitInterface_constant_declaration(
        self, ctx: vhdlParser.Interface_constant_declarationContext
    ) -> list[VhdlParameter]:
        identifiers: list[str]
        value: str
        rule: Union[vhdlParser.ExpressionContext, vhdlParser.Identifier_listContext]

        identifier_list = ctx.identifier_list()
        expression = ctx.expression()
        subtype_indication = ctx.subtype_indication()

        if not subtype_indication:
            raise IllegalStateException("Generics must be strictly typed")

        if identifier_list:
            identifiers = self.visitIdentifier_list(identifier_list)

            value = ""
            if expression:
                value = expression.getText()
                rule = expression
            else:
                rule = subtype_indication

            return [
                VhdlParameter(
                    name=identifier,
                    value=value,
                    rule=rule,
                    has_default=True if value != "" else False,
                    is_boolean=self.visitSubtype_indication(subtype_indication)[0],
                )
                for identifier in identifiers
            ]
        return []

    def visitIdentifier_list(self, ctx: vhdlParser.Identifier_listContext) -> list[str]:
        identifiers = ctx.identifier()

        if identifiers:
            return [identifier.getText() for identifier in identifiers]

        return []
