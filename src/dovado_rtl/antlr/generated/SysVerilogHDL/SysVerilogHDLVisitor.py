# Generated from SysVerilogHDL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SysVerilogHDLParser import SysVerilogHDLParser
else:
    from SysVerilogHDLParser import SysVerilogHDLParser

# This class defines a complete generic visitor for a parse tree produced by SysVerilogHDLParser.

class SysVerilogHDLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SysVerilogHDLParser#module_keyword.
    def visitModule_keyword(self, ctx:SysVerilogHDLParser.Module_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#struct_keyword.
    def visitStruct_keyword(self, ctx:SysVerilogHDLParser.Struct_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#any_case_keyword.
    def visitAny_case_keyword(self, ctx:SysVerilogHDLParser.Any_case_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#semicolon.
    def visitSemicolon(self, ctx:SysVerilogHDLParser.SemicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#unary_operator.
    def visitUnary_operator(self, ctx:SysVerilogHDLParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#binary_operator.
    def visitBinary_operator(self, ctx:SysVerilogHDLParser.Binary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#unary_assign_operator.
    def visitUnary_assign_operator(self, ctx:SysVerilogHDLParser.Unary_assign_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#binary_assign_operator.
    def visitBinary_assign_operator(self, ctx:SysVerilogHDLParser.Binary_assign_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#source_text.
    def visitSource_text(self, ctx:SysVerilogHDLParser.Source_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#description_star.
    def visitDescription_star(self, ctx:SysVerilogHDLParser.Description_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#header_text.
    def visitHeader_text(self, ctx:SysVerilogHDLParser.Header_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#design_attribute.
    def visitDesign_attribute(self, ctx:SysVerilogHDLParser.Design_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#compiler_directive.
    def visitCompiler_directive(self, ctx:SysVerilogHDLParser.Compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#description.
    def visitDescription(self, ctx:SysVerilogHDLParser.DescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#module_declaration.
    def visitModule_declaration(self, ctx:SysVerilogHDLParser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#module_identifier.
    def visitModule_identifier(self, ctx:SysVerilogHDLParser.Module_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#module_interface.
    def visitModule_interface(self, ctx:SysVerilogHDLParser.Module_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#module_parameter_interface.
    def visitModule_parameter_interface(self, ctx:SysVerilogHDLParser.Module_parameter_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#module_port_interface.
    def visitModule_port_interface(self, ctx:SysVerilogHDLParser.Module_port_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#module_item_star.
    def visitModule_item_star(self, ctx:SysVerilogHDLParser.Module_item_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#module_item.
    def visitModule_item(self, ctx:SysVerilogHDLParser.Module_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#colon_module_identifier.
    def visitColon_module_identifier(self, ctx:SysVerilogHDLParser.Colon_module_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#package_declaration.
    def visitPackage_declaration(self, ctx:SysVerilogHDLParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#package_identifier.
    def visitPackage_identifier(self, ctx:SysVerilogHDLParser.Package_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#colon_package_identifier.
    def visitColon_package_identifier(self, ctx:SysVerilogHDLParser.Colon_package_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#package_item_star.
    def visitPackage_item_star(self, ctx:SysVerilogHDLParser.Package_item_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#package_item.
    def visitPackage_item(self, ctx:SysVerilogHDLParser.Package_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#import_package.
    def visitImport_package(self, ctx:SysVerilogHDLParser.Import_packageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#package_item_identifier.
    def visitPackage_item_identifier(self, ctx:SysVerilogHDLParser.Package_item_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#parameter_item_semicolon.
    def visitParameter_item_semicolon(self, ctx:SysVerilogHDLParser.Parameter_item_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#parameter_item.
    def visitParameter_item(self, ctx:SysVerilogHDLParser.Parameter_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_port_item_semicolon.
    def visitAttr_port_item_semicolon(self, ctx:SysVerilogHDLParser.Attr_port_item_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_variable_item_semicolon.
    def visitAttr_variable_item_semicolon(self, ctx:SysVerilogHDLParser.Attr_variable_item_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#variable_item.
    def visitVariable_item(self, ctx:SysVerilogHDLParser.Variable_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#subroutine_item_semicolon.
    def visitSubroutine_item_semicolon(self, ctx:SysVerilogHDLParser.Subroutine_item_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#subroutine_item.
    def visitSubroutine_item(self, ctx:SysVerilogHDLParser.Subroutine_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_construct_item.
    def visitAttr_construct_item(self, ctx:SysVerilogHDLParser.Attr_construct_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#construct_item.
    def visitConstruct_item(self, ctx:SysVerilogHDLParser.Construct_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_component_item.
    def visitAttr_component_item(self, ctx:SysVerilogHDLParser.Attr_component_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#component_item.
    def visitComponent_item(self, ctx:SysVerilogHDLParser.Component_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#compiler_item.
    def visitCompiler_item(self, ctx:SysVerilogHDLParser.Compiler_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#type_item.
    def visitType_item(self, ctx:SysVerilogHDLParser.Type_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#null_item.
    def visitNull_item(self, ctx:SysVerilogHDLParser.Null_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_interface_parameters.
    def visitList_of_interface_parameters(self, ctx:SysVerilogHDLParser.List_of_interface_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_parameter_declarations.
    def visitList_of_parameter_declarations(self, ctx:SysVerilogHDLParser.List_of_parameter_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_parameter_declaration_star.
    def visitComma_parameter_declaration_star(self, ctx:SysVerilogHDLParser.Comma_parameter_declaration_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_parameter_declaration.
    def visitComma_parameter_declaration(self, ctx:SysVerilogHDLParser.Comma_parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_parameter_descriptions.
    def visitList_of_parameter_descriptions(self, ctx:SysVerilogHDLParser.List_of_parameter_descriptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#param_declaration.
    def visitParam_declaration(self, ctx:SysVerilogHDLParser.Param_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#param_description.
    def visitParam_description(self, ctx:SysVerilogHDLParser.Param_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:SysVerilogHDLParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#local_parameter_declaration.
    def visitLocal_parameter_declaration(self, ctx:SysVerilogHDLParser.Local_parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#parameter_override.
    def visitParameter_override(self, ctx:SysVerilogHDLParser.Parameter_overrideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_tf_interface_ports.
    def visitList_of_tf_interface_ports(self, ctx:SysVerilogHDLParser.List_of_tf_interface_portsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_tf_port_declarations.
    def visitList_of_tf_port_declarations(self, ctx:SysVerilogHDLParser.List_of_tf_port_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_tf_port_declarations_comma.
    def visitList_of_tf_port_declarations_comma(self, ctx:SysVerilogHDLParser.List_of_tf_port_declarations_commaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_attr_tf_port_declaration_star.
    def visitComma_attr_tf_port_declaration_star(self, ctx:SysVerilogHDLParser.Comma_attr_tf_port_declaration_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_attr_tf_port_declaration.
    def visitComma_attr_tf_port_declaration(self, ctx:SysVerilogHDLParser.Comma_attr_tf_port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_tf_port_declarations_semicolon.
    def visitList_of_tf_port_declarations_semicolon(self, ctx:SysVerilogHDLParser.List_of_tf_port_declarations_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_tf_port_declaration_semicolon_plus.
    def visitAttr_tf_port_declaration_semicolon_plus(self, ctx:SysVerilogHDLParser.Attr_tf_port_declaration_semicolon_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_tf_port_declaration_semicolon_star.
    def visitAttr_tf_port_declaration_semicolon_star(self, ctx:SysVerilogHDLParser.Attr_tf_port_declaration_semicolon_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_tf_port_declaration_semicolon.
    def visitAttr_tf_port_declaration_semicolon(self, ctx:SysVerilogHDLParser.Attr_tf_port_declaration_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_tf_port_declaration.
    def visitAttr_tf_port_declaration(self, ctx:SysVerilogHDLParser.Attr_tf_port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#tf_port_declaration.
    def visitTf_port_declaration(self, ctx:SysVerilogHDLParser.Tf_port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_interface_ports.
    def visitList_of_interface_ports(self, ctx:SysVerilogHDLParser.List_of_interface_portsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_port_identifiers.
    def visitList_of_port_identifiers(self, ctx:SysVerilogHDLParser.List_of_port_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_port_identifier_star.
    def visitComma_port_identifier_star(self, ctx:SysVerilogHDLParser.Comma_port_identifier_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_port_identifier.
    def visitComma_port_identifier(self, ctx:SysVerilogHDLParser.Comma_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#port_identifier.
    def visitPort_identifier(self, ctx:SysVerilogHDLParser.Port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_port_declarations.
    def visitList_of_port_declarations(self, ctx:SysVerilogHDLParser.List_of_port_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_port_declarations_comma.
    def visitList_of_port_declarations_comma(self, ctx:SysVerilogHDLParser.List_of_port_declarations_commaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_attr_port_declaration_star.
    def visitComma_attr_port_declaration_star(self, ctx:SysVerilogHDLParser.Comma_attr_port_declaration_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_attr_port_declaration.
    def visitComma_attr_port_declaration(self, ctx:SysVerilogHDLParser.Comma_attr_port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_port_declarations_semicolon.
    def visitList_of_port_declarations_semicolon(self, ctx:SysVerilogHDLParser.List_of_port_declarations_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_port_declaration_semicolon_plus.
    def visitAttr_port_declaration_semicolon_plus(self, ctx:SysVerilogHDLParser.Attr_port_declaration_semicolon_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_port_declaration_semicolon_star.
    def visitAttr_port_declaration_semicolon_star(self, ctx:SysVerilogHDLParser.Attr_port_declaration_semicolon_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_port_declaration_semicolon.
    def visitAttr_port_declaration_semicolon(self, ctx:SysVerilogHDLParser.Attr_port_declaration_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_port_declaration.
    def visitAttr_port_declaration(self, ctx:SysVerilogHDLParser.Attr_port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#port_declaration.
    def visitPort_declaration(self, ctx:SysVerilogHDLParser.Port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#port_description.
    def visitPort_description(self, ctx:SysVerilogHDLParser.Port_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#inout_description.
    def visitInout_description(self, ctx:SysVerilogHDLParser.Inout_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#input_description.
    def visitInput_description(self, ctx:SysVerilogHDLParser.Input_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#output_description.
    def visitOutput_description(self, ctx:SysVerilogHDLParser.Output_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#ref_description.
    def visitRef_description(self, ctx:SysVerilogHDLParser.Ref_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#tf_declaration.
    def visitTf_declaration(self, ctx:SysVerilogHDLParser.Tf_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#inout_declaration.
    def visitInout_declaration(self, ctx:SysVerilogHDLParser.Inout_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#input_declaration.
    def visitInput_declaration(self, ctx:SysVerilogHDLParser.Input_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#output_declaration.
    def visitOutput_declaration(self, ctx:SysVerilogHDLParser.Output_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#ref_declaration.
    def visitRef_declaration(self, ctx:SysVerilogHDLParser.Ref_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#user_type.
    def visitUser_type(self, ctx:SysVerilogHDLParser.User_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#user_type_identifer.
    def visitUser_type_identifer(self, ctx:SysVerilogHDLParser.User_type_identiferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#dimension_plus.
    def visitDimension_plus(self, ctx:SysVerilogHDLParser.Dimension_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#dimension_star.
    def visitDimension_star(self, ctx:SysVerilogHDLParser.Dimension_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#dimension.
    def visitDimension(self, ctx:SysVerilogHDLParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#range_expression.
    def visitRange_expression(self, ctx:SysVerilogHDLParser.Range_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#index_expression.
    def visitIndex_expression(self, ctx:SysVerilogHDLParser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#sb_range.
    def visitSb_range(self, ctx:SysVerilogHDLParser.Sb_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#base_increment_range.
    def visitBase_increment_range(self, ctx:SysVerilogHDLParser.Base_increment_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#base_decrement_range.
    def visitBase_decrement_range(self, ctx:SysVerilogHDLParser.Base_decrement_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#base_expression.
    def visitBase_expression(self, ctx:SysVerilogHDLParser.Base_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#net_type.
    def visitNet_type(self, ctx:SysVerilogHDLParser.Net_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#drive_strength.
    def visitDrive_strength(self, ctx:SysVerilogHDLParser.Drive_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#drive_strength_value_0.
    def visitDrive_strength_value_0(self, ctx:SysVerilogHDLParser.Drive_strength_value_0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#drive_strength_value_1.
    def visitDrive_strength_value_1(self, ctx:SysVerilogHDLParser.Drive_strength_value_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#strength0.
    def visitStrength0(self, ctx:SysVerilogHDLParser.Strength0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#strength1.
    def visitStrength1(self, ctx:SysVerilogHDLParser.Strength1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#highz0.
    def visitHighz0(self, ctx:SysVerilogHDLParser.Highz0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#highz1.
    def visitHighz1(self, ctx:SysVerilogHDLParser.Highz1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#charge_strength.
    def visitCharge_strength(self, ctx:SysVerilogHDLParser.Charge_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#charge_size.
    def visitCharge_size(self, ctx:SysVerilogHDLParser.Charge_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_variable_descriptions.
    def visitList_of_variable_descriptions(self, ctx:SysVerilogHDLParser.List_of_variable_descriptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_variable_description_star.
    def visitComma_variable_description_star(self, ctx:SysVerilogHDLParser.Comma_variable_description_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_variable_description.
    def visitComma_variable_description(self, ctx:SysVerilogHDLParser.Comma_variable_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#variable_description.
    def visitVariable_description(self, ctx:SysVerilogHDLParser.Variable_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#variable_identifier.
    def visitVariable_identifier(self, ctx:SysVerilogHDLParser.Variable_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_hierarchical_variable_descriptions.
    def visitList_of_hierarchical_variable_descriptions(self, ctx:SysVerilogHDLParser.List_of_hierarchical_variable_descriptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_hierarchical_variable_description_star.
    def visitComma_hierarchical_variable_description_star(self, ctx:SysVerilogHDLParser.Comma_hierarchical_variable_description_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_hierarchical_variable_description.
    def visitComma_hierarchical_variable_description(self, ctx:SysVerilogHDLParser.Comma_hierarchical_variable_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#hierarchical_variable_description.
    def visitHierarchical_variable_description(self, ctx:SysVerilogHDLParser.Hierarchical_variable_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#hierarchical_variable_identifier.
    def visitHierarchical_variable_identifier(self, ctx:SysVerilogHDLParser.Hierarchical_variable_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#net_declaration.
    def visitNet_declaration(self, ctx:SysVerilogHDLParser.Net_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#reg_declaration.
    def visitReg_declaration(self, ctx:SysVerilogHDLParser.Reg_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#logic_declaration.
    def visitLogic_declaration(self, ctx:SysVerilogHDLParser.Logic_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#bits_type.
    def visitBits_type(self, ctx:SysVerilogHDLParser.Bits_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#bits_declaration.
    def visitBits_declaration(self, ctx:SysVerilogHDLParser.Bits_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#integer_declaration.
    def visitInteger_declaration(self, ctx:SysVerilogHDLParser.Integer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#int_declaration.
    def visitInt_declaration(self, ctx:SysVerilogHDLParser.Int_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#real_declaration.
    def visitReal_declaration(self, ctx:SysVerilogHDLParser.Real_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#time_declaration.
    def visitTime_declaration(self, ctx:SysVerilogHDLParser.Time_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#realtime_declaration.
    def visitRealtime_declaration(self, ctx:SysVerilogHDLParser.Realtime_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#event_declaration.
    def visitEvent_declaration(self, ctx:SysVerilogHDLParser.Event_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#genvar_declaration.
    def visitGenvar_declaration(self, ctx:SysVerilogHDLParser.Genvar_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#usertype_variable_declaration.
    def visitUsertype_variable_declaration(self, ctx:SysVerilogHDLParser.Usertype_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#string_declaration.
    def visitString_declaration(self, ctx:SysVerilogHDLParser.String_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#struct_declaration.
    def visitStruct_declaration(self, ctx:SysVerilogHDLParser.Struct_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#enum_declaration.
    def visitEnum_declaration(self, ctx:SysVerilogHDLParser.Enum_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#function_declaration.
    def visitFunction_declaration(self, ctx:SysVerilogHDLParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#function_type.
    def visitFunction_type(self, ctx:SysVerilogHDLParser.Function_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#function_identifier.
    def visitFunction_identifier(self, ctx:SysVerilogHDLParser.Function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#function_interface.
    def visitFunction_interface(self, ctx:SysVerilogHDLParser.Function_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#function_item_declaration_star.
    def visitFunction_item_declaration_star(self, ctx:SysVerilogHDLParser.Function_item_declaration_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#function_item_declaration_semicolon.
    def visitFunction_item_declaration_semicolon(self, ctx:SysVerilogHDLParser.Function_item_declaration_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#function_item_declaration.
    def visitFunction_item_declaration(self, ctx:SysVerilogHDLParser.Function_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#function_statement.
    def visitFunction_statement(self, ctx:SysVerilogHDLParser.Function_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#colon_function_identifier.
    def visitColon_function_identifier(self, ctx:SysVerilogHDLParser.Colon_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#task_declaration.
    def visitTask_declaration(self, ctx:SysVerilogHDLParser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#task_identifier.
    def visitTask_identifier(self, ctx:SysVerilogHDLParser.Task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#task_interface.
    def visitTask_interface(self, ctx:SysVerilogHDLParser.Task_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#task_item_declaration_semicolon.
    def visitTask_item_declaration_semicolon(self, ctx:SysVerilogHDLParser.Task_item_declaration_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#task_item_declaration.
    def visitTask_item_declaration(self, ctx:SysVerilogHDLParser.Task_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#task_item_declaration_star.
    def visitTask_item_declaration_star(self, ctx:SysVerilogHDLParser.Task_item_declaration_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#task_statement.
    def visitTask_statement(self, ctx:SysVerilogHDLParser.Task_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#struct_item_semicolon.
    def visitStruct_item_semicolon(self, ctx:SysVerilogHDLParser.Struct_item_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#struct_item_star.
    def visitStruct_item_star(self, ctx:SysVerilogHDLParser.Struct_item_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#struct_item.
    def visitStruct_item(self, ctx:SysVerilogHDLParser.Struct_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#struct_type.
    def visitStruct_type(self, ctx:SysVerilogHDLParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#enum_type.
    def visitEnum_type(self, ctx:SysVerilogHDLParser.Enum_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_enum_items.
    def visitList_of_enum_items(self, ctx:SysVerilogHDLParser.List_of_enum_itemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#enum_item.
    def visitEnum_item(self, ctx:SysVerilogHDLParser.Enum_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#enum_identifier.
    def visitEnum_identifier(self, ctx:SysVerilogHDLParser.Enum_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_enum_item_star.
    def visitComma_enum_item_star(self, ctx:SysVerilogHDLParser.Comma_enum_item_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_enum_item.
    def visitComma_enum_item(self, ctx:SysVerilogHDLParser.Comma_enum_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#enumerated_type.
    def visitEnumerated_type(self, ctx:SysVerilogHDLParser.Enumerated_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#module_instantiation.
    def visitModule_instantiation(self, ctx:SysVerilogHDLParser.Module_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#parameter_interface_assignments.
    def visitParameter_interface_assignments(self, ctx:SysVerilogHDLParser.Parameter_interface_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_interface_assignments.
    def visitList_of_interface_assignments(self, ctx:SysVerilogHDLParser.List_of_interface_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_ordered_interface_assignments.
    def visitList_of_ordered_interface_assignments(self, ctx:SysVerilogHDLParser.List_of_ordered_interface_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_ordered_interface_assignment_star.
    def visitComma_ordered_interface_assignment_star(self, ctx:SysVerilogHDLParser.Comma_ordered_interface_assignment_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_ordered_interface_assignment.
    def visitComma_ordered_interface_assignment(self, ctx:SysVerilogHDLParser.Comma_ordered_interface_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#ordered_interface_assignment.
    def visitOrdered_interface_assignment(self, ctx:SysVerilogHDLParser.Ordered_interface_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_named_interface_assignments.
    def visitList_of_named_interface_assignments(self, ctx:SysVerilogHDLParser.List_of_named_interface_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_named_interface_assignment_star.
    def visitComma_named_interface_assignment_star(self, ctx:SysVerilogHDLParser.Comma_named_interface_assignment_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_named_interface_assignment.
    def visitComma_named_interface_assignment(self, ctx:SysVerilogHDLParser.Comma_named_interface_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#named_interface_assignment.
    def visitNamed_interface_assignment(self, ctx:SysVerilogHDLParser.Named_interface_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_module_instances.
    def visitList_of_module_instances(self, ctx:SysVerilogHDLParser.List_of_module_instancesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_module_instance_star.
    def visitComma_module_instance_star(self, ctx:SysVerilogHDLParser.Comma_module_instance_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_module_instance.
    def visitComma_module_instance(self, ctx:SysVerilogHDLParser.Comma_module_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#module_instance.
    def visitModule_instance(self, ctx:SysVerilogHDLParser.Module_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#module_instance_identifier.
    def visitModule_instance_identifier(self, ctx:SysVerilogHDLParser.Module_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#arrayed_identifier.
    def visitArrayed_identifier(self, ctx:SysVerilogHDLParser.Arrayed_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#simple_arrayed_identifier.
    def visitSimple_arrayed_identifier(self, ctx:SysVerilogHDLParser.Simple_arrayed_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#escaped_arrayed_identifier.
    def visitEscaped_arrayed_identifier(self, ctx:SysVerilogHDLParser.Escaped_arrayed_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#port_interface_assignments.
    def visitPort_interface_assignments(self, ctx:SysVerilogHDLParser.Port_interface_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#delay.
    def visitDelay(self, ctx:SysVerilogHDLParser.DelayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_delay_values.
    def visitList_of_delay_values(self, ctx:SysVerilogHDLParser.List_of_delay_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_delay_value_star.
    def visitComma_delay_value_star(self, ctx:SysVerilogHDLParser.Comma_delay_value_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_delay_value.
    def visitComma_delay_value(self, ctx:SysVerilogHDLParser.Comma_delay_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#delay_value.
    def visitDelay_value(self, ctx:SysVerilogHDLParser.Delay_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pulldown_strength.
    def visitPulldown_strength(self, ctx:SysVerilogHDLParser.Pulldown_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pullup_strength.
    def visitPullup_strength(self, ctx:SysVerilogHDLParser.Pullup_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#gate_instance_identifier.
    def visitGate_instance_identifier(self, ctx:SysVerilogHDLParser.Gate_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#gate_instantiation.
    def visitGate_instantiation(self, ctx:SysVerilogHDLParser.Gate_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#enable_gatetype.
    def visitEnable_gatetype(self, ctx:SysVerilogHDLParser.Enable_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#mos_switchtype.
    def visitMos_switchtype(self, ctx:SysVerilogHDLParser.Mos_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#cmos_switchtype.
    def visitCmos_switchtype(self, ctx:SysVerilogHDLParser.Cmos_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#n_output_gatetype.
    def visitN_output_gatetype(self, ctx:SysVerilogHDLParser.N_output_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#n_input_gatetype.
    def visitN_input_gatetype(self, ctx:SysVerilogHDLParser.N_input_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pass_switchtype.
    def visitPass_switchtype(self, ctx:SysVerilogHDLParser.Pass_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pass_enable_switchtype.
    def visitPass_enable_switchtype(self, ctx:SysVerilogHDLParser.Pass_enable_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pulldown_instantiation.
    def visitPulldown_instantiation(self, ctx:SysVerilogHDLParser.Pulldown_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pullup_instantiation.
    def visitPullup_instantiation(self, ctx:SysVerilogHDLParser.Pullup_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#enable_instantiation.
    def visitEnable_instantiation(self, ctx:SysVerilogHDLParser.Enable_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#mos_instantiation.
    def visitMos_instantiation(self, ctx:SysVerilogHDLParser.Mos_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#cmos_instantiation.
    def visitCmos_instantiation(self, ctx:SysVerilogHDLParser.Cmos_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#n_output_instantiation.
    def visitN_output_instantiation(self, ctx:SysVerilogHDLParser.N_output_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#n_input_instantiation.
    def visitN_input_instantiation(self, ctx:SysVerilogHDLParser.N_input_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pass_instantiation.
    def visitPass_instantiation(self, ctx:SysVerilogHDLParser.Pass_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pass_enable_instantiation.
    def visitPass_enable_instantiation(self, ctx:SysVerilogHDLParser.Pass_enable_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_pull_gate_instance.
    def visitList_of_pull_gate_instance(self, ctx:SysVerilogHDLParser.List_of_pull_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_enable_gate_instance.
    def visitList_of_enable_gate_instance(self, ctx:SysVerilogHDLParser.List_of_enable_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_mos_switch_instance.
    def visitList_of_mos_switch_instance(self, ctx:SysVerilogHDLParser.List_of_mos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_cmos_switch_instance.
    def visitList_of_cmos_switch_instance(self, ctx:SysVerilogHDLParser.List_of_cmos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_n_input_gate_instance.
    def visitList_of_n_input_gate_instance(self, ctx:SysVerilogHDLParser.List_of_n_input_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_n_output_gate_instance.
    def visitList_of_n_output_gate_instance(self, ctx:SysVerilogHDLParser.List_of_n_output_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_pass_switch_instance.
    def visitList_of_pass_switch_instance(self, ctx:SysVerilogHDLParser.List_of_pass_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_pass_enable_switch_instance.
    def visitList_of_pass_enable_switch_instance(self, ctx:SysVerilogHDLParser.List_of_pass_enable_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_pull_gate_instance_star.
    def visitComma_pull_gate_instance_star(self, ctx:SysVerilogHDLParser.Comma_pull_gate_instance_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_enable_gate_instance_star.
    def visitComma_enable_gate_instance_star(self, ctx:SysVerilogHDLParser.Comma_enable_gate_instance_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_mos_switch_instance_star.
    def visitComma_mos_switch_instance_star(self, ctx:SysVerilogHDLParser.Comma_mos_switch_instance_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_cmos_switch_instance_star.
    def visitComma_cmos_switch_instance_star(self, ctx:SysVerilogHDLParser.Comma_cmos_switch_instance_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_n_input_gate_instance_star.
    def visitComma_n_input_gate_instance_star(self, ctx:SysVerilogHDLParser.Comma_n_input_gate_instance_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_n_output_gate_instance_star.
    def visitComma_n_output_gate_instance_star(self, ctx:SysVerilogHDLParser.Comma_n_output_gate_instance_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_pass_switch_instance_star.
    def visitComma_pass_switch_instance_star(self, ctx:SysVerilogHDLParser.Comma_pass_switch_instance_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_pass_enable_switch_instance_star.
    def visitComma_pass_enable_switch_instance_star(self, ctx:SysVerilogHDLParser.Comma_pass_enable_switch_instance_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_pull_gate_instance.
    def visitComma_pull_gate_instance(self, ctx:SysVerilogHDLParser.Comma_pull_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_enable_gate_instance.
    def visitComma_enable_gate_instance(self, ctx:SysVerilogHDLParser.Comma_enable_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_mos_switch_instance.
    def visitComma_mos_switch_instance(self, ctx:SysVerilogHDLParser.Comma_mos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_cmos_switch_instance.
    def visitComma_cmos_switch_instance(self, ctx:SysVerilogHDLParser.Comma_cmos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_n_input_gate_instance.
    def visitComma_n_input_gate_instance(self, ctx:SysVerilogHDLParser.Comma_n_input_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_n_output_gate_instance.
    def visitComma_n_output_gate_instance(self, ctx:SysVerilogHDLParser.Comma_n_output_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_pass_switch_instance.
    def visitComma_pass_switch_instance(self, ctx:SysVerilogHDLParser.Comma_pass_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_pass_enable_switch_instance.
    def visitComma_pass_enable_switch_instance(self, ctx:SysVerilogHDLParser.Comma_pass_enable_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pull_gate_instance.
    def visitPull_gate_instance(self, ctx:SysVerilogHDLParser.Pull_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#enable_gate_instance.
    def visitEnable_gate_instance(self, ctx:SysVerilogHDLParser.Enable_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#mos_switch_instance.
    def visitMos_switch_instance(self, ctx:SysVerilogHDLParser.Mos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#cmos_switch_instance.
    def visitCmos_switch_instance(self, ctx:SysVerilogHDLParser.Cmos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#n_input_gate_instance.
    def visitN_input_gate_instance(self, ctx:SysVerilogHDLParser.N_input_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#n_output_gate_instance.
    def visitN_output_gate_instance(self, ctx:SysVerilogHDLParser.N_output_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pass_switch_instance.
    def visitPass_switch_instance(self, ctx:SysVerilogHDLParser.Pass_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pass_enable_switch_instance.
    def visitPass_enable_switch_instance(self, ctx:SysVerilogHDLParser.Pass_enable_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pull_gate_interface.
    def visitPull_gate_interface(self, ctx:SysVerilogHDLParser.Pull_gate_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#enable_gate_interface.
    def visitEnable_gate_interface(self, ctx:SysVerilogHDLParser.Enable_gate_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#mos_switch_interface.
    def visitMos_switch_interface(self, ctx:SysVerilogHDLParser.Mos_switch_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#cmos_switch_interface.
    def visitCmos_switch_interface(self, ctx:SysVerilogHDLParser.Cmos_switch_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#n_input_gate_interface.
    def visitN_input_gate_interface(self, ctx:SysVerilogHDLParser.N_input_gate_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#n_output_gate_interface.
    def visitN_output_gate_interface(self, ctx:SysVerilogHDLParser.N_output_gate_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pass_switch_interface.
    def visitPass_switch_interface(self, ctx:SysVerilogHDLParser.Pass_switch_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pass_enable_switch_interface.
    def visitPass_enable_switch_interface(self, ctx:SysVerilogHDLParser.Pass_enable_switch_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_input_terminals.
    def visitList_of_input_terminals(self, ctx:SysVerilogHDLParser.List_of_input_terminalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_output_terminals.
    def visitList_of_output_terminals(self, ctx:SysVerilogHDLParser.List_of_output_terminalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_input_terminal_star.
    def visitComma_input_terminal_star(self, ctx:SysVerilogHDLParser.Comma_input_terminal_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_output_terminal_star.
    def visitComma_output_terminal_star(self, ctx:SysVerilogHDLParser.Comma_output_terminal_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_input_terminal.
    def visitComma_input_terminal(self, ctx:SysVerilogHDLParser.Comma_input_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_output_terminal.
    def visitComma_output_terminal(self, ctx:SysVerilogHDLParser.Comma_output_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#enable_terminal.
    def visitEnable_terminal(self, ctx:SysVerilogHDLParser.Enable_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#input_terminal.
    def visitInput_terminal(self, ctx:SysVerilogHDLParser.Input_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#inout_terminal.
    def visitInout_terminal(self, ctx:SysVerilogHDLParser.Inout_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#ncontrol_terminal.
    def visitNcontrol_terminal(self, ctx:SysVerilogHDLParser.Ncontrol_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#output_terminal.
    def visitOutput_terminal(self, ctx:SysVerilogHDLParser.Output_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#pcontrol_terminal.
    def visitPcontrol_terminal(self, ctx:SysVerilogHDLParser.Pcontrol_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#statement_star.
    def visitStatement_star(self, ctx:SysVerilogHDLParser.Statement_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#statement_semicolon.
    def visitStatement_semicolon(self, ctx:SysVerilogHDLParser.Statement_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#statement.
    def visitStatement(self, ctx:SysVerilogHDLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#assignment_statement.
    def visitAssignment_statement(self, ctx:SysVerilogHDLParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#flow_control_statement.
    def visitFlow_control_statement(self, ctx:SysVerilogHDLParser.Flow_control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#block_statement.
    def visitBlock_statement(self, ctx:SysVerilogHDLParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#task_call_statement.
    def visitTask_call_statement(self, ctx:SysVerilogHDLParser.Task_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#event_statement.
    def visitEvent_statement(self, ctx:SysVerilogHDLParser.Event_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#procedural_statement.
    def visitProcedural_statement(self, ctx:SysVerilogHDLParser.Procedural_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#expression_statement.
    def visitExpression_statement(self, ctx:SysVerilogHDLParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#subroutine_statement.
    def visitSubroutine_statement(self, ctx:SysVerilogHDLParser.Subroutine_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#return_statement.
    def visitReturn_statement(self, ctx:SysVerilogHDLParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#null_statement.
    def visitNull_statement(self, ctx:SysVerilogHDLParser.Null_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#procedural_continuous_assignments.
    def visitProcedural_continuous_assignments(self, ctx:SysVerilogHDLParser.Procedural_continuous_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#assign_statement.
    def visitAssign_statement(self, ctx:SysVerilogHDLParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#deassign_statement.
    def visitDeassign_statement(self, ctx:SysVerilogHDLParser.Deassign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#force_statement.
    def visitForce_statement(self, ctx:SysVerilogHDLParser.Force_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#release_statement.
    def visitRelease_statement(self, ctx:SysVerilogHDLParser.Release_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#procedural_timing_control_statement.
    def visitProcedural_timing_control_statement(self, ctx:SysVerilogHDLParser.Procedural_timing_control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#property_statement.
    def visitProperty_statement(self, ctx:SysVerilogHDLParser.Property_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#disable_condition_statement.
    def visitDisable_condition_statement(self, ctx:SysVerilogHDLParser.Disable_condition_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#property_expression.
    def visitProperty_expression(self, ctx:SysVerilogHDLParser.Property_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#procedural_assertion_statement.
    def visitProcedural_assertion_statement(self, ctx:SysVerilogHDLParser.Procedural_assertion_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#assert_else_statement.
    def visitAssert_else_statement(self, ctx:SysVerilogHDLParser.Assert_else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#assert_statement.
    def visitAssert_statement(self, ctx:SysVerilogHDLParser.Assert_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#system_task_enable.
    def visitSystem_task_enable(self, ctx:SysVerilogHDLParser.System_task_enableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#system_task_identifier.
    def visitSystem_task_identifier(self, ctx:SysVerilogHDLParser.System_task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#task_interface_assignments.
    def visitTask_interface_assignments(self, ctx:SysVerilogHDLParser.Task_interface_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#task_enable.
    def visitTask_enable(self, ctx:SysVerilogHDLParser.Task_enableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#hierarchical_task_identifier.
    def visitHierarchical_task_identifier(self, ctx:SysVerilogHDLParser.Hierarchical_task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#disable_statement.
    def visitDisable_statement(self, ctx:SysVerilogHDLParser.Disable_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#hierarchical_block_identifier.
    def visitHierarchical_block_identifier(self, ctx:SysVerilogHDLParser.Hierarchical_block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#variable_lvalue.
    def visitVariable_lvalue(self, ctx:SysVerilogHDLParser.Variable_lvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#hierarchical_variable_lvalue.
    def visitHierarchical_variable_lvalue(self, ctx:SysVerilogHDLParser.Hierarchical_variable_lvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#variable_concatenation.
    def visitVariable_concatenation(self, ctx:SysVerilogHDLParser.Variable_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#variable_concatenation_value.
    def visitVariable_concatenation_value(self, ctx:SysVerilogHDLParser.Variable_concatenation_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_vcv_star.
    def visitComma_vcv_star(self, ctx:SysVerilogHDLParser.Comma_vcv_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#blocking_assignment.
    def visitBlocking_assignment(self, ctx:SysVerilogHDLParser.Blocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#nonblocking_assignment.
    def visitNonblocking_assignment(self, ctx:SysVerilogHDLParser.Nonblocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#prefix_assignment.
    def visitPrefix_assignment(self, ctx:SysVerilogHDLParser.Prefix_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#postfix_assignment.
    def visitPostfix_assignment(self, ctx:SysVerilogHDLParser.Postfix_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#operator_assignment.
    def visitOperator_assignment(self, ctx:SysVerilogHDLParser.Operator_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#declarative_assignment.
    def visitDeclarative_assignment(self, ctx:SysVerilogHDLParser.Declarative_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#delay_or_event_control.
    def visitDelay_or_event_control(self, ctx:SysVerilogHDLParser.Delay_or_event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#delay_control.
    def visitDelay_control(self, ctx:SysVerilogHDLParser.Delay_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#event_control.
    def visitEvent_control(self, ctx:SysVerilogHDLParser.Event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#event_control_identifier.
    def visitEvent_control_identifier(self, ctx:SysVerilogHDLParser.Event_control_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#event_control_expression.
    def visitEvent_control_expression(self, ctx:SysVerilogHDLParser.Event_control_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#event_expression.
    def visitEvent_expression(self, ctx:SysVerilogHDLParser.Event_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#single_event_expression.
    def visitSingle_event_expression(self, ctx:SysVerilogHDLParser.Single_event_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#event_expression_edgespec.
    def visitEvent_expression_edgespec(self, ctx:SysVerilogHDLParser.Event_expression_edgespecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#event_expression_or.
    def visitEvent_expression_or(self, ctx:SysVerilogHDLParser.Event_expression_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_event_expression_comma.
    def visitList_of_event_expression_comma(self, ctx:SysVerilogHDLParser.List_of_event_expression_commaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_event_expression_star.
    def visitComma_event_expression_star(self, ctx:SysVerilogHDLParser.Comma_event_expression_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_event_expression.
    def visitComma_event_expression(self, ctx:SysVerilogHDLParser.Comma_event_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_event_expression_or.
    def visitList_of_event_expression_or(self, ctx:SysVerilogHDLParser.List_of_event_expression_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#or_event_expression_star.
    def visitOr_event_expression_star(self, ctx:SysVerilogHDLParser.Or_event_expression_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#or_event_expression.
    def visitOr_event_expression(self, ctx:SysVerilogHDLParser.Or_event_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#event_control_wildcard.
    def visitEvent_control_wildcard(self, ctx:SysVerilogHDLParser.Event_control_wildcardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#repeat_event_control.
    def visitRepeat_event_control(self, ctx:SysVerilogHDLParser.Repeat_event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#event_trigger.
    def visitEvent_trigger(self, ctx:SysVerilogHDLParser.Event_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#hierarchical_event_identifier.
    def visitHierarchical_event_identifier(self, ctx:SysVerilogHDLParser.Hierarchical_event_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#event_identifier.
    def visitEvent_identifier(self, ctx:SysVerilogHDLParser.Event_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#wait_statement.
    def visitWait_statement(self, ctx:SysVerilogHDLParser.Wait_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_generated_instantiation.
    def visitAttr_generated_instantiation(self, ctx:SysVerilogHDLParser.Attr_generated_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generated_instantiation.
    def visitGenerated_instantiation(self, ctx:SysVerilogHDLParser.Generated_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_item_star.
    def visitGenerate_item_star(self, ctx:SysVerilogHDLParser.Generate_item_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_item.
    def visitGenerate_item(self, ctx:SysVerilogHDLParser.Generate_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_block.
    def visitGenerate_block(self, ctx:SysVerilogHDLParser.Generate_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_colon_block_identifier0.
    def visitGenerate_colon_block_identifier0(self, ctx:SysVerilogHDLParser.Generate_colon_block_identifier0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_colon_block_identifier1.
    def visitGenerate_colon_block_identifier1(self, ctx:SysVerilogHDLParser.Generate_colon_block_identifier1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_colon_block_identifier.
    def visitGenerate_colon_block_identifier(self, ctx:SysVerilogHDLParser.Generate_colon_block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_block_identifier.
    def visitGenerate_block_identifier(self, ctx:SysVerilogHDLParser.Generate_block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_conditional_statement.
    def visitGenerate_conditional_statement(self, ctx:SysVerilogHDLParser.Generate_conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_if_statement.
    def visitGenerate_if_statement(self, ctx:SysVerilogHDLParser.Generate_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_else_statement.
    def visitGenerate_else_statement(self, ctx:SysVerilogHDLParser.Generate_else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_loop_statement.
    def visitGenerate_loop_statement(self, ctx:SysVerilogHDLParser.Generate_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_forever_loop_statement.
    def visitGenerate_forever_loop_statement(self, ctx:SysVerilogHDLParser.Generate_forever_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_repeat_loop_statement.
    def visitGenerate_repeat_loop_statement(self, ctx:SysVerilogHDLParser.Generate_repeat_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_while_loop_statement.
    def visitGenerate_while_loop_statement(self, ctx:SysVerilogHDLParser.Generate_while_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_do_loop_statement.
    def visitGenerate_do_loop_statement(self, ctx:SysVerilogHDLParser.Generate_do_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_for_loop_statement.
    def visitGenerate_for_loop_statement(self, ctx:SysVerilogHDLParser.Generate_for_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_case_statement.
    def visitGenerate_case_statement(self, ctx:SysVerilogHDLParser.Generate_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_case_item_star.
    def visitGenerate_case_item_star(self, ctx:SysVerilogHDLParser.Generate_case_item_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#generate_case_item.
    def visitGenerate_case_item(self, ctx:SysVerilogHDLParser.Generate_case_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#conditional_statement.
    def visitConditional_statement(self, ctx:SysVerilogHDLParser.Conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#if_statement.
    def visitIf_statement(self, ctx:SysVerilogHDLParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#else_statement.
    def visitElse_statement(self, ctx:SysVerilogHDLParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#conditional_expression.
    def visitConditional_expression(self, ctx:SysVerilogHDLParser.Conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#loop_statement.
    def visitLoop_statement(self, ctx:SysVerilogHDLParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#forever_loop_statement.
    def visitForever_loop_statement(self, ctx:SysVerilogHDLParser.Forever_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#repeat_loop_statement.
    def visitRepeat_loop_statement(self, ctx:SysVerilogHDLParser.Repeat_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#while_loop_statement.
    def visitWhile_loop_statement(self, ctx:SysVerilogHDLParser.While_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#do_loop_statement.
    def visitDo_loop_statement(self, ctx:SysVerilogHDLParser.Do_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#for_loop_statement.
    def visitFor_loop_statement(self, ctx:SysVerilogHDLParser.For_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#loop_init_assignment.
    def visitLoop_init_assignment(self, ctx:SysVerilogHDLParser.Loop_init_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#loop_terminate_expression.
    def visitLoop_terminate_expression(self, ctx:SysVerilogHDLParser.Loop_terminate_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#loop_step_assignment.
    def visitLoop_step_assignment(self, ctx:SysVerilogHDLParser.Loop_step_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#case_statement.
    def visitCase_statement(self, ctx:SysVerilogHDLParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#case_item_star.
    def visitCase_item_star(self, ctx:SysVerilogHDLParser.Case_item_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#case_item.
    def visitCase_item(self, ctx:SysVerilogHDLParser.Case_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#case_switch.
    def visitCase_switch(self, ctx:SysVerilogHDLParser.Case_switchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#case_item_key.
    def visitCase_item_key(self, ctx:SysVerilogHDLParser.Case_item_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#case_item_key_expression.
    def visitCase_item_key_expression(self, ctx:SysVerilogHDLParser.Case_item_key_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_case_item_key_expression.
    def visitComma_case_item_key_expression(self, ctx:SysVerilogHDLParser.Comma_case_item_key_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_case_item_key_expression_star.
    def visitComma_case_item_key_expression_star(self, ctx:SysVerilogHDLParser.Comma_case_item_key_expression_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#expression.
    def visitExpression(self, ctx:SysVerilogHDLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#single_expression.
    def visitSingle_expression(self, ctx:SysVerilogHDLParser.Single_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#primary_range.
    def visitPrimary_range(self, ctx:SysVerilogHDLParser.Primary_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#primary.
    def visitPrimary(self, ctx:SysVerilogHDLParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#unary_expression.
    def visitUnary_expression(self, ctx:SysVerilogHDLParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#unary_post_assign_expression.
    def visitUnary_post_assign_expression(self, ctx:SysVerilogHDLParser.Unary_post_assign_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#unary_pre_assign_expression.
    def visitUnary_pre_assign_expression(self, ctx:SysVerilogHDLParser.Unary_pre_assign_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#binary_expression.
    def visitBinary_expression(self, ctx:SysVerilogHDLParser.Binary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#ternary_expression.
    def visitTernary_expression(self, ctx:SysVerilogHDLParser.Ternary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#mintypmax_expression.
    def visitMintypmax_expression(self, ctx:SysVerilogHDLParser.Mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#structured_value.
    def visitStructured_value(self, ctx:SysVerilogHDLParser.Structured_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#arrayed_structured_value.
    def visitArrayed_structured_value(self, ctx:SysVerilogHDLParser.Arrayed_structured_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#arrayed_structure_item.
    def visitArrayed_structure_item(self, ctx:SysVerilogHDLParser.Arrayed_structure_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_arrayed_structure_item.
    def visitComma_arrayed_structure_item(self, ctx:SysVerilogHDLParser.Comma_arrayed_structure_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_arrayed_structure_item_star.
    def visitComma_arrayed_structure_item_star(self, ctx:SysVerilogHDLParser.Comma_arrayed_structure_item_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#arrayed_structure_item_plus.
    def visitArrayed_structure_item_plus(self, ctx:SysVerilogHDLParser.Arrayed_structure_item_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#variable_type_cast.
    def visitVariable_type_cast(self, ctx:SysVerilogHDLParser.Variable_type_castContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#width_type_cast.
    def visitWidth_type_cast(self, ctx:SysVerilogHDLParser.Width_type_castContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#sign_type_cast.
    def visitSign_type_cast(self, ctx:SysVerilogHDLParser.Sign_type_castContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#null_type_cast.
    def visitNull_type_cast(self, ctx:SysVerilogHDLParser.Null_type_castContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#variable_type.
    def visitVariable_type(self, ctx:SysVerilogHDLParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#type_cast_identifier.
    def visitType_cast_identifier(self, ctx:SysVerilogHDLParser.Type_cast_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#type_cast_expression.
    def visitType_cast_expression(self, ctx:SysVerilogHDLParser.Type_cast_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#function_call.
    def visitFunction_call(self, ctx:SysVerilogHDLParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#hierarchical_function_identifier.
    def visitHierarchical_function_identifier(self, ctx:SysVerilogHDLParser.Hierarchical_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#function_interface_assignments.
    def visitFunction_interface_assignments(self, ctx:SysVerilogHDLParser.Function_interface_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#system_function_call.
    def visitSystem_function_call(self, ctx:SysVerilogHDLParser.System_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#system_function_identifier.
    def visitSystem_function_identifier(self, ctx:SysVerilogHDLParser.System_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#constant_function_call.
    def visitConstant_function_call(self, ctx:SysVerilogHDLParser.Constant_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#imported_function_call.
    def visitImported_function_call(self, ctx:SysVerilogHDLParser.Imported_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#imported_function_hierarchical_identifier.
    def visitImported_function_hierarchical_identifier(self, ctx:SysVerilogHDLParser.Imported_function_hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#primary_hierarchical_identifier.
    def visitPrimary_hierarchical_identifier(self, ctx:SysVerilogHDLParser.Primary_hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#primary_imported_hierarchical_identifier.
    def visitPrimary_imported_hierarchical_identifier(self, ctx:SysVerilogHDLParser.Primary_imported_hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#imported_hierarchical_identifier.
    def visitImported_hierarchical_identifier(self, ctx:SysVerilogHDLParser.Imported_hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#parenthesis_expression.
    def visitParenthesis_expression(self, ctx:SysVerilogHDLParser.Parenthesis_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#concatenation.
    def visitConcatenation(self, ctx:SysVerilogHDLParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#multiple_concatenation.
    def visitMultiple_concatenation(self, ctx:SysVerilogHDLParser.Multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_expression_plus.
    def visitComma_expression_plus(self, ctx:SysVerilogHDLParser.Comma_expression_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_expression_star.
    def visitComma_expression_star(self, ctx:SysVerilogHDLParser.Comma_expression_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#typedef_declaration.
    def visitTypedef_declaration(self, ctx:SysVerilogHDLParser.Typedef_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#typedef_identifier.
    def visitTypedef_identifier(self, ctx:SysVerilogHDLParser.Typedef_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#typedef_definition.
    def visitTypedef_definition(self, ctx:SysVerilogHDLParser.Typedef_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#typedef_definition_type.
    def visitTypedef_definition_type(self, ctx:SysVerilogHDLParser.Typedef_definition_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#complex_type.
    def visitComplex_type(self, ctx:SysVerilogHDLParser.Complex_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#typedef_type.
    def visitTypedef_type(self, ctx:SysVerilogHDLParser.Typedef_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#par_block.
    def visitPar_block(self, ctx:SysVerilogHDLParser.Par_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#seq_block.
    def visitSeq_block(self, ctx:SysVerilogHDLParser.Seq_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#block_identifier.
    def visitBlock_identifier(self, ctx:SysVerilogHDLParser.Block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#colon_block_identifier.
    def visitColon_block_identifier(self, ctx:SysVerilogHDLParser.Colon_block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#block_item_declaration_star.
    def visitBlock_item_declaration_star(self, ctx:SysVerilogHDLParser.Block_item_declaration_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#block_item_declaration_semicolon.
    def visitBlock_item_declaration_semicolon(self, ctx:SysVerilogHDLParser.Block_item_declaration_semicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#block_item_declaration.
    def visitBlock_item_declaration(self, ctx:SysVerilogHDLParser.Block_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#join_keyword.
    def visitJoin_keyword(self, ctx:SysVerilogHDLParser.Join_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#continuous_assign.
    def visitContinuous_assign(self, ctx:SysVerilogHDLParser.Continuous_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#list_of_variable_assignments.
    def visitList_of_variable_assignments(self, ctx:SysVerilogHDLParser.List_of_variable_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_variable_assignment_star.
    def visitComma_variable_assignment_star(self, ctx:SysVerilogHDLParser.Comma_variable_assignment_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#comma_variable_assignment.
    def visitComma_variable_assignment(self, ctx:SysVerilogHDLParser.Comma_variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#variable_assignment.
    def visitVariable_assignment(self, ctx:SysVerilogHDLParser.Variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#initial_construct.
    def visitInitial_construct(self, ctx:SysVerilogHDLParser.Initial_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#final_construct.
    def visitFinal_construct(self, ctx:SysVerilogHDLParser.Final_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#always_keyword.
    def visitAlways_keyword(self, ctx:SysVerilogHDLParser.Always_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#always_construct.
    def visitAlways_construct(self, ctx:SysVerilogHDLParser.Always_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attribute_instance_star.
    def visitAttribute_instance_star(self, ctx:SysVerilogHDLParser.Attribute_instance_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attribute_instance.
    def visitAttribute_instance(self, ctx:SysVerilogHDLParser.Attribute_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_spec_star.
    def visitAttr_spec_star(self, ctx:SysVerilogHDLParser.Attr_spec_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_spec.
    def visitAttr_spec(self, ctx:SysVerilogHDLParser.Attr_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#attr_name.
    def visitAttr_name(self, ctx:SysVerilogHDLParser.Attr_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#identifier.
    def visitIdentifier(self, ctx:SysVerilogHDLParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#hierarchical_identifier.
    def visitHierarchical_identifier(self, ctx:SysVerilogHDLParser.Hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#dot_hierarchical_identifier_branch_item_star.
    def visitDot_hierarchical_identifier_branch_item_star(self, ctx:SysVerilogHDLParser.Dot_hierarchical_identifier_branch_item_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#dot_hierarchical_identifier_branch_item.
    def visitDot_hierarchical_identifier_branch_item(self, ctx:SysVerilogHDLParser.Dot_hierarchical_identifier_branch_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#hierarchical_identifier_branch_item.
    def visitHierarchical_identifier_branch_item(self, ctx:SysVerilogHDLParser.Hierarchical_identifier_branch_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#timescale_compiler_directive.
    def visitTimescale_compiler_directive(self, ctx:SysVerilogHDLParser.Timescale_compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#timeunit_directive.
    def visitTimeunit_directive(self, ctx:SysVerilogHDLParser.Timeunit_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#timeprecision_directive.
    def visitTimeprecision_directive(self, ctx:SysVerilogHDLParser.Timeprecision_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#default_nettype_statement.
    def visitDefault_nettype_statement(self, ctx:SysVerilogHDLParser.Default_nettype_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#number.
    def visitNumber(self, ctx:SysVerilogHDLParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#integral_number.
    def visitIntegral_number(self, ctx:SysVerilogHDLParser.Integral_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysVerilogHDLParser#real_number.
    def visitReal_number(self, ctx:SysVerilogHDLParser.Real_numberContext):
        return self.visitChildren(ctx)



del SysVerilogHDLParser