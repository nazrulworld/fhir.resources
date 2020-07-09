# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Range
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Range(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Set of values bounded by low and high.
    A set of ordered Quantities defined by a low and high limit.
    """

    resource_type = Field("Range", const=True)

    high: fhirtypes.QuantityType = Field(
        None,
        alias="high",
        title="High limit",
        description="The high limit. The boundary is inclusive.",
        # if property is element of this resource.
        element_property=True,
    )

    low: fhirtypes.QuantityType = Field(
        None,
        alias="low",
        title="Low limit",
        description="The low limit. The boundary is inclusive.",
        # if property is element of this resource.
        element_property=True,
    )
