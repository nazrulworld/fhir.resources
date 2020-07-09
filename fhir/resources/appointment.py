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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """

    resource_type = Field("Appointment", const=True)

    appointmentType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="appointmentType",
        title=(
            "The style of appointment or patient that has been booked in the slot "
            "(not service type)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="The service request this appointment is allocated to assess",
        description=(
            "The service request this appointment is allocated to assess (e.g. "
            "incoming referral or procedure request)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ServiceRequest"],
    )

    cancelationReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="cancelationReason",
        title="The coded reason for the appointment being cancelled",
        description=(
            "The coded reason for the appointment being cancelled. This is often "
            "used in reporting/billing/futher processing to determine if further "
            "actions are required, or specific fees apply."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Additional comments",
        description="Additional comments about the appointment.",
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="The date that this appointment was initially created",
        description=(
            "The date that this appointment was initially created. This could be "
            "different to the meta.lastModified value on the initial entry, as this"
            " could have been before the resource was created on the FHIR server, "
            "and should remain unchanged over the lifespan of the appointment."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Shown on a subject line in a meeting request, or appointment list",
        description=(
            "The brief description of the appointment as would be shown on a "
            "subject line in a meeting request, or appointment list. Detailed or "
            "expanded information should be put in the comment field."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    end: fhirtypes.Instant = Field(
        None,
        alias="end",
        title="When appointment is to conclude",
        description="Date/Time that the appointment is to conclude.",
        # if property is element of this resource.
        element_property=True,
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Ids for this item",
        description=(
            "This records identifiers associated with this appointment concern that"
            " are defined by business processes and/or used to refer to it when a "
            "direct URL reference to the resource itself is not appropriate (e.g. "
            "in CDA documents, or in written / printed documentation)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    minutesDuration: fhirtypes.PositiveInt = Field(
        None,
        alias="minutesDuration",
        title="Can be less than start/end (e.g. estimate)",
        description=(
            "Number of minutes that the appointment is to take. This can be less "
            "than the duration between the start and end times.  For example, where"
            " the actual time of appointment is only an estimate or if a 30 minute "
            "appointment is being requested, but any time would work.  Also, if "
            "there is, for example, a planned 15 minute break in the middle of a "
            "long appointment, the duration may be 15 minutes less than the "
            "difference between the start and end."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    minutesDuration__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_minutesDuration", title="Extension field for ``minutesDuration``."
    )

    participant: ListType[fhirtypes.AppointmentParticipantType] = Field(
        ...,
        alias="participant",
        title="Participants involved in appointment",
        description="List of participants involved in the appointment.",
        # if property is element of this resource.
        element_property=True,
    )

    patientInstruction: fhirtypes.String = Field(
        None,
        alias="patientInstruction",
        title="Detailed information and instructions for the patient",
        description=(
            "While Appointment.comment contains information for internal use, "
            "Appointment.patientInstructions is used to capture patient facing "
            "information about the Appointment (e.g. please bring your referral or "
            "fast from 8pm night before)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    patientInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_patientInstruction",
        title="Extension field for ``patientInstruction``.",
    )

    priority: fhirtypes.UnsignedInt = Field(
        None,
        alias="priority",
        title="Used to make informed decisions if needing to re-prioritize",
        description=(
            "The priority of the appointment. Can be used to make informed "
            "decisions if needing to re-prioritize appointments. (The iCal Standard"
            " specifies 0 as undefined, 1 as highest, 9 as lowest priority)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Coded reason this appointment is scheduled",
        description=(
            "The coded reason that this appointment is being scheduled. This is "
            "more clinical than administrative."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Reason the appointment is to take place (resource)",
        description=(
            "Reason the appointment has been scheduled to take place, as specified "
            "using information from another resource. When the patient arrives and "
            "the encounter begins it may be used as the admission diagnosis. The "
            "indication will typically be a Condition (with other resources "
            "referenced in the evidence.detail), or a Procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Procedure",
            "Observation",
            "ImmunizationRecommendation",
        ],
    )

    requestedPeriod: ListType[fhirtypes.PeriodType] = Field(
        None,
        alias="requestedPeriod",
        title=(
            "Potential date/time interval(s) requested to allocate the appointment "
            "within"
        ),
        description=(
            "A set of date ranges (potentially including times) that the "
            "appointment is preferred to be scheduled within.  The duration "
            "(usually in minutes) could also be provided to indicate the length of "
            "the appointment to fill and populate the start/end times for the "
            "actual allocated time. However, in other situations the duration may "
            "be calculated by the scheduling system."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    serviceCategory: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceCategory",
        title=(
            "A broad categorization of the service that is to be performed during "
            "this appointment"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    serviceType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceType",
        title="The specific service that is to be performed during this appointment",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    slot: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="slot",
        title="The slots that this appointment is filling",
        description=(
            "The slots from the participants' schedules that will be filled by the "
            "appointment."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Slot"],
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
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

    start: fhirtypes.Instant = Field(
        None,
        alias="start",
        title="When appointment is to take place",
        description="Date/Time that the appointment is to take place.",
        # if property is element of this resource.
        element_property=True,
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "proposed | pending | booked | arrived | fulfilled | cancelled | noshow"
            " | entered-in-error | checked-in | waitlist"
        ),
        description=(
            "The overall status of the Appointment. Each of the participants has "
            "their own participation status which indicates their involvement in "
            "the process, however this status indicates the shared status."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "proposed",
            "pending",
            "booked",
            "arrived",
            "fulfilled",
            "cancelled",
            "noshow",
            "entered-in-error",
            "checked-in",
            "waitlist",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title="Additional information to support the appointment",
        description=(
            "Additional information to support the appointment provided when making"
            " the appointment."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )


class AppointmentParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Participants involved in appointment.
    List of participants involved in the appointment.
    """

    resource_type = Field("AppointmentParticipant", const=True)

    actor: fhirtypes.ReferenceType = Field(
        None,
        alias="actor",
        title="Person, Location/HealthcareService or Device",
        description=(
            "A Person, Location/HealthcareService or Device that is participating "
            "in the appointment."
        ),
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

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Participation period of the actor",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    required: fhirtypes.Code = Field(
        None,
        alias="required",
        title="required | optional | information-only",
        description=(
            "Whether this participant is required to be present at the meeting. "
            "This covers a use-case where two doctors need to meet to discuss the "
            "results for a specific patient, and the patient is not required to be "
            "present."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["required", "optional", "information-only"],
    )
    required__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_required", title="Extension field for ``required``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="accepted | declined | tentative | needs-action",
        description="Participation status of the actor.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["accepted", "declined", "tentative", "needs-action"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Role of participant in the appointment",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
