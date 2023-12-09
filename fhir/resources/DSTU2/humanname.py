# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/HumanName
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""

from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .element import Element


class HumanName(Element):
    """Name of a human - parts and usage.

    A human's name with the ability to identify parts and usage.
    """

    resource_type = Field("HumanName", const=True)

    family: ListType[fhirtypes.String] = Field(
        None,
        alias="family",
        title="Type `String` (represented as `dict` in JSON)",
        description="Family name (often called 'Surname')",
    )

    given: ListType[fhirtypes.String] = Field(
        None,
        alias="given",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Given names (not always 'first'). Includes middle names",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period when name was/is in use",
    )

    prefix: ListType[fhirtypes.String] = Field(
        None,
        alias="prefix",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Parts that come before the name",
    )

    suffix: ListType[fhirtypes.String] = Field(
        None,
        alias="suffix",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Parts that come after the name",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Text representation of the full name",
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="usual | official | temp | nickname | anonymous | old | maiden",
    )
