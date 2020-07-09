# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PractitionerRole
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class PractitionerRole(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    availabilityExceptions: fhirtypes.String = Field(
        None,
        alias="availabilityExceptions",
        title="Description of availability exceptions",
        description=(
            "A description of site availability exceptions, e.g. public holiday "
            "availability. Succinctly describing all possible exceptions to normal "
            "site availability as details in the available Times and not available "
            "Times."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    availabilityExceptions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_availabilityExceptions",
        title="Extension field for ``availabilityExceptions``.",
    )

    availableTime: ListType[fhirtypes.PractitionerRoleAvailableTimeType] = Field(
        None,
        alias="availableTime",
        title="Times the Service Site is available",
        description=(
            "A collection of times the practitioner is available or performing this"
            " role at the location and/or healthcareservice."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: ListType[fhirtypes.CodeableConceptType] = Field(
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

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "Technical endpoints providing access to services operated for the "
            "practitioner with this role"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    healthcareService: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="healthcareService",
        title=(
            "The list of healthcare services that this worker provides for this "
            "role's Organization/Location(s)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["HealthcareService"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifiers that are specific to a role/location",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    location: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="location",
        title="The location(s) at which this practitioner provides care",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    notAvailable: ListType[fhirtypes.PractitionerRoleNotAvailableType] = Field(
        None,
        alias="notAvailable",
        title="Not available during this time due to provided reason",
        description=(
            "The practitioner is not available or performing this role during this "
            "period of time due to the provided reason."
        ),
        # if property is element of this resource.
        element_property=True,
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
        title=(
            "Practitioner that is able to provide the defined services for the "
            "organization"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="Specific specialty of the practitioner",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contact details that are specific to the role/location/service",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class PractitionerRoleAvailableTime(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Times the Service Site is available.
    A collection of times the practitioner is available or performing this role
    at the location and/or healthcareservice.
    """

    resource_type = Field("PractitionerRoleAvailableTime", const=True)

    allDay: bool = Field(
        None,
        alias="allDay",
        title="Always available? e.g. 24 hour service",
        description=(
            "Is this always available? (hence times are irrelevant) e.g. 24 hour "
            "service."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    allDay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allDay", title="Extension field for ``allDay``."
    )

    availableEndTime: fhirtypes.Time = Field(
        None,
        alias="availableEndTime",
        title="Closing time of day (ignored if allDay = true)",
        description=(
            "The closing time of day. Note: If the AllDay flag is set, then this "
            "time is ignored."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    availableEndTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_availableEndTime",
        title="Extension field for ``availableEndTime``.",
    )

    availableStartTime: fhirtypes.Time = Field(
        None,
        alias="availableStartTime",
        title="Opening time of day (ignored if allDay = true)",
        description=(
            "The opening time of day. Note: If the AllDay flag is set, then this "
            "time is ignored."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    availableStartTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_availableStartTime",
        title="Extension field for ``availableStartTime``.",
    )

    daysOfWeek: ListType[fhirtypes.Code] = Field(
        None,
        alias="daysOfWeek",
        title="mon | tue | wed | thu | fri | sat | sun",
        description=(
            "Indicates which days of the week are available between the start and "
            "end Times."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
    )
    daysOfWeek__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_daysOfWeek", title="Extension field for ``daysOfWeek``.")


class PractitionerRoleNotAvailable(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Not available during this time due to provided reason.
    The practitioner is not available or performing this role during this
    period of time due to the provided reason.
    """

    resource_type = Field("PractitionerRoleNotAvailable", const=True)

    description: fhirtypes.String = Field(
        ...,
        alias="description",
        title="Reason presented to the user explaining why time not available",
        description=(
            "The reason that can be presented to the user as to why this time is "
            "not available."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    during: fhirtypes.PeriodType = Field(
        None,
        alias="during",
        title="Service not available from this date",
        description=(
            "Service is not available (seasonally or for a public holiday) from "
            "this date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
