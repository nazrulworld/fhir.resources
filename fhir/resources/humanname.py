# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/HumanName
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import element, fhirtypes


class HumanName(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Name of a human - parts and usage.
    A human's name with the ability to identify parts and usage.
    """

    resource_type = Field("HumanName", const=True)

    family: fhirtypes.String = Field(
        None,
        alias="family",
        title="Type `String`",
        description="Family name (often called \u0027Surname\u0027)",
    )
    family__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_family", title="Extension field for ``family``."
    )

    given: ListType[fhirtypes.String] = Field(
        None,
        alias="given",
        title="List of `String` items",
        description="Given names (not always \u0027first\u0027). Includes middle names",
    )
    given__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_given", title="Extension field for ``given``."
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
        title="List of `String` items",
        description="Parts that come before the name",
    )
    prefix__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_prefix", title="Extension field for ``prefix``."
    )

    suffix: ListType[fhirtypes.String] = Field(
        None,
        alias="suffix",
        title="List of `String` items",
        description="Parts that come after the name",
    )
    suffix__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_suffix", title="Extension field for ``suffix``."
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String`",
        description="Text representation of the full name",
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code`",
        description="usual | official | temp | nickname | anonymous | old | maiden",
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )
