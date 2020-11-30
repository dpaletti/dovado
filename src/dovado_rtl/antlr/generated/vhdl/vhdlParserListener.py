# Generated from vhdlParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .vhdlParser import vhdlParser
else:
    from vhdlParser import vhdlParser

# This class defines a complete listener for a parse tree produced by vhdlParser.
class vhdlParserListener(ParseTreeListener):

    # Enter a parse tree produced by vhdlParser#any_keyword.
    def enterAny_keyword(self, ctx:vhdlParser.Any_keywordContext):
        pass

    # Exit a parse tree produced by vhdlParser#any_keyword.
    def exitAny_keyword(self, ctx:vhdlParser.Any_keywordContext):
        pass


    # Enter a parse tree produced by vhdlParser#name_literal.
    def enterName_literal(self, ctx:vhdlParser.Name_literalContext):
        pass

    # Exit a parse tree produced by vhdlParser#name_literal.
    def exitName_literal(self, ctx:vhdlParser.Name_literalContext):
        pass


    # Enter a parse tree produced by vhdlParser#name.
    def enterName(self, ctx:vhdlParser.NameContext):
        pass

    # Exit a parse tree produced by vhdlParser#name.
    def exitName(self, ctx:vhdlParser.NameContext):
        pass


    # Enter a parse tree produced by vhdlParser#name_slice_part.
    def enterName_slice_part(self, ctx:vhdlParser.Name_slice_partContext):
        pass

    # Exit a parse tree produced by vhdlParser#name_slice_part.
    def exitName_slice_part(self, ctx:vhdlParser.Name_slice_partContext):
        pass


    # Enter a parse tree produced by vhdlParser#name_attribute_part.
    def enterName_attribute_part(self, ctx:vhdlParser.Name_attribute_partContext):
        pass

    # Exit a parse tree produced by vhdlParser#name_attribute_part.
    def exitName_attribute_part(self, ctx:vhdlParser.Name_attribute_partContext):
        pass


    # Enter a parse tree produced by vhdlParser#attribute_name.
    def enterAttribute_name(self, ctx:vhdlParser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by vhdlParser#attribute_name.
    def exitAttribute_name(self, ctx:vhdlParser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by vhdlParser#suffix.
    def enterSuffix(self, ctx:vhdlParser.SuffixContext):
        pass

    # Exit a parse tree produced by vhdlParser#suffix.
    def exitSuffix(self, ctx:vhdlParser.SuffixContext):
        pass


    # Enter a parse tree produced by vhdlParser#explicit_range.
    def enterExplicit_range(self, ctx:vhdlParser.Explicit_rangeContext):
        pass

    # Exit a parse tree produced by vhdlParser#explicit_range.
    def exitExplicit_range(self, ctx:vhdlParser.Explicit_rangeContext):
        pass


    # Enter a parse tree produced by vhdlParser#selected_name.
    def enterSelected_name(self, ctx:vhdlParser.Selected_nameContext):
        pass

    # Exit a parse tree produced by vhdlParser#selected_name.
    def exitSelected_name(self, ctx:vhdlParser.Selected_nameContext):
        pass


    # Enter a parse tree produced by vhdlParser#entity_declaration.
    def enterEntity_declaration(self, ctx:vhdlParser.Entity_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#entity_declaration.
    def exitEntity_declaration(self, ctx:vhdlParser.Entity_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#entity_declarative_item.
    def enterEntity_declarative_item(self, ctx:vhdlParser.Entity_declarative_itemContext):
        pass

    # Exit a parse tree produced by vhdlParser#entity_declarative_item.
    def exitEntity_declarative_item(self, ctx:vhdlParser.Entity_declarative_itemContext):
        pass


    # Enter a parse tree produced by vhdlParser#entity_statement.
    def enterEntity_statement(self, ctx:vhdlParser.Entity_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#entity_statement.
    def exitEntity_statement(self, ctx:vhdlParser.Entity_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#architecture_body.
    def enterArchitecture_body(self, ctx:vhdlParser.Architecture_bodyContext):
        pass

    # Exit a parse tree produced by vhdlParser#architecture_body.
    def exitArchitecture_body(self, ctx:vhdlParser.Architecture_bodyContext):
        pass


    # Enter a parse tree produced by vhdlParser#block_declarative_item.
    def enterBlock_declarative_item(self, ctx:vhdlParser.Block_declarative_itemContext):
        pass

    # Exit a parse tree produced by vhdlParser#block_declarative_item.
    def exitBlock_declarative_item(self, ctx:vhdlParser.Block_declarative_itemContext):
        pass


    # Enter a parse tree produced by vhdlParser#configuration_declaration.
    def enterConfiguration_declaration(self, ctx:vhdlParser.Configuration_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#configuration_declaration.
    def exitConfiguration_declaration(self, ctx:vhdlParser.Configuration_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#configuration_declarative_item.
    def enterConfiguration_declarative_item(self, ctx:vhdlParser.Configuration_declarative_itemContext):
        pass

    # Exit a parse tree produced by vhdlParser#configuration_declarative_item.
    def exitConfiguration_declarative_item(self, ctx:vhdlParser.Configuration_declarative_itemContext):
        pass


    # Enter a parse tree produced by vhdlParser#block_configuration.
    def enterBlock_configuration(self, ctx:vhdlParser.Block_configurationContext):
        pass

    # Exit a parse tree produced by vhdlParser#block_configuration.
    def exitBlock_configuration(self, ctx:vhdlParser.Block_configurationContext):
        pass


    # Enter a parse tree produced by vhdlParser#block_specification.
    def enterBlock_specification(self, ctx:vhdlParser.Block_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#block_specification.
    def exitBlock_specification(self, ctx:vhdlParser.Block_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#generate_specification.
    def enterGenerate_specification(self, ctx:vhdlParser.Generate_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#generate_specification.
    def exitGenerate_specification(self, ctx:vhdlParser.Generate_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#configuration_item.
    def enterConfiguration_item(self, ctx:vhdlParser.Configuration_itemContext):
        pass

    # Exit a parse tree produced by vhdlParser#configuration_item.
    def exitConfiguration_item(self, ctx:vhdlParser.Configuration_itemContext):
        pass


    # Enter a parse tree produced by vhdlParser#component_configuration.
    def enterComponent_configuration(self, ctx:vhdlParser.Component_configurationContext):
        pass

    # Exit a parse tree produced by vhdlParser#component_configuration.
    def exitComponent_configuration(self, ctx:vhdlParser.Component_configurationContext):
        pass


    # Enter a parse tree produced by vhdlParser#subprogram_declaration.
    def enterSubprogram_declaration(self, ctx:vhdlParser.Subprogram_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#subprogram_declaration.
    def exitSubprogram_declaration(self, ctx:vhdlParser.Subprogram_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#subprogram_specification.
    def enterSubprogram_specification(self, ctx:vhdlParser.Subprogram_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#subprogram_specification.
    def exitSubprogram_specification(self, ctx:vhdlParser.Subprogram_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#procedure_specification.
    def enterProcedure_specification(self, ctx:vhdlParser.Procedure_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#procedure_specification.
    def exitProcedure_specification(self, ctx:vhdlParser.Procedure_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#function_specification.
    def enterFunction_specification(self, ctx:vhdlParser.Function_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#function_specification.
    def exitFunction_specification(self, ctx:vhdlParser.Function_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#subprogram_header.
    def enterSubprogram_header(self, ctx:vhdlParser.Subprogram_headerContext):
        pass

    # Exit a parse tree produced by vhdlParser#subprogram_header.
    def exitSubprogram_header(self, ctx:vhdlParser.Subprogram_headerContext):
        pass


    # Enter a parse tree produced by vhdlParser#designator.
    def enterDesignator(self, ctx:vhdlParser.DesignatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#designator.
    def exitDesignator(self, ctx:vhdlParser.DesignatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#operator_symbol.
    def enterOperator_symbol(self, ctx:vhdlParser.Operator_symbolContext):
        pass

    # Exit a parse tree produced by vhdlParser#operator_symbol.
    def exitOperator_symbol(self, ctx:vhdlParser.Operator_symbolContext):
        pass


    # Enter a parse tree produced by vhdlParser#formal_parameter_list.
    def enterFormal_parameter_list(self, ctx:vhdlParser.Formal_parameter_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#formal_parameter_list.
    def exitFormal_parameter_list(self, ctx:vhdlParser.Formal_parameter_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#subprogram_body.
    def enterSubprogram_body(self, ctx:vhdlParser.Subprogram_bodyContext):
        pass

    # Exit a parse tree produced by vhdlParser#subprogram_body.
    def exitSubprogram_body(self, ctx:vhdlParser.Subprogram_bodyContext):
        pass


    # Enter a parse tree produced by vhdlParser#subprogram_kind.
    def enterSubprogram_kind(self, ctx:vhdlParser.Subprogram_kindContext):
        pass

    # Exit a parse tree produced by vhdlParser#subprogram_kind.
    def exitSubprogram_kind(self, ctx:vhdlParser.Subprogram_kindContext):
        pass


    # Enter a parse tree produced by vhdlParser#subprogram_instantiation_declaration.
    def enterSubprogram_instantiation_declaration(self, ctx:vhdlParser.Subprogram_instantiation_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#subprogram_instantiation_declaration.
    def exitSubprogram_instantiation_declaration(self, ctx:vhdlParser.Subprogram_instantiation_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#signature.
    def enterSignature(self, ctx:vhdlParser.SignatureContext):
        pass

    # Exit a parse tree produced by vhdlParser#signature.
    def exitSignature(self, ctx:vhdlParser.SignatureContext):
        pass


    # Enter a parse tree produced by vhdlParser#package_declaration.
    def enterPackage_declaration(self, ctx:vhdlParser.Package_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#package_declaration.
    def exitPackage_declaration(self, ctx:vhdlParser.Package_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#package_declarative_item.
    def enterPackage_declarative_item(self, ctx:vhdlParser.Package_declarative_itemContext):
        pass

    # Exit a parse tree produced by vhdlParser#package_declarative_item.
    def exitPackage_declarative_item(self, ctx:vhdlParser.Package_declarative_itemContext):
        pass


    # Enter a parse tree produced by vhdlParser#package_body.
    def enterPackage_body(self, ctx:vhdlParser.Package_bodyContext):
        pass

    # Exit a parse tree produced by vhdlParser#package_body.
    def exitPackage_body(self, ctx:vhdlParser.Package_bodyContext):
        pass


    # Enter a parse tree produced by vhdlParser#package_instantiation_declaration.
    def enterPackage_instantiation_declaration(self, ctx:vhdlParser.Package_instantiation_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#package_instantiation_declaration.
    def exitPackage_instantiation_declaration(self, ctx:vhdlParser.Package_instantiation_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#scalar_type_definition.
    def enterScalar_type_definition(self, ctx:vhdlParser.Scalar_type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#scalar_type_definition.
    def exitScalar_type_definition(self, ctx:vhdlParser.Scalar_type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#range_constraint.
    def enterRange_constraint(self, ctx:vhdlParser.Range_constraintContext):
        pass

    # Exit a parse tree produced by vhdlParser#range_constraint.
    def exitRange_constraint(self, ctx:vhdlParser.Range_constraintContext):
        pass


    # Enter a parse tree produced by vhdlParser#range_.
    def enterRange_(self, ctx:vhdlParser.Range_Context):
        pass

    # Exit a parse tree produced by vhdlParser#range_.
    def exitRange_(self, ctx:vhdlParser.Range_Context):
        pass


    # Enter a parse tree produced by vhdlParser#direction.
    def enterDirection(self, ctx:vhdlParser.DirectionContext):
        pass

    # Exit a parse tree produced by vhdlParser#direction.
    def exitDirection(self, ctx:vhdlParser.DirectionContext):
        pass


    # Enter a parse tree produced by vhdlParser#enumeration_type_definition.
    def enterEnumeration_type_definition(self, ctx:vhdlParser.Enumeration_type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#enumeration_type_definition.
    def exitEnumeration_type_definition(self, ctx:vhdlParser.Enumeration_type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#enumeration_literal.
    def enterEnumeration_literal(self, ctx:vhdlParser.Enumeration_literalContext):
        pass

    # Exit a parse tree produced by vhdlParser#enumeration_literal.
    def exitEnumeration_literal(self, ctx:vhdlParser.Enumeration_literalContext):
        pass


    # Enter a parse tree produced by vhdlParser#integer_type_definition.
    def enterInteger_type_definition(self, ctx:vhdlParser.Integer_type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#integer_type_definition.
    def exitInteger_type_definition(self, ctx:vhdlParser.Integer_type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#physical_type_definition.
    def enterPhysical_type_definition(self, ctx:vhdlParser.Physical_type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#physical_type_definition.
    def exitPhysical_type_definition(self, ctx:vhdlParser.Physical_type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#primary_unit_declaration.
    def enterPrimary_unit_declaration(self, ctx:vhdlParser.Primary_unit_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#primary_unit_declaration.
    def exitPrimary_unit_declaration(self, ctx:vhdlParser.Primary_unit_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#secondary_unit_declaration.
    def enterSecondary_unit_declaration(self, ctx:vhdlParser.Secondary_unit_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#secondary_unit_declaration.
    def exitSecondary_unit_declaration(self, ctx:vhdlParser.Secondary_unit_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#floating_type_definition.
    def enterFloating_type_definition(self, ctx:vhdlParser.Floating_type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#floating_type_definition.
    def exitFloating_type_definition(self, ctx:vhdlParser.Floating_type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#composite_type_definition.
    def enterComposite_type_definition(self, ctx:vhdlParser.Composite_type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#composite_type_definition.
    def exitComposite_type_definition(self, ctx:vhdlParser.Composite_type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#array_type_definition.
    def enterArray_type_definition(self, ctx:vhdlParser.Array_type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#array_type_definition.
    def exitArray_type_definition(self, ctx:vhdlParser.Array_type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#unbounded_array_definition.
    def enterUnbounded_array_definition(self, ctx:vhdlParser.Unbounded_array_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#unbounded_array_definition.
    def exitUnbounded_array_definition(self, ctx:vhdlParser.Unbounded_array_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#constrained_array_definition.
    def enterConstrained_array_definition(self, ctx:vhdlParser.Constrained_array_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#constrained_array_definition.
    def exitConstrained_array_definition(self, ctx:vhdlParser.Constrained_array_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#index_subtype_definition.
    def enterIndex_subtype_definition(self, ctx:vhdlParser.Index_subtype_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#index_subtype_definition.
    def exitIndex_subtype_definition(self, ctx:vhdlParser.Index_subtype_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#array_constraint.
    def enterArray_constraint(self, ctx:vhdlParser.Array_constraintContext):
        pass

    # Exit a parse tree produced by vhdlParser#array_constraint.
    def exitArray_constraint(self, ctx:vhdlParser.Array_constraintContext):
        pass


    # Enter a parse tree produced by vhdlParser#array_element_constraint.
    def enterArray_element_constraint(self, ctx:vhdlParser.Array_element_constraintContext):
        pass

    # Exit a parse tree produced by vhdlParser#array_element_constraint.
    def exitArray_element_constraint(self, ctx:vhdlParser.Array_element_constraintContext):
        pass


    # Enter a parse tree produced by vhdlParser#index_constraint.
    def enterIndex_constraint(self, ctx:vhdlParser.Index_constraintContext):
        pass

    # Exit a parse tree produced by vhdlParser#index_constraint.
    def exitIndex_constraint(self, ctx:vhdlParser.Index_constraintContext):
        pass


    # Enter a parse tree produced by vhdlParser#discrete_range.
    def enterDiscrete_range(self, ctx:vhdlParser.Discrete_rangeContext):
        pass

    # Exit a parse tree produced by vhdlParser#discrete_range.
    def exitDiscrete_range(self, ctx:vhdlParser.Discrete_rangeContext):
        pass


    # Enter a parse tree produced by vhdlParser#record_type_definition.
    def enterRecord_type_definition(self, ctx:vhdlParser.Record_type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#record_type_definition.
    def exitRecord_type_definition(self, ctx:vhdlParser.Record_type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#element_declaration.
    def enterElement_declaration(self, ctx:vhdlParser.Element_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#element_declaration.
    def exitElement_declaration(self, ctx:vhdlParser.Element_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#identifier_list.
    def enterIdentifier_list(self, ctx:vhdlParser.Identifier_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#identifier_list.
    def exitIdentifier_list(self, ctx:vhdlParser.Identifier_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#element_subtype_definition.
    def enterElement_subtype_definition(self, ctx:vhdlParser.Element_subtype_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#element_subtype_definition.
    def exitElement_subtype_definition(self, ctx:vhdlParser.Element_subtype_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#record_constraint.
    def enterRecord_constraint(self, ctx:vhdlParser.Record_constraintContext):
        pass

    # Exit a parse tree produced by vhdlParser#record_constraint.
    def exitRecord_constraint(self, ctx:vhdlParser.Record_constraintContext):
        pass


    # Enter a parse tree produced by vhdlParser#record_element_constraint.
    def enterRecord_element_constraint(self, ctx:vhdlParser.Record_element_constraintContext):
        pass

    # Exit a parse tree produced by vhdlParser#record_element_constraint.
    def exitRecord_element_constraint(self, ctx:vhdlParser.Record_element_constraintContext):
        pass


    # Enter a parse tree produced by vhdlParser#access_type_definition.
    def enterAccess_type_definition(self, ctx:vhdlParser.Access_type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#access_type_definition.
    def exitAccess_type_definition(self, ctx:vhdlParser.Access_type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#incomplete_type_declaration.
    def enterIncomplete_type_declaration(self, ctx:vhdlParser.Incomplete_type_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#incomplete_type_declaration.
    def exitIncomplete_type_declaration(self, ctx:vhdlParser.Incomplete_type_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#file_type_definition.
    def enterFile_type_definition(self, ctx:vhdlParser.File_type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#file_type_definition.
    def exitFile_type_definition(self, ctx:vhdlParser.File_type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#protected_type_definition.
    def enterProtected_type_definition(self, ctx:vhdlParser.Protected_type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#protected_type_definition.
    def exitProtected_type_definition(self, ctx:vhdlParser.Protected_type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#protected_type_declaration.
    def enterProtected_type_declaration(self, ctx:vhdlParser.Protected_type_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#protected_type_declaration.
    def exitProtected_type_declaration(self, ctx:vhdlParser.Protected_type_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#protected_type_declarative_item.
    def enterProtected_type_declarative_item(self, ctx:vhdlParser.Protected_type_declarative_itemContext):
        pass

    # Exit a parse tree produced by vhdlParser#protected_type_declarative_item.
    def exitProtected_type_declarative_item(self, ctx:vhdlParser.Protected_type_declarative_itemContext):
        pass


    # Enter a parse tree produced by vhdlParser#protected_type_body.
    def enterProtected_type_body(self, ctx:vhdlParser.Protected_type_bodyContext):
        pass

    # Exit a parse tree produced by vhdlParser#protected_type_body.
    def exitProtected_type_body(self, ctx:vhdlParser.Protected_type_bodyContext):
        pass


    # Enter a parse tree produced by vhdlParser#type_declaration.
    def enterType_declaration(self, ctx:vhdlParser.Type_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#type_declaration.
    def exitType_declaration(self, ctx:vhdlParser.Type_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#full_type_declaration.
    def enterFull_type_declaration(self, ctx:vhdlParser.Full_type_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#full_type_declaration.
    def exitFull_type_declaration(self, ctx:vhdlParser.Full_type_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#type_definition.
    def enterType_definition(self, ctx:vhdlParser.Type_definitionContext):
        pass

    # Exit a parse tree produced by vhdlParser#type_definition.
    def exitType_definition(self, ctx:vhdlParser.Type_definitionContext):
        pass


    # Enter a parse tree produced by vhdlParser#subtype_declaration.
    def enterSubtype_declaration(self, ctx:vhdlParser.Subtype_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#subtype_declaration.
    def exitSubtype_declaration(self, ctx:vhdlParser.Subtype_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#subtype_indication.
    def enterSubtype_indication(self, ctx:vhdlParser.Subtype_indicationContext):
        pass

    # Exit a parse tree produced by vhdlParser#subtype_indication.
    def exitSubtype_indication(self, ctx:vhdlParser.Subtype_indicationContext):
        pass


    # Enter a parse tree produced by vhdlParser#resolution_indication.
    def enterResolution_indication(self, ctx:vhdlParser.Resolution_indicationContext):
        pass

    # Exit a parse tree produced by vhdlParser#resolution_indication.
    def exitResolution_indication(self, ctx:vhdlParser.Resolution_indicationContext):
        pass


    # Enter a parse tree produced by vhdlParser#element_resolution.
    def enterElement_resolution(self, ctx:vhdlParser.Element_resolutionContext):
        pass

    # Exit a parse tree produced by vhdlParser#element_resolution.
    def exitElement_resolution(self, ctx:vhdlParser.Element_resolutionContext):
        pass


    # Enter a parse tree produced by vhdlParser#array_element_resolution.
    def enterArray_element_resolution(self, ctx:vhdlParser.Array_element_resolutionContext):
        pass

    # Exit a parse tree produced by vhdlParser#array_element_resolution.
    def exitArray_element_resolution(self, ctx:vhdlParser.Array_element_resolutionContext):
        pass


    # Enter a parse tree produced by vhdlParser#record_resolution.
    def enterRecord_resolution(self, ctx:vhdlParser.Record_resolutionContext):
        pass

    # Exit a parse tree produced by vhdlParser#record_resolution.
    def exitRecord_resolution(self, ctx:vhdlParser.Record_resolutionContext):
        pass


    # Enter a parse tree produced by vhdlParser#record_element_resolution.
    def enterRecord_element_resolution(self, ctx:vhdlParser.Record_element_resolutionContext):
        pass

    # Exit a parse tree produced by vhdlParser#record_element_resolution.
    def exitRecord_element_resolution(self, ctx:vhdlParser.Record_element_resolutionContext):
        pass


    # Enter a parse tree produced by vhdlParser#type_mark.
    def enterType_mark(self, ctx:vhdlParser.Type_markContext):
        pass

    # Exit a parse tree produced by vhdlParser#type_mark.
    def exitType_mark(self, ctx:vhdlParser.Type_markContext):
        pass


    # Enter a parse tree produced by vhdlParser#constraint.
    def enterConstraint(self, ctx:vhdlParser.ConstraintContext):
        pass

    # Exit a parse tree produced by vhdlParser#constraint.
    def exitConstraint(self, ctx:vhdlParser.ConstraintContext):
        pass


    # Enter a parse tree produced by vhdlParser#element_constraint.
    def enterElement_constraint(self, ctx:vhdlParser.Element_constraintContext):
        pass

    # Exit a parse tree produced by vhdlParser#element_constraint.
    def exitElement_constraint(self, ctx:vhdlParser.Element_constraintContext):
        pass


    # Enter a parse tree produced by vhdlParser#object_declaration.
    def enterObject_declaration(self, ctx:vhdlParser.Object_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#object_declaration.
    def exitObject_declaration(self, ctx:vhdlParser.Object_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#constant_declaration.
    def enterConstant_declaration(self, ctx:vhdlParser.Constant_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#constant_declaration.
    def exitConstant_declaration(self, ctx:vhdlParser.Constant_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#signal_declaration.
    def enterSignal_declaration(self, ctx:vhdlParser.Signal_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#signal_declaration.
    def exitSignal_declaration(self, ctx:vhdlParser.Signal_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#signal_kind.
    def enterSignal_kind(self, ctx:vhdlParser.Signal_kindContext):
        pass

    # Exit a parse tree produced by vhdlParser#signal_kind.
    def exitSignal_kind(self, ctx:vhdlParser.Signal_kindContext):
        pass


    # Enter a parse tree produced by vhdlParser#variable_declaration.
    def enterVariable_declaration(self, ctx:vhdlParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#variable_declaration.
    def exitVariable_declaration(self, ctx:vhdlParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#file_declaration.
    def enterFile_declaration(self, ctx:vhdlParser.File_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#file_declaration.
    def exitFile_declaration(self, ctx:vhdlParser.File_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#file_open_information.
    def enterFile_open_information(self, ctx:vhdlParser.File_open_informationContext):
        pass

    # Exit a parse tree produced by vhdlParser#file_open_information.
    def exitFile_open_information(self, ctx:vhdlParser.File_open_informationContext):
        pass


    # Enter a parse tree produced by vhdlParser#file_logical_name.
    def enterFile_logical_name(self, ctx:vhdlParser.File_logical_nameContext):
        pass

    # Exit a parse tree produced by vhdlParser#file_logical_name.
    def exitFile_logical_name(self, ctx:vhdlParser.File_logical_nameContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_declaration.
    def enterInterface_declaration(self, ctx:vhdlParser.Interface_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_declaration.
    def exitInterface_declaration(self, ctx:vhdlParser.Interface_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_object_declaration.
    def enterInterface_object_declaration(self, ctx:vhdlParser.Interface_object_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_object_declaration.
    def exitInterface_object_declaration(self, ctx:vhdlParser.Interface_object_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_constant_declaration.
    def enterInterface_constant_declaration(self, ctx:vhdlParser.Interface_constant_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_constant_declaration.
    def exitInterface_constant_declaration(self, ctx:vhdlParser.Interface_constant_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_signal_declaration.
    def enterInterface_signal_declaration(self, ctx:vhdlParser.Interface_signal_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_signal_declaration.
    def exitInterface_signal_declaration(self, ctx:vhdlParser.Interface_signal_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_variable_declaration.
    def enterInterface_variable_declaration(self, ctx:vhdlParser.Interface_variable_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_variable_declaration.
    def exitInterface_variable_declaration(self, ctx:vhdlParser.Interface_variable_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_file_declaration.
    def enterInterface_file_declaration(self, ctx:vhdlParser.Interface_file_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_file_declaration.
    def exitInterface_file_declaration(self, ctx:vhdlParser.Interface_file_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#signal_mode.
    def enterSignal_mode(self, ctx:vhdlParser.Signal_modeContext):
        pass

    # Exit a parse tree produced by vhdlParser#signal_mode.
    def exitSignal_mode(self, ctx:vhdlParser.Signal_modeContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_type_declaration.
    def enterInterface_type_declaration(self, ctx:vhdlParser.Interface_type_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_type_declaration.
    def exitInterface_type_declaration(self, ctx:vhdlParser.Interface_type_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_incomplete_type_declaration.
    def enterInterface_incomplete_type_declaration(self, ctx:vhdlParser.Interface_incomplete_type_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_incomplete_type_declaration.
    def exitInterface_incomplete_type_declaration(self, ctx:vhdlParser.Interface_incomplete_type_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_subprogram_declaration.
    def enterInterface_subprogram_declaration(self, ctx:vhdlParser.Interface_subprogram_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_subprogram_declaration.
    def exitInterface_subprogram_declaration(self, ctx:vhdlParser.Interface_subprogram_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_subprogram_specification.
    def enterInterface_subprogram_specification(self, ctx:vhdlParser.Interface_subprogram_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_subprogram_specification.
    def exitInterface_subprogram_specification(self, ctx:vhdlParser.Interface_subprogram_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_procedure_specification.
    def enterInterface_procedure_specification(self, ctx:vhdlParser.Interface_procedure_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_procedure_specification.
    def exitInterface_procedure_specification(self, ctx:vhdlParser.Interface_procedure_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_function_specification.
    def enterInterface_function_specification(self, ctx:vhdlParser.Interface_function_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_function_specification.
    def exitInterface_function_specification(self, ctx:vhdlParser.Interface_function_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_subprogram_default.
    def enterInterface_subprogram_default(self, ctx:vhdlParser.Interface_subprogram_defaultContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_subprogram_default.
    def exitInterface_subprogram_default(self, ctx:vhdlParser.Interface_subprogram_defaultContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_package_declaration.
    def enterInterface_package_declaration(self, ctx:vhdlParser.Interface_package_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_package_declaration.
    def exitInterface_package_declaration(self, ctx:vhdlParser.Interface_package_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_package_generic_map_aspect.
    def enterInterface_package_generic_map_aspect(self, ctx:vhdlParser.Interface_package_generic_map_aspectContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_package_generic_map_aspect.
    def exitInterface_package_generic_map_aspect(self, ctx:vhdlParser.Interface_package_generic_map_aspectContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_list.
    def enterInterface_list(self, ctx:vhdlParser.Interface_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_list.
    def exitInterface_list(self, ctx:vhdlParser.Interface_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#interface_element.
    def enterInterface_element(self, ctx:vhdlParser.Interface_elementContext):
        pass

    # Exit a parse tree produced by vhdlParser#interface_element.
    def exitInterface_element(self, ctx:vhdlParser.Interface_elementContext):
        pass


    # Enter a parse tree produced by vhdlParser#generic_clause.
    def enterGeneric_clause(self, ctx:vhdlParser.Generic_clauseContext):
        pass

    # Exit a parse tree produced by vhdlParser#generic_clause.
    def exitGeneric_clause(self, ctx:vhdlParser.Generic_clauseContext):
        pass


    # Enter a parse tree produced by vhdlParser#generic_list.
    def enterGeneric_list(self, ctx:vhdlParser.Generic_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#generic_list.
    def exitGeneric_list(self, ctx:vhdlParser.Generic_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#port_clause.
    def enterPort_clause(self, ctx:vhdlParser.Port_clauseContext):
        pass

    # Exit a parse tree produced by vhdlParser#port_clause.
    def exitPort_clause(self, ctx:vhdlParser.Port_clauseContext):
        pass


    # Enter a parse tree produced by vhdlParser#port_list.
    def enterPort_list(self, ctx:vhdlParser.Port_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#port_list.
    def exitPort_list(self, ctx:vhdlParser.Port_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#association_list.
    def enterAssociation_list(self, ctx:vhdlParser.Association_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#association_list.
    def exitAssociation_list(self, ctx:vhdlParser.Association_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#association_element.
    def enterAssociation_element(self, ctx:vhdlParser.Association_elementContext):
        pass

    # Exit a parse tree produced by vhdlParser#association_element.
    def exitAssociation_element(self, ctx:vhdlParser.Association_elementContext):
        pass


    # Enter a parse tree produced by vhdlParser#formal_part.
    def enterFormal_part(self, ctx:vhdlParser.Formal_partContext):
        pass

    # Exit a parse tree produced by vhdlParser#formal_part.
    def exitFormal_part(self, ctx:vhdlParser.Formal_partContext):
        pass


    # Enter a parse tree produced by vhdlParser#actual_part.
    def enterActual_part(self, ctx:vhdlParser.Actual_partContext):
        pass

    # Exit a parse tree produced by vhdlParser#actual_part.
    def exitActual_part(self, ctx:vhdlParser.Actual_partContext):
        pass


    # Enter a parse tree produced by vhdlParser#actual_designator.
    def enterActual_designator(self, ctx:vhdlParser.Actual_designatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#actual_designator.
    def exitActual_designator(self, ctx:vhdlParser.Actual_designatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#generic_map_aspect.
    def enterGeneric_map_aspect(self, ctx:vhdlParser.Generic_map_aspectContext):
        pass

    # Exit a parse tree produced by vhdlParser#generic_map_aspect.
    def exitGeneric_map_aspect(self, ctx:vhdlParser.Generic_map_aspectContext):
        pass


    # Enter a parse tree produced by vhdlParser#port_map_aspect.
    def enterPort_map_aspect(self, ctx:vhdlParser.Port_map_aspectContext):
        pass

    # Exit a parse tree produced by vhdlParser#port_map_aspect.
    def exitPort_map_aspect(self, ctx:vhdlParser.Port_map_aspectContext):
        pass


    # Enter a parse tree produced by vhdlParser#alias_declaration.
    def enterAlias_declaration(self, ctx:vhdlParser.Alias_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#alias_declaration.
    def exitAlias_declaration(self, ctx:vhdlParser.Alias_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#alias_designator.
    def enterAlias_designator(self, ctx:vhdlParser.Alias_designatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#alias_designator.
    def exitAlias_designator(self, ctx:vhdlParser.Alias_designatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#attribute_declaration.
    def enterAttribute_declaration(self, ctx:vhdlParser.Attribute_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#attribute_declaration.
    def exitAttribute_declaration(self, ctx:vhdlParser.Attribute_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#component_declaration.
    def enterComponent_declaration(self, ctx:vhdlParser.Component_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#component_declaration.
    def exitComponent_declaration(self, ctx:vhdlParser.Component_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#group_template_declaration.
    def enterGroup_template_declaration(self, ctx:vhdlParser.Group_template_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#group_template_declaration.
    def exitGroup_template_declaration(self, ctx:vhdlParser.Group_template_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#entity_class_entry_list.
    def enterEntity_class_entry_list(self, ctx:vhdlParser.Entity_class_entry_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#entity_class_entry_list.
    def exitEntity_class_entry_list(self, ctx:vhdlParser.Entity_class_entry_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#entity_class_entry.
    def enterEntity_class_entry(self, ctx:vhdlParser.Entity_class_entryContext):
        pass

    # Exit a parse tree produced by vhdlParser#entity_class_entry.
    def exitEntity_class_entry(self, ctx:vhdlParser.Entity_class_entryContext):
        pass


    # Enter a parse tree produced by vhdlParser#group_declaration.
    def enterGroup_declaration(self, ctx:vhdlParser.Group_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#group_declaration.
    def exitGroup_declaration(self, ctx:vhdlParser.Group_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#group_constituent_list.
    def enterGroup_constituent_list(self, ctx:vhdlParser.Group_constituent_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#group_constituent_list.
    def exitGroup_constituent_list(self, ctx:vhdlParser.Group_constituent_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#group_constituent.
    def enterGroup_constituent(self, ctx:vhdlParser.Group_constituentContext):
        pass

    # Exit a parse tree produced by vhdlParser#group_constituent.
    def exitGroup_constituent(self, ctx:vhdlParser.Group_constituentContext):
        pass


    # Enter a parse tree produced by vhdlParser#attribute_specification.
    def enterAttribute_specification(self, ctx:vhdlParser.Attribute_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#attribute_specification.
    def exitAttribute_specification(self, ctx:vhdlParser.Attribute_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#entity_specification.
    def enterEntity_specification(self, ctx:vhdlParser.Entity_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#entity_specification.
    def exitEntity_specification(self, ctx:vhdlParser.Entity_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#entity_class.
    def enterEntity_class(self, ctx:vhdlParser.Entity_classContext):
        pass

    # Exit a parse tree produced by vhdlParser#entity_class.
    def exitEntity_class(self, ctx:vhdlParser.Entity_classContext):
        pass


    # Enter a parse tree produced by vhdlParser#entity_name_list.
    def enterEntity_name_list(self, ctx:vhdlParser.Entity_name_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#entity_name_list.
    def exitEntity_name_list(self, ctx:vhdlParser.Entity_name_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#entity_designator.
    def enterEntity_designator(self, ctx:vhdlParser.Entity_designatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#entity_designator.
    def exitEntity_designator(self, ctx:vhdlParser.Entity_designatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#entity_tag.
    def enterEntity_tag(self, ctx:vhdlParser.Entity_tagContext):
        pass

    # Exit a parse tree produced by vhdlParser#entity_tag.
    def exitEntity_tag(self, ctx:vhdlParser.Entity_tagContext):
        pass


    # Enter a parse tree produced by vhdlParser#configuration_specification.
    def enterConfiguration_specification(self, ctx:vhdlParser.Configuration_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#configuration_specification.
    def exitConfiguration_specification(self, ctx:vhdlParser.Configuration_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#simple_configuration_specification.
    def enterSimple_configuration_specification(self, ctx:vhdlParser.Simple_configuration_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#simple_configuration_specification.
    def exitSimple_configuration_specification(self, ctx:vhdlParser.Simple_configuration_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#compound_configuration_specification.
    def enterCompound_configuration_specification(self, ctx:vhdlParser.Compound_configuration_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#compound_configuration_specification.
    def exitCompound_configuration_specification(self, ctx:vhdlParser.Compound_configuration_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#component_specification.
    def enterComponent_specification(self, ctx:vhdlParser.Component_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#component_specification.
    def exitComponent_specification(self, ctx:vhdlParser.Component_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#instantiation_list.
    def enterInstantiation_list(self, ctx:vhdlParser.Instantiation_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#instantiation_list.
    def exitInstantiation_list(self, ctx:vhdlParser.Instantiation_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#binding_indication.
    def enterBinding_indication(self, ctx:vhdlParser.Binding_indicationContext):
        pass

    # Exit a parse tree produced by vhdlParser#binding_indication.
    def exitBinding_indication(self, ctx:vhdlParser.Binding_indicationContext):
        pass


    # Enter a parse tree produced by vhdlParser#entity_aspect.
    def enterEntity_aspect(self, ctx:vhdlParser.Entity_aspectContext):
        pass

    # Exit a parse tree produced by vhdlParser#entity_aspect.
    def exitEntity_aspect(self, ctx:vhdlParser.Entity_aspectContext):
        pass


    # Enter a parse tree produced by vhdlParser#verification_unit_binding_indication.
    def enterVerification_unit_binding_indication(self, ctx:vhdlParser.Verification_unit_binding_indicationContext):
        pass

    # Exit a parse tree produced by vhdlParser#verification_unit_binding_indication.
    def exitVerification_unit_binding_indication(self, ctx:vhdlParser.Verification_unit_binding_indicationContext):
        pass


    # Enter a parse tree produced by vhdlParser#verification_unit_list.
    def enterVerification_unit_list(self, ctx:vhdlParser.Verification_unit_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#verification_unit_list.
    def exitVerification_unit_list(self, ctx:vhdlParser.Verification_unit_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#disconnection_specification.
    def enterDisconnection_specification(self, ctx:vhdlParser.Disconnection_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#disconnection_specification.
    def exitDisconnection_specification(self, ctx:vhdlParser.Disconnection_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#guarded_signal_specification.
    def enterGuarded_signal_specification(self, ctx:vhdlParser.Guarded_signal_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#guarded_signal_specification.
    def exitGuarded_signal_specification(self, ctx:vhdlParser.Guarded_signal_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#signal_list.
    def enterSignal_list(self, ctx:vhdlParser.Signal_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#signal_list.
    def exitSignal_list(self, ctx:vhdlParser.Signal_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#attribute_designator.
    def enterAttribute_designator(self, ctx:vhdlParser.Attribute_designatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#attribute_designator.
    def exitAttribute_designator(self, ctx:vhdlParser.Attribute_designatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#external_name.
    def enterExternal_name(self, ctx:vhdlParser.External_nameContext):
        pass

    # Exit a parse tree produced by vhdlParser#external_name.
    def exitExternal_name(self, ctx:vhdlParser.External_nameContext):
        pass


    # Enter a parse tree produced by vhdlParser#external_pathname.
    def enterExternal_pathname(self, ctx:vhdlParser.External_pathnameContext):
        pass

    # Exit a parse tree produced by vhdlParser#external_pathname.
    def exitExternal_pathname(self, ctx:vhdlParser.External_pathnameContext):
        pass


    # Enter a parse tree produced by vhdlParser#package_pathname.
    def enterPackage_pathname(self, ctx:vhdlParser.Package_pathnameContext):
        pass

    # Exit a parse tree produced by vhdlParser#package_pathname.
    def exitPackage_pathname(self, ctx:vhdlParser.Package_pathnameContext):
        pass


    # Enter a parse tree produced by vhdlParser#absolute_pathname.
    def enterAbsolute_pathname(self, ctx:vhdlParser.Absolute_pathnameContext):
        pass

    # Exit a parse tree produced by vhdlParser#absolute_pathname.
    def exitAbsolute_pathname(self, ctx:vhdlParser.Absolute_pathnameContext):
        pass


    # Enter a parse tree produced by vhdlParser#relative_pathname.
    def enterRelative_pathname(self, ctx:vhdlParser.Relative_pathnameContext):
        pass

    # Exit a parse tree produced by vhdlParser#relative_pathname.
    def exitRelative_pathname(self, ctx:vhdlParser.Relative_pathnameContext):
        pass


    # Enter a parse tree produced by vhdlParser#partial_pathname.
    def enterPartial_pathname(self, ctx:vhdlParser.Partial_pathnameContext):
        pass

    # Exit a parse tree produced by vhdlParser#partial_pathname.
    def exitPartial_pathname(self, ctx:vhdlParser.Partial_pathnameContext):
        pass


    # Enter a parse tree produced by vhdlParser#pathname_element.
    def enterPathname_element(self, ctx:vhdlParser.Pathname_elementContext):
        pass

    # Exit a parse tree produced by vhdlParser#pathname_element.
    def exitPathname_element(self, ctx:vhdlParser.Pathname_elementContext):
        pass


    # Enter a parse tree produced by vhdlParser#expression.
    def enterExpression(self, ctx:vhdlParser.ExpressionContext):
        pass

    # Exit a parse tree produced by vhdlParser#expression.
    def exitExpression(self, ctx:vhdlParser.ExpressionContext):
        pass


    # Enter a parse tree produced by vhdlParser#simple_expression.
    def enterSimple_expression(self, ctx:vhdlParser.Simple_expressionContext):
        pass

    # Exit a parse tree produced by vhdlParser#simple_expression.
    def exitSimple_expression(self, ctx:vhdlParser.Simple_expressionContext):
        pass


    # Enter a parse tree produced by vhdlParser#primary.
    def enterPrimary(self, ctx:vhdlParser.PrimaryContext):
        pass

    # Exit a parse tree produced by vhdlParser#primary.
    def exitPrimary(self, ctx:vhdlParser.PrimaryContext):
        pass


    # Enter a parse tree produced by vhdlParser#logical_operator.
    def enterLogical_operator(self, ctx:vhdlParser.Logical_operatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#logical_operator.
    def exitLogical_operator(self, ctx:vhdlParser.Logical_operatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#relational_operator.
    def enterRelational_operator(self, ctx:vhdlParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#relational_operator.
    def exitRelational_operator(self, ctx:vhdlParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#shift_operator.
    def enterShift_operator(self, ctx:vhdlParser.Shift_operatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#shift_operator.
    def exitShift_operator(self, ctx:vhdlParser.Shift_operatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#adding_operator.
    def enterAdding_operator(self, ctx:vhdlParser.Adding_operatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#adding_operator.
    def exitAdding_operator(self, ctx:vhdlParser.Adding_operatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#sign.
    def enterSign(self, ctx:vhdlParser.SignContext):
        pass

    # Exit a parse tree produced by vhdlParser#sign.
    def exitSign(self, ctx:vhdlParser.SignContext):
        pass


    # Enter a parse tree produced by vhdlParser#multiplying_operator.
    def enterMultiplying_operator(self, ctx:vhdlParser.Multiplying_operatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#multiplying_operator.
    def exitMultiplying_operator(self, ctx:vhdlParser.Multiplying_operatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#miscellaneous_operator.
    def enterMiscellaneous_operator(self, ctx:vhdlParser.Miscellaneous_operatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#miscellaneous_operator.
    def exitMiscellaneous_operator(self, ctx:vhdlParser.Miscellaneous_operatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#numeric_literal.
    def enterNumeric_literal(self, ctx:vhdlParser.Numeric_literalContext):
        pass

    # Exit a parse tree produced by vhdlParser#numeric_literal.
    def exitNumeric_literal(self, ctx:vhdlParser.Numeric_literalContext):
        pass


    # Enter a parse tree produced by vhdlParser#physical_literal.
    def enterPhysical_literal(self, ctx:vhdlParser.Physical_literalContext):
        pass

    # Exit a parse tree produced by vhdlParser#physical_literal.
    def exitPhysical_literal(self, ctx:vhdlParser.Physical_literalContext):
        pass


    # Enter a parse tree produced by vhdlParser#aggregate.
    def enterAggregate(self, ctx:vhdlParser.AggregateContext):
        pass

    # Exit a parse tree produced by vhdlParser#aggregate.
    def exitAggregate(self, ctx:vhdlParser.AggregateContext):
        pass


    # Enter a parse tree produced by vhdlParser#element_association.
    def enterElement_association(self, ctx:vhdlParser.Element_associationContext):
        pass

    # Exit a parse tree produced by vhdlParser#element_association.
    def exitElement_association(self, ctx:vhdlParser.Element_associationContext):
        pass


    # Enter a parse tree produced by vhdlParser#choices.
    def enterChoices(self, ctx:vhdlParser.ChoicesContext):
        pass

    # Exit a parse tree produced by vhdlParser#choices.
    def exitChoices(self, ctx:vhdlParser.ChoicesContext):
        pass


    # Enter a parse tree produced by vhdlParser#choice.
    def enterChoice(self, ctx:vhdlParser.ChoiceContext):
        pass

    # Exit a parse tree produced by vhdlParser#choice.
    def exitChoice(self, ctx:vhdlParser.ChoiceContext):
        pass


    # Enter a parse tree produced by vhdlParser#qualified_expression.
    def enterQualified_expression(self, ctx:vhdlParser.Qualified_expressionContext):
        pass

    # Exit a parse tree produced by vhdlParser#qualified_expression.
    def exitQualified_expression(self, ctx:vhdlParser.Qualified_expressionContext):
        pass


    # Enter a parse tree produced by vhdlParser#allocator.
    def enterAllocator(self, ctx:vhdlParser.AllocatorContext):
        pass

    # Exit a parse tree produced by vhdlParser#allocator.
    def exitAllocator(self, ctx:vhdlParser.AllocatorContext):
        pass


    # Enter a parse tree produced by vhdlParser#sequence_of_statements.
    def enterSequence_of_statements(self, ctx:vhdlParser.Sequence_of_statementsContext):
        pass

    # Exit a parse tree produced by vhdlParser#sequence_of_statements.
    def exitSequence_of_statements(self, ctx:vhdlParser.Sequence_of_statementsContext):
        pass


    # Enter a parse tree produced by vhdlParser#sequential_statement.
    def enterSequential_statement(self, ctx:vhdlParser.Sequential_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#sequential_statement.
    def exitSequential_statement(self, ctx:vhdlParser.Sequential_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#wait_statement.
    def enterWait_statement(self, ctx:vhdlParser.Wait_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#wait_statement.
    def exitWait_statement(self, ctx:vhdlParser.Wait_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#sensitivity_clause.
    def enterSensitivity_clause(self, ctx:vhdlParser.Sensitivity_clauseContext):
        pass

    # Exit a parse tree produced by vhdlParser#sensitivity_clause.
    def exitSensitivity_clause(self, ctx:vhdlParser.Sensitivity_clauseContext):
        pass


    # Enter a parse tree produced by vhdlParser#sensitivity_list.
    def enterSensitivity_list(self, ctx:vhdlParser.Sensitivity_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#sensitivity_list.
    def exitSensitivity_list(self, ctx:vhdlParser.Sensitivity_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#condition_clause.
    def enterCondition_clause(self, ctx:vhdlParser.Condition_clauseContext):
        pass

    # Exit a parse tree produced by vhdlParser#condition_clause.
    def exitCondition_clause(self, ctx:vhdlParser.Condition_clauseContext):
        pass


    # Enter a parse tree produced by vhdlParser#condition.
    def enterCondition(self, ctx:vhdlParser.ConditionContext):
        pass

    # Exit a parse tree produced by vhdlParser#condition.
    def exitCondition(self, ctx:vhdlParser.ConditionContext):
        pass


    # Enter a parse tree produced by vhdlParser#timeout_clause.
    def enterTimeout_clause(self, ctx:vhdlParser.Timeout_clauseContext):
        pass

    # Exit a parse tree produced by vhdlParser#timeout_clause.
    def exitTimeout_clause(self, ctx:vhdlParser.Timeout_clauseContext):
        pass


    # Enter a parse tree produced by vhdlParser#assertion_statement.
    def enterAssertion_statement(self, ctx:vhdlParser.Assertion_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#assertion_statement.
    def exitAssertion_statement(self, ctx:vhdlParser.Assertion_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#assertion.
    def enterAssertion(self, ctx:vhdlParser.AssertionContext):
        pass

    # Exit a parse tree produced by vhdlParser#assertion.
    def exitAssertion(self, ctx:vhdlParser.AssertionContext):
        pass


    # Enter a parse tree produced by vhdlParser#report_statement.
    def enterReport_statement(self, ctx:vhdlParser.Report_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#report_statement.
    def exitReport_statement(self, ctx:vhdlParser.Report_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#signal_assignment_statement.
    def enterSignal_assignment_statement(self, ctx:vhdlParser.Signal_assignment_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#signal_assignment_statement.
    def exitSignal_assignment_statement(self, ctx:vhdlParser.Signal_assignment_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#simple_signal_assignment.
    def enterSimple_signal_assignment(self, ctx:vhdlParser.Simple_signal_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#simple_signal_assignment.
    def exitSimple_signal_assignment(self, ctx:vhdlParser.Simple_signal_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#simple_waveform_assignment.
    def enterSimple_waveform_assignment(self, ctx:vhdlParser.Simple_waveform_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#simple_waveform_assignment.
    def exitSimple_waveform_assignment(self, ctx:vhdlParser.Simple_waveform_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#simple_force_assignment.
    def enterSimple_force_assignment(self, ctx:vhdlParser.Simple_force_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#simple_force_assignment.
    def exitSimple_force_assignment(self, ctx:vhdlParser.Simple_force_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#simple_release_assignment.
    def enterSimple_release_assignment(self, ctx:vhdlParser.Simple_release_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#simple_release_assignment.
    def exitSimple_release_assignment(self, ctx:vhdlParser.Simple_release_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#force_mode.
    def enterForce_mode(self, ctx:vhdlParser.Force_modeContext):
        pass

    # Exit a parse tree produced by vhdlParser#force_mode.
    def exitForce_mode(self, ctx:vhdlParser.Force_modeContext):
        pass


    # Enter a parse tree produced by vhdlParser#delay_mechanism.
    def enterDelay_mechanism(self, ctx:vhdlParser.Delay_mechanismContext):
        pass

    # Exit a parse tree produced by vhdlParser#delay_mechanism.
    def exitDelay_mechanism(self, ctx:vhdlParser.Delay_mechanismContext):
        pass


    # Enter a parse tree produced by vhdlParser#target.
    def enterTarget(self, ctx:vhdlParser.TargetContext):
        pass

    # Exit a parse tree produced by vhdlParser#target.
    def exitTarget(self, ctx:vhdlParser.TargetContext):
        pass


    # Enter a parse tree produced by vhdlParser#waveform.
    def enterWaveform(self, ctx:vhdlParser.WaveformContext):
        pass

    # Exit a parse tree produced by vhdlParser#waveform.
    def exitWaveform(self, ctx:vhdlParser.WaveformContext):
        pass


    # Enter a parse tree produced by vhdlParser#waveform_element.
    def enterWaveform_element(self, ctx:vhdlParser.Waveform_elementContext):
        pass

    # Exit a parse tree produced by vhdlParser#waveform_element.
    def exitWaveform_element(self, ctx:vhdlParser.Waveform_elementContext):
        pass


    # Enter a parse tree produced by vhdlParser#conditional_signal_assignment.
    def enterConditional_signal_assignment(self, ctx:vhdlParser.Conditional_signal_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#conditional_signal_assignment.
    def exitConditional_signal_assignment(self, ctx:vhdlParser.Conditional_signal_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#conditional_waveform_assignment.
    def enterConditional_waveform_assignment(self, ctx:vhdlParser.Conditional_waveform_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#conditional_waveform_assignment.
    def exitConditional_waveform_assignment(self, ctx:vhdlParser.Conditional_waveform_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#conditional_waveforms.
    def enterConditional_waveforms(self, ctx:vhdlParser.Conditional_waveformsContext):
        pass

    # Exit a parse tree produced by vhdlParser#conditional_waveforms.
    def exitConditional_waveforms(self, ctx:vhdlParser.Conditional_waveformsContext):
        pass


    # Enter a parse tree produced by vhdlParser#conditional_force_assignment.
    def enterConditional_force_assignment(self, ctx:vhdlParser.Conditional_force_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#conditional_force_assignment.
    def exitConditional_force_assignment(self, ctx:vhdlParser.Conditional_force_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#conditional_expressions.
    def enterConditional_expressions(self, ctx:vhdlParser.Conditional_expressionsContext):
        pass

    # Exit a parse tree produced by vhdlParser#conditional_expressions.
    def exitConditional_expressions(self, ctx:vhdlParser.Conditional_expressionsContext):
        pass


    # Enter a parse tree produced by vhdlParser#selected_signal_assignment.
    def enterSelected_signal_assignment(self, ctx:vhdlParser.Selected_signal_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#selected_signal_assignment.
    def exitSelected_signal_assignment(self, ctx:vhdlParser.Selected_signal_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#selected_waveform_assignment.
    def enterSelected_waveform_assignment(self, ctx:vhdlParser.Selected_waveform_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#selected_waveform_assignment.
    def exitSelected_waveform_assignment(self, ctx:vhdlParser.Selected_waveform_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#selected_waveforms.
    def enterSelected_waveforms(self, ctx:vhdlParser.Selected_waveformsContext):
        pass

    # Exit a parse tree produced by vhdlParser#selected_waveforms.
    def exitSelected_waveforms(self, ctx:vhdlParser.Selected_waveformsContext):
        pass


    # Enter a parse tree produced by vhdlParser#selected_force_assignment.
    def enterSelected_force_assignment(self, ctx:vhdlParser.Selected_force_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#selected_force_assignment.
    def exitSelected_force_assignment(self, ctx:vhdlParser.Selected_force_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#selected_expressions.
    def enterSelected_expressions(self, ctx:vhdlParser.Selected_expressionsContext):
        pass

    # Exit a parse tree produced by vhdlParser#selected_expressions.
    def exitSelected_expressions(self, ctx:vhdlParser.Selected_expressionsContext):
        pass


    # Enter a parse tree produced by vhdlParser#variable_assignment_statement.
    def enterVariable_assignment_statement(self, ctx:vhdlParser.Variable_assignment_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#variable_assignment_statement.
    def exitVariable_assignment_statement(self, ctx:vhdlParser.Variable_assignment_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#simple_variable_assignment.
    def enterSimple_variable_assignment(self, ctx:vhdlParser.Simple_variable_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#simple_variable_assignment.
    def exitSimple_variable_assignment(self, ctx:vhdlParser.Simple_variable_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#conditional_variable_assignment.
    def enterConditional_variable_assignment(self, ctx:vhdlParser.Conditional_variable_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#conditional_variable_assignment.
    def exitConditional_variable_assignment(self, ctx:vhdlParser.Conditional_variable_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#selected_variable_assignment.
    def enterSelected_variable_assignment(self, ctx:vhdlParser.Selected_variable_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#selected_variable_assignment.
    def exitSelected_variable_assignment(self, ctx:vhdlParser.Selected_variable_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#procedure_call_statement.
    def enterProcedure_call_statement(self, ctx:vhdlParser.Procedure_call_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#procedure_call_statement.
    def exitProcedure_call_statement(self, ctx:vhdlParser.Procedure_call_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#procedure_call.
    def enterProcedure_call(self, ctx:vhdlParser.Procedure_callContext):
        pass

    # Exit a parse tree produced by vhdlParser#procedure_call.
    def exitProcedure_call(self, ctx:vhdlParser.Procedure_callContext):
        pass


    # Enter a parse tree produced by vhdlParser#if_statement.
    def enterIf_statement(self, ctx:vhdlParser.If_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#if_statement.
    def exitIf_statement(self, ctx:vhdlParser.If_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#case_statement.
    def enterCase_statement(self, ctx:vhdlParser.Case_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#case_statement.
    def exitCase_statement(self, ctx:vhdlParser.Case_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#case_statement_alternative.
    def enterCase_statement_alternative(self, ctx:vhdlParser.Case_statement_alternativeContext):
        pass

    # Exit a parse tree produced by vhdlParser#case_statement_alternative.
    def exitCase_statement_alternative(self, ctx:vhdlParser.Case_statement_alternativeContext):
        pass


    # Enter a parse tree produced by vhdlParser#loop_statement.
    def enterLoop_statement(self, ctx:vhdlParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#loop_statement.
    def exitLoop_statement(self, ctx:vhdlParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#iteration_scheme.
    def enterIteration_scheme(self, ctx:vhdlParser.Iteration_schemeContext):
        pass

    # Exit a parse tree produced by vhdlParser#iteration_scheme.
    def exitIteration_scheme(self, ctx:vhdlParser.Iteration_schemeContext):
        pass


    # Enter a parse tree produced by vhdlParser#parameter_specification.
    def enterParameter_specification(self, ctx:vhdlParser.Parameter_specificationContext):
        pass

    # Exit a parse tree produced by vhdlParser#parameter_specification.
    def exitParameter_specification(self, ctx:vhdlParser.Parameter_specificationContext):
        pass


    # Enter a parse tree produced by vhdlParser#next_statement.
    def enterNext_statement(self, ctx:vhdlParser.Next_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#next_statement.
    def exitNext_statement(self, ctx:vhdlParser.Next_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#exit_statement.
    def enterExit_statement(self, ctx:vhdlParser.Exit_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#exit_statement.
    def exitExit_statement(self, ctx:vhdlParser.Exit_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#return_statement.
    def enterReturn_statement(self, ctx:vhdlParser.Return_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#return_statement.
    def exitReturn_statement(self, ctx:vhdlParser.Return_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#null_statement.
    def enterNull_statement(self, ctx:vhdlParser.Null_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#null_statement.
    def exitNull_statement(self, ctx:vhdlParser.Null_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#concurrent_statement_with_optional_label.
    def enterConcurrent_statement_with_optional_label(self, ctx:vhdlParser.Concurrent_statement_with_optional_labelContext):
        pass

    # Exit a parse tree produced by vhdlParser#concurrent_statement_with_optional_label.
    def exitConcurrent_statement_with_optional_label(self, ctx:vhdlParser.Concurrent_statement_with_optional_labelContext):
        pass


    # Enter a parse tree produced by vhdlParser#concurrent_statement.
    def enterConcurrent_statement(self, ctx:vhdlParser.Concurrent_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#concurrent_statement.
    def exitConcurrent_statement(self, ctx:vhdlParser.Concurrent_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#block_statement.
    def enterBlock_statement(self, ctx:vhdlParser.Block_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#block_statement.
    def exitBlock_statement(self, ctx:vhdlParser.Block_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#block_header.
    def enterBlock_header(self, ctx:vhdlParser.Block_headerContext):
        pass

    # Exit a parse tree produced by vhdlParser#block_header.
    def exitBlock_header(self, ctx:vhdlParser.Block_headerContext):
        pass


    # Enter a parse tree produced by vhdlParser#process_statement.
    def enterProcess_statement(self, ctx:vhdlParser.Process_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#process_statement.
    def exitProcess_statement(self, ctx:vhdlParser.Process_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#process_sensitivity_list.
    def enterProcess_sensitivity_list(self, ctx:vhdlParser.Process_sensitivity_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#process_sensitivity_list.
    def exitProcess_sensitivity_list(self, ctx:vhdlParser.Process_sensitivity_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#process_or_package_declarative_item.
    def enterProcess_or_package_declarative_item(self, ctx:vhdlParser.Process_or_package_declarative_itemContext):
        pass

    # Exit a parse tree produced by vhdlParser#process_or_package_declarative_item.
    def exitProcess_or_package_declarative_item(self, ctx:vhdlParser.Process_or_package_declarative_itemContext):
        pass


    # Enter a parse tree produced by vhdlParser#process_declarative_item.
    def enterProcess_declarative_item(self, ctx:vhdlParser.Process_declarative_itemContext):
        pass

    # Exit a parse tree produced by vhdlParser#process_declarative_item.
    def exitProcess_declarative_item(self, ctx:vhdlParser.Process_declarative_itemContext):
        pass


    # Enter a parse tree produced by vhdlParser#concurrent_procedure_call_statement.
    def enterConcurrent_procedure_call_statement(self, ctx:vhdlParser.Concurrent_procedure_call_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#concurrent_procedure_call_statement.
    def exitConcurrent_procedure_call_statement(self, ctx:vhdlParser.Concurrent_procedure_call_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#concurrent_assertion_statement.
    def enterConcurrent_assertion_statement(self, ctx:vhdlParser.Concurrent_assertion_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#concurrent_assertion_statement.
    def exitConcurrent_assertion_statement(self, ctx:vhdlParser.Concurrent_assertion_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#concurrent_signal_assignment_statement.
    def enterConcurrent_signal_assignment_statement(self, ctx:vhdlParser.Concurrent_signal_assignment_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#concurrent_signal_assignment_statement.
    def exitConcurrent_signal_assignment_statement(self, ctx:vhdlParser.Concurrent_signal_assignment_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#concurrent_signal_assignment_any.
    def enterConcurrent_signal_assignment_any(self, ctx:vhdlParser.Concurrent_signal_assignment_anyContext):
        pass

    # Exit a parse tree produced by vhdlParser#concurrent_signal_assignment_any.
    def exitConcurrent_signal_assignment_any(self, ctx:vhdlParser.Concurrent_signal_assignment_anyContext):
        pass


    # Enter a parse tree produced by vhdlParser#concurrent_selected_signal_assignment.
    def enterConcurrent_selected_signal_assignment(self, ctx:vhdlParser.Concurrent_selected_signal_assignmentContext):
        pass

    # Exit a parse tree produced by vhdlParser#concurrent_selected_signal_assignment.
    def exitConcurrent_selected_signal_assignment(self, ctx:vhdlParser.Concurrent_selected_signal_assignmentContext):
        pass


    # Enter a parse tree produced by vhdlParser#component_instantiation_statement.
    def enterComponent_instantiation_statement(self, ctx:vhdlParser.Component_instantiation_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#component_instantiation_statement.
    def exitComponent_instantiation_statement(self, ctx:vhdlParser.Component_instantiation_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#instantiated_unit.
    def enterInstantiated_unit(self, ctx:vhdlParser.Instantiated_unitContext):
        pass

    # Exit a parse tree produced by vhdlParser#instantiated_unit.
    def exitInstantiated_unit(self, ctx:vhdlParser.Instantiated_unitContext):
        pass


    # Enter a parse tree produced by vhdlParser#generate_statement.
    def enterGenerate_statement(self, ctx:vhdlParser.Generate_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#generate_statement.
    def exitGenerate_statement(self, ctx:vhdlParser.Generate_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#for_generate_statement.
    def enterFor_generate_statement(self, ctx:vhdlParser.For_generate_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#for_generate_statement.
    def exitFor_generate_statement(self, ctx:vhdlParser.For_generate_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#if_generate_statement.
    def enterIf_generate_statement(self, ctx:vhdlParser.If_generate_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#if_generate_statement.
    def exitIf_generate_statement(self, ctx:vhdlParser.If_generate_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#case_generate_statement.
    def enterCase_generate_statement(self, ctx:vhdlParser.Case_generate_statementContext):
        pass

    # Exit a parse tree produced by vhdlParser#case_generate_statement.
    def exitCase_generate_statement(self, ctx:vhdlParser.Case_generate_statementContext):
        pass


    # Enter a parse tree produced by vhdlParser#case_generate_alternative.
    def enterCase_generate_alternative(self, ctx:vhdlParser.Case_generate_alternativeContext):
        pass

    # Exit a parse tree produced by vhdlParser#case_generate_alternative.
    def exitCase_generate_alternative(self, ctx:vhdlParser.Case_generate_alternativeContext):
        pass


    # Enter a parse tree produced by vhdlParser#generate_statement_body_with_begin_end.
    def enterGenerate_statement_body_with_begin_end(self, ctx:vhdlParser.Generate_statement_body_with_begin_endContext):
        pass

    # Exit a parse tree produced by vhdlParser#generate_statement_body_with_begin_end.
    def exitGenerate_statement_body_with_begin_end(self, ctx:vhdlParser.Generate_statement_body_with_begin_endContext):
        pass


    # Enter a parse tree produced by vhdlParser#generate_statement_body.
    def enterGenerate_statement_body(self, ctx:vhdlParser.Generate_statement_bodyContext):
        pass

    # Exit a parse tree produced by vhdlParser#generate_statement_body.
    def exitGenerate_statement_body(self, ctx:vhdlParser.Generate_statement_bodyContext):
        pass


    # Enter a parse tree produced by vhdlParser#label.
    def enterLabel(self, ctx:vhdlParser.LabelContext):
        pass

    # Exit a parse tree produced by vhdlParser#label.
    def exitLabel(self, ctx:vhdlParser.LabelContext):
        pass


    # Enter a parse tree produced by vhdlParser#use_clause.
    def enterUse_clause(self, ctx:vhdlParser.Use_clauseContext):
        pass

    # Exit a parse tree produced by vhdlParser#use_clause.
    def exitUse_clause(self, ctx:vhdlParser.Use_clauseContext):
        pass


    # Enter a parse tree produced by vhdlParser#design_file.
    def enterDesign_file(self, ctx:vhdlParser.Design_fileContext):
        pass

    # Exit a parse tree produced by vhdlParser#design_file.
    def exitDesign_file(self, ctx:vhdlParser.Design_fileContext):
        pass


    # Enter a parse tree produced by vhdlParser#design_unit.
    def enterDesign_unit(self, ctx:vhdlParser.Design_unitContext):
        pass

    # Exit a parse tree produced by vhdlParser#design_unit.
    def exitDesign_unit(self, ctx:vhdlParser.Design_unitContext):
        pass


    # Enter a parse tree produced by vhdlParser#library_unit.
    def enterLibrary_unit(self, ctx:vhdlParser.Library_unitContext):
        pass

    # Exit a parse tree produced by vhdlParser#library_unit.
    def exitLibrary_unit(self, ctx:vhdlParser.Library_unitContext):
        pass


    # Enter a parse tree produced by vhdlParser#primary_unit.
    def enterPrimary_unit(self, ctx:vhdlParser.Primary_unitContext):
        pass

    # Exit a parse tree produced by vhdlParser#primary_unit.
    def exitPrimary_unit(self, ctx:vhdlParser.Primary_unitContext):
        pass


    # Enter a parse tree produced by vhdlParser#secondary_unit.
    def enterSecondary_unit(self, ctx:vhdlParser.Secondary_unitContext):
        pass

    # Exit a parse tree produced by vhdlParser#secondary_unit.
    def exitSecondary_unit(self, ctx:vhdlParser.Secondary_unitContext):
        pass


    # Enter a parse tree produced by vhdlParser#library_clause.
    def enterLibrary_clause(self, ctx:vhdlParser.Library_clauseContext):
        pass

    # Exit a parse tree produced by vhdlParser#library_clause.
    def exitLibrary_clause(self, ctx:vhdlParser.Library_clauseContext):
        pass


    # Enter a parse tree produced by vhdlParser#logical_name_list.
    def enterLogical_name_list(self, ctx:vhdlParser.Logical_name_listContext):
        pass

    # Exit a parse tree produced by vhdlParser#logical_name_list.
    def exitLogical_name_list(self, ctx:vhdlParser.Logical_name_listContext):
        pass


    # Enter a parse tree produced by vhdlParser#context_declaration.
    def enterContext_declaration(self, ctx:vhdlParser.Context_declarationContext):
        pass

    # Exit a parse tree produced by vhdlParser#context_declaration.
    def exitContext_declaration(self, ctx:vhdlParser.Context_declarationContext):
        pass


    # Enter a parse tree produced by vhdlParser#context_clause.
    def enterContext_clause(self, ctx:vhdlParser.Context_clauseContext):
        pass

    # Exit a parse tree produced by vhdlParser#context_clause.
    def exitContext_clause(self, ctx:vhdlParser.Context_clauseContext):
        pass


    # Enter a parse tree produced by vhdlParser#context_item.
    def enterContext_item(self, ctx:vhdlParser.Context_itemContext):
        pass

    # Exit a parse tree produced by vhdlParser#context_item.
    def exitContext_item(self, ctx:vhdlParser.Context_itemContext):
        pass


    # Enter a parse tree produced by vhdlParser#context_reference.
    def enterContext_reference(self, ctx:vhdlParser.Context_referenceContext):
        pass

    # Exit a parse tree produced by vhdlParser#context_reference.
    def exitContext_reference(self, ctx:vhdlParser.Context_referenceContext):
        pass


    # Enter a parse tree produced by vhdlParser#identifier.
    def enterIdentifier(self, ctx:vhdlParser.IdentifierContext):
        pass

    # Exit a parse tree produced by vhdlParser#identifier.
    def exitIdentifier(self, ctx:vhdlParser.IdentifierContext):
        pass



del vhdlParser