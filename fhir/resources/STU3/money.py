from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Money
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from . import quantity


class Money(quantity.Quantity):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An amount of economic utility in some recognized currency.
    """

    __resource_type__ = "Money"

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``Money`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``Money`` according to specification,
        with preserving the original sequence order.
        """
        return ["value", "comparator", "unit", "system", "code"]
