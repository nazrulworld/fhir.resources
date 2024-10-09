from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/PractitionerRole
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class PractitionerRole(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Roles/organizations the practitioner is associated with.
    A specific set of Roles/Locations/specialties/services that a practitioner
    may perform at an organization for a period of time.
    """

    __resource_type__ = "PractitionerRole"

    active: bool | None = Field(  # type: ignore
        None,
        alias="active",
        title="Whether this practitioner's record is in active use",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_active", title="Extension field for ``active``."
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

    availableTime: typing.List[fhirtypes.PractitionerRoleAvailableTimeType] | None = Field(  # type: ignore
        None,
        alias="availableTime",
        title="Times the Service Site is available",
        description="A collection of times that the Service Site is available.",
        json_schema_extra={
            "element_property": True,
        },
    )

    code: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="code",
        title="Roles which this practitioner may perform",
        description=(
            "Roles which this practitioner is authorized to perform for the "
            "organization."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    endpoint: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="endpoint",
        title=(
            "Technical endpoints providing access to services operated for the "
            "practitioner with this role"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Endpoint"],
        },
    )

    healthcareService: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="healthcareService",
        title=(
            "The list of healthcare services that this worker provides for this "
            "role's Organization/Location(s)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["HealthcareService"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifiers that are specific to a role/location",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    location: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="location",
        title="The location(s) at which this practitioner provides care",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    notAvailable: typing.List[fhirtypes.PractitionerRoleNotAvailableType] | None = Field(  # type: ignore
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

    organization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="organization",
        title="Organization where the roles are available",
        description="The organization where the Practitioner performs the roles associated.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    practitioner: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="practitioner",
        title=(
            "Practitioner that is able to provide the defined services for the "
            "organation"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    specialty: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="specialty",
        title="Specific specialty of the practitioner",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    telecom: typing.List[fhirtypes.ContactPointType] | None = Field(  # type: ignore
        None,
        alias="telecom",
        title="Contact details that are specific to the role/location/service",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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
            "telecom",
            "availableTime",
            "notAvailable",
            "availabilityExceptions",
            "endpoint",
        ]


class PractitionerRoleAvailableTime(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Times the Service Site is available.
    A collection of times that the Service Site is available.
    """

    __resource_type__ = "PractitionerRoleAvailableTime"

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
        ``PractitionerRoleAvailableTime`` according specification,
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


class PractitionerRoleNotAvailable(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Not available during this time due to provided reason.
    The HealthcareService is not available during this period of time due to
    the provided reason.
    """

    __resource_type__ = "PractitionerRoleNotAvailable"

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
        title="Service not availablefrom this date",
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
        ``PractitionerRoleNotAvailable`` according specification,
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
