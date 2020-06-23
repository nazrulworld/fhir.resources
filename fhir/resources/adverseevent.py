# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class AdverseEvent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Medical care, research study or other healthcare event causing physical
    injury.
    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """

    resource_type = Field("AdverseEvent", const=True)

    actuality: fhirtypes.Code = Field(
        ..., alias="actuality", title="Type `Code`", description="actual | potential"
    )
    actuality__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actuality", title="Extension field for ``actuality``."
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description=(
            "product-problem | product-quality | product-use-error | wrong-dose | "
            "incorrect-prescribing-information | wrong-technique | wrong-route-of-"
            "administration | wrong-rate | wrong-duration | wrong-time | expired-"
            "drug | medical-device-use-error | problem-different-manufacturer | "
            "unsafe-physical-environment"
        ),
    )

    contributor: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="contributor",
        title=(
            "List of `Reference` items referencing `Practitioner, PractitionerRole,"
            " Device` (represented as `dict` in JSON)"
        ),
        description="Who  was involved in the adverse event or the potential adverse event",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`",
        description="When the event occurred",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    detected: fhirtypes.DateTime = Field(
        None,
        alias="detected",
        title="Type `DateTime`",
        description="When the event was detected",
    )
    detected__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detected", title="Extension field for ``detected``."
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Encounter created as part of",
    )

    event: fhirtypes.CodeableConceptType = Field(
        None,
        alias="event",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of the event itself in relation to the subject",
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

    recordedDate: fhirtypes.DateTime = Field(
        None,
        alias="recordedDate",
        title="Type `DateTime`",
        description="When the event was recorded",
    )
    recordedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recordedDate", title="Extension field for ``recordedDate``."
    )

    recorder: fhirtypes.ReferenceType = Field(
        None,
        alias="recorder",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, PractitionerRole,"
            " RelatedPerson` (represented as `dict` in JSON)"
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

    resultingCondition: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="resultingCondition",
        title=(
            "List of `Reference` items referencing `Condition` (represented as "
            "`dict` in JSON)"
        ),
        description="Effect on the subject due to this event",
    )

    seriousness: fhirtypes.CodeableConceptType = Field(
        None,
        alias="seriousness",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Seriousness of the event",
    )

    severity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="severity",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="mild | moderate | severe",
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
        ...,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group, Practitioner, "
            "RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Subject impacted by event",
    )

    subjectMedicalHistory: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="subjectMedicalHistory",
        title=(
            "List of `Reference` items referencing `Condition, Observation, "
            "AllergyIntolerance, FamilyMemberHistory, Immunization, Procedure, "
            "Media, DocumentReference` (represented as `dict` in JSON)"
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


class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The suspected agent causing the adverse event.
    Describes the entity that is suspected to have caused the adverse event.
    """

    resource_type = Field("AdverseEventSuspectEntity", const=True)

    causality: ListType[fhirtypes.AdverseEventSuspectEntityCausalityType] = Field(
        None,
        alias="causality",
        title=(
            "List of `AdverseEventSuspectEntityCausality` items (represented as "
            "`dict` in JSON)"
        ),
        description="Information on the possible cause of the event",
    )

    instance: fhirtypes.ReferenceType = Field(
        ...,
        alias="instance",
        title=(
            "Type `Reference` referencing `Immunization, Procedure, Substance, "
            "Medication, MedicationAdministration, MedicationStatement, Device` "
            "(represented as `dict` in JSON)"
        ),
        description="Refers to the specific entity that caused the adverse event",
    )


class AdverseEventSuspectEntityCausality(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information on the possible cause of the event.
    """

    resource_type = Field("AdverseEventSuspectEntityCausality", const=True)

    assessment: fhirtypes.CodeableConceptType = Field(
        None,
        alias="assessment",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Assessment of if the entity caused the event",
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole` "
            "(represented as `dict` in JSON)"
        ),
        description="AdverseEvent.suspectEntity.causalityAuthor",
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="ProbabilityScale | Bayesian | Checklist",
    )

    productRelatedness: fhirtypes.String = Field(
        None,
        alias="productRelatedness",
        title="Type `String`",
        description="AdverseEvent.suspectEntity.causalityProductRelatedness",
    )
    productRelatedness__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_productRelatedness",
        title="Extension field for ``productRelatedness``.",
    )
