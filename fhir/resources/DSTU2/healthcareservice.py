# -*- coding: utf-8 -*-
"""
Profile: https://www.hl7.org/fhir/DSTU2/healthcareservice.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class HealthcareService(domainresource.DomainResource):
    """The details of a healthcare service available at a location."""

    resource_type = Field("HealthcareService", const=True)

    appointmentRequired: fhirtypes.Boolean = Field(
        None,
        alias="appointmentRequired",
        title="If an appointment is required for access to this service",
        description=(
            "Indicates whether or not a prospective consumer will require an "
            "appointment for a particular service at a site to be provided by the "
            "Organization. Indicates if an appointment is required for access to "
            "this service."
        ),
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
    )

    availableTime: ListType[fhirtypes.HealthcareServiceAvailableTimeType] = Field(
        None,
        alias="availableTime",
        title="Times the Service Site is available",
        description="A collection of times that the Service Site is available.",
    )

    characteristic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="characteristic",
        title="Collection of characteristics (attributes)",
        description=None,
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title=(
            "Additional description and/or any specific issues not covered " "elsewhere"
        ),
        description=(
            "Any additional description of the service and/or any specific issues "
            "not covered by the other attributes, which can be displayed as further"
            " detail under the serviceName."
        ),
    )

    coverageArea: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="coverageArea",
        title="Location(s) service is intended for/available to",
        description=(
            "The location(s) that this service is available to (not where the "
            "service is provided)."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    eligibility: fhirtypes.CodeableConceptType = Field(
        None,
        alias="eligibility",
        title="Specific eligibility requirements required to use the service",
        description=(
            "Does this service have specific eligibility requirements that need to "
            "be met in order to use the service?"
        ),
    )

    eligibilityNote: fhirtypes.String = Field(
        None,
        alias="eligibilityNote",
        title="Describes the eligibility conditions for the service",
        description=None,
    )

    extraDetails: fhirtypes.String = Field(
        None,
        alias="extraDetails",
        title=(
            "Extra details about the service that can't be placed in the other "
            "fields"
        ),
        description=None,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifiers for this item",
        description=None,
    )

    location: fhirtypes.ReferenceType = Field(
        ...,
        alias="location",
        title="Location(s) where service may be provided",
        description="The location(s) where this healthcare service may be provided.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    notAvailable: ListType[fhirtypes.HealthcareServiceNotAvailableType] = Field(
        None,
        alias="notAvailable",
        title="Not available during this time due to provided reason",
        description=(
            "The HealthcareService is not available during this period of time due "
            "to the provided reason."
        ),
    )

    photo: fhirtypes.AttachmentType = Field(
        None,
        alias="photo",
        title="Facilitates quick identification of the service",
        description=(
            "If there is a photo/symbol associated with this HealthcareService, it "
            "may be included here to facilitate quick identification of the service"
            " in a list."
        ),
    )

    programName: ListType[fhirtypes.String] = Field(
        None,
        alias="programName",
        title="Program Names that categorize the service",
        description=None,
    )

    providedBy: fhirtypes.ReferenceType = Field(
        None,
        alias="providedBy",
        title="Organization that provides this service",
        description="The organization that provides this healthcare service.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    publicKey: fhirtypes.String = Field(
        None,
        alias="publicKey",
        title="PKI Public keys to support secure communications",
        description=None,
    )

    referralMethod: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="referralMethod",
        title="Ways that the service accepts referrals",
        description=(
            "Ways that the service accepts referrals, if this is not provided then "
            "it is implied that no referral is required."
        ),
    )

    serviceCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="serviceCategory",
        title="Broad category of service being performed or delivered",
        description="Identifies the broad category of service being performed or delivered.",
    )

    serviceProvisionCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceProvisionCode",
        title="Conditions under which service is available/offered",
        description=(
            "The code(s) that detail the conditions under which the healthcare "
            "service is available/offered."
        ),
    )

    serviceName: fhirtypes.String = Field(
        None,
        alias="serviceName",
        title="Description of service as presented to a consumer while searching",
        description=(
            "Further description of the service as it would be presented to a "
            "consumer while searching."
        ),
    )

    serviceType: ListType[fhirtypes.HealthcareServiceServiceTypeType] = Field(
        None,
        alias="serviceType",
        title="Specific service delivered or performed",
        description=None,
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contacts related to the healthcare service",
        description="List of contacts related to this specific healthcare service.",
    )


class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """Times the Service Site is available.

    A collection of times that the Service Site is available.
    """

    resource_type = Field("HealthcareServiceAvailableTime", const=True)

    allDay: fhirtypes.Boolean = Field(
        None,
        alias="allDay",
        title="Always available? e.g. 24 hour service",
        description=(
            "Is this always available? (hence times are irrelevant) e.g. 24 hour "
            "service."
        ),
    )

    availableEndTime: fhirtypes.Time = Field(
        None,
        alias="availableEndTime",
        title="Closing time of day (ignored if allDay = true)",
        description=(
            "The closing time of day. Note: If the AllDay flag is set, then this "
            "time is ignored."
        ),
    )

    availableStartTime: fhirtypes.Time = Field(
        None,
        alias="availableStartTime",
        title="Opening time of day (ignored if allDay = true)",
        description=(
            "The opening time of day. Note: If the AllDay flag is set, then this "
            "time is ignored."
        ),
    )

    daysOfWeek: ListType[fhirtypes.Code] = Field(
        None,
        alias="daysOfWeek",
        title="mon | tue | wed | thu | fri | sat | sun",
        description=(
            "Indicates which days of the week are available between the start and "
            "end Times."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
    )


class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """Not available during this time due to provided reason.

    The HealthcareService is not available during this period of time due to
    the provided reason.
    """

    resource_type = Field("HealthcareServiceNotAvailable", const=True)

    description: fhirtypes.String = Field(
        ...,
        alias="description",
        title="Reason presented to the user explaining why time not available",
        description=(
            "The reason that can be presented to the user as to why this time is "
            "not available."
        ),
    )

    during: fhirtypes.PeriodType = Field(
        None,
        alias="during",
        title="Service not available from this date",
        description=(
            "Service is not available (seasonally or for a public holiday) from "
            "this date."
        ),
    )


class HealthcareServiceServiceType(backboneelement.BackboneElement):
    """Specific service delivered or performed.

    A specific type of service that may be delivered or performed.
    """

    resource_type = Field("HealthcareServiceEligibility", const=True)

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Specialties handled by the Service Site.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Type of service delivered or performed.",
    )
