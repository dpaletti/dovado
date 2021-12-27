# Generated from VerilogPreprocessorParser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VerilogPreprocessorParser import VerilogPreprocessorParser
else:
    from VerilogPreprocessorParser import VerilogPreprocessorParser

# This class defines a complete listener for a parse tree produced by VerilogPreprocessorParser.
class VerilogPreprocessorParserListener(ParseTreeListener):

    # Enter a parse tree produced by VerilogPreprocessorParser#source_text.
    def enterSource_text(self, ctx:VerilogPreprocessorParser.Source_textContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#source_text.
    def exitSource_text(self, ctx:VerilogPreprocessorParser.Source_textContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#compiler_directive.
    def enterCompiler_directive(self, ctx:VerilogPreprocessorParser.Compiler_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#compiler_directive.
    def exitCompiler_directive(self, ctx:VerilogPreprocessorParser.Compiler_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#celldefine_compiler_directive.
    def enterCelldefine_compiler_directive(self, ctx:VerilogPreprocessorParser.Celldefine_compiler_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#celldefine_compiler_directive.
    def exitCelldefine_compiler_directive(self, ctx:VerilogPreprocessorParser.Celldefine_compiler_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#endcelldefine_compiler_directive.
    def enterEndcelldefine_compiler_directive(self, ctx:VerilogPreprocessorParser.Endcelldefine_compiler_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#endcelldefine_compiler_directive.
    def exitEndcelldefine_compiler_directive(self, ctx:VerilogPreprocessorParser.Endcelldefine_compiler_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#default_nettype_compiler_directive.
    def enterDefault_nettype_compiler_directive(self, ctx:VerilogPreprocessorParser.Default_nettype_compiler_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#default_nettype_compiler_directive.
    def exitDefault_nettype_compiler_directive(self, ctx:VerilogPreprocessorParser.Default_nettype_compiler_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#default_nettype_value.
    def enterDefault_nettype_value(self, ctx:VerilogPreprocessorParser.Default_nettype_valueContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#default_nettype_value.
    def exitDefault_nettype_value(self, ctx:VerilogPreprocessorParser.Default_nettype_valueContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#text_macro_definition.
    def enterText_macro_definition(self, ctx:VerilogPreprocessorParser.Text_macro_definitionContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#text_macro_definition.
    def exitText_macro_definition(self, ctx:VerilogPreprocessorParser.Text_macro_definitionContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#text_macro_usage.
    def enterText_macro_usage(self, ctx:VerilogPreprocessorParser.Text_macro_usageContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#text_macro_usage.
    def exitText_macro_usage(self, ctx:VerilogPreprocessorParser.Text_macro_usageContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#macro_list_of_actual_arguments.
    def enterMacro_list_of_actual_arguments(self, ctx:VerilogPreprocessorParser.Macro_list_of_actual_argumentsContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#macro_list_of_actual_arguments.
    def exitMacro_list_of_actual_arguments(self, ctx:VerilogPreprocessorParser.Macro_list_of_actual_argumentsContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#text_macro_identifier.
    def enterText_macro_identifier(self, ctx:VerilogPreprocessorParser.Text_macro_identifierContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#text_macro_identifier.
    def exitText_macro_identifier(self, ctx:VerilogPreprocessorParser.Text_macro_identifierContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#undefine_compiler_directive.
    def enterUndefine_compiler_directive(self, ctx:VerilogPreprocessorParser.Undefine_compiler_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#undefine_compiler_directive.
    def exitUndefine_compiler_directive(self, ctx:VerilogPreprocessorParser.Undefine_compiler_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#ifdef_directive.
    def enterIfdef_directive(self, ctx:VerilogPreprocessorParser.Ifdef_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#ifdef_directive.
    def exitIfdef_directive(self, ctx:VerilogPreprocessorParser.Ifdef_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#ifndef_directive.
    def enterIfndef_directive(self, ctx:VerilogPreprocessorParser.Ifndef_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#ifndef_directive.
    def exitIfndef_directive(self, ctx:VerilogPreprocessorParser.Ifndef_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#elsif_directive.
    def enterElsif_directive(self, ctx:VerilogPreprocessorParser.Elsif_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#elsif_directive.
    def exitElsif_directive(self, ctx:VerilogPreprocessorParser.Elsif_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#else_directive.
    def enterElse_directive(self, ctx:VerilogPreprocessorParser.Else_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#else_directive.
    def exitElse_directive(self, ctx:VerilogPreprocessorParser.Else_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#endif_directive.
    def enterEndif_directive(self, ctx:VerilogPreprocessorParser.Endif_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#endif_directive.
    def exitEndif_directive(self, ctx:VerilogPreprocessorParser.Endif_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#include_compiler_directive.
    def enterInclude_compiler_directive(self, ctx:VerilogPreprocessorParser.Include_compiler_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#include_compiler_directive.
    def exitInclude_compiler_directive(self, ctx:VerilogPreprocessorParser.Include_compiler_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#filename.
    def enterFilename(self, ctx:VerilogPreprocessorParser.FilenameContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#filename.
    def exitFilename(self, ctx:VerilogPreprocessorParser.FilenameContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#resetall_compiler_directive.
    def enterResetall_compiler_directive(self, ctx:VerilogPreprocessorParser.Resetall_compiler_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#resetall_compiler_directive.
    def exitResetall_compiler_directive(self, ctx:VerilogPreprocessorParser.Resetall_compiler_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#line_compiler_directive.
    def enterLine_compiler_directive(self, ctx:VerilogPreprocessorParser.Line_compiler_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#line_compiler_directive.
    def exitLine_compiler_directive(self, ctx:VerilogPreprocessorParser.Line_compiler_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#line_number.
    def enterLine_number(self, ctx:VerilogPreprocessorParser.Line_numberContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#line_number.
    def exitLine_number(self, ctx:VerilogPreprocessorParser.Line_numberContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#line_level.
    def enterLine_level(self, ctx:VerilogPreprocessorParser.Line_levelContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#line_level.
    def exitLine_level(self, ctx:VerilogPreprocessorParser.Line_levelContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#timescale_compiler_directive.
    def enterTimescale_compiler_directive(self, ctx:VerilogPreprocessorParser.Timescale_compiler_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#timescale_compiler_directive.
    def exitTimescale_compiler_directive(self, ctx:VerilogPreprocessorParser.Timescale_compiler_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#time_literal.
    def enterTime_literal(self, ctx:VerilogPreprocessorParser.Time_literalContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#time_literal.
    def exitTime_literal(self, ctx:VerilogPreprocessorParser.Time_literalContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#time_number.
    def enterTime_number(self, ctx:VerilogPreprocessorParser.Time_numberContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#time_number.
    def exitTime_number(self, ctx:VerilogPreprocessorParser.Time_numberContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#time_unit.
    def enterTime_unit(self, ctx:VerilogPreprocessorParser.Time_unitContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#time_unit.
    def exitTime_unit(self, ctx:VerilogPreprocessorParser.Time_unitContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#unconnected_drive_compiler_directive.
    def enterUnconnected_drive_compiler_directive(self, ctx:VerilogPreprocessorParser.Unconnected_drive_compiler_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#unconnected_drive_compiler_directive.
    def exitUnconnected_drive_compiler_directive(self, ctx:VerilogPreprocessorParser.Unconnected_drive_compiler_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#unconnected_drive_value.
    def enterUnconnected_drive_value(self, ctx:VerilogPreprocessorParser.Unconnected_drive_valueContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#unconnected_drive_value.
    def exitUnconnected_drive_value(self, ctx:VerilogPreprocessorParser.Unconnected_drive_valueContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#nounconnected_drive_compiler_directive.
    def enterNounconnected_drive_compiler_directive(self, ctx:VerilogPreprocessorParser.Nounconnected_drive_compiler_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#nounconnected_drive_compiler_directive.
    def exitNounconnected_drive_compiler_directive(self, ctx:VerilogPreprocessorParser.Nounconnected_drive_compiler_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#keywords_directive.
    def enterKeywords_directive(self, ctx:VerilogPreprocessorParser.Keywords_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#keywords_directive.
    def exitKeywords_directive(self, ctx:VerilogPreprocessorParser.Keywords_directiveContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#version_specifier.
    def enterVersion_specifier(self, ctx:VerilogPreprocessorParser.Version_specifierContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#version_specifier.
    def exitVersion_specifier(self, ctx:VerilogPreprocessorParser.Version_specifierContext):
        pass


    # Enter a parse tree produced by VerilogPreprocessorParser#endkeywords_directive.
    def enterEndkeywords_directive(self, ctx:VerilogPreprocessorParser.Endkeywords_directiveContext):
        pass

    # Exit a parse tree produced by VerilogPreprocessorParser#endkeywords_directive.
    def exitEndkeywords_directive(self, ctx:VerilogPreprocessorParser.Endkeywords_directiveContext):
        pass



del VerilogPreprocessorParser