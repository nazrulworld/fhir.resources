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
        title="Type `bool`",
        description="Whether this practitioner role record is in active use",
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    availabilityExceptions: fhirtypes.String = Field(
        None,
        alias="availabilityExceptions",
        title="Type `String`",
        description="Description of availability exceptions",
    )
    availabilityExceptions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_availabilityExceptions",
        title="Extension field for ``availabilityExceptions``.",
    )

    availableTime: ListType[fhirtypes.PractitionerRoleAvailableTimeType] = Field(
        None,
        alias="availableTime",
        title=(
            "List of `PractitionerRoleAvailableTime` items (represented as `dict` "
            "in JSON)"
        ),
        description="Times the Service Site is available",
    )

    code: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Roles which this practitioner may perform",
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "List of `Reference` items referencing `Endpoint` (represented as "
            "`dict` in JSON)"
        ),
        description=(
            "Technical endpoints providing access to services operated for the "
            "practitioner with this role"
        ),
    )

    healthcareService: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="healthcareService",
        title=(
            "List of `Reference` items referencing `HealthcareService` (represented"
            " as `dict` in JSON)"
        ),
        description=(
            "The list of healthcare services that this worker provides for this "
            "role\u0027s Organization/Location(s)"
        ),
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business Identifiers that are specific to a role/location",
    )

    location: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="location",
        title=(
            "List of `Reference` items referencing `Location` (represented as "
            "`dict` in JSON)"
        ),
        description="The location(s) at which this practitioner provides care",
    )

    notAvailable: ListType[fhirtypes.PractitionerRoleNotAvailableType] = Field(
        None,
        alias="notAvailable",
        title=(
            "List of `PractitionerRoleNotAvailable` items (represented as `dict` in"
            " JSON)"
        ),
        description="Not available during this time due to provided reason",
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization where the roles are available",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description=(
            "The period during which the practitioner is authorized to perform in "
            "these role(s)"
        ),
    )

    practitioner: fhirtypes.ReferenceType = Field(
        None,
        alias="practitioner",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description=(
            "Practitioner that is able to provide the defined services for the "
            "organization"
        ),
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Specific specialty of the practitioner",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="Contact details that are specific to the role/location/service",
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
        title="Type `bool`",
        description="Always available? e.g. 24 hour service",
    )
    allDay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allDay", title="Extension field for ``allDay``."
    )

    availableEndTime: fhirtypes.Time = Field(
        None,
        alias="availableEndTime",
        title="Type `Time`",
        description="Closing time of day (ignored if allDay = true)",
    )
    availableEndTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_availableEndTime",
        title="Extension field for ``availableEndTime``.",
    )

    availableStartTime: fhirtypes.Time = Field(
        None,
        alias="availableStartTime",
        title="Type `Time`",
        description="Opening time of day (ignored if allDay = true)",
    )
    availableStartTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_availableStartTime",
        title="Extension field for ``availableStartTime``.",
    )

    daysOfWeek: ListType[fhirtypes.Code] = Field(
        None,
        alias="daysOfWeek",
        title="List of `Code` items",
        description="mon | tue | wed | thu | fri | sat | sun",
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
        title="Type `String`",
        description="Reason presented to the user explaining why time not available",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    during: fhirtypes.PeriodType = Field(
        None,
        alias="during",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Service not available from this date",
    )
