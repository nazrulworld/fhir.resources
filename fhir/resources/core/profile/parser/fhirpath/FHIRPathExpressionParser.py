# Generated from https://github.com/nazrulworld/fhir-parser/blob/c8e819379db32f15c7b806c769ed9ead3426b5ec/FHIRPathExpression.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,64,150,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,3,0,33,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,73,8,0,10,
        0,12,0,76,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,85,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,96,8,2,1,3,1,3,1,3,3,3,101,8,3,1,4,1,
        4,1,4,1,4,1,4,3,4,108,8,4,1,5,1,5,1,5,3,5,113,8,5,1,5,1,5,1,6,1,
        6,1,6,5,6,120,8,6,10,6,12,6,123,9,6,1,7,1,7,3,7,127,8,7,1,8,1,8,
        1,8,3,8,132,8,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,5,12,
        143,8,12,10,12,12,12,146,9,12,1,13,1,13,1,13,0,1,0,14,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,0,12,1,0,4,5,1,0,6,9,2,0,4,5,10,10,1,
        0,14,17,1,0,18,21,1,0,22,23,1,0,25,26,1,0,11,12,1,0,32,33,1,0,39,
        46,1,0,47,54,3,0,11,12,22,23,58,59,169,0,32,1,0,0,0,2,84,1,0,0,0,
        4,95,1,0,0,0,6,97,1,0,0,0,8,107,1,0,0,0,10,109,1,0,0,0,12,116,1,
        0,0,0,14,124,1,0,0,0,16,131,1,0,0,0,18,133,1,0,0,0,20,135,1,0,0,
        0,22,137,1,0,0,0,24,139,1,0,0,0,26,147,1,0,0,0,28,29,6,0,-1,0,29,
        33,3,2,1,0,30,31,7,0,0,0,31,33,3,0,0,11,32,28,1,0,0,0,32,30,1,0,
        0,0,33,74,1,0,0,0,34,35,10,10,0,0,35,36,7,1,0,0,36,73,3,0,0,11,37,
        38,10,9,0,0,38,39,7,2,0,0,39,73,3,0,0,10,40,41,10,7,0,0,41,42,5,
        13,0,0,42,73,3,0,0,8,43,44,10,6,0,0,44,45,7,3,0,0,45,73,3,0,0,7,
        46,47,10,5,0,0,47,48,7,4,0,0,48,73,3,0,0,6,49,50,10,4,0,0,50,51,
        7,5,0,0,51,73,3,0,0,5,52,53,10,3,0,0,53,54,5,24,0,0,54,73,3,0,0,
        4,55,56,10,2,0,0,56,57,7,6,0,0,57,73,3,0,0,3,58,59,10,1,0,0,59,60,
        5,27,0,0,60,73,3,0,0,2,61,62,10,13,0,0,62,63,5,1,0,0,63,73,3,8,4,
        0,64,65,10,12,0,0,65,66,5,2,0,0,66,67,3,0,0,0,67,68,5,3,0,0,68,73,
        1,0,0,0,69,70,10,8,0,0,70,71,7,7,0,0,71,73,3,22,11,0,72,34,1,0,0,
        0,72,37,1,0,0,0,72,40,1,0,0,0,72,43,1,0,0,0,72,46,1,0,0,0,72,49,
        1,0,0,0,72,52,1,0,0,0,72,55,1,0,0,0,72,58,1,0,0,0,72,61,1,0,0,0,
        72,64,1,0,0,0,72,69,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,
        0,0,0,75,1,1,0,0,0,76,74,1,0,0,0,77,85,3,8,4,0,78,85,3,4,2,0,79,
        85,3,6,3,0,80,81,5,28,0,0,81,82,3,0,0,0,82,83,5,29,0,0,83,85,1,0,
        0,0,84,77,1,0,0,0,84,78,1,0,0,0,84,79,1,0,0,0,84,80,1,0,0,0,85,3,
        1,0,0,0,86,87,5,30,0,0,87,96,5,31,0,0,88,96,7,8,0,0,89,96,5,60,0,
        0,90,96,5,61,0,0,91,96,5,55,0,0,92,96,5,56,0,0,93,96,5,57,0,0,94,
        96,3,14,7,0,95,86,1,0,0,0,95,88,1,0,0,0,95,89,1,0,0,0,95,90,1,0,
        0,0,95,91,1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,5,
        1,0,0,0,97,100,5,34,0,0,98,101,3,26,13,0,99,101,5,60,0,0,100,98,
        1,0,0,0,100,99,1,0,0,0,101,7,1,0,0,0,102,108,3,26,13,0,103,108,3,
        10,5,0,104,108,5,35,0,0,105,108,5,36,0,0,106,108,5,37,0,0,107,102,
        1,0,0,0,107,103,1,0,0,0,107,104,1,0,0,0,107,105,1,0,0,0,107,106,
        1,0,0,0,108,9,1,0,0,0,109,110,3,26,13,0,110,112,5,28,0,0,111,113,
        3,12,6,0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,
        5,29,0,0,115,11,1,0,0,0,116,121,3,0,0,0,117,118,5,38,0,0,118,120,
        3,0,0,0,119,117,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,
        1,0,0,0,122,13,1,0,0,0,123,121,1,0,0,0,124,126,5,61,0,0,125,127,
        3,16,8,0,126,125,1,0,0,0,126,127,1,0,0,0,127,15,1,0,0,0,128,132,
        3,18,9,0,129,132,3,20,10,0,130,132,5,60,0,0,131,128,1,0,0,0,131,
        129,1,0,0,0,131,130,1,0,0,0,132,17,1,0,0,0,133,134,7,9,0,0,134,19,
        1,0,0,0,135,136,7,10,0,0,136,21,1,0,0,0,137,138,3,24,12,0,138,23,
        1,0,0,0,139,144,3,26,13,0,140,141,5,1,0,0,141,143,3,26,13,0,142,
        140,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,
        25,1,0,0,0,146,144,1,0,0,0,147,148,7,11,0,0,148,27,1,0,0,0,12,32,
        72,74,84,95,100,107,112,121,126,131,144
    ]

