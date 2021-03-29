# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Money
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import quantity


class Money(quantity.Quantity):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An amount of economic utility in some recognized currency.
    """

    resource_type = Field("Money", const=True)

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Money`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]
