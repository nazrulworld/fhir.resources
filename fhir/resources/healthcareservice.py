# -*- coding: utf-8 -*-
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

    resource_type = Field("HealthcareService", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this HealthcareService record is in active use",
        description=(
            "This flag is used to mark the record to not be used. This is not used "
            "when a center is closed for maintenance, or for holidays, the "
            "notAvailable period is to be used for this."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    appointmentRequired: bool = Field(
        None,
        alias="appointmentRequired",
        title="If an appointment is required for access to this service",
        description=(
            "Indicates whether or not a prospective consumer will require an "
            "appointment for a particular service at a site to be provided by the "
            "Organization. Indicates if an appointment is required for access to "
            "this service."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    appointmentRequired__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_appointmentRequired",
        title="Extension field for ``appointmentRequired``.",
    )

    availability: typing.List[fhirtypes.AvailabilityType] = Field(
        None,
        alias="availability",
        title="Times the healthcare service is available (including exceptions)",
        description="A collection of times that the healthcare service is available.",
        # if property is element of this resource.
        element_property=True,
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Broad category of service being performed or delivered",
        description="Identifies the broad category of service being performed or delivered.",
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

    comment: fhirtypes.Markdown = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    communication: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="communication",
        title="The language that this service is offered in",
        description=(
            "Some services are specifically made available in multiple languages, "
            "this property permits a directory to declare the languages this is "
            "offered in. Typically this is only provided where a service operates "
            "in communities with mixed languages used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ExtendedContactDetailType] = Field(
        None,
        alias="contact",
        title="Official contact details for the HealthcareService",
        description=(
            "The contact details of communication devices available relevant to the"
            " specific HealthcareService. This can include addresses, phone "
            "numbers, fax numbers, mobile numbers, email addresses and web sites."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    coverageArea: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="coverageArea",
        title="Location(s) service is intended for/available to",
        description=(
            "The location(s) that this service is available to (not where the "
            "service is provided)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    eligibility: typing.List[fhirtypes.HealthcareServiceEligibilityType] = Field(
        None,
        alias="eligibility",
        title="Specific eligibility requirements required to use the service",
        description=(
            "Does this service have specific eligibility requirements that need to "
            "be met in order to use the service?"
        ),
        # if property is element of this resource.
        element_property=True,
    )

    endpoint: typing.List[fhirtypes.ReferenceType] = Field(
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
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    extraDetails: fhirtypes.Markdown = Field(
        None,
        alias="extraDetails",
        title=(
            "Extra details about the service that can't be placed in the other "
            "fields"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    extraDetails__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_extraDetails", title="Extension field for ``extraDetails``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifiers for this item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    location: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="location",
        title="Location(s) where service may be provided",
        description="The location(s) where this healthcare service may be provided.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Description of service as presented to a consumer while searching",
        description=(
            "Further description of the service as it would be presented to a "
            "consumer while searching."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    offeredIn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="offeredIn",
        title="The service within which this service is offered",
        description=(
            "When the HealthcareService is representing a specific, schedulable "
            "service, the availableIn property can refer to a generic service."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["HealthcareService"],
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
        # if property is element of this resource.
        element_property=True,
    )

    program: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="program",
        title="Programs that this service is applicable to",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    providedBy: fhirtypes.ReferenceType = Field(
        None,
        alias="providedBy",
        title="Organization that provides this service",
        description="The organization that provides this healthcare service.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    referralMethod: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="referralMethod",
        title="Ways that the service accepts referrals",
        description=(
            "Ways that the service accepts referrals, if this is not provided then "
            "it is implied that no referral is required."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    serviceProvisionCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceProvisionCode",
        title="Conditions under which service is available/offered",
        description=(
            "The code(s) that detail the conditions under which the healthcare "
            "service is available/offered."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    specialty: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="Specialties handled by the HealthcareService",
        description=(
            "Collection of specialties handled by the Healthcare service. This is "
            "more of a medical term."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Type of service that may be delivered or performed",
        description="The specific type of service that may be delivered or performed.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("HealthcareServiceEligibility", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Coded value for the eligibility",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    comment: fhirtypes.Markdown = Field(
        None,
        alias="comment",
        title="Describes the eligibility conditions for the service",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``HealthcareServiceEligibility`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "comment"]
