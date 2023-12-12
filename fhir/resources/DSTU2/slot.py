# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Slot
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .domainresource import DomainResource


class Slot(DomainResource):
    """A slot of time on a schedule that may be available for booking appointments."""

    resource_type = Field("Slot", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "The style of appointment or patient that may be booked in the slot "
            "(not service type)"
        ),
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description=(
            "Comments on the slot to describe any extended information. Such as "
            "custom constraints on the slot"
        ),
    )

    end: fhirtypes.Instant = Field(
        ...,
        alias="end",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Date/Time that the slot is to conclude",
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

    start: fhirtypes.Instant = Field(
        ...,
        alias="start",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Date/Time that the slot is to begin",
    )

    freeBusyType: fhirtypes.Code = Field(
        ...,
        alias="freeBusyType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="busy | free | busy-unavailable | busy-tentative | entered-in-error",
    )
