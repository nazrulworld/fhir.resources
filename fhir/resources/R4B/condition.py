from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Condition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Condition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Detailed information about conditions, problems or diagnoses.
    A clinical condition, problem, diagnosis, or other event, situation, issue,
    or clinical concept that has risen to a level of concern.
    """

    __resource_type__ = "Condition"

    abatementAge: fhirtypes.AgeType | None = Field(  # type: ignore
        None,
        alias="abatementAge",
        title="When in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Conditions '
            "are never really resolved, but they can abate."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e abatement[x]
            "one_of_many": "abatement",
            "one_of_many_required": False,
        },
    )

    abatementDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="abatementDateTime",
        title="When in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Conditions '
            "are never really resolved, but they can abate."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e abatement[x]
            "one_of_many": "abatement",
            "one_of_many_required": False,
        },
    )
    abatementDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_abatementDateTime",
        title="Extension field for ``abatementDateTime``.",
    )

    abatementPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="abatementPeriod",
        title="When in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Conditions '
            "are never really resolved, but they can abate."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e abatement[x]
            "one_of_many": "abatement",
            "one_of_many_required": False,
        },
    )

    abatementRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="abatementRange",
        title="When in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Conditions '
            "are never really resolved, but they can abate."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e abatement[x]
            "one_of_many": "abatement",
            "one_of_many_required": False,
        },
    )

    abatementString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="abatementString",
        title="When in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Conditions '
            "are never really resolved, but they can abate."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e abatement[x]
            "one_of_many": "abatement",
            "one_of_many_required": False,
        },
    )
    abatementString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_abatementString", title="Extension field for ``abatementString``."
    )

    asserter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="asserter",
        title="Person who asserts this condition",
        description="Individual who is making the condition statement.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    bodySite: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="bodySite",
        title="Anatomical location, if relevant",
        description="The anatomical location where this condition manifests itself.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="category",
        title="problem-list-item | encounter-diagnosis",
        description="A category assigned to the condition.",
        json_schema_extra={
            "element_property": True,
        },
    )

    clinicalStatus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="clinicalStatus",
        title="active | recurrence | relapse | inactive | remission | resolved",
        description="The clinical status of the condition.",
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Identification of the condition, problem or diagnosis",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounter created as part of",
        description=(
            "The Encounter during which this Condition was created or to which the "
            "creation of this record is tightly associated."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    evidence: typing.List[fhirtypes.ConditionEvidenceType] | None = Field(  # type: ignore
        None,
        alias="evidence",
        title="Supporting evidence",
        description=(
            "Supporting evidence / manifestations that are the basis of the "
            "Condition's verification status, such as evidence that confirmed or "
            "refuted the condition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External Ids for this condition",
        description=(
            "Business identifiers assigned to this condition by the performer or "
            "other systems which remain constant as the resource is updated and "
            "propagates from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Additional information about the Condition",
        description=(
            "Additional information about the Condition. This is a general "
            "notes/comments entry  for description of the Condition, its diagnosis "
            "and prognosis."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    onsetAge: fhirtypes.AgeType | None = Field(  # type: ignore
        None,
        alias="onsetAge",
        title="Estimated or actual date,  date-time, or age",
        description=(
            "Estimated or actual date or date-time  the condition began, in the "
            "opinion of the clinician."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onset[x]
            "one_of_many": "onset",
            "one_of_many_required": False,
        },
    )

    onsetDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="onsetDateTime",
        title="Estimated or actual date,  date-time, or age",
        description=(
            "Estimated or actual date or date-time  the condition began, in the "
            "opinion of the clinician."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onset[x]
            "one_of_many": "onset",
            "one_of_many_required": False,
        },
    )
    onsetDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_onsetDateTime", title="Extension field for ``onsetDateTime``."
    )

    onsetPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="onsetPeriod",
        title="Estimated or actual date,  date-time, or age",
        description=(
            "Estimated or actual date or date-time  the condition began, in the "
            "opinion of the clinician."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onset[x]
            "one_of_many": "onset",
            "one_of_many_required": False,
        },
    )

    onsetRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="onsetRange",
        title="Estimated or actual date,  date-time, or age",
        description=(
            "Estimated or actual date or date-time  the condition began, in the "
            "opinion of the clinician."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onset[x]
            "one_of_many": "onset",
            "one_of_many_required": False,
        },
    )

    onsetString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="onsetString",
        title="Estimated or actual date,  date-time, or age",
        description=(
            "Estimated or actual date or date-time  the condition began, in the "
            "opinion of the clinician."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e onset[x]
            "one_of_many": "onset",
            "one_of_many_required": False,
        },
    )
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_onsetString", title="Extension field for ``onsetString``."
    )

    recordedDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="recordedDate",
        title="Date record was first recorded",
        description=(
            "The recordedDate represents when this particular Condition record was "
            "created in the system, which is often a system-generated date."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    recordedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_recordedDate", title="Extension field for ``recordedDate``."
    )

    recorder: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="recorder",
        title="Who recorded the condition",
        description=(
            "Individual who recorded the record and takes responsibility for its "
            "content."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    severity: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="severity",
        title="Subjective severity of condition",
        description=(
            "A subjective assessment of the severity of the condition as evaluated "
            "by the clinician."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    stage: typing.List[fhirtypes.ConditionStageType] | None = Field(  # type: ignore
        None,
        alias="stage",
        title="Stage/grade, usually assessed formally",
        description=(
            "Clinical stage or grade of a condition. May include formal severity "
            "assessments."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Who has the condition?",
        description=(
            "Indicates the patient or group who the condition record is associated "
            "with."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    verificationStatus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="verificationStatus",
        title=(
            "unconfirmed | provisional | differential | confirmed | refuted | "
            "entered-in-error"
        ),
        description=(
            "The verification status to support the clinical status of the "
            "condition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Condition`` according specification,
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
            "clinicalStatus",
            "verificationStatus",
            "category",
            "severity",
            "code",
            "bodySite",
            "subject",
            "encounter",
            "onsetDateTime",
            "onsetAge",
            "onsetPeriod",
            "onsetRange",
            "onsetString",
            "abatementDateTime",
            "abatementAge",
            "abatementPeriod",
            "abatementRange",
            "abatementString",
            "recordedDate",
            "recorder",
            "asserter",
            "stage",
            "evidence",
            "note",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields


class ConditionEvidence(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supporting evidence.
    Supporting evidence / manifestations that are the basis of the Condition's
    verification status, such as evidence that confirmed or refuted the
    condition.
    """

    __resource_type__ = "ConditionEvidence"

    code: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="code",
        title="Manifestation/symptom",
        description=(
            "A manifestation or symptom that led to the recording of this " "condition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="detail",
        title="Supporting information found elsewhere",
        description="Links to other relevant information, including pathology reports.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionEvidence`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "detail"]


class ConditionStage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stage/grade, usually assessed formally.
    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """

    __resource_type__ = "ConditionStage"

    assessment: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="assessment",
        title="Formal record of assessment",
        description=(
            "Reference to a formal record of the evidence on which the staging "
            "assessment is based."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "ClinicalImpression",
                "DiagnosticReport",
                "Observation",
            ],
        },
    )

    summary: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="summary",
        title="Simple summary (disease specific)",
        description=(
            'A simple summary of the stage such as "Stage 3". The determination of '
            "the stage is disease-specific."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Kind of staging",
        description="The kind of staging, such as pathological or clinical staging.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionStage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "summary", "assessment", "type"]
