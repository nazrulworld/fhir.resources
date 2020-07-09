# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Ratio
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Ratio(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A ratio of two Quantity values - a numerator and a denominator.
    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """

    resource_type = Field("Ratio", const=True)

    denominator: fhirtypes.QuantityType = Field(
        None,
        alias="denominator",
        title="Denominator value",
        description="The value of the denominator.",
        # if property is element of this resource.
        element_property=True,
    )

    numerator: fhirtypes.QuantityType = Field(
        None,
        alias="numerator",
        title="Numerator value",
        description="The value of the numerator.",
        # if property is element of this resource.
        element_property=True,
    )
