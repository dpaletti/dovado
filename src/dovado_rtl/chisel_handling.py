import json
from pathlib import Path

import pexpect
from antlr4 import FileStream, CommonTokenStream

from dovado_rtl.antlr.generated.Scala.ScalaLexer import ScalaLexer
from dovado_rtl.antlr.generated.Scala.ScalaParser import ScalaParser
from dovado_rtl.antlr.scala_decl_visitor import ScalaDeclVisitor
from dovado_rtl.antlr.scala_representation import ScalaParameter


def source_compilation_script(script_path: str):
    bash = pexpect.spawnu(
        "bash",
        encoding="utf-8",
        codec_errors="ignore",
    )
    bash.sendline("source " + script_path)
    bash.expect("%Compilation End%", timeout=None)

    print("\n-----------------COMPILATION OUTPUT------------------")
    print(bash.before)
    print("-----------------------------------------------------")


def set_parameters(json_path: str):
    input_json = json.load(Path(json_path).open())
    for f in input_json["files"]:
        input_stream = FileStream(f["path"])
        lexer = ScalaLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ScalaParser(token_stream)
        visitor = ScalaDeclVisitor(f["path"], token_stream)
        tree = parser.compilationUnit()
        visitor.visit(tree)
        scala_file = visitor.scala_file
        for cls in f["classes"]:
            scala_object = scala_file.getObject(cls["name"])
            for parameter in cls["parameters"]:
                scala_parameter = scala_object.getParameter(parameter["name"])
                __set_parameter_value(
                    scala_parameter, parameter["value"], scala_file.path
                )


def __set_parameter_value(
    parameter: ScalaParameter, new_value: str, file_path: str
):
    read_file = open(file_path, "r")
    lines = read_file.readlines()

    line_to_modify = lines[parameter.expr_start.line - 1]
    prefix = line_to_modify[0 : parameter.expr_start.column]
    postfix = line_to_modify[parameter.expr_end.column + 1 :]
    new_line = prefix + new_value + postfix
    lines[parameter.expr_start.line - 1] = new_line

    write_file = open(file_path, "w")
    write_file.writelines(lines)
    write_file.close()
