# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Appointment
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Appointment(DomainResource):
    """A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """

    resource_type = Field("Appointment", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "The style of appointment or patient that has been booked in the slot "
            "(not service type)"
        ),
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional comments",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Shown on a subject line in a meeting request, or appointment list",
    )

    end: fhirtypes.Instant = Field(
        None,
        alias="end",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="When appointment is to conclude",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Ids for this item",
    )

    minutesDuration: fhirtypes.PositiveInt = Field(
        None,
        alias="minutesDuration",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Can be less than start/end (e.g. estimate)",
    )

    participant: ListType[fhirtypes.AppointmentParticipantType] = Field(
        ...,
        alias="participant",
        title="List of `AppointmentParticipant` items (represented as `dict` in JSON)",
        description="Participants involved in appointment",
    )

    priority: fhirtypes.UnsignedInt = Field(
        None,
        alias="priority",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Used to make informed decisions if needing to re-prioritize",
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="CodeableConcept` (represented as `dict` in JSON)",
        description="Reason this appointment is scheduled",
    )

    slot: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="slot",
        title=(
            "List of `Reference` items referencing `Slot` (represented as `dict` in"
            " JSON)"
        ),
        description="The slots that this appointment is filling",
    )

    start: fhirtypes.Instant = Field(
        None,
        alias="start",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="When appointment is to take place",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "proposed | pending | booked | arrived | fulfilled | cancelled | noshow"
            " | entered-in-error"
        ),
    )


class AppointmentParticipant(BackboneElement):
    """Participants involved in appointment.

    List of participants involved in the appointment.
    """

    resource_type = Field("AppointmentParticipant", const=True)

    actor: fhirtypes.ReferenceType = Field(
        None,
        alias="actor",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, RelatedPerson, "
            "Device, HealthcareService, Location` (represented as `dict` in JSON)"
        ),
        description="Person, Location/HealthcareService or Device",
    )

    required: fhirtypes.Code = Field(
        None,
        alias="required",
        title="Type `Code` (represented as `dict` in JSON)",
        description="required | optional | information-only",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="accepted | declined | tentative | needs-action",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Role of participant in the appointment",
    )
