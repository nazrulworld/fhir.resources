# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Schedule
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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

    resource_type = Field("Schedule", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this schedule is in active use",
        description=(
            "Whether this schedule record is in active use, or should not be used "
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
        title=(
            "The resource this Schedule resource is providing availability "
            "information for. These are expected to usually be one of "
            "HealthcareService, Location, Practitioner, PractitionerRole, Device, "
            "Patient or RelatedPerson"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Device",
            "HealthcareService",
            "Location",
        ],
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title=(
            "Comments on the availability to describe any extended information. "
            "Such as custom constraints on the slots that may be associated"
        ),
        description=None,
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

    planningHorizon: fhirtypes.PeriodType = Field(
        None,
        alias="planningHorizon",
        title=(
            "The period of time that the slots that are attached to this Schedule "
            "resource cover (even if none exist). These  cover the amount of time "
            "that an organization's planning horizon; the interval for which they "
            "are currently accepting appointments. This does not define a "
            '"template" for planning outside these dates'
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    serviceCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="serviceCategory",
        title=(
            "A broad categorisation of the service that is to be performed during "
            "this appointment"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    serviceType: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceType",
        title="The specific service that is to be performed during this appointment",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    specialty: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title=(
            "The specialty of a practitioner that would be required to perform the "
            "service requested in this appointment"
        ),
        description=None,
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
            "actor",
            "planningHorizon",
            "comment",
        ]