class FHIRPathExpressionParser ( Parser ):

    grammarFileName = "FHIRPathExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'['", "']'", "'+'", "'-'", "'*'",
                     "'/'", "'div'", "'mod'", "'&'", "'is'", "'as'", "'|'",
                     "'<='", "'<'", "'>'", "'>='", "'='", "'~'", "'!='",
                     "'!~'", "'in'", "'contains'", "'and'", "'or'", "'xor'",
                     "'implies'", "'('", "')'", "'{'", "'}'", "'true'",
                     "'false'", "'%'", "'$this'", "'$index'", "'$total'",
                     "','", "'year'", "'month'", "'week'", "'day'", "'hour'",
                     "'minute'", "'second'", "'millisecond'", "'years'",
                     "'months'", "'weeks'", "'days'", "'hours'", "'minutes'",
                     "'seconds'", "'milliseconds'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "DATE", "DATETIME",
                      "TIME", "IDENTIFIER", "DELIMITEDIDENTIFIER", "STRING",
                      "NUMBER", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_expression = 0
    RULE_term = 1
    RULE_literal = 2
    RULE_externalConstant = 3
    RULE_invocation = 4
    RULE_function = 5
    RULE_paramList = 6
    RULE_quantity = 7
    RULE_unit = 8
    RULE_dateTimePrecision = 9
    RULE_pluralDateTimePrecision = 10
    RULE_typeSpecifier = 11
    RULE_qualifiedIdentifier = 12
    RULE_identifier = 13

    ruleNames =  [ "expression", "term", "literal", "externalConstant",
                   "invocation", "function", "paramList", "quantity", "unit",
                   "dateTimePrecision", "pluralDateTimePrecision", "typeSpecifier",
                   "qualifiedIdentifier", "identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    DATE=55
    DATETIME=56
    TIME=57
    IDENTIFIER=58
    DELIMITEDIDENTIFIER=59
    STRING=60
    NUMBER=61
    WS=62
    COMMENT=63
    LINE_COMMENT=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_expression


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IndexerExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexerExpression" ):
                listener.enterIndexerExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexerExpression" ):
                listener.exitIndexerExpression(self)


    class PolarityExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolarityExpression" ):
                listener.enterPolarityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolarityExpression" ):
                listener.exitPolarityExpression(self)


    class AdditiveExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)


    class MultiplicativeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)


    class UnionExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnionExpression" ):
                listener.enterUnionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnionExpression" ):
                listener.exitUnionExpression(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpression" ):
                listener.enterOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpression" ):
                listener.exitOrExpression(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpression" ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpression" ):
                listener.exitAndExpression(self)


    class MembershipExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMembershipExpression" ):
                listener.enterMembershipExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMembershipExpression" ):
                listener.exitMembershipExpression(self)


    class InequalityExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInequalityExpression" ):
                listener.enterInequalityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInequalityExpression" ):
                listener.exitInequalityExpression(self)


    class InvocationExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,0)

        def invocation(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.InvocationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvocationExpression" ):
                listener.enterInvocationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvocationExpression" ):
                listener.exitInvocationExpression(self)


    class EqualityExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)


    class ImpliesExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpliesExpression" ):
                listener.enterImpliesExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpliesExpression" ):
                listener.exitImpliesExpression(self)


    class TermExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermExpression" ):
                listener.enterTermExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermExpression" ):
                listener.exitTermExpression(self)


    class TypeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.TypeSpecifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeExpression" ):
                listener.enterTypeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeExpression" ):
                listener.exitTypeExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FHIRPathExpressionParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 22, 23, 28, 30, 32, 33, 34, 35, 36, 37, 55, 56, 57, 58, 59, 60, 61]:
                localctx = FHIRPathExpressionParser.TermExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 29
                self.term()
                pass
            elif token in [4, 5]:
                localctx = FHIRPathExpressionParser.PolarityExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 31
                self.expression(11)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 72
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = FHIRPathExpressionParser.MultiplicativeExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 34
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 35
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 36
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = FHIRPathExpressionParser.AdditiveExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 37
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 38
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1072) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = FHIRPathExpressionParser.UnionExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 40
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 41
                        self.match(FHIRPathExpressionParser.T__12)
                        self.state = 42
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = FHIRPathExpressionParser.InequalityExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 43
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 44
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 45
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = FHIRPathExpressionParser.EqualityExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 46
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 47
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        self.expression(6)
                        pass

                    elif la_ == 6:
                        localctx = FHIRPathExpressionParser.MembershipExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 49
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 50
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        self.expression(5)
                        pass

                    elif la_ == 7:
                        localctx = FHIRPathExpressionParser.AndExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 52
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 53
                        self.match(FHIRPathExpressionParser.T__23)
                        self.state = 54
                        self.expression(4)
                        pass

                    elif la_ == 8:
                        localctx = FHIRPathExpressionParser.OrExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 55
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 56
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expression(3)
                        pass

                    elif la_ == 9:
                        localctx = FHIRPathExpressionParser.ImpliesExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 58
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 59
                        self.match(FHIRPathExpressionParser.T__26)
                        self.state = 60
                        self.expression(2)
                        pass

                    elif la_ == 10:
                        localctx = FHIRPathExpressionParser.InvocationExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 61
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 62
                        self.match(FHIRPathExpressionParser.T__0)
                        self.state = 63
                        self.invocation()
                        pass

                    elif la_ == 11:
                        localctx = FHIRPathExpressionParser.IndexerExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 64
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 65
                        self.match(FHIRPathExpressionParser.T__1)
                        self.state = 66
                        self.expression(0)
                        self.state = 67
                        self.match(FHIRPathExpressionParser.T__2)
                        pass

                    elif la_ == 12:
                        localctx = FHIRPathExpressionParser.TypeExpressionContext(self, FHIRPathExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 69
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 70
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        self.typeSpecifier()
                        pass


                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_term


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExternalConstantTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def externalConstant(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.ExternalConstantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExternalConstantTerm" ):
                listener.enterExternalConstantTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExternalConstantTerm" ):
                listener.exitExternalConstantTerm(self)


    class LiteralTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralTerm" ):
                listener.enterLiteralTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralTerm" ):
                listener.exitLiteralTerm(self)


    class ParenthesizedTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedTerm" ):
                listener.enterParenthesizedTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedTerm" ):
                listener.exitParenthesizedTerm(self)


    class InvocationTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def invocation(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.InvocationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvocationTerm" ):
                listener.enterInvocationTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvocationTerm" ):
                listener.exitInvocationTerm(self)



    def term(self):

        localctx = FHIRPathExpressionParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 22, 23, 35, 36, 37, 58, 59]:
                localctx = FHIRPathExpressionParser.InvocationTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.invocation()
                pass
            elif token in [30, 32, 33, 55, 56, 57, 60, 61]:
                localctx = FHIRPathExpressionParser.LiteralTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.literal()
                pass
            elif token in [34]:
                localctx = FHIRPathExpressionParser.ExternalConstantTermContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.externalConstant()
                pass
            elif token in [28]:
                localctx = FHIRPathExpressionParser.ParenthesizedTermContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                self.match(FHIRPathExpressionParser.T__27)
                self.state = 81
                self.expression(0)
                self.state = 82
                self.match(FHIRPathExpressionParser.T__28)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_literal


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TimeLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(FHIRPathExpressionParser.TIME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeLiteral" ):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeLiteral" ):
                listener.exitTimeLiteral(self)


    class NullLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullLiteral" ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullLiteral" ):
                listener.exitNullLiteral(self)


    class DateTimeLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(FHIRPathExpressionParser.DATETIME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDateTimeLiteral" ):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDateTimeLiteral" ):
                listener.exitDateTimeLiteral(self)


    class StringLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(FHIRPathExpressionParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)


    class DateLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(FHIRPathExpressionParser.DATE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDateLiteral" ):
                listener.enterDateLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDateLiteral" ):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanLiteral" ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanLiteral" ):
                listener.exitBooleanLiteral(self)


    class NumberLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(FHIRPathExpressionParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberLiteral" ):
                listener.enterNumberLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberLiteral" ):
                listener.exitNumberLiteral(self)


    class QuantityLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def quantity(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.QuantityContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantityLiteral" ):
                listener.enterQuantityLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantityLiteral" ):
                listener.exitQuantityLiteral(self)



    def literal(self):

        localctx = FHIRPathExpressionParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = FHIRPathExpressionParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(FHIRPathExpressionParser.T__29)
                self.state = 87
                self.match(FHIRPathExpressionParser.T__30)
                pass

            elif la_ == 2:
                localctx = FHIRPathExpressionParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = FHIRPathExpressionParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.match(FHIRPathExpressionParser.STRING)
                pass

            elif la_ == 4:
                localctx = FHIRPathExpressionParser.NumberLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.match(FHIRPathExpressionParser.NUMBER)
                pass

            elif la_ == 5:
                localctx = FHIRPathExpressionParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.match(FHIRPathExpressionParser.DATE)
                pass

            elif la_ == 6:
                localctx = FHIRPathExpressionParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 92
                self.match(FHIRPathExpressionParser.DATETIME)
                pass

            elif la_ == 7:
                localctx = FHIRPathExpressionParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 93
                self.match(FHIRPathExpressionParser.TIME)
                pass

            elif la_ == 8:
                localctx = FHIRPathExpressionParser.QuantityLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 94
                self.quantity()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExternalConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.IdentifierContext,0)


        def STRING(self):
            return self.getToken(FHIRPathExpressionParser.STRING, 0)

        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_externalConstant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExternalConstant" ):
                listener.enterExternalConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExternalConstant" ):
                listener.exitExternalConstant(self)




    def externalConstant(self):

        localctx = FHIRPathExpressionParser.ExternalConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_externalConstant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(FHIRPathExpressionParser.T__33)
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 22, 23, 58, 59]:
                self.state = 98
                self.identifier()
                pass
            elif token in [60]:
                self.state = 99
                self.match(FHIRPathExpressionParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_invocation


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TotalInvocationContext(InvocationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.InvocationContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTotalInvocation" ):
                listener.enterTotalInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTotalInvocation" ):
                listener.exitTotalInvocation(self)


    class ThisInvocationContext(InvocationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.InvocationContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThisInvocation" ):
                listener.enterThisInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThisInvocation" ):
                listener.exitThisInvocation(self)


    class IndexInvocationContext(InvocationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.InvocationContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexInvocation" ):
                listener.enterIndexInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexInvocation" ):
                listener.exitIndexInvocation(self)


    class FunctionInvocationContext(InvocationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.InvocationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.FunctionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionInvocation" ):
                listener.enterFunctionInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionInvocation" ):
                listener.exitFunctionInvocation(self)


    class MemberInvocationContext(InvocationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FHIRPathExpressionParser.InvocationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberInvocation" ):
                listener.enterMemberInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberInvocation" ):
                listener.exitMemberInvocation(self)



    def invocation(self):

        localctx = FHIRPathExpressionParser.InvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_invocation)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = FHIRPathExpressionParser.MemberInvocationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.identifier()
                pass

            elif la_ == 2:
                localctx = FHIRPathExpressionParser.FunctionInvocationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.function()
                pass

            elif la_ == 3:
                localctx = FHIRPathExpressionParser.ThisInvocationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.match(FHIRPathExpressionParser.T__34)
                pass

            elif la_ == 4:
                localctx = FHIRPathExpressionParser.IndexInvocationContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.match(FHIRPathExpressionParser.T__35)
                pass

            elif la_ == 5:
                localctx = FHIRPathExpressionParser.TotalInvocationContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 106
                self.match(FHIRPathExpressionParser.T__36)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.IdentifierContext,0)


        def paramList(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.ParamListContext,0)


        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = FHIRPathExpressionParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.identifier()
            self.state = 110
            self.match(FHIRPathExpressionParser.T__27)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4575657493346129968) != 0:
                self.state = 111
                self.paramList()


            self.state = 114
            self.match(FHIRPathExpressionParser.T__28)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)




    def paramList(self):

        localctx = FHIRPathExpressionParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.expression(0)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 117
                self.match(FHIRPathExpressionParser.T__37)
                self.state = 118
                self.expression(0)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(FHIRPathExpressionParser.NUMBER, 0)

        def unit(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.UnitContext,0)


        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_quantity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantity" ):
                listener.enterQuantity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantity" ):
                listener.exitQuantity(self)




    def quantity(self):

        localctx = FHIRPathExpressionParser.QuantityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_quantity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(FHIRPathExpressionParser.NUMBER)
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 125
                self.unit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dateTimePrecision(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.DateTimePrecisionContext,0)


        def pluralDateTimePrecision(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.PluralDateTimePrecisionContext,0)


        def STRING(self):
            return self.getToken(FHIRPathExpressionParser.STRING, 0)

        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)




    def unit(self):

        localctx = FHIRPathExpressionParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_unit)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39, 40, 41, 42, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.dateTimePrecision()
                pass
            elif token in [47, 48, 49, 50, 51, 52, 53, 54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.pluralDateTimePrecision()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.match(FHIRPathExpressionParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateTimePrecisionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_dateTimePrecision

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDateTimePrecision" ):
                listener.enterDateTimePrecision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDateTimePrecision" ):
                listener.exitDateTimePrecision(self)




    def dateTimePrecision(self):

        localctx = FHIRPathExpressionParser.DateTimePrecisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dateTimePrecision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 140187732541440) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PluralDateTimePrecisionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_pluralDateTimePrecision

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPluralDateTimePrecision" ):
                listener.enterPluralDateTimePrecision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPluralDateTimePrecision" ):
                listener.exitPluralDateTimePrecision(self)




    def pluralDateTimePrecision(self):

        localctx = FHIRPathExpressionParser.PluralDateTimePrecisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_pluralDateTimePrecision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 35888059530608640) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedIdentifier(self):
            return self.getTypedRuleContext(FHIRPathExpressionParser.QualifiedIdentifierContext,0)


        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)




    def typeSpecifier(self):

        localctx = FHIRPathExpressionParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.qualifiedIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FHIRPathExpressionParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(FHIRPathExpressionParser.IdentifierContext,i)


        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_qualifiedIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedIdentifier" ):
                listener.enterQualifiedIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedIdentifier" ):
                listener.exitQualifiedIdentifier(self)




    def qualifiedIdentifier(self):

        localctx = FHIRPathExpressionParser.QualifiedIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_qualifiedIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.identifier()
            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 140
                    self.match(FHIRPathExpressionParser.T__0)
                    self.state = 141
                    self.identifier()
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(FHIRPathExpressionParser.IDENTIFIER, 0)

        def DELIMITEDIDENTIFIER(self):
            return self.getToken(FHIRPathExpressionParser.DELIMITEDIDENTIFIER, 0)

        def getRuleIndex(self):
            return FHIRPathExpressionParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = FHIRPathExpressionParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 864691128467724288) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)


            if predIndex == 1:
                return self.precpred(self._ctx, 9)


            if predIndex == 2:
                return self.precpred(self._ctx, 7)


            if predIndex == 3:
                return self.precpred(self._ctx, 6)


            if predIndex == 4:
                return self.precpred(self._ctx, 5)


            if predIndex == 5:
                return self.precpred(self._ctx, 4)


            if predIndex == 6:
                return self.precpred(self._ctx, 3)


            if predIndex == 7:
                return self.precpred(self._ctx, 2)


            if predIndex == 8:
                return self.precpred(self._ctx, 1)


            if predIndex == 9:
                return self.precpred(self._ctx, 13)


            if predIndex == 10:
                return self.precpred(self._ctx, 12)


            if predIndex == 11:
                return self.precpred(self._ctx, 8)





