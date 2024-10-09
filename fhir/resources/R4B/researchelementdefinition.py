from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ResearchElementDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A population, intervention, or exposure definition.
    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """

    __resource_type__ = "ResearchElementDefinition"

    approvalDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="approvalDate",
        title="When the research element definition was approved by publisher",
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

    characteristic: typing.List[fhirtypes.ResearchElementDefinitionCharacteristicType] = Field(  # type: ignore
        ...,
        alias="characteristic",
        title="What defines the members of the research element",
        description=(
            "A characteristic that defines the members of the research element. "
            'Multiple characteristics are applied with "and" semantics.'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    comment: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Used for footnotes or explanatory notes",
        description=(
            "A human-readable string to clarify or explain concepts about the "
            "resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
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
            "A copyright statement relating to the research element definition "
            "and/or its contents. Copyright statements are generally legal "
            "restrictions on the use and publishing of the research element "
            "definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the research element definition "
            "was published. The date must change when the business version changes "
            "and it must change if the status code changes. In addition, it should "
            "change when the substantive content of the research element definition"
            " changes."
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
        title="Natural language description of the research element definition",
        description=(
            "A free text natural language description of the research element "
            "definition from a consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
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
        title="When the research element definition is expected to be used",
        description=(
            "The period during which the research element definition content was or"
            " is planned to be in active use."
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
            "An individual or organization responsible for officially endorsing the"
            " content for use in some setting."
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
            "A Boolean value to indicate that this research element definition is "
            "authored for testing purposes (or education/evaluation/marketing) and "
            "is not intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the research element definition",
        description=(
            "A formal identifier that is used to identify this research element "
            "definition when it is represented in other formats, or referenced in a"
            " specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for research element definition (if applicable)",
        description=(
            "A legal or geographic region in which the research element definition "
            "is intended to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lastReviewDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="lastReviewDate",
        title="When the research element definition was last reviewed",
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
        title="Logic used by the ResearchElementDefinition",
        description=(
            "A reference to a Library resource containing the formal logic used by "
            "the ResearchElementDefinition."
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
        title="Name for this research element definition (computer friendly)",
        description=(
            "A natural language name identifying the research element definition. "
            "This name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
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
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the research"
            " element definition."
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
        title="Why this research element definition is defined",
        description=(
            "Explanation of why this research element definition is needed and why "
            "it has been designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        None,
        alias="relatedArtifact",
        title="Additional documentation, citations, etc.",
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
            "An individual or organization primarily responsible for review of some"
            " aspect of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    shortTitle: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="shortTitle",
        title="Title for use in informal contexts",
        description=(
            "The short title provides an alternate title for use in informal "
            "descriptive contexts where the full, formal title is not necessary."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    shortTitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_shortTitle", title="Extension field for ``shortTitle``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this research element definition. Enables tracking the "
            "life-cycle of the content."
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
            "The intended subjects for the ResearchElementDefinition. If this "
            "element is not provided, a Patient subject is assumed, but the subject"
            " of the ResearchElementDefinition can be anything."
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
            "The intended subjects for the ResearchElementDefinition. If this "
            "element is not provided, a Patient subject is assumed, but the subject"
            " of the ResearchElementDefinition can be anything."
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
        title="Subordinate title of the ResearchElementDefinition",
        description=(
            "An explanatory or alternate title for the ResearchElementDefinition "
            "giving additional information about its content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_subtitle", title="Extension field for ``subtitle``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this research element definition (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the research element "
            "definition."
        ),
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
            "The category of the ResearchElementDefinition, such as Education, "
            "Treatment, Assessment, etc."
        ),
        description=(
            "Descriptive topics related to the content of the "
            "ResearchElementDefinition. Topics provide a high-level categorization "
            "grouping types of ResearchElementDefinitions that can be useful for "
            "filtering and searching."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="population | exposure | outcome",
        description=(
            "The type of research element, a population, an exposure, or an " "outcome."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["population", "exposure", "outcome"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this research element definition, represented"
            " as a URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this research element "
            "definition when it is referenced in a specification, model, design or "
            "an instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which at which an "
            "authoritative instance of this research element definition is (or will"
            " be) published. This URL can be the target of a canonical reference. "
            "It SHALL remain the same when the research element definition is "
            "stored on different servers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    usage: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="usage",
        title="Describes the clinical usage of the ResearchElementDefinition",
        description=(
            "A detailed description, from a clinical perspective, of how the "
            "ResearchElementDefinition is used."
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
            "indexing and searching for appropriate research element definition "
            "instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    variableType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="variableType",
        title="dichotomous | continuous | descriptive",
        description=(
            "The type of the outcome (e.g. Dichotomous, Continuous, or " "Descriptive)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["dichotomous", "continuous", "descriptive"],
        },
    )
    variableType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_variableType", title="Extension field for ``variableType``."
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the research element definition",
        description=(
            "The identifier that is used to identify this version of the research "
            "element definition when it is referenced in a specification, model, "
            "design or instance. This is an arbitrary value managed by the research"
            " element definition author and is not expected to be globally unique. "
            "For example, it might be a timestamp (e.g. yyyymmdd) if a managed "
            "version is not available. There is also no expectation that versions "
            "can be placed in a lexicographical sequence. To provide a version "
            "consistent with the Decision Support Service specification, use the "
            "format Major.Minor.Revision (e.g. 1.0.0). For more information on "
            "versioning knowledge assets, refer to the Decision Support Service "
            "specification. Note that a version is required for non-experimental "
            "active artifacts."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchElementDefinition`` according specification,
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
            "shortTitle",
            "subtitle",
            "status",
            "experimental",
            "subjectCodeableConcept",
            "subjectReference",
            "date",
            "publisher",
            "contact",
            "description",
            "comment",
            "useContext",
            "jurisdiction",
            "purpose",
            "usage",
            "copyright",
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
            "type",
            "variableType",
            "characteristic",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext"), ("type", "type__ext")]
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
        one_of_many_fields = {"subject": ["subjectCodeableConcept", "subjectReference"]}
        return one_of_many_fields


class ResearchElementDefinitionCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What defines the members of the research element.
    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """

    __resource_type__ = "ResearchElementDefinitionCharacteristic"

    definitionCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="definitionCanonical",
        title="What code or expression defines members?",
        description=(
            "Define members of the research element using Codes (such as condition,"
            " medication, or observation), Expressions ( using an expression "
            "language such as FHIRPath or CQL) or DataRequirements (such as "
            "Diabetes diagnosis onset in the last year)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e definition[x]
            "one_of_many": "definition",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_definitionCanonical",
        title="Extension field for ``definitionCanonical``.",
    )

    definitionCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="definitionCodeableConcept",
        title="What code or expression defines members?",
        description=(
            "Define members of the research element using Codes (such as condition,"
            " medication, or observation), Expressions ( using an expression "
            "language such as FHIRPath or CQL) or DataRequirements (such as "
            "Diabetes diagnosis onset in the last year)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e definition[x]
            "one_of_many": "definition",
            "one_of_many_required": True,
        },
    )

    definitionDataRequirement: fhirtypes.DataRequirementType | None = Field(  # type: ignore
        None,
        alias="definitionDataRequirement",
        title="What code or expression defines members?",
        description=(
            "Define members of the research element using Codes (such as condition,"
            " medication, or observation), Expressions ( using an expression "
            "language such as FHIRPath or CQL) or DataRequirements (such as "
            "Diabetes diagnosis onset in the last year)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e definition[x]
            "one_of_many": "definition",
            "one_of_many_required": True,
        },
    )

    definitionExpression: fhirtypes.ExpressionType | None = Field(  # type: ignore
        None,
        alias="definitionExpression",
        title="What code or expression defines members?",
        description=(
            "Define members of the research element using Codes (such as condition,"
            " medication, or observation), Expressions ( using an expression "
            "language such as FHIRPath or CQL) or DataRequirements (such as "
            "Diabetes diagnosis onset in the last year)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e definition[x]
            "one_of_many": "definition",
            "one_of_many_required": True,
        },
    )

    exclude: bool | None = Field(  # type: ignore
        None,
        alias="exclude",
        title="Whether the characteristic includes or excludes members",
        description=(
            "When true, members with this characteristic are excluded from the "
            "element."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_exclude", title="Extension field for ``exclude``."
    )

    participantEffectiveDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="participantEffectiveDateTime",
        title="What time period do participants cover",
        description="Indicates what effective period the study covers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e participantEffective[x]
            "one_of_many": "participantEffective",
            "one_of_many_required": False,
        },
    )
    participantEffectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_participantEffectiveDateTime",
        title="Extension field for ``participantEffectiveDateTime``.",
    )

    participantEffectiveDescription: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="participantEffectiveDescription",
        title="What time period do participants cover",
        description="A narrative description of the time period the study covers.",
        json_schema_extra={
            "element_property": True,
        },
    )
    participantEffectiveDescription__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_participantEffectiveDescription",
        title="Extension field for ``participantEffectiveDescription``.",
    )

    participantEffectiveDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="participantEffectiveDuration",
        title="What time period do participants cover",
        description="Indicates what effective period the study covers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e participantEffective[x]
            "one_of_many": "participantEffective",
            "one_of_many_required": False,
        },
    )

    participantEffectiveGroupMeasure: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="participantEffectiveGroupMeasure",
        title=(
            "mean | median | mean-of-mean | mean-of-median | median-of-mean | "
            "median-of-median"
        ),
        description=(
            "Indicates how elements are aggregated within the study effective "
            "period."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "mean",
                "median",
                "mean-of-mean",
                "mean-of-median",
                "median-of-mean",
                "median-of-median",
            ],
        },
    )
    participantEffectiveGroupMeasure__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_participantEffectiveGroupMeasure",
        title="Extension field for ``participantEffectiveGroupMeasure``.",
    )

    participantEffectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="participantEffectivePeriod",
        title="What time period do participants cover",
        description="Indicates what effective period the study covers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e participantEffective[x]
            "one_of_many": "participantEffective",
            "one_of_many_required": False,
        },
    )

    participantEffectiveTimeFromStart: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="participantEffectiveTimeFromStart",
        title="Observation time from study start",
        description="Indicates duration from the participant's study entry.",
        json_schema_extra={
            "element_property": True,
        },
    )

    participantEffectiveTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="participantEffectiveTiming",
        title="What time period do participants cover",
        description="Indicates what effective period the study covers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e participantEffective[x]
            "one_of_many": "participantEffective",
            "one_of_many_required": False,
        },
    )

    studyEffectiveDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="studyEffectiveDateTime",
        title="What time period does the study cover",
        description="Indicates what effective period the study covers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e studyEffective[x]
            "one_of_many": "studyEffective",
            "one_of_many_required": False,
        },
    )
    studyEffectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_studyEffectiveDateTime",
        title="Extension field for ``studyEffectiveDateTime``.",
    )

    studyEffectiveDescription: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="studyEffectiveDescription",
        title="What time period does the study cover",
        description="A narrative description of the time period the study covers.",
        json_schema_extra={
            "element_property": True,
        },
    )
    studyEffectiveDescription__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_studyEffectiveDescription",
        title="Extension field for ``studyEffectiveDescription``.",
    )

    studyEffectiveDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="studyEffectiveDuration",
        title="What time period does the study cover",
        description="Indicates what effective period the study covers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e studyEffective[x]
            "one_of_many": "studyEffective",
            "one_of_many_required": False,
        },
    )

    studyEffectiveGroupMeasure: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="studyEffectiveGroupMeasure",
        title=(
            "mean | median | mean-of-mean | mean-of-median | median-of-mean | "
            "median-of-median"
        ),
        description=(
            "Indicates how elements are aggregated within the study effective "
            "period."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "mean",
                "median",
                "mean-of-mean",
                "mean-of-median",
                "median-of-mean",
                "median-of-median",
            ],
        },
    )
    studyEffectiveGroupMeasure__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_studyEffectiveGroupMeasure",
        title="Extension field for ``studyEffectiveGroupMeasure``.",
    )

    studyEffectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="studyEffectivePeriod",
        title="What time period does the study cover",
        description="Indicates what effective period the study covers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e studyEffective[x]
            "one_of_many": "studyEffective",
            "one_of_many_required": False,
        },
    )

    studyEffectiveTimeFromStart: fhirtypes.DurationType | None = Field(  # type: ignore
        None,
        alias="studyEffectiveTimeFromStart",
        title="Observation time from study start",
        description="Indicates duration from the study initiation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    studyEffectiveTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="studyEffectiveTiming",
        title="What time period does the study cover",
        description="Indicates what effective period the study covers.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e studyEffective[x]
            "one_of_many": "studyEffective",
            "one_of_many_required": False,
        },
    )

    unitOfMeasure: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="unitOfMeasure",
        title="What unit is the outcome described in?",
        description="Specifies the UCUM unit for the outcome.",
        json_schema_extra={
            "element_property": True,
        },
    )

    usageContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        None,
        alias="usageContext",
        title="What code/value pairs define members?",
        description=(
            "Use UsageContext to define the members of the population, such as Age "
            "Ranges, Genders, Settings."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ResearchElementDefinitionCharacteristic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "definitionCodeableConcept",
            "definitionCanonical",
            "definitionExpression",
            "definitionDataRequirement",
            "usageContext",
            "exclude",
            "unitOfMeasure",
            "studyEffectiveDescription",
            "studyEffectiveDateTime",
            "studyEffectivePeriod",
            "studyEffectiveDuration",
            "studyEffectiveTiming",
            "studyEffectiveTimeFromStart",
            "studyEffectiveGroupMeasure",
            "participantEffectiveDescription",
            "participantEffectiveDateTime",
            "participantEffectivePeriod",
            "participantEffectiveDuration",
            "participantEffectiveTiming",
            "participantEffectiveTimeFromStart",
            "participantEffectiveGroupMeasure",
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
            "definition": [
                "definitionCanonical",
                "definitionCodeableConcept",
                "definitionDataRequirement",
                "definitionExpression",
            ],
            "participantEffective": [
                "participantEffectiveDateTime",
                "participantEffectiveDuration",
                "participantEffectivePeriod",
                "participantEffectiveTiming",
            ],
            "studyEffective": [
                "studyEffectiveDateTime",
                "studyEffectiveDuration",
                "studyEffectivePeriod",
                "studyEffectiveTiming",
            ],
        }
        return one_of_many_fields
