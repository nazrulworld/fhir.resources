# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class AdverseEvent(domainresource.DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.
    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """

    resource_type = Field("AdverseEvent", const=True)

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "AE | PAE  An adverse event is an event that caused harm to a patient,"
            "  an adverse reaction is a something that is a subject-specific event "
            "that is a result of an exposure to a medication, food, device or "
            "environmental substance, a potential adverse event is something that "
            "occurred and that could have caused harm to a patient but did not"
        ),
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the event occurred",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of the adverse event",
    )

    eventParticipant: fhirtypes.ReferenceType = Field(
        None,
        alias="eventParticipant",
        title=(
            "Type `Reference` referencing `Practitioner, Device` (represented as "
            "`dict` in JSON)"
        ),
        description="Who  was involved in the adverse event or the potential adverse event",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Business identifier for the event",
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Location where adverse event occurred",
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "resolved | recovering | ongoing | resolvedWithSequelae | fatal | "
            "unknown"
        ),
    )

    reaction: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reaction",
        title=(
            "List of `Reference` items referencing `Condition` (represented as "
            "`dict` in JSON)"
        ),
        description="Adverse Reaction Events linked to exposure to substance",
    )

    recorder: fhirtypes.ReferenceType = Field(
        None,
        alias="recorder",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, RelatedPerson` "
            "(represented as `dict` in JSON)"
        ),
        description="Who recorded the adverse event",
    )

    referenceDocument: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="referenceDocument",
        title=(
            "List of `Reference` items referencing `DocumentReference` (represented"
            " as `dict` in JSON)"
        ),
        description="AdverseEvent.referenceDocument",
    )

    seriousness: fhirtypes.CodeableConceptType = Field(
        None,
        alias="seriousness",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Mild | Moderate | Severe",
    )

    study: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="study",
        title=(
            "List of `Reference` items referencing `ResearchStudy` (represented as "
            "`dict` in JSON)"
        ),
        description="AdverseEvent.study",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, ResearchSubject, Medication, "
            "Device` (represented as `dict` in JSON)"
        ),
        description="Subject or group impacted by event",
    )

    subjectMedicalHistory: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="subjectMedicalHistory",
        title=(
            "List of `Reference` items referencing `Condition, Observation, "
            "AllergyIntolerance, FamilyMemberHistory, Immunization, Procedure` "
            "(represented as `dict` in JSON)"
        ),
        description="AdverseEvent.subjectMedicalHistory",
    )

    suspectEntity: ListType[fhirtypes.AdverseEventSuspectEntityType] = Field(
        None,
        alias="suspectEntity",
        title=(
            "List of `AdverseEventSuspectEntity` items (represented as `dict` in "
            "JSON)"
        ),
        description="The suspected agent causing the adverse event",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="actual | potential",
    )


class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """ The suspected agent causing the adverse event.
    Describes the entity that is suspected to have caused the adverse event.
    """

    resource_type = Field("AdverseEventSuspectEntity", const=True)

    causality: fhirtypes.Code = Field(
        None,
        alias="causality",
        title="Type `Code` (represented as `dict` in JSON)",
        description="causality1 | causality2",
    )

    causalityAssessment: fhirtypes.CodeableConceptType = Field(
        None,
        alias="causalityAssessment",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="assess1 | assess2",
    )

    causalityAuthor: fhirtypes.ReferenceType = Field(
        None,
        alias="causalityAuthor",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole` "
            "(represented as `dict` in JSON)"
        ),
        description="AdverseEvent.suspectEntity.causalityAuthor",
    )

    causalityMethod: fhirtypes.CodeableConceptType = Field(
        None,
        alias="causalityMethod",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="method1 | method2",
    )

    causalityProductRelatedness: fhirtypes.String = Field(
        None,
        alias="causalityProductRelatedness",
        title="Type `String` (represented as `dict` in JSON)",
        description="AdverseEvent.suspectEntity.causalityProductRelatedness",
    )

    causalityResult: fhirtypes.CodeableConceptType = Field(
        None,
        alias="causalityResult",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="result1 | result2",
    )

    instance: fhirtypes.ReferenceType = Field(
        ...,
        alias="instance",
        title=(
            "Type `Reference` referencing `Substance, Medication, "
            "MedicationAdministration, MedicationStatement, Device` (represented as"
            " `dict` in JSON)"
        ),
        description="Refers to the specific entity that caused the adverse event",
    )
