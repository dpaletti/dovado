# Generated from vhdlParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .vhdlParser import vhdlParser
else:
    from vhdlParser import vhdlParser

# This class defines a complete generic visitor for a parse tree produced by vhdlParser.

class vhdlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by vhdlParser#any_keyword.
    def visitAny_keyword(self, ctx:vhdlParser.Any_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#name_literal.
    def visitName_literal(self, ctx:vhdlParser.Name_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#name.
    def visitName(self, ctx:vhdlParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#name_slice_part.
    def visitName_slice_part(self, ctx:vhdlParser.Name_slice_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#name_attribute_part.
    def visitName_attribute_part(self, ctx:vhdlParser.Name_attribute_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#attribute_name.
    def visitAttribute_name(self, ctx:vhdlParser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#suffix.
    def visitSuffix(self, ctx:vhdlParser.SuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#explicit_range.
    def visitExplicit_range(self, ctx:vhdlParser.Explicit_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#selected_name.
    def visitSelected_name(self, ctx:vhdlParser.Selected_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_declaration.
    def visitEntity_declaration(self, ctx:vhdlParser.Entity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_declarative_item.
    def visitEntity_declarative_item(self, ctx:vhdlParser.Entity_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_statement.
    def visitEntity_statement(self, ctx:vhdlParser.Entity_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#architecture_body.
    def visitArchitecture_body(self, ctx:vhdlParser.Architecture_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_declarative_item.
    def visitBlock_declarative_item(self, ctx:vhdlParser.Block_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#configuration_declaration.
    def visitConfiguration_declaration(self, ctx:vhdlParser.Configuration_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#configuration_declarative_item.
    def visitConfiguration_declarative_item(self, ctx:vhdlParser.Configuration_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_configuration.
    def visitBlock_configuration(self, ctx:vhdlParser.Block_configurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_specification.
    def visitBlock_specification(self, ctx:vhdlParser.Block_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generate_specification.
    def visitGenerate_specification(self, ctx:vhdlParser.Generate_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#configuration_item.
    def visitConfiguration_item(self, ctx:vhdlParser.Configuration_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#component_configuration.
    def visitComponent_configuration(self, ctx:vhdlParser.Component_configurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subprogram_declaration.
    def visitSubprogram_declaration(self, ctx:vhdlParser.Subprogram_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subprogram_specification.
    def visitSubprogram_specification(self, ctx:vhdlParser.Subprogram_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#procedure_specification.
    def visitProcedure_specification(self, ctx:vhdlParser.Procedure_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#function_specification.
    def visitFunction_specification(self, ctx:vhdlParser.Function_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subprogram_header.
    def visitSubprogram_header(self, ctx:vhdlParser.Subprogram_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#designator.
    def visitDesignator(self, ctx:vhdlParser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#operator_symbol.
    def visitOperator_symbol(self, ctx:vhdlParser.Operator_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#formal_parameter_list.
    def visitFormal_parameter_list(self, ctx:vhdlParser.Formal_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subprogram_body.
    def visitSubprogram_body(self, ctx:vhdlParser.Subprogram_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subprogram_kind.
    def visitSubprogram_kind(self, ctx:vhdlParser.Subprogram_kindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subprogram_instantiation_declaration.
    def visitSubprogram_instantiation_declaration(self, ctx:vhdlParser.Subprogram_instantiation_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signature.
    def visitSignature(self, ctx:vhdlParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#package_declaration.
    def visitPackage_declaration(self, ctx:vhdlParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#package_declarative_item.
    def visitPackage_declarative_item(self, ctx:vhdlParser.Package_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#package_body.
    def visitPackage_body(self, ctx:vhdlParser.Package_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#package_instantiation_declaration.
    def visitPackage_instantiation_declaration(self, ctx:vhdlParser.Package_instantiation_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#scalar_type_definition.
    def visitScalar_type_definition(self, ctx:vhdlParser.Scalar_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#range_constraint.
    def visitRange_constraint(self, ctx:vhdlParser.Range_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#range_.
    def visitRange_(self, ctx:vhdlParser.Range_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#direction.
    def visitDirection(self, ctx:vhdlParser.DirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#enumeration_type_definition.
    def visitEnumeration_type_definition(self, ctx:vhdlParser.Enumeration_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#enumeration_literal.
    def visitEnumeration_literal(self, ctx:vhdlParser.Enumeration_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#integer_type_definition.
    def visitInteger_type_definition(self, ctx:vhdlParser.Integer_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#physical_type_definition.
    def visitPhysical_type_definition(self, ctx:vhdlParser.Physical_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#primary_unit_declaration.
    def visitPrimary_unit_declaration(self, ctx:vhdlParser.Primary_unit_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#secondary_unit_declaration.
    def visitSecondary_unit_declaration(self, ctx:vhdlParser.Secondary_unit_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#floating_type_definition.
    def visitFloating_type_definition(self, ctx:vhdlParser.Floating_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#composite_type_definition.
    def visitComposite_type_definition(self, ctx:vhdlParser.Composite_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#array_type_definition.
    def visitArray_type_definition(self, ctx:vhdlParser.Array_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#unbounded_array_definition.
    def visitUnbounded_array_definition(self, ctx:vhdlParser.Unbounded_array_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#constrained_array_definition.
    def visitConstrained_array_definition(self, ctx:vhdlParser.Constrained_array_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#index_subtype_definition.
    def visitIndex_subtype_definition(self, ctx:vhdlParser.Index_subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#array_constraint.
    def visitArray_constraint(self, ctx:vhdlParser.Array_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#array_element_constraint.
    def visitArray_element_constraint(self, ctx:vhdlParser.Array_element_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#index_constraint.
    def visitIndex_constraint(self, ctx:vhdlParser.Index_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#discrete_range.
    def visitDiscrete_range(self, ctx:vhdlParser.Discrete_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#record_type_definition.
    def visitRecord_type_definition(self, ctx:vhdlParser.Record_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#element_declaration.
    def visitElement_declaration(self, ctx:vhdlParser.Element_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#identifier_list.
    def visitIdentifier_list(self, ctx:vhdlParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#element_subtype_definition.
    def visitElement_subtype_definition(self, ctx:vhdlParser.Element_subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#record_constraint.
    def visitRecord_constraint(self, ctx:vhdlParser.Record_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#record_element_constraint.
    def visitRecord_element_constraint(self, ctx:vhdlParser.Record_element_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#access_type_definition.
    def visitAccess_type_definition(self, ctx:vhdlParser.Access_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#incomplete_type_declaration.
    def visitIncomplete_type_declaration(self, ctx:vhdlParser.Incomplete_type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#file_type_definition.
    def visitFile_type_definition(self, ctx:vhdlParser.File_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#protected_type_definition.
    def visitProtected_type_definition(self, ctx:vhdlParser.Protected_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#protected_type_declaration.
    def visitProtected_type_declaration(self, ctx:vhdlParser.Protected_type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#protected_type_declarative_item.
    def visitProtected_type_declarative_item(self, ctx:vhdlParser.Protected_type_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#protected_type_body.
    def visitProtected_type_body(self, ctx:vhdlParser.Protected_type_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#type_declaration.
    def visitType_declaration(self, ctx:vhdlParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#full_type_declaration.
    def visitFull_type_declaration(self, ctx:vhdlParser.Full_type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#type_definition.
    def visitType_definition(self, ctx:vhdlParser.Type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subtype_declaration.
    def visitSubtype_declaration(self, ctx:vhdlParser.Subtype_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subtype_indication.
    def visitSubtype_indication(self, ctx:vhdlParser.Subtype_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#resolution_indication.
    def visitResolution_indication(self, ctx:vhdlParser.Resolution_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#element_resolution.
    def visitElement_resolution(self, ctx:vhdlParser.Element_resolutionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#array_element_resolution.
    def visitArray_element_resolution(self, ctx:vhdlParser.Array_element_resolutionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#record_resolution.
    def visitRecord_resolution(self, ctx:vhdlParser.Record_resolutionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#record_element_resolution.
    def visitRecord_element_resolution(self, ctx:vhdlParser.Record_element_resolutionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#type_mark.
    def visitType_mark(self, ctx:vhdlParser.Type_markContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#constraint.
    def visitConstraint(self, ctx:vhdlParser.ConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#element_constraint.
    def visitElement_constraint(self, ctx:vhdlParser.Element_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#object_declaration.
    def visitObject_declaration(self, ctx:vhdlParser.Object_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#constant_declaration.
    def visitConstant_declaration(self, ctx:vhdlParser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signal_declaration.
    def visitSignal_declaration(self, ctx:vhdlParser.Signal_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signal_kind.
    def visitSignal_kind(self, ctx:vhdlParser.Signal_kindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#variable_declaration.
    def visitVariable_declaration(self, ctx:vhdlParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#file_declaration.
    def visitFile_declaration(self, ctx:vhdlParser.File_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#file_open_information.
    def visitFile_open_information(self, ctx:vhdlParser.File_open_informationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#file_logical_name.
    def visitFile_logical_name(self, ctx:vhdlParser.File_logical_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_declaration.
    def visitInterface_declaration(self, ctx:vhdlParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_object_declaration.
    def visitInterface_object_declaration(self, ctx:vhdlParser.Interface_object_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_constant_declaration.
    def visitInterface_constant_declaration(self, ctx:vhdlParser.Interface_constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_signal_declaration.
    def visitInterface_signal_declaration(self, ctx:vhdlParser.Interface_signal_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_variable_declaration.
    def visitInterface_variable_declaration(self, ctx:vhdlParser.Interface_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_file_declaration.
    def visitInterface_file_declaration(self, ctx:vhdlParser.Interface_file_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signal_mode.
    def visitSignal_mode(self, ctx:vhdlParser.Signal_modeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_type_declaration.
    def visitInterface_type_declaration(self, ctx:vhdlParser.Interface_type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_incomplete_type_declaration.
    def visitInterface_incomplete_type_declaration(self, ctx:vhdlParser.Interface_incomplete_type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_subprogram_declaration.
    def visitInterface_subprogram_declaration(self, ctx:vhdlParser.Interface_subprogram_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_subprogram_specification.
    def visitInterface_subprogram_specification(self, ctx:vhdlParser.Interface_subprogram_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_procedure_specification.
    def visitInterface_procedure_specification(self, ctx:vhdlParser.Interface_procedure_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_function_specification.
    def visitInterface_function_specification(self, ctx:vhdlParser.Interface_function_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_subprogram_default.
    def visitInterface_subprogram_default(self, ctx:vhdlParser.Interface_subprogram_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_package_declaration.
    def visitInterface_package_declaration(self, ctx:vhdlParser.Interface_package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_package_generic_map_aspect.
    def visitInterface_package_generic_map_aspect(self, ctx:vhdlParser.Interface_package_generic_map_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_list.
    def visitInterface_list(self, ctx:vhdlParser.Interface_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_element.
    def visitInterface_element(self, ctx:vhdlParser.Interface_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generic_clause.
    def visitGeneric_clause(self, ctx:vhdlParser.Generic_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generic_list.
    def visitGeneric_list(self, ctx:vhdlParser.Generic_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#port_clause.
    def visitPort_clause(self, ctx:vhdlParser.Port_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#port_list.
    def visitPort_list(self, ctx:vhdlParser.Port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#association_list.
    def visitAssociation_list(self, ctx:vhdlParser.Association_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#association_element.
    def visitAssociation_element(self, ctx:vhdlParser.Association_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#formal_part.
    def visitFormal_part(self, ctx:vhdlParser.Formal_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#actual_part.
    def visitActual_part(self, ctx:vhdlParser.Actual_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#actual_designator.
    def visitActual_designator(self, ctx:vhdlParser.Actual_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generic_map_aspect.
    def visitGeneric_map_aspect(self, ctx:vhdlParser.Generic_map_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#port_map_aspect.
    def visitPort_map_aspect(self, ctx:vhdlParser.Port_map_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#alias_declaration.
    def visitAlias_declaration(self, ctx:vhdlParser.Alias_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#alias_designator.
    def visitAlias_designator(self, ctx:vhdlParser.Alias_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:vhdlParser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#component_declaration.
    def visitComponent_declaration(self, ctx:vhdlParser.Component_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#group_template_declaration.
    def visitGroup_template_declaration(self, ctx:vhdlParser.Group_template_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_class_entry_list.
    def visitEntity_class_entry_list(self, ctx:vhdlParser.Entity_class_entry_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_class_entry.
    def visitEntity_class_entry(self, ctx:vhdlParser.Entity_class_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#group_declaration.
    def visitGroup_declaration(self, ctx:vhdlParser.Group_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#group_constituent_list.
    def visitGroup_constituent_list(self, ctx:vhdlParser.Group_constituent_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#group_constituent.
    def visitGroup_constituent(self, ctx:vhdlParser.Group_constituentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#attribute_specification.
    def visitAttribute_specification(self, ctx:vhdlParser.Attribute_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_specification.
    def visitEntity_specification(self, ctx:vhdlParser.Entity_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_class.
    def visitEntity_class(self, ctx:vhdlParser.Entity_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_name_list.
    def visitEntity_name_list(self, ctx:vhdlParser.Entity_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_designator.
    def visitEntity_designator(self, ctx:vhdlParser.Entity_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_tag.
    def visitEntity_tag(self, ctx:vhdlParser.Entity_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#configuration_specification.
    def visitConfiguration_specification(self, ctx:vhdlParser.Configuration_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simple_configuration_specification.
    def visitSimple_configuration_specification(self, ctx:vhdlParser.Simple_configuration_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#compound_configuration_specification.
    def visitCompound_configuration_specification(self, ctx:vhdlParser.Compound_configuration_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#component_specification.
    def visitComponent_specification(self, ctx:vhdlParser.Component_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#instantiation_list.
    def visitInstantiation_list(self, ctx:vhdlParser.Instantiation_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#binding_indication.
    def visitBinding_indication(self, ctx:vhdlParser.Binding_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_aspect.
    def visitEntity_aspect(self, ctx:vhdlParser.Entity_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#verification_unit_binding_indication.
    def visitVerification_unit_binding_indication(self, ctx:vhdlParser.Verification_unit_binding_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#verification_unit_list.
    def visitVerification_unit_list(self, ctx:vhdlParser.Verification_unit_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#disconnection_specification.
    def visitDisconnection_specification(self, ctx:vhdlParser.Disconnection_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#guarded_signal_specification.
    def visitGuarded_signal_specification(self, ctx:vhdlParser.Guarded_signal_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signal_list.
    def visitSignal_list(self, ctx:vhdlParser.Signal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#attribute_designator.
    def visitAttribute_designator(self, ctx:vhdlParser.Attribute_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#external_name.
    def visitExternal_name(self, ctx:vhdlParser.External_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#external_pathname.
    def visitExternal_pathname(self, ctx:vhdlParser.External_pathnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#package_pathname.
    def visitPackage_pathname(self, ctx:vhdlParser.Package_pathnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#absolute_pathname.
    def visitAbsolute_pathname(self, ctx:vhdlParser.Absolute_pathnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#relative_pathname.
    def visitRelative_pathname(self, ctx:vhdlParser.Relative_pathnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#partial_pathname.
    def visitPartial_pathname(self, ctx:vhdlParser.Partial_pathnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#pathname_element.
    def visitPathname_element(self, ctx:vhdlParser.Pathname_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#expression.
    def visitExpression(self, ctx:vhdlParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simple_expression.
    def visitSimple_expression(self, ctx:vhdlParser.Simple_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#primary.
    def visitPrimary(self, ctx:vhdlParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#logical_operator.
    def visitLogical_operator(self, ctx:vhdlParser.Logical_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#relational_operator.
    def visitRelational_operator(self, ctx:vhdlParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#shift_operator.
    def visitShift_operator(self, ctx:vhdlParser.Shift_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#adding_operator.
    def visitAdding_operator(self, ctx:vhdlParser.Adding_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#sign.
    def visitSign(self, ctx:vhdlParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#multiplying_operator.
    def visitMultiplying_operator(self, ctx:vhdlParser.Multiplying_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#miscellaneous_operator.
    def visitMiscellaneous_operator(self, ctx:vhdlParser.Miscellaneous_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#numeric_literal.
    def visitNumeric_literal(self, ctx:vhdlParser.Numeric_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#physical_literal.
    def visitPhysical_literal(self, ctx:vhdlParser.Physical_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#aggregate.
    def visitAggregate(self, ctx:vhdlParser.AggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#element_association.
    def visitElement_association(self, ctx:vhdlParser.Element_associationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#choices.
    def visitChoices(self, ctx:vhdlParser.ChoicesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#choice.
    def visitChoice(self, ctx:vhdlParser.ChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#qualified_expression.
    def visitQualified_expression(self, ctx:vhdlParser.Qualified_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#allocator.
    def visitAllocator(self, ctx:vhdlParser.AllocatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#sequence_of_statements.
    def visitSequence_of_statements(self, ctx:vhdlParser.Sequence_of_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#sequential_statement.
    def visitSequential_statement(self, ctx:vhdlParser.Sequential_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#wait_statement.
    def visitWait_statement(self, ctx:vhdlParser.Wait_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#sensitivity_clause.
    def visitSensitivity_clause(self, ctx:vhdlParser.Sensitivity_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#sensitivity_list.
    def visitSensitivity_list(self, ctx:vhdlParser.Sensitivity_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#condition_clause.
    def visitCondition_clause(self, ctx:vhdlParser.Condition_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#condition.
    def visitCondition(self, ctx:vhdlParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#timeout_clause.
    def visitTimeout_clause(self, ctx:vhdlParser.Timeout_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#assertion_statement.
    def visitAssertion_statement(self, ctx:vhdlParser.Assertion_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#assertion.
    def visitAssertion(self, ctx:vhdlParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#report_statement.
    def visitReport_statement(self, ctx:vhdlParser.Report_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signal_assignment_statement.
    def visitSignal_assignment_statement(self, ctx:vhdlParser.Signal_assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simple_signal_assignment.
    def visitSimple_signal_assignment(self, ctx:vhdlParser.Simple_signal_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simple_waveform_assignment.
    def visitSimple_waveform_assignment(self, ctx:vhdlParser.Simple_waveform_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simple_force_assignment.
    def visitSimple_force_assignment(self, ctx:vhdlParser.Simple_force_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simple_release_assignment.
    def visitSimple_release_assignment(self, ctx:vhdlParser.Simple_release_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#force_mode.
    def visitForce_mode(self, ctx:vhdlParser.Force_modeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#delay_mechanism.
    def visitDelay_mechanism(self, ctx:vhdlParser.Delay_mechanismContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#target.
    def visitTarget(self, ctx:vhdlParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#waveform.
    def visitWaveform(self, ctx:vhdlParser.WaveformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#waveform_element.
    def visitWaveform_element(self, ctx:vhdlParser.Waveform_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#conditional_signal_assignment.
    def visitConditional_signal_assignment(self, ctx:vhdlParser.Conditional_signal_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#conditional_waveform_assignment.
    def visitConditional_waveform_assignment(self, ctx:vhdlParser.Conditional_waveform_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#conditional_waveforms.
    def visitConditional_waveforms(self, ctx:vhdlParser.Conditional_waveformsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#conditional_force_assignment.
    def visitConditional_force_assignment(self, ctx:vhdlParser.Conditional_force_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#conditional_expressions.
    def visitConditional_expressions(self, ctx:vhdlParser.Conditional_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#selected_signal_assignment.
    def visitSelected_signal_assignment(self, ctx:vhdlParser.Selected_signal_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#selected_waveform_assignment.
    def visitSelected_waveform_assignment(self, ctx:vhdlParser.Selected_waveform_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#selected_waveforms.
    def visitSelected_waveforms(self, ctx:vhdlParser.Selected_waveformsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#selected_force_assignment.
    def visitSelected_force_assignment(self, ctx:vhdlParser.Selected_force_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#selected_expressions.
    def visitSelected_expressions(self, ctx:vhdlParser.Selected_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#variable_assignment_statement.
    def visitVariable_assignment_statement(self, ctx:vhdlParser.Variable_assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simple_variable_assignment.
    def visitSimple_variable_assignment(self, ctx:vhdlParser.Simple_variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#conditional_variable_assignment.
    def visitConditional_variable_assignment(self, ctx:vhdlParser.Conditional_variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#selected_variable_assignment.
    def visitSelected_variable_assignment(self, ctx:vhdlParser.Selected_variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#procedure_call_statement.
    def visitProcedure_call_statement(self, ctx:vhdlParser.Procedure_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#procedure_call.
    def visitProcedure_call(self, ctx:vhdlParser.Procedure_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#if_statement.
    def visitIf_statement(self, ctx:vhdlParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#case_statement.
    def visitCase_statement(self, ctx:vhdlParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#case_statement_alternative.
    def visitCase_statement_alternative(self, ctx:vhdlParser.Case_statement_alternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#loop_statement.
    def visitLoop_statement(self, ctx:vhdlParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#iteration_scheme.
    def visitIteration_scheme(self, ctx:vhdlParser.Iteration_schemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#parameter_specification.
    def visitParameter_specification(self, ctx:vhdlParser.Parameter_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#next_statement.
    def visitNext_statement(self, ctx:vhdlParser.Next_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#exit_statement.
    def visitExit_statement(self, ctx:vhdlParser.Exit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#return_statement.
    def visitReturn_statement(self, ctx:vhdlParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#null_statement.
    def visitNull_statement(self, ctx:vhdlParser.Null_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#concurrent_statement_with_optional_label.
    def visitConcurrent_statement_with_optional_label(self, ctx:vhdlParser.Concurrent_statement_with_optional_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#concurrent_statement.
    def visitConcurrent_statement(self, ctx:vhdlParser.Concurrent_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_statement.
    def visitBlock_statement(self, ctx:vhdlParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_header.
    def visitBlock_header(self, ctx:vhdlParser.Block_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#process_statement.
    def visitProcess_statement(self, ctx:vhdlParser.Process_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#process_sensitivity_list.
    def visitProcess_sensitivity_list(self, ctx:vhdlParser.Process_sensitivity_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#process_or_package_declarative_item.
    def visitProcess_or_package_declarative_item(self, ctx:vhdlParser.Process_or_package_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#process_declarative_item.
    def visitProcess_declarative_item(self, ctx:vhdlParser.Process_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#concurrent_procedure_call_statement.
    def visitConcurrent_procedure_call_statement(self, ctx:vhdlParser.Concurrent_procedure_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#concurrent_assertion_statement.
    def visitConcurrent_assertion_statement(self, ctx:vhdlParser.Concurrent_assertion_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#concurrent_signal_assignment_statement.
    def visitConcurrent_signal_assignment_statement(self, ctx:vhdlParser.Concurrent_signal_assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#concurrent_signal_assignment_any.
    def visitConcurrent_signal_assignment_any(self, ctx:vhdlParser.Concurrent_signal_assignment_anyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#concurrent_selected_signal_assignment.
    def visitConcurrent_selected_signal_assignment(self, ctx:vhdlParser.Concurrent_selected_signal_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#component_instantiation_statement.
    def visitComponent_instantiation_statement(self, ctx:vhdlParser.Component_instantiation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#instantiated_unit.
    def visitInstantiated_unit(self, ctx:vhdlParser.Instantiated_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generate_statement.
    def visitGenerate_statement(self, ctx:vhdlParser.Generate_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#for_generate_statement.
    def visitFor_generate_statement(self, ctx:vhdlParser.For_generate_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#if_generate_statement.
    def visitIf_generate_statement(self, ctx:vhdlParser.If_generate_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#case_generate_statement.
    def visitCase_generate_statement(self, ctx:vhdlParser.Case_generate_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#case_generate_alternative.
    def visitCase_generate_alternative(self, ctx:vhdlParser.Case_generate_alternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generate_statement_body_with_begin_end.
    def visitGenerate_statement_body_with_begin_end(self, ctx:vhdlParser.Generate_statement_body_with_begin_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generate_statement_body.
    def visitGenerate_statement_body(self, ctx:vhdlParser.Generate_statement_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#label.
    def visitLabel(self, ctx:vhdlParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#use_clause.
    def visitUse_clause(self, ctx:vhdlParser.Use_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#design_file.
    def visitDesign_file(self, ctx:vhdlParser.Design_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#design_unit.
    def visitDesign_unit(self, ctx:vhdlParser.Design_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#library_unit.
    def visitLibrary_unit(self, ctx:vhdlParser.Library_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#primary_unit.
    def visitPrimary_unit(self, ctx:vhdlParser.Primary_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#secondary_unit.
    def visitSecondary_unit(self, ctx:vhdlParser.Secondary_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#library_clause.
    def visitLibrary_clause(self, ctx:vhdlParser.Library_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#logical_name_list.
    def visitLogical_name_list(self, ctx:vhdlParser.Logical_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#context_declaration.
    def visitContext_declaration(self, ctx:vhdlParser.Context_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#context_clause.
    def visitContext_clause(self, ctx:vhdlParser.Context_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#context_item.
    def visitContext_item(self, ctx:vhdlParser.Context_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#context_reference.
    def visitContext_reference(self, ctx:vhdlParser.Context_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#identifier.
    def visitIdentifier(self, ctx:vhdlParser.IdentifierContext):
        return self.visitChildren(ctx)



del vhdlParser