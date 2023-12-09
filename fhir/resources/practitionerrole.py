# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PractitionerRole
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field

from . import domainresource, fhirtypes


class PractitionerRole(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Roles/organizations the practitioner is associated with.
    A specific set of Roles/Locations/specialties/services that a practitioner
    may perform at an organization for a period of time.
    """

    resource_type = Field("PractitionerRole", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this practitioner role record is in active use",
        description=(
            " Whether this practitioner role record is in active use. Some systems "
            "may use this property to mark non-active practitioners, such as those "
            "that are not currently employed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    availability: typing.List[fhirtypes.AvailabilityType] = Field(
        None,
        alias="availability",
        title=(
            "Times the Practitioner is available at this location and/or healthcare"
            " service (including exceptions)"
        ),
        description=(
            "A collection of times the practitioner is available or performing this"
            " role at the location and/or healthcareservice."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    characteristic: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="characteristic",
        title="Collection of characteristics (attributes)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    code: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="Roles which this practitioner may perform",
        description=(
            "Roles which this practitioner is authorized to perform for the "
            "organization."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    communication: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="communication",
        title=(
            "A language the practitioner (in this role) can use in patient "
            "communication"
        ),
        description=(
            "A language the practitioner can use in patient communication. The "
            "practitioner may know several languages (listed in "
            "practitioner.communication), however these are the languages that "
            "could be advertised in a directory for a patient to search."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ExtendedContactDetailType] = Field(
        None,
        alias="contact",
        title="Official contact details relating to this PractitionerRole",
        description=(
            "The contact details of communication devices available relevant to the"
            " specific PractitionerRole. This can include addresses, phone numbers,"
            " fax numbers, mobile numbers, email addresses and web sites."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    endpoint: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="Endpoints for interacting with the practitioner in this role",
        description=(
            " Technical endpoints providing access to services operated for the "
            "practitioner with this role. Commonly used for locating scheduling "
            "services, or identifying where to send referrals electronically."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    healthcareService: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="healthcareService",
        title="Healthcare services provided for this role's Organization/Location(s)",
        description=(
            "The list of healthcare services that this worker provides for this "
            "role's Organization/Location(s)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["HealthcareService"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifiers for a role/location",
        description="Business Identifiers that are specific to a role/location.",
        # if property is element of this resource.
        element_property=True,
    )

    location: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="location",
        title="Location(s) where the practitioner provides care",
        description="The location(s) at which this practitioner provides care.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Organization where the roles are available",
        description="The organization where the Practitioner performs the roles associated.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title=(
            "The period during which the practitioner is authorized to perform in "
            "these role(s)"
        ),
        description=(
            "The period during which the person is authorized to act as a "
            "practitioner in these role(s) for the organization."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    practitioner: fhirtypes.ReferenceType = Field(
        None,
        alias="practitioner",
        title="Practitioner that provides services for the organization",
        description=(
            "Practitioner that is able to provide the defined services for the "
            "organization."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    specialty: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="Specific specialty of the practitioner",
        description=(
            "The specialty of a practitioner that describes the functional role "
            "they are practicing at a given organization or location."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``PractitionerRole`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "active",
            "period",
            "practitioner",
            "organization",
            "code",
            "specialty",
            "location",
            "healthcareService",
            "contact",
            "characteristic",
            "communication",
            "availability",
            "endpoint",
        ]
