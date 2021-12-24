# Generated from vhdl.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .vhdlParser import vhdlParser
else:
    from vhdlParser import vhdlParser

# This class defines a complete generic visitor for a parse tree produced by vhdlParser.

class vhdlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by vhdlParser#abstract_literal.
    def visitAbstract_literal(self, ctx:vhdlParser.Abstract_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#access_type_definition.
    def visitAccess_type_definition(self, ctx:vhdlParser.Access_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#across_aspect.
    def visitAcross_aspect(self, ctx:vhdlParser.Across_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#actual_designator.
    def visitActual_designator(self, ctx:vhdlParser.Actual_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#actual_parameter_part.
    def visitActual_parameter_part(self, ctx:vhdlParser.Actual_parameter_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#actual_part.
    def visitActual_part(self, ctx:vhdlParser.Actual_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#adding_operator.
    def visitAdding_operator(self, ctx:vhdlParser.Adding_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#aggregate.
    def visitAggregate(self, ctx:vhdlParser.AggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#alias_declaration.
    def visitAlias_declaration(self, ctx:vhdlParser.Alias_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#alias_designator.
    def visitAlias_designator(self, ctx:vhdlParser.Alias_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#alias_indication.
    def visitAlias_indication(self, ctx:vhdlParser.Alias_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#allocator.
    def visitAllocator(self, ctx:vhdlParser.AllocatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#architecture_body.
    def visitArchitecture_body(self, ctx:vhdlParser.Architecture_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#architecture_declarative_part.
    def visitArchitecture_declarative_part(self, ctx:vhdlParser.Architecture_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#architecture_statement.
    def visitArchitecture_statement(self, ctx:vhdlParser.Architecture_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#architecture_statement_part.
    def visitArchitecture_statement_part(self, ctx:vhdlParser.Architecture_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#array_nature_definition.
    def visitArray_nature_definition(self, ctx:vhdlParser.Array_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#array_type_definition.
    def visitArray_type_definition(self, ctx:vhdlParser.Array_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#assertion.
    def visitAssertion(self, ctx:vhdlParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#assertion_statement.
    def visitAssertion_statement(self, ctx:vhdlParser.Assertion_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#association_element.
    def visitAssociation_element(self, ctx:vhdlParser.Association_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#association_list.
    def visitAssociation_list(self, ctx:vhdlParser.Association_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:vhdlParser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#attribute_designator.
    def visitAttribute_designator(self, ctx:vhdlParser.Attribute_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#attribute_specification.
    def visitAttribute_specification(self, ctx:vhdlParser.Attribute_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#base_unit_declaration.
    def visitBase_unit_declaration(self, ctx:vhdlParser.Base_unit_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#binding_indication.
    def visitBinding_indication(self, ctx:vhdlParser.Binding_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_configuration.
    def visitBlock_configuration(self, ctx:vhdlParser.Block_configurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_declarative_item.
    def visitBlock_declarative_item(self, ctx:vhdlParser.Block_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_declarative_part.
    def visitBlock_declarative_part(self, ctx:vhdlParser.Block_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_header.
    def visitBlock_header(self, ctx:vhdlParser.Block_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_specification.
    def visitBlock_specification(self, ctx:vhdlParser.Block_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_statement.
    def visitBlock_statement(self, ctx:vhdlParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#block_statement_part.
    def visitBlock_statement_part(self, ctx:vhdlParser.Block_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#branch_quantity_declaration.
    def visitBranch_quantity_declaration(self, ctx:vhdlParser.Branch_quantity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#break_element.
    def visitBreak_element(self, ctx:vhdlParser.Break_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#break_list.
    def visitBreak_list(self, ctx:vhdlParser.Break_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#break_selector_clause.
    def visitBreak_selector_clause(self, ctx:vhdlParser.Break_selector_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#break_statement.
    def visitBreak_statement(self, ctx:vhdlParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#case_statement.
    def visitCase_statement(self, ctx:vhdlParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#case_statement_alternative.
    def visitCase_statement_alternative(self, ctx:vhdlParser.Case_statement_alternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#choice.
    def visitChoice(self, ctx:vhdlParser.ChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#choices.
    def visitChoices(self, ctx:vhdlParser.ChoicesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#component_configuration.
    def visitComponent_configuration(self, ctx:vhdlParser.Component_configurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#component_declaration.
    def visitComponent_declaration(self, ctx:vhdlParser.Component_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#component_instantiation_statement.
    def visitComponent_instantiation_statement(self, ctx:vhdlParser.Component_instantiation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#component_specification.
    def visitComponent_specification(self, ctx:vhdlParser.Component_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#composite_nature_definition.
    def visitComposite_nature_definition(self, ctx:vhdlParser.Composite_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#composite_type_definition.
    def visitComposite_type_definition(self, ctx:vhdlParser.Composite_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#concurrent_assertion_statement.
    def visitConcurrent_assertion_statement(self, ctx:vhdlParser.Concurrent_assertion_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#concurrent_break_statement.
    def visitConcurrent_break_statement(self, ctx:vhdlParser.Concurrent_break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#concurrent_procedure_call_statement.
    def visitConcurrent_procedure_call_statement(self, ctx:vhdlParser.Concurrent_procedure_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#concurrent_signal_assignment_statement.
    def visitConcurrent_signal_assignment_statement(self, ctx:vhdlParser.Concurrent_signal_assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#condition.
    def visitCondition(self, ctx:vhdlParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#condition_clause.
    def visitCondition_clause(self, ctx:vhdlParser.Condition_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#conditional_signal_assignment.
    def visitConditional_signal_assignment(self, ctx:vhdlParser.Conditional_signal_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#conditional_waveforms.
    def visitConditional_waveforms(self, ctx:vhdlParser.Conditional_waveformsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#configuration_declaration.
    def visitConfiguration_declaration(self, ctx:vhdlParser.Configuration_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#configuration_declarative_item.
    def visitConfiguration_declarative_item(self, ctx:vhdlParser.Configuration_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#configuration_declarative_part.
    def visitConfiguration_declarative_part(self, ctx:vhdlParser.Configuration_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#configuration_item.
    def visitConfiguration_item(self, ctx:vhdlParser.Configuration_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#configuration_specification.
    def visitConfiguration_specification(self, ctx:vhdlParser.Configuration_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#constant_declaration.
    def visitConstant_declaration(self, ctx:vhdlParser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#constrained_array_definition.
    def visitConstrained_array_definition(self, ctx:vhdlParser.Constrained_array_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#constrained_nature_definition.
    def visitConstrained_nature_definition(self, ctx:vhdlParser.Constrained_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#constraint.
    def visitConstraint(self, ctx:vhdlParser.ConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#context_clause.
    def visitContext_clause(self, ctx:vhdlParser.Context_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#context_item.
    def visitContext_item(self, ctx:vhdlParser.Context_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#delay_mechanism.
    def visitDelay_mechanism(self, ctx:vhdlParser.Delay_mechanismContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#design_file.
    def visitDesign_file(self, ctx:vhdlParser.Design_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#design_unit.
    def visitDesign_unit(self, ctx:vhdlParser.Design_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#designator.
    def visitDesignator(self, ctx:vhdlParser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#direction.
    def visitDirection(self, ctx:vhdlParser.DirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#disconnection_specification.
    def visitDisconnection_specification(self, ctx:vhdlParser.Disconnection_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#discrete_range.
    def visitDiscrete_range(self, ctx:vhdlParser.Discrete_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#element_association.
    def visitElement_association(self, ctx:vhdlParser.Element_associationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#element_declaration.
    def visitElement_declaration(self, ctx:vhdlParser.Element_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#element_subnature_definition.
    def visitElement_subnature_definition(self, ctx:vhdlParser.Element_subnature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#element_subtype_definition.
    def visitElement_subtype_definition(self, ctx:vhdlParser.Element_subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_aspect.
    def visitEntity_aspect(self, ctx:vhdlParser.Entity_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_class.
    def visitEntity_class(self, ctx:vhdlParser.Entity_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_class_entry.
    def visitEntity_class_entry(self, ctx:vhdlParser.Entity_class_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_class_entry_list.
    def visitEntity_class_entry_list(self, ctx:vhdlParser.Entity_class_entry_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_declaration.
    def visitEntity_declaration(self, ctx:vhdlParser.Entity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_declarative_item.
    def visitEntity_declarative_item(self, ctx:vhdlParser.Entity_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_declarative_part.
    def visitEntity_declarative_part(self, ctx:vhdlParser.Entity_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_designator.
    def visitEntity_designator(self, ctx:vhdlParser.Entity_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_header.
    def visitEntity_header(self, ctx:vhdlParser.Entity_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_name_list.
    def visitEntity_name_list(self, ctx:vhdlParser.Entity_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_specification.
    def visitEntity_specification(self, ctx:vhdlParser.Entity_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_statement.
    def visitEntity_statement(self, ctx:vhdlParser.Entity_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_statement_part.
    def visitEntity_statement_part(self, ctx:vhdlParser.Entity_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#entity_tag.
    def visitEntity_tag(self, ctx:vhdlParser.Entity_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#enumeration_literal.
    def visitEnumeration_literal(self, ctx:vhdlParser.Enumeration_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#enumeration_type_definition.
    def visitEnumeration_type_definition(self, ctx:vhdlParser.Enumeration_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#exit_statement.
    def visitExit_statement(self, ctx:vhdlParser.Exit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#expression.
    def visitExpression(self, ctx:vhdlParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#factor.
    def visitFactor(self, ctx:vhdlParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#file_declaration.
    def visitFile_declaration(self, ctx:vhdlParser.File_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#file_logical_name.
    def visitFile_logical_name(self, ctx:vhdlParser.File_logical_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#file_open_information.
    def visitFile_open_information(self, ctx:vhdlParser.File_open_informationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#file_type_definition.
    def visitFile_type_definition(self, ctx:vhdlParser.File_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#formal_parameter_list.
    def visitFormal_parameter_list(self, ctx:vhdlParser.Formal_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#formal_part.
    def visitFormal_part(self, ctx:vhdlParser.Formal_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#free_quantity_declaration.
    def visitFree_quantity_declaration(self, ctx:vhdlParser.Free_quantity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generate_statement.
    def visitGenerate_statement(self, ctx:vhdlParser.Generate_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generation_scheme.
    def visitGeneration_scheme(self, ctx:vhdlParser.Generation_schemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generic_clause.
    def visitGeneric_clause(self, ctx:vhdlParser.Generic_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generic_list.
    def visitGeneric_list(self, ctx:vhdlParser.Generic_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#generic_map_aspect.
    def visitGeneric_map_aspect(self, ctx:vhdlParser.Generic_map_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#group_constituent.
    def visitGroup_constituent(self, ctx:vhdlParser.Group_constituentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#group_constituent_list.
    def visitGroup_constituent_list(self, ctx:vhdlParser.Group_constituent_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#group_declaration.
    def visitGroup_declaration(self, ctx:vhdlParser.Group_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#group_template_declaration.
    def visitGroup_template_declaration(self, ctx:vhdlParser.Group_template_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#guarded_signal_specification.
    def visitGuarded_signal_specification(self, ctx:vhdlParser.Guarded_signal_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#identifier.
    def visitIdentifier(self, ctx:vhdlParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#identifier_list.
    def visitIdentifier_list(self, ctx:vhdlParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#if_statement.
    def visitIf_statement(self, ctx:vhdlParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#index_constraint.
    def visitIndex_constraint(self, ctx:vhdlParser.Index_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#index_specification.
    def visitIndex_specification(self, ctx:vhdlParser.Index_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#index_subtype_definition.
    def visitIndex_subtype_definition(self, ctx:vhdlParser.Index_subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#instantiated_unit.
    def visitInstantiated_unit(self, ctx:vhdlParser.Instantiated_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#instantiation_list.
    def visitInstantiation_list(self, ctx:vhdlParser.Instantiation_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_constant_declaration.
    def visitInterface_constant_declaration(self, ctx:vhdlParser.Interface_constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_declaration.
    def visitInterface_declaration(self, ctx:vhdlParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_element.
    def visitInterface_element(self, ctx:vhdlParser.Interface_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_file_declaration.
    def visitInterface_file_declaration(self, ctx:vhdlParser.Interface_file_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_signal_list.
    def visitInterface_signal_list(self, ctx:vhdlParser.Interface_signal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_port_list.
    def visitInterface_port_list(self, ctx:vhdlParser.Interface_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_list.
    def visitInterface_list(self, ctx:vhdlParser.Interface_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_quantity_declaration.
    def visitInterface_quantity_declaration(self, ctx:vhdlParser.Interface_quantity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_port_declaration.
    def visitInterface_port_declaration(self, ctx:vhdlParser.Interface_port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_signal_declaration.
    def visitInterface_signal_declaration(self, ctx:vhdlParser.Interface_signal_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_terminal_declaration.
    def visitInterface_terminal_declaration(self, ctx:vhdlParser.Interface_terminal_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#interface_variable_declaration.
    def visitInterface_variable_declaration(self, ctx:vhdlParser.Interface_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#iteration_scheme.
    def visitIteration_scheme(self, ctx:vhdlParser.Iteration_schemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#label_colon.
    def visitLabel_colon(self, ctx:vhdlParser.Label_colonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#library_clause.
    def visitLibrary_clause(self, ctx:vhdlParser.Library_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#library_unit.
    def visitLibrary_unit(self, ctx:vhdlParser.Library_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#literal.
    def visitLiteral(self, ctx:vhdlParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#logical_name.
    def visitLogical_name(self, ctx:vhdlParser.Logical_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#logical_name_list.
    def visitLogical_name_list(self, ctx:vhdlParser.Logical_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#logical_operator.
    def visitLogical_operator(self, ctx:vhdlParser.Logical_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#loop_statement.
    def visitLoop_statement(self, ctx:vhdlParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signal_mode.
    def visitSignal_mode(self, ctx:vhdlParser.Signal_modeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#multiplying_operator.
    def visitMultiplying_operator(self, ctx:vhdlParser.Multiplying_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#name.
    def visitName(self, ctx:vhdlParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#name_part.
    def visitName_part(self, ctx:vhdlParser.Name_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#selected_name.
    def visitSelected_name(self, ctx:vhdlParser.Selected_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#selected_name_part.
    def visitSelected_name_part(self, ctx:vhdlParser.Selected_name_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#function_call_or_indexed_name_part.
    def visitFunction_call_or_indexed_name_part(self, ctx:vhdlParser.Function_call_or_indexed_name_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#slice_name_part.
    def visitSlice_name_part(self, ctx:vhdlParser.Slice_name_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#attribute_name_part.
    def visitAttribute_name_part(self, ctx:vhdlParser.Attribute_name_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#nature_declaration.
    def visitNature_declaration(self, ctx:vhdlParser.Nature_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#nature_definition.
    def visitNature_definition(self, ctx:vhdlParser.Nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#nature_element_declaration.
    def visitNature_element_declaration(self, ctx:vhdlParser.Nature_element_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#next_statement.
    def visitNext_statement(self, ctx:vhdlParser.Next_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#numeric_literal.
    def visitNumeric_literal(self, ctx:vhdlParser.Numeric_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#object_declaration.
    def visitObject_declaration(self, ctx:vhdlParser.Object_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#opts.
    def visitOpts(self, ctx:vhdlParser.OptsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#package_body.
    def visitPackage_body(self, ctx:vhdlParser.Package_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#package_body_declarative_item.
    def visitPackage_body_declarative_item(self, ctx:vhdlParser.Package_body_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#package_body_declarative_part.
    def visitPackage_body_declarative_part(self, ctx:vhdlParser.Package_body_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#package_declaration.
    def visitPackage_declaration(self, ctx:vhdlParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#package_declarative_item.
    def visitPackage_declarative_item(self, ctx:vhdlParser.Package_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#package_declarative_part.
    def visitPackage_declarative_part(self, ctx:vhdlParser.Package_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#parameter_specification.
    def visitParameter_specification(self, ctx:vhdlParser.Parameter_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#physical_literal.
    def visitPhysical_literal(self, ctx:vhdlParser.Physical_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#physical_type_definition.
    def visitPhysical_type_definition(self, ctx:vhdlParser.Physical_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#port_clause.
    def visitPort_clause(self, ctx:vhdlParser.Port_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#port_list.
    def visitPort_list(self, ctx:vhdlParser.Port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#port_map_aspect.
    def visitPort_map_aspect(self, ctx:vhdlParser.Port_map_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#primary.
    def visitPrimary(self, ctx:vhdlParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#primary_unit.
    def visitPrimary_unit(self, ctx:vhdlParser.Primary_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#procedural_declarative_item.
    def visitProcedural_declarative_item(self, ctx:vhdlParser.Procedural_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#procedural_declarative_part.
    def visitProcedural_declarative_part(self, ctx:vhdlParser.Procedural_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#procedural_statement_part.
    def visitProcedural_statement_part(self, ctx:vhdlParser.Procedural_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#procedure_call.
    def visitProcedure_call(self, ctx:vhdlParser.Procedure_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#procedure_call_statement.
    def visitProcedure_call_statement(self, ctx:vhdlParser.Procedure_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#process_declarative_item.
    def visitProcess_declarative_item(self, ctx:vhdlParser.Process_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#process_declarative_part.
    def visitProcess_declarative_part(self, ctx:vhdlParser.Process_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#process_statement.
    def visitProcess_statement(self, ctx:vhdlParser.Process_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#process_statement_part.
    def visitProcess_statement_part(self, ctx:vhdlParser.Process_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#qualified_expression.
    def visitQualified_expression(self, ctx:vhdlParser.Qualified_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#quantity_declaration.
    def visitQuantity_declaration(self, ctx:vhdlParser.Quantity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#quantity_list.
    def visitQuantity_list(self, ctx:vhdlParser.Quantity_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#quantity_specification.
    def visitQuantity_specification(self, ctx:vhdlParser.Quantity_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#range_decl.
    def visitRange_decl(self, ctx:vhdlParser.Range_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#explicit_range.
    def visitExplicit_range(self, ctx:vhdlParser.Explicit_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#range_constraint.
    def visitRange_constraint(self, ctx:vhdlParser.Range_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#record_nature_definition.
    def visitRecord_nature_definition(self, ctx:vhdlParser.Record_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#record_type_definition.
    def visitRecord_type_definition(self, ctx:vhdlParser.Record_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#relation.
    def visitRelation(self, ctx:vhdlParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#relational_operator.
    def visitRelational_operator(self, ctx:vhdlParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#report_statement.
    def visitReport_statement(self, ctx:vhdlParser.Report_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#return_statement.
    def visitReturn_statement(self, ctx:vhdlParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#scalar_nature_definition.
    def visitScalar_nature_definition(self, ctx:vhdlParser.Scalar_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#scalar_type_definition.
    def visitScalar_type_definition(self, ctx:vhdlParser.Scalar_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#secondary_unit.
    def visitSecondary_unit(self, ctx:vhdlParser.Secondary_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#secondary_unit_declaration.
    def visitSecondary_unit_declaration(self, ctx:vhdlParser.Secondary_unit_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#selected_signal_assignment.
    def visitSelected_signal_assignment(self, ctx:vhdlParser.Selected_signal_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#selected_waveforms.
    def visitSelected_waveforms(self, ctx:vhdlParser.Selected_waveformsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#sensitivity_clause.
    def visitSensitivity_clause(self, ctx:vhdlParser.Sensitivity_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#sensitivity_list.
    def visitSensitivity_list(self, ctx:vhdlParser.Sensitivity_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#sequence_of_statements.
    def visitSequence_of_statements(self, ctx:vhdlParser.Sequence_of_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#sequential_statement.
    def visitSequential_statement(self, ctx:vhdlParser.Sequential_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#shift_expression.
    def visitShift_expression(self, ctx:vhdlParser.Shift_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#shift_operator.
    def visitShift_operator(self, ctx:vhdlParser.Shift_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signal_assignment_statement.
    def visitSignal_assignment_statement(self, ctx:vhdlParser.Signal_assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signal_declaration.
    def visitSignal_declaration(self, ctx:vhdlParser.Signal_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signal_kind.
    def visitSignal_kind(self, ctx:vhdlParser.Signal_kindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signal_list.
    def visitSignal_list(self, ctx:vhdlParser.Signal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#signature.
    def visitSignature(self, ctx:vhdlParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simple_expression.
    def visitSimple_expression(self, ctx:vhdlParser.Simple_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simple_simultaneous_statement.
    def visitSimple_simultaneous_statement(self, ctx:vhdlParser.Simple_simultaneous_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simultaneous_alternative.
    def visitSimultaneous_alternative(self, ctx:vhdlParser.Simultaneous_alternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simultaneous_case_statement.
    def visitSimultaneous_case_statement(self, ctx:vhdlParser.Simultaneous_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simultaneous_if_statement.
    def visitSimultaneous_if_statement(self, ctx:vhdlParser.Simultaneous_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simultaneous_procedural_statement.
    def visitSimultaneous_procedural_statement(self, ctx:vhdlParser.Simultaneous_procedural_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simultaneous_statement.
    def visitSimultaneous_statement(self, ctx:vhdlParser.Simultaneous_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#simultaneous_statement_part.
    def visitSimultaneous_statement_part(self, ctx:vhdlParser.Simultaneous_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#source_aspect.
    def visitSource_aspect(self, ctx:vhdlParser.Source_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#source_quantity_declaration.
    def visitSource_quantity_declaration(self, ctx:vhdlParser.Source_quantity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#step_limit_specification.
    def visitStep_limit_specification(self, ctx:vhdlParser.Step_limit_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subnature_declaration.
    def visitSubnature_declaration(self, ctx:vhdlParser.Subnature_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subnature_indication.
    def visitSubnature_indication(self, ctx:vhdlParser.Subnature_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subprogram_body.
    def visitSubprogram_body(self, ctx:vhdlParser.Subprogram_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subprogram_declaration.
    def visitSubprogram_declaration(self, ctx:vhdlParser.Subprogram_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subprogram_declarative_item.
    def visitSubprogram_declarative_item(self, ctx:vhdlParser.Subprogram_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subprogram_declarative_part.
    def visitSubprogram_declarative_part(self, ctx:vhdlParser.Subprogram_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subprogram_kind.
    def visitSubprogram_kind(self, ctx:vhdlParser.Subprogram_kindContext):
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


    # Visit a parse tree produced by vhdlParser#subprogram_statement_part.
    def visitSubprogram_statement_part(self, ctx:vhdlParser.Subprogram_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subtype_declaration.
    def visitSubtype_declaration(self, ctx:vhdlParser.Subtype_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#subtype_indication.
    def visitSubtype_indication(self, ctx:vhdlParser.Subtype_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#suffix.
    def visitSuffix(self, ctx:vhdlParser.SuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#target.
    def visitTarget(self, ctx:vhdlParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#term.
    def visitTerm(self, ctx:vhdlParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#terminal_aspect.
    def visitTerminal_aspect(self, ctx:vhdlParser.Terminal_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#terminal_declaration.
    def visitTerminal_declaration(self, ctx:vhdlParser.Terminal_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#through_aspect.
    def visitThrough_aspect(self, ctx:vhdlParser.Through_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#timeout_clause.
    def visitTimeout_clause(self, ctx:vhdlParser.Timeout_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#tolerance_aspect.
    def visitTolerance_aspect(self, ctx:vhdlParser.Tolerance_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#type_declaration.
    def visitType_declaration(self, ctx:vhdlParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#type_definition.
    def visitType_definition(self, ctx:vhdlParser.Type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#unconstrained_array_definition.
    def visitUnconstrained_array_definition(self, ctx:vhdlParser.Unconstrained_array_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#unconstrained_nature_definition.
    def visitUnconstrained_nature_definition(self, ctx:vhdlParser.Unconstrained_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#use_clause.
    def visitUse_clause(self, ctx:vhdlParser.Use_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#variable_assignment_statement.
    def visitVariable_assignment_statement(self, ctx:vhdlParser.Variable_assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#variable_declaration.
    def visitVariable_declaration(self, ctx:vhdlParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#wait_statement.
    def visitWait_statement(self, ctx:vhdlParser.Wait_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#waveform.
    def visitWaveform(self, ctx:vhdlParser.WaveformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vhdlParser#waveform_element.
    def visitWaveform_element(self, ctx:vhdlParser.Waveform_elementContext):
        return self.visitChildren(ctx)



del vhdlParser