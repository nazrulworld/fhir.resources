from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Age
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from . import quantity


class Age(quantity.Quantity):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A duration of time during which an organism (or a process) has existed.
    """

    __resource_type__ = "Age"

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Age`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]
