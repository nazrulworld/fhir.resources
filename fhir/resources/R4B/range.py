from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Range
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic import Field

from . import element, fhirtypes


class Range(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Set of values bounded by low and high.
    A set of ordered Quantities defined by a low and high limit.
    """

    __resource_type__ = "Range"

    high: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="high",
        title="High limit",
        description="The high limit. The boundary is inclusive.",
        json_schema_extra={
            "element_property": True,
        },
    )

    low: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="low",
        title="Low limit",
        description="The low limit. The boundary is inclusive.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Range`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "low", "high"]
