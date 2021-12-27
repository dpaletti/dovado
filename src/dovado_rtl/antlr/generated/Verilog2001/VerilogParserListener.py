# Generated from VerilogParser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VerilogParser import VerilogParser
else:
    from VerilogParser import VerilogParser

# This class defines a complete listener for a parse tree produced by VerilogParser.
class VerilogParserListener(ParseTreeListener):

    # Enter a parse tree produced by VerilogParser#display_tasks.
    def enterDisplay_tasks(self, ctx:VerilogParser.Display_tasksContext):
        pass

    # Exit a parse tree produced by VerilogParser#display_tasks.
    def exitDisplay_tasks(self, ctx:VerilogParser.Display_tasksContext):
        pass


    # Enter a parse tree produced by VerilogParser#display_task_name.
    def enterDisplay_task_name(self, ctx:VerilogParser.Display_task_nameContext):
        pass

    # Exit a parse tree produced by VerilogParser#display_task_name.
    def exitDisplay_task_name(self, ctx:VerilogParser.Display_task_nameContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_arguments.
    def enterList_of_arguments(self, ctx:VerilogParser.List_of_argumentsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_arguments.
    def exitList_of_arguments(self, ctx:VerilogParser.List_of_argumentsContext):
        pass


    # Enter a parse tree produced by VerilogParser#argument.
    def enterArgument(self, ctx:VerilogParser.ArgumentContext):
        pass

    # Exit a parse tree produced by VerilogParser#argument.
    def exitArgument(self, ctx:VerilogParser.ArgumentContext):
        pass


    # Enter a parse tree produced by VerilogParser#strobe_tasks.
    def enterStrobe_tasks(self, ctx:VerilogParser.Strobe_tasksContext):
        pass

    # Exit a parse tree produced by VerilogParser#strobe_tasks.
    def exitStrobe_tasks(self, ctx:VerilogParser.Strobe_tasksContext):
        pass


    # Enter a parse tree produced by VerilogParser#strobe_task_name.
    def enterStrobe_task_name(self, ctx:VerilogParser.Strobe_task_nameContext):
        pass

    # Exit a parse tree produced by VerilogParser#strobe_task_name.
    def exitStrobe_task_name(self, ctx:VerilogParser.Strobe_task_nameContext):
        pass


    # Enter a parse tree produced by VerilogParser#monitor_tasks.
    def enterMonitor_tasks(self, ctx:VerilogParser.Monitor_tasksContext):
        pass

    # Exit a parse tree produced by VerilogParser#monitor_tasks.
    def exitMonitor_tasks(self, ctx:VerilogParser.Monitor_tasksContext):
        pass


    # Enter a parse tree produced by VerilogParser#monitor_task_name.
    def enterMonitor_task_name(self, ctx:VerilogParser.Monitor_task_nameContext):
        pass

    # Exit a parse tree produced by VerilogParser#monitor_task_name.
    def exitMonitor_task_name(self, ctx:VerilogParser.Monitor_task_nameContext):
        pass


    # Enter a parse tree produced by VerilogParser#file_open_function.
    def enterFile_open_function(self, ctx:VerilogParser.File_open_functionContext):
        pass

    # Exit a parse tree produced by VerilogParser#file_open_function.
    def exitFile_open_function(self, ctx:VerilogParser.File_open_functionContext):
        pass


    # Enter a parse tree produced by VerilogParser#file_close_task.
    def enterFile_close_task(self, ctx:VerilogParser.File_close_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#file_close_task.
    def exitFile_close_task(self, ctx:VerilogParser.File_close_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#multi_channel_descriptor.
    def enterMulti_channel_descriptor(self, ctx:VerilogParser.Multi_channel_descriptorContext):
        pass

    # Exit a parse tree produced by VerilogParser#multi_channel_descriptor.
    def exitMulti_channel_descriptor(self, ctx:VerilogParser.Multi_channel_descriptorContext):
        pass


    # Enter a parse tree produced by VerilogParser#fd.
    def enterFd(self, ctx:VerilogParser.FdContext):
        pass

    # Exit a parse tree produced by VerilogParser#fd.
    def exitFd(self, ctx:VerilogParser.FdContext):
        pass


    # Enter a parse tree produced by VerilogParser#file_name.
    def enterFile_name(self, ctx:VerilogParser.File_nameContext):
        pass

    # Exit a parse tree produced by VerilogParser#file_name.
    def exitFile_name(self, ctx:VerilogParser.File_nameContext):
        pass


    # Enter a parse tree produced by VerilogParser#type_.
    def enterType_(self, ctx:VerilogParser.Type_Context):
        pass

    # Exit a parse tree produced by VerilogParser#type_.
    def exitType_(self, ctx:VerilogParser.Type_Context):
        pass


    # Enter a parse tree produced by VerilogParser#file_output_tasks.
    def enterFile_output_tasks(self, ctx:VerilogParser.File_output_tasksContext):
        pass

    # Exit a parse tree produced by VerilogParser#file_output_tasks.
    def exitFile_output_tasks(self, ctx:VerilogParser.File_output_tasksContext):
        pass


    # Enter a parse tree produced by VerilogParser#file_output_task_name.
    def enterFile_output_task_name(self, ctx:VerilogParser.File_output_task_nameContext):
        pass

    # Exit a parse tree produced by VerilogParser#file_output_task_name.
    def exitFile_output_task_name(self, ctx:VerilogParser.File_output_task_nameContext):
        pass


    # Enter a parse tree produced by VerilogParser#load_memory_tasks.
    def enterLoad_memory_tasks(self, ctx:VerilogParser.Load_memory_tasksContext):
        pass

    # Exit a parse tree produced by VerilogParser#load_memory_tasks.
    def exitLoad_memory_tasks(self, ctx:VerilogParser.Load_memory_tasksContext):
        pass


    # Enter a parse tree produced by VerilogParser#memory_name.
    def enterMemory_name(self, ctx:VerilogParser.Memory_nameContext):
        pass

    # Exit a parse tree produced by VerilogParser#memory_name.
    def exitMemory_name(self, ctx:VerilogParser.Memory_nameContext):
        pass


    # Enter a parse tree produced by VerilogParser#start_addr.
    def enterStart_addr(self, ctx:VerilogParser.Start_addrContext):
        pass

    # Exit a parse tree produced by VerilogParser#start_addr.
    def exitStart_addr(self, ctx:VerilogParser.Start_addrContext):
        pass


    # Enter a parse tree produced by VerilogParser#finish_addr.
    def enterFinish_addr(self, ctx:VerilogParser.Finish_addrContext):
        pass

    # Exit a parse tree produced by VerilogParser#finish_addr.
    def exitFinish_addr(self, ctx:VerilogParser.Finish_addrContext):
        pass


    # Enter a parse tree produced by VerilogParser#filename.
    def enterFilename(self, ctx:VerilogParser.FilenameContext):
        pass

    # Exit a parse tree produced by VerilogParser#filename.
    def exitFilename(self, ctx:VerilogParser.FilenameContext):
        pass


    # Enter a parse tree produced by VerilogParser#finish_task.
    def enterFinish_task(self, ctx:VerilogParser.Finish_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#finish_task.
    def exitFinish_task(self, ctx:VerilogParser.Finish_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#finish_number.
    def enterFinish_number(self, ctx:VerilogParser.Finish_numberContext):
        pass

    # Exit a parse tree produced by VerilogParser#finish_number.
    def exitFinish_number(self, ctx:VerilogParser.Finish_numberContext):
        pass


    # Enter a parse tree produced by VerilogParser#stop_task.
    def enterStop_task(self, ctx:VerilogParser.Stop_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#stop_task.
    def exitStop_task(self, ctx:VerilogParser.Stop_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#time_function.
    def enterTime_function(self, ctx:VerilogParser.Time_functionContext):
        pass

    # Exit a parse tree produced by VerilogParser#time_function.
    def exitTime_function(self, ctx:VerilogParser.Time_functionContext):
        pass


    # Enter a parse tree produced by VerilogParser#stime_function.
    def enterStime_function(self, ctx:VerilogParser.Stime_functionContext):
        pass

    # Exit a parse tree produced by VerilogParser#stime_function.
    def exitStime_function(self, ctx:VerilogParser.Stime_functionContext):
        pass


    # Enter a parse tree produced by VerilogParser#realtime_function.
    def enterRealtime_function(self, ctx:VerilogParser.Realtime_functionContext):
        pass

    # Exit a parse tree produced by VerilogParser#realtime_function.
    def exitRealtime_function(self, ctx:VerilogParser.Realtime_functionContext):
        pass


    # Enter a parse tree produced by VerilogParser#conversion_functions.
    def enterConversion_functions(self, ctx:VerilogParser.Conversion_functionsContext):
        pass

    # Exit a parse tree produced by VerilogParser#conversion_functions.
    def exitConversion_functions(self, ctx:VerilogParser.Conversion_functionsContext):
        pass


    # Enter a parse tree produced by VerilogParser#conversion_function_name.
    def enterConversion_function_name(self, ctx:VerilogParser.Conversion_function_nameContext):
        pass

    # Exit a parse tree produced by VerilogParser#conversion_function_name.
    def exitConversion_function_name(self, ctx:VerilogParser.Conversion_function_nameContext):
        pass


    # Enter a parse tree produced by VerilogParser#constant_argument.
    def enterConstant_argument(self, ctx:VerilogParser.Constant_argumentContext):
        pass

    # Exit a parse tree produced by VerilogParser#constant_argument.
    def exitConstant_argument(self, ctx:VerilogParser.Constant_argumentContext):
        pass


    # Enter a parse tree produced by VerilogParser#random_function.
    def enterRandom_function(self, ctx:VerilogParser.Random_functionContext):
        pass

    # Exit a parse tree produced by VerilogParser#random_function.
    def exitRandom_function(self, ctx:VerilogParser.Random_functionContext):
        pass


    # Enter a parse tree produced by VerilogParser#seed.
    def enterSeed(self, ctx:VerilogParser.SeedContext):
        pass

    # Exit a parse tree produced by VerilogParser#seed.
    def exitSeed(self, ctx:VerilogParser.SeedContext):
        pass


    # Enter a parse tree produced by VerilogParser#dist_functions.
    def enterDist_functions(self, ctx:VerilogParser.Dist_functionsContext):
        pass

    # Exit a parse tree produced by VerilogParser#dist_functions.
    def exitDist_functions(self, ctx:VerilogParser.Dist_functionsContext):
        pass


    # Enter a parse tree produced by VerilogParser#start_.
    def enterStart_(self, ctx:VerilogParser.Start_Context):
        pass

    # Exit a parse tree produced by VerilogParser#start_.
    def exitStart_(self, ctx:VerilogParser.Start_Context):
        pass


    # Enter a parse tree produced by VerilogParser#end.
    def enterEnd(self, ctx:VerilogParser.EndContext):
        pass

    # Exit a parse tree produced by VerilogParser#end.
    def exitEnd(self, ctx:VerilogParser.EndContext):
        pass


    # Enter a parse tree produced by VerilogParser#mean.
    def enterMean(self, ctx:VerilogParser.MeanContext):
        pass

    # Exit a parse tree produced by VerilogParser#mean.
    def exitMean(self, ctx:VerilogParser.MeanContext):
        pass


    # Enter a parse tree produced by VerilogParser#standard_deviation.
    def enterStandard_deviation(self, ctx:VerilogParser.Standard_deviationContext):
        pass

    # Exit a parse tree produced by VerilogParser#standard_deviation.
    def exitStandard_deviation(self, ctx:VerilogParser.Standard_deviationContext):
        pass


    # Enter a parse tree produced by VerilogParser#degree_of_freedom.
    def enterDegree_of_freedom(self, ctx:VerilogParser.Degree_of_freedomContext):
        pass

    # Exit a parse tree produced by VerilogParser#degree_of_freedom.
    def exitDegree_of_freedom(self, ctx:VerilogParser.Degree_of_freedomContext):
        pass


    # Enter a parse tree produced by VerilogParser#k_stage.
    def enterK_stage(self, ctx:VerilogParser.K_stageContext):
        pass

    # Exit a parse tree produced by VerilogParser#k_stage.
    def exitK_stage(self, ctx:VerilogParser.K_stageContext):
        pass


    # Enter a parse tree produced by VerilogParser#math_functions.
    def enterMath_functions(self, ctx:VerilogParser.Math_functionsContext):
        pass

    # Exit a parse tree produced by VerilogParser#math_functions.
    def exitMath_functions(self, ctx:VerilogParser.Math_functionsContext):
        pass


    # Enter a parse tree produced by VerilogParser#integer_math_functions.
    def enterInteger_math_functions(self, ctx:VerilogParser.Integer_math_functionsContext):
        pass

    # Exit a parse tree produced by VerilogParser#integer_math_functions.
    def exitInteger_math_functions(self, ctx:VerilogParser.Integer_math_functionsContext):
        pass


    # Enter a parse tree produced by VerilogParser#real_math_functions.
    def enterReal_math_functions(self, ctx:VerilogParser.Real_math_functionsContext):
        pass

    # Exit a parse tree produced by VerilogParser#real_math_functions.
    def exitReal_math_functions(self, ctx:VerilogParser.Real_math_functionsContext):
        pass


    # Enter a parse tree produced by VerilogParser#single_argument_real_math_function_name.
    def enterSingle_argument_real_math_function_name(self, ctx:VerilogParser.Single_argument_real_math_function_nameContext):
        pass

    # Exit a parse tree produced by VerilogParser#single_argument_real_math_function_name.
    def exitSingle_argument_real_math_function_name(self, ctx:VerilogParser.Single_argument_real_math_function_nameContext):
        pass


    # Enter a parse tree produced by VerilogParser#double_argument_real_math_function_name.
    def enterDouble_argument_real_math_function_name(self, ctx:VerilogParser.Double_argument_real_math_function_nameContext):
        pass

    # Exit a parse tree produced by VerilogParser#double_argument_real_math_function_name.
    def exitDouble_argument_real_math_function_name(self, ctx:VerilogParser.Double_argument_real_math_function_nameContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpfile_task.
    def enterDumpfile_task(self, ctx:VerilogParser.Dumpfile_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpfile_task.
    def exitDumpfile_task(self, ctx:VerilogParser.Dumpfile_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpvars_task.
    def enterDumpvars_task(self, ctx:VerilogParser.Dumpvars_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpvars_task.
    def exitDumpvars_task(self, ctx:VerilogParser.Dumpvars_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_modules_or_variables.
    def enterList_of_modules_or_variables(self, ctx:VerilogParser.List_of_modules_or_variablesContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_modules_or_variables.
    def exitList_of_modules_or_variables(self, ctx:VerilogParser.List_of_modules_or_variablesContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_or_variable.
    def enterModule_or_variable(self, ctx:VerilogParser.Module_or_variableContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_or_variable.
    def exitModule_or_variable(self, ctx:VerilogParser.Module_or_variableContext):
        pass


    # Enter a parse tree produced by VerilogParser#levels.
    def enterLevels(self, ctx:VerilogParser.LevelsContext):
        pass

    # Exit a parse tree produced by VerilogParser#levels.
    def exitLevels(self, ctx:VerilogParser.LevelsContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpoff_task.
    def enterDumpoff_task(self, ctx:VerilogParser.Dumpoff_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpoff_task.
    def exitDumpoff_task(self, ctx:VerilogParser.Dumpoff_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpon_task.
    def enterDumpon_task(self, ctx:VerilogParser.Dumpon_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpon_task.
    def exitDumpon_task(self, ctx:VerilogParser.Dumpon_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpall_task.
    def enterDumpall_task(self, ctx:VerilogParser.Dumpall_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpall_task.
    def exitDumpall_task(self, ctx:VerilogParser.Dumpall_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumplimit_task.
    def enterDumplimit_task(self, ctx:VerilogParser.Dumplimit_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumplimit_task.
    def exitDumplimit_task(self, ctx:VerilogParser.Dumplimit_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#file_size.
    def enterFile_size(self, ctx:VerilogParser.File_sizeContext):
        pass

    # Exit a parse tree produced by VerilogParser#file_size.
    def exitFile_size(self, ctx:VerilogParser.File_sizeContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpflush_task.
    def enterDumpflush_task(self, ctx:VerilogParser.Dumpflush_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpflush_task.
    def exitDumpflush_task(self, ctx:VerilogParser.Dumpflush_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpports_task.
    def enterDumpports_task(self, ctx:VerilogParser.Dumpports_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpports_task.
    def exitDumpports_task(self, ctx:VerilogParser.Dumpports_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#scope_list.
    def enterScope_list(self, ctx:VerilogParser.Scope_listContext):
        pass

    # Exit a parse tree produced by VerilogParser#scope_list.
    def exitScope_list(self, ctx:VerilogParser.Scope_listContext):
        pass


    # Enter a parse tree produced by VerilogParser#file_pathname.
    def enterFile_pathname(self, ctx:VerilogParser.File_pathnameContext):
        pass

    # Exit a parse tree produced by VerilogParser#file_pathname.
    def exitFile_pathname(self, ctx:VerilogParser.File_pathnameContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpportsoff_task.
    def enterDumpportsoff_task(self, ctx:VerilogParser.Dumpportsoff_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpportsoff_task.
    def exitDumpportsoff_task(self, ctx:VerilogParser.Dumpportsoff_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpportson_task.
    def enterDumpportson_task(self, ctx:VerilogParser.Dumpportson_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpportson_task.
    def exitDumpportson_task(self, ctx:VerilogParser.Dumpportson_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpportsall_task.
    def enterDumpportsall_task(self, ctx:VerilogParser.Dumpportsall_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpportsall_task.
    def exitDumpportsall_task(self, ctx:VerilogParser.Dumpportsall_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpportslimit_task.
    def enterDumpportslimit_task(self, ctx:VerilogParser.Dumpportslimit_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpportslimit_task.
    def exitDumpportslimit_task(self, ctx:VerilogParser.Dumpportslimit_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#dumpportsflush_task.
    def enterDumpportsflush_task(self, ctx:VerilogParser.Dumpportsflush_taskContext):
        pass

    # Exit a parse tree produced by VerilogParser#dumpportsflush_task.
    def exitDumpportsflush_task(self, ctx:VerilogParser.Dumpportsflush_taskContext):
        pass


    # Enter a parse tree produced by VerilogParser#library_text.
    def enterLibrary_text(self, ctx:VerilogParser.Library_textContext):
        pass

    # Exit a parse tree produced by VerilogParser#library_text.
    def exitLibrary_text(self, ctx:VerilogParser.Library_textContext):
        pass


    # Enter a parse tree produced by VerilogParser#library_description.
    def enterLibrary_description(self, ctx:VerilogParser.Library_descriptionContext):
        pass

    # Exit a parse tree produced by VerilogParser#library_description.
    def exitLibrary_description(self, ctx:VerilogParser.Library_descriptionContext):
        pass


    # Enter a parse tree produced by VerilogParser#library_declaration.
    def enterLibrary_declaration(self, ctx:VerilogParser.Library_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#library_declaration.
    def exitLibrary_declaration(self, ctx:VerilogParser.Library_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#include_statement.
    def enterInclude_statement(self, ctx:VerilogParser.Include_statementContext):
        pass

    # Exit a parse tree produced by VerilogParser#include_statement.
    def exitInclude_statement(self, ctx:VerilogParser.Include_statementContext):
        pass


    # Enter a parse tree produced by VerilogParser#source_text.
    def enterSource_text(self, ctx:VerilogParser.Source_textContext):
        pass

    # Exit a parse tree produced by VerilogParser#source_text.
    def exitSource_text(self, ctx:VerilogParser.Source_textContext):
        pass


    # Enter a parse tree produced by VerilogParser#description.
    def enterDescription(self, ctx:VerilogParser.DescriptionContext):
        pass

    # Exit a parse tree produced by VerilogParser#description.
    def exitDescription(self, ctx:VerilogParser.DescriptionContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_declaration.
    def enterModule_declaration(self, ctx:VerilogParser.Module_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_declaration.
    def exitModule_declaration(self, ctx:VerilogParser.Module_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_keyword.
    def enterModule_keyword(self, ctx:VerilogParser.Module_keywordContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_keyword.
    def exitModule_keyword(self, ctx:VerilogParser.Module_keywordContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_parameter_port_list.
    def enterModule_parameter_port_list(self, ctx:VerilogParser.Module_parameter_port_listContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_parameter_port_list.
    def exitModule_parameter_port_list(self, ctx:VerilogParser.Module_parameter_port_listContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_ports.
    def enterList_of_ports(self, ctx:VerilogParser.List_of_portsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_ports.
    def exitList_of_ports(self, ctx:VerilogParser.List_of_portsContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_port_declarations.
    def enterList_of_port_declarations(self, ctx:VerilogParser.List_of_port_declarationsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_port_declarations.
    def exitList_of_port_declarations(self, ctx:VerilogParser.List_of_port_declarationsContext):
        pass


    # Enter a parse tree produced by VerilogParser#port.
    def enterPort(self, ctx:VerilogParser.PortContext):
        pass

    # Exit a parse tree produced by VerilogParser#port.
    def exitPort(self, ctx:VerilogParser.PortContext):
        pass


    # Enter a parse tree produced by VerilogParser#port_expression.
    def enterPort_expression(self, ctx:VerilogParser.Port_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#port_expression.
    def exitPort_expression(self, ctx:VerilogParser.Port_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#port_reference.
    def enterPort_reference(self, ctx:VerilogParser.Port_referenceContext):
        pass

    # Exit a parse tree produced by VerilogParser#port_reference.
    def exitPort_reference(self, ctx:VerilogParser.Port_referenceContext):
        pass


    # Enter a parse tree produced by VerilogParser#port_declaration.
    def enterPort_declaration(self, ctx:VerilogParser.Port_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#port_declaration.
    def exitPort_declaration(self, ctx:VerilogParser.Port_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_item.
    def enterModule_item(self, ctx:VerilogParser.Module_itemContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_item.
    def exitModule_item(self, ctx:VerilogParser.Module_itemContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_or_generate_item.
    def enterModule_or_generate_item(self, ctx:VerilogParser.Module_or_generate_itemContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_or_generate_item.
    def exitModule_or_generate_item(self, ctx:VerilogParser.Module_or_generate_itemContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_or_generate_item_declaration.
    def enterModule_or_generate_item_declaration(self, ctx:VerilogParser.Module_or_generate_item_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_or_generate_item_declaration.
    def exitModule_or_generate_item_declaration(self, ctx:VerilogParser.Module_or_generate_item_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#non_port_module_item.
    def enterNon_port_module_item(self, ctx:VerilogParser.Non_port_module_itemContext):
        pass

    # Exit a parse tree produced by VerilogParser#non_port_module_item.
    def exitNon_port_module_item(self, ctx:VerilogParser.Non_port_module_itemContext):
        pass


    # Enter a parse tree produced by VerilogParser#parameter_override.
    def enterParameter_override(self, ctx:VerilogParser.Parameter_overrideContext):
        pass

    # Exit a parse tree produced by VerilogParser#parameter_override.
    def exitParameter_override(self, ctx:VerilogParser.Parameter_overrideContext):
        pass


    # Enter a parse tree produced by VerilogParser#config_declaration.
    def enterConfig_declaration(self, ctx:VerilogParser.Config_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#config_declaration.
    def exitConfig_declaration(self, ctx:VerilogParser.Config_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#design_statement.
    def enterDesign_statement(self, ctx:VerilogParser.Design_statementContext):
        pass

    # Exit a parse tree produced by VerilogParser#design_statement.
    def exitDesign_statement(self, ctx:VerilogParser.Design_statementContext):
        pass


    # Enter a parse tree produced by VerilogParser#config_rule_statement.
    def enterConfig_rule_statement(self, ctx:VerilogParser.Config_rule_statementContext):
        pass

    # Exit a parse tree produced by VerilogParser#config_rule_statement.
    def exitConfig_rule_statement(self, ctx:VerilogParser.Config_rule_statementContext):
        pass


    # Enter a parse tree produced by VerilogParser#default_clause.
    def enterDefault_clause(self, ctx:VerilogParser.Default_clauseContext):
        pass

    # Exit a parse tree produced by VerilogParser#default_clause.
    def exitDefault_clause(self, ctx:VerilogParser.Default_clauseContext):
        pass


    # Enter a parse tree produced by VerilogParser#inst_clause.
    def enterInst_clause(self, ctx:VerilogParser.Inst_clauseContext):
        pass

    # Exit a parse tree produced by VerilogParser#inst_clause.
    def exitInst_clause(self, ctx:VerilogParser.Inst_clauseContext):
        pass


    # Enter a parse tree produced by VerilogParser#inst_name.
    def enterInst_name(self, ctx:VerilogParser.Inst_nameContext):
        pass

    # Exit a parse tree produced by VerilogParser#inst_name.
    def exitInst_name(self, ctx:VerilogParser.Inst_nameContext):
        pass


    # Enter a parse tree produced by VerilogParser#cell_clause.
    def enterCell_clause(self, ctx:VerilogParser.Cell_clauseContext):
        pass

    # Exit a parse tree produced by VerilogParser#cell_clause.
    def exitCell_clause(self, ctx:VerilogParser.Cell_clauseContext):
        pass


    # Enter a parse tree produced by VerilogParser#liblist_clause.
    def enterLiblist_clause(self, ctx:VerilogParser.Liblist_clauseContext):
        pass

    # Exit a parse tree produced by VerilogParser#liblist_clause.
    def exitLiblist_clause(self, ctx:VerilogParser.Liblist_clauseContext):
        pass


    # Enter a parse tree produced by VerilogParser#use_clause.
    def enterUse_clause(self, ctx:VerilogParser.Use_clauseContext):
        pass

    # Exit a parse tree produced by VerilogParser#use_clause.
    def exitUse_clause(self, ctx:VerilogParser.Use_clauseContext):
        pass


    # Enter a parse tree produced by VerilogParser#local_parameter_declaration.
    def enterLocal_parameter_declaration(self, ctx:VerilogParser.Local_parameter_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#local_parameter_declaration.
    def exitLocal_parameter_declaration(self, ctx:VerilogParser.Local_parameter_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#parameter_declaration.
    def enterParameter_declaration(self, ctx:VerilogParser.Parameter_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#parameter_declaration.
    def exitParameter_declaration(self, ctx:VerilogParser.Parameter_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#specparam_declaration.
    def enterSpecparam_declaration(self, ctx:VerilogParser.Specparam_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#specparam_declaration.
    def exitSpecparam_declaration(self, ctx:VerilogParser.Specparam_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#parameter_type.
    def enterParameter_type(self, ctx:VerilogParser.Parameter_typeContext):
        pass

    # Exit a parse tree produced by VerilogParser#parameter_type.
    def exitParameter_type(self, ctx:VerilogParser.Parameter_typeContext):
        pass


    # Enter a parse tree produced by VerilogParser#inout_declaration.
    def enterInout_declaration(self, ctx:VerilogParser.Inout_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#inout_declaration.
    def exitInout_declaration(self, ctx:VerilogParser.Inout_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#input_declaration.
    def enterInput_declaration(self, ctx:VerilogParser.Input_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#input_declaration.
    def exitInput_declaration(self, ctx:VerilogParser.Input_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#output_declaration.
    def enterOutput_declaration(self, ctx:VerilogParser.Output_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#output_declaration.
    def exitOutput_declaration(self, ctx:VerilogParser.Output_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#event_declaration.
    def enterEvent_declaration(self, ctx:VerilogParser.Event_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#event_declaration.
    def exitEvent_declaration(self, ctx:VerilogParser.Event_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#integer_declaration.
    def enterInteger_declaration(self, ctx:VerilogParser.Integer_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#integer_declaration.
    def exitInteger_declaration(self, ctx:VerilogParser.Integer_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#net_declaration.
    def enterNet_declaration(self, ctx:VerilogParser.Net_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#net_declaration.
    def exitNet_declaration(self, ctx:VerilogParser.Net_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#real_declaration.
    def enterReal_declaration(self, ctx:VerilogParser.Real_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#real_declaration.
    def exitReal_declaration(self, ctx:VerilogParser.Real_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#realtime_declaration.
    def enterRealtime_declaration(self, ctx:VerilogParser.Realtime_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#realtime_declaration.
    def exitRealtime_declaration(self, ctx:VerilogParser.Realtime_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#reg_declaration.
    def enterReg_declaration(self, ctx:VerilogParser.Reg_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#reg_declaration.
    def exitReg_declaration(self, ctx:VerilogParser.Reg_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#time_declaration.
    def enterTime_declaration(self, ctx:VerilogParser.Time_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#time_declaration.
    def exitTime_declaration(self, ctx:VerilogParser.Time_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#net_type.
    def enterNet_type(self, ctx:VerilogParser.Net_typeContext):
        pass

    # Exit a parse tree produced by VerilogParser#net_type.
    def exitNet_type(self, ctx:VerilogParser.Net_typeContext):
        pass


    # Enter a parse tree produced by VerilogParser#output_variable_type.
    def enterOutput_variable_type(self, ctx:VerilogParser.Output_variable_typeContext):
        pass

    # Exit a parse tree produced by VerilogParser#output_variable_type.
    def exitOutput_variable_type(self, ctx:VerilogParser.Output_variable_typeContext):
        pass


    # Enter a parse tree produced by VerilogParser#real_type.
    def enterReal_type(self, ctx:VerilogParser.Real_typeContext):
        pass

    # Exit a parse tree produced by VerilogParser#real_type.
    def exitReal_type(self, ctx:VerilogParser.Real_typeContext):
        pass


    # Enter a parse tree produced by VerilogParser#variable_type.
    def enterVariable_type(self, ctx:VerilogParser.Variable_typeContext):
        pass

    # Exit a parse tree produced by VerilogParser#variable_type.
    def exitVariable_type(self, ctx:VerilogParser.Variable_typeContext):
        pass


    # Enter a parse tree produced by VerilogParser#drive_strength.
    def enterDrive_strength(self, ctx:VerilogParser.Drive_strengthContext):
        pass

    # Exit a parse tree produced by VerilogParser#drive_strength.
    def exitDrive_strength(self, ctx:VerilogParser.Drive_strengthContext):
        pass


    # Enter a parse tree produced by VerilogParser#strength0.
    def enterStrength0(self, ctx:VerilogParser.Strength0Context):
        pass

    # Exit a parse tree produced by VerilogParser#strength0.
    def exitStrength0(self, ctx:VerilogParser.Strength0Context):
        pass


    # Enter a parse tree produced by VerilogParser#strength1.
    def enterStrength1(self, ctx:VerilogParser.Strength1Context):
        pass

    # Exit a parse tree produced by VerilogParser#strength1.
    def exitStrength1(self, ctx:VerilogParser.Strength1Context):
        pass


    # Enter a parse tree produced by VerilogParser#charge_strength.
    def enterCharge_strength(self, ctx:VerilogParser.Charge_strengthContext):
        pass

    # Exit a parse tree produced by VerilogParser#charge_strength.
    def exitCharge_strength(self, ctx:VerilogParser.Charge_strengthContext):
        pass


    # Enter a parse tree produced by VerilogParser#delay3.
    def enterDelay3(self, ctx:VerilogParser.Delay3Context):
        pass

    # Exit a parse tree produced by VerilogParser#delay3.
    def exitDelay3(self, ctx:VerilogParser.Delay3Context):
        pass


    # Enter a parse tree produced by VerilogParser#delay2.
    def enterDelay2(self, ctx:VerilogParser.Delay2Context):
        pass

    # Exit a parse tree produced by VerilogParser#delay2.
    def exitDelay2(self, ctx:VerilogParser.Delay2Context):
        pass


    # Enter a parse tree produced by VerilogParser#delay_value.
    def enterDelay_value(self, ctx:VerilogParser.Delay_valueContext):
        pass

    # Exit a parse tree produced by VerilogParser#delay_value.
    def exitDelay_value(self, ctx:VerilogParser.Delay_valueContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_defparam_assignments.
    def enterList_of_defparam_assignments(self, ctx:VerilogParser.List_of_defparam_assignmentsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_defparam_assignments.
    def exitList_of_defparam_assignments(self, ctx:VerilogParser.List_of_defparam_assignmentsContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_event_identifiers.
    def enterList_of_event_identifiers(self, ctx:VerilogParser.List_of_event_identifiersContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_event_identifiers.
    def exitList_of_event_identifiers(self, ctx:VerilogParser.List_of_event_identifiersContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_net_decl_assignments.
    def enterList_of_net_decl_assignments(self, ctx:VerilogParser.List_of_net_decl_assignmentsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_net_decl_assignments.
    def exitList_of_net_decl_assignments(self, ctx:VerilogParser.List_of_net_decl_assignmentsContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_net_identifiers.
    def enterList_of_net_identifiers(self, ctx:VerilogParser.List_of_net_identifiersContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_net_identifiers.
    def exitList_of_net_identifiers(self, ctx:VerilogParser.List_of_net_identifiersContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_param_assignments.
    def enterList_of_param_assignments(self, ctx:VerilogParser.List_of_param_assignmentsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_param_assignments.
    def exitList_of_param_assignments(self, ctx:VerilogParser.List_of_param_assignmentsContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_port_identifiers.
    def enterList_of_port_identifiers(self, ctx:VerilogParser.List_of_port_identifiersContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_port_identifiers.
    def exitList_of_port_identifiers(self, ctx:VerilogParser.List_of_port_identifiersContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_real_identifiers.
    def enterList_of_real_identifiers(self, ctx:VerilogParser.List_of_real_identifiersContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_real_identifiers.
    def exitList_of_real_identifiers(self, ctx:VerilogParser.List_of_real_identifiersContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_specparam_assignments.
    def enterList_of_specparam_assignments(self, ctx:VerilogParser.List_of_specparam_assignmentsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_specparam_assignments.
    def exitList_of_specparam_assignments(self, ctx:VerilogParser.List_of_specparam_assignmentsContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_variable_identifiers.
    def enterList_of_variable_identifiers(self, ctx:VerilogParser.List_of_variable_identifiersContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_variable_identifiers.
    def exitList_of_variable_identifiers(self, ctx:VerilogParser.List_of_variable_identifiersContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_variable_port_identifiers.
    def enterList_of_variable_port_identifiers(self, ctx:VerilogParser.List_of_variable_port_identifiersContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_variable_port_identifiers.
    def exitList_of_variable_port_identifiers(self, ctx:VerilogParser.List_of_variable_port_identifiersContext):
        pass


    # Enter a parse tree produced by VerilogParser#defparam_assignment.
    def enterDefparam_assignment(self, ctx:VerilogParser.Defparam_assignmentContext):
        pass

    # Exit a parse tree produced by VerilogParser#defparam_assignment.
    def exitDefparam_assignment(self, ctx:VerilogParser.Defparam_assignmentContext):
        pass


    # Enter a parse tree produced by VerilogParser#net_decl_assignment.
    def enterNet_decl_assignment(self, ctx:VerilogParser.Net_decl_assignmentContext):
        pass

    # Exit a parse tree produced by VerilogParser#net_decl_assignment.
    def exitNet_decl_assignment(self, ctx:VerilogParser.Net_decl_assignmentContext):
        pass


    # Enter a parse tree produced by VerilogParser#param_assignment.
    def enterParam_assignment(self, ctx:VerilogParser.Param_assignmentContext):
        pass

    # Exit a parse tree produced by VerilogParser#param_assignment.
    def exitParam_assignment(self, ctx:VerilogParser.Param_assignmentContext):
        pass


    # Enter a parse tree produced by VerilogParser#specparam_assignment.
    def enterSpecparam_assignment(self, ctx:VerilogParser.Specparam_assignmentContext):
        pass

    # Exit a parse tree produced by VerilogParser#specparam_assignment.
    def exitSpecparam_assignment(self, ctx:VerilogParser.Specparam_assignmentContext):
        pass


    # Enter a parse tree produced by VerilogParser#pulse_control_specparam.
    def enterPulse_control_specparam(self, ctx:VerilogParser.Pulse_control_specparamContext):
        pass

    # Exit a parse tree produced by VerilogParser#pulse_control_specparam.
    def exitPulse_control_specparam(self, ctx:VerilogParser.Pulse_control_specparamContext):
        pass


    # Enter a parse tree produced by VerilogParser#error_limit_value.
    def enterError_limit_value(self, ctx:VerilogParser.Error_limit_valueContext):
        pass

    # Exit a parse tree produced by VerilogParser#error_limit_value.
    def exitError_limit_value(self, ctx:VerilogParser.Error_limit_valueContext):
        pass


    # Enter a parse tree produced by VerilogParser#reject_limit_value.
    def enterReject_limit_value(self, ctx:VerilogParser.Reject_limit_valueContext):
        pass

    # Exit a parse tree produced by VerilogParser#reject_limit_value.
    def exitReject_limit_value(self, ctx:VerilogParser.Reject_limit_valueContext):
        pass


    # Enter a parse tree produced by VerilogParser#limit_value.
    def enterLimit_value(self, ctx:VerilogParser.Limit_valueContext):
        pass

    # Exit a parse tree produced by VerilogParser#limit_value.
    def exitLimit_value(self, ctx:VerilogParser.Limit_valueContext):
        pass


    # Enter a parse tree produced by VerilogParser#dimension.
    def enterDimension(self, ctx:VerilogParser.DimensionContext):
        pass

    # Exit a parse tree produced by VerilogParser#dimension.
    def exitDimension(self, ctx:VerilogParser.DimensionContext):
        pass


    # Enter a parse tree produced by VerilogParser#range_.
    def enterRange_(self, ctx:VerilogParser.Range_Context):
        pass

    # Exit a parse tree produced by VerilogParser#range_.
    def exitRange_(self, ctx:VerilogParser.Range_Context):
        pass


    # Enter a parse tree produced by VerilogParser#function_declaration.
    def enterFunction_declaration(self, ctx:VerilogParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#function_declaration.
    def exitFunction_declaration(self, ctx:VerilogParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#function_item_declaration.
    def enterFunction_item_declaration(self, ctx:VerilogParser.Function_item_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#function_item_declaration.
    def exitFunction_item_declaration(self, ctx:VerilogParser.Function_item_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#function_port_list.
    def enterFunction_port_list(self, ctx:VerilogParser.Function_port_listContext):
        pass

    # Exit a parse tree produced by VerilogParser#function_port_list.
    def exitFunction_port_list(self, ctx:VerilogParser.Function_port_listContext):
        pass


    # Enter a parse tree produced by VerilogParser#function_range_or_type.
    def enterFunction_range_or_type(self, ctx:VerilogParser.Function_range_or_typeContext):
        pass

    # Exit a parse tree produced by VerilogParser#function_range_or_type.
    def exitFunction_range_or_type(self, ctx:VerilogParser.Function_range_or_typeContext):
        pass


    # Enter a parse tree produced by VerilogParser#task_declaration.
    def enterTask_declaration(self, ctx:VerilogParser.Task_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#task_declaration.
    def exitTask_declaration(self, ctx:VerilogParser.Task_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#task_item_declaration.
    def enterTask_item_declaration(self, ctx:VerilogParser.Task_item_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#task_item_declaration.
    def exitTask_item_declaration(self, ctx:VerilogParser.Task_item_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#task_port_list.
    def enterTask_port_list(self, ctx:VerilogParser.Task_port_listContext):
        pass

    # Exit a parse tree produced by VerilogParser#task_port_list.
    def exitTask_port_list(self, ctx:VerilogParser.Task_port_listContext):
        pass


    # Enter a parse tree produced by VerilogParser#task_port_item.
    def enterTask_port_item(self, ctx:VerilogParser.Task_port_itemContext):
        pass

    # Exit a parse tree produced by VerilogParser#task_port_item.
    def exitTask_port_item(self, ctx:VerilogParser.Task_port_itemContext):
        pass


    # Enter a parse tree produced by VerilogParser#tf_input_declaration.
    def enterTf_input_declaration(self, ctx:VerilogParser.Tf_input_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#tf_input_declaration.
    def exitTf_input_declaration(self, ctx:VerilogParser.Tf_input_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#tf_output_declaration.
    def enterTf_output_declaration(self, ctx:VerilogParser.Tf_output_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#tf_output_declaration.
    def exitTf_output_declaration(self, ctx:VerilogParser.Tf_output_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#tf_inout_declaration.
    def enterTf_inout_declaration(self, ctx:VerilogParser.Tf_inout_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#tf_inout_declaration.
    def exitTf_inout_declaration(self, ctx:VerilogParser.Tf_inout_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#task_port_type.
    def enterTask_port_type(self, ctx:VerilogParser.Task_port_typeContext):
        pass

    # Exit a parse tree produced by VerilogParser#task_port_type.
    def exitTask_port_type(self, ctx:VerilogParser.Task_port_typeContext):
        pass


    # Enter a parse tree produced by VerilogParser#block_item_declaration.
    def enterBlock_item_declaration(self, ctx:VerilogParser.Block_item_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#block_item_declaration.
    def exitBlock_item_declaration(self, ctx:VerilogParser.Block_item_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_block_variable_identifiers.
    def enterList_of_block_variable_identifiers(self, ctx:VerilogParser.List_of_block_variable_identifiersContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_block_variable_identifiers.
    def exitList_of_block_variable_identifiers(self, ctx:VerilogParser.List_of_block_variable_identifiersContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_block_real_identifiers.
    def enterList_of_block_real_identifiers(self, ctx:VerilogParser.List_of_block_real_identifiersContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_block_real_identifiers.
    def exitList_of_block_real_identifiers(self, ctx:VerilogParser.List_of_block_real_identifiersContext):
        pass


    # Enter a parse tree produced by VerilogParser#block_variable_type.
    def enterBlock_variable_type(self, ctx:VerilogParser.Block_variable_typeContext):
        pass

    # Exit a parse tree produced by VerilogParser#block_variable_type.
    def exitBlock_variable_type(self, ctx:VerilogParser.Block_variable_typeContext):
        pass


    # Enter a parse tree produced by VerilogParser#block_real_type.
    def enterBlock_real_type(self, ctx:VerilogParser.Block_real_typeContext):
        pass

    # Exit a parse tree produced by VerilogParser#block_real_type.
    def exitBlock_real_type(self, ctx:VerilogParser.Block_real_typeContext):
        pass


    # Enter a parse tree produced by VerilogParser#gate_instantiation.
    def enterGate_instantiation(self, ctx:VerilogParser.Gate_instantiationContext):
        pass

    # Exit a parse tree produced by VerilogParser#gate_instantiation.
    def exitGate_instantiation(self, ctx:VerilogParser.Gate_instantiationContext):
        pass


    # Enter a parse tree produced by VerilogParser#cmos_switch_instance.
    def enterCmos_switch_instance(self, ctx:VerilogParser.Cmos_switch_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#cmos_switch_instance.
    def exitCmos_switch_instance(self, ctx:VerilogParser.Cmos_switch_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#enable_gate_instance.
    def enterEnable_gate_instance(self, ctx:VerilogParser.Enable_gate_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#enable_gate_instance.
    def exitEnable_gate_instance(self, ctx:VerilogParser.Enable_gate_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#mos_switch_instance.
    def enterMos_switch_instance(self, ctx:VerilogParser.Mos_switch_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#mos_switch_instance.
    def exitMos_switch_instance(self, ctx:VerilogParser.Mos_switch_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#n_input_gate_instance.
    def enterN_input_gate_instance(self, ctx:VerilogParser.N_input_gate_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#n_input_gate_instance.
    def exitN_input_gate_instance(self, ctx:VerilogParser.N_input_gate_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#n_output_gate_instance.
    def enterN_output_gate_instance(self, ctx:VerilogParser.N_output_gate_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#n_output_gate_instance.
    def exitN_output_gate_instance(self, ctx:VerilogParser.N_output_gate_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#pass_switch_instance.
    def enterPass_switch_instance(self, ctx:VerilogParser.Pass_switch_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#pass_switch_instance.
    def exitPass_switch_instance(self, ctx:VerilogParser.Pass_switch_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#pass_enable_switch_instance.
    def enterPass_enable_switch_instance(self, ctx:VerilogParser.Pass_enable_switch_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#pass_enable_switch_instance.
    def exitPass_enable_switch_instance(self, ctx:VerilogParser.Pass_enable_switch_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#pull_gate_instance.
    def enterPull_gate_instance(self, ctx:VerilogParser.Pull_gate_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#pull_gate_instance.
    def exitPull_gate_instance(self, ctx:VerilogParser.Pull_gate_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#name_of_gate_instance.
    def enterName_of_gate_instance(self, ctx:VerilogParser.Name_of_gate_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#name_of_gate_instance.
    def exitName_of_gate_instance(self, ctx:VerilogParser.Name_of_gate_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#pulldown_strength.
    def enterPulldown_strength(self, ctx:VerilogParser.Pulldown_strengthContext):
        pass

    # Exit a parse tree produced by VerilogParser#pulldown_strength.
    def exitPulldown_strength(self, ctx:VerilogParser.Pulldown_strengthContext):
        pass


    # Enter a parse tree produced by VerilogParser#pullup_strength.
    def enterPullup_strength(self, ctx:VerilogParser.Pullup_strengthContext):
        pass

    # Exit a parse tree produced by VerilogParser#pullup_strength.
    def exitPullup_strength(self, ctx:VerilogParser.Pullup_strengthContext):
        pass


    # Enter a parse tree produced by VerilogParser#enable_terminal.
    def enterEnable_terminal(self, ctx:VerilogParser.Enable_terminalContext):
        pass

    # Exit a parse tree produced by VerilogParser#enable_terminal.
    def exitEnable_terminal(self, ctx:VerilogParser.Enable_terminalContext):
        pass


    # Enter a parse tree produced by VerilogParser#inout_terminal.
    def enterInout_terminal(self, ctx:VerilogParser.Inout_terminalContext):
        pass

    # Exit a parse tree produced by VerilogParser#inout_terminal.
    def exitInout_terminal(self, ctx:VerilogParser.Inout_terminalContext):
        pass


    # Enter a parse tree produced by VerilogParser#input_terminal.
    def enterInput_terminal(self, ctx:VerilogParser.Input_terminalContext):
        pass

    # Exit a parse tree produced by VerilogParser#input_terminal.
    def exitInput_terminal(self, ctx:VerilogParser.Input_terminalContext):
        pass


    # Enter a parse tree produced by VerilogParser#ncontrol_terminal.
    def enterNcontrol_terminal(self, ctx:VerilogParser.Ncontrol_terminalContext):
        pass

    # Exit a parse tree produced by VerilogParser#ncontrol_terminal.
    def exitNcontrol_terminal(self, ctx:VerilogParser.Ncontrol_terminalContext):
        pass


    # Enter a parse tree produced by VerilogParser#output_terminal.
    def enterOutput_terminal(self, ctx:VerilogParser.Output_terminalContext):
        pass

    # Exit a parse tree produced by VerilogParser#output_terminal.
    def exitOutput_terminal(self, ctx:VerilogParser.Output_terminalContext):
        pass


    # Enter a parse tree produced by VerilogParser#pcontrol_terminal.
    def enterPcontrol_terminal(self, ctx:VerilogParser.Pcontrol_terminalContext):
        pass

    # Exit a parse tree produced by VerilogParser#pcontrol_terminal.
    def exitPcontrol_terminal(self, ctx:VerilogParser.Pcontrol_terminalContext):
        pass


    # Enter a parse tree produced by VerilogParser#cmos_switchtype.
    def enterCmos_switchtype(self, ctx:VerilogParser.Cmos_switchtypeContext):
        pass

    # Exit a parse tree produced by VerilogParser#cmos_switchtype.
    def exitCmos_switchtype(self, ctx:VerilogParser.Cmos_switchtypeContext):
        pass


    # Enter a parse tree produced by VerilogParser#enable_gatetype.
    def enterEnable_gatetype(self, ctx:VerilogParser.Enable_gatetypeContext):
        pass

    # Exit a parse tree produced by VerilogParser#enable_gatetype.
    def exitEnable_gatetype(self, ctx:VerilogParser.Enable_gatetypeContext):
        pass


    # Enter a parse tree produced by VerilogParser#mos_switchtype.
    def enterMos_switchtype(self, ctx:VerilogParser.Mos_switchtypeContext):
        pass

    # Exit a parse tree produced by VerilogParser#mos_switchtype.
    def exitMos_switchtype(self, ctx:VerilogParser.Mos_switchtypeContext):
        pass


    # Enter a parse tree produced by VerilogParser#n_input_gatetype.
    def enterN_input_gatetype(self, ctx:VerilogParser.N_input_gatetypeContext):
        pass

    # Exit a parse tree produced by VerilogParser#n_input_gatetype.
    def exitN_input_gatetype(self, ctx:VerilogParser.N_input_gatetypeContext):
        pass


    # Enter a parse tree produced by VerilogParser#n_output_gatetype.
    def enterN_output_gatetype(self, ctx:VerilogParser.N_output_gatetypeContext):
        pass

    # Exit a parse tree produced by VerilogParser#n_output_gatetype.
    def exitN_output_gatetype(self, ctx:VerilogParser.N_output_gatetypeContext):
        pass


    # Enter a parse tree produced by VerilogParser#pass_en_switchtype.
    def enterPass_en_switchtype(self, ctx:VerilogParser.Pass_en_switchtypeContext):
        pass

    # Exit a parse tree produced by VerilogParser#pass_en_switchtype.
    def exitPass_en_switchtype(self, ctx:VerilogParser.Pass_en_switchtypeContext):
        pass


    # Enter a parse tree produced by VerilogParser#pass_switchtype.
    def enterPass_switchtype(self, ctx:VerilogParser.Pass_switchtypeContext):
        pass

    # Exit a parse tree produced by VerilogParser#pass_switchtype.
    def exitPass_switchtype(self, ctx:VerilogParser.Pass_switchtypeContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_instantiation.
    def enterModule_instantiation(self, ctx:VerilogParser.Module_instantiationContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_instantiation.
    def exitModule_instantiation(self, ctx:VerilogParser.Module_instantiationContext):
        pass


    # Enter a parse tree produced by VerilogParser#parameter_value_assignment.
    def enterParameter_value_assignment(self, ctx:VerilogParser.Parameter_value_assignmentContext):
        pass

    # Exit a parse tree produced by VerilogParser#parameter_value_assignment.
    def exitParameter_value_assignment(self, ctx:VerilogParser.Parameter_value_assignmentContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_parameter_assignments.
    def enterList_of_parameter_assignments(self, ctx:VerilogParser.List_of_parameter_assignmentsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_parameter_assignments.
    def exitList_of_parameter_assignments(self, ctx:VerilogParser.List_of_parameter_assignmentsContext):
        pass


    # Enter a parse tree produced by VerilogParser#ordered_parameter_assignment.
    def enterOrdered_parameter_assignment(self, ctx:VerilogParser.Ordered_parameter_assignmentContext):
        pass

    # Exit a parse tree produced by VerilogParser#ordered_parameter_assignment.
    def exitOrdered_parameter_assignment(self, ctx:VerilogParser.Ordered_parameter_assignmentContext):
        pass


    # Enter a parse tree produced by VerilogParser#named_parameter_assignment.
    def enterNamed_parameter_assignment(self, ctx:VerilogParser.Named_parameter_assignmentContext):
        pass

    # Exit a parse tree produced by VerilogParser#named_parameter_assignment.
    def exitNamed_parameter_assignment(self, ctx:VerilogParser.Named_parameter_assignmentContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_instance.
    def enterModule_instance(self, ctx:VerilogParser.Module_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_instance.
    def exitModule_instance(self, ctx:VerilogParser.Module_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#name_of_module_instance.
    def enterName_of_module_instance(self, ctx:VerilogParser.Name_of_module_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#name_of_module_instance.
    def exitName_of_module_instance(self, ctx:VerilogParser.Name_of_module_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_port_connections.
    def enterList_of_port_connections(self, ctx:VerilogParser.List_of_port_connectionsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_port_connections.
    def exitList_of_port_connections(self, ctx:VerilogParser.List_of_port_connectionsContext):
        pass


    # Enter a parse tree produced by VerilogParser#ordered_port_connection.
    def enterOrdered_port_connection(self, ctx:VerilogParser.Ordered_port_connectionContext):
        pass

    # Exit a parse tree produced by VerilogParser#ordered_port_connection.
    def exitOrdered_port_connection(self, ctx:VerilogParser.Ordered_port_connectionContext):
        pass


    # Enter a parse tree produced by VerilogParser#named_port_connection.
    def enterNamed_port_connection(self, ctx:VerilogParser.Named_port_connectionContext):
        pass

    # Exit a parse tree produced by VerilogParser#named_port_connection.
    def exitNamed_port_connection(self, ctx:VerilogParser.Named_port_connectionContext):
        pass


    # Enter a parse tree produced by VerilogParser#generate_region.
    def enterGenerate_region(self, ctx:VerilogParser.Generate_regionContext):
        pass

    # Exit a parse tree produced by VerilogParser#generate_region.
    def exitGenerate_region(self, ctx:VerilogParser.Generate_regionContext):
        pass


    # Enter a parse tree produced by VerilogParser#genvar_declaration.
    def enterGenvar_declaration(self, ctx:VerilogParser.Genvar_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#genvar_declaration.
    def exitGenvar_declaration(self, ctx:VerilogParser.Genvar_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_genvar_identifiers.
    def enterList_of_genvar_identifiers(self, ctx:VerilogParser.List_of_genvar_identifiersContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_genvar_identifiers.
    def exitList_of_genvar_identifiers(self, ctx:VerilogParser.List_of_genvar_identifiersContext):
        pass


    # Enter a parse tree produced by VerilogParser#loop_generate_construct.
    def enterLoop_generate_construct(self, ctx:VerilogParser.Loop_generate_constructContext):
        pass

    # Exit a parse tree produced by VerilogParser#loop_generate_construct.
    def exitLoop_generate_construct(self, ctx:VerilogParser.Loop_generate_constructContext):
        pass


    # Enter a parse tree produced by VerilogParser#genvar_initialization.
    def enterGenvar_initialization(self, ctx:VerilogParser.Genvar_initializationContext):
        pass

    # Exit a parse tree produced by VerilogParser#genvar_initialization.
    def exitGenvar_initialization(self, ctx:VerilogParser.Genvar_initializationContext):
        pass


    # Enter a parse tree produced by VerilogParser#genvar_expression.
    def enterGenvar_expression(self, ctx:VerilogParser.Genvar_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#genvar_expression.
    def exitGenvar_expression(self, ctx:VerilogParser.Genvar_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#genvar_iteration.
    def enterGenvar_iteration(self, ctx:VerilogParser.Genvar_iterationContext):
        pass

    # Exit a parse tree produced by VerilogParser#genvar_iteration.
    def exitGenvar_iteration(self, ctx:VerilogParser.Genvar_iterationContext):
        pass


    # Enter a parse tree produced by VerilogParser#genvar_primary.
    def enterGenvar_primary(self, ctx:VerilogParser.Genvar_primaryContext):
        pass

    # Exit a parse tree produced by VerilogParser#genvar_primary.
    def exitGenvar_primary(self, ctx:VerilogParser.Genvar_primaryContext):
        pass


    # Enter a parse tree produced by VerilogParser#conditional_generate_construct.
    def enterConditional_generate_construct(self, ctx:VerilogParser.Conditional_generate_constructContext):
        pass

    # Exit a parse tree produced by VerilogParser#conditional_generate_construct.
    def exitConditional_generate_construct(self, ctx:VerilogParser.Conditional_generate_constructContext):
        pass


    # Enter a parse tree produced by VerilogParser#if_generate_construct.
    def enterIf_generate_construct(self, ctx:VerilogParser.If_generate_constructContext):
        pass

    # Exit a parse tree produced by VerilogParser#if_generate_construct.
    def exitIf_generate_construct(self, ctx:VerilogParser.If_generate_constructContext):
        pass


    # Enter a parse tree produced by VerilogParser#case_generate_construct.
    def enterCase_generate_construct(self, ctx:VerilogParser.Case_generate_constructContext):
        pass

    # Exit a parse tree produced by VerilogParser#case_generate_construct.
    def exitCase_generate_construct(self, ctx:VerilogParser.Case_generate_constructContext):
        pass


    # Enter a parse tree produced by VerilogParser#generate_block.
    def enterGenerate_block(self, ctx:VerilogParser.Generate_blockContext):
        pass

    # Exit a parse tree produced by VerilogParser#generate_block.
    def exitGenerate_block(self, ctx:VerilogParser.Generate_blockContext):
        pass


    # Enter a parse tree produced by VerilogParser#generate_block_or_null.
    def enterGenerate_block_or_null(self, ctx:VerilogParser.Generate_block_or_nullContext):
        pass

    # Exit a parse tree produced by VerilogParser#generate_block_or_null.
    def exitGenerate_block_or_null(self, ctx:VerilogParser.Generate_block_or_nullContext):
        pass


    # Enter a parse tree produced by VerilogParser#continuous_assign.
    def enterContinuous_assign(self, ctx:VerilogParser.Continuous_assignContext):
        pass

    # Exit a parse tree produced by VerilogParser#continuous_assign.
    def exitContinuous_assign(self, ctx:VerilogParser.Continuous_assignContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_net_assignments.
    def enterList_of_net_assignments(self, ctx:VerilogParser.List_of_net_assignmentsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_net_assignments.
    def exitList_of_net_assignments(self, ctx:VerilogParser.List_of_net_assignmentsContext):
        pass


    # Enter a parse tree produced by VerilogParser#net_assignment.
    def enterNet_assignment(self, ctx:VerilogParser.Net_assignmentContext):
        pass

    # Exit a parse tree produced by VerilogParser#net_assignment.
    def exitNet_assignment(self, ctx:VerilogParser.Net_assignmentContext):
        pass


    # Enter a parse tree produced by VerilogParser#initial_construct.
    def enterInitial_construct(self, ctx:VerilogParser.Initial_constructContext):
        pass

    # Exit a parse tree produced by VerilogParser#initial_construct.
    def exitInitial_construct(self, ctx:VerilogParser.Initial_constructContext):
        pass


    # Enter a parse tree produced by VerilogParser#always_construct.
    def enterAlways_construct(self, ctx:VerilogParser.Always_constructContext):
        pass

    # Exit a parse tree produced by VerilogParser#always_construct.
    def exitAlways_construct(self, ctx:VerilogParser.Always_constructContext):
        pass


    # Enter a parse tree produced by VerilogParser#blocking_assignment.
    def enterBlocking_assignment(self, ctx:VerilogParser.Blocking_assignmentContext):
        pass

    # Exit a parse tree produced by VerilogParser#blocking_assignment.
    def exitBlocking_assignment(self, ctx:VerilogParser.Blocking_assignmentContext):
        pass


    # Enter a parse tree produced by VerilogParser#nonblocking_assignment.
    def enterNonblocking_assignment(self, ctx:VerilogParser.Nonblocking_assignmentContext):
        pass

    # Exit a parse tree produced by VerilogParser#nonblocking_assignment.
    def exitNonblocking_assignment(self, ctx:VerilogParser.Nonblocking_assignmentContext):
        pass


    # Enter a parse tree produced by VerilogParser#procedural_continuous_assignments.
    def enterProcedural_continuous_assignments(self, ctx:VerilogParser.Procedural_continuous_assignmentsContext):
        pass

    # Exit a parse tree produced by VerilogParser#procedural_continuous_assignments.
    def exitProcedural_continuous_assignments(self, ctx:VerilogParser.Procedural_continuous_assignmentsContext):
        pass


    # Enter a parse tree produced by VerilogParser#variable_assignment.
    def enterVariable_assignment(self, ctx:VerilogParser.Variable_assignmentContext):
        pass

    # Exit a parse tree produced by VerilogParser#variable_assignment.
    def exitVariable_assignment(self, ctx:VerilogParser.Variable_assignmentContext):
        pass


    # Enter a parse tree produced by VerilogParser#par_block.
    def enterPar_block(self, ctx:VerilogParser.Par_blockContext):
        pass

    # Exit a parse tree produced by VerilogParser#par_block.
    def exitPar_block(self, ctx:VerilogParser.Par_blockContext):
        pass


    # Enter a parse tree produced by VerilogParser#seq_block.
    def enterSeq_block(self, ctx:VerilogParser.Seq_blockContext):
        pass

    # Exit a parse tree produced by VerilogParser#seq_block.
    def exitSeq_block(self, ctx:VerilogParser.Seq_blockContext):
        pass


    # Enter a parse tree produced by VerilogParser#statement.
    def enterStatement(self, ctx:VerilogParser.StatementContext):
        pass

    # Exit a parse tree produced by VerilogParser#statement.
    def exitStatement(self, ctx:VerilogParser.StatementContext):
        pass


    # Enter a parse tree produced by VerilogParser#statement_or_null.
    def enterStatement_or_null(self, ctx:VerilogParser.Statement_or_nullContext):
        pass

    # Exit a parse tree produced by VerilogParser#statement_or_null.
    def exitStatement_or_null(self, ctx:VerilogParser.Statement_or_nullContext):
        pass


    # Enter a parse tree produced by VerilogParser#function_statement.
    def enterFunction_statement(self, ctx:VerilogParser.Function_statementContext):
        pass

    # Exit a parse tree produced by VerilogParser#function_statement.
    def exitFunction_statement(self, ctx:VerilogParser.Function_statementContext):
        pass


    # Enter a parse tree produced by VerilogParser#delay_control.
    def enterDelay_control(self, ctx:VerilogParser.Delay_controlContext):
        pass

    # Exit a parse tree produced by VerilogParser#delay_control.
    def exitDelay_control(self, ctx:VerilogParser.Delay_controlContext):
        pass


    # Enter a parse tree produced by VerilogParser#delay_or_event_control.
    def enterDelay_or_event_control(self, ctx:VerilogParser.Delay_or_event_controlContext):
        pass

    # Exit a parse tree produced by VerilogParser#delay_or_event_control.
    def exitDelay_or_event_control(self, ctx:VerilogParser.Delay_or_event_controlContext):
        pass


    # Enter a parse tree produced by VerilogParser#disable_statement.
    def enterDisable_statement(self, ctx:VerilogParser.Disable_statementContext):
        pass

    # Exit a parse tree produced by VerilogParser#disable_statement.
    def exitDisable_statement(self, ctx:VerilogParser.Disable_statementContext):
        pass


    # Enter a parse tree produced by VerilogParser#event_control.
    def enterEvent_control(self, ctx:VerilogParser.Event_controlContext):
        pass

    # Exit a parse tree produced by VerilogParser#event_control.
    def exitEvent_control(self, ctx:VerilogParser.Event_controlContext):
        pass


    # Enter a parse tree produced by VerilogParser#event_trigger.
    def enterEvent_trigger(self, ctx:VerilogParser.Event_triggerContext):
        pass

    # Exit a parse tree produced by VerilogParser#event_trigger.
    def exitEvent_trigger(self, ctx:VerilogParser.Event_triggerContext):
        pass


    # Enter a parse tree produced by VerilogParser#event_expression.
    def enterEvent_expression(self, ctx:VerilogParser.Event_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#event_expression.
    def exitEvent_expression(self, ctx:VerilogParser.Event_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#event_primary.
    def enterEvent_primary(self, ctx:VerilogParser.Event_primaryContext):
        pass

    # Exit a parse tree produced by VerilogParser#event_primary.
    def exitEvent_primary(self, ctx:VerilogParser.Event_primaryContext):
        pass


    # Enter a parse tree produced by VerilogParser#procedural_timing_control.
    def enterProcedural_timing_control(self, ctx:VerilogParser.Procedural_timing_controlContext):
        pass

    # Exit a parse tree produced by VerilogParser#procedural_timing_control.
    def exitProcedural_timing_control(self, ctx:VerilogParser.Procedural_timing_controlContext):
        pass


    # Enter a parse tree produced by VerilogParser#procedural_timing_control_statement.
    def enterProcedural_timing_control_statement(self, ctx:VerilogParser.Procedural_timing_control_statementContext):
        pass

    # Exit a parse tree produced by VerilogParser#procedural_timing_control_statement.
    def exitProcedural_timing_control_statement(self, ctx:VerilogParser.Procedural_timing_control_statementContext):
        pass


    # Enter a parse tree produced by VerilogParser#wait_statement.
    def enterWait_statement(self, ctx:VerilogParser.Wait_statementContext):
        pass

    # Exit a parse tree produced by VerilogParser#wait_statement.
    def exitWait_statement(self, ctx:VerilogParser.Wait_statementContext):
        pass


    # Enter a parse tree produced by VerilogParser#conditional_statement.
    def enterConditional_statement(self, ctx:VerilogParser.Conditional_statementContext):
        pass

    # Exit a parse tree produced by VerilogParser#conditional_statement.
    def exitConditional_statement(self, ctx:VerilogParser.Conditional_statementContext):
        pass


    # Enter a parse tree produced by VerilogParser#case_statement.
    def enterCase_statement(self, ctx:VerilogParser.Case_statementContext):
        pass

    # Exit a parse tree produced by VerilogParser#case_statement.
    def exitCase_statement(self, ctx:VerilogParser.Case_statementContext):
        pass


    # Enter a parse tree produced by VerilogParser#case_item.
    def enterCase_item(self, ctx:VerilogParser.Case_itemContext):
        pass

    # Exit a parse tree produced by VerilogParser#case_item.
    def exitCase_item(self, ctx:VerilogParser.Case_itemContext):
        pass


    # Enter a parse tree produced by VerilogParser#loop_statement.
    def enterLoop_statement(self, ctx:VerilogParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by VerilogParser#loop_statement.
    def exitLoop_statement(self, ctx:VerilogParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by VerilogParser#system_task_enable.
    def enterSystem_task_enable(self, ctx:VerilogParser.System_task_enableContext):
        pass

    # Exit a parse tree produced by VerilogParser#system_task_enable.
    def exitSystem_task_enable(self, ctx:VerilogParser.System_task_enableContext):
        pass


    # Enter a parse tree produced by VerilogParser#task_enable.
    def enterTask_enable(self, ctx:VerilogParser.Task_enableContext):
        pass

    # Exit a parse tree produced by VerilogParser#task_enable.
    def exitTask_enable(self, ctx:VerilogParser.Task_enableContext):
        pass


    # Enter a parse tree produced by VerilogParser#specify_block.
    def enterSpecify_block(self, ctx:VerilogParser.Specify_blockContext):
        pass

    # Exit a parse tree produced by VerilogParser#specify_block.
    def exitSpecify_block(self, ctx:VerilogParser.Specify_blockContext):
        pass


    # Enter a parse tree produced by VerilogParser#specify_item.
    def enterSpecify_item(self, ctx:VerilogParser.Specify_itemContext):
        pass

    # Exit a parse tree produced by VerilogParser#specify_item.
    def exitSpecify_item(self, ctx:VerilogParser.Specify_itemContext):
        pass


    # Enter a parse tree produced by VerilogParser#pulsestyle_declaration.
    def enterPulsestyle_declaration(self, ctx:VerilogParser.Pulsestyle_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#pulsestyle_declaration.
    def exitPulsestyle_declaration(self, ctx:VerilogParser.Pulsestyle_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#showcancelled_declaration.
    def enterShowcancelled_declaration(self, ctx:VerilogParser.Showcancelled_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#showcancelled_declaration.
    def exitShowcancelled_declaration(self, ctx:VerilogParser.Showcancelled_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#path_declaration.
    def enterPath_declaration(self, ctx:VerilogParser.Path_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#path_declaration.
    def exitPath_declaration(self, ctx:VerilogParser.Path_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#simple_path_declaration.
    def enterSimple_path_declaration(self, ctx:VerilogParser.Simple_path_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#simple_path_declaration.
    def exitSimple_path_declaration(self, ctx:VerilogParser.Simple_path_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#parallel_path_description.
    def enterParallel_path_description(self, ctx:VerilogParser.Parallel_path_descriptionContext):
        pass

    # Exit a parse tree produced by VerilogParser#parallel_path_description.
    def exitParallel_path_description(self, ctx:VerilogParser.Parallel_path_descriptionContext):
        pass


    # Enter a parse tree produced by VerilogParser#full_path_description.
    def enterFull_path_description(self, ctx:VerilogParser.Full_path_descriptionContext):
        pass

    # Exit a parse tree produced by VerilogParser#full_path_description.
    def exitFull_path_description(self, ctx:VerilogParser.Full_path_descriptionContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_path_inputs.
    def enterList_of_path_inputs(self, ctx:VerilogParser.List_of_path_inputsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_path_inputs.
    def exitList_of_path_inputs(self, ctx:VerilogParser.List_of_path_inputsContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_path_outputs.
    def enterList_of_path_outputs(self, ctx:VerilogParser.List_of_path_outputsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_path_outputs.
    def exitList_of_path_outputs(self, ctx:VerilogParser.List_of_path_outputsContext):
        pass


    # Enter a parse tree produced by VerilogParser#specify_input_terminal_descriptor.
    def enterSpecify_input_terminal_descriptor(self, ctx:VerilogParser.Specify_input_terminal_descriptorContext):
        pass

    # Exit a parse tree produced by VerilogParser#specify_input_terminal_descriptor.
    def exitSpecify_input_terminal_descriptor(self, ctx:VerilogParser.Specify_input_terminal_descriptorContext):
        pass


    # Enter a parse tree produced by VerilogParser#specify_output_terminal_descriptor.
    def enterSpecify_output_terminal_descriptor(self, ctx:VerilogParser.Specify_output_terminal_descriptorContext):
        pass

    # Exit a parse tree produced by VerilogParser#specify_output_terminal_descriptor.
    def exitSpecify_output_terminal_descriptor(self, ctx:VerilogParser.Specify_output_terminal_descriptorContext):
        pass


    # Enter a parse tree produced by VerilogParser#input_identifier.
    def enterInput_identifier(self, ctx:VerilogParser.Input_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#input_identifier.
    def exitInput_identifier(self, ctx:VerilogParser.Input_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#output_identifier.
    def enterOutput_identifier(self, ctx:VerilogParser.Output_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#output_identifier.
    def exitOutput_identifier(self, ctx:VerilogParser.Output_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#path_delay_value.
    def enterPath_delay_value(self, ctx:VerilogParser.Path_delay_valueContext):
        pass

    # Exit a parse tree produced by VerilogParser#path_delay_value.
    def exitPath_delay_value(self, ctx:VerilogParser.Path_delay_valueContext):
        pass


    # Enter a parse tree produced by VerilogParser#list_of_path_delay_expressions.
    def enterList_of_path_delay_expressions(self, ctx:VerilogParser.List_of_path_delay_expressionsContext):
        pass

    # Exit a parse tree produced by VerilogParser#list_of_path_delay_expressions.
    def exitList_of_path_delay_expressions(self, ctx:VerilogParser.List_of_path_delay_expressionsContext):
        pass


    # Enter a parse tree produced by VerilogParser#t_path_delay_expression.
    def enterT_path_delay_expression(self, ctx:VerilogParser.T_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#t_path_delay_expression.
    def exitT_path_delay_expression(self, ctx:VerilogParser.T_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#trise_path_delay_expression.
    def enterTrise_path_delay_expression(self, ctx:VerilogParser.Trise_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#trise_path_delay_expression.
    def exitTrise_path_delay_expression(self, ctx:VerilogParser.Trise_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#tfall_path_delay_expression.
    def enterTfall_path_delay_expression(self, ctx:VerilogParser.Tfall_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#tfall_path_delay_expression.
    def exitTfall_path_delay_expression(self, ctx:VerilogParser.Tfall_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#tz_path_delay_expression.
    def enterTz_path_delay_expression(self, ctx:VerilogParser.Tz_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#tz_path_delay_expression.
    def exitTz_path_delay_expression(self, ctx:VerilogParser.Tz_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#t01_path_delay_expression.
    def enterT01_path_delay_expression(self, ctx:VerilogParser.T01_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#t01_path_delay_expression.
    def exitT01_path_delay_expression(self, ctx:VerilogParser.T01_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#t10_path_delay_expression.
    def enterT10_path_delay_expression(self, ctx:VerilogParser.T10_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#t10_path_delay_expression.
    def exitT10_path_delay_expression(self, ctx:VerilogParser.T10_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#t0z_path_delay_expression.
    def enterT0z_path_delay_expression(self, ctx:VerilogParser.T0z_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#t0z_path_delay_expression.
    def exitT0z_path_delay_expression(self, ctx:VerilogParser.T0z_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#tz1_path_delay_expression.
    def enterTz1_path_delay_expression(self, ctx:VerilogParser.Tz1_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#tz1_path_delay_expression.
    def exitTz1_path_delay_expression(self, ctx:VerilogParser.Tz1_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#t1z_path_delay_expression.
    def enterT1z_path_delay_expression(self, ctx:VerilogParser.T1z_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#t1z_path_delay_expression.
    def exitT1z_path_delay_expression(self, ctx:VerilogParser.T1z_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#tz0_path_delay_expression.
    def enterTz0_path_delay_expression(self, ctx:VerilogParser.Tz0_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#tz0_path_delay_expression.
    def exitTz0_path_delay_expression(self, ctx:VerilogParser.Tz0_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#t0x_path_delay_expression.
    def enterT0x_path_delay_expression(self, ctx:VerilogParser.T0x_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#t0x_path_delay_expression.
    def exitT0x_path_delay_expression(self, ctx:VerilogParser.T0x_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#tx1_path_delay_expression.
    def enterTx1_path_delay_expression(self, ctx:VerilogParser.Tx1_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#tx1_path_delay_expression.
    def exitTx1_path_delay_expression(self, ctx:VerilogParser.Tx1_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#t1x_path_delay_expression.
    def enterT1x_path_delay_expression(self, ctx:VerilogParser.T1x_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#t1x_path_delay_expression.
    def exitT1x_path_delay_expression(self, ctx:VerilogParser.T1x_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#tx0_path_delay_expression.
    def enterTx0_path_delay_expression(self, ctx:VerilogParser.Tx0_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#tx0_path_delay_expression.
    def exitTx0_path_delay_expression(self, ctx:VerilogParser.Tx0_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#txz_path_delay_expression.
    def enterTxz_path_delay_expression(self, ctx:VerilogParser.Txz_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#txz_path_delay_expression.
    def exitTxz_path_delay_expression(self, ctx:VerilogParser.Txz_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#tzx_path_delay_expression.
    def enterTzx_path_delay_expression(self, ctx:VerilogParser.Tzx_path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#tzx_path_delay_expression.
    def exitTzx_path_delay_expression(self, ctx:VerilogParser.Tzx_path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#path_delay_expression.
    def enterPath_delay_expression(self, ctx:VerilogParser.Path_delay_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#path_delay_expression.
    def exitPath_delay_expression(self, ctx:VerilogParser.Path_delay_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#edge_sensitive_path_declaration.
    def enterEdge_sensitive_path_declaration(self, ctx:VerilogParser.Edge_sensitive_path_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#edge_sensitive_path_declaration.
    def exitEdge_sensitive_path_declaration(self, ctx:VerilogParser.Edge_sensitive_path_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#parallel_edge_sensitive_path_description.
    def enterParallel_edge_sensitive_path_description(self, ctx:VerilogParser.Parallel_edge_sensitive_path_descriptionContext):
        pass

    # Exit a parse tree produced by VerilogParser#parallel_edge_sensitive_path_description.
    def exitParallel_edge_sensitive_path_description(self, ctx:VerilogParser.Parallel_edge_sensitive_path_descriptionContext):
        pass


    # Enter a parse tree produced by VerilogParser#full_edge_sensitive_path_description.
    def enterFull_edge_sensitive_path_description(self, ctx:VerilogParser.Full_edge_sensitive_path_descriptionContext):
        pass

    # Exit a parse tree produced by VerilogParser#full_edge_sensitive_path_description.
    def exitFull_edge_sensitive_path_description(self, ctx:VerilogParser.Full_edge_sensitive_path_descriptionContext):
        pass


    # Enter a parse tree produced by VerilogParser#data_source_expression.
    def enterData_source_expression(self, ctx:VerilogParser.Data_source_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#data_source_expression.
    def exitData_source_expression(self, ctx:VerilogParser.Data_source_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#edge_identifier.
    def enterEdge_identifier(self, ctx:VerilogParser.Edge_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#edge_identifier.
    def exitEdge_identifier(self, ctx:VerilogParser.Edge_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#state_dependent_path_declaration.
    def enterState_dependent_path_declaration(self, ctx:VerilogParser.State_dependent_path_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#state_dependent_path_declaration.
    def exitState_dependent_path_declaration(self, ctx:VerilogParser.State_dependent_path_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#polarity_operator.
    def enterPolarity_operator(self, ctx:VerilogParser.Polarity_operatorContext):
        pass

    # Exit a parse tree produced by VerilogParser#polarity_operator.
    def exitPolarity_operator(self, ctx:VerilogParser.Polarity_operatorContext):
        pass


    # Enter a parse tree produced by VerilogParser#concatenation.
    def enterConcatenation(self, ctx:VerilogParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by VerilogParser#concatenation.
    def exitConcatenation(self, ctx:VerilogParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by VerilogParser#constant_concatenation.
    def enterConstant_concatenation(self, ctx:VerilogParser.Constant_concatenationContext):
        pass

    # Exit a parse tree produced by VerilogParser#constant_concatenation.
    def exitConstant_concatenation(self, ctx:VerilogParser.Constant_concatenationContext):
        pass


    # Enter a parse tree produced by VerilogParser#constant_multiple_concatenation.
    def enterConstant_multiple_concatenation(self, ctx:VerilogParser.Constant_multiple_concatenationContext):
        pass

    # Exit a parse tree produced by VerilogParser#constant_multiple_concatenation.
    def exitConstant_multiple_concatenation(self, ctx:VerilogParser.Constant_multiple_concatenationContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_path_concatenation.
    def enterModule_path_concatenation(self, ctx:VerilogParser.Module_path_concatenationContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_path_concatenation.
    def exitModule_path_concatenation(self, ctx:VerilogParser.Module_path_concatenationContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_path_multiple_concatenation.
    def enterModule_path_multiple_concatenation(self, ctx:VerilogParser.Module_path_multiple_concatenationContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_path_multiple_concatenation.
    def exitModule_path_multiple_concatenation(self, ctx:VerilogParser.Module_path_multiple_concatenationContext):
        pass


    # Enter a parse tree produced by VerilogParser#multiple_concatenation.
    def enterMultiple_concatenation(self, ctx:VerilogParser.Multiple_concatenationContext):
        pass

    # Exit a parse tree produced by VerilogParser#multiple_concatenation.
    def exitMultiple_concatenation(self, ctx:VerilogParser.Multiple_concatenationContext):
        pass


    # Enter a parse tree produced by VerilogParser#constant_function_call.
    def enterConstant_function_call(self, ctx:VerilogParser.Constant_function_callContext):
        pass

    # Exit a parse tree produced by VerilogParser#constant_function_call.
    def exitConstant_function_call(self, ctx:VerilogParser.Constant_function_callContext):
        pass


    # Enter a parse tree produced by VerilogParser#constant_system_function_call.
    def enterConstant_system_function_call(self, ctx:VerilogParser.Constant_system_function_callContext):
        pass

    # Exit a parse tree produced by VerilogParser#constant_system_function_call.
    def exitConstant_system_function_call(self, ctx:VerilogParser.Constant_system_function_callContext):
        pass


    # Enter a parse tree produced by VerilogParser#function_call.
    def enterFunction_call(self, ctx:VerilogParser.Function_callContext):
        pass

    # Exit a parse tree produced by VerilogParser#function_call.
    def exitFunction_call(self, ctx:VerilogParser.Function_callContext):
        pass


    # Enter a parse tree produced by VerilogParser#system_function_call.
    def enterSystem_function_call(self, ctx:VerilogParser.System_function_callContext):
        pass

    # Exit a parse tree produced by VerilogParser#system_function_call.
    def exitSystem_function_call(self, ctx:VerilogParser.System_function_callContext):
        pass


    # Enter a parse tree produced by VerilogParser#base_expression.
    def enterBase_expression(self, ctx:VerilogParser.Base_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#base_expression.
    def exitBase_expression(self, ctx:VerilogParser.Base_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#constant_base_expression.
    def enterConstant_base_expression(self, ctx:VerilogParser.Constant_base_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#constant_base_expression.
    def exitConstant_base_expression(self, ctx:VerilogParser.Constant_base_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#constant_expression.
    def enterConstant_expression(self, ctx:VerilogParser.Constant_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#constant_expression.
    def exitConstant_expression(self, ctx:VerilogParser.Constant_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#constant_mintypmax_expression.
    def enterConstant_mintypmax_expression(self, ctx:VerilogParser.Constant_mintypmax_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#constant_mintypmax_expression.
    def exitConstant_mintypmax_expression(self, ctx:VerilogParser.Constant_mintypmax_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#constant_range_expression.
    def enterConstant_range_expression(self, ctx:VerilogParser.Constant_range_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#constant_range_expression.
    def exitConstant_range_expression(self, ctx:VerilogParser.Constant_range_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#dimension_constant_expression.
    def enterDimension_constant_expression(self, ctx:VerilogParser.Dimension_constant_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#dimension_constant_expression.
    def exitDimension_constant_expression(self, ctx:VerilogParser.Dimension_constant_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#expression.
    def enterExpression(self, ctx:VerilogParser.ExpressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#expression.
    def exitExpression(self, ctx:VerilogParser.ExpressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#lsb_constant_expression.
    def enterLsb_constant_expression(self, ctx:VerilogParser.Lsb_constant_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#lsb_constant_expression.
    def exitLsb_constant_expression(self, ctx:VerilogParser.Lsb_constant_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#mintypmax_expression.
    def enterMintypmax_expression(self, ctx:VerilogParser.Mintypmax_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#mintypmax_expression.
    def exitMintypmax_expression(self, ctx:VerilogParser.Mintypmax_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_path_expression.
    def enterModule_path_expression(self, ctx:VerilogParser.Module_path_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_path_expression.
    def exitModule_path_expression(self, ctx:VerilogParser.Module_path_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_path_mintypmax_expression.
    def enterModule_path_mintypmax_expression(self, ctx:VerilogParser.Module_path_mintypmax_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_path_mintypmax_expression.
    def exitModule_path_mintypmax_expression(self, ctx:VerilogParser.Module_path_mintypmax_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#msb_constant_expression.
    def enterMsb_constant_expression(self, ctx:VerilogParser.Msb_constant_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#msb_constant_expression.
    def exitMsb_constant_expression(self, ctx:VerilogParser.Msb_constant_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#range_expression.
    def enterRange_expression(self, ctx:VerilogParser.Range_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#range_expression.
    def exitRange_expression(self, ctx:VerilogParser.Range_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#width_constant_expression.
    def enterWidth_constant_expression(self, ctx:VerilogParser.Width_constant_expressionContext):
        pass

    # Exit a parse tree produced by VerilogParser#width_constant_expression.
    def exitWidth_constant_expression(self, ctx:VerilogParser.Width_constant_expressionContext):
        pass


    # Enter a parse tree produced by VerilogParser#constant_primary.
    def enterConstant_primary(self, ctx:VerilogParser.Constant_primaryContext):
        pass

    # Exit a parse tree produced by VerilogParser#constant_primary.
    def exitConstant_primary(self, ctx:VerilogParser.Constant_primaryContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_path_primary.
    def enterModule_path_primary(self, ctx:VerilogParser.Module_path_primaryContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_path_primary.
    def exitModule_path_primary(self, ctx:VerilogParser.Module_path_primaryContext):
        pass


    # Enter a parse tree produced by VerilogParser#primary.
    def enterPrimary(self, ctx:VerilogParser.PrimaryContext):
        pass

    # Exit a parse tree produced by VerilogParser#primary.
    def exitPrimary(self, ctx:VerilogParser.PrimaryContext):
        pass


    # Enter a parse tree produced by VerilogParser#net_lvalue.
    def enterNet_lvalue(self, ctx:VerilogParser.Net_lvalueContext):
        pass

    # Exit a parse tree produced by VerilogParser#net_lvalue.
    def exitNet_lvalue(self, ctx:VerilogParser.Net_lvalueContext):
        pass


    # Enter a parse tree produced by VerilogParser#variable_lvalue.
    def enterVariable_lvalue(self, ctx:VerilogParser.Variable_lvalueContext):
        pass

    # Exit a parse tree produced by VerilogParser#variable_lvalue.
    def exitVariable_lvalue(self, ctx:VerilogParser.Variable_lvalueContext):
        pass


    # Enter a parse tree produced by VerilogParser#unary_operator.
    def enterUnary_operator(self, ctx:VerilogParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by VerilogParser#unary_operator.
    def exitUnary_operator(self, ctx:VerilogParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by VerilogParser#binary_operator.
    def enterBinary_operator(self, ctx:VerilogParser.Binary_operatorContext):
        pass

    # Exit a parse tree produced by VerilogParser#binary_operator.
    def exitBinary_operator(self, ctx:VerilogParser.Binary_operatorContext):
        pass


    # Enter a parse tree produced by VerilogParser#unary_module_path_operator.
    def enterUnary_module_path_operator(self, ctx:VerilogParser.Unary_module_path_operatorContext):
        pass

    # Exit a parse tree produced by VerilogParser#unary_module_path_operator.
    def exitUnary_module_path_operator(self, ctx:VerilogParser.Unary_module_path_operatorContext):
        pass


    # Enter a parse tree produced by VerilogParser#binary_module_path_operator.
    def enterBinary_module_path_operator(self, ctx:VerilogParser.Binary_module_path_operatorContext):
        pass

    # Exit a parse tree produced by VerilogParser#binary_module_path_operator.
    def exitBinary_module_path_operator(self, ctx:VerilogParser.Binary_module_path_operatorContext):
        pass


    # Enter a parse tree produced by VerilogParser#number.
    def enterNumber(self, ctx:VerilogParser.NumberContext):
        pass

    # Exit a parse tree produced by VerilogParser#number.
    def exitNumber(self, ctx:VerilogParser.NumberContext):
        pass


    # Enter a parse tree produced by VerilogParser#attribute_instance.
    def enterAttribute_instance(self, ctx:VerilogParser.Attribute_instanceContext):
        pass

    # Exit a parse tree produced by VerilogParser#attribute_instance.
    def exitAttribute_instance(self, ctx:VerilogParser.Attribute_instanceContext):
        pass


    # Enter a parse tree produced by VerilogParser#attr_spec.
    def enterAttr_spec(self, ctx:VerilogParser.Attr_specContext):
        pass

    # Exit a parse tree produced by VerilogParser#attr_spec.
    def exitAttr_spec(self, ctx:VerilogParser.Attr_specContext):
        pass


    # Enter a parse tree produced by VerilogParser#attr_name.
    def enterAttr_name(self, ctx:VerilogParser.Attr_nameContext):
        pass

    # Exit a parse tree produced by VerilogParser#attr_name.
    def exitAttr_name(self, ctx:VerilogParser.Attr_nameContext):
        pass


    # Enter a parse tree produced by VerilogParser#block_identifier.
    def enterBlock_identifier(self, ctx:VerilogParser.Block_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#block_identifier.
    def exitBlock_identifier(self, ctx:VerilogParser.Block_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#cell_identifier.
    def enterCell_identifier(self, ctx:VerilogParser.Cell_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#cell_identifier.
    def exitCell_identifier(self, ctx:VerilogParser.Cell_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#config_identifier.
    def enterConfig_identifier(self, ctx:VerilogParser.Config_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#config_identifier.
    def exitConfig_identifier(self, ctx:VerilogParser.Config_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#event_identifier.
    def enterEvent_identifier(self, ctx:VerilogParser.Event_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#event_identifier.
    def exitEvent_identifier(self, ctx:VerilogParser.Event_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#function_identifier.
    def enterFunction_identifier(self, ctx:VerilogParser.Function_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#function_identifier.
    def exitFunction_identifier(self, ctx:VerilogParser.Function_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#gate_instance_identifier.
    def enterGate_instance_identifier(self, ctx:VerilogParser.Gate_instance_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#gate_instance_identifier.
    def exitGate_instance_identifier(self, ctx:VerilogParser.Gate_instance_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#generate_block_identifier.
    def enterGenerate_block_identifier(self, ctx:VerilogParser.Generate_block_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#generate_block_identifier.
    def exitGenerate_block_identifier(self, ctx:VerilogParser.Generate_block_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#genvar_identifier.
    def enterGenvar_identifier(self, ctx:VerilogParser.Genvar_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#genvar_identifier.
    def exitGenvar_identifier(self, ctx:VerilogParser.Genvar_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#hierarchical_block_identifier.
    def enterHierarchical_block_identifier(self, ctx:VerilogParser.Hierarchical_block_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#hierarchical_block_identifier.
    def exitHierarchical_block_identifier(self, ctx:VerilogParser.Hierarchical_block_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#hierarchical_event_identifier.
    def enterHierarchical_event_identifier(self, ctx:VerilogParser.Hierarchical_event_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#hierarchical_event_identifier.
    def exitHierarchical_event_identifier(self, ctx:VerilogParser.Hierarchical_event_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#hierarchical_function_identifier.
    def enterHierarchical_function_identifier(self, ctx:VerilogParser.Hierarchical_function_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#hierarchical_function_identifier.
    def exitHierarchical_function_identifier(self, ctx:VerilogParser.Hierarchical_function_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#hierarchical_identifier.
    def enterHierarchical_identifier(self, ctx:VerilogParser.Hierarchical_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#hierarchical_identifier.
    def exitHierarchical_identifier(self, ctx:VerilogParser.Hierarchical_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#hierarchical_net_identifier.
    def enterHierarchical_net_identifier(self, ctx:VerilogParser.Hierarchical_net_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#hierarchical_net_identifier.
    def exitHierarchical_net_identifier(self, ctx:VerilogParser.Hierarchical_net_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#hierarchical_parameter_identifier.
    def enterHierarchical_parameter_identifier(self, ctx:VerilogParser.Hierarchical_parameter_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#hierarchical_parameter_identifier.
    def exitHierarchical_parameter_identifier(self, ctx:VerilogParser.Hierarchical_parameter_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#hierarchical_variable_identifier.
    def enterHierarchical_variable_identifier(self, ctx:VerilogParser.Hierarchical_variable_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#hierarchical_variable_identifier.
    def exitHierarchical_variable_identifier(self, ctx:VerilogParser.Hierarchical_variable_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#hierarchical_task_identifier.
    def enterHierarchical_task_identifier(self, ctx:VerilogParser.Hierarchical_task_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#hierarchical_task_identifier.
    def exitHierarchical_task_identifier(self, ctx:VerilogParser.Hierarchical_task_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#identifier.
    def enterIdentifier(self, ctx:VerilogParser.IdentifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#identifier.
    def exitIdentifier(self, ctx:VerilogParser.IdentifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#inout_port_identifier.
    def enterInout_port_identifier(self, ctx:VerilogParser.Inout_port_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#inout_port_identifier.
    def exitInout_port_identifier(self, ctx:VerilogParser.Inout_port_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#input_port_identifier.
    def enterInput_port_identifier(self, ctx:VerilogParser.Input_port_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#input_port_identifier.
    def exitInput_port_identifier(self, ctx:VerilogParser.Input_port_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#instance_identifier.
    def enterInstance_identifier(self, ctx:VerilogParser.Instance_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#instance_identifier.
    def exitInstance_identifier(self, ctx:VerilogParser.Instance_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#library_identifier.
    def enterLibrary_identifier(self, ctx:VerilogParser.Library_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#library_identifier.
    def exitLibrary_identifier(self, ctx:VerilogParser.Library_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_identifier.
    def enterModule_identifier(self, ctx:VerilogParser.Module_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_identifier.
    def exitModule_identifier(self, ctx:VerilogParser.Module_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_instance_identifier.
    def enterModule_instance_identifier(self, ctx:VerilogParser.Module_instance_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_instance_identifier.
    def exitModule_instance_identifier(self, ctx:VerilogParser.Module_instance_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#net_identifier.
    def enterNet_identifier(self, ctx:VerilogParser.Net_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#net_identifier.
    def exitNet_identifier(self, ctx:VerilogParser.Net_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#output_port_identifier.
    def enterOutput_port_identifier(self, ctx:VerilogParser.Output_port_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#output_port_identifier.
    def exitOutput_port_identifier(self, ctx:VerilogParser.Output_port_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#parameter_identifier.
    def enterParameter_identifier(self, ctx:VerilogParser.Parameter_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#parameter_identifier.
    def exitParameter_identifier(self, ctx:VerilogParser.Parameter_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#port_identifier.
    def enterPort_identifier(self, ctx:VerilogParser.Port_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#port_identifier.
    def exitPort_identifier(self, ctx:VerilogParser.Port_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#real_identifier.
    def enterReal_identifier(self, ctx:VerilogParser.Real_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#real_identifier.
    def exitReal_identifier(self, ctx:VerilogParser.Real_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#specparam_identifier.
    def enterSpecparam_identifier(self, ctx:VerilogParser.Specparam_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#specparam_identifier.
    def exitSpecparam_identifier(self, ctx:VerilogParser.Specparam_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#system_function_identifier.
    def enterSystem_function_identifier(self, ctx:VerilogParser.System_function_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#system_function_identifier.
    def exitSystem_function_identifier(self, ctx:VerilogParser.System_function_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#system_task_identifier.
    def enterSystem_task_identifier(self, ctx:VerilogParser.System_task_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#system_task_identifier.
    def exitSystem_task_identifier(self, ctx:VerilogParser.System_task_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#task_identifier.
    def enterTask_identifier(self, ctx:VerilogParser.Task_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#task_identifier.
    def exitTask_identifier(self, ctx:VerilogParser.Task_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#terminal_identifier.
    def enterTerminal_identifier(self, ctx:VerilogParser.Terminal_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#terminal_identifier.
    def exitTerminal_identifier(self, ctx:VerilogParser.Terminal_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#topmodule_identifier.
    def enterTopmodule_identifier(self, ctx:VerilogParser.Topmodule_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#topmodule_identifier.
    def exitTopmodule_identifier(self, ctx:VerilogParser.Topmodule_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#udp_identifier.
    def enterUdp_identifier(self, ctx:VerilogParser.Udp_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#udp_identifier.
    def exitUdp_identifier(self, ctx:VerilogParser.Udp_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#udp_instance_identifier.
    def enterUdp_instance_identifier(self, ctx:VerilogParser.Udp_instance_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#udp_instance_identifier.
    def exitUdp_instance_identifier(self, ctx:VerilogParser.Udp_instance_identifierContext):
        pass


    # Enter a parse tree produced by VerilogParser#variable_identifier.
    def enterVariable_identifier(self, ctx:VerilogParser.Variable_identifierContext):
        pass

    # Exit a parse tree produced by VerilogParser#variable_identifier.
    def exitVariable_identifier(self, ctx:VerilogParser.Variable_identifierContext):
        pass



del VerilogParser