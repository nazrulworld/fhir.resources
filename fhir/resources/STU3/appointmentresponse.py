# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AppointmentResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class AppointmentResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """

    resource_type = Field("AppointmentResponse", const=True)

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
            "RelatedPerson",
            "Device",
            "HealthcareService",
            "Location",
        ],
    )

    appointment: fhirtypes.ReferenceType = Field(
        ...,
        alias="appointment",
        title="Appointment this response relates to",
        description="Appointment that this response is replying to.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Appointment"],
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

    end: fhirtypes.Instant = Field(
        None,
        alias="end",
        title="Time from appointment, or requested new end time",
        description=(
            "This may be either the same as the appointment request to confirm the "
            "details of the appointment, or alternately a new time to request a re-"
            "negotiation of the end time."
        ),
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
            "This records identifiers associated with this appointment response "
            "concern that are defined by business processes and/ or used to refer "
            "to it when a direct URL reference to the resource itself is not "
            "appropriate."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    participantStatus: fhirtypes.Code = Field(
        ...,
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
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "accepted",
            "declined",
            "tentative",
            "in-process",
            "completed",
            "needs-action",
            "entered-in-error",
        ],
    )
    participantStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_participantStatus",
        title="Extension field for ``participantStatus``.",
    )

    participantType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="participantType",
        title="Role of participant in the appointment",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    start: fhirtypes.Instant = Field(
        None,
        alias="start",
        title="Time from appointment, or requested new start time",
        description=(
            "Date/Time that the appointment is to take place, or requested new "
            "start time."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )
