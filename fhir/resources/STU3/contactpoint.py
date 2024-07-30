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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of a Technology mediated contact point (phone, fax, email, etc.).
    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """

    __resource_type__ = "ContactPoint"

    period: fhirtypes.PeriodType = Field(  # type: ignore
        None,
        alias="period",
        title="Time period when the contact point was/is in use",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    rank: fhirtypes.PositiveIntType = Field(  # type: ignore
        None,
        alias="rank",
        title="Specify preferred order of use (1 = highest)",
        description=(
            "Specifies a preferred order in which to use a set of contacts. "
            "Contacts are ranked with lower values coming before higher values."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_rank", title="Extension field for ``rank``."
    )

    system: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="system",
        title="phone | fax | email | pager | url | sms | other",
        description=(
            "Telecommunications form for contact point - what communications system"
            " is required to make use of the contact."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["phone", "fax", "email", "pager", "url", "sms", "other"],
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_system", title="Extension field for ``system``."
    )

    use: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="use",
        title="home | work | temp | old | mobile - purpose of this contact point",
        description="Identifies the purpose for the contact point.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["home", "work", "temp", "old", "mobile"],
        },
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_use", title="Extension field for ``use``."
    )

    value: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="value",
        title="The actual contact point details",
        description=(
            "The actual contact point details, in a form that is meaningful to the "
            "designated communication system (i.e. phone number or email address)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ContactPoint`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "system", "value", "use", "rank", "period"]
