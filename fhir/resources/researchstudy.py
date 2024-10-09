from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ResearchStudy(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Investigation to increase healthcare-related patient-independent knowledge.
    A scientific study of nature that sometimes includes processes involved in
    health and disease. For example, clinical trials are research studies that
    involve people. These studies may be related to new ways to screen,
    prevent, diagnose, and treat disease. They may also study certain outcomes
    and certain groups of people by looking at data collected in the past or
    future.
    """

    __resource_type__ = "ResearchStudy"

    associatedParty: typing.List[fhirtypes.ResearchStudyAssociatedPartyType] | None = Field(  # type: ignore
        None,
        alias="associatedParty",
        title="Sponsors, collaborators, and other parties",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    classifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="classifier",
        title="Classification for the study",
        description=(
            "Additional grouping mechanism or categorization of a research study. "
            "Example: FDA regulated device, FDA regulated drug, MPG Paragraph 23b "
            "(a German legal requirement), IRB-exempt, etc. Implementation Note: do"
            " not use the classifier element to support existing semantics that are"
            " already supported thru explicit elements in the resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    comparisonGroup: typing.List[fhirtypes.ResearchStudyComparisonGroupType] | None = Field(  # type: ignore
        None,
        alias="comparisonGroup",
        title="Defined path through the study for a subject",
        description=(
            "Describes an expected event or sequence of events for one of the "
            "subjects of a study. E.g. for a living subject: exposure to drug A, "
            "wash-out, exposure to drug B, wash-out, follow-up. E.g. for a "
            "stability study: {store sample from lot A at 25 degrees for 1 month}, "
            "{store sample from lot A at 40 degrees for 1 month}."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    condition: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="condition",
        title="Condition being studied",
        description=(
            "The condition that is the focus of the study.  For example, In a study"
            " to examine risk factors for Lupus, might have as an inclusion "
            'criterion "healthy volunteer", but the target condition code would be '
            "a Lupus SNOMED code."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date the resource last changed",
        description=(
            "The date (and optionally time) when the ResearchStudy Resource was "
            "last significantly changed. The date must change when the business "
            "version changes and it must change if the status code changes. In "
            "addition, it should change when the substantive content of the "
            "ResearchStudy Resource changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Detailed narrative of the study",
        description=(
            "A detailed and human-readable narrative of the study. E.g., study "
            "abstract."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    descriptionSummary: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="descriptionSummary",
        title="Brief text explaining the study",
        description="A brief text for explaining the study.",
        json_schema_extra={
            "element_property": True,
        },
    )
    descriptionSummary__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_descriptionSummary",
        title="Extension field for ``descriptionSummary``.",
    )

    focus: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="focus",
        title="Drugs, devices, etc. under study",
        description=(
            "The medication(s), food(s), therapy(ies), device(s) or other concerns "
            "or interventions that the study is seeking to gain more information "
            "about."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Medication",
                "MedicinalProductDefinition",
                "SubstanceDefinition",
                "EvidenceVariable",
            ],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for study",
        description=(
            "Identifiers assigned to this research study by the sponsor or other "
            "systems."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    keyword: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="keyword",
        title="Used to search for the study",
        description="Key terms to aid in searching for or filtering the study.",
        json_schema_extra={
            "element_property": True,
        },
    )

    label: typing.List[fhirtypes.ResearchStudyLabelType] | None = Field(  # type: ignore
        None,
        alias="label",
        title="Additional names for the study",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this study (computer friendly)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="Comments made about the study",
        description=(
            "Comments made about the study by the performer, subject or other "
            "participants."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    objective: typing.List[fhirtypes.ResearchStudyObjectiveType] | None = Field(  # type: ignore
        None,
        alias="objective",
        title="A goal for the study",
        description=(
            "A goal that the study is aiming to achieve in terms of a scientific "
            "question to be answered by the analysis of data collected during the "
            "study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    outcomeMeasure: typing.List[fhirtypes.ResearchStudyOutcomeMeasureType] | None = Field(  # type: ignore
        None,
        alias="outcomeMeasure",
        title="A variable measured during the study",
        description=(
            'An "outcome measure", "endpoint", "effect measure" or "measure of '
            'effect" is a specific measurement or observation used to quantify the '
            "effect of experimental variables on the participants in a study, or "
            "for observational studies, to describe patterns of diseases or traits "
            "or associations with exposures, risk factors or treatment."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="Part of larger study",
        description=(
            "A larger research study of which this particular study is a component "
            "or step."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ResearchStudy"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="When the study began and ended",
        description=(
            "Identifies the start date and the expected (or actual, depending on "
            "status) end date for the study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    phase: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="phase",
        title=(
            "n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 | "
            "phase-2-phase-3 | phase-3 | phase-4"
        ),
        description=(
            "The stage in the progression of a therapy from initial experimental "
            "use in humans in clinical trials to post-market evaluation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    primaryPurposeType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="primaryPurposeType",
        title=(
            "treatment | prevention | diagnostic | supportive-care | screening | "
            "health-services-research | basic-science | device-feasibility"
        ),
        description=(
            "The type of study based upon the intent of the study activities. A "
            "classification of the intent of the study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    progressStatus: typing.List[fhirtypes.ResearchStudyProgressStatusType] | None = Field(  # type: ignore
        None,
        alias="progressStatus",
        title="Status of study with time for that status",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    protocol: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="protocol",
        title="Steps followed in executing study",
        description=(
            "The set of steps expected to be performed as part of the execution of "
            "the study."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["PlanDefinition"],
        },
    )

    recruitment: fhirtypes.ResearchStudyRecruitmentType | None = Field(  # type: ignore
        None,
        alias="recruitment",
        title="Target or actual group of participants enrolled in study",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    region: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="region",
        title="Geographic area for the study",
        description=(
            "A country, state or other area where the study is taking place rather "
            "than its precise geographic location or address."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        None,
        alias="relatedArtifact",
        title="References, URLs, and attachments",
        description=(
            "Citations, references, URLs and other related documents.  When using "
            "relatedArtifact to share URLs, the relatedArtifact.type will often be "
            'set to one of "documentation" or "supported-with" and the URL value '
            "will often be in relatedArtifact.document.url but another possible "
            "location is relatedArtifact.resource when it is a canonical URL."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    result: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="result",
        title="Link to results generated during the study",
        description=(
            "Link to one or more sets of results generated by the study.  Could "
            "also link to a research registry holding the results such as "
            "ClinicalTrials.gov."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["EvidenceReport", "Citation", "DiagnosticReport"],
        },
    )

    site: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="site",
        title="Facility where study activities are conducted",
        description="A facility in which study activities are conducted.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location", "ResearchStudy", "Organization"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The publication state of the resource (not of the study).",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    studyDesign: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="studyDesign",
        title="Classifications of the study design characteristics",
        description=(
            "Codes categorizing the type of study such as investigational vs. "
            "observational, type of blinding, type of randomization, safety vs. "
            "efficacy, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Human readable name of the study",
        description="The human readable name of the research study.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Canonical identifier for this study resource",
        description=(
            "Canonical identifier for this study resource, represented as a "
            "globally unique URI."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="The business version for the study record",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    whyStopped: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="whyStopped",
        title=(
            "accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-"
            "study-progress | temporarily-closed-per-study-design"
        ),
        description=(
            "A description and/or code explaining the premature termination of the "
            "study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudy`` according specification,
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
            "url",
            "identifier",
            "version",
            "name",
            "title",
            "label",
            "protocol",
            "partOf",
            "relatedArtifact",
            "date",
            "status",
            "primaryPurposeType",
            "phase",
            "studyDesign",
            "focus",
            "condition",
            "keyword",
            "region",
            "descriptionSummary",
            "description",
            "period",
            "site",
            "note",
            "classifier",
            "associatedParty",
            "progressStatus",
            "whyStopped",
            "recruitment",
            "comparisonGroup",
            "objective",
            "outcomeMeasure",
            "result",
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


class ResearchStudyAssociatedParty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Sponsors, collaborators, and other parties.
    """

    __resource_type__ = "ResearchStudyAssociatedParty"

    classifier: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="classifier",
        title="nih | fda | government | nonprofit | academic | industry",
        description="A categorization other than role for the associated party.",
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name of associated party",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    party: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="party",
        title=(
            "Individual or organization associated with study (use practitionerRole"
            " to specify their organisation)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    period: typing.List[fhirtypes.PeriodType] | None = Field(  # type: ignore
        None,
        alias="period",
        title="When active in the role",
        description=(
            "Identifies the start date and the end date of the associated party in "
            "the role."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    role: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="role",
        title=(
            "sponsor | lead-sponsor | sponsor-investigator | primary-investigator |"
            " collaborator | funding-source | general-contact | recruitment-contact"
            " | sub-investigator | study-director | study-chair"
        ),
        description="Type of association.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyAssociatedParty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "role",
            "period",
            "classifier",
            "party",
        ]


class ResearchStudyComparisonGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defined path through the study for a subject.
    Describes an expected event or sequence of events for one of the subjects
    of a study. E.g. for a living subject: exposure to drug A, wash-out,
    exposure to drug B, wash-out, follow-up. E.g. for a stability study: {store
    sample from lot A at 25 degrees for 1 month}, {store sample from lot A at
    40 degrees for 1 month}.
    """

    __resource_type__ = "ResearchStudyComparisonGroup"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Short explanation of study path",
        description=(
            "A succinct description of the path through the study that would be "
            "followed by a subject adhering to this comparisonGroup."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    intendedExposure: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="intendedExposure",
        title="Interventions or exposures in this comparisonGroup or cohort",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["EvidenceVariable"],
        },
    )

    linkId: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="linkId",
        title=(
            "Allows the comparisonGroup for the study and the comparisonGroup for "
            "the subject to be linked easily"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Label for study comparisonGroup",
        description="Unique, human-readable label for this comparisonGroup of the study.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    observedGroup: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="observedGroup",
        title="Group of participants who were enrolled in study comparisonGroup",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Categorization of study comparisonGroup",
        description=(
            "Categorization of study comparisonGroup, e.g. experimental, active "
            "comparator, placebo comparater."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyComparisonGroup`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "name",
            "type",
            "description",
            "intendedExposure",
            "observedGroup",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
        return required_fields


class ResearchStudyLabel(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional names for the study.
    """

    __resource_type__ = "ResearchStudyLabel"

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "primary | official | scientific | plain-language | subtitle | short-"
            "title | acronym | earlier-title | language | auto-translated | human-"
            "use | machine-use | duplicate-uid"
        ),
        description="Kind of name.",
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="value",
        title="The name",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyLabel`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "value"]


class ResearchStudyObjective(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A goal for the study.
    A goal that the study is aiming to achieve in terms of a scientific
    question to be answered by the analysis of data collected during the study.
    """

    __resource_type__ = "ResearchStudyObjective"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Description of the objective",
        description=(
            "Free text description of the objective of the study.  This is what the"
            " study is trying to achieve rather than how it is going to achieve it "
            "(see ResearchStudy.description)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Label for the objective",
        description="Unique, human-readable label for this objective of the study.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="primary | secondary | exploratory",
        description="The kind of study objective.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyObjective`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "type", "description"]


