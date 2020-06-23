# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Schedule
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class Schedule(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A container for slots of time that may be available for booking
    appointments.
    """

    resource_type = Field("Schedule", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Type `bool`",
        description="Whether this schedule is in active use",
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    actor: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="actor",
        title=(
            "List of `Reference` items referencing `Patient, Practitioner, "
            "PractitionerRole, RelatedPerson, Device, HealthcareService, Location` "
            "(represented as `dict` in JSON)"
        ),
        description="Resource(s) that availability information is being provided for",
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String`",
        description="Comments on availability",
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Ids for this item",
    )

    planningHorizon: fhirtypes.PeriodType = Field(
        None,
        alias="planningHorizon",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period of time covered by schedule",
    )

    serviceCategory: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceCategory",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="High-level category",
    )

    serviceType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Specific service",
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Type of specialty needed",
    )
