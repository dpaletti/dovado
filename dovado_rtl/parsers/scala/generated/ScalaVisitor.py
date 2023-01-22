# Generated from Scala.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ScalaParser import ScalaParser
else:
    from ScalaParser import ScalaParser

# This class defines a complete generic visitor for a parse tree produced by ScalaParser.

class ScalaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ScalaParser#literal.
    def visitLiteral(self, ctx:ScalaParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#qualId.
    def visitQualId(self, ctx:ScalaParser.QualIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#ids.
    def visitIds(self, ctx:ScalaParser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#stableId.
    def visitStableId(self, ctx:ScalaParser.StableIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#classQualifier.
    def visitClassQualifier(self, ctx:ScalaParser.ClassQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#type_.
    def visitType_(self, ctx:ScalaParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#functionArgTypes.
    def visitFunctionArgTypes(self, ctx:ScalaParser.FunctionArgTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#existentialClause.
    def visitExistentialClause(self, ctx:ScalaParser.ExistentialClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#existentialDcl.
    def visitExistentialDcl(self, ctx:ScalaParser.ExistentialDclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#infixType.
    def visitInfixType(self, ctx:ScalaParser.InfixTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#compoundType.
    def visitCompoundType(self, ctx:ScalaParser.CompoundTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#annotType.
    def visitAnnotType(self, ctx:ScalaParser.AnnotTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#simpleType.
    def visitSimpleType(self, ctx:ScalaParser.SimpleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#typeArgs.
    def visitTypeArgs(self, ctx:ScalaParser.TypeArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#types.
    def visitTypes(self, ctx:ScalaParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#refinement.
    def visitRefinement(self, ctx:ScalaParser.RefinementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#refineStat.
    def visitRefineStat(self, ctx:ScalaParser.RefineStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#typePat.
    def visitTypePat(self, ctx:ScalaParser.TypePatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#ascription.
    def visitAscription(self, ctx:ScalaParser.AscriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#expr.
    def visitExpr(self, ctx:ScalaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#expr1.
    def visitExpr1(self, ctx:ScalaParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#prefixDef.
    def visitPrefixDef(self, ctx:ScalaParser.PrefixDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#postfixExpr.
    def visitPostfixExpr(self, ctx:ScalaParser.PostfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#infixExpr.
    def visitInfixExpr(self, ctx:ScalaParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#prefixExpr.
    def visitPrefixExpr(self, ctx:ScalaParser.PrefixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#simpleExpr.
    def visitSimpleExpr(self, ctx:ScalaParser.SimpleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#simpleExpr1.
    def visitSimpleExpr1(self, ctx:ScalaParser.SimpleExpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#exprs.
    def visitExprs(self, ctx:ScalaParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#argumentExprs.
    def visitArgumentExprs(self, ctx:ScalaParser.ArgumentExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#args.
    def visitArgs(self, ctx:ScalaParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#blockExpr.
    def visitBlockExpr(self, ctx:ScalaParser.BlockExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#block.
    def visitBlock(self, ctx:ScalaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#blockStat.
    def visitBlockStat(self, ctx:ScalaParser.BlockStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#resultExpr.
    def visitResultExpr(self, ctx:ScalaParser.ResultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#enumerators.
    def visitEnumerators(self, ctx:ScalaParser.EnumeratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#generator.
    def visitGenerator(self, ctx:ScalaParser.GeneratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#caseClauses.
    def visitCaseClauses(self, ctx:ScalaParser.CaseClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#caseClause.
    def visitCaseClause(self, ctx:ScalaParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#guard_.
    def visitGuard_(self, ctx:ScalaParser.Guard_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#pattern.
    def visitPattern(self, ctx:ScalaParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#pattern1.
    def visitPattern1(self, ctx:ScalaParser.Pattern1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#pattern2.
    def visitPattern2(self, ctx:ScalaParser.Pattern2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#pattern3.
    def visitPattern3(self, ctx:ScalaParser.Pattern3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#simplePattern.
    def visitSimplePattern(self, ctx:ScalaParser.SimplePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#patterns.
    def visitPatterns(self, ctx:ScalaParser.PatternsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#typeParamClause.
    def visitTypeParamClause(self, ctx:ScalaParser.TypeParamClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#funTypeParamClause.
    def visitFunTypeParamClause(self, ctx:ScalaParser.FunTypeParamClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#variantTypeParam.
    def visitVariantTypeParam(self, ctx:ScalaParser.VariantTypeParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#typeParam.
    def visitTypeParam(self, ctx:ScalaParser.TypeParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#paramClauses.
    def visitParamClauses(self, ctx:ScalaParser.ParamClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#paramClause.
    def visitParamClause(self, ctx:ScalaParser.ParamClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#params.
    def visitParams(self, ctx:ScalaParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#param.
    def visitParam(self, ctx:ScalaParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#paramType.
    def visitParamType(self, ctx:ScalaParser.ParamTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#classParamClauses.
    def visitClassParamClauses(self, ctx:ScalaParser.ClassParamClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#classParamClause.
    def visitClassParamClause(self, ctx:ScalaParser.ClassParamClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#classParams.
    def visitClassParams(self, ctx:ScalaParser.ClassParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#classParam.
    def visitClassParam(self, ctx:ScalaParser.ClassParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#bindings.
    def visitBindings(self, ctx:ScalaParser.BindingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#binding.
    def visitBinding(self, ctx:ScalaParser.BindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#modifier.
    def visitModifier(self, ctx:ScalaParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#localModifier.
    def visitLocalModifier(self, ctx:ScalaParser.LocalModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#accessModifier.
    def visitAccessModifier(self, ctx:ScalaParser.AccessModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#accessQualifier.
    def visitAccessQualifier(self, ctx:ScalaParser.AccessQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#annotation.
    def visitAnnotation(self, ctx:ScalaParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#constrAnnotation.
    def visitConstrAnnotation(self, ctx:ScalaParser.ConstrAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#templateBody.
    def visitTemplateBody(self, ctx:ScalaParser.TemplateBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#templateStat.
    def visitTemplateStat(self, ctx:ScalaParser.TemplateStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#selfType.
    def visitSelfType(self, ctx:ScalaParser.SelfTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#import_.
    def visitImport_(self, ctx:ScalaParser.Import_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#importExpr.
    def visitImportExpr(self, ctx:ScalaParser.ImportExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#importSelectors.
    def visitImportSelectors(self, ctx:ScalaParser.ImportSelectorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#importSelector.
    def visitImportSelector(self, ctx:ScalaParser.ImportSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#dcl.
    def visitDcl(self, ctx:ScalaParser.DclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#valDcl.
    def visitValDcl(self, ctx:ScalaParser.ValDclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#varDcl.
    def visitVarDcl(self, ctx:ScalaParser.VarDclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#funDcl.
    def visitFunDcl(self, ctx:ScalaParser.FunDclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#funSig.
    def visitFunSig(self, ctx:ScalaParser.FunSigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#typeDcl.
    def visitTypeDcl(self, ctx:ScalaParser.TypeDclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#patVarDef.
    def visitPatVarDef(self, ctx:ScalaParser.PatVarDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#def_.
    def visitDef_(self, ctx:ScalaParser.Def_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#patDef.
    def visitPatDef(self, ctx:ScalaParser.PatDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#varDef.
    def visitVarDef(self, ctx:ScalaParser.VarDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#funDef.
    def visitFunDef(self, ctx:ScalaParser.FunDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#typeDef.
    def visitTypeDef(self, ctx:ScalaParser.TypeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#tmplDef.
    def visitTmplDef(self, ctx:ScalaParser.TmplDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#classDef.
    def visitClassDef(self, ctx:ScalaParser.ClassDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#traitDef.
    def visitTraitDef(self, ctx:ScalaParser.TraitDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#objectDef.
    def visitObjectDef(self, ctx:ScalaParser.ObjectDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#classTemplateOpt.
    def visitClassTemplateOpt(self, ctx:ScalaParser.ClassTemplateOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#traitTemplateOpt.
    def visitTraitTemplateOpt(self, ctx:ScalaParser.TraitTemplateOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#classTemplate.
    def visitClassTemplate(self, ctx:ScalaParser.ClassTemplateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#traitTemplate.
    def visitTraitTemplate(self, ctx:ScalaParser.TraitTemplateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#classParents.
    def visitClassParents(self, ctx:ScalaParser.ClassParentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#traitParents.
    def visitTraitParents(self, ctx:ScalaParser.TraitParentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#constr.
    def visitConstr(self, ctx:ScalaParser.ConstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#earlyDefs.
    def visitEarlyDefs(self, ctx:ScalaParser.EarlyDefsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#earlyDef.
    def visitEarlyDef(self, ctx:ScalaParser.EarlyDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#constrExpr.
    def visitConstrExpr(self, ctx:ScalaParser.ConstrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#constrBlock.
    def visitConstrBlock(self, ctx:ScalaParser.ConstrBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#selfInvocation.
    def visitSelfInvocation(self, ctx:ScalaParser.SelfInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#topStatSeq.
    def visitTopStatSeq(self, ctx:ScalaParser.TopStatSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#topStat.
    def visitTopStat(self, ctx:ScalaParser.TopStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#packaging.
    def visitPackaging(self, ctx:ScalaParser.PackagingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#packageObject.
    def visitPackageObject(self, ctx:ScalaParser.PackageObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalaParser#compilationUnit.
    def visitCompilationUnit(self, ctx:ScalaParser.CompilationUnitContext):
        return self.visitChildren(ctx)



del ScalaParser