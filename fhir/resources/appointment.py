# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Appointment
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Appointment(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """

    resource_type = Field("Appointment", const=True)

    account: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="account",
        title="The set of accounts that may be used for billing for this Appointment",
        description=(
            "The set of accounts that is expected to be used for billing the "
            "activities that result from this Appointment."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Account"],
    )

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

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="The request this appointment is allocated to assess",
        description=(
            "The request this appointment is allocated to assess (e.g. incoming "
            "referral or procedure request)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "CarePlan",
            "DeviceRequest",
            "MedicationRequest",
            "ServiceRequest",
        ],
    )

    cancellationDate: fhirtypes.DateTime = Field(
        None,
        alias="cancellationDate",
        title="When the appointment was cancelled",
        description="The date/time describing when the appointment was cancelled.",
        # if property is element of this resource.
        element_property=True,
    )
    cancellationDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_cancellationDate",
        title="Extension field for ``cancellationDate``.",
    )

    cancellationReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="cancellationReason",
        title="The coded reason for the appointment being cancelled",
        description=(
            "The coded reason for the appointment being cancelled. This is often "
            "used in reporting/billing/futher processing to determine if further "
            "actions are required, or specific fees apply."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    class_fhir: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="class",
        title="Classification when becoming an encounter",
        description=(
            "Concepts representing classification of patient encounter such as "
            "ambulatory (outpatient), inpatient, emergency, home health or others "
            "due to local variations."
        ),
        # if property is element of this resource.
        element_property=True,
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
            "expanded information should be put in the note field."
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

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
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

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Additional comments",
        description="Additional notes/comments about the appointment.",
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceChanged: bool = Field(
        None,
        alias="occurrenceChanged",
        title="Indicates that this appointment varies from a recurrence pattern",
        description="This appointment varies from the recurring pattern.",
        # if property is element of this resource.
        element_property=True,
    )
    occurrenceChanged__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceChanged",
        title="Extension field for ``occurrenceChanged``.",
    )

    originatingAppointment: fhirtypes.ReferenceType = Field(
        None,
        alias="originatingAppointment",
        title="The originating appointment in a recurring set of appointments",
        description=(
            "The originating appointment in a recurring set of related " "appointments."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Appointment"],
    )

    participant: typing.List[fhirtypes.AppointmentParticipantType] = Field(
        ...,
        alias="participant",
        title="Participants involved in appointment",
        description="List of participants involved in the appointment.",
        # if property is element of this resource.
        element_property=True,
    )

    patientInstruction: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="patientInstruction",
        title="Detailed information and instructions for the patient",
        description=(
            "While Appointment.note contains information for internal use, "
            "Appointment.patientInstructions is used to capture patient facing "
            "information about the Appointment (e.g. please bring your referral or "
            "fast from 8pm night before)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference", "Binary", "Communication"],
    )

    previousAppointment: fhirtypes.ReferenceType = Field(
        None,
        alias="previousAppointment",
        title="The previous appointment in a series",
        description="The previous appointment in a series of related appointments.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Appointment"],
    )

    priority: fhirtypes.CodeableConceptType = Field(
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

    reason: typing.List[fhirtypes.CodeableReferenceType] = Field(
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

    recurrenceId: fhirtypes.PositiveInt = Field(
        None,
        alias="recurrenceId",
        title="The sequence number in the recurrence",
        description=(
            "The sequence number that identifies a specific appointment in a "
            "recurring pattern."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    recurrenceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recurrenceId", title="Extension field for ``recurrenceId``."
    )

    recurrenceTemplate: typing.List[
        fhirtypes.AppointmentRecurrenceTemplateType
    ] = Field(
        None,
        alias="recurrenceTemplate",
        title=(
            "Details of the recurrence pattern/template used to generate " "occurrences"
        ),
        description=(
            "The details of the recurrence pattern or template that is used to "
            "generate recurring appointments."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    replaces: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title="Appointment replaced by this Appointment",
        description=(
            "Appointment replaced by this Appointment in cases where there is a "
            "cancellation, the details of the cancellation can be found in the "
            "cancellationReason property (on the referenced resource)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Appointment"],
    )

    requestedPeriod: typing.List[fhirtypes.PeriodType] = Field(
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

    serviceCategory: typing.List[fhirtypes.CodeableConceptType] = Field(
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

    serviceType: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="serviceType",
        title="The specific service that is to be performed during this appointment",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["HealthcareService"],
    )

    slot: typing.List[fhirtypes.ReferenceType] = Field(
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
        # if property is element of this resource.
        element_property=True,
        element_required=True,
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

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="The patient or group associated with the appointment",
        description=(
            "The patient or group associated with the appointment, if they are to "
            "be present (usually) then they should also be included in the "
            "participant backbone element."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    supportingInformation: typing.List[fhirtypes.ReferenceType] = Field(
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

    virtualService: typing.List[fhirtypes.VirtualServiceDetailType] = Field(
        None,
        alias="virtualService",
        title="Connection details of a virtual service (e.g. conference call)",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1348(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class AppointmentParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Participants involved in appointment.
    List of participants involved in the appointment.
    """

    resource_type = Field("AppointmentParticipant", const=True)

    actor: fhirtypes.ReferenceType = Field(
        None,
        alias="actor",
        title=(
            "The individual, device, location, or service participating in the "
            "appointment"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
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
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Participation period of the actor",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    required: bool = Field(
        None,
        alias="required",
        title="The participant is required to attend (optional when false)",
        description=(
            "Whether this participant is required to be present at the meeting. If "
            "false, the participant is optional."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    required__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_required", title="Extension field for ``required``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="accepted | declined | tentative | needs-action",
        description="Participation status of the actor.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["accepted", "declined", "tentative", "needs-action"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Role of participant in the appointment",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2499(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class AppointmentRecurrenceTemplate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of the recurrence pattern/template used to generate occurrences.
    The details of the recurrence pattern or template that is used to generate
    recurring appointments.
    """

    resource_type = Field("AppointmentRecurrenceTemplate", const=True)

    excludingDate: typing.List[typing.Optional[fhirtypes.Date]] = Field(
        None,
        alias="excludingDate",
        title="Any dates that should be excluded from the series",
        description=(
            "Any dates, such as holidays, that should be excluded from the "
            "recurrence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    excludingDate__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_excludingDate", title="Extension field for ``excludingDate``."
    )

    excludingRecurrenceId: typing.List[typing.Optional[fhirtypes.PositiveInt]] = Field(
        None,
        alias="excludingRecurrenceId",
        title="Any recurrence IDs that should be excluded from the recurrence",
        description=(
            "Any dates, such as holidays, that should be excluded from the "
            "recurrence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    excludingRecurrenceId__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_excludingRecurrenceId",
        title="Extension field for ``excludingRecurrenceId``.",
    )

    lastOccurrenceDate: fhirtypes.Date = Field(
        None,
        alias="lastOccurrenceDate",
        title="The date when the recurrence should end",
        description="Recurring appointments will not occur after this date.",
        # if property is element of this resource.
        element_property=True,
    )
    lastOccurrenceDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_lastOccurrenceDate",
        title="Extension field for ``lastOccurrenceDate``.",
    )

    monthlyTemplate: fhirtypes.AppointmentRecurrenceTemplateMonthlyTemplateType = Field(
        None,
        alias="monthlyTemplate",
        title="Information about monthly recurring appointments",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceCount: fhirtypes.PositiveInt = Field(
        None,
        alias="occurrenceCount",
        title="The number of planned occurrences",
        description="How many appointments are planned in the recurrence.",
        # if property is element of this resource.
        element_property=True,
    )
    occurrenceCount__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_occurrenceCount", title="Extension field for ``occurrenceCount``."
    )

    occurrenceDate: typing.List[typing.Optional[fhirtypes.Date]] = Field(
        None,
        alias="occurrenceDate",
        title="Specific dates for a recurring set of appointments (no template)",
        description="The list of specific dates that will have appointments generated.",
        # if property is element of this resource.
        element_property=True,
    )
    occurrenceDate__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_occurrenceDate", title="Extension field for ``occurrenceDate``."
    )

    recurrenceType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="recurrenceType",
        title="The frequency of the recurrence",
        description="How often the appointment series should recur.",
        # if property is element of this resource.
        element_property=True,
    )

    timezone: fhirtypes.CodeableConceptType = Field(
        None,
        alias="timezone",
        title="The timezone of the occurrences",
        description="The timezone of the recurring appointment occurrences.",
        # if property is element of this resource.
        element_property=True,
    )

    weeklyTemplate: fhirtypes.AppointmentRecurrenceTemplateWeeklyTemplateType = Field(
        None,
        alias="weeklyTemplate",
        title="Information about weekly recurring appointments",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    yearlyTemplate: fhirtypes.AppointmentRecurrenceTemplateYearlyTemplateType = Field(
        None,
        alias="yearlyTemplate",
        title="Information about yearly recurring appointments",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("AppointmentRecurrenceTemplateMonthlyTemplate", const=True)

    dayOfMonth: fhirtypes.PositiveInt = Field(
        None,
        alias="dayOfMonth",
        title="Recurs on a specific day of the month",
        description=(
            "Indicates that appointments in the series of recurring appointments "
            "should occur on a specific day of the month."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    dayOfMonth__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dayOfMonth", title="Extension field for ``dayOfMonth``."
    )

    dayOfWeek: fhirtypes.CodingType = Field(
        None,
        alias="dayOfWeek",
        title="Indicates which day of the week the appointment should occur",
        description=(
            "Indicates which day of the week the recurring appointments should "
            "occur each nth week."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    monthInterval: fhirtypes.PositiveInt = Field(
        None,
        alias="monthInterval",
        title="Recurs every nth month",
        description="Indicates that recurring appointments should occur every nth month.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    monthInterval__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_monthInterval", title="Extension field for ``monthInterval``."
    )

    nthWeekOfMonth: fhirtypes.CodingType = Field(
        None,
        alias="nthWeekOfMonth",
        title="Indicates which week of the month the appointment should occur",
        description=(
            "Indicates which week within a month the appointments in the series of "
            "recurring appointments should occur on."
        ),
        # if property is element of this resource.
        element_property=True,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4774(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("monthInterval", "monthInterval__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class AppointmentRecurrenceTemplateWeeklyTemplate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about weekly recurring appointments.
    """

    resource_type = Field("AppointmentRecurrenceTemplateWeeklyTemplate", const=True)

    friday: bool = Field(
        None,
        alias="friday",
        title="Recurs on Friday",
        description="Indicates that recurring appointments should occur on Fridays.",
        # if property is element of this resource.
        element_property=True,
    )
    friday__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_friday", title="Extension field for ``friday``."
    )

    monday: bool = Field(
        None,
        alias="monday",
        title="Recurs on Mondays",
        description="Indicates that recurring appointments should occur on Mondays.",
        # if property is element of this resource.
        element_property=True,
    )
    monday__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_monday", title="Extension field for ``monday``."
    )

    saturday: bool = Field(
        None,
        alias="saturday",
        title="Recurs on Saturday",
        description="Indicates that recurring appointments should occur on Saturdays.",
        # if property is element of this resource.
        element_property=True,
    )
    saturday__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_saturday", title="Extension field for ``saturday``."
    )

    sunday: bool = Field(
        None,
        alias="sunday",
        title="Recurs on Sunday",
        description="Indicates that recurring appointments should occur on Sundays.",
        # if property is element of this resource.
        element_property=True,
    )
    sunday__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sunday", title="Extension field for ``sunday``."
    )

    thursday: bool = Field(
        None,
        alias="thursday",
        title="Recurs on Thursday",
        description="Indicates that recurring appointments should occur on Thursdays.",
        # if property is element of this resource.
        element_property=True,
    )
    thursday__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_thursday", title="Extension field for ``thursday``."
    )

    tuesday: bool = Field(
        None,
        alias="tuesday",
        title="Recurs on Tuesday",
        description="Indicates that recurring appointments should occur on Tuesdays.",
        # if property is element of this resource.
        element_property=True,
    )
    tuesday__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_tuesday", title="Extension field for ``tuesday``."
    )

    wednesday: bool = Field(
        None,
        alias="wednesday",
        title="Recurs on Wednesday",
        description="Indicates that recurring appointments should occur on Wednesdays.",
        # if property is element of this resource.
        element_property=True,
    )
    wednesday__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_wednesday", title="Extension field for ``wednesday``."
    )

    weekInterval: fhirtypes.PositiveInt = Field(
        None,
        alias="weekInterval",
        title="Recurs every nth week",
        description=(
            "The interval defines if the recurrence is every nth week. The default "
            "is every week, so it is expected that this value will be 2 or more.  "
            "e.g. For recurring every second week this interval would be 2, or "
            "every third week the interval would be 3."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    weekInterval__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    resource_type = Field("AppointmentRecurrenceTemplateYearlyTemplate", const=True)

    yearInterval: fhirtypes.PositiveInt = Field(
        None,
        alias="yearInterval",
        title="Recurs every nth year",
        description="Appointment recurs every nth year.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    yearInterval__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_yearInterval", title="Extension field for ``yearInterval``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AppointmentRecurrenceTemplateYearlyTemplate`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "yearInterval"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4657(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("yearInterval", "yearInterval__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
