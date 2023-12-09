# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Condition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator

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
        title="When in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Some '
            "conditions, such as chronic conditions, are never really resolved, but"
            " they can abate."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e abatement[x]
        one_of_many="abatement",
        one_of_many_required=False,
    )

    abatementDateTime: fhirtypes.DateTime = Field(
        None,
        alias="abatementDateTime",
        title="When in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Some '
            "conditions, such as chronic conditions, are never really resolved, but"
            " they can abate."
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
        title="When in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Some '
            "conditions, such as chronic conditions, are never really resolved, but"
            " they can abate."
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
        title="When in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Some '
            "conditions, such as chronic conditions, are never really resolved, but"
            " they can abate."
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
        title="When in resolution/remission",
        description=(
            "The date or estimated date that the condition resolved or went into "
            'remission. This is called "abatement" because of the many overloaded '
            'connotations associated with "remission" or "resolution" - Some '
            "conditions, such as chronic conditions, are never really resolved, but"
            " they can abate."
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

    clinicalStatus: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="clinicalStatus",
        title=(
            "active | recurrence | relapse | inactive | remission | resolved | "
            "unknown"
        ),
        description="The clinical status of the condition.",
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Identification of the condition, problem or diagnosis",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="The Encounter during which this Condition was created",
        description=(
            "The Encounter during which this Condition was created or to which the "
            "creation of this record is tightly associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    evidence: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="evidence",
        title="Supporting evidence for the verification status",
        description=(
            "Supporting evidence / manifestations that are the basis of the "
            "Condition's verification status, such as evidence that confirmed or "
            "refuted the condition."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Ids for this condition",
        description=(
            "Business identifiers assigned to this condition by the performer or "
            "other systems which remain constant as the resource is updated and "
            "propagates from server to server."
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

    participant: typing.List[fhirtypes.ConditionParticipantType] = Field(
        None,
        alias="participant",
        title=(
            "Who or what participated in the activities related to the condition "
            "and how they were involved"
        ),
        description=(
            "Indicates who or what participated in the activities related to the "
            "condition and how they were involved."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    recordedDate: fhirtypes.DateTime = Field(
        None,
        alias="recordedDate",
        title="Date condition was first recorded",
        description=(
            "The recordedDate represents when this particular Condition record was "
            "created in the system, which is often a system-generated date."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    recordedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_recordedDate", title="Extension field for ``recordedDate``."
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

    stage: typing.List[fhirtypes.ConditionStageType] = Field(
        None,
        alias="stage",
        title="Stage/grade, usually assessed formally",
        description=(
            'A simple summary of the stage such as "Stage 3" or "Early Onset". The '
            "determination of the stage is disease-specific, such as cancer, "
            "retinopathy of prematurity, kidney diseases, Alzheimer's, or Parkinson"
            " disease."
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

    verificationStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="verificationStatus",
        title=(
            "unconfirmed | provisional | differential | confirmed | refuted | "
            "entered-in-error"
        ),
        description=(
            "The verification status to support the clinical status of the "
            "condition.  The verification status pertains to the condition, itself,"
            " not to any specific condition attribute."
        ),
        # if property is element of this resource.
        element_property=True,
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
            "participant",
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


class ConditionParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who or what participated in the activities related to the condition and how
    they were involved.
    Indicates who or what participated in the activities related to the
    condition and how they were involved.
    """

    resource_type = Field("ConditionParticipant", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Who or what participated in the activities related to the condition",
        description=(
            "Indicates who or what participated in the activities related to the "
            "condition."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Patient",
            "RelatedPerson",
            "Device",
            "Organization",
            "CareTeam",
        ],
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type of involvement",
        description=(
            "Distinguishes the type of involvement of the actor in the activities "
            "related to the condition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionParticipant`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]


class ConditionStage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stage/grade, usually assessed formally.
    A simple summary of the stage such as "Stage 3" or "Early Onset". The
    determination of the stage is disease-specific, such as cancer, retinopathy
    of prematurity, kidney diseases, Alzheimer's, or Parkinson disease.
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
            'A simple summary of the stage such as "Stage 3" or "Early Onset". The '
            "determination of the stage is disease-specific, such as cancer, "
            "retinopathy of prematurity, kidney diseases, Alzheimer's, or Parkinson"
            " disease."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Kind of staging",
        description="The kind of staging, such as pathological or clinical staging.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ConditionStage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "summary", "assessment", "type"]
