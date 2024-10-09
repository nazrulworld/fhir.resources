from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Condition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
        title="If/when in resolution/remission",
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

    abatementBoolean: bool | None = Field(  # type: ignore
        None,
        alias="abatementBoolean",
        title="If/when in resolution/remission",
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
    abatementBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_abatementBoolean",
        title="Extension field for ``abatementBoolean``.",
    )

    abatementDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="abatementDateTime",
        title="If/when in resolution/remission",
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
        title="If/when in resolution/remission",
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
        title="If/when in resolution/remission",
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
        title="If/when in resolution/remission",
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

    assertedDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="assertedDate",
        title="Date record was believed accurate",
        description=(
            "The date on which the existance of the Condition was first asserted or"
            " acknowledged."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    assertedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_assertedDate", title="Extension field for ``assertedDate``."
    )

    asserter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="asserter",
        title="Person who asserts this condition",
        description="Individual who is making the condition statement.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "Patient", "RelatedPerson"],
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

    clinicalStatus: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="clinicalStatus",
        title="active | recurrence | inactive | remission | resolved",
        description="The clinical status of the condition.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "active",
                "recurrence",
                "inactive",
                "remission",
                "resolved",
            ],
        },
    )
    clinicalStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_clinicalStatus", title="Extension field for ``clinicalStatus``."
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

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="context",
        title="Encounter or episode when condition first asserted",
        description="Encounter during which the condition was first asserted.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    evidence: typing.List[fhirtypes.ConditionEvidenceType] | None = Field(  # type: ignore
        None,
        alias="evidence",
        title="Supporting evidence",
        description=(
            "Supporting Evidence / manifestations that are the basis on which this "
            "condition is suspected or confirmed."
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
            "This records identifiers associated with this condition that are "
            "defined by business processes and/or used to refer to it when a direct"
            " URL reference to the resource itself is not appropriate (e.g. in CDA "
            "documents, or in written / printed documentation)."
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

    stage: fhirtypes.ConditionStageType | None = Field(  # type: ignore
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

    verificationStatus: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="verificationStatus",
        title=(
            "provisional | differential | confirmed | refuted | entered-in-error | "
            "unknown"
        ),
        description=(
            "The verification status to support the clinical status of the "
            "condition."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "provisional",
                "differential",
                "confirmed",
                "refuted",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    verificationStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_verificationStatus",
        title="Extension field for ``verificationStatus``.",
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
            "context",
            "onsetDateTime",
            "onsetAge",
            "onsetPeriod",
            "onsetRange",
            "onsetString",
            "abatementDateTime",
            "abatementAge",
            "abatementBoolean",
            "abatementPeriod",
            "abatementRange",
            "abatementString",
            "assertedDate",
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
        return one_of_many_fields


class ConditionEvidence(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supporting evidence.
    Supporting Evidence / manifestations that are the basis on which this
    condition is suspected or confirmed.
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionStage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "summary", "assessment"]
