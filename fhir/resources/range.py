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
    """ Set of values bounded by low and high.
    A set of ordered Quantities defined by a low and high limit.
    """

    resource_type = Field("Range", const=True)

    high: fhirtypes.QuantityType = Field(
        None,
        alias="high",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="High limit",
    )

    low: fhirtypes.QuantityType = Field(
        None,
        alias="low",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Low limit",
    )
