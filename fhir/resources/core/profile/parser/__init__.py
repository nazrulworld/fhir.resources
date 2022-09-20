# _*_ coding: utf-8 _*_
from antlr4 import *
from antlr4.tree.Tree import ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from .fhirpath.FHIRPathExpressionLexer import FHIRPathExpressionLexer
from .fhirpath.FHIRPathExpressionParser import FHIRPathExpressionParser
from .listener import FHIRPathExpressionListener

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


def recover(e):
    raise e


def compile_fhirpath_expression(expression: str):
    """https://github.com/antlr/antlr4/blob/master/doc/python-target.md"""
    textStream = InputStream(expression)

    listener = FHIRPathExpressionListener()
    errorListener = ErrorListener()

    lexer = FHIRPathExpressionLexer(textStream)
    lexer.recover = recover
    lexer.removeErrorListeners()
    lexer.addErrorListener(errorListener)

    parser = FHIRPathExpressionParser(CommonTokenStream(lexer))
    parser.buildParseTrees = True
    parser.removeErrorListeners()
    parser.addErrorListener(errorListener)

    walker = ParseTreeWalker()
    walker.walk(listener, parser.expression())
    return listener