class ResearchStudyOutcomeMeasure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A variable measured during the study.
    An "outcome measure", "endpoint", "effect measure" or "measure of effect"
    is a specific measurement or observation used to quantify the effect of
    experimental variables on the participants in a study, or for observational
    studies, to describe patterns of diseases or traits or associations with
    exposures, risk factors or treatment.
    """

    __resource_type__ = "ResearchStudyOutcomeMeasure"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Description of the outcome",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Label for the outcome",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    reference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="reference",
        title="Structured outcome definition",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["EvidenceVariable"],
        },
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="primary | secondary | exploratory",
        description=(
            "The parameter or characteristic being assessed as one of the values by"
            " which the study is assessed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyOutcomeMeasure`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "type",
            "description",
            "reference",
        ]


class ResearchStudyProgressStatus(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Status of study with time for that status.
    """

    __resource_type__ = "ResearchStudyProgressStatus"

    actual: bool | None = Field(  # type: ignore
        None,
        alias="actual",
        title="Actual if true else anticipated",
        description=(
            "An indication of whether or not the date is a known date when the "
            "state changed or will change. A value of true indicates a known date. "
            "A value of false indicates an estimated date."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_actual", title="Extension field for ``actual``."
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="period",
        title="Date range",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    state: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="state",
        title="Label for status or state (e.g. recruitment status)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyProgressStatus`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "state", "actual", "period"]


class ResearchStudyRecruitment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Target or actual group of participants enrolled in study.
    """

    __resource_type__ = "ResearchStudyRecruitment"

    actualGroup: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="actualGroup",
        title="Group of participants who were enrolled in study",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    actualNumber: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="actualNumber",
        title="Actual total number of participants enrolled in study",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    actualNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_actualNumber", title="Extension field for ``actualNumber``."
    )

    eligibility: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="eligibility",
        title="Inclusion and exclusion criteria",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group", "EvidenceVariable"],
        },
    )

    targetNumber: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="targetNumber",
        title="Estimated total number of participants to be enrolled",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    targetNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_targetNumber", title="Extension field for ``targetNumber``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchStudyRecruitment`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "targetNumber",
            "actualNumber",
            "eligibility",
            "actualGroup",
        ]
