# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Range
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from pydantic import Field

from . import fhirtypes
from .element import Element


class Range(Element):
    """Set of values bounded by low and high.

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
