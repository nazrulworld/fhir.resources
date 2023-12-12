# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field

from . import backboneelement, domainresource, fhirtypes


class AdverseEvent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title=(
            "AE | PAE  An adverse event is an event that caused harm to a patient,"
            "  an adverse reaction is a something that is a subject-specific event "
            "that is a result of an exposure to a medication, food, device or "
            "environmental substance, a potential adverse event is something that "
            "occurred and that could have caused harm to a patient but did not"
        ),
        description=(
            "The type of event which is important to characterize what occurred and"
            " caused harm to the subject, or had the potential to cause harm to the"
            " subject."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["AE", "PAE"],
    )
    category__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_category", title="Extension field for ``category``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When the event occurred",
        description="The date (and perhaps time) when the adverse event occurred.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Description of the adverse event",
        description="Describes the adverse event in text.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    eventParticipant: fhirtypes.ReferenceType = Field(
        None,
        alias="eventParticipant",
        title="Who  was involved in the adverse event or the potential adverse event",
        description=(
            "Parties that may or should contribute or have contributed information "
            "to the Act. Such information includes information leading to the "
            "decision to perform the Act and how to perform the Act (e.g. "
            "consultant), information that the Act itself seeks to reveal (e.g. "
            "informant of clinical history), or information about what Act was "
            "performed (e.g. informant witness)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Device"],
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Business identifier for the event",
        description=(
            "The identifier(s) of this adverse event that are assigned by business "
            "processes and/or used to refer to it when a direct URL reference to "
            "the resource itsefl is not appropriate."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Location where adverse event occurred",
        description="The information about where the adverse event occurred.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title=(
            "resolved | recovering | ongoing | resolvedWithSequelae | fatal | "
            "unknown"
        ),
        description="Describes the type of outcome from the adverse event.",
        # if property is element of this resource.
        element_property=True,
    )

    reaction: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="reaction",
        title="Adverse Reaction Events linked to exposure to substance",
        description=(
            "Includes information about the reaction that occurred as a result of "
            "exposure to a substance (for example, a drug or a chemical)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    recorder: fhirtypes.ReferenceType = Field(
        None,
        alias="recorder",
        title="Who recorded the adverse event",
        description=(
            "Information on who recorded the adverse event.  May be the patient or "
            "a practitioner."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner", "RelatedPerson"],
    )

    referenceDocument: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="referenceDocument",
        title="AdverseEvent.referenceDocument",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    seriousness: fhirtypes.CodeableConceptType = Field(
        None,
        alias="seriousness",
        title="Mild | Moderate | Severe",
        description="Describes the seriousness or severity of the adverse event.",
        # if property is element of this resource.
        element_property=True,
    )

    study: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="study",
        title="AdverseEvent.study",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ResearchStudy"],
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Subject or group impacted by event",
        description=(
            "This subject or group impacted by the event.  With a prospective "
            "adverse event, there will be no subject as the adverse event was "
            "prevented."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "ResearchSubject", "Medication", "Device"],
    )

    subjectMedicalHistory: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="subjectMedicalHistory",
        title="AdverseEvent.subjectMedicalHistory",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "AllergyIntolerance",
            "FamilyMemberHistory",
            "Immunization",
            "Procedure",
        ],
    )

    suspectEntity: typing.List[fhirtypes.AdverseEventSuspectEntityType] = Field(
        None,
        alias="suspectEntity",
        title="The suspected agent causing the adverse event",
        description=(
            "Describes the entity that is suspected to have caused the adverse "
            "event."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="actual | potential",
        description=(
            "This element defines the specific type of event that occurred or that "
            "was prevented from occurring."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdverseEvent`` according specification,
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
            "category",
            "type",
            "subject",
            "date",
            "reaction",
            "location",
            "seriousness",
            "outcome",
            "recorder",
            "eventParticipant",
            "description",
            "suspectEntity",
            "subjectMedicalHistory",
            "referenceDocument",
            "study",
        ]


class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The suspected agent causing the adverse event.
    Describes the entity that is suspected to have caused the adverse event.
    """

    resource_type = Field("AdverseEventSuspectEntity", const=True)

    causality: fhirtypes.Code = Field(
        None,
        alias="causality",
        title="causality1 | causality2",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["causality1", "causality2"],
    )
    causality__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_causality", title="Extension field for ``causality``."
    )

    causalityAssessment: fhirtypes.CodeableConceptType = Field(
        None,
        alias="causalityAssessment",
        title="assess1 | assess2",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    causalityAuthor: fhirtypes.ReferenceType = Field(
        None,
        alias="causalityAuthor",
        title="AdverseEvent.suspectEntity.causalityAuthor",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole"],
    )

    causalityMethod: fhirtypes.CodeableConceptType = Field(
        None,
        alias="causalityMethod",
        title="method1 | method2",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    causalityProductRelatedness: fhirtypes.String = Field(
        None,
        alias="causalityProductRelatedness",
        title="AdverseEvent.suspectEntity.causalityProductRelatedness",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    causalityProductRelatedness__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_causalityProductRelatedness",
        title="Extension field for ``causalityProductRelatedness``.",
    )

    causalityResult: fhirtypes.CodeableConceptType = Field(
        None,
        alias="causalityResult",
        title="result1 | result2",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    instance: fhirtypes.ReferenceType = Field(
        ...,
        alias="instance",
        title="Refers to the specific entity that caused the adverse event",
        description=(
            "Identifies the actual instance of what caused the adverse event.  May "
            "be a substance, medication, medication administration, medication "
            "statement or a device."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Substance",
            "Medication",
            "MedicationAdministration",
            "MedicationStatement",
            "Device",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``AdverseEventSuspectEntity`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "instance",
            "causality",
            "causalityAssessment",
            "causalityProductRelatedness",
            "causalityMethod",
            "causalityAuthor",
            "causalityResult",
        ]
