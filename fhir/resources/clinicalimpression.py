# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalImpression
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ClinicalImpression(domainresource.DomainResource):
    """ A clinical assessment performed when planning treatments and management
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

    assessor: fhirtypes.ReferenceType = Field(
        None,
        alias="assessor",
        title="Type `Reference` referencing `Practitioner, PractitionerRole` (represented as `dict` in JSON)",
        description="The clinician performing the assessment",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of assessment performed",
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

    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Time of assessment",
        one_of_many="effective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time of assessment",
        one_of_many="effective",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON)",
        description="Encounter created as part of",
    )

    finding: ListType[fhirtypes.ClinicalImpressionFindingType] = Field(
        None,
        alias="finding",
        title="List of `ClinicalImpressionFinding` items (represented as `dict` in JSON)",
        description="Possible or likely findings and diagnoses",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier",
    )

    investigation: ListType[fhirtypes.ClinicalImpressionInvestigationType] = Field(
        None,
        alias="investigation",
        title="List of `ClinicalImpressionInvestigation` items (represented as `dict` in JSON)",
        description="One or more sets of investigations (signs, symptoms, etc.)",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments made about the ClinicalImpression",
    )

    previous: fhirtypes.ReferenceType = Field(
        None,
        alias="previous",
        title="Type `Reference` referencing `ClinicalImpression` (represented as `dict` in JSON)",
        description="Reference to last assessment",
    )

    problem: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="problem",
        title="List of `Reference` items referencing `Condition, AllergyIntolerance` (represented as `dict` in JSON)",
        description="Relevant impressions of patient state",
    )

    prognosisCodeableConcept: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="prognosisCodeableConcept",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Estimate of likely outcome",
    )

    prognosisReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="prognosisReference",
        title="List of `Reference` items referencing `RiskAssessment` (represented as `dict` in JSON)",
        description="RiskAssessment expressing likely outcome",
    )

    protocol: ListType[fhirtypes.Uri] = Field(
        None,
        alias="protocol",
        title="List of `Uri` items (represented as `dict` in JSON)",
        description="Clinical Protocol followed",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="in-progress | completed | entered-in-error",
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Reason for current status",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON)",
        description="Patient or group assessed",
    )

    summary: fhirtypes.String = Field(
        None,
        alias="summary",
        title="Type `String` (represented as `dict` in JSON)",
        description="Summary of the assessment",
    )

    supportingInfo: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInfo",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Information supporting the clinical impression",
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
        one_of_many_fields = {
            "effective": ["effectiveDateTime", "effectivePeriod",],
        }
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


class ClinicalImpressionFinding(backboneelement.BackboneElement):
    """ Possible or likely findings and diagnoses.
    Specific findings or diagnoses that were considered likely or relevant to
    ongoing treatment.
    """

    resource_type = Field("ClinicalImpressionFinding", const=True)

    basis: fhirtypes.String = Field(
        None,
        alias="basis",
        title="Type `String` (represented as `dict` in JSON)",
        description="Which investigations support finding",
    )

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="What was found",
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="Type `Reference` referencing `Condition, Observation, Media` (represented as `dict` in JSON)",
        description="What was found",
    )


class ClinicalImpressionInvestigation(backboneelement.BackboneElement):
    """ One or more sets of investigations (signs, symptoms, etc.).
    One or more sets of investigations (signs, symptoms, etc.). The actual
    grouping of investigations varies greatly depending on the type and context
    of the assessment. These investigations may include data generated during
    the assessment process, or data previously generated and recorded that is
    pertinent to the outcomes.
    """

    resource_type = Field("ClinicalImpressionInvestigation", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="A name/code for the set",
    )

    item: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="item",
        title="List of `Reference` items referencing `Observation, QuestionnaireResponse, FamilyMemberHistory, DiagnosticReport, RiskAssessment, ImagingStudy, Media` (represented as `dict` in JSON)",
        description="Record of a specific investigation",
    )
