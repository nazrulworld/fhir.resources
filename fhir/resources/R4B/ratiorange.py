# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RatioRange
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1 import Field

from . import element, fhirtypes


class RatioRange(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Range of ratio values.
    A range of ratios expressed as a low and high numerator and a denominator.
    """

    resource_type = Field("RatioRange", const=True)

    denominator: fhirtypes.QuantityType = Field(
        None,
        alias="denominator",
        title="Denominator value",
        description="The value of the denominator.",
        # if property is element of this resource.
        element_property=True,
    )

    highNumerator: fhirtypes.QuantityType = Field(
        None,
        alias="highNumerator",
        title="High Numerator limit",
        description="The value of the high limit numerator.",
        # if property is element of this resource.
        element_property=True,
    )

    lowNumerator: fhirtypes.QuantityType = Field(
        None,
        alias="lowNumerator",
        title="Low Numerator limit",
        description="The value of the low limit numerator.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RatioRange`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "lowNumerator", "highNumerator", "denominator"]
