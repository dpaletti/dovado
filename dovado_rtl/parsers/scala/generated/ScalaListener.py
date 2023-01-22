# Generated from Scala.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ScalaParser import ScalaParser
else:
    from ScalaParser import ScalaParser

# This class defines a complete listener for a parse tree produced by ScalaParser.
class ScalaListener(ParseTreeListener):

    # Enter a parse tree produced by ScalaParser#literal.
    def enterLiteral(self, ctx:ScalaParser.LiteralContext):
        pass

    # Exit a parse tree produced by ScalaParser#literal.
    def exitLiteral(self, ctx:ScalaParser.LiteralContext):
        pass


    # Enter a parse tree produced by ScalaParser#qualId.
    def enterQualId(self, ctx:ScalaParser.QualIdContext):
        pass

    # Exit a parse tree produced by ScalaParser#qualId.
    def exitQualId(self, ctx:ScalaParser.QualIdContext):
        pass


    # Enter a parse tree produced by ScalaParser#ids.
    def enterIds(self, ctx:ScalaParser.IdsContext):
        pass

    # Exit a parse tree produced by ScalaParser#ids.
    def exitIds(self, ctx:ScalaParser.IdsContext):
        pass


    # Enter a parse tree produced by ScalaParser#stableId.
    def enterStableId(self, ctx:ScalaParser.StableIdContext):
        pass

    # Exit a parse tree produced by ScalaParser#stableId.
    def exitStableId(self, ctx:ScalaParser.StableIdContext):
        pass


    # Enter a parse tree produced by ScalaParser#classQualifier.
    def enterClassQualifier(self, ctx:ScalaParser.ClassQualifierContext):
        pass

    # Exit a parse tree produced by ScalaParser#classQualifier.
    def exitClassQualifier(self, ctx:ScalaParser.ClassQualifierContext):
        pass


    # Enter a parse tree produced by ScalaParser#type_.
    def enterType_(self, ctx:ScalaParser.Type_Context):
        pass

    # Exit a parse tree produced by ScalaParser#type_.
    def exitType_(self, ctx:ScalaParser.Type_Context):
        pass


    # Enter a parse tree produced by ScalaParser#functionArgTypes.
    def enterFunctionArgTypes(self, ctx:ScalaParser.FunctionArgTypesContext):
        pass

    # Exit a parse tree produced by ScalaParser#functionArgTypes.
    def exitFunctionArgTypes(self, ctx:ScalaParser.FunctionArgTypesContext):
        pass


    # Enter a parse tree produced by ScalaParser#existentialClause.
    def enterExistentialClause(self, ctx:ScalaParser.ExistentialClauseContext):
        pass

    # Exit a parse tree produced by ScalaParser#existentialClause.
    def exitExistentialClause(self, ctx:ScalaParser.ExistentialClauseContext):
        pass


    # Enter a parse tree produced by ScalaParser#existentialDcl.
    def enterExistentialDcl(self, ctx:ScalaParser.ExistentialDclContext):
        pass

    # Exit a parse tree produced by ScalaParser#existentialDcl.
    def exitExistentialDcl(self, ctx:ScalaParser.ExistentialDclContext):
        pass


    # Enter a parse tree produced by ScalaParser#infixType.
    def enterInfixType(self, ctx:ScalaParser.InfixTypeContext):
        pass

    # Exit a parse tree produced by ScalaParser#infixType.
    def exitInfixType(self, ctx:ScalaParser.InfixTypeContext):
        pass


    # Enter a parse tree produced by ScalaParser#compoundType.
    def enterCompoundType(self, ctx:ScalaParser.CompoundTypeContext):
        pass

    # Exit a parse tree produced by ScalaParser#compoundType.
    def exitCompoundType(self, ctx:ScalaParser.CompoundTypeContext):
        pass


    # Enter a parse tree produced by ScalaParser#annotType.
    def enterAnnotType(self, ctx:ScalaParser.AnnotTypeContext):
        pass

    # Exit a parse tree produced by ScalaParser#annotType.
    def exitAnnotType(self, ctx:ScalaParser.AnnotTypeContext):
        pass


    # Enter a parse tree produced by ScalaParser#simpleType.
    def enterSimpleType(self, ctx:ScalaParser.SimpleTypeContext):
        pass

    # Exit a parse tree produced by ScalaParser#simpleType.
    def exitSimpleType(self, ctx:ScalaParser.SimpleTypeContext):
        pass


    # Enter a parse tree produced by ScalaParser#typeArgs.
    def enterTypeArgs(self, ctx:ScalaParser.TypeArgsContext):
        pass

    # Exit a parse tree produced by ScalaParser#typeArgs.
    def exitTypeArgs(self, ctx:ScalaParser.TypeArgsContext):
        pass


    # Enter a parse tree produced by ScalaParser#types.
    def enterTypes(self, ctx:ScalaParser.TypesContext):
        pass

    # Exit a parse tree produced by ScalaParser#types.
    def exitTypes(self, ctx:ScalaParser.TypesContext):
        pass


    # Enter a parse tree produced by ScalaParser#refinement.
    def enterRefinement(self, ctx:ScalaParser.RefinementContext):
        pass

    # Exit a parse tree produced by ScalaParser#refinement.
    def exitRefinement(self, ctx:ScalaParser.RefinementContext):
        pass


    # Enter a parse tree produced by ScalaParser#refineStat.
    def enterRefineStat(self, ctx:ScalaParser.RefineStatContext):
        pass

    # Exit a parse tree produced by ScalaParser#refineStat.
    def exitRefineStat(self, ctx:ScalaParser.RefineStatContext):
        pass


    # Enter a parse tree produced by ScalaParser#typePat.
    def enterTypePat(self, ctx:ScalaParser.TypePatContext):
        pass

    # Exit a parse tree produced by ScalaParser#typePat.
    def exitTypePat(self, ctx:ScalaParser.TypePatContext):
        pass


    # Enter a parse tree produced by ScalaParser#ascription.
    def enterAscription(self, ctx:ScalaParser.AscriptionContext):
        pass

    # Exit a parse tree produced by ScalaParser#ascription.
    def exitAscription(self, ctx:ScalaParser.AscriptionContext):
        pass


    # Enter a parse tree produced by ScalaParser#expr.
    def enterExpr(self, ctx:ScalaParser.ExprContext):
        pass

    # Exit a parse tree produced by ScalaParser#expr.
    def exitExpr(self, ctx:ScalaParser.ExprContext):
        pass


    # Enter a parse tree produced by ScalaParser#expr1.
    def enterExpr1(self, ctx:ScalaParser.Expr1Context):
        pass

    # Exit a parse tree produced by ScalaParser#expr1.
    def exitExpr1(self, ctx:ScalaParser.Expr1Context):
        pass


    # Enter a parse tree produced by ScalaParser#prefixDef.
    def enterPrefixDef(self, ctx:ScalaParser.PrefixDefContext):
        pass

    # Exit a parse tree produced by ScalaParser#prefixDef.
    def exitPrefixDef(self, ctx:ScalaParser.PrefixDefContext):
        pass


    # Enter a parse tree produced by ScalaParser#postfixExpr.
    def enterPostfixExpr(self, ctx:ScalaParser.PostfixExprContext):
        pass

    # Exit a parse tree produced by ScalaParser#postfixExpr.
    def exitPostfixExpr(self, ctx:ScalaParser.PostfixExprContext):
        pass


    # Enter a parse tree produced by ScalaParser#infixExpr.
    def enterInfixExpr(self, ctx:ScalaParser.InfixExprContext):
        pass

    # Exit a parse tree produced by ScalaParser#infixExpr.
    def exitInfixExpr(self, ctx:ScalaParser.InfixExprContext):
        pass


    # Enter a parse tree produced by ScalaParser#prefixExpr.
    def enterPrefixExpr(self, ctx:ScalaParser.PrefixExprContext):
        pass

    # Exit a parse tree produced by ScalaParser#prefixExpr.
    def exitPrefixExpr(self, ctx:ScalaParser.PrefixExprContext):
        pass


    # Enter a parse tree produced by ScalaParser#simpleExpr.
    def enterSimpleExpr(self, ctx:ScalaParser.SimpleExprContext):
        pass

    # Exit a parse tree produced by ScalaParser#simpleExpr.
    def exitSimpleExpr(self, ctx:ScalaParser.SimpleExprContext):
        pass


    # Enter a parse tree produced by ScalaParser#simpleExpr1.
    def enterSimpleExpr1(self, ctx:ScalaParser.SimpleExpr1Context):
        pass

    # Exit a parse tree produced by ScalaParser#simpleExpr1.
    def exitSimpleExpr1(self, ctx:ScalaParser.SimpleExpr1Context):
        pass


    # Enter a parse tree produced by ScalaParser#exprs.
    def enterExprs(self, ctx:ScalaParser.ExprsContext):
        pass

    # Exit a parse tree produced by ScalaParser#exprs.
    def exitExprs(self, ctx:ScalaParser.ExprsContext):
        pass


    # Enter a parse tree produced by ScalaParser#argumentExprs.
    def enterArgumentExprs(self, ctx:ScalaParser.ArgumentExprsContext):
        pass

    # Exit a parse tree produced by ScalaParser#argumentExprs.
    def exitArgumentExprs(self, ctx:ScalaParser.ArgumentExprsContext):
        pass


    # Enter a parse tree produced by ScalaParser#args.
    def enterArgs(self, ctx:ScalaParser.ArgsContext):
        pass

    # Exit a parse tree produced by ScalaParser#args.
    def exitArgs(self, ctx:ScalaParser.ArgsContext):
        pass


    # Enter a parse tree produced by ScalaParser#blockExpr.
    def enterBlockExpr(self, ctx:ScalaParser.BlockExprContext):
        pass

    # Exit a parse tree produced by ScalaParser#blockExpr.
    def exitBlockExpr(self, ctx:ScalaParser.BlockExprContext):
        pass


    # Enter a parse tree produced by ScalaParser#block.
    def enterBlock(self, ctx:ScalaParser.BlockContext):
        pass

    # Exit a parse tree produced by ScalaParser#block.
    def exitBlock(self, ctx:ScalaParser.BlockContext):
        pass


    # Enter a parse tree produced by ScalaParser#blockStat.
    def enterBlockStat(self, ctx:ScalaParser.BlockStatContext):
        pass

    # Exit a parse tree produced by ScalaParser#blockStat.
    def exitBlockStat(self, ctx:ScalaParser.BlockStatContext):
        pass


    # Enter a parse tree produced by ScalaParser#resultExpr.
    def enterResultExpr(self, ctx:ScalaParser.ResultExprContext):
        pass

    # Exit a parse tree produced by ScalaParser#resultExpr.
    def exitResultExpr(self, ctx:ScalaParser.ResultExprContext):
        pass


    # Enter a parse tree produced by ScalaParser#enumerators.
    def enterEnumerators(self, ctx:ScalaParser.EnumeratorsContext):
        pass

    # Exit a parse tree produced by ScalaParser#enumerators.
    def exitEnumerators(self, ctx:ScalaParser.EnumeratorsContext):
        pass


    # Enter a parse tree produced by ScalaParser#generator.
    def enterGenerator(self, ctx:ScalaParser.GeneratorContext):
        pass

    # Exit a parse tree produced by ScalaParser#generator.
    def exitGenerator(self, ctx:ScalaParser.GeneratorContext):
        pass


    # Enter a parse tree produced by ScalaParser#caseClauses.
    def enterCaseClauses(self, ctx:ScalaParser.CaseClausesContext):
        pass

    # Exit a parse tree produced by ScalaParser#caseClauses.
    def exitCaseClauses(self, ctx:ScalaParser.CaseClausesContext):
        pass


    # Enter a parse tree produced by ScalaParser#caseClause.
    def enterCaseClause(self, ctx:ScalaParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by ScalaParser#caseClause.
    def exitCaseClause(self, ctx:ScalaParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by ScalaParser#guard_.
    def enterGuard_(self, ctx:ScalaParser.Guard_Context):
        pass

    # Exit a parse tree produced by ScalaParser#guard_.
    def exitGuard_(self, ctx:ScalaParser.Guard_Context):
        pass


    # Enter a parse tree produced by ScalaParser#pattern.
    def enterPattern(self, ctx:ScalaParser.PatternContext):
        pass

    # Exit a parse tree produced by ScalaParser#pattern.
    def exitPattern(self, ctx:ScalaParser.PatternContext):
        pass


    # Enter a parse tree produced by ScalaParser#pattern1.
    def enterPattern1(self, ctx:ScalaParser.Pattern1Context):
        pass

    # Exit a parse tree produced by ScalaParser#pattern1.
    def exitPattern1(self, ctx:ScalaParser.Pattern1Context):
        pass


    # Enter a parse tree produced by ScalaParser#pattern2.
    def enterPattern2(self, ctx:ScalaParser.Pattern2Context):
        pass

    # Exit a parse tree produced by ScalaParser#pattern2.
    def exitPattern2(self, ctx:ScalaParser.Pattern2Context):
        pass


    # Enter a parse tree produced by ScalaParser#pattern3.
    def enterPattern3(self, ctx:ScalaParser.Pattern3Context):
        pass

    # Exit a parse tree produced by ScalaParser#pattern3.
    def exitPattern3(self, ctx:ScalaParser.Pattern3Context):
        pass


    # Enter a parse tree produced by ScalaParser#simplePattern.
    def enterSimplePattern(self, ctx:ScalaParser.SimplePatternContext):
        pass

    # Exit a parse tree produced by ScalaParser#simplePattern.
    def exitSimplePattern(self, ctx:ScalaParser.SimplePatternContext):
        pass


    # Enter a parse tree produced by ScalaParser#patterns.
    def enterPatterns(self, ctx:ScalaParser.PatternsContext):
        pass

    # Exit a parse tree produced by ScalaParser#patterns.
    def exitPatterns(self, ctx:ScalaParser.PatternsContext):
        pass


    # Enter a parse tree produced by ScalaParser#typeParamClause.
    def enterTypeParamClause(self, ctx:ScalaParser.TypeParamClauseContext):
        pass

    # Exit a parse tree produced by ScalaParser#typeParamClause.
    def exitTypeParamClause(self, ctx:ScalaParser.TypeParamClauseContext):
        pass


    # Enter a parse tree produced by ScalaParser#funTypeParamClause.
    def enterFunTypeParamClause(self, ctx:ScalaParser.FunTypeParamClauseContext):
        pass

    # Exit a parse tree produced by ScalaParser#funTypeParamClause.
    def exitFunTypeParamClause(self, ctx:ScalaParser.FunTypeParamClauseContext):
        pass


    # Enter a parse tree produced by ScalaParser#variantTypeParam.
    def enterVariantTypeParam(self, ctx:ScalaParser.VariantTypeParamContext):
        pass

    # Exit a parse tree produced by ScalaParser#variantTypeParam.
    def exitVariantTypeParam(self, ctx:ScalaParser.VariantTypeParamContext):
        pass


    # Enter a parse tree produced by ScalaParser#typeParam.
    def enterTypeParam(self, ctx:ScalaParser.TypeParamContext):
        pass

    # Exit a parse tree produced by ScalaParser#typeParam.
    def exitTypeParam(self, ctx:ScalaParser.TypeParamContext):
        pass


    # Enter a parse tree produced by ScalaParser#paramClauses.
    def enterParamClauses(self, ctx:ScalaParser.ParamClausesContext):
        pass

    # Exit a parse tree produced by ScalaParser#paramClauses.
    def exitParamClauses(self, ctx:ScalaParser.ParamClausesContext):
        pass


    # Enter a parse tree produced by ScalaParser#paramClause.
    def enterParamClause(self, ctx:ScalaParser.ParamClauseContext):
        pass

    # Exit a parse tree produced by ScalaParser#paramClause.
    def exitParamClause(self, ctx:ScalaParser.ParamClauseContext):
        pass


    # Enter a parse tree produced by ScalaParser#params.
    def enterParams(self, ctx:ScalaParser.ParamsContext):
        pass

    # Exit a parse tree produced by ScalaParser#params.
    def exitParams(self, ctx:ScalaParser.ParamsContext):
        pass


    # Enter a parse tree produced by ScalaParser#param.
    def enterParam(self, ctx:ScalaParser.ParamContext):
        pass

    # Exit a parse tree produced by ScalaParser#param.
    def exitParam(self, ctx:ScalaParser.ParamContext):
        pass


    # Enter a parse tree produced by ScalaParser#paramType.
    def enterParamType(self, ctx:ScalaParser.ParamTypeContext):
        pass

    # Exit a parse tree produced by ScalaParser#paramType.
    def exitParamType(self, ctx:ScalaParser.ParamTypeContext):
        pass


    # Enter a parse tree produced by ScalaParser#classParamClauses.
    def enterClassParamClauses(self, ctx:ScalaParser.ClassParamClausesContext):
        pass

    # Exit a parse tree produced by ScalaParser#classParamClauses.
    def exitClassParamClauses(self, ctx:ScalaParser.ClassParamClausesContext):
        pass


    # Enter a parse tree produced by ScalaParser#classParamClause.
    def enterClassParamClause(self, ctx:ScalaParser.ClassParamClauseContext):
        pass

    # Exit a parse tree produced by ScalaParser#classParamClause.
    def exitClassParamClause(self, ctx:ScalaParser.ClassParamClauseContext):
        pass


    # Enter a parse tree produced by ScalaParser#classParams.
    def enterClassParams(self, ctx:ScalaParser.ClassParamsContext):
        pass

    # Exit a parse tree produced by ScalaParser#classParams.
    def exitClassParams(self, ctx:ScalaParser.ClassParamsContext):
        pass


    # Enter a parse tree produced by ScalaParser#classParam.
    def enterClassParam(self, ctx:ScalaParser.ClassParamContext):
        pass

    # Exit a parse tree produced by ScalaParser#classParam.
    def exitClassParam(self, ctx:ScalaParser.ClassParamContext):
        pass


    # Enter a parse tree produced by ScalaParser#bindings.
    def enterBindings(self, ctx:ScalaParser.BindingsContext):
        pass

    # Exit a parse tree produced by ScalaParser#bindings.
    def exitBindings(self, ctx:ScalaParser.BindingsContext):
        pass


    # Enter a parse tree produced by ScalaParser#binding.
    def enterBinding(self, ctx:ScalaParser.BindingContext):
        pass

    # Exit a parse tree produced by ScalaParser#binding.
    def exitBinding(self, ctx:ScalaParser.BindingContext):
        pass


    # Enter a parse tree produced by ScalaParser#modifier.
    def enterModifier(self, ctx:ScalaParser.ModifierContext):
        pass

    # Exit a parse tree produced by ScalaParser#modifier.
    def exitModifier(self, ctx:ScalaParser.ModifierContext):
        pass


    # Enter a parse tree produced by ScalaParser#localModifier.
    def enterLocalModifier(self, ctx:ScalaParser.LocalModifierContext):
        pass

    # Exit a parse tree produced by ScalaParser#localModifier.
    def exitLocalModifier(self, ctx:ScalaParser.LocalModifierContext):
        pass


    # Enter a parse tree produced by ScalaParser#accessModifier.
    def enterAccessModifier(self, ctx:ScalaParser.AccessModifierContext):
        pass

    # Exit a parse tree produced by ScalaParser#accessModifier.
    def exitAccessModifier(self, ctx:ScalaParser.AccessModifierContext):
        pass


    # Enter a parse tree produced by ScalaParser#accessQualifier.
    def enterAccessQualifier(self, ctx:ScalaParser.AccessQualifierContext):
        pass

    # Exit a parse tree produced by ScalaParser#accessQualifier.
    def exitAccessQualifier(self, ctx:ScalaParser.AccessQualifierContext):
        pass


    # Enter a parse tree produced by ScalaParser#annotation.
    def enterAnnotation(self, ctx:ScalaParser.AnnotationContext):
        pass

    # Exit a parse tree produced by ScalaParser#annotation.
    def exitAnnotation(self, ctx:ScalaParser.AnnotationContext):
        pass


    # Enter a parse tree produced by ScalaParser#constrAnnotation.
    def enterConstrAnnotation(self, ctx:ScalaParser.ConstrAnnotationContext):
        pass

    # Exit a parse tree produced by ScalaParser#constrAnnotation.
    def exitConstrAnnotation(self, ctx:ScalaParser.ConstrAnnotationContext):
        pass


    # Enter a parse tree produced by ScalaParser#templateBody.
    def enterTemplateBody(self, ctx:ScalaParser.TemplateBodyContext):
        pass

    # Exit a parse tree produced by ScalaParser#templateBody.
    def exitTemplateBody(self, ctx:ScalaParser.TemplateBodyContext):
        pass


    # Enter a parse tree produced by ScalaParser#templateStat.
    def enterTemplateStat(self, ctx:ScalaParser.TemplateStatContext):
        pass

    # Exit a parse tree produced by ScalaParser#templateStat.
    def exitTemplateStat(self, ctx:ScalaParser.TemplateStatContext):
        pass


    # Enter a parse tree produced by ScalaParser#selfType.
    def enterSelfType(self, ctx:ScalaParser.SelfTypeContext):
        pass

    # Exit a parse tree produced by ScalaParser#selfType.
    def exitSelfType(self, ctx:ScalaParser.SelfTypeContext):
        pass


    # Enter a parse tree produced by ScalaParser#import_.
    def enterImport_(self, ctx:ScalaParser.Import_Context):
        pass

    # Exit a parse tree produced by ScalaParser#import_.
    def exitImport_(self, ctx:ScalaParser.Import_Context):
        pass


    # Enter a parse tree produced by ScalaParser#importExpr.
    def enterImportExpr(self, ctx:ScalaParser.ImportExprContext):
        pass

    # Exit a parse tree produced by ScalaParser#importExpr.
    def exitImportExpr(self, ctx:ScalaParser.ImportExprContext):
        pass


    # Enter a parse tree produced by ScalaParser#importSelectors.
    def enterImportSelectors(self, ctx:ScalaParser.ImportSelectorsContext):
        pass

    # Exit a parse tree produced by ScalaParser#importSelectors.
    def exitImportSelectors(self, ctx:ScalaParser.ImportSelectorsContext):
        pass


    # Enter a parse tree produced by ScalaParser#importSelector.
    def enterImportSelector(self, ctx:ScalaParser.ImportSelectorContext):
        pass

    # Exit a parse tree produced by ScalaParser#importSelector.
    def exitImportSelector(self, ctx:ScalaParser.ImportSelectorContext):
        pass


    # Enter a parse tree produced by ScalaParser#dcl.
    def enterDcl(self, ctx:ScalaParser.DclContext):
        pass

    # Exit a parse tree produced by ScalaParser#dcl.
    def exitDcl(self, ctx:ScalaParser.DclContext):
        pass


    # Enter a parse tree produced by ScalaParser#valDcl.
    def enterValDcl(self, ctx:ScalaParser.ValDclContext):
        pass

    # Exit a parse tree produced by ScalaParser#valDcl.
    def exitValDcl(self, ctx:ScalaParser.ValDclContext):
        pass


    # Enter a parse tree produced by ScalaParser#varDcl.
    def enterVarDcl(self, ctx:ScalaParser.VarDclContext):
        pass

    # Exit a parse tree produced by ScalaParser#varDcl.
    def exitVarDcl(self, ctx:ScalaParser.VarDclContext):
        pass


    # Enter a parse tree produced by ScalaParser#funDcl.
    def enterFunDcl(self, ctx:ScalaParser.FunDclContext):
        pass

    # Exit a parse tree produced by ScalaParser#funDcl.
    def exitFunDcl(self, ctx:ScalaParser.FunDclContext):
        pass


    # Enter a parse tree produced by ScalaParser#funSig.
    def enterFunSig(self, ctx:ScalaParser.FunSigContext):
        pass

    # Exit a parse tree produced by ScalaParser#funSig.
    def exitFunSig(self, ctx:ScalaParser.FunSigContext):
        pass


    # Enter a parse tree produced by ScalaParser#typeDcl.
    def enterTypeDcl(self, ctx:ScalaParser.TypeDclContext):
        pass

    # Exit a parse tree produced by ScalaParser#typeDcl.
    def exitTypeDcl(self, ctx:ScalaParser.TypeDclContext):
        pass


    # Enter a parse tree produced by ScalaParser#patVarDef.
    def enterPatVarDef(self, ctx:ScalaParser.PatVarDefContext):
        pass

    # Exit a parse tree produced by ScalaParser#patVarDef.
    def exitPatVarDef(self, ctx:ScalaParser.PatVarDefContext):
        pass


    # Enter a parse tree produced by ScalaParser#def_.
    def enterDef_(self, ctx:ScalaParser.Def_Context):
        pass

    # Exit a parse tree produced by ScalaParser#def_.
    def exitDef_(self, ctx:ScalaParser.Def_Context):
        pass


    # Enter a parse tree produced by ScalaParser#patDef.
    def enterPatDef(self, ctx:ScalaParser.PatDefContext):
        pass

    # Exit a parse tree produced by ScalaParser#patDef.
    def exitPatDef(self, ctx:ScalaParser.PatDefContext):
        pass


    # Enter a parse tree produced by ScalaParser#varDef.
    def enterVarDef(self, ctx:ScalaParser.VarDefContext):
        pass

    # Exit a parse tree produced by ScalaParser#varDef.
    def exitVarDef(self, ctx:ScalaParser.VarDefContext):
        pass


    # Enter a parse tree produced by ScalaParser#funDef.
    def enterFunDef(self, ctx:ScalaParser.FunDefContext):
        pass

    # Exit a parse tree produced by ScalaParser#funDef.
    def exitFunDef(self, ctx:ScalaParser.FunDefContext):
        pass


    # Enter a parse tree produced by ScalaParser#typeDef.
    def enterTypeDef(self, ctx:ScalaParser.TypeDefContext):
        pass

    # Exit a parse tree produced by ScalaParser#typeDef.
    def exitTypeDef(self, ctx:ScalaParser.TypeDefContext):
        pass


    # Enter a parse tree produced by ScalaParser#tmplDef.
    def enterTmplDef(self, ctx:ScalaParser.TmplDefContext):
        pass

    # Exit a parse tree produced by ScalaParser#tmplDef.
    def exitTmplDef(self, ctx:ScalaParser.TmplDefContext):
        pass


    # Enter a parse tree produced by ScalaParser#classDef.
    def enterClassDef(self, ctx:ScalaParser.ClassDefContext):
        pass

    # Exit a parse tree produced by ScalaParser#classDef.
    def exitClassDef(self, ctx:ScalaParser.ClassDefContext):
        pass


    # Enter a parse tree produced by ScalaParser#traitDef.
    def enterTraitDef(self, ctx:ScalaParser.TraitDefContext):
        pass

    # Exit a parse tree produced by ScalaParser#traitDef.
    def exitTraitDef(self, ctx:ScalaParser.TraitDefContext):
        pass


    # Enter a parse tree produced by ScalaParser#objectDef.
    def enterObjectDef(self, ctx:ScalaParser.ObjectDefContext):
        pass

    # Exit a parse tree produced by ScalaParser#objectDef.
    def exitObjectDef(self, ctx:ScalaParser.ObjectDefContext):
        pass


    # Enter a parse tree produced by ScalaParser#classTemplateOpt.
    def enterClassTemplateOpt(self, ctx:ScalaParser.ClassTemplateOptContext):
        pass

    # Exit a parse tree produced by ScalaParser#classTemplateOpt.
    def exitClassTemplateOpt(self, ctx:ScalaParser.ClassTemplateOptContext):
        pass


    # Enter a parse tree produced by ScalaParser#traitTemplateOpt.
    def enterTraitTemplateOpt(self, ctx:ScalaParser.TraitTemplateOptContext):
        pass

    # Exit a parse tree produced by ScalaParser#traitTemplateOpt.
    def exitTraitTemplateOpt(self, ctx:ScalaParser.TraitTemplateOptContext):
        pass


    # Enter a parse tree produced by ScalaParser#classTemplate.
    def enterClassTemplate(self, ctx:ScalaParser.ClassTemplateContext):
        pass

    # Exit a parse tree produced by ScalaParser#classTemplate.
    def exitClassTemplate(self, ctx:ScalaParser.ClassTemplateContext):
        pass


    # Enter a parse tree produced by ScalaParser#traitTemplate.
    def enterTraitTemplate(self, ctx:ScalaParser.TraitTemplateContext):
        pass

    # Exit a parse tree produced by ScalaParser#traitTemplate.
    def exitTraitTemplate(self, ctx:ScalaParser.TraitTemplateContext):
        pass


    # Enter a parse tree produced by ScalaParser#classParents.
    def enterClassParents(self, ctx:ScalaParser.ClassParentsContext):
        pass

    # Exit a parse tree produced by ScalaParser#classParents.
    def exitClassParents(self, ctx:ScalaParser.ClassParentsContext):
        pass


    # Enter a parse tree produced by ScalaParser#traitParents.
    def enterTraitParents(self, ctx:ScalaParser.TraitParentsContext):
        pass

    # Exit a parse tree produced by ScalaParser#traitParents.
    def exitTraitParents(self, ctx:ScalaParser.TraitParentsContext):
        pass


    # Enter a parse tree produced by ScalaParser#constr.
    def enterConstr(self, ctx:ScalaParser.ConstrContext):
        pass

    # Exit a parse tree produced by ScalaParser#constr.
    def exitConstr(self, ctx:ScalaParser.ConstrContext):
        pass


    # Enter a parse tree produced by ScalaParser#earlyDefs.
    def enterEarlyDefs(self, ctx:ScalaParser.EarlyDefsContext):
        pass

    # Exit a parse tree produced by ScalaParser#earlyDefs.
    def exitEarlyDefs(self, ctx:ScalaParser.EarlyDefsContext):
        pass


    # Enter a parse tree produced by ScalaParser#earlyDef.
    def enterEarlyDef(self, ctx:ScalaParser.EarlyDefContext):
        pass

    # Exit a parse tree produced by ScalaParser#earlyDef.
    def exitEarlyDef(self, ctx:ScalaParser.EarlyDefContext):
        pass


    # Enter a parse tree produced by ScalaParser#constrExpr.
    def enterConstrExpr(self, ctx:ScalaParser.ConstrExprContext):
        pass

    # Exit a parse tree produced by ScalaParser#constrExpr.
    def exitConstrExpr(self, ctx:ScalaParser.ConstrExprContext):
        pass


    # Enter a parse tree produced by ScalaParser#constrBlock.
    def enterConstrBlock(self, ctx:ScalaParser.ConstrBlockContext):
        pass

    # Exit a parse tree produced by ScalaParser#constrBlock.
    def exitConstrBlock(self, ctx:ScalaParser.ConstrBlockContext):
        pass


    # Enter a parse tree produced by ScalaParser#selfInvocation.
    def enterSelfInvocation(self, ctx:ScalaParser.SelfInvocationContext):
        pass

    # Exit a parse tree produced by ScalaParser#selfInvocation.
    def exitSelfInvocation(self, ctx:ScalaParser.SelfInvocationContext):
        pass


    # Enter a parse tree produced by ScalaParser#topStatSeq.
    def enterTopStatSeq(self, ctx:ScalaParser.TopStatSeqContext):
        pass

    # Exit a parse tree produced by ScalaParser#topStatSeq.
    def exitTopStatSeq(self, ctx:ScalaParser.TopStatSeqContext):
        pass


    # Enter a parse tree produced by ScalaParser#topStat.
    def enterTopStat(self, ctx:ScalaParser.TopStatContext):
        pass

    # Exit a parse tree produced by ScalaParser#topStat.
    def exitTopStat(self, ctx:ScalaParser.TopStatContext):
        pass


    # Enter a parse tree produced by ScalaParser#packaging.
    def enterPackaging(self, ctx:ScalaParser.PackagingContext):
        pass

    # Exit a parse tree produced by ScalaParser#packaging.
    def exitPackaging(self, ctx:ScalaParser.PackagingContext):
        pass


    # Enter a parse tree produced by ScalaParser#packageObject.
    def enterPackageObject(self, ctx:ScalaParser.PackageObjectContext):
        pass

    # Exit a parse tree produced by ScalaParser#packageObject.
    def exitPackageObject(self, ctx:ScalaParser.PackageObjectContext):
        pass


    # Enter a parse tree produced by ScalaParser#compilationUnit.
    def enterCompilationUnit(self, ctx:ScalaParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by ScalaParser#compilationUnit.
    def exitCompilationUnit(self, ctx:ScalaParser.CompilationUnitContext):
        pass



del ScalaParser