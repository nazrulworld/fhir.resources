# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Address
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import element, fhirtypes


class Address(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).
    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey
    addresses for use in delivering mail as well as for visiting locations
    which might not be valid for mail delivery.  There are a variety of postal
    address formats defined around the world.
    """

    resource_type = Field("Address", const=True)

    city: fhirtypes.String = Field(
        None, alias="city", title="Type `String`", description="Name of city, town etc."
    )
    city__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_city", title="Extension field for ``city``."
    )

    country: fhirtypes.String = Field(
        None,
        alias="country",
        title="Type `String`",
        description="Country (e.g. can be ISO 3166 2 or 3 letter code)",
    )
    country__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_country", title="Extension field for ``country``."
    )

    district: fhirtypes.String = Field(
        None,
        alias="district",
        title="Type `String`",
        description="District name (aka county)",
    )
    district__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_district", title="Extension field for ``district``."
    )

    line: ListType[fhirtypes.String] = Field(
        None,
        alias="line",
        title="List of `String` items",
        description="Street name, number, direction \u0026 P.O. Box etc.",
    )
    line__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_line", title="Extension field for ``line``."
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period when address was/is in use",
    )

    postalCode: fhirtypes.String = Field(
        None,
        alias="postalCode",
        title="Type `String`",
        description="Postal code for area",
    )
    postalCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_postalCode", title="Extension field for ``postalCode``."
    )

    state: fhirtypes.String = Field(
        None,
        alias="state",
        title="Type `String`",
        description="Sub-unit of country (abbreviations ok)",
    )
    state__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_state", title="Extension field for ``state``."
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String`",
        description="Text representation of the address",
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.Code = Field(
        None, alias="type", title="Type `Code`", description="postal | physical | both"
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code`",
        description="home | work | temp | old | billing - purpose of this address",
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )
