# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Condition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Condition(domainresource.DomainResource):
    """ Detailed information about conditions, problems or diagnoses.
    A clinical condition, problem, diagnosis, or other event, situation, issue,
    or clinical concept that has risen to a level of concern.
    """

    resource_type = Field("Condition", const=True)

    abatementAge: fhirtypes.AgeType = Field(
        None,
        alias="abatementAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="If/when in resolution/remission",
        one_of_many="abatement",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    abatementBoolean: bool = Field(
        None,
        alias="abatementBoolean",
        title="Type `bool`",
        description="If/when in resolution/remission",
        one_of_many="abatement",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    abatementDateTime: fhirtypes.DateTime = Field(
        None,
        alias="abatementDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="If/when in resolution/remission",
        one_of_many="abatement",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    abatementPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="abatementPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="If/when in resolution/remission",
        one_of_many="abatement",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    abatementRange: fhirtypes.RangeType = Field(
        None,
        alias="abatementRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="If/when in resolution/remission",
        one_of_many="abatement",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    abatementString: fhirtypes.String = Field(
        None,
        alias="abatementString",
        title="Type `String` (represented as `dict` in JSON)",
        description="If/when in resolution/remission",
        one_of_many="abatement",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    assertedDate: fhirtypes.DateTime = Field(
        None,
        alias="assertedDate",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date record was believed accurate",
    )

    asserter: fhirtypes.ReferenceType = Field(
        None,
        alias="asserter",
        title="Type `Reference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON)",
        description="Person who asserts this condition",
    )

    bodySite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodySite",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Anatomical location, if relevant",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="problem-list-item | encounter-diagnosis",
    )

    clinicalStatus: fhirtypes.Code = Field(
        None,
        alias="clinicalStatus",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | recurrence | inactive | remission | resolved",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Identification of the condition, problem or diagnosis",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Type `Reference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON)",
        description="Encounter or episode when condition first asserted",
    )

    evidence: ListType[fhirtypes.ConditionEvidenceType] = Field(
        None,
        alias="evidence",
        title="List of `ConditionEvidence` items (represented as `dict` in JSON)",
        description="Supporting evidence",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="External Ids for this condition",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Additional information about the Condition",
    )

    onsetAge: fhirtypes.AgeType = Field(
        None,
        alias="onsetAge",
        title="Type `Age` (represented as `dict` in JSON)",
        description="Estimated or actual date,  date-time, or age",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onsetDateTime: fhirtypes.DateTime = Field(
        None,
        alias="onsetDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Estimated or actual date,  date-time, or age",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onsetPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="onsetPeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Estimated or actual date,  date-time, or age",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onsetRange: fhirtypes.RangeType = Field(
        None,
        alias="onsetRange",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Estimated or actual date,  date-time, or age",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    onsetString: fhirtypes.String = Field(
        None,
        alias="onsetString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Estimated or actual date,  date-time, or age",
        one_of_many="onset",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    severity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="severity",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Subjective severity of condition",
    )

    stage: fhirtypes.ConditionStageType = Field(
        None,
        alias="stage",
        title="Type `ConditionStage` (represented as `dict` in JSON)",
        description="Stage/grade, usually assessed formally",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON)",
        description="Who has the condition?",
    )

    verificationStatus: fhirtypes.Code = Field(
        None,
        alias="verificationStatus",
        title="Type `Code` (represented as `dict` in JSON)",
        description="provisional | differential | confirmed | refuted | entered-in-error | unknown",
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
            "abatement": [
                "abatementAge",
                "abatementBoolean",
                "abatementDateTime",
                "abatementPeriod",
                "abatementRange",
                "abatementString",
            ],
            "onset": [
                "onsetAge",
                "onsetDateTime",
                "onsetPeriod",
                "onsetRange",
                "onsetString",
            ],
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


class ConditionEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.
    Supporting Evidence / manifestations that are the basis on which this
    condition is suspected or confirmed.
    """

    resource_type = Field("ConditionEvidence", const=True)

    code: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Manifestation/symptom",
    )

    detail: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="detail",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Supporting information found elsewhere",
    )


class ConditionStage(backboneelement.BackboneElement):
    """ Stage/grade, usually assessed formally.
    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """

    resource_type = Field("ConditionStage", const=True)

    assessment: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="assessment",
        title="List of `Reference` items referencing `ClinicalImpression, DiagnosticReport, Observation` (represented as `dict` in JSON)",
        description="Formal record of assessment",
    )

    summary: fhirtypes.CodeableConceptType = Field(
        None,
        alias="summary",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Simple summary (disease specific)",
    )
