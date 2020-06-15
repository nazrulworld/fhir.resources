# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Appointment
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Appointment(domainresource.DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """

    resource_type = Field("Appointment", const=True)

    appointmentType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="appointmentType",
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

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="The date that this appointment was initially created",
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

    incomingReferral: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="incomingReferral",
        title=(
            "List of `Reference` items referencing `ReferralRequest` (represented "
            "as `dict` in JSON)"
        ),
        description=(
            "The ReferralRequest provided as information to allocate to the "
            "Encounter"
        ),
    )

    indication: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="indication",
        title=(
            "List of `Reference` items referencing `Condition, Procedure` "
            "(represented as `dict` in JSON)"
        ),
        description="Reason the appointment is to takes place (resource)",
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

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Reason this appointment is scheduled",
    )

    requestedPeriod: ListType[fhirtypes.PeriodType] = Field(
        None,
        alias="requestedPeriod",
        title="List of `Period` items (represented as `dict` in JSON)",
        description=(
            "Potential date/time interval(s) requested to allocate the appointment "
            "within"
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
        description="The specific service that is to be performed during this appointment",
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

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title=(
            "List of `Reference` items referencing `Resource` (represented as "
            "`dict` in JSON)"
        ),
        description="Additional information to support the appointment",
    )


class AppointmentParticipant(backboneelement.BackboneElement):
    """ Participants involved in appointment.
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
