# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AppointmentResponse
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .domainresource import DomainResource


class AppointmentResponse(DomainResource):
    """A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """

    resource_type = Field("AppointmentResponse", const=True)

    actor: fhirtypes.ReferenceType = Field(
        None,
        alias="actor",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, RelatedPerson, "
            "Device, HealthcareService, Location` (represented as `dict` in JSON)"
        ),
        description="Person, Location/HealthcareService or Device",
    )

    appointment: fhirtypes.ReferenceType = Field(
        ...,
        alias="appointment",
        title=(
            "Type `Reference` referencing `Appointment` (represented as `dict` in "
            "JSON)"
        ),
        description="Appointment this response relates to",
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional comments",
    )

    end: fhirtypes.Instant = Field(
        None,
        alias="end",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Time from appointment, or requested new end time",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Ids for this item",
    )

    participantStatus: fhirtypes.Code = Field(
        ...,
        alias="participantStatus",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "accepted | declined | tentative | in-process | completed | needs-"
            "action | entered-in-error"
        ),
    )

    participantType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="participantType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Role of participant in the appointment",
    )

    start: fhirtypes.Instant = Field(
        None,
        alias="start",
        title="Type `Instant` (represented as `dict` in JSON)",
        description="Time from appointment, or requested new start time",
    )
