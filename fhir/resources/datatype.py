from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DataType
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from . import element


class DataType(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Reuseable Types.
    The base class for all re-useable types defined as part of the FHIR
    Specification.
    """

    __resource_type__ = "DataType"

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``DataType`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension"]
