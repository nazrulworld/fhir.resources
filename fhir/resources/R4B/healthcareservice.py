from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/HealthcareService
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
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

    availabilityExceptions: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="availabilityExceptions",
        title="Description of availability exceptions",
        description=(
            "A description of site availability exceptions, e.g. public holiday "
            "availability. Succinctly describing all possible exceptions to normal "
            "site availability as details in the available Times and not available "
            "Times."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    availabilityExceptions__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_availabilityExceptions",
        title="Extension field for ``availabilityExceptions``.",
    )

    availableTime: typing.List[fhirtypes.HealthcareServiceAvailableTimeType] | None = Field(  # type: ignore
        None,
        alias="availableTime",
        title="Times the Service Site is available",
        description="A collection of times that the Service Site is available.",
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

    comment: fhirtypes.StringType | None = Field(  # type: ignore
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

    notAvailable: typing.List[fhirtypes.HealthcareServiceNotAvailableType] | None = Field(  # type: ignore
        None,
        alias="notAvailable",
        title="Not available during this time due to provided reason",
        description=(
            "The HealthcareService is not available during this period of time due "
            "to the provided reason."
        ),
        json_schema_extra={
            "element_property": True,
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
            "Collection of specialties handled by the service site. This is more of"
            " a medical term."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    telecom: typing.List[fhirtypes.ContactPointType] | None = Field(  # type: ignore
        None,
        alias="telecom",
        title="Contacts related to the healthcare service",
        description="List of contacts related to this specific healthcare service.",
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
            "category",
            "type",
            "specialty",
            "location",
            "name",
            "comment",
            "extraDetails",
            "photo",
            "telecom",
            "coverageArea",
            "serviceProvisionCode",
            "eligibility",
            "program",
            "characteristic",
            "communication",
            "referralMethod",
            "appointmentRequired",
            "availableTime",
            "notAvailable",
            "availabilityExceptions",
            "endpoint",
        ]


class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Times the Service Site is available.
    A collection of times that the Service Site is available.
    """

    __resource_type__ = "HealthcareServiceAvailableTime"

    allDay: bool | None = Field(  # type: ignore
        None,
        alias="allDay",
        title="Always available? e.g. 24 hour service",
        description=(
            "Is this always available? (hence times are irrelevant) e.g. 24 hour "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    allDay__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_allDay", title="Extension field for ``allDay``."
    )

    availableEndTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="availableEndTime",
        title="Closing time of day (ignored if allDay = true)",
        description=(
            "The closing time of day. Note: If the AllDay flag is set, then this "
            "time is ignored."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    availableEndTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_availableEndTime",
        title="Extension field for ``availableEndTime``.",
    )

    availableStartTime: fhirtypes.TimeType | None = Field(  # type: ignore
        None,
        alias="availableStartTime",
        title="Opening time of day (ignored if allDay = true)",
        description=(
            "The opening time of day. Note: If the AllDay flag is set, then this "
            "time is ignored."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    availableStartTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_availableStartTime",
        title="Extension field for ``availableStartTime``.",
    )

    daysOfWeek: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="daysOfWeek",
        title="mon | tue | wed | thu | fri | sat | sun",
        description=(
            "Indicates which days of the week are available between the start and "
            "end Times."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
        },
    )
    daysOfWeek__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_daysOfWeek", title="Extension field for ``daysOfWeek``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``HealthcareServiceAvailableTime`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "daysOfWeek",
            "allDay",
            "availableStartTime",
            "availableEndTime",
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


class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Not available during this time due to provided reason.
    The HealthcareService is not available during this period of time due to
    the provided reason.
    """

    __resource_type__ = "HealthcareServiceNotAvailable"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Reason presented to the user explaining why time not available",
        description=(
            "The reason that can be presented to the user as to why this time is "
            "not available."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    during: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="during",
        title="Service not available from this date",
        description=(
            "Service is not available (seasonally or for a public holiday) from "
            "this date."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``HealthcareServiceNotAvailable`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "description", "during"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("description", "description__ext")]
        return required_fields
