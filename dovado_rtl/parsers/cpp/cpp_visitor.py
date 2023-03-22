from typing import Optional
from dovado_rtl.parsers.cpp.generated.CPP14Parser import CPP14Parser
from dovado_rtl.parsers.cpp.generated.CPP14ParserVisitor import CPP14ParserVisitor
from dovado_rtl.parsers.utilities.antlr.antlr_parameter import AntlrParameter
from dovado_rtl.parsers.utilities.antlr.antlr_module import AntlrModule


class CppVisitor(CPP14ParserVisitor):
    def visitTranslationUnit(
        self, ctx: CPP14Parser.TranslationUnitContext
    ) -> list[AntlrModule]:
        declaration_seq = ctx.declarationseq()
        if declaration_seq:
            return [self.visitDeclarationseq(declaration_seq)]
        return [AntlrModule(name="", parameters=[])]

    def visitDeclarationseq(
        self, ctx: CPP14Parser.DeclarationseqContext
    ) -> AntlrModule:
        declarations = ctx.declaration()
        if declarations is None:
            raise ValueError("A declarationseq must contain at least one declaration")

        parameters: list[AntlrParameter] = []
        for declaration in declarations:
            declaration = self.visitDeclaration(declaration)
            if declaration is not None:
                parameters.append(declaration)

        return AntlrModule(name="", parameters=parameters)

    def visitDeclaration(
        self, ctx: CPP14Parser.DeclarationContext
    ) -> Optional[AntlrParameter]:
        define = ctx.define()

        if define:
            return self.visitDefine(define)
        return None

    def visitDefine(self, ctx: CPP14Parser.DefineContext) -> Optional[AntlrParameter]:
        identifier = ctx.Identifier()
        expression = ctx.primaryExpression()

        if ctx.declarator():
            return None

        if identifier is None or expression is None:
            raise ValueError("Identifier and Expression are necessary for a define")
        return AntlrParameter(
            name=str(identifier),
            value=expression.getText(),
            rule=expression,
            has_default=True,
        )
