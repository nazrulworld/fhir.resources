from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Appointment
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Appointment(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """

    __resource_type__ = "Appointment"

    account: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="account",
        title="The set of accounts that may be used for billing for this Appointment",
        description=(
            "The set of accounts that is expected to be used for billing the "
            "activities that result from this Appointment."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Account"],
        },
    )

    appointmentType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="appointmentType",
        title=(
            "The style of appointment or patient that has been booked in the slot "
            "(not service type)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="The request this appointment is allocated to assess",
        description=(
            "The request this appointment is allocated to assess (e.g. incoming "
            "referral or procedure request)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CarePlan",
                "DeviceRequest",
                "MedicationRequest",
                "ServiceRequest",
            ],
        },
    )

    cancellationDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="cancellationDate",
        title="When the appointment was cancelled",
        description="The date/time describing when the appointment was cancelled.",
        json_schema_extra={
            "element_property": True,
        },
    )
    cancellationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_cancellationDate",
        title="Extension field for ``cancellationDate``.",
    )

    cancellationReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="cancellationReason",
        title="The coded reason for the appointment being cancelled",
        description=(
            "The coded reason for the appointment being cancelled. This is often "
            "used in reporting/billing/futher processing to determine if further "
            "actions are required, or specific fees apply."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    class_fhir: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="class",
        title="Classification when becoming an encounter",
        description=(
            "Concepts representing classification of patient encounter such as "
            "ambulatory (outpatient), inpatient, emergency, home health or others "
            "due to local variations."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="created",
        title="The date that this appointment was initially created",
        description=(
            "The date that this appointment was initially created. This could be "
            "different to the meta.lastModified value on the initial entry, as this"
            " could have been before the resource was created on the FHIR server, "
            "and should remain unchanged over the lifespan of the appointment."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_created", title="Extension field for ``created``."
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Shown on a subject line in a meeting request, or appointment list",
        description=(
            "The brief description of the appointment as would be shown on a "
            "subject line in a meeting request, or appointment list. Detailed or "
            "expanded information should be put in the note field."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    end: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="end",
        title="When appointment is to conclude",
        description="Date/Time that the appointment is to conclude.",
        json_schema_extra={
            "element_property": True,
        },
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_end", title="Extension field for ``end``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External Ids for this item",
        description=(
            "This records identifiers associated with this appointment concern that"
            " are defined by business processes and/or used to refer to it when a "
            "direct URL reference to the resource itself is not appropriate (e.g. "
            "in CDA documents, or in written / printed documentation)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    minutesDuration: fhirtypes.PositiveIntType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )
    minutesDuration__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_minutesDuration", title="Extension field for ``minutesDuration``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Additional comments",
        description="Additional notes/comments about the appointment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    occurrenceChanged: bool | None = Field(  # type: ignore
        None,
        alias="occurrenceChanged",
        title="Indicates that this appointment varies from a recurrence pattern",
        description="This appointment varies from the recurring pattern.",
        json_schema_extra={
            "element_property": True,
        },
    )
    occurrenceChanged__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_occurrenceChanged",
        title="Extension field for ``occurrenceChanged``.",
    )

    originatingAppointment: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="originatingAppointment",
        title="The originating appointment in a recurring set of appointments",
        description=(
            "The originating appointment in a recurring set of related " "appointments."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Appointment"],
        },
    )

    participant: typing.List[fhirtypes.AppointmentParticipantType] = Field(  # type: ignore
        ...,
        alias="participant",
        title="Participants involved in appointment",
        description="List of participants involved in the appointment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    patientInstruction: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="patientInstruction",
        title="Detailed information and instructions for the patient",
        description=(
            "While Appointment.note contains information for internal use, "
            "Appointment.patientInstructions is used to capture patient facing "
            "information about the Appointment (e.g. please bring your referral or "
            "fast from 8pm night before)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference", "Binary", "Communication"],
        },
    )

    previousAppointment: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="previousAppointment",
        title="The previous appointment in a series",
        description="The previous appointment in a series of related appointments.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Appointment"],
        },
    )

    priority: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="Used to make informed decisions if needing to re-prioritize",
        description=(
            "The priority of the appointment. Can be used to make informed "
            "decisions if needing to re-prioritize appointments. (The iCal Standard"
            " specifies 0 as undefined, 1 as highest, 9 as lowest priority)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Reason this appointment is scheduled",
        description=(
            "The reason that this appointment is being scheduled. This is more "
            "clinical than administrative. This can be coded, or as specified using"
            " information from another resource. When the patient arrives and the "
            "encounter begins it may be used as the admission diagnosis. The "
            "indication will typically be a Condition (with other resources "
            "referenced in the evidence.detail), or a Procedure."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Condition",
                "Procedure",
                "Observation",
                "ImmunizationRecommendation",
            ],
        },
    )

    recurrenceId: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="recurrenceId",
        title="The sequence number in the recurrence",
        description=(
            "The sequence number that identifies a specific appointment in a "
            "recurring pattern."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    recurrenceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_recurrenceId", title="Extension field for ``recurrenceId``."
    )

    recurrenceTemplate: typing.List[fhirtypes.AppointmentRecurrenceTemplateType] | None = Field(  # type: ignore
        None,
        alias="recurrenceTemplate",
        title=(
            "Details of the recurrence pattern/template used to generate " "occurrences"
        ),
        description=(
            "The details of the recurrence pattern or template that is used to "
            "generate recurring appointments."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    replaces: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="replaces",
        title="Appointment replaced by this Appointment",
        description=(
            "Appointment replaced by this Appointment in cases where there is a "
            "cancellation, the details of the cancellation can be found in the "
            "cancellationReason property (on the referenced resource)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Appointment"],
        },
    )

    requestedPeriod: typing.List[fhirtypes.PeriodType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    serviceCategory: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="serviceCategory",
        title=(
            "A broad categorization of the service that is to be performed during "
            "this appointment"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    serviceType: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="serviceType",
        title="The specific service that is to be performed during this appointment",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["HealthcareService"],
        },
    )

    slot: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="slot",
        title="The slots that this appointment is filling",
        description=(
            "The slots from the participants' schedules that will be filled by the "
            "appointment."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Slot"],
        },
    )

    specialty: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="specialty",
        title=(
            "The specialty of a practitioner that would be required to perform the "
            "service requested in this appointment"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    start: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="start",
        title="When appointment is to take place",
        description="Date/Time that the appointment is to take place.",
        json_schema_extra={
            "element_property": True,
        },
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_start", title="Extension field for ``start``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
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
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
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
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subject",
        title="The patient or group associated with the appointment",
        description=(
            "The patient or group associated with the appointment, if they are to "
            "be present (usually) then they should also be included in the "
            "participant backbone element."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    supportingInformation: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supportingInformation",
        title="Additional information to support the appointment",
        description=(
            "Additional information to support the appointment provided when making"
            " the appointment."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    virtualService: typing.List[fhirtypes.VirtualServiceDetailType] | None = Field(  # type: ignore
        None,
        alias="virtualService",
        title="Connection details of a virtual service (e.g. conference call)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Appointment`` according specification,
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
            "status",
            "cancellationReason",
            "class",
            "serviceCategory",
            "serviceType",
            "specialty",
            "appointmentType",
            "reason",
            "priority",
            "description",
            "replaces",
            "virtualService",
            "supportingInformation",
            "previousAppointment",
            "originatingAppointment",
            "start",
            "end",
            "minutesDuration",
            "requestedPeriod",
            "slot",
            "account",
            "created",
            "cancellationDate",
            "note",
            "patientInstruction",
            "basedOn",
            "subject",
            "participant",
            "recurrenceId",
            "occurrenceChanged",
            "recurrenceTemplate",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class AppointmentParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Participants involved in appointment.
    List of participants involved in the appointment.
    """

    __resource_type__ = "AppointmentParticipant"

    actor: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="actor",
        title=(
            "The individual, device, location, or service participating in the "
            "appointment"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Group",
                "Practitioner",
                "PractitionerRole",
                "CareTeam",
                "RelatedPerson",
                "Device",
                "HealthcareService",
                "Location",
            ],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Participation period of the actor",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    required: bool | None = Field(  # type: ignore
        None,
        alias="required",
        title="The participant is required to attend (optional when false)",
        description=(
            "Whether this participant is required to be present at the meeting. If "
            "false, the participant is optional."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    required__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_required", title="Extension field for ``required``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="accepted | declined | tentative | needs-action",
        description="Participation status of the actor.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["accepted", "declined", "tentative", "needs-action"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="Role of participant in the appointment",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AppointmentParticipant`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "period",
            "actor",
            "required",
            "status",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class AppointmentRecurrenceTemplate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of the recurrence pattern/template used to generate occurrences.
    The details of the recurrence pattern or template that is used to generate
    recurring appointments.
    """

    __resource_type__ = "AppointmentRecurrenceTemplate"

    excludingDate: typing.List[fhirtypes.DateType | None] | None = Field(  # type: ignore
        None,
        alias="excludingDate",
        title="Any dates that should be excluded from the series",
        description=(
            "Any dates, such as holidays, that should be excluded from the "
            "recurrence."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    excludingDate__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_excludingDate", title="Extension field for ``excludingDate``."
    )

    excludingRecurrenceId: typing.List[fhirtypes.PositiveIntType | None] | None = Field(  # type: ignore
        None,
        alias="excludingRecurrenceId",
        title="Any recurrence IDs that should be excluded from the recurrence",
        description=(
            "Any dates, such as holidays, that should be excluded from the "
            "recurrence."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    excludingRecurrenceId__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_excludingRecurrenceId",
        title="Extension field for ``excludingRecurrenceId``.",
    )

    lastOccurrenceDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="lastOccurrenceDate",
        title="The date when the recurrence should end",
        description="Recurring appointments will not occur after this date.",
        json_schema_extra={
            "element_property": True,
        },
    )
    lastOccurrenceDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_lastOccurrenceDate",
        title="Extension field for ``lastOccurrenceDate``.",
    )

    monthlyTemplate: fhirtypes.AppointmentRecurrenceTemplateMonthlyTemplateType | None = Field(  # type: ignore
        None,
        alias="monthlyTemplate",
        title="Information about monthly recurring appointments",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    occurrenceCount: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="occurrenceCount",
        title="The number of planned occurrences",
        description="How many appointments are planned in the recurrence.",
        json_schema_extra={
            "element_property": True,
        },
    )
    occurrenceCount__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_occurrenceCount", title="Extension field for ``occurrenceCount``."
    )

    occurrenceDate: typing.List[fhirtypes.DateType | None] | None = Field(  # type: ignore
        None,
        alias="occurrenceDate",
        title="Specific dates for a recurring set of appointments (no template)",
        description="The list of specific dates that will have appointments generated.",
        json_schema_extra={
            "element_property": True,
        },
    )
    occurrenceDate__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_occurrenceDate", title="Extension field for ``occurrenceDate``."
    )

    recurrenceType: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="recurrenceType",
        title="The frequency of the recurrence",
        description="How often the appointment series should recur.",
        json_schema_extra={
            "element_property": True,
        },
    )

    timezone: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="timezone",
        title="The timezone of the occurrences",
        description="The timezone of the recurring appointment occurrences.",
        json_schema_extra={
            "element_property": True,
        },
    )

    weeklyTemplate: fhirtypes.AppointmentRecurrenceTemplateWeeklyTemplateType | None = Field(  # type: ignore
        None,
        alias="weeklyTemplate",
        title="Information about weekly recurring appointments",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    yearlyTemplate: fhirtypes.AppointmentRecurrenceTemplateYearlyTemplateType | None = Field(  # type: ignore
        None,
        alias="yearlyTemplate",
        title="Information about yearly recurring appointments",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AppointmentRecurrenceTemplate`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "timezone",
            "recurrenceType",
            "lastOccurrenceDate",
            "occurrenceCount",
            "occurrenceDate",
            "weeklyTemplate",
            "monthlyTemplate",
            "yearlyTemplate",
            "excludingDate",
            "excludingRecurrenceId",
        ]


class AppointmentRecurrenceTemplateMonthlyTemplate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about monthly recurring appointments.
    """

    __resource_type__ = "AppointmentRecurrenceTemplateMonthlyTemplate"

    dayOfMonth: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="dayOfMonth",
        title="Recurs on a specific day of the month",
        description=(
            "Indicates that appointments in the series of recurring appointments "
            "should occur on a specific day of the month."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    dayOfMonth__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_dayOfMonth", title="Extension field for ``dayOfMonth``."
    )

    dayOfWeek: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="dayOfWeek",
        title="Indicates which day of the week the appointment should occur",
        description=(
            "Indicates which day of the week the recurring appointments should "
            "occur each nth week."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    monthInterval: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="monthInterval",
        title="Recurs every nth month",
        description="Indicates that recurring appointments should occur every nth month.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    monthInterval__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_monthInterval", title="Extension field for ``monthInterval``."
    )

    nthWeekOfMonth: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="nthWeekOfMonth",
        title="Indicates which week of the month the appointment should occur",
        description=(
            "Indicates which week within a month the appointments in the series of "
            "recurring appointments should occur on."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AppointmentRecurrenceTemplateMonthlyTemplate`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "dayOfMonth",
            "nthWeekOfMonth",
            "dayOfWeek",
            "monthInterval",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("monthInterval", "monthInterval__ext")]
        return required_fields


class AppointmentRecurrenceTemplateWeeklyTemplate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about weekly recurring appointments.
    """

    __resource_type__ = "AppointmentRecurrenceTemplateWeeklyTemplate"

    friday: bool | None = Field(  # type: ignore
        None,
        alias="friday",
        title="Recurs on Friday",
        description="Indicates that recurring appointments should occur on Fridays.",
        json_schema_extra={
            "element_property": True,
        },
    )
    friday__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_friday", title="Extension field for ``friday``."
    )

    monday: bool | None = Field(  # type: ignore
        None,
        alias="monday",
        title="Recurs on Mondays",
        description="Indicates that recurring appointments should occur on Mondays.",
        json_schema_extra={
            "element_property": True,
        },
    )
    monday__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_monday", title="Extension field for ``monday``."
    )

    saturday: bool | None = Field(  # type: ignore
        None,
        alias="saturday",
        title="Recurs on Saturday",
        description="Indicates that recurring appointments should occur on Saturdays.",
        json_schema_extra={
            "element_property": True,
        },
    )
    saturday__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_saturday", title="Extension field for ``saturday``."
    )

    sunday: bool | None = Field(  # type: ignore
        None,
        alias="sunday",
        title="Recurs on Sunday",
        description="Indicates that recurring appointments should occur on Sundays.",
        json_schema_extra={
            "element_property": True,
        },
    )
    sunday__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sunday", title="Extension field for ``sunday``."
    )

    thursday: bool | None = Field(  # type: ignore
        None,
        alias="thursday",
        title="Recurs on Thursday",
        description="Indicates that recurring appointments should occur on Thursdays.",
        json_schema_extra={
            "element_property": True,
        },
    )
    thursday__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_thursday", title="Extension field for ``thursday``."
    )

    tuesday: bool | None = Field(  # type: ignore
        None,
        alias="tuesday",
        title="Recurs on Tuesday",
        description="Indicates that recurring appointments should occur on Tuesdays.",
        json_schema_extra={
            "element_property": True,
        },
    )
    tuesday__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_tuesday", title="Extension field for ``tuesday``."
    )

    wednesday: bool | None = Field(  # type: ignore
        None,
        alias="wednesday",
        title="Recurs on Wednesday",
        description="Indicates that recurring appointments should occur on Wednesdays.",
        json_schema_extra={
            "element_property": True,
        },
    )
    wednesday__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_wednesday", title="Extension field for ``wednesday``."
    )

    weekInterval: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="weekInterval",
        title="Recurs every nth week",
        description=(
            "The interval defines if the recurrence is every nth week. The default "
            "is every week, so it is expected that this value will be 2 or more.  "
            "e.g. For recurring every second week this interval would be 2, or "
            "every third week the interval would be 3."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    weekInterval__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_weekInterval", title="Extension field for ``weekInterval``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AppointmentRecurrenceTemplateWeeklyTemplate`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
            "weekInterval",
        ]


class AppointmentRecurrenceTemplateYearlyTemplate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about yearly recurring appointments.
    """

    __resource_type__ = "AppointmentRecurrenceTemplateYearlyTemplate"

    yearInterval: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="yearInterval",
        title="Recurs every nth year",
        description="Appointment recurs every nth year.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    yearInterval__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_yearInterval", title="Extension field for ``yearInterval``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AppointmentRecurrenceTemplateYearlyTemplate`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "yearInterval"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("yearInterval", "yearInterval__ext")]
        return required_fields
