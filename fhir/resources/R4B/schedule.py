from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Schedule
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class Schedule(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A container for slots of time that may be available for booking
    appointments.
    """

    __resource_type__ = "Schedule"

    active: bool | None = Field(  # type: ignore
        None,
        alias="active",
        title="Whether this schedule is in active use",
        description=(
            "Whether this schedule record is in active use or should not be used "
            "(such as was entered in error)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_active", title="Extension field for ``active``."
    )

    actor: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        ...,
        alias="actor",
        title="Resource(s) that availability information is being provided for",
        description=(
            "Slots that reference this schedule resource provide the availability "
            "details to these referenced resource(s)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
                "Device",
                "HealthcareService",
                "Location",
            ],
        },
    )

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Comments on availability",
        description=(
            "Comments on the availability to describe any extended information. "
            "Such as custom constraints on the slots that may be associated."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External Ids for this item",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    planningHorizon: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="planningHorizon",
        title="Period of time covered by schedule",
        description=(
            "The period of time that the slots that reference this Schedule "
            "resource cover (even if none exist). These  cover the amount of time "
            "that an organization's planning horizon; the interval for which they "
            "are currently accepting appointments. This does not define a "
            '"template" for planning outside these dates.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    serviceCategory: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="serviceCategory",
        title="High-level category",
        description=(
            "A broad categorization of the service that is to be performed during "
            "this appointment."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    serviceType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="serviceType",
        title="Specific service",
        description="The specific service that is to be performed during this appointment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    specialty: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="specialty",
        title="Type of specialty needed",
        description=(
            "The specialty of a practitioner that would be required to perform the "
            "service requested in this appointment."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Schedule`` according specification,
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
            "serviceCategory",
            "serviceType",
            "specialty",
            "actor",
            "planningHorizon",
            "comment",
        ]
