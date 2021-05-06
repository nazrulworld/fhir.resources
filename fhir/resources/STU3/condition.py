# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Condition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Condition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Detailed information about conditions, problems or diagnoses.
    A clinical condition, problem, diagnosis, or other event, situation, issue,
    or clinical concept that has risen to a level of concern.
    """

    resource_type = Field("Condition", const=True)

    abatementAge: fhirtypes.AgeType = Field(
        None,
        alias="abatementAge",
        title="If/when in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Conditions '
            "are never really resolved, but they can abate."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e abatement[x]
        one_of_many="abatement",
        one_of_many_required=False,
    )

    abatementBoolean: bool = Field(
        None,
        alias="abatementBoolean",
        title="If/when in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Conditions '
            "are never really resolved, but they can abate."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e abatement[x]
        one_of_many="abatement",
        one_of_many_required=False,
    )
    abatementBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_abatementBoolean",
        title="Extension field for ``abatementBoolean``.",
    )

    abatementDateTime: fhirtypes.DateTime = Field(
        None,
        alias="abatementDateTime",
        title="If/when in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Conditions '
            "are never really resolved, but they can abate."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e abatement[x]
        one_of_many="abatement",
        one_of_many_required=False,
    )
    abatementDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_abatementDateTime",
        title="Extension field for ``abatementDateTime``.",
    )

    abatementPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="abatementPeriod",
        title="If/when in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Conditions '
            "are never really resolved, but they can abate."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e abatement[x]
        one_of_many="abatement",
        one_of_many_required=False,
    )

    abatementRange: fhirtypes.RangeType = Field(
        None,
        alias="abatementRange",
        title="If/when in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Conditions '
            "are never really resolved, but they can abate."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e abatement[x]
        one_of_many="abatement",
        one_of_many_required=False,
    )

    abatementString: fhirtypes.String = Field(
        None,
        alias="abatementString",
        title="If/when in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Conditions '
            "are never really resolved, but they can abate."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e abatement[x]
        one_of_many="abatement",
        one_of_many_required=False,
    )
    abatementString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_abatementString", title="Extension field for ``abatementString``."
    )

    assertedDate: fhirtypes.DateTime = Field(
        None,
        alias="assertedDate",
        title="Date record was believed accurate",
        description=(
            "The date on which the existance of the Condition was first asserted or"
            " acknowledged."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    assertedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_assertedDate", title="Extension field for ``assertedDate``."
    )

    asserter: fhirtypes.ReferenceType = Field(
        None,
        alias="asserter",
        title="Person who asserts this condition",
        description="Individual who is making the condition statement.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Patient", "RelatedPerson"],
    )

    bodySite: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodySite",
        title="Anatomical location, if relevant",
        description="The anatomical location where this condition manifests itself.",
        # if property is element of this resource.
        element_property=True,
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="problem-list-item | encounter-diagnosis",
        description="A category assigned to the condition.",
        # if property is element of this resource.
        element_property=True,
    )

    clinicalStatus: fhirtypes.Code = Field(
        None,
        alias="clinicalStatus",
        title="active | recurrence | inactive | remission | resolved",
        description="The clinical status of the condition.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "recurrence", "inactive", "remission", "resolved"],
    )
    clinicalStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_clinicalStatus", title="Extension field for ``clinicalStatus``."
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Identification of the condition, problem or diagnosis",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Encounter or episode when condition first asserted",
        description="Encounter during which the condition was first asserted.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    evidence: typing.List[fhirtypes.ConditionEvidenceType] = Field(
        None,
        alias="evidence",
        title="Supporting evidence",
        description=(
            "Supporting Evidence / manifestations that are the basis on which this "
            "condition is suspected or confirmed."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Ids for this condition",
        description=(
            "This records identifiers associated with this condition that are "
            "defined by business processes and/or used to refer to it when a direct"
            " URL reference to the resource itself is not appropriate (e.g. in CDA "
            "documents, or in written / printed documentation)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Additional information about the Condition",
        description=(
            "Additional information about the Condition. This is a general "
            "notes/comments entry  for description of the Condition, its diagnosis "
            "and prognosis."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    onsetAge: fhirtypes.AgeType = Field(
        None,
        alias="onsetAge",
        title="Estimated or actual date,  date-time, or age",
        description=(
            "Estimated or actual date or date-time  the condition began, in the "
            "opinion of the clinician."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetDateTime: fhirtypes.DateTime = Field(
        None,
        alias="onsetDateTime",
        title="Estimated or actual date,  date-time, or age",
        description=(
            "Estimated or actual date or date-time  the condition began, in the "
            "opinion of the clinician."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )
    onsetDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onsetDateTime", title="Extension field for ``onsetDateTime``."
    )

    onsetPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="onsetPeriod",
        title="Estimated or actual date,  date-time, or age",
        description=(
            "Estimated or actual date or date-time  the condition began, in the "
            "opinion of the clinician."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetRange: fhirtypes.RangeType = Field(
        None,
        alias="onsetRange",
        title="Estimated or actual date,  date-time, or age",
        description=(
            "Estimated or actual date or date-time  the condition began, in the "
            "opinion of the clinician."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )

    onsetString: fhirtypes.String = Field(
        None,
        alias="onsetString",
        title="Estimated or actual date,  date-time, or age",
        description=(
            "Estimated or actual date or date-time  the condition began, in the "
            "opinion of the clinician."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e onset[x]
        one_of_many="onset",
        one_of_many_required=False,
    )
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_onsetString", title="Extension field for ``onsetString``."
    )

    severity: fhirtypes.CodeableConceptType = Field(
        None,
        alias="severity",
        title="Subjective severity of condition",
        description=(
            "A subjective assessment of the severity of the condition as evaluated "
            "by the clinician."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    stage: fhirtypes.ConditionStageType = Field(
        None,
        alias="stage",
        title="Stage/grade, usually assessed formally",
        description=(
            "Clinical stage or grade of a condition. May include formal severity "
            "assessments."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who has the condition?",
        description=(
            "Indicates the patient or group who the condition record is associated "
            "with."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    verificationStatus: fhirtypes.Code = Field(
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
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "provisional",
            "differential",
            "confirmed",
            "refuted",
            "entered-in-error",
            "unknown",
        ],
    )
    verificationStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1112(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supporting evidence.
    Supporting Evidence / manifestations that are the basis on which this
    condition is suspected or confirmed.
    """

    resource_type = Field("ConditionEvidence", const=True)

    code: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="Manifestation/symptom",
        description=(
            "A manifestation or symptom that led to the recording of this " "condition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    detail: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="detail",
        title="Supporting information found elsewhere",
        description="Links to other relevant information, including pathology reports.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
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

    resource_type = Field("ConditionStage", const=True)

    assessment: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="assessment",
        title="Formal record of assessment",
        description=(
            "Reference to a formal record of the evidence on which the staging "
            "assessment is based."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ClinicalImpression", "DiagnosticReport", "Observation"],
    )

    summary: fhirtypes.CodeableConceptType = Field(
        None,
        alias="summary",
        title="Simple summary (disease specific)",
        description=(
            'A simple summary of the stage such as "Stage 3". The determination of '
            "the stage is disease-specific."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionStage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "summary", "assessment"]
