# Generated from Verilog2001.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Verilog2001Parser import Verilog2001Parser
else:
    from Verilog2001Parser import Verilog2001Parser

# This class defines a complete generic visitor for a parse tree produced by Verilog2001Parser.

class Verilog2001Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Verilog2001Parser#config_declaration.
    def visitConfig_declaration(self, ctx:Verilog2001Parser.Config_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#design_statement.
    def visitDesign_statement(self, ctx:Verilog2001Parser.Design_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#config_rule_statement.
    def visitConfig_rule_statement(self, ctx:Verilog2001Parser.Config_rule_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#default_clause.
    def visitDefault_clause(self, ctx:Verilog2001Parser.Default_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#inst_clause.
    def visitInst_clause(self, ctx:Verilog2001Parser.Inst_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#inst_name.
    def visitInst_name(self, ctx:Verilog2001Parser.Inst_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#liblist_clause.
    def visitLiblist_clause(self, ctx:Verilog2001Parser.Liblist_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#cell_clause.
    def visitCell_clause(self, ctx:Verilog2001Parser.Cell_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#use_clause.
    def visitUse_clause(self, ctx:Verilog2001Parser.Use_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#source_text.
    def visitSource_text(self, ctx:Verilog2001Parser.Source_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#description.
    def visitDescription(self, ctx:Verilog2001Parser.DescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_declaration.
    def visitModule_declaration(self, ctx:Verilog2001Parser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_keyword.
    def visitModule_keyword(self, ctx:Verilog2001Parser.Module_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_parameter_port_list.
    def visitModule_parameter_port_list(self, ctx:Verilog2001Parser.Module_parameter_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_ports.
    def visitList_of_ports(self, ctx:Verilog2001Parser.List_of_portsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_port_declarations.
    def visitList_of_port_declarations(self, ctx:Verilog2001Parser.List_of_port_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#port.
    def visitPort(self, ctx:Verilog2001Parser.PortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#port_expression.
    def visitPort_expression(self, ctx:Verilog2001Parser.Port_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#port_reference.
    def visitPort_reference(self, ctx:Verilog2001Parser.Port_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#port_declaration.
    def visitPort_declaration(self, ctx:Verilog2001Parser.Port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_item.
    def visitModule_item(self, ctx:Verilog2001Parser.Module_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_or_generate_item.
    def visitModule_or_generate_item(self, ctx:Verilog2001Parser.Module_or_generate_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#non_port_module_item.
    def visitNon_port_module_item(self, ctx:Verilog2001Parser.Non_port_module_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_or_generate_item_declaration.
    def visitModule_or_generate_item_declaration(self, ctx:Verilog2001Parser.Module_or_generate_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#parameter_override.
    def visitParameter_override(self, ctx:Verilog2001Parser.Parameter_overrideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#local_parameter_declaration.
    def visitLocal_parameter_declaration(self, ctx:Verilog2001Parser.Local_parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#parameter_declaration.
    def visitParameter_declaration(self, ctx:Verilog2001Parser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#parameter_declaration_.
    def visitParameter_declaration_(self, ctx:Verilog2001Parser.Parameter_declaration_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#specparam_declaration.
    def visitSpecparam_declaration(self, ctx:Verilog2001Parser.Specparam_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#inout_declaration.
    def visitInout_declaration(self, ctx:Verilog2001Parser.Inout_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#input_declaration.
    def visitInput_declaration(self, ctx:Verilog2001Parser.Input_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#output_declaration.
    def visitOutput_declaration(self, ctx:Verilog2001Parser.Output_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#event_declaration.
    def visitEvent_declaration(self, ctx:Verilog2001Parser.Event_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#genvar_declaration.
    def visitGenvar_declaration(self, ctx:Verilog2001Parser.Genvar_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#integer_declaration.
    def visitInteger_declaration(self, ctx:Verilog2001Parser.Integer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#time_declaration.
    def visitTime_declaration(self, ctx:Verilog2001Parser.Time_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#real_declaration.
    def visitReal_declaration(self, ctx:Verilog2001Parser.Real_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#realtime_declaration.
    def visitRealtime_declaration(self, ctx:Verilog2001Parser.Realtime_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#reg_declaration.
    def visitReg_declaration(self, ctx:Verilog2001Parser.Reg_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#net_declaration.
    def visitNet_declaration(self, ctx:Verilog2001Parser.Net_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#net_type.
    def visitNet_type(self, ctx:Verilog2001Parser.Net_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#output_variable_type.
    def visitOutput_variable_type(self, ctx:Verilog2001Parser.Output_variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#real_type.
    def visitReal_type(self, ctx:Verilog2001Parser.Real_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#variable_type.
    def visitVariable_type(self, ctx:Verilog2001Parser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#drive_strength.
    def visitDrive_strength(self, ctx:Verilog2001Parser.Drive_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#strength0.
    def visitStrength0(self, ctx:Verilog2001Parser.Strength0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#strength1.
    def visitStrength1(self, ctx:Verilog2001Parser.Strength1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#charge_strength.
    def visitCharge_strength(self, ctx:Verilog2001Parser.Charge_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#delay3.
    def visitDelay3(self, ctx:Verilog2001Parser.Delay3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#delay2.
    def visitDelay2(self, ctx:Verilog2001Parser.Delay2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#delay_value.
    def visitDelay_value(self, ctx:Verilog2001Parser.Delay_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_event_identifiers.
    def visitList_of_event_identifiers(self, ctx:Verilog2001Parser.List_of_event_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_net_identifiers.
    def visitList_of_net_identifiers(self, ctx:Verilog2001Parser.List_of_net_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_genvar_identifiers.
    def visitList_of_genvar_identifiers(self, ctx:Verilog2001Parser.List_of_genvar_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_port_identifiers.
    def visitList_of_port_identifiers(self, ctx:Verilog2001Parser.List_of_port_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_net_decl_assignments.
    def visitList_of_net_decl_assignments(self, ctx:Verilog2001Parser.List_of_net_decl_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_param_assignments.
    def visitList_of_param_assignments(self, ctx:Verilog2001Parser.List_of_param_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_specparam_assignments.
    def visitList_of_specparam_assignments(self, ctx:Verilog2001Parser.List_of_specparam_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_real_identifiers.
    def visitList_of_real_identifiers(self, ctx:Verilog2001Parser.List_of_real_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_variable_identifiers.
    def visitList_of_variable_identifiers(self, ctx:Verilog2001Parser.List_of_variable_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_variable_port_identifiers.
    def visitList_of_variable_port_identifiers(self, ctx:Verilog2001Parser.List_of_variable_port_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#net_decl_assignment.
    def visitNet_decl_assignment(self, ctx:Verilog2001Parser.Net_decl_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#param_assignment.
    def visitParam_assignment(self, ctx:Verilog2001Parser.Param_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#specparam_assignment.
    def visitSpecparam_assignment(self, ctx:Verilog2001Parser.Specparam_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#pulse_control_specparam.
    def visitPulse_control_specparam(self, ctx:Verilog2001Parser.Pulse_control_specparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#error_limit_value.
    def visitError_limit_value(self, ctx:Verilog2001Parser.Error_limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#reject_limit_value.
    def visitReject_limit_value(self, ctx:Verilog2001Parser.Reject_limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#limit_value.
    def visitLimit_value(self, ctx:Verilog2001Parser.Limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#dimension.
    def visitDimension(self, ctx:Verilog2001Parser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#range_.
    def visitRange_(self, ctx:Verilog2001Parser.Range_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_declaration.
    def visitFunction_declaration(self, ctx:Verilog2001Parser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_item_declaration.
    def visitFunction_item_declaration(self, ctx:Verilog2001Parser.Function_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_port_list.
    def visitFunction_port_list(self, ctx:Verilog2001Parser.Function_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_port.
    def visitFunction_port(self, ctx:Verilog2001Parser.Function_portContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#range_or_type.
    def visitRange_or_type(self, ctx:Verilog2001Parser.Range_or_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#task_declaration.
    def visitTask_declaration(self, ctx:Verilog2001Parser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#task_item_declaration.
    def visitTask_item_declaration(self, ctx:Verilog2001Parser.Task_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#task_port_list.
    def visitTask_port_list(self, ctx:Verilog2001Parser.Task_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#task_port_item.
    def visitTask_port_item(self, ctx:Verilog2001Parser.Task_port_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#tf_decl_header.
    def visitTf_decl_header(self, ctx:Verilog2001Parser.Tf_decl_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#tf_declaration.
    def visitTf_declaration(self, ctx:Verilog2001Parser.Tf_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#task_port_type.
    def visitTask_port_type(self, ctx:Verilog2001Parser.Task_port_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#block_item_declaration.
    def visitBlock_item_declaration(self, ctx:Verilog2001Parser.Block_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#block_reg_declaration.
    def visitBlock_reg_declaration(self, ctx:Verilog2001Parser.Block_reg_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_block_variable_identifiers.
    def visitList_of_block_variable_identifiers(self, ctx:Verilog2001Parser.List_of_block_variable_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#block_variable_type.
    def visitBlock_variable_type(self, ctx:Verilog2001Parser.Block_variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#gate_instantiation.
    def visitGate_instantiation(self, ctx:Verilog2001Parser.Gate_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#cmos_switch_instance.
    def visitCmos_switch_instance(self, ctx:Verilog2001Parser.Cmos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#enable_gate_instance.
    def visitEnable_gate_instance(self, ctx:Verilog2001Parser.Enable_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#mos_switch_instance.
    def visitMos_switch_instance(self, ctx:Verilog2001Parser.Mos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#n_input_gate_instance.
    def visitN_input_gate_instance(self, ctx:Verilog2001Parser.N_input_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#n_output_gate_instance.
    def visitN_output_gate_instance(self, ctx:Verilog2001Parser.N_output_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#pass_switch_instance.
    def visitPass_switch_instance(self, ctx:Verilog2001Parser.Pass_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#pass_enable_switch_instance.
    def visitPass_enable_switch_instance(self, ctx:Verilog2001Parser.Pass_enable_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#pull_gate_instance.
    def visitPull_gate_instance(self, ctx:Verilog2001Parser.Pull_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#name_of_gate_instance.
    def visitName_of_gate_instance(self, ctx:Verilog2001Parser.Name_of_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#pulldown_strength.
    def visitPulldown_strength(self, ctx:Verilog2001Parser.Pulldown_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#pullup_strength.
    def visitPullup_strength(self, ctx:Verilog2001Parser.Pullup_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#enable_terminal.
    def visitEnable_terminal(self, ctx:Verilog2001Parser.Enable_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#ncontrol_terminal.
    def visitNcontrol_terminal(self, ctx:Verilog2001Parser.Ncontrol_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#pcontrol_terminal.
    def visitPcontrol_terminal(self, ctx:Verilog2001Parser.Pcontrol_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#input_terminal.
    def visitInput_terminal(self, ctx:Verilog2001Parser.Input_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#inout_terminal.
    def visitInout_terminal(self, ctx:Verilog2001Parser.Inout_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#output_terminal.
    def visitOutput_terminal(self, ctx:Verilog2001Parser.Output_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#cmos_switchtype.
    def visitCmos_switchtype(self, ctx:Verilog2001Parser.Cmos_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#enable_gatetype.
    def visitEnable_gatetype(self, ctx:Verilog2001Parser.Enable_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#mos_switchtype.
    def visitMos_switchtype(self, ctx:Verilog2001Parser.Mos_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#n_input_gatetype.
    def visitN_input_gatetype(self, ctx:Verilog2001Parser.N_input_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#n_output_gatetype.
    def visitN_output_gatetype(self, ctx:Verilog2001Parser.N_output_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#pass_en_switchtype.
    def visitPass_en_switchtype(self, ctx:Verilog2001Parser.Pass_en_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#pass_switchtype.
    def visitPass_switchtype(self, ctx:Verilog2001Parser.Pass_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_instantiation.
    def visitModule_instantiation(self, ctx:Verilog2001Parser.Module_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#parameter_value_assignment.
    def visitParameter_value_assignment(self, ctx:Verilog2001Parser.Parameter_value_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_parameter_assignments.
    def visitList_of_parameter_assignments(self, ctx:Verilog2001Parser.List_of_parameter_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#ordered_parameter_assignment.
    def visitOrdered_parameter_assignment(self, ctx:Verilog2001Parser.Ordered_parameter_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#named_parameter_assignment.
    def visitNamed_parameter_assignment(self, ctx:Verilog2001Parser.Named_parameter_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_instance.
    def visitModule_instance(self, ctx:Verilog2001Parser.Module_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#name_of_instance.
    def visitName_of_instance(self, ctx:Verilog2001Parser.Name_of_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_port_connections.
    def visitList_of_port_connections(self, ctx:Verilog2001Parser.List_of_port_connectionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#ordered_port_connection.
    def visitOrdered_port_connection(self, ctx:Verilog2001Parser.Ordered_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#named_port_connection.
    def visitNamed_port_connection(self, ctx:Verilog2001Parser.Named_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#generated_instantiation.
    def visitGenerated_instantiation(self, ctx:Verilog2001Parser.Generated_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#generate_item_or_null.
    def visitGenerate_item_or_null(self, ctx:Verilog2001Parser.Generate_item_or_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#generate_item.
    def visitGenerate_item(self, ctx:Verilog2001Parser.Generate_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#generate_conditional_statement.
    def visitGenerate_conditional_statement(self, ctx:Verilog2001Parser.Generate_conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#generate_case_statement.
    def visitGenerate_case_statement(self, ctx:Verilog2001Parser.Generate_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#genvar_case_item.
    def visitGenvar_case_item(self, ctx:Verilog2001Parser.Genvar_case_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#generate_loop_statement.
    def visitGenerate_loop_statement(self, ctx:Verilog2001Parser.Generate_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#genvar_assignment.
    def visitGenvar_assignment(self, ctx:Verilog2001Parser.Genvar_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#generate_block.
    def visitGenerate_block(self, ctx:Verilog2001Parser.Generate_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#continuous_assign.
    def visitContinuous_assign(self, ctx:Verilog2001Parser.Continuous_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_net_assignments.
    def visitList_of_net_assignments(self, ctx:Verilog2001Parser.List_of_net_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#net_assignment.
    def visitNet_assignment(self, ctx:Verilog2001Parser.Net_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#initial_construct.
    def visitInitial_construct(self, ctx:Verilog2001Parser.Initial_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#always_construct.
    def visitAlways_construct(self, ctx:Verilog2001Parser.Always_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#blocking_assignment.
    def visitBlocking_assignment(self, ctx:Verilog2001Parser.Blocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#nonblocking_assignment.
    def visitNonblocking_assignment(self, ctx:Verilog2001Parser.Nonblocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#procedural_continuous_assignments.
    def visitProcedural_continuous_assignments(self, ctx:Verilog2001Parser.Procedural_continuous_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_blocking_assignment.
    def visitFunction_blocking_assignment(self, ctx:Verilog2001Parser.Function_blocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_statement_or_null.
    def visitFunction_statement_or_null(self, ctx:Verilog2001Parser.Function_statement_or_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_seq_block.
    def visitFunction_seq_block(self, ctx:Verilog2001Parser.Function_seq_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#variable_assignment.
    def visitVariable_assignment(self, ctx:Verilog2001Parser.Variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#par_block.
    def visitPar_block(self, ctx:Verilog2001Parser.Par_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#seq_block.
    def visitSeq_block(self, ctx:Verilog2001Parser.Seq_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#statement.
    def visitStatement(self, ctx:Verilog2001Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#statement_or_null.
    def visitStatement_or_null(self, ctx:Verilog2001Parser.Statement_or_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_statement.
    def visitFunction_statement(self, ctx:Verilog2001Parser.Function_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#delay_or_event_control.
    def visitDelay_or_event_control(self, ctx:Verilog2001Parser.Delay_or_event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#delay_control.
    def visitDelay_control(self, ctx:Verilog2001Parser.Delay_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#disable_statement.
    def visitDisable_statement(self, ctx:Verilog2001Parser.Disable_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#event_control.
    def visitEvent_control(self, ctx:Verilog2001Parser.Event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#event_trigger.
    def visitEvent_trigger(self, ctx:Verilog2001Parser.Event_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#event_expression.
    def visitEvent_expression(self, ctx:Verilog2001Parser.Event_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#event_primary.
    def visitEvent_primary(self, ctx:Verilog2001Parser.Event_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#procedural_timing_control_statement.
    def visitProcedural_timing_control_statement(self, ctx:Verilog2001Parser.Procedural_timing_control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#wait_statement.
    def visitWait_statement(self, ctx:Verilog2001Parser.Wait_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#conditional_statement.
    def visitConditional_statement(self, ctx:Verilog2001Parser.Conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#if_else_if_statement.
    def visitIf_else_if_statement(self, ctx:Verilog2001Parser.If_else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_conditional_statement.
    def visitFunction_conditional_statement(self, ctx:Verilog2001Parser.Function_conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_if_else_if_statement.
    def visitFunction_if_else_if_statement(self, ctx:Verilog2001Parser.Function_if_else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#case_statement.
    def visitCase_statement(self, ctx:Verilog2001Parser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#case_item.
    def visitCase_item(self, ctx:Verilog2001Parser.Case_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_case_statement.
    def visitFunction_case_statement(self, ctx:Verilog2001Parser.Function_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_case_item.
    def visitFunction_case_item(self, ctx:Verilog2001Parser.Function_case_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_loop_statement.
    def visitFunction_loop_statement(self, ctx:Verilog2001Parser.Function_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#loop_statement.
    def visitLoop_statement(self, ctx:Verilog2001Parser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#system_task_enable.
    def visitSystem_task_enable(self, ctx:Verilog2001Parser.System_task_enableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#task_enable.
    def visitTask_enable(self, ctx:Verilog2001Parser.Task_enableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#specify_block.
    def visitSpecify_block(self, ctx:Verilog2001Parser.Specify_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#specify_item.
    def visitSpecify_item(self, ctx:Verilog2001Parser.Specify_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#pulsestyle_declaration.
    def visitPulsestyle_declaration(self, ctx:Verilog2001Parser.Pulsestyle_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#showcancelled_declaration.
    def visitShowcancelled_declaration(self, ctx:Verilog2001Parser.Showcancelled_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#path_declaration.
    def visitPath_declaration(self, ctx:Verilog2001Parser.Path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#simple_path_declaration.
    def visitSimple_path_declaration(self, ctx:Verilog2001Parser.Simple_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#parallel_path_description.
    def visitParallel_path_description(self, ctx:Verilog2001Parser.Parallel_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#full_path_description.
    def visitFull_path_description(self, ctx:Verilog2001Parser.Full_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_path_inputs.
    def visitList_of_path_inputs(self, ctx:Verilog2001Parser.List_of_path_inputsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_path_outputs.
    def visitList_of_path_outputs(self, ctx:Verilog2001Parser.List_of_path_outputsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#specify_input_terminal_descriptor.
    def visitSpecify_input_terminal_descriptor(self, ctx:Verilog2001Parser.Specify_input_terminal_descriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#specify_output_terminal_descriptor.
    def visitSpecify_output_terminal_descriptor(self, ctx:Verilog2001Parser.Specify_output_terminal_descriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#input_identifier.
    def visitInput_identifier(self, ctx:Verilog2001Parser.Input_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#output_identifier.
    def visitOutput_identifier(self, ctx:Verilog2001Parser.Output_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#path_delay_value.
    def visitPath_delay_value(self, ctx:Verilog2001Parser.Path_delay_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#list_of_path_delay_expressions.
    def visitList_of_path_delay_expressions(self, ctx:Verilog2001Parser.List_of_path_delay_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#t_path_delay_expression.
    def visitT_path_delay_expression(self, ctx:Verilog2001Parser.T_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#trise_path_delay_expression.
    def visitTrise_path_delay_expression(self, ctx:Verilog2001Parser.Trise_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#tfall_path_delay_expression.
    def visitTfall_path_delay_expression(self, ctx:Verilog2001Parser.Tfall_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#tz_path_delay_expression.
    def visitTz_path_delay_expression(self, ctx:Verilog2001Parser.Tz_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#t01_path_delay_expression.
    def visitT01_path_delay_expression(self, ctx:Verilog2001Parser.T01_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#t10_path_delay_expression.
    def visitT10_path_delay_expression(self, ctx:Verilog2001Parser.T10_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#t0z_path_delay_expression.
    def visitT0z_path_delay_expression(self, ctx:Verilog2001Parser.T0z_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#tz1_path_delay_expression.
    def visitTz1_path_delay_expression(self, ctx:Verilog2001Parser.Tz1_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#t1z_path_delay_expression.
    def visitT1z_path_delay_expression(self, ctx:Verilog2001Parser.T1z_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#tz0_path_delay_expression.
    def visitTz0_path_delay_expression(self, ctx:Verilog2001Parser.Tz0_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#t0x_path_delay_expression.
    def visitT0x_path_delay_expression(self, ctx:Verilog2001Parser.T0x_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#tx1_path_delay_expression.
    def visitTx1_path_delay_expression(self, ctx:Verilog2001Parser.Tx1_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#t1x_path_delay_expression.
    def visitT1x_path_delay_expression(self, ctx:Verilog2001Parser.T1x_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#tx0_path_delay_expression.
    def visitTx0_path_delay_expression(self, ctx:Verilog2001Parser.Tx0_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#txz_path_delay_expression.
    def visitTxz_path_delay_expression(self, ctx:Verilog2001Parser.Txz_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#tzx_path_delay_expression.
    def visitTzx_path_delay_expression(self, ctx:Verilog2001Parser.Tzx_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#path_delay_expression.
    def visitPath_delay_expression(self, ctx:Verilog2001Parser.Path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#edge_sensitive_path_declaration.
    def visitEdge_sensitive_path_declaration(self, ctx:Verilog2001Parser.Edge_sensitive_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#parallel_edge_sensitive_path_description.
    def visitParallel_edge_sensitive_path_description(self, ctx:Verilog2001Parser.Parallel_edge_sensitive_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#full_edge_sensitive_path_description.
    def visitFull_edge_sensitive_path_description(self, ctx:Verilog2001Parser.Full_edge_sensitive_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#data_source_expression.
    def visitData_source_expression(self, ctx:Verilog2001Parser.Data_source_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#edge_identifier.
    def visitEdge_identifier(self, ctx:Verilog2001Parser.Edge_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#state_dependent_path_declaration.
    def visitState_dependent_path_declaration(self, ctx:Verilog2001Parser.State_dependent_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#polarity_operator.
    def visitPolarity_operator(self, ctx:Verilog2001Parser.Polarity_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#checktime_condition.
    def visitChecktime_condition(self, ctx:Verilog2001Parser.Checktime_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#delayed_data.
    def visitDelayed_data(self, ctx:Verilog2001Parser.Delayed_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#delayed_reference.
    def visitDelayed_reference(self, ctx:Verilog2001Parser.Delayed_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#end_edge_offset.
    def visitEnd_edge_offset(self, ctx:Verilog2001Parser.End_edge_offsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#event_based_flag.
    def visitEvent_based_flag(self, ctx:Verilog2001Parser.Event_based_flagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#notify_reg.
    def visitNotify_reg(self, ctx:Verilog2001Parser.Notify_regContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#remain_active_flag.
    def visitRemain_active_flag(self, ctx:Verilog2001Parser.Remain_active_flagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#stamptime_condition.
    def visitStamptime_condition(self, ctx:Verilog2001Parser.Stamptime_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#start_edge_offset.
    def visitStart_edge_offset(self, ctx:Verilog2001Parser.Start_edge_offsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#threshold.
    def visitThreshold(self, ctx:Verilog2001Parser.ThresholdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#timing_check_limit.
    def visitTiming_check_limit(self, ctx:Verilog2001Parser.Timing_check_limitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#concatenation.
    def visitConcatenation(self, ctx:Verilog2001Parser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#constant_concatenation.
    def visitConstant_concatenation(self, ctx:Verilog2001Parser.Constant_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#constant_multiple_concatenation.
    def visitConstant_multiple_concatenation(self, ctx:Verilog2001Parser.Constant_multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_path_concatenation.
    def visitModule_path_concatenation(self, ctx:Verilog2001Parser.Module_path_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_path_multiple_concatenation.
    def visitModule_path_multiple_concatenation(self, ctx:Verilog2001Parser.Module_path_multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#multiple_concatenation.
    def visitMultiple_concatenation(self, ctx:Verilog2001Parser.Multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#net_concatenation.
    def visitNet_concatenation(self, ctx:Verilog2001Parser.Net_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#net_concatenation_value.
    def visitNet_concatenation_value(self, ctx:Verilog2001Parser.Net_concatenation_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#variable_concatenation.
    def visitVariable_concatenation(self, ctx:Verilog2001Parser.Variable_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#variable_concatenation_value.
    def visitVariable_concatenation_value(self, ctx:Verilog2001Parser.Variable_concatenation_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#constant_function_call.
    def visitConstant_function_call(self, ctx:Verilog2001Parser.Constant_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_call.
    def visitFunction_call(self, ctx:Verilog2001Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#system_function_call.
    def visitSystem_function_call(self, ctx:Verilog2001Parser.System_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#genvar_function_call.
    def visitGenvar_function_call(self, ctx:Verilog2001Parser.Genvar_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#base_expression.
    def visitBase_expression(self, ctx:Verilog2001Parser.Base_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#constant_base_expression.
    def visitConstant_base_expression(self, ctx:Verilog2001Parser.Constant_base_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#constant_expression.
    def visitConstant_expression(self, ctx:Verilog2001Parser.Constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#constant_mintypmax_expression.
    def visitConstant_mintypmax_expression(self, ctx:Verilog2001Parser.Constant_mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#constant_range_expression.
    def visitConstant_range_expression(self, ctx:Verilog2001Parser.Constant_range_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#dimension_constant_expression.
    def visitDimension_constant_expression(self, ctx:Verilog2001Parser.Dimension_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#expression.
    def visitExpression(self, ctx:Verilog2001Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#term.
    def visitTerm(self, ctx:Verilog2001Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#lsb_constant_expression.
    def visitLsb_constant_expression(self, ctx:Verilog2001Parser.Lsb_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#mintypmax_expression.
    def visitMintypmax_expression(self, ctx:Verilog2001Parser.Mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_path_conditional_expression.
    def visitModule_path_conditional_expression(self, ctx:Verilog2001Parser.Module_path_conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_path_expression.
    def visitModule_path_expression(self, ctx:Verilog2001Parser.Module_path_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_path_mintypmax_expression.
    def visitModule_path_mintypmax_expression(self, ctx:Verilog2001Parser.Module_path_mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#msb_constant_expression.
    def visitMsb_constant_expression(self, ctx:Verilog2001Parser.Msb_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#range_expression.
    def visitRange_expression(self, ctx:Verilog2001Parser.Range_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#width_constant_expression.
    def visitWidth_constant_expression(self, ctx:Verilog2001Parser.Width_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#constant_primary.
    def visitConstant_primary(self, ctx:Verilog2001Parser.Constant_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_path_primary.
    def visitModule_path_primary(self, ctx:Verilog2001Parser.Module_path_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#primary.
    def visitPrimary(self, ctx:Verilog2001Parser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#net_lvalue.
    def visitNet_lvalue(self, ctx:Verilog2001Parser.Net_lvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#variable_lvalue.
    def visitVariable_lvalue(self, ctx:Verilog2001Parser.Variable_lvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#unary_operator.
    def visitUnary_operator(self, ctx:Verilog2001Parser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#binary_operator.
    def visitBinary_operator(self, ctx:Verilog2001Parser.Binary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#unary_module_path_operator.
    def visitUnary_module_path_operator(self, ctx:Verilog2001Parser.Unary_module_path_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#binary_module_path_operator.
    def visitBinary_module_path_operator(self, ctx:Verilog2001Parser.Binary_module_path_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#number.
    def visitNumber(self, ctx:Verilog2001Parser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#timing_spec.
    def visitTiming_spec(self, ctx:Verilog2001Parser.Timing_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#attribute_instance.
    def visitAttribute_instance(self, ctx:Verilog2001Parser.Attribute_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#attr_spec.
    def visitAttr_spec(self, ctx:Verilog2001Parser.Attr_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#attr_name.
    def visitAttr_name(self, ctx:Verilog2001Parser.Attr_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#arrayed_identifier.
    def visitArrayed_identifier(self, ctx:Verilog2001Parser.Arrayed_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#block_identifier.
    def visitBlock_identifier(self, ctx:Verilog2001Parser.Block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#cell_identifier.
    def visitCell_identifier(self, ctx:Verilog2001Parser.Cell_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#config_identifier.
    def visitConfig_identifier(self, ctx:Verilog2001Parser.Config_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#escaped_arrayed_identifier.
    def visitEscaped_arrayed_identifier(self, ctx:Verilog2001Parser.Escaped_arrayed_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#escaped_hierarchical_identifier.
    def visitEscaped_hierarchical_identifier(self, ctx:Verilog2001Parser.Escaped_hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#event_identifier.
    def visitEvent_identifier(self, ctx:Verilog2001Parser.Event_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#function_identifier.
    def visitFunction_identifier(self, ctx:Verilog2001Parser.Function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#gate_instance_identifier.
    def visitGate_instance_identifier(self, ctx:Verilog2001Parser.Gate_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#generate_block_identifier.
    def visitGenerate_block_identifier(self, ctx:Verilog2001Parser.Generate_block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#genvar_function_identifier.
    def visitGenvar_function_identifier(self, ctx:Verilog2001Parser.Genvar_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#genvar_identifier.
    def visitGenvar_identifier(self, ctx:Verilog2001Parser.Genvar_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#hierarchical_block_identifier.
    def visitHierarchical_block_identifier(self, ctx:Verilog2001Parser.Hierarchical_block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#hierarchical_event_identifier.
    def visitHierarchical_event_identifier(self, ctx:Verilog2001Parser.Hierarchical_event_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#hierarchical_function_identifier.
    def visitHierarchical_function_identifier(self, ctx:Verilog2001Parser.Hierarchical_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#hierarchical_identifier.
    def visitHierarchical_identifier(self, ctx:Verilog2001Parser.Hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#hierarchical_net_identifier.
    def visitHierarchical_net_identifier(self, ctx:Verilog2001Parser.Hierarchical_net_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#hierarchical_variable_identifier.
    def visitHierarchical_variable_identifier(self, ctx:Verilog2001Parser.Hierarchical_variable_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#hierarchical_task_identifier.
    def visitHierarchical_task_identifier(self, ctx:Verilog2001Parser.Hierarchical_task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#identifier.
    def visitIdentifier(self, ctx:Verilog2001Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#inout_port_identifier.
    def visitInout_port_identifier(self, ctx:Verilog2001Parser.Inout_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#input_port_identifier.
    def visitInput_port_identifier(self, ctx:Verilog2001Parser.Input_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#instance_identifier.
    def visitInstance_identifier(self, ctx:Verilog2001Parser.Instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#library_identifier.
    def visitLibrary_identifier(self, ctx:Verilog2001Parser.Library_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#memory_identifier.
    def visitMemory_identifier(self, ctx:Verilog2001Parser.Memory_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_identifier.
    def visitModule_identifier(self, ctx:Verilog2001Parser.Module_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#module_instance_identifier.
    def visitModule_instance_identifier(self, ctx:Verilog2001Parser.Module_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#net_identifier.
    def visitNet_identifier(self, ctx:Verilog2001Parser.Net_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#output_port_identifier.
    def visitOutput_port_identifier(self, ctx:Verilog2001Parser.Output_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#parameter_identifier.
    def visitParameter_identifier(self, ctx:Verilog2001Parser.Parameter_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#port_identifier.
    def visitPort_identifier(self, ctx:Verilog2001Parser.Port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#real_identifier.
    def visitReal_identifier(self, ctx:Verilog2001Parser.Real_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#simple_arrayed_identifier.
    def visitSimple_arrayed_identifier(self, ctx:Verilog2001Parser.Simple_arrayed_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#simple_hierarchical_identifier.
    def visitSimple_hierarchical_identifier(self, ctx:Verilog2001Parser.Simple_hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#specparam_identifier.
    def visitSpecparam_identifier(self, ctx:Verilog2001Parser.Specparam_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#system_function_identifier.
    def visitSystem_function_identifier(self, ctx:Verilog2001Parser.System_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#system_task_identifier.
    def visitSystem_task_identifier(self, ctx:Verilog2001Parser.System_task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#task_identifier.
    def visitTask_identifier(self, ctx:Verilog2001Parser.Task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#terminal_identifier.
    def visitTerminal_identifier(self, ctx:Verilog2001Parser.Terminal_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#text_macro_identifier.
    def visitText_macro_identifier(self, ctx:Verilog2001Parser.Text_macro_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#topmodule_identifier.
    def visitTopmodule_identifier(self, ctx:Verilog2001Parser.Topmodule_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#udp_identifier.
    def visitUdp_identifier(self, ctx:Verilog2001Parser.Udp_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#udp_instance_identifier.
    def visitUdp_instance_identifier(self, ctx:Verilog2001Parser.Udp_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#variable_identifier.
    def visitVariable_identifier(self, ctx:Verilog2001Parser.Variable_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#simple_hierarchical_branch.
    def visitSimple_hierarchical_branch(self, ctx:Verilog2001Parser.Simple_hierarchical_branchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Verilog2001Parser#escaped_hierarchical_branch.
    def visitEscaped_hierarchical_branch(self, ctx:Verilog2001Parser.Escaped_hierarchical_branchContext):
        return self.visitChildren(ctx)



del Verilog2001Parser