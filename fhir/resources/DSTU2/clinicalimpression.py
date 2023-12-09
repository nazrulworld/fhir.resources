# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalImpression
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class ClinicalImpression(DomainResource):
    """A clinical assessment performed when planning treatments and management
    strategies for a patient.

    A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments are
    often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow. This resource is called
    "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion
    with the recording of assessment tools such as Apgar score.
    """

    resource_type = Field("ClinicalImpression", const=True)

    action: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="action",
        title=(
            "List of `Reference` items referencing `ReferralRequest, "
            "ProcedureRequest, Procedure, MedicationRequest, Appointment` "
            "(represented as `dict` in JSON)"
        ),
        description="Action taken as part of assessment procedure",
    )

    assessor: fhirtypes.ReferenceType = Field(
        None,
        alias="assessor",
        title=(
            "Type `Reference` referencing `Practitioner` (represented as `dict` in "
            "JSON)"
        ),
        description="The clinician performing the assessment",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the assessment was documented",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Why/how the assessment was performed",
    )

    finding: ListType[fhirtypes.ClinicalImpressionFindingType] = Field(
        None,
        alias="finding",
        title=(
            "List of `ClinicalImpressionFinding` items (represented as `dict` in "
            "JSON)"
        ),
        description="Possible or likely findings and diagnoses",
    )

    investigations: ListType[fhirtypes.ClinicalImpressionInvestigationsType] = Field(
        None,
        alias="investigations",
        title=(
            "List of `ClinicalImpressionInvestigations` items (represented as `dict`"
            " in JSON)"
        ),
        description="One or more sets of investigations (signs, symptions, etc.)",
    )

    previous: fhirtypes.ReferenceType = Field(
        None,
        alias="previous",
        title=(
            "Type `Reference` referencing `ClinicalImpression` (represented as "
            "`dict` in JSON)"
        ),
        description="Reference to last assessment",
    )

    problem: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="problem",
        title=(
            "List of `Reference` items referencing `Condition, AllergyIntolerance` "
            "(represented as `dict` in JSON)"
        ),
        description="Relevant impressions of patient state",
    )

    prognosis: fhirtypes.String = Field(
        None,
        alias="prognosis",
        title="Type String",
        description="Estimate of likely outcome",
    )

    protocol: fhirtypes.Uri = Field(
        None,
        alias="protocol",
        title="`Uri` (represented as `dict` in JSON)",
        description="Clinical Protocol followed",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | completed | entered-in-error",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="Patient or group assessed",
    )

    plan: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="plan",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="Plan of action after assessment",
    )

    summary: fhirtypes.String = Field(
        None,
        alias="summary",
        title="Type `String` (represented as `dict` in JSON)",
        description="Summary of the assessment",
    )
    resolved: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="resolved",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Summary of the assessment",
    )
    triggerCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="triggerCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Summary of the assessment",
        one_of_many="trigger",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )
    triggerReference: fhirtypes.ReferenceType = Field(
        None,
        alias="triggerReference",
        title="Type `Reference` (represented as `dict` in JSON)",
        description="Summary of the assessment",
        one_of_many="trigger",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    ruledOut: ListType[fhirtypes.ClinicalImpressionRuledOutType] = Field(
        None,
        alias="ruledOut",
        title=(
            "List of `ClinicalImpressionRuledOut` items (represented as `dict`"
            " in JSON)"
        ),
        description="Diagnosis considered not possible.",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"trigger": ["triggerReference", "triggerCodeableConcept"]}
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class ClinicalImpressionFinding(BackboneElement):
    """Possible or likely findings and diagnoses.

    Specific findings or diagnoses that was considered likely or relevant to
    ongoing treatment.
    """

    resource_type = Field("ClinicalImpressionFinding", const=True)
    cause: fhirtypes.String = Field(
        None,
        alias="cause",
        title="Type `String`",
        description="Which investigations support finding.",
    )
    item: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="item",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Specific text or code for finding.",
    )


class ClinicalImpressionInvestigations(BackboneElement):
    """One or more sets of investigations (signs, symptions, etc.).

    One or more sets of investigations (signs, symptions, etc.). The actual
    grouping of investigations vary greatly depending on the type and context
    of the assessment. These investigations may include data generated during
    the assessment process, or data previously generated and recorded that is
    pertinent to the outcomes.
    """

    resource_type = Field("ClinicalImpressionInvestigations", const=True)
    item: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="item",
        title=(
            "List of `FHIRReference` items referencing `Observation,"
            " QuestionnaireResponse, FamilyMemberHistory, "
            "DiagnosticReport` (represented as `dict` in JSON)"
        ),
        description="Which investigations support finding.",
    )
    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="A name/code for the set.",
    )


class ClinicalImpressionRuledOut(BackboneElement):
    """Diagnosis considered not possible."""

    resource_type = Field("ClinicalImpressionRuledOut", const=True)

    reason: fhirtypes.String = Field(
        None,
        alias="reason",
        title="Type `String`.",
        description="Grounds for elimination.",
    )
    item: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="item",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Specific text of code for diagnosis.",
    )
