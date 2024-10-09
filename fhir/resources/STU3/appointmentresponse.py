from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/AppointmentResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class AppointmentResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """

    __resource_type__ = "AppointmentResponse"

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

    appointment: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="appointment",
        title="Appointment this response relates to",
        description="Appointment that this response is replying to.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Appointment"],
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

    end: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="end",
        title="Time from appointment, or requested new end time",
        description=(
            "This may be either the same as the appointment request to confirm the "
            "details of the appointment, or alternately a new time to request a re-"
            "negotiation of the end time."
        ),
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
            "This records identifiers associated with this appointment response "
            "concern that are defined by business processes and/ or used to refer "
            "to it when a direct URL reference to the resource itself is not "
            "appropriate."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    participantStatus: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="participantStatus",
        title=(
            "accepted | declined | tentative | in-process | completed | needs-"
            "action | entered-in-error"
        ),
        description=(
            "Participation status of the participant. When the status is declined "
            "or tentative if the start/end times are different to the appointment, "
            "then these times should be interpreted as a requested time change. "
            "When the status is accepted, the times can either be the time of the "
            "appointment (as a confirmation of the time) or can be empty."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "accepted",
                "declined",
                "tentative",
                "in-process",
                "completed",
                "needs-action",
                "entered-in-error",
            ],
        },
    )
    participantStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_participantStatus",
        title="Extension field for ``participantStatus``.",
    )

    participantType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="participantType",
        title="Role of participant in the appointment",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    start: fhirtypes.InstantType | None = Field(  # type: ignore
        None,
        alias="start",
        title="Time from appointment, or requested new start time",
        description=(
            "Date/Time that the appointment is to take place, or requested new "
            "start time."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_start", title="Extension field for ``start``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AppointmentResponse`` according specification,
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
            "appointment",
            "start",
            "end",
            "participantType",
            "actor",
            "participantStatus",
            "comment",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("participantStatus", "participantStatus__ext")]
        return required_fields
