# Generated from https://github.com/nazrulworld/fhir-parser/blob/c8e819379db32f15c7b806c769ed9ead3426b5ec/FHIRPathExpression.g4 by ANTLR 4.9.3from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FHIRPathExpressionParser import FHIRPathExpressionParser
else:
    from FHIRPathExpressionParser import FHIRPathExpressionParser

# This class defines a complete listener for a parse tree produced by FHIRPathExpressionParser.
class FHIRPathExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by FHIRPathExpressionParser#indexerExpression.
    def enterIndexerExpression(self, ctx:FHIRPathExpressionParser.IndexerExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#indexerExpression.
    def exitIndexerExpression(self, ctx:FHIRPathExpressionParser.IndexerExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#polarityExpression.
    def enterPolarityExpression(self, ctx:FHIRPathExpressionParser.PolarityExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#polarityExpression.
    def exitPolarityExpression(self, ctx:FHIRPathExpressionParser.PolarityExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:FHIRPathExpressionParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:FHIRPathExpressionParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:FHIRPathExpressionParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:FHIRPathExpressionParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#unionExpression.
    def enterUnionExpression(self, ctx:FHIRPathExpressionParser.UnionExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#unionExpression.
    def exitUnionExpression(self, ctx:FHIRPathExpressionParser.UnionExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#orExpression.
    def enterOrExpression(self, ctx:FHIRPathExpressionParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#orExpression.
    def exitOrExpression(self, ctx:FHIRPathExpressionParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#andExpression.
    def enterAndExpression(self, ctx:FHIRPathExpressionParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#andExpression.
    def exitAndExpression(self, ctx:FHIRPathExpressionParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#membershipExpression.
    def enterMembershipExpression(self, ctx:FHIRPathExpressionParser.MembershipExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#membershipExpression.
    def exitMembershipExpression(self, ctx:FHIRPathExpressionParser.MembershipExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#inequalityExpression.
    def enterInequalityExpression(self, ctx:FHIRPathExpressionParser.InequalityExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#inequalityExpression.
    def exitInequalityExpression(self, ctx:FHIRPathExpressionParser.InequalityExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#invocationExpression.
    def enterInvocationExpression(self, ctx:FHIRPathExpressionParser.InvocationExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#invocationExpression.
    def exitInvocationExpression(self, ctx:FHIRPathExpressionParser.InvocationExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#equalityExpression.
    def enterEqualityExpression(self, ctx:FHIRPathExpressionParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#equalityExpression.
    def exitEqualityExpression(self, ctx:FHIRPathExpressionParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#impliesExpression.
    def enterImpliesExpression(self, ctx:FHIRPathExpressionParser.ImpliesExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#impliesExpression.
    def exitImpliesExpression(self, ctx:FHIRPathExpressionParser.ImpliesExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#termExpression.
    def enterTermExpression(self, ctx:FHIRPathExpressionParser.TermExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#termExpression.
    def exitTermExpression(self, ctx:FHIRPathExpressionParser.TermExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#typeExpression.
    def enterTypeExpression(self, ctx:FHIRPathExpressionParser.TypeExpressionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#typeExpression.
    def exitTypeExpression(self, ctx:FHIRPathExpressionParser.TypeExpressionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#invocationTerm.
    def enterInvocationTerm(self, ctx:FHIRPathExpressionParser.InvocationTermContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#invocationTerm.
    def exitInvocationTerm(self, ctx:FHIRPathExpressionParser.InvocationTermContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#literalTerm.
    def enterLiteralTerm(self, ctx:FHIRPathExpressionParser.LiteralTermContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#literalTerm.
    def exitLiteralTerm(self, ctx:FHIRPathExpressionParser.LiteralTermContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#externalConstantTerm.
    def enterExternalConstantTerm(self, ctx:FHIRPathExpressionParser.ExternalConstantTermContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#externalConstantTerm.
    def exitExternalConstantTerm(self, ctx:FHIRPathExpressionParser.ExternalConstantTermContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#parenthesizedTerm.
    def enterParenthesizedTerm(self, ctx:FHIRPathExpressionParser.ParenthesizedTermContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#parenthesizedTerm.
    def exitParenthesizedTerm(self, ctx:FHIRPathExpressionParser.ParenthesizedTermContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#nullLiteral.
    def enterNullLiteral(self, ctx:FHIRPathExpressionParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#nullLiteral.
    def exitNullLiteral(self, ctx:FHIRPathExpressionParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:FHIRPathExpressionParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:FHIRPathExpressionParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#stringLiteral.
    def enterStringLiteral(self, ctx:FHIRPathExpressionParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#stringLiteral.
    def exitStringLiteral(self, ctx:FHIRPathExpressionParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#numberLiteral.
    def enterNumberLiteral(self, ctx:FHIRPathExpressionParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#numberLiteral.
    def exitNumberLiteral(self, ctx:FHIRPathExpressionParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#dateLiteral.
    def enterDateLiteral(self, ctx:FHIRPathExpressionParser.DateLiteralContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#dateLiteral.
    def exitDateLiteral(self, ctx:FHIRPathExpressionParser.DateLiteralContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#dateTimeLiteral.
    def enterDateTimeLiteral(self, ctx:FHIRPathExpressionParser.DateTimeLiteralContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#dateTimeLiteral.
    def exitDateTimeLiteral(self, ctx:FHIRPathExpressionParser.DateTimeLiteralContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#timeLiteral.
    def enterTimeLiteral(self, ctx:FHIRPathExpressionParser.TimeLiteralContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#timeLiteral.
    def exitTimeLiteral(self, ctx:FHIRPathExpressionParser.TimeLiteralContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#quantityLiteral.
    def enterQuantityLiteral(self, ctx:FHIRPathExpressionParser.QuantityLiteralContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#quantityLiteral.
    def exitQuantityLiteral(self, ctx:FHIRPathExpressionParser.QuantityLiteralContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#externalConstant.
    def enterExternalConstant(self, ctx:FHIRPathExpressionParser.ExternalConstantContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#externalConstant.
    def exitExternalConstant(self, ctx:FHIRPathExpressionParser.ExternalConstantContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#memberInvocation.
    def enterMemberInvocation(self, ctx:FHIRPathExpressionParser.MemberInvocationContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#memberInvocation.
    def exitMemberInvocation(self, ctx:FHIRPathExpressionParser.MemberInvocationContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#functionInvocation.
    def enterFunctionInvocation(self, ctx:FHIRPathExpressionParser.FunctionInvocationContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#functionInvocation.
    def exitFunctionInvocation(self, ctx:FHIRPathExpressionParser.FunctionInvocationContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#thisInvocation.
    def enterThisInvocation(self, ctx:FHIRPathExpressionParser.ThisInvocationContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#thisInvocation.
    def exitThisInvocation(self, ctx:FHIRPathExpressionParser.ThisInvocationContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#indexInvocation.
    def enterIndexInvocation(self, ctx:FHIRPathExpressionParser.IndexInvocationContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#indexInvocation.
    def exitIndexInvocation(self, ctx:FHIRPathExpressionParser.IndexInvocationContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#totalInvocation.
    def enterTotalInvocation(self, ctx:FHIRPathExpressionParser.TotalInvocationContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#totalInvocation.
    def exitTotalInvocation(self, ctx:FHIRPathExpressionParser.TotalInvocationContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#function.
    def enterFunction(self, ctx:FHIRPathExpressionParser.FunctionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#function.
    def exitFunction(self, ctx:FHIRPathExpressionParser.FunctionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#paramList.
    def enterParamList(self, ctx:FHIRPathExpressionParser.ParamListContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#paramList.
    def exitParamList(self, ctx:FHIRPathExpressionParser.ParamListContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#quantity.
    def enterQuantity(self, ctx:FHIRPathExpressionParser.QuantityContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#quantity.
    def exitQuantity(self, ctx:FHIRPathExpressionParser.QuantityContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#unit.
    def enterUnit(self, ctx:FHIRPathExpressionParser.UnitContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#unit.
    def exitUnit(self, ctx:FHIRPathExpressionParser.UnitContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#dateTimePrecision.
    def enterDateTimePrecision(self, ctx:FHIRPathExpressionParser.DateTimePrecisionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#dateTimePrecision.
    def exitDateTimePrecision(self, ctx:FHIRPathExpressionParser.DateTimePrecisionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#pluralDateTimePrecision.
    def enterPluralDateTimePrecision(self, ctx:FHIRPathExpressionParser.PluralDateTimePrecisionContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#pluralDateTimePrecision.
    def exitPluralDateTimePrecision(self, ctx:FHIRPathExpressionParser.PluralDateTimePrecisionContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:FHIRPathExpressionParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:FHIRPathExpressionParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#qualifiedIdentifier.
    def enterQualifiedIdentifier(self, ctx:FHIRPathExpressionParser.QualifiedIdentifierContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#qualifiedIdentifier.
    def exitQualifiedIdentifier(self, ctx:FHIRPathExpressionParser.QualifiedIdentifierContext):
        pass


    # Enter a parse tree produced by FHIRPathExpressionParser#identifier.
    def enterIdentifier(self, ctx:FHIRPathExpressionParser.IdentifierContext):
        pass

    # Exit a parse tree produced by FHIRPathExpressionParser#identifier.
    def exitIdentifier(self, ctx:FHIRPathExpressionParser.IdentifierContext):
        pass



del FHIRPathExpressionParser
