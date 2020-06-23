# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Slot
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class Slot(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A slot of time on a schedule that may be available for booking appointments.
    """

    resource_type = Field("Slot", const=True)

    appointmentType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="appointmentType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "The style of appointment or patient that may be booked in the slot "
            "(not service type)"
        ),
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String`",
        description=(
            "Comments on the slot to describe any extended information. Such as "
            "custom constraints on the slot"
        ),
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    end: fhirtypes.Instant = Field(
        ...,
        alias="end",
        title="Type `Instant`",
        description="Date/Time that the slot is to conclude",
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Ids for this item",
    )

    overbooked: bool = Field(
        None,
        alias="overbooked",
        title="Type `bool`",
        description=(
            "This slot has already been overbooked, appointments are unlikely to be"
            " accepted for this time"
        ),
    )
    overbooked__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_overbooked", title="Extension field for ``overbooked``."
    )

    schedule: fhirtypes.ReferenceType = Field(
        ...,
        alias="schedule",
        title=(
            "Type `Reference` referencing `Schedule` (represented as `dict` in " "JSON)"
        ),
        description=(
            "The schedule resource that this slot defines an interval of status "
            "information"
        ),
    )

    serviceCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="serviceCategory",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "A broad categorisation of the service that is to be performed during "
            "this appointment"
        ),
    )

    serviceType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "The type of appointments that can be booked into this slot (ideally "
            "this would be an identifiable service - which is at a location, rather"
            " than the location itself). If provided then this overrides the value "
            "provided on the availability resource"
        ),
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "The specialty of a practitioner that would be required to perform the "
            "service requested in this appointment"
        ),
    )

    start: fhirtypes.Instant = Field(
        ...,
        alias="start",
        title="Type `Instant`",
        description="Date/Time that the slot is to begin",
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="busy | free | busy-unavailable | busy-tentative | entered-in-error",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )
