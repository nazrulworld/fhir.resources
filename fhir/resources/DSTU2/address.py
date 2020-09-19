# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Address
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .element import Element


class Address(Element):
    """A postal address.

    There is a variety of postal address formats defined around the world. This
    format defines a superset that is the basis for all addresses around the
    world.
    """

    resource_type = Field("Address", const=True)

    city: fhirtypes.String = Field(
        None,
        alias="city",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of city, town etc.",
    )

    country: fhirtypes.String = Field(
        None,
        alias="country",
        title="Type `String` (represented as `dict` in JSON)",
        description="Country (e.g. can be ISO 3166 2 or 3 letter code)",
    )

    district: fhirtypes.String = Field(
        None,
        alias="district",
        title="Type `String` (represented as `dict` in JSON)",
        description="District name (aka county)",
    )

    line: ListType[fhirtypes.String] = Field(
        None,
        alias="line",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Street name, number, direction \u0026 P.O. Box etc.",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Postal code for area",
    )

    state: fhirtypes.String = Field(
        None,
        alias="state",
        title="Type `String` (represented as `dict` in JSON)",
        description="Sub-unit of country (abbreviations ok)",
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Type `String` (represented as `dict` in JSON)",
        description="Text representation of the address",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="postal | physical | both",
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="home | work | temp | old - purpose of this address",
    )
