# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AllergyIntolerance
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import List as ListType

from pydantic import Field

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class AllergyIntolerance(DomainResource):
    """Allergy or Intolerance (generally: Risk Of Adverse reaction to a substance).

    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """

    resource_type = Field("AllergyIntolerance", const=True)

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="Type `Code` (represented as `dict` in JSON)",
        description="food | medication | environment | biologic",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "active | unconfirmed | confirmed | inactive | resolved | "
            "refuted | entered-in-error"
        ),
    )

    criticality: fhirtypes.Code = Field(
        None,
        alias="criticality",
        title="Type `Code` (represented as `dict` in JSON)",
        description="low | high | unable-to-assess",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External ids for this item",
    )

    lastOccurrence: fhirtypes.DateTime = Field(
        None,
        alias="lastOccurrence",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date(/time) of last known occurrence of a reaction",
    )

    note: fhirtypes.AnnotationType = Field(
        None,
        alias="note",
        title="`Annotation` items (represented as `dict` in JSON)",
        description="Additional text not captured in other fields",
    )

    onset: fhirtypes.DateTime = Field(
        None,
        alias="onset",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date(/time) when manifestations showed",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="Who the sensitivity is for",
    )

    reaction: ListType[fhirtypes.AllergyIntoleranceReactionType] = Field(
        None,
        alias="reaction",
        title=(
            "List of `AllergyIntoleranceReaction` items (represented as `dict` in "
            "JSON)"
        ),
        description="Adverse Reaction Events linked to exposure to substance",
    )
    reporter: fhirtypes.ReferenceType = Field(
        None,
        alias="reporter",
        title=(
            "Type `Reference` referencing `Practitioner, Patient` (represented as "
            "`dict` in JSON)"
        ),
        description="Source of the information about the allergy",
    )

    recorder: fhirtypes.ReferenceType = Field(
        None,
        alias="recorder",
        title=(
            "Type `Reference` referencing `Practitioner, Patient` (represented as "
            "`dict` in JSON)"
        ),
        description="Who recorded the sensitivity",
    )
    recordedDate: fhirtypes.DateTime = Field(
        None,
        alias="recordedDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When recorded",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="allergy | intolerance - Underlying mechanism (if known)",
    )

    substance: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substance",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Substance, (or class) considered to be responsible for risk",
    )


class AllergyIntoleranceReaction(BackboneElement):
    """Adverse Reaction Events linked to exposure to substance.

    Details about each adverse reaction event linked to exposure to the
    identified Substance.
    """

    resource_type = Field("AllergyIntoleranceReaction", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of the event as a whole",
    )

    exposureRoute: fhirtypes.CodeableConceptType = Field(
        None,
        alias="exposureRoute",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How the subject was exposed to the substance",
    )

    manifestation: ListType[fhirtypes.CodeableConceptType] = Field(
        ...,
        alias="manifestation",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Clinical symptoms/signs associated with the Event",
    )

    note: fhirtypes.AnnotationType = Field(
        None,
        alias="note",
        title="`Annotation` (represented as `dict` in JSON)",
        description="Text about event not captured in other fields",
    )

    onset: fhirtypes.DateTime = Field(
        None,
        alias="onset",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date(/time) when manifestations showed",
    )

    severity: fhirtypes.Code = Field(
        None,
        alias="severity",
        title="Type `Code` (represented as `dict` in JSON)",
        description="mild | moderate | severe (of event as a whole)",
    )

    substance: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substance",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "Specific substance or pharmaceutical product considered to be "
            "responsible for event"
        ),
    )
    certainty: fhirtypes.Code = Field(
        None,
        alias="certainty",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "unlikely | likely | confirmed - clinical certainty "
            "about the specific substance"
        ),
    )
