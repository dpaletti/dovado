# Generated from VerilogPreprocessorParser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VerilogPreprocessorParser import VerilogPreprocessorParser
else:
    from VerilogPreprocessorParser import VerilogPreprocessorParser

# This class defines a complete generic visitor for a parse tree produced by VerilogPreprocessorParser.

class VerilogPreprocessorParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VerilogPreprocessorParser#source_text.
    def visitSource_text(self, ctx:VerilogPreprocessorParser.Source_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#compiler_directive.
    def visitCompiler_directive(self, ctx:VerilogPreprocessorParser.Compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#celldefine_compiler_directive.
    def visitCelldefine_compiler_directive(self, ctx:VerilogPreprocessorParser.Celldefine_compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#endcelldefine_compiler_directive.
    def visitEndcelldefine_compiler_directive(self, ctx:VerilogPreprocessorParser.Endcelldefine_compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#default_nettype_compiler_directive.
    def visitDefault_nettype_compiler_directive(self, ctx:VerilogPreprocessorParser.Default_nettype_compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#default_nettype_value.
    def visitDefault_nettype_value(self, ctx:VerilogPreprocessorParser.Default_nettype_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#text_macro_definition.
    def visitText_macro_definition(self, ctx:VerilogPreprocessorParser.Text_macro_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#text_macro_usage.
    def visitText_macro_usage(self, ctx:VerilogPreprocessorParser.Text_macro_usageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#macro_list_of_actual_arguments.
    def visitMacro_list_of_actual_arguments(self, ctx:VerilogPreprocessorParser.Macro_list_of_actual_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#text_macro_identifier.
    def visitText_macro_identifier(self, ctx:VerilogPreprocessorParser.Text_macro_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#undefine_compiler_directive.
    def visitUndefine_compiler_directive(self, ctx:VerilogPreprocessorParser.Undefine_compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#ifdef_directive.
    def visitIfdef_directive(self, ctx:VerilogPreprocessorParser.Ifdef_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#ifndef_directive.
    def visitIfndef_directive(self, ctx:VerilogPreprocessorParser.Ifndef_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#elsif_directive.
    def visitElsif_directive(self, ctx:VerilogPreprocessorParser.Elsif_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#else_directive.
    def visitElse_directive(self, ctx:VerilogPreprocessorParser.Else_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#endif_directive.
    def visitEndif_directive(self, ctx:VerilogPreprocessorParser.Endif_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#include_compiler_directive.
    def visitInclude_compiler_directive(self, ctx:VerilogPreprocessorParser.Include_compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#filename.
    def visitFilename(self, ctx:VerilogPreprocessorParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#resetall_compiler_directive.
    def visitResetall_compiler_directive(self, ctx:VerilogPreprocessorParser.Resetall_compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#line_compiler_directive.
    def visitLine_compiler_directive(self, ctx:VerilogPreprocessorParser.Line_compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#line_number.
    def visitLine_number(self, ctx:VerilogPreprocessorParser.Line_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#line_level.
    def visitLine_level(self, ctx:VerilogPreprocessorParser.Line_levelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#timescale_compiler_directive.
    def visitTimescale_compiler_directive(self, ctx:VerilogPreprocessorParser.Timescale_compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#time_literal.
    def visitTime_literal(self, ctx:VerilogPreprocessorParser.Time_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#time_number.
    def visitTime_number(self, ctx:VerilogPreprocessorParser.Time_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#time_unit.
    def visitTime_unit(self, ctx:VerilogPreprocessorParser.Time_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#unconnected_drive_compiler_directive.
    def visitUnconnected_drive_compiler_directive(self, ctx:VerilogPreprocessorParser.Unconnected_drive_compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#unconnected_drive_value.
    def visitUnconnected_drive_value(self, ctx:VerilogPreprocessorParser.Unconnected_drive_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#nounconnected_drive_compiler_directive.
    def visitNounconnected_drive_compiler_directive(self, ctx:VerilogPreprocessorParser.Nounconnected_drive_compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#keywords_directive.
    def visitKeywords_directive(self, ctx:VerilogPreprocessorParser.Keywords_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#version_specifier.
    def visitVersion_specifier(self, ctx:VerilogPreprocessorParser.Version_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogPreprocessorParser#endkeywords_directive.
    def visitEndkeywords_directive(self, ctx:VerilogPreprocessorParser.Endkeywords_directiveContext):
        return self.visitChildren(ctx)



del VerilogPreprocessorParser