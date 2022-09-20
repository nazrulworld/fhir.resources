# _*_ coding: utf-8 _*_
from .fhirpath import FHIRPathExpressionListener as BaseListener
from antlr4.tree.Tree import TerminalNodeImpl
__author__ = ""
import pytest
class FHIRPathExpressionListener(BaseListener):
    """ """
    def __init__(self):
        self.parentStack = [{}]

    def pushNode(self, nodeType, ctx):
        parentNode = self.parentStack[-1]
        node = {"type": nodeType, "text": ctx.getText(), "terminalNodeText": []}

        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                node["terminalNodeText"].append(child.getText())

        if not "children" in parentNode:
            parentNode["children"] = []

        parentNode["children"].append(node)

        self.parentStack.append(node)

    def popNode(self):
        if len(self.parentStack) > 0:
            self.parentStack.pop()

    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)

        if name in FHIRPathExpressionListener.__dict__ and hasattr(attr, "__call__"):
            def newfunc(*args, **kwargs):
                if name.startswith("enter"):
                    self.pushNode(name[5:], args[0])

                if name.startswith("exit"):
                    self.popNode()

                return attr(*args, **kwargs)

            return newfunc
        return attr
