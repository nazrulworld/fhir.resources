# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Schedule
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field

from . import domainresource, fhirtypes


class Schedule(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A container for slots of time that may be available for booking
    appointments.
    """

    resource_type = Field("Schedule", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this schedule is in active use",
        description=(
            "Whether this schedule record is in active use or should not be used "
            "(such as was entered in error)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    actor: typing.List[fhirtypes.ReferenceType] = Field(
        ...,
        alias="actor",
        title="Resource(s) that availability information is being provided for",
        description=(
            "Slots that reference this schedule resource provide the availability "
            "details to these referenced resource(s)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "CareTeam",
            "RelatedPerson",
            "Device",
            "HealthcareService",
            "Location",
        ],
    )

    comment: fhirtypes.Markdown = Field(
        None,
        alias="comment",
        title="Comments on availability",
        description=(
            "Comments on the availability to describe any extended information. "
            "Such as custom constraints on the slots that may be associated."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Ids for this item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Human-readable label",
        description=(
            "Further description of the schedule as it would be presented to a "
            "consumer while searching."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    planningHorizon: fhirtypes.PeriodType = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    serviceCategory: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceCategory",
        title="High-level category",
        description=(
            "A broad categorization of the service that is to be performed during "
            "this appointment."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    serviceType: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="serviceType",
        title="Specific service",
        description="The specific service that is to be performed during this appointment.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["HealthcareService"],
    )

    specialty: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="Type of specialty needed",
        description=(
            "The specialty of a practitioner that would be required to perform the "
            "service requested in this appointment."
        ),
        # if property is element of this resource.
        element_property=True,
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
            "name",
            "actor",
            "planningHorizon",
            "comment",
        ]
