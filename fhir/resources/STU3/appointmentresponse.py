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
        None, alias="comment", title="Type `String`", description="Additional comments"
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    end: fhirtypes.Instant = Field(
        None,
        alias="end",
        title="Type `Instant`",
        description="Time from appointment, or requested new end time",
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
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
        title="Type `Code`",
        description=(
            "accepted | declined | tentative | in-process | completed | needs-"
            "action | entered-in-error"
        ),
    )
    participantStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_participantStatus",
        title="Extension field for ``participantStatus``.",
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
        title="Type `Instant`",
        description="Time from appointment, or requested new start time",
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )
