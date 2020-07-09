# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Flag
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class Flag(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Key information to flag to healthcare providers.
    Prospective warnings of potential issues when providing care to the
    patient.
    """

    resource_type = Field("Flag", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Flag creator",
        description="The person, organization or device that created the flag.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Organization",
            "Patient",
            "Practitioner",
            "PractitionerRole",
        ],
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Clinical, administrative, etc.",
        description=(
            "Allows a flag to be divided into different categories like clinical, "
            "administrative etc. Intended to be used as a means of filtering which "
            "flags are displayed to particular user or in a given context."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Coded or textual message to display to user",
        description=(
            "The coded value or textual component of the flag to display to the "
            "user."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Alert relevant during encounter",
        description="This alert is only relevant during the encounter.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Business identifiers assigned to this flag by the performer or other "
            "systems which remain constant as the resource is updated and "
            "propagates from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time period when flag is active",
        description=(
            "The period of time from the activation of the flag to inactivation of "
            "the flag. If the flag is active, the end of the period should be "
            "unspecified."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="active | inactive | entered-in-error",
        description="Supports basic workflow.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "inactive", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who/What is flag about?",
        description=(
            "The patient, location, group, organization, or practitioner etc. this "
            "is about record this flag is associated with."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Location",
            "Group",
            "Organization",
            "Practitioner",
            "PlanDefinition",
            "Medication",
            "Procedure",
        ],
    )
