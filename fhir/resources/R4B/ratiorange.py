# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RatioRange
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic import Field

from . import element, fhirtypes


class RatioRange(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Range of ratio values.
    A range of ratios expressed as a low and high numerator and a denominator.
    """

    __resource_type__ = "RatioRange"

    denominator: fhirtypes.QuantityType = Field(  # type: ignore
        None,
        alias="denominator",
        title="Denominator value",
        description="The value of the denominator.",
        json_schema_extra={
            "element_property": True,
        },
    )

    highNumerator: fhirtypes.QuantityType = Field(  # type: ignore
        None,
        alias="highNumerator",
        title="High Numerator limit",
        description="The value of the high limit numerator.",
        json_schema_extra={
            "element_property": True,
        },
    )

    lowNumerator: fhirtypes.QuantityType = Field(  # type: ignore
        None,
        alias="lowNumerator",
        title="Low Numerator limit",
        description="The value of the low limit numerator.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RatioRange`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "lowNumerator", "highNumerator", "denominator"]
