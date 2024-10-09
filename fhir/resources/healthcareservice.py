from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/HealthcareService
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class HealthcareService(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The details of a healthcare service available at a location.
    """

    __resource_type__ = "HealthcareService"

    active: bool | None = Field(  # type: ignore
        None,
        alias="active",
        title="Whether this HealthcareService record is in active use",
        description=(
            "This flag is used to mark the record to not be used. This is not used "
            "when a center is closed for maintenance, or for holidays, the "
            "notAvailable period is to be used for this."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_active", title="Extension field for ``active``."
    )

    appointmentRequired: bool | None = Field(  # type: ignore
        None,
        alias="appointmentRequired",
        title="If an appointment is required for access to this service",
        description=(
            "Indicates whether or not a prospective consumer will require an "
            "appointment for a particular service at a site to be provided by the "
            "Organization. Indicates if an appointment is required for access to "
            "this service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    appointmentRequired__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_appointmentRequired",
        title="Extension field for ``appointmentRequired``.",
    )

    availability: typing.List[fhirtypes.AvailabilityType] | None = Field(  # type: ignore
        None,
        alias="availability",
        title="Times the healthcare service is available (including exceptions)",
        description="A collection of times that the healthcare service is available.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="Broad category of service being performed or delivered",
        description="Identifies the broad category of service being performed or delivered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    characteristic: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="characteristic",
        title="Collection of characteristics (attributes)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    comment: fhirtypes.MarkdownType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    communication: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="communication",
        title="The language that this service is offered in",
        description=(
            "Some services are specifically made available in multiple languages, "
            "this property permits a directory to declare the languages this is "
            "offered in. Typically this is only provided where a service operates "
            "in communities with mixed languages used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ExtendedContactDetailType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Official contact details for the HealthcareService",
        description=(
            "The contact details of communication devices available relevant to the"
            " specific HealthcareService. This can include addresses, phone "
            "numbers, fax numbers, mobile numbers, email addresses and web sites."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    coverageArea: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="coverageArea",
        title="Location(s) service is intended for/available to",
        description=(
            "The location(s) that this service is available to (not where the "
            "service is provided)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    eligibility: typing.List[fhirtypes.HealthcareServiceEligibilityType] | None = Field(  # type: ignore
        None,
        alias="eligibility",
        title="Specific eligibility requirements required to use the service",
        description=(
            "Does this service have specific eligibility requirements that need to "
            "be met in order to use the service?"
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    endpoint: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="endpoint",
        title=(
            "Technical endpoints providing access to electronic services operated "
            "for the healthcare service"
        ),
        description=(
            "Technical endpoints providing access to services operated for the "
            "specific healthcare services defined at this resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Endpoint"],
        },
    )

    extraDetails: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="extraDetails",
        title=(
            "Extra details about the service that can't be placed in the other "
            "fields"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    extraDetails__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_extraDetails", title="Extension field for ``extraDetails``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External identifiers for this item",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    location: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="location",
        title="Location(s) where service may be provided",
        description="The location(s) where this healthcare service may be provided.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Description of service as presented to a consumer while searching",
        description=(
            "Further description of the service as it would be presented to a "
            "consumer while searching."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    offeredIn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="offeredIn",
        title="The service within which this service is offered",
        description=(
            "When the HealthcareService is representing a specific, schedulable "
            "service, the availableIn property can refer to a generic service."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["HealthcareService"],
        },
    )

    photo: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="photo",
        title="Facilitates quick identification of the service",
        description=(
            "If there is a photo/symbol associated with this HealthcareService, it "
            "may be included here to facilitate quick identification of the service"
            " in a list."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    program: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="program",
        title="Programs that this service is applicable to",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    providedBy: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="providedBy",
        title="Organization that provides this service",
        description="The organization that provides this healthcare service.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    referralMethod: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="referralMethod",
        title="Ways that the service accepts referrals",
        description=(
            "Ways that the service accepts referrals, if this is not provided then "
            "it is implied that no referral is required."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    serviceProvisionCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="serviceProvisionCode",
        title="Conditions under which service is available/offered",
        description=(
            "The code(s) that detail the conditions under which the healthcare "
            "service is available/offered."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    specialty: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="specialty",
        title="Specialties handled by the HealthcareService",
        description=(
            "Collection of specialties handled by the Healthcare service. This is "
            "more of a medical term."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type of service that may be delivered or performed",
        description="The specific type of service that may be delivered or performed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``HealthcareService`` according specification,
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
            "providedBy",
            "offeredIn",
            "category",
            "type",
            "specialty",
            "location",
            "name",
            "comment",
            "extraDetails",
            "photo",
            "contact",
            "coverageArea",
            "serviceProvisionCode",
            "eligibility",
            "program",
            "characteristic",
            "communication",
            "referralMethod",
            "appointmentRequired",
            "availability",
            "endpoint",
        ]


class HealthcareServiceEligibility(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specific eligibility requirements required to use the service.
    Does this service have specific eligibility requirements that need to be
    met in order to use the service?
    """

    __resource_type__ = "HealthcareServiceEligibility"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Coded value for the eligibility",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    comment: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Describes the eligibility conditions for the service",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``HealthcareServiceEligibility`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "comment"]
