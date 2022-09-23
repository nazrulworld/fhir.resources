# _*_ coding: utf-8 _*_
from antlr4 import *
from antlr4.tree.Tree import ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from .fhirpath_grammar.FHIRPathExpressionLexer import FHIRPathExpressionLexer
from .fhirpath_grammar.FHIRPathExpressionParser import FHIRPathExpressionParser
from .listeners import FHIRPathExpressionTreeListener
from .node import ExpressionNode

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


def reraise(e):
    raise e


def compile_fhirpath_expression(expression: str) -> ExpressionNode:
    """https://github.com/antlr/antlr4/blob/master/doc/python-target.md"""
    text_stream = InputStream(expression)
    tree_listener = FHIRPathExpressionTreeListener()
    error_listener = ErrorListener()

    lexer = FHIRPathExpressionLexer(text_stream)
    lexer.recover = reraise
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    parser = FHIRPathExpressionParser(CommonTokenStream(lexer))
    parser.buildParseTrees = True
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    walker = ParseTreeWalker()
    walker.walk(tree_listener, parser.expression())
    return tree_listener.get_node()
