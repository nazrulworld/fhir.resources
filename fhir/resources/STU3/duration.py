# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Duration
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import quantity


class Duration(quantity.Quantity):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A length of time.
    """

    resource_type = Field("Duration", const=True)

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Duration`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]
