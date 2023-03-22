from antlr4 import IllegalStateException
from typing import Optional, Sequence
from dovado_rtl.parsers.scala.generated.ScalaVisitor import (
    ScalaVisitor as GeneratedScalaVisitor,
)
from dovado_rtl.parsers.scala.generated.ScalaParser import ScalaParser
from dovado_rtl.parsers.utilities.antlr.antlr_module import AntlrModule
from dovado_rtl.parsers.utilities.antlr.antlr_parameter import AntlrParameter


class ScalaVisitor(GeneratedScalaVisitor):
    def visitCompilationUnit(
        self, ctx: ScalaParser.CompilationUnitContext
    ) -> Sequence[AntlrModule]:
        # package declarations are ignored
        top_stat_seq = ctx.topStatSeq()

        if top_stat_seq:
            return self.visitTopStatSeq(top_stat_seq)
        raise IllegalStateException("TopStatSeq is mandatory in compilation unit")

    def visitTopStatSeq(self, ctx: ScalaParser.TopStatSeqContext) -> list[AntlrModule]:
        top_stats = ctx.topStat()

        if top_stats:
            return list(
                filter(
                    lambda x: x is not None,
                    [self.visitTopStat(top_stat) for top_stat in top_stats],
                )
            )
        return []

    def visitTopStat(self, ctx: ScalaParser.TopStatContext) -> Optional[AntlrModule]:
        # only template definitions are taken into account

        tmpl_def = ctx.tmplDef()

        if tmpl_def:
            return self.visitTmplDef(tmpl_def)
        return None

    def visitTmplDef(self, ctx: ScalaParser.TmplDefContext) -> Optional[AntlrModule]:
        # Objects and traits have no parameters so we ignore them
        class_def = ctx.classDef()

        if class_def:
            return self.visitClassDef(class_def)
        return None

    def visitObjectDef(self, ctx: ScalaParser.ObjectDefContext):
        return super().visitObjectDef(ctx)

    def visitClassDef(self, ctx: ScalaParser.ClassDefContext) -> AntlrModule:
        # eventual generic type is ignored
        # constraints are ignored
        # access modifier is ignored

        parsed_id: str
        parameters: list[AntlrParameter]

        id = ctx.Id()
        class_param_clauses = ctx.classParamClauses()

        if id:
            parsed_id = id.getText()  # type: ignore

            if class_param_clauses:
                parameters = self.visitClassParamClauses(class_param_clauses)

                return AntlrModule(name=parsed_id, parameters=parameters)
            else:
                raise IllegalStateException(
                    "Class parameter clauses is mandatory in class definition"
                )

        else:
            raise IllegalStateException("Id is mandatory in class definition")

    def visitClassParamClauses(
        self, ctx: ScalaParser.ClassParamClausesContext
    ) -> list[AntlrParameter]:
        # implicit parameters are ignored
        # this grammar is not scala 3 compatible, does not support "given"
        parameters: list[AntlrParameter]

        class_param_clauses = ctx.classParamClause()

        parameters = []
        if class_param_clauses:
            for class_param_clause in class_param_clauses:
                parameters += self.visitClassParamClause(class_param_clause)
        return parameters

    def visitClassParamClause(
        self, ctx: ScalaParser.ClassParamClauseContext
    ) -> list[AntlrParameter]:
        class_params = ctx.classParams()

        if class_params:
            return self.visitClassParams(class_params)
        return []

    def visitClassParams(
        self, ctx: ScalaParser.ClassParamsContext
    ) -> list[AntlrParameter]:
        class_params = ctx.classParam()

        if class_params:
            return [self.visitClassParam(class_param) for class_param in class_params]
        return []

    def visitClassParam(self, ctx: ScalaParser.ClassParamContext) -> AntlrParameter:
        parsed_id: str

        id = ctx.Id()
        expr = ctx.expr()
        param_type = ctx.paramType()
        if id:
            parsed_id = id.getText()  # type:ignore
            if expr:
                return AntlrParameter(
                    name=parsed_id, value=expr.getText(), rule=expr, has_default=True
                )
            if param_type:
                return AntlrParameter(
                    name=parsed_id, value="", rule=param_type, has_default=False
                )
            else:
                raise IllegalStateException("Found parameter with None type")
        else:
            raise IllegalStateException("Found parameter with None Id")
