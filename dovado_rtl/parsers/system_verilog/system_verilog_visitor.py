from typing import Any, Optional, Sequence, Union, cast
from antlr4 import IllegalStateException
from dovado_rtl.parsers.system_verilog.generated.SystemVerilogParserVisitor import (
    SystemVerilogParserVisitor,
)
from dovado_rtl.parsers.system_verilog.generated.SystemVerilogParser import (
    SystemVerilogParser,
)
from dovado_rtl.parsers.utilities import (
    AntlrParameter,
    HdlAntlrModule,
    PORT_DIRECTION,
    PORT_DIMENSION,
    Port,
)


class SystemVerilogVisitor(SystemVerilogParserVisitor):
    def visitSource_text(
        self, ctx: SystemVerilogParser.Source_textContext
    ) -> Sequence[HdlAntlrModule]:
        modules: list[HdlAntlrModule]

        descriptions = ctx.description()

        modules = []
        if descriptions:
            for description in descriptions:
                modules.append(self.visitDescription(description))
        return modules

    def visitDescription(
        self, ctx: SystemVerilogParser.DescriptionContext
    ) -> HdlAntlrModule:
        # configurations, bind directives, attributes and udp are ignored
        module_declaration = ctx.module_declaration()
        interface_declaration = ctx.interface_declaration()
        package_declaration = ctx.package_declaration()
        package_item = ctx.package_item()

        if module_declaration:
            return self.visitModule_declaration(module_declaration)
        elif interface_declaration:
            return self.visitInterface_declaration(interface_declaration)
        elif package_declaration:
            return self.visitPackage_declaration(package_declaration)
        elif package_item:
            return HdlAntlrModule(
                name="", parameters=self.visitPackage_item(package_item), ports=[]
            )
        else:
            raise IllegalStateException("Empty description found.")

    def visitPackage_declaration(
        self, ctx: SystemVerilogParser.Package_declarationContext
    ) -> HdlAntlrModule:
        parsed_identifier: str
        parameters: list[AntlrParameter]

        package_identifier = ctx.package_identifier()
        pkg_decl_items = ctx.pkg_decl_item()

        if package_identifier:
            parsed_identifier = package_identifier.getText()
        else:
            raise IllegalStateException("Package name is mandatory")
        parameters = []
        if pkg_decl_items:
            for pkg_decl_item in pkg_decl_items:
                parameters += self.visitPkg_decl_item(pkg_decl_item)
        return HdlAntlrModule(name=parsed_identifier, parameters=parameters, ports=[])

    def visitPkg_decl_item(
        self, ctx: SystemVerilogParser.Pkg_decl_itemContext
    ) -> list[AntlrParameter]:
        package_item = ctx.package_item()
        if package_item:
            return self.visitPackage_item(package_item)
        return []

    def visitPackage_item(
        self, ctx: SystemVerilogParser.Package_itemContext
    ) -> list[AntlrParameter]:
        package_item_declaration = ctx.package_item_declaration()
        if package_item_declaration:
            return self.visitPackage_item_declaration(package_item_declaration)
        return []

    def visitModule_declaration(
        self, ctx: SystemVerilogParser.Module_declarationContext
    ) -> HdlAntlrModule:
        # Module name after "endmodule" is ignored
        def parse_module_items(
            module_items: list[SystemVerilogParser.Module_itemContext],
        ) -> tuple[list[Port], list[AntlrParameter], list[HdlAntlrModule]]:
            ports = []
            parameters = []
            submodules = []
            for module_item in module_items:
                module_item = self.visitModule_item(module_item)
                if module_item:
                    if isinstance(module_item, list):
                        if isinstance(module_item[0], Port):
                            module_item = cast(list[Port], module_item)
                            ports += module_item
                        else:
                            module_item = cast(list[AntlrParameter], module_item)
                            parameters += module_item
                    else:
                        submodules.append(module_item)
                return ports, parameters, submodules
            return [], [], []

        parsed_module: HdlAntlrModule
        ports: list[Port]
        parameters: list[AntlrParameter]
        submodules: list[HdlAntlrModule]

        module_header = ctx.module_header()
        module_items = ctx.module_item()
        module_identifier = ctx.module_identifier()

        ports = []
        parameters = []
        submodules = []
        if module_header:
            parsed_module = self.visitModule_header(module_header)
            if module_items:
                ports, parameters, submodules = parse_module_items(module_items)
            return HdlAntlrModule(
                name=parsed_module.name,
                parameters=parsed_module.parameters + parameters,
                ports=parsed_module.ports + ports,
                submodules=submodules,
            )

        elif module_identifier:
            parsed_module_identifier = self.visitModule_identifier(module_identifier)
            if module_items:
                ports, parameters, submodules = parse_module_items(module_items)
            return HdlAntlrModule(
                name=parsed_module_identifier,
                parameters=parameters,
                ports=ports,
                submodules=submodules,
            )

        else:
            raise IllegalStateException(
                "Module header or module identifier are mandatory in module_declaration"
            )

    def visitModule_header(
        self, ctx: SystemVerilogParser.Module_headerContext
    ) -> HdlAntlrModule:
        parsed_module_identifier: str
        parameters: list[AntlrParameter]

        module_identifier = ctx.module_identifier()
        parameter_port_list = ctx.parameter_port_list()
        list_of_port_declarations = ctx.list_of_port_declarations()

        if module_identifier:
            parsed_module_identifier: str = self.visitModule_identifier(
                module_identifier
            )
        else:
            raise IllegalStateException(
                "Module identifier is mandatory in module header"
            )

        parameters = []
        if parameter_port_list:
            parameters = self.visitParameter_port_list(parameter_port_list)

        ports = []
        if list_of_port_declarations:
            ports = self.visitList_of_port_declarations(list_of_port_declarations)

        return HdlAntlrModule(
            name=parsed_module_identifier, parameters=parameters, ports=ports
        )

    def visitList_of_port_declarations(
        self, ctx: SystemVerilogParser.List_of_port_declarationsContext
    ) -> list[Port]:
        # we only parse port declarations
        ports: list[Port]

        port_decls = ctx.port_decl()

        if port_decls:
            ports = []
            for port_decl in port_decls:
                parsed_port_decl = self.visitPort_decl(port_decl)
                if parsed_port_decl:
                    ports.append(parsed_port_decl)
            return ports

        return []

    def visitPort_decl(
        self, ctx: SystemVerilogParser.Port_declContext
    ) -> Optional[Port]:
        # attributes are ignored
        ansi_port_declaration = ctx.ansi_port_declaration()

        if ansi_port_declaration:
            return self.visitAnsi_port_declaration(ansi_port_declaration)
        raise IllegalStateException(
            "A port decl requires a corresponding ansi port declaration"
        )

    def visitAnsi_port_declaration(
        self, ctx: SystemVerilogParser.Ansi_port_declarationContext
    ) -> Optional[Port]:
        # all ports without explicit direction are ignored
        parsed_port_direction: PORT_DIRECTION
        parsed_port_identifier: str
        port_dimension: PORT_DIMENSION

        port_direction = ctx.port_direction()
        port_identifier = ctx.port_identifier()
        implicit_data_type = ctx.implicit_data_type()
        data_type_or_implicit = ctx.data_type_or_implicit()
        data_type = ctx.data_type()
        constant_expression = ctx.constant_expression()

        if port_direction:
            parsed_port_direction = port_direction.getText()
            parsed_port_direction = (
                parsed_port_direction if parsed_port_direction != "ref" else "input"
            )
            if port_identifier:
                parsed_port_identifier = port_identifier.getText()
                port_dimension = "scalar"
                if implicit_data_type:
                    port_dimension = self.visitImplicit_data_type(implicit_data_type)
                elif data_type_or_implicit:
                    port_dimension = self.visitData_type_or_implicit(
                        data_type_or_implicit
                    )
                elif data_type:
                    port_dimension = self.visitData_type(data_type)

                return Port(
                    name=parsed_port_identifier,
                    direction=parsed_port_direction,
                    dimension=port_dimension,
                    has_default=constant_expression is not None,
                )
        return None

    def visitParameter_port_list(
        self, ctx: SystemVerilogParser.Parameter_port_listContext
    ) -> list[AntlrParameter]:
        parameters: list[AntlrParameter]

        list_of_param_assignments = ctx.list_of_param_assignments()
        parameter_port_declarations = ctx.parameter_port_declaration()

        parameters = []
        if list_of_param_assignments:
            parameters = self.visitList_of_param_assignments(list_of_param_assignments)
        if parameter_port_declarations:
            for parameter_port_declaration in parameter_port_declarations:
                parameters += self.visitParameter_port_declaration(
                    parameter_port_declaration
                )

        return parameters

    def visitParameter_port_declaration(
        self, ctx: SystemVerilogParser.Parameter_port_declarationContext
    ) -> list[AntlrParameter]:

        parameter_declaration = ctx.parameter_declaration()
        local_parameter_declaration = ctx.local_parameter_declaration()
        list_of_param_assignments = ctx.list_of_param_assignments()

        if parameter_declaration:
            return self.visitParameter_declaration(parameter_declaration)
        if local_parameter_declaration:
            return self.visitLocal_parameter_declaration(local_parameter_declaration)
        if list_of_param_assignments:
            return self.visitList_of_param_assignments(list_of_param_assignments)
        return []

    def visitModule_identifier(
        self, ctx: SystemVerilogParser.Module_identifierContext
    ) -> str:
        identifier = ctx.identifier()
        if identifier:
            return identifier.getText()

        raise IllegalStateException("Found none identifier in module identifier")

    def visitPackage_import_declaration(
        self, ctx: SystemVerilogParser.Package_import_declarationContext
    ) -> list[tuple[str, str]]:
        parsed_package_import_items: list[tuple[str, str]]

        package_import_items = ctx.package_import_item()
        if package_import_items:
            parsed_package_import_items = []
            for package_import_item in package_import_items:
                parsed_package_import_items.append(
                    self.visitPackage_import_item(package_import_item)
                )
            return parsed_package_import_items
        else:
            raise IllegalStateException(
                "An import declaration must have at least one item"
            )

    def visitPackage_import_item(
        self, ctx: SystemVerilogParser.Package_import_itemContext
    ) -> tuple[str, str]:
        parsed_identifier: str
        parsed_package_identifier: str

        package_identifier = ctx.package_identifier()
        identifier = ctx.identifier()

        if package_identifier:
            parsed_package_identifier = self.visitPackage_identifier(package_identifier)
        else:
            raise IllegalStateException(
                "A package import must have exactly one identifier"
            )

        if identifier:
            parsed_identifier = identifier.getText()
        else:
            parsed_identifier = "*"

        return parsed_package_identifier, parsed_identifier

    def visitPackage_identifier(
        self, ctx: SystemVerilogParser.Package_identifierContext
    ) -> str:
        identifier = ctx.identifier()
        if identifier:
            return identifier.getText()
        raise IllegalStateException(
            "A package identifier must contain exactly one identifier"
        )

    def visitModule_item(
        self, ctx: SystemVerilogParser.Module_itemContext
    ) -> Optional[Union[list[Port], list[AntlrParameter], HdlAntlrModule]]:
        # parameter override is not supported
        # neither with the "#-syntax" nor with the defparam syntax
        # program blocks are ignored
        # attributes are ignored
        # timeunits declarations are ignored

        port_declaration = ctx.port_declaration()
        module_common_item = ctx.module_common_item()
        specparam_declaration = ctx.specparam_declaration()
        specify_block = ctx.specify_block()
        module_declaration = ctx.module_declaration()
        interface_declaration = ctx.interface_declaration()

        if port_declaration:
            # list[Port]
            return self.visitPort_declaration(port_declaration)
        elif module_common_item:
            # list[AntlrParameter]
            return self.visitModule_common_item(module_common_item)
        elif specparam_declaration:
            # list[AntlrParameter]
            return self.visitSpecparam_declaration(specparam_declaration)
        elif specify_block:
            # list[AntlrParameter]
            return self.visitSpecify_block(specify_block)
        elif module_declaration:
            # HdlAntlrModule
            return self.visitModule_declaration(module_declaration)
        elif interface_declaration:
            # HdlAntlrModule
            return self.visitInterface_declaration(interface_declaration)
        return None

    def visitPort_declaration(
        self, ctx: SystemVerilogParser.Port_declarationContext
    ) -> list[Port]:
        # interface ports are ignored

        inout_declaration = ctx.inout_declaration()
        input_declaration = ctx.input_declaration()
        output_declaration = ctx.output_declaration()
        ref_declaration = ctx.ref_declaration()

        if inout_declaration:
            return self.visitInout_declaration(inout_declaration)

        if input_declaration:
            return self.visitInput_declaration(input_declaration)

        if output_declaration:
            return self.visitOutput_declaration(output_declaration)

        if ref_declaration:
            return self.visitRef_declaration(ref_declaration)
        return []

    def visitInterface_declaration(
        self, ctx: SystemVerilogParser.Interface_declarationContext
    ) -> HdlAntlrModule:
        def parse_interface_items(
            interface_items: list[SystemVerilogParser.Interface_itemContext],
        ) -> tuple[list[Port], list[AntlrParameter], list[HdlAntlrModule]]:
            ports = []
            parameters = []
            submodules = []
            for interface_item in interface_items:
                parsed_interface_item = self.visitInterface_item(interface_item)
                if parsed_interface_item:
                    if isinstance(parsed_interface_item, list):
                        if isinstance(parsed_interface_item[0], Port):
                            parsed_interface_item = cast(
                                list[Port], parsed_interface_item
                            )
                            ports += parsed_interface_item
                        else:
                            parsed_interface_item = cast(
                                list[AntlrParameter], parsed_interface_item
                            )
                            parameters += parsed_interface_item
                    else:
                        submodules.append(parsed_interface_item)
                return ports, parameters, submodules
            return [], [], []

        module: HdlAntlrModule
        parsed_interface_identifier: str
        module: HdlAntlrModule
        ports: list[Port]
        parameters: list[AntlrParameter]
        submodules: list[HdlAntlrModule]

        interface_header = ctx.interface_header()
        interface_identifier = ctx.interface_identifier()
        interface_items = ctx.interface_item()

        ports = []
        parameters = []
        submodules = []
        if interface_header:
            module: HdlAntlrModule = self.visitInterface_header(interface_header)
            if interface_items:
                ports, parameters, submodules = parse_interface_items(interface_items)
            return HdlAntlrModule(
                name=module.name,
                parameters=module.parameters + parameters,
                ports=module.ports + ports,
                submodules=submodules,
            )

        elif interface_identifier:
            parsed_interface_identifier = self.visitInterface_identifier(
                interface_identifier
            )
            if interface_items:
                ports, parameters, submodules = parse_interface_items(interface_items)
            return HdlAntlrModule(
                name=parsed_interface_identifier,
                ports=ports,
                parameters=parameters,
                submodules=submodules,
            )

        raise IllegalStateException("Empty interface declaration is forbidden")

    def visitInterface_item(
        self, ctx: SystemVerilogParser.Interface_itemContext
    ) -> Optional[Union[list[Port], list[AntlrParameter], HdlAntlrModule]]:

        port_declaration = ctx.port_declaration()
        module_common_item = ctx.module_common_item()
        interface_declaration = ctx.interface_declaration()

        if port_declaration:
            # list[Port]
            return self.visitPort_declaration(port_declaration)
        if module_common_item:
            # list[AntlrParameter]
            return self.visitModule_common_item(module_common_item)
        if interface_declaration:
            # HdlAntlrModule
            return self.visitInterface_declaration(interface_declaration)
        return None

    def visitInterface_header(
        self, ctx: SystemVerilogParser.Interface_headerContext
    ) -> HdlAntlrModule:
        interface_name: str
        parameters: list[AntlrParameter]
        ports: list[Port]
        interface_identifier = ctx.interface_identifier()
        parameter_port_list = ctx.parameter_port_list()
        list_of_port_declarations = ctx.list_of_port_declarations()

        if interface_identifier:
            interface_name = self.visitInterface_identifier(interface_identifier)

            parameters = []
            if parameter_port_list:
                parameters = self.visitParameter_port_list(parameter_port_list)

            ports = []
            if list_of_port_declarations:
                ports = self.visitList_of_port_declarations(list_of_port_declarations)

            return HdlAntlrModule(
                name=interface_name, parameters=parameters, ports=ports
            )
        raise IllegalStateException("An interface header must hold an identifier")

    def visitInterface_identifier(
        self, ctx: SystemVerilogParser.Interface_identifierContext
    ) -> str:
        identifier = ctx.identifier
        if identifier:
            return identifier.getText()

        raise IllegalStateException("Interface identifier must hold an identifier")

    def visitRef_declaration(
        self, ctx: SystemVerilogParser.Ref_declarationContext
    ) -> list[Port]:
        variable_identifiers: list[str]
        port_dimension: PORT_DIMENSION

        list_of_variable_identifiers = ctx.list_of_variable_identifiers()
        variable_port_type = ctx.variable_port_type()

        if list_of_variable_identifiers:
            variable_identifiers = self.visitList_of_variable_identifiers(
                list_of_variable_identifiers
            )

            if variable_port_type:
                port_dimension = self.visitVariable_port_type(variable_port_type)
            else:
                raise IllegalStateException(
                    "Variable port type is mandatory for ref declaration"
                )

            return [
                Port(
                    name=variable_identifier,
                    direction="input",
                    dimension=port_dimension,
                    has_default=False,
                )
                for variable_identifier in variable_identifiers
            ]
        return []

    def visitVariable_port_type(
        self, ctx: SystemVerilogParser.Variable_port_typeContext
    ) -> PORT_DIMENSION:
        var_data_type = ctx.var_data_type()
        if var_data_type:
            return self.visitVar_data_type(var_data_type)
        raise IllegalStateException("Variable port type must hold a vard data type")

    def visitVar_data_type(self, ctx: SystemVerilogParser.Var_data_typeContext):
        data_type = ctx.data_type()
        data_type_or_implicit = ctx.data_type_or_implicit()

        if data_type:
            return self.visitData_type(data_type)
        if data_type_or_implicit:
            return self.visitData_type_or_implicit(data_type_or_implicit)

        return "scalar"

    def visitInout_declaration(
        self, ctx: SystemVerilogParser.Inout_declarationContext
    ) -> list[Port]:

        parsed_identifiers: list[str]
        parsed_port_size: PORT_DIMENSION
        ports: list[Port]

        list_of_port_identifiers = ctx.list_of_port_identifiers()
        net_port_type = ctx.net_port_type()

        if list_of_port_identifiers:
            parsed_identifiers = self.visitList_of_port_identifiers(
                list_of_port_identifiers
            )

            if net_port_type:
                parsed_port_size = self.visitNet_port_type(net_port_type)
            else:
                parsed_port_size = "scalar"

            ports = []
            for parsed_identifier in parsed_identifiers:
                ports.append(
                    Port(
                        name=parsed_identifier,
                        direction="inout",
                        dimension=parsed_port_size,
                        has_default=False,
                    )
                )

        return []

    def visitOutput_declaration(
        self, ctx: SystemVerilogParser.Input_declarationContext
    ) -> list[Port]:
        port_identifiers: list[str]
        variable_identifiers: list[str]
        port_dimension: PORT_DIMENSION

        list_of_port_identifiers = ctx.list_of_port_identifiers()
        list_of_variable_identifiers = ctx.list_of_variable_identifiers()
        implicit_data_type = ctx.implicit_data_type()
        data_type_or_implicit = ctx.data_type_or_implicit()
        data_type = ctx.data_type()

        if list_of_port_identifiers:
            port_identifiers = self.visitList_of_port_identifiers(
                list_of_port_identifiers
            )
            port_dimension = "scalar"
            if implicit_data_type:
                port_dimension = self.visitImplicit_data_type(implicit_data_type)
            elif data_type_or_implicit:
                port_dimension = self.visitData_type_or_implicit(data_type_or_implicit)
            return [
                Port(
                    name=port_identifier,
                    direction="output",
                    dimension=port_dimension,
                    has_default=False,
                )
                for port_identifier in port_identifiers
            ]
        elif list_of_variable_identifiers:
            variable_identifiers = self.visitList_of_variable_identifiers(
                list_of_variable_identifiers
            )
            port_dimension = "scalar"
            if data_type_or_implicit:
                port_dimension = self.visitData_type_or_implicit(data_type_or_implicit)
            if data_type:
                port_dimension = self.visitData_type(data_type)
            return [
                Port(
                    name=port_identifier,
                    direction="output",
                    dimension=port_dimension,
                    has_default=False,
                )
                for port_identifier in variable_identifiers
            ]

        return []

    def visitInput_declaration(
        self, ctx: SystemVerilogParser.Input_declarationContext
    ) -> list[Port]:
        port_identifiers: list[str]
        variable_identifiers: list[str]
        port_dimension: PORT_DIMENSION

        list_of_port_identifiers = ctx.list_of_port_identifiers()
        list_of_variable_identifiers = ctx.list_of_variable_identifiers()
        implicit_data_type = ctx.implicit_data_type()
        data_type_or_implicit = ctx.data_type_or_implicit()
        data_type = ctx.data_type()

        if list_of_port_identifiers:
            port_identifiers = self.visitList_of_port_identifiers(
                list_of_port_identifiers
            )
            port_dimension = "scalar"
            if implicit_data_type:
                port_dimension = self.visitImplicit_data_type(implicit_data_type)
            elif data_type_or_implicit:
                port_dimension = self.visitData_type_or_implicit(data_type_or_implicit)
            return [
                Port(
                    name=port_identifier,
                    direction="input",
                    dimension=port_dimension,
                    has_default=False,
                )
                for port_identifier in port_identifiers
            ]
        elif list_of_variable_identifiers:
            variable_identifiers = self.visitList_of_variable_identifiers(
                list_of_variable_identifiers
            )
            port_dimension = "scalar"
            if data_type_or_implicit:
                port_dimension = self.visitData_type_or_implicit(data_type_or_implicit)
            if data_type:
                port_dimension = self.visitData_type(data_type)
            return [
                Port(
                    name=port_identifier,
                    direction="input",
                    dimension=port_dimension,
                    has_default=False,
                )
                for port_identifier in variable_identifiers
            ]

        return []

    def visitList_of_variable_identifiers(
        self, ctx: SystemVerilogParser.List_of_variable_identifiersContext
    ) -> list[str]:
        variables: list[str]

        var_ids = ctx.var_id()
        if var_ids:
            variables = []
            for var_id in var_ids:
                variables.append(self.visitVar_id(var_id))
            return variables
        raise IllegalStateException(
            "A list of variable identifiers must contain at least one identifier"
        )

    def visitVar_id(self, ctx: SystemVerilogParser.Var_idContext) -> str:

        variable_identifier = ctx.variable_identifier()

        if variable_identifier:
            return variable_identifier.getText()
        raise IllegalStateException("A var_id must contain a variable identifier")

    def visitNet_port_type(
        self, ctx: SystemVerilogParser.Net_port_typeContext
    ) -> PORT_DIMENSION:
        data_type_or_implicit = ctx.data_type_or_implicit()
        implicit_data_type = ctx.implicit_data_type()

        if data_type_or_implicit:
            return self.visitData_type_or_implicit(data_type_or_implicit)
        if implicit_data_type:
            return self.visitImplicit_data_type(implicit_data_type)

        return "scalar"

    def visitData_type_or_implicit(
        self, ctx: SystemVerilogParser.Data_type_or_implicitContext
    ) -> PORT_DIMENSION:
        data_type = ctx.data_type()
        implicit_data_type = ctx.implicit_data_type()

        if data_type:
            return self.visitData_type(data_type)
        if implicit_data_type:
            return self.visitImplicit_data_type(implicit_data_type)

        raise IllegalStateException(
            "Data type or implicit needs either data type or implicit"
        )

    def visitData_type(
        self, ctx: SystemVerilogParser.Data_typeContext
    ) -> PORT_DIMENSION:
        packed_dimension = ctx.packed_dimension()
        if packed_dimension:
            return "vectorial"
        else:
            return "scalar"

    def visitImplicit_data_type(
        self, ctx: SystemVerilogParser.Implicit_data_typeContext
    ) -> PORT_DIMENSION:
        packed_dimension = ctx.packed_dimension()

        if packed_dimension:
            return "vectorial"
        else:
            return "scalar"

    def visitList_of_port_identifiers(
        self, ctx: SystemVerilogParser.List_of_port_identifiersContext
    ) -> list[str]:
        parsed_port_ids: list[str]

        port_ids = ctx.port_id()

        if port_ids:
            parsed_port_ids = []
            for port_id in port_ids:
                parsed_port_ids.append(port_id.getText())
            return parsed_port_ids
        return []

    def visitSpecify_block(
        self, ctx: SystemVerilogParser.Specify_blockContext
    ) -> list[AntlrParameter]:
        parsed_specify_items: list[AntlrParameter]

        specify_items = ctx.specify_item()
        if specify_items:
            parsed_specify_items = []
            for specify_item in specify_items:
                parameters = self.visitSpecify_item(specify_item)
                if parameters:
                    parsed_specify_items += parameters
            return parsed_specify_items

        return []

    def visitSpecify_item(
        self, ctx: SystemVerilogParser.Specify_itemContext
    ) -> list[AntlrParameter]:
        specparam_declaration = ctx.specparam_declaration()

        if specparam_declaration:
            return self.visitSpecparam_declaration(specparam_declaration)

        return []

    def visitSpecparam_declaration(
        self, ctx: SystemVerilogParser.Specparam_declarationContext
    ) -> list[AntlrParameter]:
        list_of_specparam_assignments = ctx.list_of_specparam_assignments()

        if list_of_specparam_assignments:
            return self.visitList_of_specparam_assignments(
                list_of_specparam_assignments
            )

        return []

    def visitList_of_specparam_assignments(
        self, ctx: SystemVerilogParser.List_of_specparam_assignmentsContext
    ) -> list[AntlrParameter]:
        parsed_spec_param_assignments: list[AntlrParameter]

        spec_param_assignments = ctx.specparam_assignment()
        if spec_param_assignments:
            parsed_spec_param_assignments = []
            for spec_param_assignment in spec_param_assignments:
                parameter = self.visitSpecparam_assignment(spec_param_assignment)
                if parameter:
                    parsed_spec_param_assignments.append(parameter)
            return parsed_spec_param_assignments

        raise IllegalStateException(
            "Specparam assignment list must have at least one item"
        )

    def visitSpecparam_assignment(
        self, ctx: SystemVerilogParser.Specparam_assignmentContext
    ) -> Optional[AntlrParameter]:
        # pulse control is ignored

        parsed_identifier: str
        specparam_identifier = ctx.specparam_identifier()
        expression = ctx.constant_mintypmax_expression()

        if specparam_identifier:
            parsed_identifier = specparam_identifier.getText()
            if expression:
                return AntlrParameter(
                    name=parsed_identifier,
                    value=expression.getText(),
                    rule=expression,
                    has_default=True,
                )
            else:
                raise IllegalStateException("Specparams must have an assigned values")

        return None

    def visitModule_common_item(
        self, ctx: SystemVerilogParser.Module_common_itemContext
    ) -> list[AntlrParameter]:
        module_item_declaration = ctx.module_item_declaration()

        if module_item_declaration:
            return self.visitModule_item_declaration(module_item_declaration)

        return []

    def visitModule_item_declaration(
        self, ctx: SystemVerilogParser.Module_item_declarationContext
    ) -> list[AntlrParameter]:
        # genvar and clocking declarations are ignored

        package_item_declaration = ctx.package_item_declaration()

        if package_item_declaration:
            return self.visitPackage_item_declaration(package_item_declaration)

        return []

    def visitPackage_item_declaration(
        self, ctx: SystemVerilogParser.Package_item_declarationContext
    ) -> list[AntlrParameter]:
        # we only parse local_parameters and parameters
        # all other constructs (classes, interface, functions...)
        # are ignored

        local_parameter_declaration = ctx.local_parameter_declaration()
        parameter_declaration = ctx.parameter_declaration()

        if local_parameter_declaration:
            return self.visitLocal_parameter_declaration(local_parameter_declaration)
        elif parameter_declaration:
            return self.visitParameter_declaration(parameter_declaration)

        return []

    def visitLocal_parameter_declaration(
        self, ctx: SystemVerilogParser.Local_parameter_declarationContext
    ) -> list[AntlrParameter]:
        # localparam types are ignored
        # localparam type handle definitions are ignored

        list_of_param_assignments = ctx.list_of_param_assignments()
        if list_of_param_assignments:
            return self.visitList_of_param_assignments(list_of_param_assignments)

        return []

    def visitParameter_declaration(
        self, ctx: SystemVerilogParser.Local_parameter_declarationContext
    ) -> list[AntlrParameter]:
        # param types are ignored
        # param type handle definitions are ignored

        list_of_param_assignments = ctx.list_of_param_assignments()
        if list_of_param_assignments:
            return self.visitList_of_param_assignments(list_of_param_assignments)

        return []

    def visitList_of_param_assignments(
        self, ctx: SystemVerilogParser.List_of_param_assignmentsContext
    ) -> list[AntlrParameter]:
        parsed_param_assignments: list[AntlrParameter]

        param_assignments = ctx.param_assignment()
        if param_assignments:
            parsed_param_assignments = []
            for param_assignment in param_assignments:
                parsed_param_assignments.append(
                    self.visitParam_assignment(param_assignment)
                )
            return parsed_param_assignments

        raise IllegalStateException(
            "A list of parameter assignments must include at least one parameter"
        )

    def visitParam_assignment(
        self, ctx: SystemVerilogParser.Param_assignmentContext
    ) -> AntlrParameter:
        # eventual dimensions are skipped
        parsed_parameter_identifier: str
        parsed_parameter_value: str
        parameter_value_context: SystemVerilogParser.Constant_param_expressionContext
        has_default: bool

        parameter_identifier = ctx.parameter_identifier()
        constant_param_expression = ctx.constant_param_expression()

        if parameter_identifier:
            parsed_parameter_identifier = parameter_identifier.getText()

            if constant_param_expression:
                parsed_parameter_value = constant_param_expression.getText()
                parameter_value_context = constant_param_expression
                has_default = True
            else:
                parsed_parameter_value = ""
                parameter_value_context = parameter_identifier
                has_default = False

            return AntlrParameter(
                name=parsed_parameter_identifier,
                value=parsed_parameter_value,
                rule=parameter_value_context,
                has_default=has_default,
            )
        raise IllegalStateException(
            "Parameter identifier is mandatory in parameter assignment"
        )

    @staticmethod
    def multiple_not_none_items(l: list[Any]):
        return any(
            [
                (True if context_1 is not None and context_2 is not None else False)
                for context_1, context_2 in zip(l, l)
            ]
        )
