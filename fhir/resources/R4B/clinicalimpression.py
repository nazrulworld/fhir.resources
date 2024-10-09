from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalImpression
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ClinicalImpression(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A clinical assessment performed when planning treatments and management
    strategies for a patient.
    A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments are
    often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow. This resource is called
    "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion
    with the recording of assessment tools such as Apgar score.
    """

    __resource_type__ = "ClinicalImpression"

    assessor: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="assessor",
        title="The clinician performing the assessment",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Kind of assessment performed",
        description="Categorizes the type of clinical assessment performed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="When the assessment was documented",
        description="Indicates when the documentation of the assessment was complete.",
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Why/how the assessment was performed",
        description=(
            "A summary of the context and/or cause of the assessment - why / where "
            "it was performed, and what patient events/status prompted it."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    effectiveDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="effectiveDateTime",
        title="Time of assessment",
        description="The point in time or period over which the subject was assessed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e effective[x]
            "one_of_many": "effective",
            "one_of_many_required": False,
        },
    )
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_effectiveDateTime",
        title="Extension field for ``effectiveDateTime``.",
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="effectivePeriod",
        title="Time of assessment",
        description="The point in time or period over which the subject was assessed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e effective[x]
            "one_of_many": "effective",
            "one_of_many_required": False,
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="encounter",
        title="Encounter created as part of",
        description=(
            "The Encounter during which this ClinicalImpression was created or to "
            "which the creation of this record is tightly associated."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    finding: typing.List[fhirtypes.ClinicalImpressionFindingType] | None = Field(  # type: ignore
        None,
        alias="finding",
        title="Possible or likely findings and diagnoses",
        description=(
            "Specific findings or diagnoses that were considered likely or relevant"
            " to ongoing treatment."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Business identifiers assigned to this clinical impression by the "
            "performer or other systems which remain constant as the resource is "
            "updated and propagates from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    investigation: typing.List[fhirtypes.ClinicalImpressionInvestigationType] | None = Field(  # type: ignore
        None,
        alias="investigation",
        title="One or more sets of investigations (signs, symptoms, etc.)",
        description=(
            "One or more sets of investigations (signs, symptoms, etc.). The actual"
            " grouping of investigations varies greatly depending on the type and "
            "context of the assessment. These investigations may include data "
            "generated during the assessment process, or data previously generated "
            "and recorded that is pertinent to the outcomes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments made about the ClinicalImpression",
        description=(
            "Commentary about the impression, typically recorded after the "
            "impression itself was made, though supplemental notes by the original "
            "author could also appear."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    previous: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="previous",
        title="Reference to last assessment",
        description=(
            "A reference to the last assessment that was conducted on this patient."
            " Assessments are often/usually ongoing in nature; a care provider "
            "(practitioner or team) will make new assessments on an ongoing basis "
            "as new data arises or the patient's conditions changes."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ClinicalImpression"],
        },
    )

    problem: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="problem",
        title="Relevant impressions of patient state",
        description="A list of the relevant problems/conditions for a patient.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition", "AllergyIntolerance"],
        },
    )

    prognosisCodeableConcept: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="prognosisCodeableConcept",
        title="Estimate of likely outcome",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    prognosisReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="prognosisReference",
        title="RiskAssessment expressing likely outcome",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["RiskAssessment"],
        },
    )

    protocol: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="protocol",
        title="Clinical Protocol followed",
        description=(
            "Reference to a specific published clinical protocol that was followed "
            "during this assessment, and/or that provides evidence in support of "
            "the diagnosis."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    protocol__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_protocol", title="Extension field for ``protocol``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="in-progress | completed | entered-in-error",
        description="Identifies the workflow status of the assessment.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["in-progress", "completed", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="statusReason",
        title="Reason for current status",
        description="Captures the reason for the current state of the ClinicalImpression.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Patient or group assessed",
        description="The patient or group of individuals assessed as part of this record.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    summary: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="summary",
        title="Summary of the assessment",
        description="A text summary of the investigations and the diagnosis.",
        json_schema_extra={
            "element_property": True,
        },
    )
    summary__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_summary", title="Extension field for ``summary``."
    )

    supportingInfo: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supportingInfo",
        title="Information supporting the clinical impression",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalImpression`` according specification,
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
            "status",
            "statusReason",
            "code",
            "description",
            "subject",
            "encounter",
            "effectiveDateTime",
            "effectivePeriod",
            "date",
            "assessor",
            "previous",
            "problem",
            "investigation",
            "protocol",
            "summary",
            "finding",
            "prognosisCodeableConcept",
            "prognosisReference",
            "supportingInfo",
            "note",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields

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
        one_of_many_fields = {"effective": ["effectiveDateTime", "effectivePeriod"]}
        return one_of_many_fields


class ClinicalImpressionFinding(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Possible or likely findings and diagnoses.
    Specific findings or diagnoses that were considered likely or relevant to
    ongoing treatment.
    """

    __resource_type__ = "ClinicalImpressionFinding"

    basis: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="basis",
        title="Which investigations support finding",
        description="Which investigations support finding or diagnosis.",
        json_schema_extra={
            "element_property": True,
        },
    )
    basis__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_basis", title="Extension field for ``basis``."
    )

    itemCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="itemCodeableConcept",
        title="What was found",
        description=(
            "Specific text or code for finding or diagnosis, which may include "
            "ruled-out or resolved conditions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    itemReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="itemReference",
        title="What was found",
        description=(
            "Specific reference for finding or diagnosis, which may include ruled-"
            "out or resolved conditions."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition", "Observation", "Media"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalImpressionFinding`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemCodeableConcept",
            "itemReference",
            "basis",
        ]


class ClinicalImpressionInvestigation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    One or more sets of investigations (signs, symptoms, etc.).
    One or more sets of investigations (signs, symptoms, etc.). The actual
    grouping of investigations varies greatly depending on the type and context
    of the assessment. These investigations may include data generated during
    the assessment process, or data previously generated and recorded that is
    pertinent to the outcomes.
    """

    __resource_type__ = "ClinicalImpressionInvestigation"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="A name/code for the set",
        description=(
            'A name/code for the group ("set") of investigations. Typically, this '
            'will be something like "signs", "symptoms", "clinical", "diagnostic", '
            "but the list is not constrained, and others such groups such as "
            "(exposure|family|travel|nutritional) history may be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    item: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="Record of a specific investigation",
        description="A record of a specific investigation that was undertaken.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Observation",
                "QuestionnaireResponse",
                "FamilyMemberHistory",
                "DiagnosticReport",
                "RiskAssessment",
                "ImagingStudy",
                "Media",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalImpressionInvestigation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "item"]
