from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalImpression
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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

    changePattern: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="changePattern",
        title=(
            "Change in the status/pattern of a subject's condition since previously"
            " assessed, such as worsening, improving, or no change"
        ),
        description=(
            "Change in the status/pattern of a subject's condition since previously"
            " assessed, such as worsening, improving, or no change.  It is a "
            "subjective assessment of the direction of the change."
        ),
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
        title="The Encounter during which this ClinicalImpression was created",
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

    performer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="performer",
        title="The clinician performing the assessment",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
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
        title=(
            "preparation | in-progress | not-done | on-hold | stopped | completed |"
            " entered-in-error | unknown"
        ),
        description="Identifies the workflow status of the assessment.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "preparation",
                "in-progress",
                "not-done",
                "on-hold",
                "stopped",
                "completed",
                "entered-in-error",
                "unknown",
            ],
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
        description=(
            "Information supporting the clinical impression, which can contain "
            "investigation results."
        ),
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
            "description",
            "subject",
            "encounter",
            "effectiveDateTime",
            "effectivePeriod",
            "date",
            "performer",
            "previous",
            "problem",
            "changePattern",
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

    item: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        None,
        alias="item",
        title="What was found",
        description=(
            "Specific text, code or reference for finding or diagnosis, which may "
            "include ruled-out or resolved conditions."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition", "Observation", "DocumentReference"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClinicalImpressionFinding`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "item", "basis"]
