from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Appointment
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Additional comments",
        description="Additional comments about the appointment.",
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
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
            "expanded information should be put in the comment field."
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

    incomingReferral: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="incomingReferral",
        title=(
            "The ReferralRequest provided as information to allocate to the "
            "Encounter"
        ),
        description=(
            "The referral request this appointment is allocated to assess (incoming"
            " referral)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ReferralRequest"],
        },
    )

    indication: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="indication",
        title="Reason the appointment is to takes place (resource)",
        description=(
            "Reason the appointment has been scheduled to take place, as specified "
            "using information from another resource. When the patient arrives and "
            "the encounter begins it may be used as the admission diagnosis. The "
            "indication will typically be a Condition (with other resources "
            "referenced in the evidence.detail), or a Procedure."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition", "Procedure"],
        },
    )

    minutesDuration: fhirtypes.PositiveIntType | None = Field(  # type: ignore
        None,
        alias="minutesDuration",
        title="Can be less than start/end (e.g. estimate)",
        description=(
            "Number of minutes that the appointment is to take. This can be less "
            "than the duration between the start and end times (where actual time "
            "of appointment is only an estimate or is a planned appointment "
            "request)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    minutesDuration__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_minutesDuration", title="Extension field for ``minutesDuration``."
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

    priority: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
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
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Reason this appointment is scheduled",
        description=(
            "The reason that this appointment is being scheduled. This is more "
            "clinical than administrative."
        ),
        json_schema_extra={
            "element_property": True,
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
            "appointment is preferred to be scheduled within. When using these "
            "values, the minutes duration should be provided to indicate the length"
            " of the appointment to fill and populate the start/end times for the "
            "actual allocated time."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    serviceCategory: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="serviceCategory",
        title=(
            "A broad categorisation of the service that is to be performed during "
            "this appointment"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    serviceType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="serviceType",
        title="The specific service that is to be performed during this appointment",
        description=None,
        json_schema_extra={
            "element_property": True,
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
            " | entered-in-error"
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
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
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
            "serviceCategory",
            "serviceType",
            "specialty",
            "appointmentType",
            "reason",
            "indication",
            "priority",
            "description",
            "supportingInformation",
            "start",
            "end",
            "minutesDuration",
            "slot",
            "created",
            "comment",
            "incomingReferral",
            "participant",
            "requestedPeriod",
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
        title="Person, Location/HealthcareService or Device",
        description=(
            "A Person, Location/HealthcareService or Device that is participating "
            "in the appointment."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "RelatedPerson",
                "Device",
                "HealthcareService",
                "Location",
            ],
        },
    )

    required: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="required",
        title="required | optional | information-only",
        description=(
            "Is this participant required to be present at the meeting. This covers"
            " a use-case where 2 doctors need to meet to discuss the results for a "
            "specific patient, and the patient is not required to be present."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["required", "optional", "information-only"],
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
