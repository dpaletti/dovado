from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.tree.Tree import TerminalNode
from antlr4.Token import Token
from dovado_rtl.parsers.scala.generated.ScalaVisitor import ScalaVisitor
from dovado_rtl.parsers.scala.generated.ScalaParser import ScalaParser
from typing import List, Tuple, Optional, Union
from dovado_rtl.parsers.scala.scala_representation import (
    ClassSpecification,
    Position,
    ScalaFile,
    ScalaObject,
    ScalaParameter,
)


class ScalaDeclVisitor(ScalaVisitor):
    def __init__(self, file_path: str, token_stream: CommonTokenStream) -> None:
        self.scala_file: ScalaFile = ScalaFile(file_path)
        self.token_stream: CommonTokenStream = token_stream

    def visitCompilationUnit(self, ctx: ScalaParser.CompilationUnitContext) -> None:
        top_stat_seq: Optional[ScalaParser.TopStatSeqContext] = ctx.topStatSeq()
        if top_stat_seq is None:
            raise Exception(
                "A compilation unit must have exacly on sequence of top statements"
            )
        self.visitTopStatSeq(top_stat_seq)

    def visitTopStatSeq(self, ctx: ScalaParser.TopStatSeqContext):
        top_stat: Optional[List[ScalaParser.TopStatContext]] = ctx.topStat()

        if not top_stat:
            raise Exception("A top statement sequence must hold at least one statement")
        for statement in top_stat:
            self.visitTopStat(statement)

    def visitTopStat(self, ctx: ScalaParser.TopStatContext):
        tmpl_def: Optional[ScalaParser.TmplDefContext] = ctx.tmplDef()
        packaging: Optional[ScalaParser.PackagingContext] = ctx.packaging()
        package_object: Optional[ScalaParser.PackageObjectContext] = ctx.packageObject()
        import_: Optional[ScalaParser.Import_Context] = ctx.import_()
        if tmpl_def is not None:
            self.visitTmplDef(tmpl_def)
        elif packaging is not None:
            self.visitPackaging(packaging)
        elif package_object is not None:
            self.visitPackageObject(package_object)
        elif import_ is not None:
            # imports are ignored
            pass
        else:
            raise Exception(
                "A top statement must be either a template definition, "
                + " a package or a package object"
                + " this is neither"
            )

    def visitPackageObject(self, ctx: ScalaParser.PackageObjectContext):
        object_def: Optional[ScalaParser.ObjectDefContext] = ctx.objectDef()

        if object_def is None:
            raise Exception("Found None object_def in PackageObject")

        self.visitObjectDef(object_def)

    def visitPackaging(self, ctx: ScalaParser.PackagingContext):
        top_stat_seq: Optional[ScalaParser.TopStatSeqContext] = ctx.topStatSeq()

        if top_stat_seq is None:
            raise Exception(
                "When visiting a package there must be a non-empty sequence"
                + " of top statements"
            )
        self.visitTopStatSeq(top_stat_seq)

    def visitTemplateBody(
        self,
        ctx: ScalaParser.TemplateBodyContext,
        class_name: Optional[str] = None,
    ):
        template_stat: Optional[
            List[Optional[ScalaParser.TemplateStatContext]]
        ] = ctx.templateStat()
        if not template_stat or None in template_stat:
            raise Exception("Malformed body in template body")
        for template in template_stat:
            self.visitTemplateStat(template, class_name)

    def visitTemplateStat(
        self,
        ctx: ScalaParser.TemplateStatContext,
        class_name: Optional[str] = None,
    ):
        # We are not parsing dcl (pure label declarations) but only def_ which include the value

        def_: Optional[ScalaParser.Def_Context] = ctx.def_()
        dcl: Optional[ScalaParser.DclContext] = ctx.dcl()

        if dcl is not None:
            print("\n")
            print("Skipping pure label declaration: " + dcl.getText())
            print("Assign a value to make it modifiable")
            print("\n")

        if def_ is not None:
            self.visitDef_(def_, class_name)

    def visitDef_(self, ctx: ScalaParser.Def_Context, class_name: Optional[str] = None):
        # considering only parameter declarations var/val/def
        fun_def: Optional[ScalaParser.FunDefContext] = ctx.funDef()
        pat_var_def: Optional[ScalaParser.PatVarDefContext] = ctx.patVarDef()
        tmpl_def: Optional[ScalaParser.TmplDefContext] = ctx.tmplDef()
        if pat_var_def is not None:
            self.visitPatVarDef(pat_var_def, class_name)
        if fun_def is not None:
            self.visitFunDef(fun_def, class_name)
        if tmpl_def is not None:
            self.visitTmplDef(tmpl_def)

    def visitFunDef(
        self, ctx: ScalaParser.FunDefContext, class_name: Optional[str] = None
    ):

        expr: Optional[ScalaParser.ExprContext] = ctx.expr()
        fun_sig: Optional[ScalaParser.FunSigContext] = ctx.funSig()

        if class_name is None:
            raise Exception("None class name found in visitFunDef")
        if expr is not None:
            # we only evaluate "def" parameters definition
            # we skip function definitions

            if fun_sig is None:
                raise Exception("Malformed function signature in visitFunDef")

            self.visitFunSig(fun_sig, class_name, expr)

    def visitFunSig(
        self,
        ctx: ScalaParser.FunSigContext,
        class_name: Optional[str] = None,
        expr: Optional[ScalaParser.ExprContext] = None,
    ):
        _id: Optional[TerminalNode] = ctx.Id()

        if class_name is None:
            raise Exception("None class_name in visitFunSig")
        if expr is None:
            raise Exception("None epxr in visitFunSig")
        self.add_parameter(class_name, self.get_safe_id(_id)[0], expr)

    def visitTmplDef(self, ctx: ScalaParser.TmplDefContext):
        class_def: Optional[ScalaParser.ClassDefContext] = ctx.classDef()
        object_def: Optional[ScalaParser.ObjectDefContext] = ctx.objectDef()
        trait_def: Optional[ScalaParser.TraitDefContext] = ctx.traitDef()

        if class_def is not None:
            self.visitClassDef(class_def)  # normal OO class
        elif object_def is not None:
            self.visitObjectDef(object_def)  # singleton
        elif trait_def is not None:
            self.visitTraitDef(trait_def)  # interface
        else:
            raise Exception(
                "Template definition must have"
                + " either a class, an object or a trait inside"
                + " this has neither"
            )

    def visitTraitDef(self, ctx: ScalaParser.TraitDefContext):
        trait_template_opt: Optional[
            ScalaParser.TraitTemplateOptContext
        ] = ctx.traitTemplateOpt()

        class_name: str
        class_name, _ = self.get_safe_id(ctx.Id())
        scala_object = ScalaObject(
            class_spec=ClassSpecification.TRAIT,
            name=class_name,
        )
        self.scala_file.addObject(scala_object)
        if trait_template_opt is None:
            raise Exception("Did not find a trait template token in: " + class_name)
        self.visitTraitTemplateOpt(trait_template_opt, class_name)

    def visitTraitTemplateOpt(
        self,
        ctx: ScalaParser.TraitTemplateOptContext,
        class_name: Optional[str] = None,
    ):
        trait_template: Optional[ScalaParser.TraitTemplateContext] = ctx.traitTemplate()
        template_body: Optional[ScalaParser.TemplateBodyContext] = ctx.templateBody()
        if class_name is None:
            raise Exception("Please pass a class name to visitTraitTemplateOpt")

        if trait_template is not None:
            self.visitTraitTemplate(trait_template, class_name)
        if template_body is not None:
            self.visitTemplateBody(template_body, class_name)

    def visitTraitTemplate(
        self,
        ctx: ScalaParser.TraitTemplateContext,
        class_name: Optional[str] = None,
    ):
        trait_parents: Optional[ScalaParser.TraitParentsContext] = ctx.traitParents()
        early_defs: Optional[ScalaParser.EarlyDefsContext] = ctx.earlyDefs()
        template_body: Optional[ScalaParser.TemplateBodyContext] = ctx.templateBody()
        if class_name is None:
            raise Exception("Please pass a class name to visitTraitTemplate")

        if trait_parents is None:
            raise Exception("None trait_parents found in visitTraitTemplate")

        # This path is useless
        # trait_parents: Optional[
        #     ScalaParser.TraitParentsContext
        # self.visitTraitParents(ctx.traitParents(), class_name)

        if early_defs is not None:
            self.visitEarlyDefs(early_defs, class_name)
        if template_body is not None:
            self.visitTemplateBody(template_body, class_name)

    def visitTraitParents(
        self,
        ctx: ScalaParser.TraitParentsContext,
        class_name: Optional[str] = None,
    ):
        annot_type: Optional[List[ScalaParser.AnnotTypeContext]] = ctx.annotType()

        if not annot_type:
            raise Exception("None annot_type found in visitTraitParents")

        for annot in annot_type:
            self.visitAnnotType(annot, class_name)

    def visitClassTemplateOpt(
        self,
        ctx: ScalaParser.ClassTemplateOptContext,
        class_name: Optional[str] = None,
    ):
        class_template: Optional[ScalaParser.ClassTemplateContext] = ctx.classTemplate()
        template_body: Optional[ScalaParser.TemplateBodyContext] = ctx.templateBody()

        if class_name is None:
            raise Exception("Please pass a class name to visitClassTemplateOpt")

        if class_template is not None:
            self.visitClassTemplate(class_template, class_name)
        if template_body is not None:
            self.visitTemplateBody(template_body, class_name)

    def visitClassTemplate(
        self,
        ctx: ScalaParser.ClassTemplateContext,
        class_name: Optional[str] = None,
    ):
        early_defs: Optional[ScalaParser.EarlyDefsContext] = ctx.earlyDefs()
        template_body: Optional[ScalaParser.TemplateBodyContext] = ctx.templateBody()

        if class_name is None:
            raise Exception("Please pass a class name to visitClassTemplate")
        # This Path is useless
        # class_parents: Optional[
        #     ScalaParser.ClassParentsContext
        # ] = ctx.classParents()
        # if class_parents is None:
        #    raise Exception("None classParents found in: " + class_name)
        # self.visitClassParents(class_parents, class_name)

        if early_defs is not None:
            self.visitEarlyDefs(early_defs, class_name)

        if template_body is not None:
            self.visitTemplateBody(template_body, class_name)

    def visitClassParents(
        self,
        ctx: ScalaParser.ClassParentsContext,
        class_name: Optional[str] = None,
    ):

        # Ignoring constr because it does not hold significant information
        annot_type: Optional[List[ScalaParser.AnnotTypeContext]] = ctx.annotType()

        if class_name is None:
            raise Exception("Found none class name in visitClassParents")

        if annot_type:
            for annot in annot_type:
                self.visitAnnotType(annot, class_name)

    def visitAnnotType(
        self, ctx: ScalaParser.AnnotTypeContext, class_name: Optional = None
    ):
        # Ignoring annotations
        simple_type: Optional[ScalaParser.SimpleTypeContext] = ctx.simpleType()

        if class_name is None:
            raise Exception("None class name in visitAnnotType")

        if simple_type is None:
            raise Exception("None simpleType found in AnnotType")

        self.visitSimpleType(simple_type, class_name)

    def visitSimpleType(
        self,
        ctx: ScalaParser.SimpleTypeContext,
        class_name: Optional[str] = None,
    ):
        type_args: Optional[ScalaParser.TypeArgsContext] = ctx.typeArgs()
        types: Optional[ScalaParser.TypesContext] = ctx.types()

        if class_name is None:
            raise Exception("None class_name in visitSimpleType")

        if type_args is not None:
            self.visitTypeArgs(type_args, class_name)
        if types is not None:
            self.visitTypes(types, class_name)

    def visitTypeArgs(
        self,
        ctx: ScalaParser.TypeArgsContext,
        class_name: Optional[str] = None,
    ):
        types: Optional[ScalaParser.TypesContext] = ctx.types()

        if types is None:
            raise Exception("None types found in visitTypeArgs")
        self.visitTypes(types, class_name)

    def visitTypes(
        self, ctx: ScalaParser.TypesContext, class_name: Optional[str] = None
    ):
        type_: Optional[List[ScalaParser.Type_Context]] = ctx.type_()

        if class_name is None:
            raise Exception("None class_name found in visitTypes")

        if type_:
            for type in type_:
                self.visitType_(type, class_name)

    def visitType_(
        self, ctx: ScalaParser.Type_Context, class_name: Optional[str] = None
    ):
        # exploring only infixType
        infix_type: Optional[ScalaParser.InfixTypeContext] = ctx.infixType()

        if class_name is None:
            raise Exception("None class_name found in visitType_")

        if infix_type is not None:
            self.visitInfixType(infix_type, class_name)

    def visitInfixType(
        self,
        ctx: ScalaParser.InfixTypeContext,
        class_name: Optional[str] = None,
    ):
        compound_types: Optional[
            List[ScalaParser.CompoundTypeContext]
        ] = ctx.compoundType()

        if class_name is None:
            raise Exception("None class_name found in visitInfixType")

        if compound_types:
            for compound_type in compound_types:
                self.visitCompoundType(compound_type, class_name)

    def visitCompoundType(
        self,
        ctx: ScalaParser.CompoundTypeContext,
        class_name: Optional[str] = None,
    ):
        refinement: Optional[ScalaParser.RefinementContext] = ctx.refinement()

        if class_name is None:
            raise Exception("None class_name found in visitCompoundType")

        if refinement:
            self.visitRefinement(refinement, class_name)

    def visitRefinement(
        self,
        ctx: ScalaParser.RefinementContext,
        class_name: Optional[str] = None,
    ):
        refine_stats: Optional[List[ScalaParser.RefineStatContext]] = ctx.refineStat()

        if class_name is None:
            raise Exception("None class_name found in visitRefinement")
        if refine_stats:
            for refine_stat in refine_stats:
                self.visitRefineStat(refine_stat, class_name)

    def visitRefineStat(
        self,
        ctx: ScalaParser.RefineStatContext,
        class_name: Optional[str] = None,
    ):

        dcl: Optional[ScalaParser.DclContext] = ctx.dcl()

        if class_name is None:
            raise Exception("None class_name found in visitRefineStat")

        if dcl is not None:
            self.visitDcl(dcl, class_name)

    def visitDcl(self, ctx: ScalaParser.DclContext, class_name: Optional[str] = None):
        # ignoring type declarations
        # CARE: this path is useless

        val_dcl: Optional[ScalaParser.ValDclContext] = ctx.valDcl()
        var_dcL: Optional[ScalaParser.VarDclContext] = ctx.varDcl()
        fun_dcl: Optional[ScalaParser.FunDclContext] = ctx.funDcl()

    def visitEarlyDefs(
        self,
        ctx: ScalaParser.EarlyDefsContext,
        class_name: Optional[str] = None,
    ):
        early_def: Optional[List[ScalaParser.EarlyDefContext]] = ctx.earlyDef()

        if class_name is None:
            raise Exception("Please pass a class name to visitEarlyDefs")

        if not early_def:
            raise Exception("Early defs block must be non-empty")
        for d in early_def:
            self.visitEarlyDef(d, class_name)

    def visitEarlyDef(
        self,
        ctx: ScalaParser.EarlyDefContext,
        class_name: Optional[str] = None,
    ):

        pat_var_def: Optional[ScalaParser.PatVarDefContext] = ctx.patVarDef()

        if class_name is None:
            raise Exception("Please pass a class name to visitEarlyDef")

        if pat_var_def is None:
            raise Exception("Empty early defs are not allowed in " + class_name)

        self.visitPatVarDef(pat_var_def, class_name)

    def visitPatVarDef(
        self,
        ctx: ScalaParser.PatVarDefContext,
        class_name: Optional[str] = None,
    ):
        pat_def: Optional[ScalaParser.PatDefContext] = ctx.patDef()
        var_def: Optional[ScalaParser.VarDefContext] = ctx.varDef()

        if class_name is None:
            raise Exception("Please pass a class name to visitPatVarDef")

        if pat_def is not None:
            self.visitPatDef(pat_def, class_name)
        if var_def is not None:
            self.visitVarDef(var_def, class_name)

    def visitVarDef(
        self, ctx: ScalaParser.VarDefContext, class_name: Optional[str] = None
    ):
        pat_def: Optional[ScalaParser.PatDefContext] = ctx.patDef()
        ids: Optional[ScalaParser.IdsContext] = ctx.ids()

        if class_name is None:
            raise Exception("None class_name in visitVarDef")

        if pat_def is not None:
            self.visitPatDef(pat_def, class_name)

        if ids is not None:
            parsed_ids = self.visitIds(ids)
            for parsed_id in parsed_ids:
                self.add_parameter(class_name, parsed_id, ctx)

    def visitPatDef(
        self, ctx: ScalaParser.PatDefContext, class_name: Optional[str] = None
    ):
        pattern2: Optional[List[Optional[ScalaParser.Pattern2Context]]] = ctx.pattern2()
        expr: Optional[ScalaParser.ExprContext] = ctx.expr()

        if class_name is None:
            raise Exception("None class name in visitPatDef")

        if not pattern2 or None in pattern2:
            raise Exception("Pattern2 list malformed")

        if expr is None:
            raise Exception("None expression found")

        for p in pattern2:
            self.visitPattern2(p, class_name, expr)

    def visitPattern2(
        self,
        ctx: ScalaParser.Pattern2Context,
        class_name: Optional[str] = None,
        expr: Optional[ScalaParser.ExprContext] = None,
    ):
        _id: Optional[TerminalNode] = ctx.Id()
        pattern3: Optional[ScalaParser.Pattern3Context] = ctx.pattern3()

        if class_name is None:
            raise Exception("Please pass class name to visitPattern2")

        if expr is None:
            raise Exception("Please pass expr to visitPattern2")

        # pattern3 may either host an "Id@pattern"
        # or a straight up "pattern"
        if _id is not None:
            self.add_parameter(class_name, self.get_safe_id(_id)[0], expr)
        elif pattern3 is not None:
            self.visitPattern3(pattern3, class_name, expr)

    def visitPattern3(
        self,
        ctx: ScalaParser.Pattern3Context,
        class_name: Optional[str] = None,
        expr: Optional[ScalaParser.ExprContext] = None,
    ):
        # Here we only visit the FIRST simple pattern
        # it is either the case of the declaration
        # or there are other simple patterns which do not hold the ID of the declared variable

        simple_pattern: Optional[
            List[Optional[ScalaParser.SimplePatternContext]]
        ] = ctx.simplePattern()
        if not simple_pattern or None in simple_pattern:
            raise Exception("Malformed simple_pattern list in visitPattern3")
        self.visitSimplePattern(simple_pattern[0], class_name, expr)

    def visitSimplePattern(
        self,
        ctx: ScalaParser.SimplePatternContext,
        class_name: Optional[str] = None,
        expr: Optional[ScalaParser.ExprContext] = None,
    ):
        var_id: Optional[TerminalNode] = ctx.Varid()
        stable_id: Optional[ScalaParser.StableIdContext] = ctx.stableId()
        if class_name is None:
            raise Exception("Found None class_name in visitSimplePattern")
        if expr is None:
            raise Exception("Found None")
        if var_id is not None:
            self.add_parameter(class_name, self.get_safe_id(var_id)[0], expr)
        if stable_id is not None:
            self.visitStableId(stable_id, class_name, expr)

    def visitStableId(
        self,
        ctx: ScalaParser.StableIdContext,
        class_name: Optional[str] = None,
        expr: Optional[ScalaParser.ExprContext] = None,
    ):
        if class_name is None:
            raise Exception("Found None class name in visitStableId")

        if expr is None:
            raise Exception("Found None expr in visitStableId")

        self.add_parameter(class_name, ctx.getText(), expr)

    def visitIds(self, ctx: ScalaParser.IdsContext) -> List[str]:
        _id: Optional[List[Optional[TerminalNode]]] = ctx.Id()
        if not _id or None in _id:
            raise Exception("Id list must be non-empty")
        return [self.get_safe_id(i)[0] for i in _id]

    @staticmethod
    def get_safe_id(unsafe_id: Optional[TerminalNode]) -> Tuple[str, Token]:
        if unsafe_id is None:
            raise Exception("Got a None terminal node when retrieving Id")

        id_token: Optional[Token] = unsafe_id.getSymbol()  # ANTLR typing issue
        if id_token is None:
            raise Exception("Got a None token when retrieving Id")

        safe_id: Optional[str] = id_token.text
        if safe_id is None:
            raise Exception("Got a None parameter name when retrieving Id")
        return safe_id, id_token

    def visitObjectDef(self, ctx: ScalaParser.ObjectDefContext):
        class_template_opt: Optional[
            ScalaParser.ClassTemplateOptContext
        ] = ctx.classTemplateOpt()

        class_name: str
        class_name, _ = self.get_safe_id(ctx.Id())
        scala_object = ScalaObject(
            class_spec=ClassSpecification.OBJECT,
            name=class_name,
        )
        self.scala_file.addObject(scala_object)
        if class_template_opt is None:
            raise Exception("Did not found class template token in " + class_name)
        self.visitClassTemplateOpt(class_template_opt, class_name)

    def visitClassDef(self, ctx: ScalaParser.ClassDefContext):
        # Annotations are ignored
        # eventual "override" accessModifier is ignored
        # eventual "extends" templating is ignored

        class_template_opt: Optional[
            ScalaParser.ClassTemplateOptContext
        ] = ctx.classTemplateOpt()
        if class_template_opt is None:
            raise Exception("Class template token must not be empty")
        class_name: str
        class_name, _ = self.get_safe_id(ctx.Id())
        type_param_clause: Optional[
            ScalaParser.TypeParamClauseContext
        ] = ctx.typeParamClause()
        class_param_clauses: Optional[
            ScalaParser.ClassParamClausesContext
        ] = ctx.classParamClauses()

        scala_object = ScalaObject(
            class_spec=ClassSpecification.CLASS,
            name=class_name,
        )

        self.scala_file.addObject(scala_object)

        if type_param_clause is not None:
            # Ignoring type parameters
            pass

        if class_param_clauses is None:
            raise Exception(
                "Class parameter clauses are mandatory for class definition"
                + " missing in "
                + class_name
            )
        self.visitClassParamClauses(class_param_clauses, class_name)

        if class_template_opt is None:
            raise Exception("Class template token must not be empty in " + class_name)
        self.visitClassTemplateOpt(class_template_opt, class_name)

    def visitClassParamClauses(
        self,
        ctx: ScalaParser.ClassParamClausesContext,
        class_name: Optional[str] = None,
    ):
        # Implicit params are ignored because cannot have default values

        if class_name is None:
            raise Exception("Please pass a class name to visitClassParamClauses")

        class_param_clause: Optional[
            List[ScalaParser.ClassParamClauseContext]
        ] = ctx.classParamClause()
        if class_param_clause is not None:
            for clause in class_param_clause:
                self.visitClassParamClause(clause, class_name)

    def visitClassParamClause(
        self,
        ctx: ScalaParser.ClassParamClauseContext,
        class_name: Optional[str] = None,
    ):
        class_params: Optional[ScalaParser.ClassParamsContext] = ctx.classParams()
        if class_params is not None:
            self.visitClassParams(class_params, class_name)

    def visitClassParams(
        self,
        ctx: ScalaParser.ClassParamsContext,
        class_name: Optional[str] = None,
    ):
        class_param: Optional[List[ScalaParser.ClassParamContext]] = ctx.classParam()
        if not class_param:
            raise Exception("Malformed classParams list")
        for param in class_param:
            self.visitClassParam(param, class_name)

    def add_parameter(
        self,
        class_name: str,
        param_name: str,
        expr: Union[ScalaParser.ExprContext, ScalaParser.VarDefContext],
        is_between_parenthesis: bool = False,
    ):

        param = ScalaParameter(
            name=param_name,
            expr_start=Position(line=expr.start.line, column=expr.start.column),
            expr_end=Position(line=expr.stop.line, column=expr.stop.column),
            value=" ".join(
                [
                    token.text
                    for token in self.token_stream.getTokens(
                        start=expr.start.tokenIndex,
                        stop=expr.stop.tokenIndex + 1,
                    )
                ]
            ),
            is_between_parenthesis=is_between_parenthesis,
        )
        self.scala_file.addParameterToObject(param, class_name)

    def visitClassParam(
        self,
        ctx: ScalaParser.ClassParamContext,
        class_name: Optional[str] = None,
    ):
        expr: Optional[ScalaParser.ExprContext] = ctx.expr()
        param_name: str
        param_name, _ = self.get_safe_id(ctx.Id())
        if expr is None:
            print("Ignoring parameter without a default value: " + param_name)
            return

        if class_name is None:
            raise Exception("Class name is None in visitClassParam")
        self.add_parameter(class_name, param_name, expr, is_between_parenthesis=True)
