# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Range
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
