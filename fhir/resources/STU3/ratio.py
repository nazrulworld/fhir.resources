from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Ratio
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Ratio(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A ratio of two Quantity values - a numerator and a denominator.
    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """

    __resource_type__ = "Ratio"

    denominator: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="denominator",
        title="Denominator value",
        description="The value of the denominator.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    numerator: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="numerator",
        title="Numerator value",
        description="The value of the numerator.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``Ratio`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "numerator", "denominator"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``Ratio`` according to specification,
        with preserving the original sequence order.
        """
        return ["numerator", "denominator"]
