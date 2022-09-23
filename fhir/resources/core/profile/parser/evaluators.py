# _*_ coding: utf-8 _*_
from typing import Optional, Union, TYPE_CHECKING

from pydantic.error_wrappers import ValidationError

if TYPE_CHECKING:
    from fhir.resources.core.fhirabstractmodel import FHIRAbstractModel

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


class Empty:
    pass


EMPTY = Empty()


class Evaluation(object):
    """ """

    __slots__ = ("error", "success")

    def __init__(self, error: Optional[ValidationError] = None):
        """ """
        object.__setattr__(self, "error", error)
        object.__setattr__(self, "success", error is None)

    def __bool__(self) -> bool:
        """ """
        return self.success

    def __setattr__(self, key, value):
        """ """
        raise TypeError("Readonly object!")


class ValuedEvaluation(Evaluation):
    """ """

    __slots__ = ("value",) + Evaluation.__slots__

    def __init__(
        self,
        value: Union["FHIRAbstractModel", Empty, None],
        error: Optional[ValidationError] = None,
    ):
        """ """
        Evaluation.__init__(self, error)
        object.__setattr__(self, "value", value)


class EvaluatorBase:
    """ """
    expression_literal: str = None

    def evaluate(self, resource: "FHIRAbstractModel") -> Evaluation:
        """ """
        raise NotImplementedError


class OperatorBase:
    """ """
    left: EvaluatorBase = None
    right: EvaluatorBase = None

    def __init__(self, left, right):
        self.left = left
        self.right = right


class LogicalOperator(OperatorBase):
    """ """


class ComparisonOperator(OperatorBase):
    """ """


class ParenthesizedTerm(EvaluatorBase):
    """ """
    term: EvaluatorBase = None

    def evaluate(self, resource: "FHIRAbstractModel") -> Evaluation:
        """ """
        # custom error in case of failed?
        return self.term.evaluate(resource)


class OrEvaluator(EvaluatorBase, LogicalOperator):
    def evaluate(self, resource: "FHIRAbstractModel"):
        left_res = self.left.evaluate(resource)
        if bool(left_res) is True:
            # evaluation passed!
            return Evaluation()
        return self.right.evaluate(resource)


class AndEvaluator(EvaluatorBase, LogicalOperator):
    def evaluate(self, resource: "FHIRAbstractModel"):
        for member in (self.left, self.right):
            res = member.evaluate(resource)
            if bool(res) is False:
                # evaluation failed!
                return res
        return Evaluation()


class XOrEvaluator(EvaluatorBase, LogicalOperator):
    def evaluate(self, resource: "FHIRAbstractModel") -> Evaluation:
        left_res = self.left.evaluate(resource)
        right_res = self.right.evaluate(resource)
        if bool(left_res) is False and bool(right_res) is False:
            # todo: combine error
            return Evaluation()
        if bool(left_res) is True and bool(right_res) is True:
            # todo: combine error
            return Evaluation()
        return Evaluation()
