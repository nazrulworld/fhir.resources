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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of a Technology mediated contact point (phone, fax, email, etc.).
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
        title="Type `PositiveInt`",
        description="Specify preferred order of use (1 = highest)",
    )
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rank", title="Extension field for ``rank``."
    )

    system: fhirtypes.Code = Field(
        None,
        alias="system",
        title="Type `Code`",
        description="phone | fax | email | pager | url | sms | other",
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code`",
        description="home | work | temp | old | mobile - purpose of this contact point",
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="Type `String`",
        description="The actual contact point details",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )
