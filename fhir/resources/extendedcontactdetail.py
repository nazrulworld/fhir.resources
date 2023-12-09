# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExtendedContactDetail
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field

from . import datatype, fhirtypes


class ExtendedContactDetail(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contact information.
    Specifies contact information for a specific purpose over a period of time,
    might be handled/monitored by a specific named person or organization.
    """

    resource_type = Field("ExtendedContactDetail", const=True)

    address: fhirtypes.AddressType = Field(
        None,
        alias="address",
        title="Address for the contact",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: typing.List[fhirtypes.HumanNameType] = Field(
        None,
        alias="name",
        title="Name of an individual to contact",
        description=(
            "The name of an individual to contact, some types of contact detail are"
            " usually blank."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="This contact detail is handled/monitored by a specific organization",
        description=(
            "This contact detail is handled/monitored by a specific organization. "
            "If the name is provided in the contact, then it is referring to the "
            "named individual within this organization."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period that this contact was valid for usage",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    purpose: fhirtypes.CodeableConceptType = Field(
        None,
        alias="purpose",
        title="The type of contact",
        description="The purpose/type of contact.",
        # if property is element of this resource.
        element_property=True,
    )

    telecom: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contact details (e.g.phone/fax/url)",
        description="The contact details application for the purpose defined.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExtendedContactDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "purpose",
            "name",
            "telecom",
            "address",
            "organization",
            "period",
        ]
