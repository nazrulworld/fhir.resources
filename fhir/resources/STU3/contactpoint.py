# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ContactPoint
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class ContactPoint(element.Element):
    """ Details of a Technology mediated contact point (phone, fax, email, etc.).
    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """

    resource_type = Field("ContactPoint", const=True)

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period when the contact point was/is in use",
    )

    rank: fhirtypes.PositiveInt = Field(
        None,
        alias="rank",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Specify preferred order of use (1 = highest)",
    )

    system: fhirtypes.Code = Field(
        None,
        alias="system",
        title="Type `Code` (represented as `dict` in JSON)",
        description="phone | fax | email | pager | url | sms | other",
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="home | work | temp | old | mobile - purpose of this contact point",
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String` (represented as `dict` in JSON)",
        description="The actual contact point details",
    )
