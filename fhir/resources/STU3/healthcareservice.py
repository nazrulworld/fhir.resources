# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/HealthcareService
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

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
        title="Whether this healthcareservice is in active use",
        description="Whether this healthcareservice record is in active use.",
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

    availableTime: typing.List[fhirtypes.HealthcareServiceAvailableTimeType] = Field(
        None,
        alias="availableTime",
        title="Times the Service Site is available",
        description="A collection of times that the Service Site is available.",
        # if property is element of this resource.
        element_property=True,
    )

    category: fhirtypes.CodeableConceptType = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    coverageArea: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="coverageArea",
        title="Location(s) service is inteded for/available to",
        description=(
            "The location(s) that this service is available to (not where the "
            "service is provided)."
        ),
        # if property is element of this resource.
        element_property=True,
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
        # if property is element of this resource.
        element_property=True,
    )

    eligibilityNote: fhirtypes.String = Field(
        None,
        alias="eligibilityNote",
        title="Describes the eligibility conditions for the service",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    eligibilityNote__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_eligibilityNote", title="Extension field for ``eligibilityNote``."
    )

    endpoint: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "Technical endpoints providing access to services operated for the "
            "location"
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

    extraDetails: fhirtypes.String = Field(
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

    notAvailable: typing.List[fhirtypes.HealthcareServiceNotAvailableType] = Field(
        None,
        alias="notAvailable",
        title="Not available during this time due to provided reason",
        description=(
            "The HealthcareService is not available during this period of time due "
            "to the provided reason."
        ),
        # if property is element of this resource.
        element_property=True,
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

    programName: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="programName",
        title="Program Names that categorize the service",
        description="Program Names that can be used to categorize the service.",
        # if property is element of this resource.
        element_property=True,
    )
    programName__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_programName", title="Extension field for ``programName``.")

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
            "Collection of specialties handled by the service site. This is more of"
            " a medical term."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    telecom: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contacts related to the healthcare service",
        description="List of contacts related to this specific healthcare service.",
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
            "eligibilityNote",
            "programName",
            "characteristic",
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

    resource_type = Field("HealthcareServiceAvailableTime", const=True)

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

    daysOfWeek: typing.List[fhirtypes.Code] = Field(
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
    daysOfWeek__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_daysOfWeek", title="Extension field for ``daysOfWeek``.")

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


class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Not available during this time due to provided reason.
    The HealthcareService is not available during this period of time due to
    the provided reason.
    """

    resource_type = Field("HealthcareServiceNotAvailable", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Reason presented to the user explaining why time not available",
        description=(
            "The reason that can be presented to the user as to why this time is "
            "not available."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    during: fhirtypes.PeriodType = Field(
        None,
        alias="during",
        title="Service not availablefrom this date",
        description=(
            "Service is not available (seasonally or for a public holiday) from "
            "this date."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``HealthcareServiceNotAvailable`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "description", "during"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3105(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("description", "description__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
