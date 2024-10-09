from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Requirements
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Requirements(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of requirements - features of systems that are necessary.
    A set of requirements - a list of features or behaviors of designed systems
    that are necessary to achieve organizational or regulatory goals.
    """

    __resource_type__ = "Requirements"

    actor: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="actor",
        title="Actor for these requirements",
        description="An actor these requirements are in regard to.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ActorDefinition"],
        },
    )
    actor__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_actor", title="Extension field for ``actor``."
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
            "A copyright statement relating to the Requirements and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the Requirements."
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
            "The date  (and optionally time) when the Requirements was published. "
            "The date must change when the business version changes and it must "
            "change if the status code changes. In addition, it should change when "
            "the substantive content of the Requirements changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFrom: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="derivedFrom",
        title="Other set of Requirements this builds on",
        description=(
            "Another set of Requirements that this set of Requirements builds on "
            "and updates."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Requirements"],
        },
    )
    derivedFrom__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_derivedFrom", title="Extension field for ``derivedFrom``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the requirements",
        description="A free text natural language description of the requirements.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this Requirements is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
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
        title="Additional identifier for the Requirements (business identifier)",
        description=(
            "A formal identifier that is used to identify this Requirements when it"
            " is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for Requirements (if applicable)",
        description=(
            "A legal or geographic region in which the Requirements is intended to "
            "be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this Requirements (computer friendly)",
        description=(
            "A natural language name identifying the Requirements. This name should"
            " be usable as an identifier for the module by machine processing "
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
            " and ongoing maintenance of the Requirements."
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
        title="Why this Requirements is defined",
        description=(
            "Explanation of why this Requirements is needed and why it has been "
            "designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    reference: typing.List[fhirtypes.UrlType | None] | None = Field(  # type: ignore
        None,
        alias="reference",
        title=(
            "External artifact (rule/document etc. that) created this set of "
            "requirements"
        ),
        description=(
            "A reference to another artifact that created this set of requirements."
            " This could be a Profile, etc., or external regulation, or business "
            "requirements expressed elsewhere."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    reference__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_reference", title="Extension field for ``reference``."
    )

    statement: typing.List[fhirtypes.RequirementsStatementType] | None = Field(  # type: ignore
        None,
        alias="statement",
        title="Actual statement as markdown",
        description="The actual statement of requirement, in markdown format.",
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this Requirements. Enables tracking the life-cycle of "
            "the content."
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

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this Requirements (human friendly)",
        description="A short, descriptive, user-friendly title for the Requirements.",
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
        title=(
            "Canonical identifier for this Requirements, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this Requirements when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " Requirements is (or will be) published. This URL can be the target of"
            " a canonical reference. It SHALL remain the same when the Requirements"
            " is stored on different servers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
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
            "indexing and searching for appropriate Requirements instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the Requirements",
        description=(
            "The identifier that is used to identify this version of the "
            "Requirements when it is referenced in a specification, model, design "
            "or instance. This is an arbitrary value managed by the Requirements "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence."
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
        ``Requirements`` according specification,
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
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "copyright",
            "copyrightLabel",
            "derivedFrom",
            "reference",
            "actor",
            "statement",
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
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"]
        }
        return one_of_many_fields


class RequirementsStatement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actual statement as markdown.
    The actual statement of requirement, in markdown format.
    """

    __resource_type__ = "RequirementsStatement"

    conditionality: bool | None = Field(  # type: ignore
        None,
        alias="conditionality",
        title="Set to true if requirements statement is conditional",
        description=(
            "This boolean flag is set to true of the text of the requirement is "
            "conditional on something e.g. it includes lanauage like 'if x then y'."
            " This conditionality flag is introduced for purposes of filtering and "
            "colour highlighting etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    conditionality__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_conditionality", title="Extension field for ``conditionality``."
    )

    conformance: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="conformance",
        title="SHALL | SHOULD | MAY | SHOULD-NOT",
        description="A short human usable label for this statement.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["SHALL", "SHOULD", "MAY", "SHOULD-NOT"],
        },
    )
    conformance__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_conformance", title="Extension field for ``conformance``."
    )

    derivedFrom: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="derivedFrom",
        title="Another statement this clarifies/restricts ([url#]key)",
        description=(
            "Another statement on one of the requirements that this requirement "
            "clarifies or restricts."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    derivedFrom__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_derivedFrom", title="Extension field for ``derivedFrom``."
    )

    key: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="key",
        title="Key that identifies this statement",
        description="Key that identifies this statement (unique within this resource).",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    key__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_key", title="Extension field for ``key``."
    )

    label: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="label",
        title="Short Human label for this statement",
        description="A short human usable label for this statement.",
        json_schema_extra={
            "element_property": True,
        },
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_label", title="Extension field for ``label``."
    )

    parent: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="parent",
        title="A larger requirement that this requirement helps to refine and enable",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    parent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_parent", title="Extension field for ``parent``."
    )

    reference: typing.List[fhirtypes.UrlType | None] | None = Field(  # type: ignore
        None,
        alias="reference",
        title="External artifact (rule/document etc. that) created this requirement",
        description=(
            "A reference to another artifact that created this requirement. This "
            "could be a Profile, etc., or external regulation, or business "
            "requirements expressed elsewhere."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    reference__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_reference", title="Extension field for ``reference``."
    )

    requirement: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="requirement",
        title="The actual requirement",
        description="The actual requirement for human consumption.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    requirement__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_requirement", title="Extension field for ``requirement``."
    )

    satisfiedBy: typing.List[fhirtypes.UrlType | None] | None = Field(  # type: ignore
        None,
        alias="satisfiedBy",
        title="Design artifact that satisfies this requirement",
        description=(
            "A reference to another artifact that satisfies this requirement. This "
            "could be a Profile, extension, or an element in one of those, or a "
            "CapabilityStatement, OperationDefinition, SearchParameter, "
            "CodeSystem(/code), ValueSet, Libary etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    satisfiedBy__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_satisfiedBy", title="Extension field for ``satisfiedBy``."
    )

    source: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="source",
        title="Who asked for this statement",
        description=(
            "Who asked for this statement to be a requirement. By default, it's "
            "assumed that the publisher knows who it is if it matters."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CareTeam",
                "Device",
                "Group",
                "HealthcareService",
                "Organization",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RequirementsStatement`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "key",
            "label",
            "conformance",
            "conditionality",
            "requirement",
            "derivedFrom",
            "parent",
            "satisfiedBy",
            "reference",
            "source",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("key", "key__ext"), ("requirement", "requirement__ext")]
        return required_fields
