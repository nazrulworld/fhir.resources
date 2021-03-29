# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Age
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import quantity


class Age(quantity.Quantity):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A duration of time during which an organism (or a process) has existed.
    """

    resource_type = Field("Age", const=True)

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Age`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]
