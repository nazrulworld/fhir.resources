# _*_ coding: utf-8 _*_
from .fhirpath_grammar.FHIRPathExpressionListener import FHIRPathExpressionListener
from antlr4.tree.Tree import TerminalNodeImpl
from .node import ExpressionNode
from inspect import ismethod
from typing import List, Dict, Any

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


class FHIRPathExpressionTreeListener(FHIRPathExpressionListener):
    """ """

    def __init__(self):
        self.stack: List[Dict[str, Any]] = [{}]

    def enter_node(self, node_type, ctx):
        parent_node = self.stack[-1]
        node = {"node_type": node_type, "text": ctx.getText(), "terminal_node_text": []}
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                node["terminal_node_text"].append(child.getText())

        if "children" not in parent_node:
            parent_node["children"] = []

        parent_node["children"].append(node)

        self.stack.append(node)

    def exit_node(self):
        if len(self.stack) > 0:
            self.stack.pop()

    def get_node(self) -> ExpressionNode:
        """ """
        if len(self.stack[0]) > 0:
            return ExpressionNode(**self.stack[0]["children"][0])

    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if name in FHIRPathExpressionListener.__dict__ and ismethod(attr):
            def func(*args, **kwargs):
                if name.startswith("enter"):
                    self.enter_node(name[5:], args[0])
                if name.startswith("exit"):
                    self.exit_node()
                return attr(*args, **kwargs)
            return func
        return attr
