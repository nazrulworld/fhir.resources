# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/HealthcareService
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class HealthcareService(domainresource.DomainResource):
    """ The details of a healthcare service available at a location.
    """

    resource_type = Field("HealthcareService", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="Whether this HealthcareService record is in active use",
    )

    appointmentRequired: bool = Field(
        None,
        alias="appointmentRequired",
        title="Type `bool`",
        description="If an appointment is required for access to this service",
    )

    availabilityExceptions: fhirtypes.String = Field(
        None,
        alias="availabilityExceptions",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of availability exceptions",
    )

    availableTime: ListType[fhirtypes.HealthcareServiceAvailableTimeType] = Field(
        None,
        alias="availableTime",
        title="List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON)",
        description="Times the Service Site is available",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional description and/or any specific issues not covered elsewhere",
    )

    communication: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="communication",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The language that this service is offered in",
    )

    coverageArea: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="coverageArea",
        title="List of `Reference` items referencing `Location` (represented as `dict` in JSON)",
        description="Location(s) service is intended for/available to",
    )

    eligibility: ListType[fhirtypes.HealthcareServiceEligibilityType] = Field(
        None,
        alias="eligibility",
        title="List of `HealthcareServiceEligibility` items (represented as `dict` in JSON)",
        description="Specific eligibility requirements required to use the service",
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="List of `Reference` items referencing `Endpoint` (represented as `dict` in JSON)",
        description="Technical endpoints providing access to electronic services operated for the healthcare service",
    )

    extraDetails: fhirtypes.Markdown = Field(
        None,
        alias="extraDetails",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Extra details about the service that can\u0027t be placed in the other fields",
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
        title="List of `Reference` items referencing `Location` (represented as `dict` in JSON)",
        description="Location(s) where service may be provided",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of service as presented to a consumer while searching",
    )

    notAvailable: ListType[fhirtypes.HealthcareServiceNotAvailableType] = Field(
        None,
        alias="notAvailable",
        title="List of `HealthcareServiceNotAvailable` items (represented as `dict` in JSON)",
        description="Not available during this time due to provided reason",
    )

    photo: fhirtypes.AttachmentType = Field(
        None,
        alias="photo",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Facilitates quick identification of the service",
    )

    program: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="program",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Programs that this service is applicable to",
    )

    providedBy: fhirtypes.ReferenceType = Field(
        None,
        alias="providedBy",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
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
    """ Times the Service Site is available.
    A collection of times that the Service Site is available.
    """

    resource_type = Field("HealthcareServiceAvailableTime", const=True)

    allDay: bool = Field(
        None,
        alias="allDay",
        title="Type `bool`",
        description="Always available? e.g. 24 hour service",
    )

    availableEndTime: fhirtypes.Time = Field(
        None,
        alias="availableEndTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Closing time of day (ignored if allDay = true)",
    )

    availableStartTime: fhirtypes.Time = Field(
        None,
        alias="availableStartTime",
        title="Type `Time` (represented as `dict` in JSON)",
        description="Opening time of day (ignored if allDay = true)",
    )

    daysOfWeek: ListType[fhirtypes.Code] = Field(
        None,
        alias="daysOfWeek",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="mon | tue | wed | thu | fri | sat | sun",
    )


class HealthcareServiceEligibility(backboneelement.BackboneElement):
    """ Specific eligibility requirements required to use the service.
    Does this service have specific eligibility requirements that need to be
    met in order to use the service?
    """

    resource_type = Field("HealthcareServiceEligibility", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Coded value for the eligibility",
    )

    comment: fhirtypes.Markdown = Field(
        None,
        alias="comment",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Describes the eligibility conditions for the service",
    )


class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.
    The HealthcareService is not available during this period of time due to
    the provided reason.
    """

    resource_type = Field("HealthcareServiceNotAvailable", const=True)

    description: fhirtypes.String = Field(
        ...,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Reason presented to the user explaining why time not available",
    )

    during: fhirtypes.PeriodType = Field(
        None,
        alias="during",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Service not available from this date",
    )
