# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic.v1 import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class DiagnosticOrder(DomainResource):
    """A request for a diagnostic service.

    A record of a request for a diagnostic investigation service to be
    performed.
    """

    resource_type = Field("DiagnosticOrder", const=True)

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code`",
        description=(
            "proposed | draft | planned | requested | received | accepted | "
            "in-progress | review | completed | cancelled | suspended | rejected | "
            "failed"
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "proposed",
            "draft",
            "planned",
            "requested",
            "received",
            "accepted",
            "in-progress",
            "review",
            "completed",
            "cancelled",
            "suspended",
            "rejected",
            "failed",
        ],
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title=(
            "Type `FHIRReference` referencing `Patient, Group, Location, Device` "
            "(represented as `dict` in JSON)."
        ),
        description="Who and/or what test is about.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group", "Location", "Device"],
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON).",
        description="The encounter that this diagnostic order is associated with.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Identifiers assigned to this order.",
    )

    specimen: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="specimen",
        title=(
            "List of `FHIRReference` items referencing `Specimen` (represented as "
            "`dict` in JSON)."
        ),
        description="If the whole order relates to specific specimens.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    orderer: fhirtypes.ReferenceType = Field(
        None,
        alias="orderer",
        title=(
            "Type `FHIRReference` referencing `Practitioner` "
            "(represented as `dict` in JSON)."
        ),
        description="Who ordered the test.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="List of `CodeableConcept` items (represented as `dict` in JSON).",
        description="Explanation/Justification for test.",
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title=(
            "List of `FHIRReference` items referencing `Observation, Condition, "
            "DocumentReference` (represented as `dict` in JSON)."
        ),
        description="Additional clinical information.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Observation", "Condition", "DocumentReference"],
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `str`.",
        description="routine | urgent | stat | asap",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["routine", "urgent", "asap", "stat"],
    )

    event: ListType[fhirtypes.DiagnosticOrderEventType] = Field(
        None,
        alias="event",
        title="List of `DiagnosticOrderEvent` items (represented as `dict` in JSON).",
        description="A list of events of interest in the lifecycle.",
    )

    item: ListType[fhirtypes.DiagnosticOrderItemType] = Field(
        None,
        alias="item",
        title="List of `DiagnosticOrderItem` items (represented as `dict` in JSON).",
        description="The items the orderer requested.",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON).",
        description="Other notes and comments.",
    )


class DiagnosticOrderEvent(BackboneElement):
    """A list of events of interest in the lifecycle.

    A summary of the events of interest that have occurred as the request is
    processed; e.g. when the order was made, various processing steps
    (specimens received), when it was completed.
    """

    resource_type = Field("DiagnosticOrderEvent", const=True)

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `str`.",
        description=(
            "proposed | draft | planned | requested | received | accepted | "
            "in-progress | review | completed | cancelled | suspended | rejected | "
            "failed"
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "proposed",
            "draft",
            "planned",
            "requested",
            "received",
            "accepted",
            "in-progress",
            "review",
            "completed",
            "cancelled",
            "suspended",
            "rejected",
            "failed",
        ],
    )

    description: fhirtypes.CodeableConceptType = Field(
        None,
        alias="description",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="More information about the event and its context.",
    )

    dateTime: fhirtypes.DateTime = Field(
        ...,
        alias="dateTime",
        title="Type `DateTime` (represented as `str` in JSON).",
        description="The date at which the event happened.",
    )

    actor: fhirtypes.ReferenceType = Field(
        None,
        alias="actor",
        title=(
            "Type `Reference` referencing `Practitioner, "
            "Device` (represented as `dict` in JSON)."
        ),
        description="Who recorded or did this.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Device"],
    )


class DiagnosticOrderItem(BackboneElement):
    """The items the orderer requested.

    The specific diagnostic investigations that are requested as part of this
    request. Sometimes, there can only be one item per request, but in most
    contexts, more than one investigation can be requested.
    """

    resource_type = Field("DiagnosticOrderItem", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Code to indicate the item (test or panel) being ordered.",
    )

    specimen: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="specimen",
        title=(
            "List of `FHIRReference` items referencing `Specimen` "
            "(represented as `dict` in JSON)."
        ),
        description="If this item relates to specific specimens.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Specimen"],
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Location of requested test (if applicable).",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `str`.",
        description=(
            "proposed | draft | planned | requested | received | accepted | "
            "in-progress | review | completed | cancelled | suspended | "
            "rejected | failed"
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "proposed",
            "draft",
            "planned",
            "requested",
            "received",
            "accepted",
            "in-progress",
            "review",
            "completed",
            "cancelled",
            "suspended",
            "rejected",
            "failed",
        ],
    )

    event: ListType[fhirtypes.DiagnosticOrderEventType] = Field(
        None,
        alias="event",
        title="List of `DiagnosticOrderEvent` items (represented as `dict` in JSON).",
        description="A list of events of interest in the lifecycle.",
    )
