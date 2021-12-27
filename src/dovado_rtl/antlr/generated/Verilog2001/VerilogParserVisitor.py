# Generated from VerilogParser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VerilogParser import VerilogParser
else:
    from VerilogParser import VerilogParser

# This class defines a complete generic visitor for a parse tree produced by VerilogParser.

class VerilogParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VerilogParser#display_tasks.
    def visitDisplay_tasks(self, ctx:VerilogParser.Display_tasksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#display_task_name.
    def visitDisplay_task_name(self, ctx:VerilogParser.Display_task_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_arguments.
    def visitList_of_arguments(self, ctx:VerilogParser.List_of_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#argument.
    def visitArgument(self, ctx:VerilogParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#strobe_tasks.
    def visitStrobe_tasks(self, ctx:VerilogParser.Strobe_tasksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#strobe_task_name.
    def visitStrobe_task_name(self, ctx:VerilogParser.Strobe_task_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#monitor_tasks.
    def visitMonitor_tasks(self, ctx:VerilogParser.Monitor_tasksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#monitor_task_name.
    def visitMonitor_task_name(self, ctx:VerilogParser.Monitor_task_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#file_open_function.
    def visitFile_open_function(self, ctx:VerilogParser.File_open_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#file_close_task.
    def visitFile_close_task(self, ctx:VerilogParser.File_close_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#multi_channel_descriptor.
    def visitMulti_channel_descriptor(self, ctx:VerilogParser.Multi_channel_descriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#fd.
    def visitFd(self, ctx:VerilogParser.FdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#file_name.
    def visitFile_name(self, ctx:VerilogParser.File_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#type_.
    def visitType_(self, ctx:VerilogParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#file_output_tasks.
    def visitFile_output_tasks(self, ctx:VerilogParser.File_output_tasksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#file_output_task_name.
    def visitFile_output_task_name(self, ctx:VerilogParser.File_output_task_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#load_memory_tasks.
    def visitLoad_memory_tasks(self, ctx:VerilogParser.Load_memory_tasksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#memory_name.
    def visitMemory_name(self, ctx:VerilogParser.Memory_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#start_addr.
    def visitStart_addr(self, ctx:VerilogParser.Start_addrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#finish_addr.
    def visitFinish_addr(self, ctx:VerilogParser.Finish_addrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#filename.
    def visitFilename(self, ctx:VerilogParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#finish_task.
    def visitFinish_task(self, ctx:VerilogParser.Finish_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#finish_number.
    def visitFinish_number(self, ctx:VerilogParser.Finish_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#stop_task.
    def visitStop_task(self, ctx:VerilogParser.Stop_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#time_function.
    def visitTime_function(self, ctx:VerilogParser.Time_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#stime_function.
    def visitStime_function(self, ctx:VerilogParser.Stime_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#realtime_function.
    def visitRealtime_function(self, ctx:VerilogParser.Realtime_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#conversion_functions.
    def visitConversion_functions(self, ctx:VerilogParser.Conversion_functionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#conversion_function_name.
    def visitConversion_function_name(self, ctx:VerilogParser.Conversion_function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_argument.
    def visitConstant_argument(self, ctx:VerilogParser.Constant_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#random_function.
    def visitRandom_function(self, ctx:VerilogParser.Random_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#seed.
    def visitSeed(self, ctx:VerilogParser.SeedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dist_functions.
    def visitDist_functions(self, ctx:VerilogParser.Dist_functionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#start_.
    def visitStart_(self, ctx:VerilogParser.Start_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#end.
    def visitEnd(self, ctx:VerilogParser.EndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#mean.
    def visitMean(self, ctx:VerilogParser.MeanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#standard_deviation.
    def visitStandard_deviation(self, ctx:VerilogParser.Standard_deviationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#degree_of_freedom.
    def visitDegree_of_freedom(self, ctx:VerilogParser.Degree_of_freedomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#k_stage.
    def visitK_stage(self, ctx:VerilogParser.K_stageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#math_functions.
    def visitMath_functions(self, ctx:VerilogParser.Math_functionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#integer_math_functions.
    def visitInteger_math_functions(self, ctx:VerilogParser.Integer_math_functionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#real_math_functions.
    def visitReal_math_functions(self, ctx:VerilogParser.Real_math_functionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#single_argument_real_math_function_name.
    def visitSingle_argument_real_math_function_name(self, ctx:VerilogParser.Single_argument_real_math_function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#double_argument_real_math_function_name.
    def visitDouble_argument_real_math_function_name(self, ctx:VerilogParser.Double_argument_real_math_function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpfile_task.
    def visitDumpfile_task(self, ctx:VerilogParser.Dumpfile_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpvars_task.
    def visitDumpvars_task(self, ctx:VerilogParser.Dumpvars_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_modules_or_variables.
    def visitList_of_modules_or_variables(self, ctx:VerilogParser.List_of_modules_or_variablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_or_variable.
    def visitModule_or_variable(self, ctx:VerilogParser.Module_or_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#levels.
    def visitLevels(self, ctx:VerilogParser.LevelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpoff_task.
    def visitDumpoff_task(self, ctx:VerilogParser.Dumpoff_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpon_task.
    def visitDumpon_task(self, ctx:VerilogParser.Dumpon_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpall_task.
    def visitDumpall_task(self, ctx:VerilogParser.Dumpall_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumplimit_task.
    def visitDumplimit_task(self, ctx:VerilogParser.Dumplimit_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#file_size.
    def visitFile_size(self, ctx:VerilogParser.File_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpflush_task.
    def visitDumpflush_task(self, ctx:VerilogParser.Dumpflush_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpports_task.
    def visitDumpports_task(self, ctx:VerilogParser.Dumpports_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#scope_list.
    def visitScope_list(self, ctx:VerilogParser.Scope_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#file_pathname.
    def visitFile_pathname(self, ctx:VerilogParser.File_pathnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpportsoff_task.
    def visitDumpportsoff_task(self, ctx:VerilogParser.Dumpportsoff_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpportson_task.
    def visitDumpportson_task(self, ctx:VerilogParser.Dumpportson_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpportsall_task.
    def visitDumpportsall_task(self, ctx:VerilogParser.Dumpportsall_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpportslimit_task.
    def visitDumpportslimit_task(self, ctx:VerilogParser.Dumpportslimit_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dumpportsflush_task.
    def visitDumpportsflush_task(self, ctx:VerilogParser.Dumpportsflush_taskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#library_text.
    def visitLibrary_text(self, ctx:VerilogParser.Library_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#library_description.
    def visitLibrary_description(self, ctx:VerilogParser.Library_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#library_declaration.
    def visitLibrary_declaration(self, ctx:VerilogParser.Library_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#include_statement.
    def visitInclude_statement(self, ctx:VerilogParser.Include_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#source_text.
    def visitSource_text(self, ctx:VerilogParser.Source_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#description.
    def visitDescription(self, ctx:VerilogParser.DescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_declaration.
    def visitModule_declaration(self, ctx:VerilogParser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_keyword.
    def visitModule_keyword(self, ctx:VerilogParser.Module_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_parameter_port_list.
    def visitModule_parameter_port_list(self, ctx:VerilogParser.Module_parameter_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_ports.
    def visitList_of_ports(self, ctx:VerilogParser.List_of_portsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_port_declarations.
    def visitList_of_port_declarations(self, ctx:VerilogParser.List_of_port_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port.
    def visitPort(self, ctx:VerilogParser.PortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port_expression.
    def visitPort_expression(self, ctx:VerilogParser.Port_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port_reference.
    def visitPort_reference(self, ctx:VerilogParser.Port_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port_declaration.
    def visitPort_declaration(self, ctx:VerilogParser.Port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_item.
    def visitModule_item(self, ctx:VerilogParser.Module_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_or_generate_item.
    def visitModule_or_generate_item(self, ctx:VerilogParser.Module_or_generate_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_or_generate_item_declaration.
    def visitModule_or_generate_item_declaration(self, ctx:VerilogParser.Module_or_generate_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#non_port_module_item.
    def visitNon_port_module_item(self, ctx:VerilogParser.Non_port_module_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parameter_override.
    def visitParameter_override(self, ctx:VerilogParser.Parameter_overrideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#config_declaration.
    def visitConfig_declaration(self, ctx:VerilogParser.Config_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#design_statement.
    def visitDesign_statement(self, ctx:VerilogParser.Design_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#config_rule_statement.
    def visitConfig_rule_statement(self, ctx:VerilogParser.Config_rule_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#default_clause.
    def visitDefault_clause(self, ctx:VerilogParser.Default_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#inst_clause.
    def visitInst_clause(self, ctx:VerilogParser.Inst_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#inst_name.
    def visitInst_name(self, ctx:VerilogParser.Inst_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#cell_clause.
    def visitCell_clause(self, ctx:VerilogParser.Cell_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#liblist_clause.
    def visitLiblist_clause(self, ctx:VerilogParser.Liblist_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#use_clause.
    def visitUse_clause(self, ctx:VerilogParser.Use_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#local_parameter_declaration.
    def visitLocal_parameter_declaration(self, ctx:VerilogParser.Local_parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:VerilogParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specparam_declaration.
    def visitSpecparam_declaration(self, ctx:VerilogParser.Specparam_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parameter_type.
    def visitParameter_type(self, ctx:VerilogParser.Parameter_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#inout_declaration.
    def visitInout_declaration(self, ctx:VerilogParser.Inout_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#input_declaration.
    def visitInput_declaration(self, ctx:VerilogParser.Input_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#output_declaration.
    def visitOutput_declaration(self, ctx:VerilogParser.Output_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_declaration.
    def visitEvent_declaration(self, ctx:VerilogParser.Event_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#integer_declaration.
    def visitInteger_declaration(self, ctx:VerilogParser.Integer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_declaration.
    def visitNet_declaration(self, ctx:VerilogParser.Net_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#real_declaration.
    def visitReal_declaration(self, ctx:VerilogParser.Real_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#realtime_declaration.
    def visitRealtime_declaration(self, ctx:VerilogParser.Realtime_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#reg_declaration.
    def visitReg_declaration(self, ctx:VerilogParser.Reg_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#time_declaration.
    def visitTime_declaration(self, ctx:VerilogParser.Time_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_type.
    def visitNet_type(self, ctx:VerilogParser.Net_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#output_variable_type.
    def visitOutput_variable_type(self, ctx:VerilogParser.Output_variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#real_type.
    def visitReal_type(self, ctx:VerilogParser.Real_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#variable_type.
    def visitVariable_type(self, ctx:VerilogParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#drive_strength.
    def visitDrive_strength(self, ctx:VerilogParser.Drive_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#strength0.
    def visitStrength0(self, ctx:VerilogParser.Strength0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#strength1.
    def visitStrength1(self, ctx:VerilogParser.Strength1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#charge_strength.
    def visitCharge_strength(self, ctx:VerilogParser.Charge_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delay3.
    def visitDelay3(self, ctx:VerilogParser.Delay3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delay2.
    def visitDelay2(self, ctx:VerilogParser.Delay2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delay_value.
    def visitDelay_value(self, ctx:VerilogParser.Delay_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_defparam_assignments.
    def visitList_of_defparam_assignments(self, ctx:VerilogParser.List_of_defparam_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_event_identifiers.
    def visitList_of_event_identifiers(self, ctx:VerilogParser.List_of_event_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_net_decl_assignments.
    def visitList_of_net_decl_assignments(self, ctx:VerilogParser.List_of_net_decl_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_net_identifiers.
    def visitList_of_net_identifiers(self, ctx:VerilogParser.List_of_net_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_param_assignments.
    def visitList_of_param_assignments(self, ctx:VerilogParser.List_of_param_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_port_identifiers.
    def visitList_of_port_identifiers(self, ctx:VerilogParser.List_of_port_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_real_identifiers.
    def visitList_of_real_identifiers(self, ctx:VerilogParser.List_of_real_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_specparam_assignments.
    def visitList_of_specparam_assignments(self, ctx:VerilogParser.List_of_specparam_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_variable_identifiers.
    def visitList_of_variable_identifiers(self, ctx:VerilogParser.List_of_variable_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_variable_port_identifiers.
    def visitList_of_variable_port_identifiers(self, ctx:VerilogParser.List_of_variable_port_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#defparam_assignment.
    def visitDefparam_assignment(self, ctx:VerilogParser.Defparam_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_decl_assignment.
    def visitNet_decl_assignment(self, ctx:VerilogParser.Net_decl_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#param_assignment.
    def visitParam_assignment(self, ctx:VerilogParser.Param_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specparam_assignment.
    def visitSpecparam_assignment(self, ctx:VerilogParser.Specparam_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pulse_control_specparam.
    def visitPulse_control_specparam(self, ctx:VerilogParser.Pulse_control_specparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#error_limit_value.
    def visitError_limit_value(self, ctx:VerilogParser.Error_limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#reject_limit_value.
    def visitReject_limit_value(self, ctx:VerilogParser.Reject_limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#limit_value.
    def visitLimit_value(self, ctx:VerilogParser.Limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dimension.
    def visitDimension(self, ctx:VerilogParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#range_.
    def visitRange_(self, ctx:VerilogParser.Range_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_declaration.
    def visitFunction_declaration(self, ctx:VerilogParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_item_declaration.
    def visitFunction_item_declaration(self, ctx:VerilogParser.Function_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_port_list.
    def visitFunction_port_list(self, ctx:VerilogParser.Function_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_range_or_type.
    def visitFunction_range_or_type(self, ctx:VerilogParser.Function_range_or_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_declaration.
    def visitTask_declaration(self, ctx:VerilogParser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_item_declaration.
    def visitTask_item_declaration(self, ctx:VerilogParser.Task_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_port_list.
    def visitTask_port_list(self, ctx:VerilogParser.Task_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_port_item.
    def visitTask_port_item(self, ctx:VerilogParser.Task_port_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tf_input_declaration.
    def visitTf_input_declaration(self, ctx:VerilogParser.Tf_input_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tf_output_declaration.
    def visitTf_output_declaration(self, ctx:VerilogParser.Tf_output_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tf_inout_declaration.
    def visitTf_inout_declaration(self, ctx:VerilogParser.Tf_inout_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_port_type.
    def visitTask_port_type(self, ctx:VerilogParser.Task_port_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#block_item_declaration.
    def visitBlock_item_declaration(self, ctx:VerilogParser.Block_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_block_variable_identifiers.
    def visitList_of_block_variable_identifiers(self, ctx:VerilogParser.List_of_block_variable_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_block_real_identifiers.
    def visitList_of_block_real_identifiers(self, ctx:VerilogParser.List_of_block_real_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#block_variable_type.
    def visitBlock_variable_type(self, ctx:VerilogParser.Block_variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#block_real_type.
    def visitBlock_real_type(self, ctx:VerilogParser.Block_real_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#gate_instantiation.
    def visitGate_instantiation(self, ctx:VerilogParser.Gate_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#cmos_switch_instance.
    def visitCmos_switch_instance(self, ctx:VerilogParser.Cmos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#enable_gate_instance.
    def visitEnable_gate_instance(self, ctx:VerilogParser.Enable_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#mos_switch_instance.
    def visitMos_switch_instance(self, ctx:VerilogParser.Mos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#n_input_gate_instance.
    def visitN_input_gate_instance(self, ctx:VerilogParser.N_input_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#n_output_gate_instance.
    def visitN_output_gate_instance(self, ctx:VerilogParser.N_output_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pass_switch_instance.
    def visitPass_switch_instance(self, ctx:VerilogParser.Pass_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pass_enable_switch_instance.
    def visitPass_enable_switch_instance(self, ctx:VerilogParser.Pass_enable_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pull_gate_instance.
    def visitPull_gate_instance(self, ctx:VerilogParser.Pull_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#name_of_gate_instance.
    def visitName_of_gate_instance(self, ctx:VerilogParser.Name_of_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pulldown_strength.
    def visitPulldown_strength(self, ctx:VerilogParser.Pulldown_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pullup_strength.
    def visitPullup_strength(self, ctx:VerilogParser.Pullup_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#enable_terminal.
    def visitEnable_terminal(self, ctx:VerilogParser.Enable_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#inout_terminal.
    def visitInout_terminal(self, ctx:VerilogParser.Inout_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#input_terminal.
    def visitInput_terminal(self, ctx:VerilogParser.Input_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#ncontrol_terminal.
    def visitNcontrol_terminal(self, ctx:VerilogParser.Ncontrol_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#output_terminal.
    def visitOutput_terminal(self, ctx:VerilogParser.Output_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pcontrol_terminal.
    def visitPcontrol_terminal(self, ctx:VerilogParser.Pcontrol_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#cmos_switchtype.
    def visitCmos_switchtype(self, ctx:VerilogParser.Cmos_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#enable_gatetype.
    def visitEnable_gatetype(self, ctx:VerilogParser.Enable_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#mos_switchtype.
    def visitMos_switchtype(self, ctx:VerilogParser.Mos_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#n_input_gatetype.
    def visitN_input_gatetype(self, ctx:VerilogParser.N_input_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#n_output_gatetype.
    def visitN_output_gatetype(self, ctx:VerilogParser.N_output_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pass_en_switchtype.
    def visitPass_en_switchtype(self, ctx:VerilogParser.Pass_en_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pass_switchtype.
    def visitPass_switchtype(self, ctx:VerilogParser.Pass_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_instantiation.
    def visitModule_instantiation(self, ctx:VerilogParser.Module_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parameter_value_assignment.
    def visitParameter_value_assignment(self, ctx:VerilogParser.Parameter_value_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_parameter_assignments.
    def visitList_of_parameter_assignments(self, ctx:VerilogParser.List_of_parameter_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#ordered_parameter_assignment.
    def visitOrdered_parameter_assignment(self, ctx:VerilogParser.Ordered_parameter_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#named_parameter_assignment.
    def visitNamed_parameter_assignment(self, ctx:VerilogParser.Named_parameter_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_instance.
    def visitModule_instance(self, ctx:VerilogParser.Module_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#name_of_module_instance.
    def visitName_of_module_instance(self, ctx:VerilogParser.Name_of_module_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_port_connections.
    def visitList_of_port_connections(self, ctx:VerilogParser.List_of_port_connectionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#ordered_port_connection.
    def visitOrdered_port_connection(self, ctx:VerilogParser.Ordered_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#named_port_connection.
    def visitNamed_port_connection(self, ctx:VerilogParser.Named_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#generate_region.
    def visitGenerate_region(self, ctx:VerilogParser.Generate_regionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#genvar_declaration.
    def visitGenvar_declaration(self, ctx:VerilogParser.Genvar_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_genvar_identifiers.
    def visitList_of_genvar_identifiers(self, ctx:VerilogParser.List_of_genvar_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#loop_generate_construct.
    def visitLoop_generate_construct(self, ctx:VerilogParser.Loop_generate_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#genvar_initialization.
    def visitGenvar_initialization(self, ctx:VerilogParser.Genvar_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#genvar_expression.
    def visitGenvar_expression(self, ctx:VerilogParser.Genvar_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#genvar_iteration.
    def visitGenvar_iteration(self, ctx:VerilogParser.Genvar_iterationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#genvar_primary.
    def visitGenvar_primary(self, ctx:VerilogParser.Genvar_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#conditional_generate_construct.
    def visitConditional_generate_construct(self, ctx:VerilogParser.Conditional_generate_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#if_generate_construct.
    def visitIf_generate_construct(self, ctx:VerilogParser.If_generate_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#case_generate_construct.
    def visitCase_generate_construct(self, ctx:VerilogParser.Case_generate_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#generate_block.
    def visitGenerate_block(self, ctx:VerilogParser.Generate_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#generate_block_or_null.
    def visitGenerate_block_or_null(self, ctx:VerilogParser.Generate_block_or_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#continuous_assign.
    def visitContinuous_assign(self, ctx:VerilogParser.Continuous_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_net_assignments.
    def visitList_of_net_assignments(self, ctx:VerilogParser.List_of_net_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_assignment.
    def visitNet_assignment(self, ctx:VerilogParser.Net_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#initial_construct.
    def visitInitial_construct(self, ctx:VerilogParser.Initial_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#always_construct.
    def visitAlways_construct(self, ctx:VerilogParser.Always_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#blocking_assignment.
    def visitBlocking_assignment(self, ctx:VerilogParser.Blocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#nonblocking_assignment.
    def visitNonblocking_assignment(self, ctx:VerilogParser.Nonblocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#procedural_continuous_assignments.
    def visitProcedural_continuous_assignments(self, ctx:VerilogParser.Procedural_continuous_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#variable_assignment.
    def visitVariable_assignment(self, ctx:VerilogParser.Variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#par_block.
    def visitPar_block(self, ctx:VerilogParser.Par_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#seq_block.
    def visitSeq_block(self, ctx:VerilogParser.Seq_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#statement.
    def visitStatement(self, ctx:VerilogParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#statement_or_null.
    def visitStatement_or_null(self, ctx:VerilogParser.Statement_or_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_statement.
    def visitFunction_statement(self, ctx:VerilogParser.Function_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delay_control.
    def visitDelay_control(self, ctx:VerilogParser.Delay_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#delay_or_event_control.
    def visitDelay_or_event_control(self, ctx:VerilogParser.Delay_or_event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#disable_statement.
    def visitDisable_statement(self, ctx:VerilogParser.Disable_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_control.
    def visitEvent_control(self, ctx:VerilogParser.Event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_trigger.
    def visitEvent_trigger(self, ctx:VerilogParser.Event_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_expression.
    def visitEvent_expression(self, ctx:VerilogParser.Event_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_primary.
    def visitEvent_primary(self, ctx:VerilogParser.Event_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#procedural_timing_control.
    def visitProcedural_timing_control(self, ctx:VerilogParser.Procedural_timing_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#procedural_timing_control_statement.
    def visitProcedural_timing_control_statement(self, ctx:VerilogParser.Procedural_timing_control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#wait_statement.
    def visitWait_statement(self, ctx:VerilogParser.Wait_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#conditional_statement.
    def visitConditional_statement(self, ctx:VerilogParser.Conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#case_statement.
    def visitCase_statement(self, ctx:VerilogParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#case_item.
    def visitCase_item(self, ctx:VerilogParser.Case_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#loop_statement.
    def visitLoop_statement(self, ctx:VerilogParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#system_task_enable.
    def visitSystem_task_enable(self, ctx:VerilogParser.System_task_enableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_enable.
    def visitTask_enable(self, ctx:VerilogParser.Task_enableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specify_block.
    def visitSpecify_block(self, ctx:VerilogParser.Specify_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specify_item.
    def visitSpecify_item(self, ctx:VerilogParser.Specify_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#pulsestyle_declaration.
    def visitPulsestyle_declaration(self, ctx:VerilogParser.Pulsestyle_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#showcancelled_declaration.
    def visitShowcancelled_declaration(self, ctx:VerilogParser.Showcancelled_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#path_declaration.
    def visitPath_declaration(self, ctx:VerilogParser.Path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#simple_path_declaration.
    def visitSimple_path_declaration(self, ctx:VerilogParser.Simple_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parallel_path_description.
    def visitParallel_path_description(self, ctx:VerilogParser.Parallel_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#full_path_description.
    def visitFull_path_description(self, ctx:VerilogParser.Full_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_path_inputs.
    def visitList_of_path_inputs(self, ctx:VerilogParser.List_of_path_inputsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_path_outputs.
    def visitList_of_path_outputs(self, ctx:VerilogParser.List_of_path_outputsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specify_input_terminal_descriptor.
    def visitSpecify_input_terminal_descriptor(self, ctx:VerilogParser.Specify_input_terminal_descriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specify_output_terminal_descriptor.
    def visitSpecify_output_terminal_descriptor(self, ctx:VerilogParser.Specify_output_terminal_descriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#input_identifier.
    def visitInput_identifier(self, ctx:VerilogParser.Input_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#output_identifier.
    def visitOutput_identifier(self, ctx:VerilogParser.Output_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#path_delay_value.
    def visitPath_delay_value(self, ctx:VerilogParser.Path_delay_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#list_of_path_delay_expressions.
    def visitList_of_path_delay_expressions(self, ctx:VerilogParser.List_of_path_delay_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t_path_delay_expression.
    def visitT_path_delay_expression(self, ctx:VerilogParser.T_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#trise_path_delay_expression.
    def visitTrise_path_delay_expression(self, ctx:VerilogParser.Trise_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tfall_path_delay_expression.
    def visitTfall_path_delay_expression(self, ctx:VerilogParser.Tfall_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tz_path_delay_expression.
    def visitTz_path_delay_expression(self, ctx:VerilogParser.Tz_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t01_path_delay_expression.
    def visitT01_path_delay_expression(self, ctx:VerilogParser.T01_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t10_path_delay_expression.
    def visitT10_path_delay_expression(self, ctx:VerilogParser.T10_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t0z_path_delay_expression.
    def visitT0z_path_delay_expression(self, ctx:VerilogParser.T0z_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tz1_path_delay_expression.
    def visitTz1_path_delay_expression(self, ctx:VerilogParser.Tz1_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t1z_path_delay_expression.
    def visitT1z_path_delay_expression(self, ctx:VerilogParser.T1z_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tz0_path_delay_expression.
    def visitTz0_path_delay_expression(self, ctx:VerilogParser.Tz0_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t0x_path_delay_expression.
    def visitT0x_path_delay_expression(self, ctx:VerilogParser.T0x_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tx1_path_delay_expression.
    def visitTx1_path_delay_expression(self, ctx:VerilogParser.Tx1_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#t1x_path_delay_expression.
    def visitT1x_path_delay_expression(self, ctx:VerilogParser.T1x_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tx0_path_delay_expression.
    def visitTx0_path_delay_expression(self, ctx:VerilogParser.Tx0_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#txz_path_delay_expression.
    def visitTxz_path_delay_expression(self, ctx:VerilogParser.Txz_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#tzx_path_delay_expression.
    def visitTzx_path_delay_expression(self, ctx:VerilogParser.Tzx_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#path_delay_expression.
    def visitPath_delay_expression(self, ctx:VerilogParser.Path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#edge_sensitive_path_declaration.
    def visitEdge_sensitive_path_declaration(self, ctx:VerilogParser.Edge_sensitive_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parallel_edge_sensitive_path_description.
    def visitParallel_edge_sensitive_path_description(self, ctx:VerilogParser.Parallel_edge_sensitive_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#full_edge_sensitive_path_description.
    def visitFull_edge_sensitive_path_description(self, ctx:VerilogParser.Full_edge_sensitive_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#data_source_expression.
    def visitData_source_expression(self, ctx:VerilogParser.Data_source_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#edge_identifier.
    def visitEdge_identifier(self, ctx:VerilogParser.Edge_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#state_dependent_path_declaration.
    def visitState_dependent_path_declaration(self, ctx:VerilogParser.State_dependent_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#polarity_operator.
    def visitPolarity_operator(self, ctx:VerilogParser.Polarity_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#concatenation.
    def visitConcatenation(self, ctx:VerilogParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_concatenation.
    def visitConstant_concatenation(self, ctx:VerilogParser.Constant_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_multiple_concatenation.
    def visitConstant_multiple_concatenation(self, ctx:VerilogParser.Constant_multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_path_concatenation.
    def visitModule_path_concatenation(self, ctx:VerilogParser.Module_path_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_path_multiple_concatenation.
    def visitModule_path_multiple_concatenation(self, ctx:VerilogParser.Module_path_multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#multiple_concatenation.
    def visitMultiple_concatenation(self, ctx:VerilogParser.Multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_function_call.
    def visitConstant_function_call(self, ctx:VerilogParser.Constant_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_system_function_call.
    def visitConstant_system_function_call(self, ctx:VerilogParser.Constant_system_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_call.
    def visitFunction_call(self, ctx:VerilogParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#system_function_call.
    def visitSystem_function_call(self, ctx:VerilogParser.System_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#base_expression.
    def visitBase_expression(self, ctx:VerilogParser.Base_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_base_expression.
    def visitConstant_base_expression(self, ctx:VerilogParser.Constant_base_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_expression.
    def visitConstant_expression(self, ctx:VerilogParser.Constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_mintypmax_expression.
    def visitConstant_mintypmax_expression(self, ctx:VerilogParser.Constant_mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_range_expression.
    def visitConstant_range_expression(self, ctx:VerilogParser.Constant_range_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#dimension_constant_expression.
    def visitDimension_constant_expression(self, ctx:VerilogParser.Dimension_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#expression.
    def visitExpression(self, ctx:VerilogParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#lsb_constant_expression.
    def visitLsb_constant_expression(self, ctx:VerilogParser.Lsb_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#mintypmax_expression.
    def visitMintypmax_expression(self, ctx:VerilogParser.Mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_path_expression.
    def visitModule_path_expression(self, ctx:VerilogParser.Module_path_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_path_mintypmax_expression.
    def visitModule_path_mintypmax_expression(self, ctx:VerilogParser.Module_path_mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#msb_constant_expression.
    def visitMsb_constant_expression(self, ctx:VerilogParser.Msb_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#range_expression.
    def visitRange_expression(self, ctx:VerilogParser.Range_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#width_constant_expression.
    def visitWidth_constant_expression(self, ctx:VerilogParser.Width_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#constant_primary.
    def visitConstant_primary(self, ctx:VerilogParser.Constant_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_path_primary.
    def visitModule_path_primary(self, ctx:VerilogParser.Module_path_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#primary.
    def visitPrimary(self, ctx:VerilogParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_lvalue.
    def visitNet_lvalue(self, ctx:VerilogParser.Net_lvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#variable_lvalue.
    def visitVariable_lvalue(self, ctx:VerilogParser.Variable_lvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#unary_operator.
    def visitUnary_operator(self, ctx:VerilogParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#binary_operator.
    def visitBinary_operator(self, ctx:VerilogParser.Binary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#unary_module_path_operator.
    def visitUnary_module_path_operator(self, ctx:VerilogParser.Unary_module_path_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#binary_module_path_operator.
    def visitBinary_module_path_operator(self, ctx:VerilogParser.Binary_module_path_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#number.
    def visitNumber(self, ctx:VerilogParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#attribute_instance.
    def visitAttribute_instance(self, ctx:VerilogParser.Attribute_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#attr_spec.
    def visitAttr_spec(self, ctx:VerilogParser.Attr_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#attr_name.
    def visitAttr_name(self, ctx:VerilogParser.Attr_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#block_identifier.
    def visitBlock_identifier(self, ctx:VerilogParser.Block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#cell_identifier.
    def visitCell_identifier(self, ctx:VerilogParser.Cell_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#config_identifier.
    def visitConfig_identifier(self, ctx:VerilogParser.Config_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#event_identifier.
    def visitEvent_identifier(self, ctx:VerilogParser.Event_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_identifier.
    def visitFunction_identifier(self, ctx:VerilogParser.Function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#gate_instance_identifier.
    def visitGate_instance_identifier(self, ctx:VerilogParser.Gate_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#generate_block_identifier.
    def visitGenerate_block_identifier(self, ctx:VerilogParser.Generate_block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#genvar_identifier.
    def visitGenvar_identifier(self, ctx:VerilogParser.Genvar_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hierarchical_block_identifier.
    def visitHierarchical_block_identifier(self, ctx:VerilogParser.Hierarchical_block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hierarchical_event_identifier.
    def visitHierarchical_event_identifier(self, ctx:VerilogParser.Hierarchical_event_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hierarchical_function_identifier.
    def visitHierarchical_function_identifier(self, ctx:VerilogParser.Hierarchical_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hierarchical_identifier.
    def visitHierarchical_identifier(self, ctx:VerilogParser.Hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hierarchical_net_identifier.
    def visitHierarchical_net_identifier(self, ctx:VerilogParser.Hierarchical_net_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hierarchical_parameter_identifier.
    def visitHierarchical_parameter_identifier(self, ctx:VerilogParser.Hierarchical_parameter_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hierarchical_variable_identifier.
    def visitHierarchical_variable_identifier(self, ctx:VerilogParser.Hierarchical_variable_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#hierarchical_task_identifier.
    def visitHierarchical_task_identifier(self, ctx:VerilogParser.Hierarchical_task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#identifier.
    def visitIdentifier(self, ctx:VerilogParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#inout_port_identifier.
    def visitInout_port_identifier(self, ctx:VerilogParser.Inout_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#input_port_identifier.
    def visitInput_port_identifier(self, ctx:VerilogParser.Input_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#instance_identifier.
    def visitInstance_identifier(self, ctx:VerilogParser.Instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#library_identifier.
    def visitLibrary_identifier(self, ctx:VerilogParser.Library_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_identifier.
    def visitModule_identifier(self, ctx:VerilogParser.Module_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_instance_identifier.
    def visitModule_instance_identifier(self, ctx:VerilogParser.Module_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#net_identifier.
    def visitNet_identifier(self, ctx:VerilogParser.Net_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#output_port_identifier.
    def visitOutput_port_identifier(self, ctx:VerilogParser.Output_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#parameter_identifier.
    def visitParameter_identifier(self, ctx:VerilogParser.Parameter_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#port_identifier.
    def visitPort_identifier(self, ctx:VerilogParser.Port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#real_identifier.
    def visitReal_identifier(self, ctx:VerilogParser.Real_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#specparam_identifier.
    def visitSpecparam_identifier(self, ctx:VerilogParser.Specparam_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#system_function_identifier.
    def visitSystem_function_identifier(self, ctx:VerilogParser.System_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#system_task_identifier.
    def visitSystem_task_identifier(self, ctx:VerilogParser.System_task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_identifier.
    def visitTask_identifier(self, ctx:VerilogParser.Task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#terminal_identifier.
    def visitTerminal_identifier(self, ctx:VerilogParser.Terminal_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#topmodule_identifier.
    def visitTopmodule_identifier(self, ctx:VerilogParser.Topmodule_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_identifier.
    def visitUdp_identifier(self, ctx:VerilogParser.Udp_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#udp_instance_identifier.
    def visitUdp_instance_identifier(self, ctx:VerilogParser.Udp_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#variable_identifier.
    def visitVariable_identifier(self, ctx:VerilogParser.Variable_identifierContext):
        return self.visitChildren(ctx)



del VerilogParser