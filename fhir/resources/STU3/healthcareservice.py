# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/HealthcareService
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class HealthcareService(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The details of a healthcare service available at a location.
    """

    resource_type = Field("HealthcareService", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="Whether this healthcareservice is in active use",
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    appointmentRequired: bool = Field(
        None,
        alias="appointmentRequired",
        title="Type `bool`",
        description="If an appointment is required for access to this service",
    )
    appointmentRequired__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_appointmentRequired",
        title="Extension field for ``appointmentRequired``.",
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

    availableTime: ListType[fhirtypes.HealthcareServiceAvailableTimeType] = Field(
        None,
        alias="availableTime",
        title=(
            "List of `HealthcareServiceAvailableTime` items (represented as `dict` "
            "in JSON)"
        ),
        description="Times the Service Site is available",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Broad category of service being performed or delivered",
    )

    characteristic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="characteristic",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Collection of characteristics (attributes)",
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String`",
        description=(
            "Additional description and/or any specific issues not covered " "elsewhere"
        ),
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    coverageArea: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="coverageArea",
        title=(
            "List of `Reference` items referencing `Location` (represented as "
            "`dict` in JSON)"
        ),
        description="Location(s) service is inteded for/available to",
    )

    eligibility: fhirtypes.CodeableConceptType = Field(
        None,
        alias="eligibility",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Specific eligibility requirements required to use the service",
    )

    eligibilityNote: fhirtypes.String = Field(
        None,
        alias="eligibilityNote",
        title="Type `String`",
        description="Describes the eligibility conditions for the service",
    )
    eligibilityNote__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_eligibilityNote", title="Extension field for ``eligibilityNote``."
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
            "location"
        ),
    )

    extraDetails: fhirtypes.String = Field(
        None,
        alias="extraDetails",
        title="Type `String`",
        description=(
            "Extra details about the service that can\u0027t be placed in the other "
            "fields"
        ),
    )
    extraDetails__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_extraDetails", title="Extension field for ``extraDetails``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External identifiers for this item",
    )

    location: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="location",
        title=(
            "List of `Reference` items referencing `Location` (represented as "
            "`dict` in JSON)"
        ),
        description="Location(s) where service may be provided",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Description of service as presented to a consumer while searching",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    notAvailable: ListType[fhirtypes.HealthcareServiceNotAvailableType] = Field(
        None,
        alias="notAvailable",
        title=(
            "List of `HealthcareServiceNotAvailable` items (represented as `dict` "
            "in JSON)"
        ),
        description="Not available during this time due to provided reason",
    )

    photo: fhirtypes.AttachmentType = Field(
        None,
        alias="photo",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Facilitates quick identification of the service",
    )

    programName: ListType[fhirtypes.String] = Field(
        None,
        alias="programName",
        title="List of `String` items",
        description="Program Names that categorize the service",
    )
    programName__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_programName", title="Extension field for ``programName``.")

    providedBy: fhirtypes.ReferenceType = Field(
        None,
        alias="providedBy",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Organization that provides this service",
    )

    referralMethod: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="referralMethod",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Ways that the service accepts referrals",
    )

    serviceProvisionCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceProvisionCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Conditions under which service is available/offered",
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Specialties handled by the HealthcareService",
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON)",
        description="Contacts related to the healthcare service",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Type of service that may be delivered or performed",
    )


class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Times the Service Site is available.
    A collection of times that the Service Site is available.
    """

    resource_type = Field("HealthcareServiceAvailableTime", const=True)

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


class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Not available during this time due to provided reason.
    The HealthcareService is not available during this period of time due to
    the provided reason.
    """

    resource_type = Field("HealthcareServiceNotAvailable", const=True)

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
        description="Service not availablefrom this date",
    )
