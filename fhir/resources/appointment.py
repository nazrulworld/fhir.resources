# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Appointment
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
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
        description="The style of appointment or patient that has been booked in the slot (not service type)",
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="List of `Reference` items referencing `ServiceRequest` (represented as `dict` in JSON)",
        description="The service request this appointment is allocated to assess",
    )

    cancelationReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="cancelationReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The coded reason for the appointment being cancelled",
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

    patientInstruction: fhirtypes.String = Field(
        None,
        alias="patientInstruction",
        title="Type `String` (represented as `dict` in JSON)",
        description="Detailed information and instructions for the patient",
    )

    priority: fhirtypes.UnsignedInt = Field(
        None,
        alias="priority",
        title="Type `UnsignedInt` (represented as `dict` in JSON)",
        description="Used to make informed decisions if needing to re-prioritize",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Coded reason this appointment is scheduled",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="List of `Reference` items referencing `Condition, Procedure, Observation, ImmunizationRecommendation` (represented as `dict` in JSON)",
        description="Reason the appointment is to take place (resource)",
    )

    requestedPeriod: ListType[fhirtypes.PeriodType] = Field(
        None,
        alias="requestedPeriod",
        title="List of `Period` items (represented as `dict` in JSON)",
        description="Potential date/time interval(s) requested to allocate the appointment within",
    )

    serviceCategory: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceCategory",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="A broad categorization of the service that is to be performed during this appointment",
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
        title="List of `Reference` items referencing `Slot` (represented as `dict` in JSON)",
        description="The slots that this appointment is filling",
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The specialty of a practitioner that would be required to perform the service requested in this appointment",
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
        description="proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist",
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
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
        title="Type `Reference` referencing `Patient, Practitioner, PractitionerRole, RelatedPerson, Device, HealthcareService, Location` (represented as `dict` in JSON)",
        description="Person, Location/HealthcareService or Device",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Participation period of the actor",
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
