from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Measure
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Measure(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A quality measure definition.
    The Measure resource provides the definition of a quality measure.
    """

    __resource_type__ = "Measure"

    approvalDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="approvalDate",
        title="When the measure was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    author: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="author",
        title="Who authored the content",
        description=(
            "An individiual or organization primarily involved in the creation and "
            "maintenance of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    basis: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="basis",
        title="Population basis",
        description=(
            "The population basis specifies the type of elements in the population."
            " For a subject-based measure, this is boolean (because the subject and"
            " the population basis are the same, and the population criteria define"
            " yes/no values for each individual in the population). For measures "
            "that have a population basis that is different than the subject, this "
            "element specifies the type of the population basis. For example, an "
            "encounter-based measure has a subject of Patient and a population "
            "basis of Encounter, and the population criteria all return lists of "
            "Encounters."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    basis__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_basis", title="Extension field for ``basis``."
    )

    clinicalRecommendationStatement: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="clinicalRecommendationStatement",
        title="Summary of clinical guidelines",
        description=(
            "Provides a summary of relevant clinical guidelines or other clinical "
            "recommendations supporting the measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    clinicalRecommendationStatement__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_clinicalRecommendationStatement",
        title="Extension field for ``clinicalRecommendationStatement``.",
    )

    compositeScoring: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="compositeScoring",
        title="opportunity | all-or-nothing | linear | weighted",
        description=(
            "If this is a composite measure, the scoring method used to combine the"
            " component measures to determine the composite score."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the measure and/or its contents. "
            "Copyright statements are generally legal restrictions on the use and "
            "publishing of the measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    copyrightLabel: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="copyrightLabel",
        title="Copyright holder and year(s)",
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyrightLabel", title="Extension field for ``copyrightLabel``."
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the measure was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the measure changes."
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
        title="Natural language description of the measure",
        description=(
            "A free text natural language description of the measure from a "
            "consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    disclaimer: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="disclaimer",
        title="Disclaimer for use of the measure or its referenced content",
        description=(
            "Notices and disclaimers regarding the use of the measure or related to"
            " intellectual property (such as code systems) referenced by the "
            "measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    disclaimer__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_disclaimer", title="Extension field for ``disclaimer``."
    )

    editor: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="editor",
        title="Who edited the content",
        description=(
            "An individual or organization primarily responsible for internal "
            "coherence of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="effectivePeriod",
        title="When the measure is expected to be used",
        description=(
            "The period during which the measure content was or is planned to be in"
            " active use."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    endorser: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="endorser",
        title="Who endorsed the content",
        description=(
            "An individual or organization asserted by the publisher to be "
            "responsible for officially endorsing the content for use in some "
            "setting."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this measure is authored for testing "
            "purposes (or education/evaluation/marketing) and is not intended to be"
            " used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    group: typing.List[fhirtypes.MeasureGroupType] | None = Field(  # type: ignore
        None,
        alias="group",
        title="Population criteria group",
        description="A group of population criteria for the measure.",
        json_schema_extra={
            "element_property": True,
        },
    )

    guidance: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="guidance",
        title="Additional guidance for implementers (deprecated)",
        description=(
            "Additional guidance for the measure including how it can be used in a "
            "clinical context, and the intent of the measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    guidance__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_guidance", title="Extension field for ``guidance``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the measure",
        description=(
            "A formal identifier that is used to identify this measure when it is "
            "represented in other formats, or referenced in a specification, model,"
            " design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    improvementNotation: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="improvementNotation",
        title="increase | decrease",
        description=(
            "Information on whether an increase or decrease in score is the "
            "preferred result (e.g., a higher score indicates better quality OR a "
            "lower score indicates better quality OR quality is within a range)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for measure (if applicable)",
        description=(
            "A legal or geographic region in which the measure is intended to be "
            "used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lastReviewDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="lastReviewDate",
        title="When the measure was last reviewed by the publisher",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    library: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="library",
        title="Logic used by the measure",
        description=(
            "A reference to a Library resource containing the formal logic used by "
            "the measure."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Library"],
        },
    )
    library__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_library", title="Extension field for ``library``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this measure (computer friendly)",
        description=(
            "A natural language name identifying the measure. This name should be "
            "usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="Why this measure is defined",
        description=(
            "Explanation of why this measure is needed and why it has been designed"
            " as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    rateAggregation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="rateAggregation",
        title="How is rate aggregation performed for this measure",
        description=(
            "Describes how to combine the information calculated, based on logic in"
            " each of several populations, into one summarized result."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    rateAggregation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_rateAggregation", title="Extension field for ``rateAggregation``."
    )

    rationale: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="rationale",
        title="Detailed description of why the measure exists",
        description=(
            "Provides a succinct statement of the need for the measure. Usually "
            "includes statements pertaining to importance criterion: impact, gap in"
            " care, and evidence."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    rationale__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_rationale", title="Extension field for ``rationale``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        None,
        alias="relatedArtifact",
        title="Additional documentation, citations, etc",
        description=(
            "Related artifacts such as additional documentation, justification, or "
            "bibliographic references."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="reviewer",
        title="Who reviewed the content",
        description=(
            "An individual or organization asserted by the publisher to be "
            "primarily responsible for review of some aspect of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    riskAdjustment: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="riskAdjustment",
        title="How risk adjustment is applied for this measure",
        description=(
            "A description of the risk adjustment factors that may impact the "
            "resulting score for the measure and how they may be accounted for when"
            " computing and reporting measure results."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    riskAdjustment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_riskAdjustment", title="Extension field for ``riskAdjustment``."
    )

    scoring: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="scoring",
        title="proportion | ratio | continuous-variable | cohort",
        description=(
            "Indicates how the calculation is performed for the measure, including "
            "proportion, ratio, continuous-variable, and cohort. The value set is "
            "extensible, allowing additional measure scoring types to be "
            "represented."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    scoringUnit: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="scoringUnit",
        title="What units?",
        description=(
            "Defines the expected units of measure for the measure score. This "
            "element SHOULD be specified as a UCUM unit."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this measure. Enables tracking the life-cycle of the "
            "content."
        ),
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

    subjectCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="subjectCodeableConcept",
        title=(
            "E.g. Patient, Practitioner, RelatedPerson, Organization, Location, "
            "Device"
        ),
        description=(
            "The intended subjects for the measure. If this element is not "
            "provided, a Patient subject is assumed, but the subject of the measure"
            " can be anything."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
        },
    )

    subjectReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subjectReference",
        title=(
            "E.g. Patient, Practitioner, RelatedPerson, Organization, Location, "
            "Device"
        ),
        description=(
            "The intended subjects for the measure. If this element is not "
            "provided, a Patient subject is assumed, but the subject of the measure"
            " can be anything."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    subtitle: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="subtitle",
        title="Subordinate title of the measure",
        description=(
            "An explanatory or alternate title for the measure giving additional "
            "information about its content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_subtitle", title="Extension field for ``subtitle``."
    )

    supplementalData: typing.List[fhirtypes.MeasureSupplementalDataType] | None = Field(  # type: ignore
        None,
        alias="supplementalData",
        title="What other data should be reported with the measure",
        description=(
            "The supplemental data criteria for the measure report, specified as "
            "either the name of a valid CQL expression within a referenced library,"
            " or a valid FHIR Resource Path."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    term: typing.List[fhirtypes.MeasureTermType] | None = Field(  # type: ignore
        None,
        alias="term",
        title="Defined terms used in the measure documentation",
        description="Provides a description of an individual term used within the measure.",
        json_schema_extra={
            "element_property": True,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this measure (human friendly)",
        description="A short, descriptive, user-friendly title for the measure.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    topic: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="topic",
        title=(
            "The category of the measure, such as Education, Treatment, Assessment,"
            " etc"
        ),
        description=(
            "Descriptive topics related to the content of the measure. Topics "
            "provide a high-level categorization grouping types of measures that "
            "can be useful for filtering and searching."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="process | outcome | structure | patient-reported-outcome | composite",
        description=(
            "Indicates whether the measure is used to examine a process, an outcome"
            " over time, a patient-reported outcome, or a structure measure such as"
            " utilization."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this measure, represented as a URI (globally "
            "unique)"
        ),
        description=(
            "An absolute URI that is used to identify this measure when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " measure is (or will be) published. This URL can be the target of a "
            "canonical reference. It SHALL remain the same when the measure is "
            "stored on different servers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    usage: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="usage",
        title="Describes the clinical usage of the measure",
        description=(
            "A detailed description, from a clinical perspective, of how the "
            "measure is used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_usage", title="Extension field for ``usage``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate measure instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the measure",
        description=(
            "The identifier that is used to identify this version of the measure "
            "when it is referenced in a specification, model, design or instance. "
            "This is an arbitrary value managed by the measure author and is not "
            "expected to be globally unique. For example, it might be a timestamp "
            "(e.g. yyyymmdd) if a managed version is not available. There is also "
            "no expectation that versions can be placed in a lexicographical "
            "sequence. To provide a version consistent with the Decision Support "
            "Service specification, use the format Major.Minor.Revision (e.g. "
            "1.0.0). For more information on versioning knowledge assets, refer to "
            "the Decision Support Service specification. Note that a version is "
            "required for non-experimental active artifacts."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    versionAlgorithmCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )

    versionAlgorithmString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Measure`` according specification,
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
            "versionAlgorithmString",
            "versionAlgorithmCoding",
            "name",
            "title",
            "subtitle",
            "status",
            "experimental",
            "subjectCodeableConcept",
            "subjectReference",
            "basis",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "usage",
            "copyright",
            "copyrightLabel",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "topic",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "relatedArtifact",
            "library",
            "disclaimer",
            "scoring",
            "scoringUnit",
            "compositeScoring",
            "type",
            "riskAdjustment",
            "rateAggregation",
            "rationale",
            "clinicalRecommendationStatement",
            "improvementNotation",
            "term",
            "guidance",
            "group",
            "supplementalData",
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
        one_of_many_fields = {
            "subject": ["subjectCodeableConcept", "subjectReference"],
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"],
        }
        return one_of_many_fields


class MeasureGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Population criteria group.
    A group of population criteria for the measure.
    """

    __resource_type__ = "MeasureGroup"

    basis: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="basis",
        title="Population basis",
        description=(
            "The population basis specifies the type of elements in the population."
            " For a subject-based measure, this is boolean (because the subject and"
            " the population basis are the same, and the population criteria define"
            " yes/no values for each individual in the population). For measures "
            "that have a population basis that is different than the subject, this "
            "element specifies the type of the population basis. For example, an "
            "encounter-based measure has a subject of Patient and a population "
            "basis of Encounter, and the population criteria all return lists of "
            "Encounters."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    basis__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_basis", title="Extension field for ``basis``."
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Meaning of the group",
        description=(
            "Indicates a meaning for the group. This can be as simple as a unique "
            "identifier, or it can establish meaning in a broader context by "
            "drawing from a terminology, allowing groups to be correlated across "
            "measures."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Summary description",
        description="The human readable description of this population group.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    improvementNotation: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="improvementNotation",
        title="increase | decrease",
        description=(
            "Information on whether an increase or decrease in score is the "
            "preferred result (e.g., a higher score indicates better quality OR a "
            "lower score indicates better quality OR quality is within a range)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    library: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="library",
        title="Logic used by the measure group",
        description=(
            "A reference to a Library resource containing the formal logic used by "
            "the measure group."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Library"],
        },
    )
    library__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_library", title="Extension field for ``library``."
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Unique id for group in measure",
        description=(
            "An identifier that is unique within the Measure allowing linkage to "
            "the equivalent item in a MeasureReport resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    population: typing.List[fhirtypes.MeasureGroupPopulationType] | None = Field(  # type: ignore
        None,
        alias="population",
        title="Population criteria",
        description="A population criteria for the measure.",
        json_schema_extra={
            "element_property": True,
        },
    )

    rateAggregation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="rateAggregation",
        title="How is rate aggregation performed for this measure",
        description=(
            "Describes how to combine the information calculated, based on logic in"
            " each of several populations, into one summarized result."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    rateAggregation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_rateAggregation", title="Extension field for ``rateAggregation``."
    )

    scoring: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="scoring",
        title="proportion | ratio | continuous-variable | cohort",
        description=(
            "Indicates how the calculation is performed for the measure, including "
            "proportion, ratio, continuous-variable, and cohort. The value set is "
            "extensible, allowing additional measure scoring types to be "
            "represented."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    scoringUnit: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="scoringUnit",
        title="What units?",
        description=(
            "Defines the expected units of measure for the measure score. This "
            "element SHOULD be specified as a UCUM unit."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    stratifier: typing.List[fhirtypes.MeasureGroupStratifierType] | None = Field(  # type: ignore
        None,
        alias="stratifier",
        title="Stratifier criteria for the measure",
        description=(
            "The stratifier criteria for the measure report, specified as either "
            "the name of a valid CQL expression defined within a referenced library"
            " or a valid FHIR Resource Path."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="subjectCodeableConcept",
        title=(
            "E.g. Patient, Practitioner, RelatedPerson, Organization, Location, "
            "Device"
        ),
        description=(
            "The intended subjects for the measure. If this element is not "
            "provided, a Patient subject is assumed, but the subject of the measure"
            " can be anything."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
        },
    )

    subjectReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="subjectReference",
        title=(
            "E.g. Patient, Practitioner, RelatedPerson, Organization, Location, "
            "Device"
        ),
        description=(
            "The intended subjects for the measure. If this element is not "
            "provided, a Patient subject is assumed, but the subject of the measure"
            " can be anything."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="type",
        title="process | outcome | structure | patient-reported-outcome | composite",
        description=(
            "Indicates whether the measure is used to examine a process, an outcome"
            " over time, a patient-reported outcome, or a structure measure such as"
            " utilization."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureGroup`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "code",
            "description",
            "type",
            "subjectCodeableConcept",
            "subjectReference",
            "basis",
            "scoring",
            "scoringUnit",
            "rateAggregation",
            "improvementNotation",
            "library",
            "population",
            "stratifier",
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
        one_of_many_fields = {"subject": ["subjectCodeableConcept", "subjectReference"]}
        return one_of_many_fields


class MeasureGroupPopulation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Population criteria.
    A population criteria for the measure.
    """

    __resource_type__ = "MeasureGroupPopulation"

    aggregateMethod: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="aggregateMethod",
        title=(
            "Aggregation method for a measure score (e.g. sum, average, median, "
            "minimum, maximum, count)"
        ),
        description=(
            "Specifies which method should be used to aggregate measure observation"
            " values. For most scoring types, this is implied by scoring (e.g. a "
            "proportion measure counts members of the populations). For continuous "
            "variables, however, this information must be specified to ensure "
            "correct calculation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title=(
            "initial-population | numerator | numerator-exclusion | denominator | "
            "denominator-exclusion | denominator-exception | measure-population | "
            "measure-population-exclusion | measure-observation"
        ),
        description="The type of population criteria.",
        json_schema_extra={
            "element_property": True,
        },
    )

    criteria: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="criteria",
        title="The criteria that defines this population",
        description=(
            "An expression that specifies the criteria for the population, "
            "typically the name of an expression in a library."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="The human readable description of this population criteria",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    groupDefinition: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="groupDefinition",
        title="A group resource that defines this population",
        description=(
            "A Group resource that defines this population as a set of "
            "characteristics."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    inputPopulationId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="inputPopulationId",
        title="Which population",
        description=(
            "The id of a population element in this measure that provides the input"
            " for this population criteria. In most cases, the scoring structure of"
            " the measure implies specific relationships (e.g. the Numerator uses "
            "the Denominator as the source in a proportion scoring). In some cases,"
            " however, multiple possible choices exist and must be resolved "
            "explicitly. For example in a ratio measure with multiple initial "
            "populations, the denominator must specify which population should be "
            "used as the starting point."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    inputPopulationId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_inputPopulationId",
        title="Extension field for ``inputPopulationId``.",
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Unique id for population in measure",
        description=(
            "An identifier that is unique within the Measure allowing linkage to "
            "the equivalent population in a MeasureReport resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureGroupPopulation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "code",
            "description",
            "criteria",
            "groupDefinition",
            "inputPopulationId",
            "aggregateMethod",
        ]


class MeasureGroupStratifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratifier criteria for the measure.
    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library or a
    valid FHIR Resource Path.
    """

    __resource_type__ = "MeasureGroupStratifier"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Meaning of the stratifier",
        description=(
            "Indicates a meaning for the stratifier. This can be as simple as a "
            "unique identifier, or it can establish meaning in a broader context by"
            " drawing from a terminology, allowing stratifiers to be correlated "
            "across measures."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    component: typing.List[fhirtypes.MeasureGroupStratifierComponentType] | None = Field(  # type: ignore
        None,
        alias="component",
        title="Stratifier criteria component for the measure",
        description=(
            "A component of the stratifier criteria for the measure report, "
            "specified as either the name of a valid CQL expression defined within "
            "a referenced library or a valid FHIR Resource Path."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    criteria: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="criteria",
        title="How the measure should be stratified",
        description=(
            "An expression that specifies the criteria for the stratifier. This is "
            "typically the name of an expression defined within a referenced "
            "library, but it may also be a path to a stratifier element."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="The human readable description of this stratifier",
        description="The human readable description of this stratifier criteria.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    groupDefinition: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="groupDefinition",
        title="A group resource that defines this population",
        description=(
            "A Group resource that defines this population as a set of "
            "characteristics."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Unique id for stratifier in measure",
        description=(
            "An identifier that is unique within the Measure allowing linkage to "
            "the equivalent item in a MeasureReport resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureGroupStratifier`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "code",
            "description",
            "criteria",
            "groupDefinition",
            "component",
        ]


class MeasureGroupStratifierComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratifier criteria component for the measure.
    A component of the stratifier criteria for the measure report, specified as
    either the name of a valid CQL expression defined within a referenced
    library or a valid FHIR Resource Path.
    """

    __resource_type__ = "MeasureGroupStratifierComponent"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Meaning of the stratifier component",
        description=(
            "Indicates a meaning for the stratifier component. This can be as "
            "simple as a unique identifier, or it can establish meaning in a "
            "broader context by drawing from a terminology, allowing stratifiers to"
            " be correlated across measures."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    criteria: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="criteria",
        title="Component of how the measure should be stratified",
        description=(
            "An expression that specifies the criteria for this component of the "
            "stratifier. This is typically the name of an expression defined within"
            " a referenced library, but it may also be a path to a stratifier "
            "element."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="The human readable description of this stratifier component",
        description="The human readable description of this stratifier criteria component.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    groupDefinition: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="groupDefinition",
        title="A group resource that defines this population",
        description=(
            "A Group resource that defines this population as a set of "
            "characteristics."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Unique id for stratifier component in measure",
        description=(
            "An identifier that is unique within the Measure allowing linkage to "
            "the equivalent item in a MeasureReport resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureGroupStratifierComponent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "code",
            "description",
            "criteria",
            "groupDefinition",
        ]


class MeasureSupplementalData(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What other data should be reported with the measure.
    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """

    __resource_type__ = "MeasureSupplementalData"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Meaning of the supplemental data",
        description=(
            "Indicates a meaning for the supplemental data. This can be as simple "
            "as a unique identifier, or it can establish meaning in a broader "
            "context by drawing from a terminology, allowing supplemental data to "
            "be correlated across measures."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    criteria: fhirtypes.ExpressionType = Field(  # type: ignore
        ...,
        alias="criteria",
        title="Expression describing additional data to be reported",
        description=(
            "The criteria for the supplemental data. This is typically the name of "
            "a valid expression defined within a referenced library, but it may "
            "also be a path to a specific data element. The criteria defines the "
            "data to be returned for this element."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="The human readable description of this supplemental data",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="linkId",
        title="Unique id for supplementalData in measure",
        description=(
            "An identifier that is unique within the Measure allowing linkage to "
            "the equivalent item in a MeasureReport resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_linkId", title="Extension field for ``linkId``."
    )

    usage: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="usage",
        title="supplemental-data | risk-adjustment-factor",
        description=(
            "An indicator of the intended usage for the supplemental data element. "
            "Supplemental data indicates the data is additional information "
            "requested to augment the measure information. Risk adjustment factor "
            "indicates the data is additional information used to calculate risk "
            "adjustment factors when applying a risk model to the measure "
            "calculation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureSupplementalData`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "code",
            "usage",
            "description",
            "criteria",
        ]


class MeasureTerm(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defined terms used in the measure documentation.
    Provides a description of an individual term used within the measure.
    """

    __resource_type__ = "MeasureTerm"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="What term?",
        description="A codeable representation of the defined term.",
        json_schema_extra={
            "element_property": True,
        },
    )

    definition: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="definition",
        title="Meaning of the term",
        description="Provides a definition for the term as used within the measure.",
        json_schema_extra={
            "element_property": True,
        },
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_definition", title="Extension field for ``definition``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MeasureTerm`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "definition"]
