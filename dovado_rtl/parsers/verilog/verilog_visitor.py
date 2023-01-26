from antlr4 import IllegalStateException, ParserRuleContext, RuleContext
from dovado_rtl.parsing_utilities import (
    AntlrParameter,
    Port,
    PORT_DIMENSION,
    PORT_DIRECTION,
)
from dovado_rtl.parsers.verilog.generated.VerilogParserVisitor import (
    VerilogParserVisitor,
)
from dovado_rtl.parsers.verilog.generated.VerilogParser import VerilogParser
from dovado_rtl.parsing_utilities.antlr.hdl.hdl_antlr_module import HdlAntlrModule


class VerilogVisitor(VerilogParserVisitor):
    def visitSource_text(
        self, ctx: VerilogParser.Source_textContext
    ) -> list[HdlAntlrModule]:
        modules: list[HdlAntlrModule]

        descriptions = ctx.description()
        modules = []
        if descriptions:
            for description in descriptions:
                modules += self.visitDescription(description)
        return modules

    def visitDescription(self, ctx: VerilogParser.DescriptionContext) -> HdlAntlrModule:
        module_declaration = ctx.module_declaration()

        if module_declaration:
            return self.visitModule_declaration(module_declaration)

    def visitModule_declaration(self, ctx: VerilogParser.Module_declarationContext):
        parsed_module_identifier: str
        parameters: list[AntlrParameter]
        ports: list[Port]

        module_identifier = ctx.module_identifier()
        module_parameter_port_list = ctx.module_parameter_port_list()
        list_of_port_declarations = ctx.list_of_port_declarations()
        module_items = ctx.module_item()

        if module_identifier:
            parsed_module_identifier = module_identifier.getText()
        else:
            raise IllegalStateException("A module must have a valid identifier")

        if module_parameter_port_list:
            self.visitModule_parameter_port_list(module_parameter_port_list)
        if list_of_port_declarations:
            self.visitList_of_port_declarations(list_of_port_declarations)
        if module_items:
            for module_item in module_items:
                self.visitModule_item(module_item)
