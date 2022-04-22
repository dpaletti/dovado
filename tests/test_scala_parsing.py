from dovado_rtl.antlr.generated.Scala.ScalaParser import ScalaParser
from dovado_rtl.antlr.generated.Scala.ScalaLexer import ScalaLexer
from dovado_rtl.antlr.scala_decl_visitor import ScalaDeclVisitor
from antlr4 import CommonTokenStream, FileStream

def test():
    input_stream = FileStream("resources/example.scala")
    lexer = ScalaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ScalaParser(token_stream)
    visitor = ScalaDeclVisitor("example.scala", token_stream)
    tree = parser.compilationUnit()
    visitor.visit(tree)
    print(visitor.scala_file)
