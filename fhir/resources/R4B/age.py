from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Age
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
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
        """returning all element names from
        ``Age`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``Age`` according to specification,
        with preserving the original sequence order.
        """
        return ["value", "comparator", "unit", "system", "code"]
