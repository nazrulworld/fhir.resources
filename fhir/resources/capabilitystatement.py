from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CapabilityStatement(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A statement of system capabilities.
    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server or Client for a particular version of FHIR that may be used as
    a statement of actual server functionality or a statement of required or
    desired server implementation.
    """

    __resource_type__ = "CapabilityStatement"

    acceptLanguage: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="acceptLanguage",
        title="Languages supported",
        description=(
            "A list of the languages supported by this implementation that are "
            "usefully supported in the ```Accept-Language``` header."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    acceptLanguage__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_acceptLanguage", title="Extension field for ``acceptLanguage``."
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
            "A copyright statement relating to the capability statement and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the capability statement."
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
            "The date  (and optionally time) when the capability statement was last"
            " significantly changed. The date must change when the business version"
            " changes and it must change if the status code changes. In addition, "
            "it should change when the substantive content of the capability "
            "statement changes."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the capability statement",
        description=(
            "A free text natural language description of the capability statement "
            "from a consumer's perspective. Typically, this is used when the "
            "capability statement describes a desired rather than an actual "
            "solution, for example as a formal expression of requirements as part "
            "of an RFP."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    document: typing.List[fhirtypes.CapabilityStatementDocumentType] | None = Field(  # type: ignore
        None,
        alias="document",
        title="Document definition",
        description="A document definition.",
        json_schema_extra={
            "element_property": True,
        },
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this capability statement is authored"
            " for testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fhirVersion: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="fhirVersion",
        title="FHIR Version the system supports",
        description=(
            "The version of the FHIR specification that this CapabilityStatement "
            "describes (which SHALL be the same as the FHIR version of the "
            "CapabilityStatement itself). There is no default value."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    fhirVersion__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_fhirVersion", title="Extension field for ``fhirVersion``."
    )

    format: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="format",
        title="formats supported (xml | json | ttl | mime type)",
        description=(
            "A list of the formats supported by this implementation using their "
            "content types."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["formats", "json", "ttl", "mime"],
        },
    )
    format__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_format", title="Extension field for ``format``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title=(
            "Additional identifier for the CapabilityStatement (business " "identifier)"
        ),
        description=(
            "A formal identifier that is used to identify this CapabilityStatement "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    implementation: fhirtypes.CapabilityStatementImplementationType | None = Field(  # type: ignore
        None,
        alias="implementation",
        title="If this describes a specific instance",
        description=(
            "Identifies a specific implementation instance that is described by the"
            " capability statement - i.e. a particular installation, rather than "
            "the capabilities of a software program."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    implementationGuide: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="implementationGuide",
        title="Implementation guides supported",
        description=(
            "A list of implementation guides that the server does (or should) "
            "support in their entirety."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ImplementationGuide"],
        },
    )
    implementationGuide__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_implementationGuide",
        title="Extension field for ``implementationGuide``.",
    )

    imports: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="imports",
        title="Canonical URL of another capability statement this adds to",
        description=(
            "Reference to a canonical URL of another CapabilityStatement that this "
            "software adds to. The capability statement automatically includes "
            "everything in the other statement, and it is not duplicated, though "
            "the server may repeat the same resources, interactions and operations "
            "to add additional details to them."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CapabilityStatement"],
        },
    )
    imports__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_imports", title="Extension field for ``imports``."
    )

    instantiates: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="instantiates",
        title="Canonical URL of another capability statement this implements",
        description=(
            "Reference to a canonical URL of another CapabilityStatement that this "
            "software implements. This capability statement is a published API "
            "description that corresponds to a business service. The server may "
            "actually implement a subset of the capability statement it claims to "
            "implement, so the capability statement must specify the full "
            "capability details."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CapabilityStatement"],
        },
    )
    instantiates__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_instantiates", title="Extension field for ``instantiates``."
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for capability statement (if applicable)",
        description=(
            "A legal or geographic region in which the capability statement is "
            "intended to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    kind: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="kind",
        title="instance | capability | requirements",
        description=(
            "The way that this statement is intended to be used, to describe an "
            "actual running instance of software, a particular product (kind, not "
            "instance of software) or a class of implementation (e.g. a desired "
            "purchase)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["instance", "capability", "requirements"],
        },
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_kind", title="Extension field for ``kind``."
    )

    messaging: typing.List[fhirtypes.CapabilityStatementMessagingType] | None = Field(  # type: ignore
        None,
        alias="messaging",
        title="If messaging is supported",
        description="A description of the messaging capabilities of the solution.",
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this capability statement (computer friendly)",
        description=(
            "A natural language name identifying the capability statement. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    patchFormat: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="patchFormat",
        title="Patch formats supported",
        description=(
            "A list of the patch formats supported by this implementation using "
            "their content types."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    patchFormat__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_patchFormat", title="Extension field for ``patchFormat``."
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the capability statement."
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
        title="Why this capability statement is defined",
        description=(
            "Explanation of why this capability statement is needed and why it has "
            "been designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    rest: typing.List[fhirtypes.CapabilityStatementRestType] | None = Field(  # type: ignore
        None,
        alias="rest",
        title="If the endpoint is a RESTful one",
        description="A definition of the restful capabilities of the solution, if any.",
        json_schema_extra={
            "element_property": True,
        },
    )

    software: fhirtypes.CapabilityStatementSoftwareType | None = Field(  # type: ignore
        None,
        alias="software",
        title="Software that is covered by this capability statement",
        description=(
            "Software that is covered by this capability statement.  It is used "
            "when the capability statement describes the capabilities of a "
            "particular software version, independent of an installation."
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
            "The status of this capability statement. Enables tracking the life-"
            "cycle of the content."
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
        title="Name for this capability statement (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the capability " "statement."
        ),
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
            "Canonical identifier for this capability statement, represented as a "
            "URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this capability statement "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which an "
            "authoritative instance of this capability statement is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the capability statement is stored on "
            "different servers."
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
            "indexing and searching for appropriate capability statement instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the capability statement",
        description=(
            "The identifier that is used to identify this version of the capability"
            " statement when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the capability "
            "statement author and is not expected to be globally unique. For "
            "example, it might be a timestamp (e.g. yyyymmdd) if a managed version "
            "is not available. There is also no expectation that versions can be "
            "placed in a lexicographical sequence."
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
        ``CapabilityStatement`` according specification,
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
            "kind",
            "instantiates",
            "imports",
            "software",
            "implementation",
            "fhirVersion",
            "format",
            "patchFormat",
            "acceptLanguage",
            "implementationGuide",
            "rest",
            "messaging",
            "document",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("date", "date__ext"),
            ("fhirVersion", "fhirVersion__ext"),
            ("format", "format__ext"),
            ("kind", "kind__ext"),
            ("status", "status__ext"),
        ]
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


class CapabilityStatementDocument(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Document definition.
    A document definition.
    """

    __resource_type__ = "CapabilityStatementDocument"

    documentation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Description of document support",
        description=(
            "A description of how the application supports or uses the specified "
            "document profile.  For example, when documents are created, what "
            "action is taken with consumed documents, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="producer | consumer",
        description=(
            "Mode of this document declaration - whether an application is a "
            "producer or consumer."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["producer", "consumer"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    profile: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="profile",
        title="Constraint on the resources used in the document",
        description=(
            "A profile on the document Bundle that constrains which resources are "
            "present, and their contents."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_profile", title="Extension field for ``profile``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementDocument`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "mode",
            "documentation",
            "profile",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext"), ("profile", "profile__ext")]
        return required_fields


class CapabilityStatementImplementation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If this describes a specific instance.
    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """

    __resource_type__ = "CapabilityStatementImplementation"

    custodian: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="custodian",
        title="Organization that manages the data",
        description=(
            "The organization responsible for the management of the instance and "
            "oversight of the data on the server at the specified URL."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Describes this specific instance",
        description=(
            "Information about the specific installation that this capability "
            "statement relates to."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    url: fhirtypes.UrlType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Base URL for the installation",
        description=(
            "An absolute base URL for the implementation.  This forms the base for "
            "REST interfaces as well as the mailbox and document interfaces."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementImplementation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "description",
            "url",
            "custodian",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("description", "description__ext")]
        return required_fields


class CapabilityStatementMessaging(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If messaging is supported.
    A description of the messaging capabilities of the solution.
    """

    __resource_type__ = "CapabilityStatementMessaging"

    documentation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Messaging interface behavior details",
        description=(
            "Documentation about the system's messaging capabilities for this "
            "endpoint not otherwise documented by the capability statement.  For "
            "example, the process for becoming an authorized messaging exchange "
            "partner."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    endpoint: typing.List[fhirtypes.CapabilityStatementMessagingEndpointType] | None = Field(  # type: ignore
        None,
        alias="endpoint",
        title="Where messages should be sent",
        description=(
            "An endpoint (network accessible address) to which messages and/or "
            "replies are to be sent."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reliableCache: fhirtypes.UnsignedIntType | None = Field(  # type: ignore
        None,
        alias="reliableCache",
        title="Reliable Message Cache Length (min)",
        description=(
            "Length if the receiver's reliable messaging cache in minutes (if a "
            "receiver) or how long the cache length on the receiver should be (if a"
            " sender)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    reliableCache__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_reliableCache", title="Extension field for ``reliableCache``."
    )

    supportedMessage: typing.List[fhirtypes.CapabilityStatementMessagingSupportedMessageType] | None = Field(  # type: ignore
        None,
        alias="supportedMessage",
        title="Messages supported by this system",
        description=(
            "References to message definitions for messages this system can send or"
            " receive."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementMessaging`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "endpoint",
            "reliableCache",
            "documentation",
            "supportedMessage",
        ]


class CapabilityStatementMessagingEndpoint(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Where messages should be sent.
    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """

    __resource_type__ = "CapabilityStatementMessagingEndpoint"

    address: fhirtypes.UrlType | None = Field(  # type: ignore
        None,
        alias="address",
        title="Network address or identifier of the end-point",
        description=(
            "The network address of the endpoint. For solutions that do not use "
            "network addresses for routing, it can be just an identifier."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    address__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_address", title="Extension field for ``address``."
    )

    protocol: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="protocol",
        title="http | ftp | mllp +",
        description=(
            "A list of the messaging transport protocol(s) identifiers, supported "
            "by this endpoint."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementMessagingEndpoint`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "protocol", "address"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("address", "address__ext")]
        return required_fields


class CapabilityStatementMessagingSupportedMessage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Messages supported by this system.
    References to message definitions for messages this system can send or
    receive.
    """

    __resource_type__ = "CapabilityStatementMessagingSupportedMessage"

    definition: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="definition",
        title="Message supported by this system",
        description=(
            "Points to a message definition that identifies the messaging event, "
            "message structure, allowed responses, etc."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MessageDefinition"],
        },
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_definition", title="Extension field for ``definition``."
    )

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="sender | receiver",
        description=(
            "The mode of this event declaration - whether application is sender or "
            "receiver."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["sender", "receiver"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementMessagingSupportedMessage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "mode", "definition"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("definition", "definition__ext"), ("mode", "mode__ext")]
        return required_fields


class CapabilityStatementRest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If the endpoint is a RESTful one.
    A definition of the restful capabilities of the solution, if any.
    """

    __resource_type__ = "CapabilityStatementRest"

    compartment: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="compartment",
        title="Compartments served/used by system",
        description=(
            "An absolute URI which is a reference to the definition of a "
            "compartment that the system supports. The reference is to a "
            "CompartmentDefinition resource by its canonical URL ."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CompartmentDefinition"],
        },
    )
    compartment__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_compartment", title="Extension field for ``compartment``."
    )

    documentation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="General description of implementation",
        description=(
            "Information about the system's restful capabilities that apply across "
            "all applications, such as security."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    interaction: typing.List[fhirtypes.CapabilityStatementRestInteractionType] | None = Field(  # type: ignore
        None,
        alias="interaction",
        title="What operations are supported?",
        description="A specification of restful operations supported by the system.",
        json_schema_extra={
            "element_property": True,
        },
    )

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="client | server",
        description=(
            "Identifies whether this portion of the statement is describing the "
            "ability to initiate or receive restful operations."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["client", "server"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    operation: typing.List[fhirtypes.CapabilityStatementRestResourceOperationType] | None = Field(  # type: ignore
        None,
        alias="operation",
        title="Definition of a system level operation",
        description=(
            "Definition of an operation or a named query together with its "
            "parameters and their meaning and type."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    resource: typing.List[fhirtypes.CapabilityStatementRestResourceType] | None = Field(  # type: ignore
        None,
        alias="resource",
        title="Resource served on the REST interface",
        description=(
            "A specification of the restful capabilities of the solution for a "
            "specific resource type."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    searchParam: typing.List[fhirtypes.CapabilityStatementRestResourceSearchParamType] | None = Field(  # type: ignore
        None,
        alias="searchParam",
        title="Search parameters for searching all resources",
        description=(
            "Search parameters that are supported for searching all resources for "
            "implementations to support and/or make use of - either references to "
            "ones defined in the specification, or additional ones defined for/by "
            "the implementation. This is only for searches executed against the "
            "system-level endpoint."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    security: fhirtypes.CapabilityStatementRestSecurityType | None = Field(  # type: ignore
        None,
        alias="security",
        title="Information about security of implementation",
        description=(
            "Information about security implementation from an interface "
            "perspective - what a client needs to know."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementRest`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "mode",
            "documentation",
            "security",
            "resource",
            "interaction",
            "searchParam",
            "operation",
            "compartment",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("mode", "mode__ext")]
        return required_fields


class CapabilityStatementRestInteraction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What operations are supported?.
    A specification of restful operations supported by the system.
    """

    __resource_type__ = "CapabilityStatementRestInteraction"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="transaction | batch | search-system | history-system",
        description="A coded identifier of the operation, supported by the system.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["transaction", "batch", "search-system", "history-system"],
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    documentation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Anything special about operation behavior",
        description=(
            "Guidance specific to the implementation of this operation, such as "
            "limitations on the kind of transactions allowed, or information about "
            "system wide search is implemented."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementRestInteraction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "documentation"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
        return required_fields


class CapabilityStatementRestResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource served on the REST interface.
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """

    __resource_type__ = "CapabilityStatementRestResource"

    conditionalCreate: bool | None = Field(  # type: ignore
        None,
        alias="conditionalCreate",
        title="If allows/uses conditional create",
        description="A flag that indicates that the server supports conditional create.",
        json_schema_extra={
            "element_property": True,
        },
    )
    conditionalCreate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_conditionalCreate",
        title="Extension field for ``conditionalCreate``.",
    )

    conditionalDelete: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="conditionalDelete",
        title=(
            "not-supported | single | multiple - how conditional delete is " "supported"
        ),
        description="A code that indicates how the server supports conditional delete.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["not-supported", "single", "multiple"],
        },
    )
    conditionalDelete__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_conditionalDelete",
        title="Extension field for ``conditionalDelete``.",
    )

    conditionalPatch: bool | None = Field(  # type: ignore
        None,
        alias="conditionalPatch",
        title="If allows/uses conditional patch",
        description="A flag that indicates that the server supports conditional patch.",
        json_schema_extra={
            "element_property": True,
        },
    )
    conditionalPatch__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_conditionalPatch",
        title="Extension field for ``conditionalPatch``.",
    )

    conditionalRead: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="conditionalRead",
        title="not-supported | modified-since | not-match | full-support",
        description="A code that indicates how the server supports conditional read.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "not-supported",
                "modified-since",
                "not-match",
                "full-support",
            ],
        },
    )
    conditionalRead__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_conditionalRead", title="Extension field for ``conditionalRead``."
    )

    conditionalUpdate: bool | None = Field(  # type: ignore
        None,
        alias="conditionalUpdate",
        title="If allows/uses conditional update",
        description="A flag that indicates that the server supports conditional update.",
        json_schema_extra={
            "element_property": True,
        },
    )
    conditionalUpdate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_conditionalUpdate",
        title="Extension field for ``conditionalUpdate``.",
    )

    documentation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Additional information about the use of the resource type",
        description="Additional information about the resource type used by the system.",
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    interaction: typing.List[fhirtypes.CapabilityStatementRestResourceInteractionType] | None = Field(  # type: ignore
        None,
        alias="interaction",
        title="What operations are supported?",
        description="Identifies a restful operation supported by the solution.",
        json_schema_extra={
            "element_property": True,
        },
    )

    operation: typing.List[fhirtypes.CapabilityStatementRestResourceOperationType] | None = Field(  # type: ignore
        None,
        alias="operation",
        title="Definition of a resource operation",
        description=(
            "Definition of an operation or a named query together with its "
            "parameters and their meaning and type. Consult the definition of the "
            "operation for details about how to invoke the operation, and the "
            "parameters."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    profile: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="profile",
        title="System-wide profile",
        description=(
            "A system-wide profile that is applied across *all* instances of the "
            "resource supported by the system. For example, if declared on "
            'Observation, this profile is the "superset" of capabilities for '
            "laboratory *and* vitals *and* other domains. See further discussion in"
            " [Using Profiles](profiling.html#profile-uses)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_profile", title="Extension field for ``profile``."
    )

    readHistory: bool | None = Field(  # type: ignore
        None,
        alias="readHistory",
        title="Whether vRead can return past versions",
        description=(
            "A flag for whether the server is able to return past versions as part "
            "of the vRead operation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    readHistory__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_readHistory", title="Extension field for ``readHistory``."
    )

    referencePolicy: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="referencePolicy",
        title="literal | logical | resolves | enforced | local",
        description="A set of flags that defines how references are supported.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["literal", "logical", "resolves", "enforced", "local"],
        },
    )
    referencePolicy__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_referencePolicy", title="Extension field for ``referencePolicy``."
    )

    searchInclude: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="searchInclude",
        title="_include values supported by the server",
        description="A list of _include values supported by the server.",
        json_schema_extra={
            "element_property": True,
        },
    )
    searchInclude__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_searchInclude", title="Extension field for ``searchInclude``."
    )

    searchParam: typing.List[fhirtypes.CapabilityStatementRestResourceSearchParamType] | None = Field(  # type: ignore
        None,
        alias="searchParam",
        title="Search parameters supported by implementation",
        description=(
            "Search parameters for implementations to support and/or make use of - "
            "either references to ones defined in the specification, or additional "
            "ones defined for/by the implementation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    searchRevInclude: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="searchRevInclude",
        title="_revinclude values supported by the server",
        description=(
            "A list of _revinclude (reverse include) values supported by the " "server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    searchRevInclude__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_searchRevInclude",
        title="Extension field for ``searchRevInclude``.",
    )

    supportedProfile: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="supportedProfile",
        title="Use-case specific profiles",
        description=(
            "A list of profiles representing different use cases the system "
            "hosts/produces. A supported profile is a statement about the "
            "functionality of the data and services provided by the server (or the "
            "client) for supported use cases. For example, a system can define and "
            "declare multiple Observation profiles for laboratory observations, "
            "vital sign observations, etc. By declaring supported profiles, systems"
            " provide a way to determine whether individual resources are "
            "conformant. See further discussion in [Using "
            "Profiles](profiling.html#profile-uses)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    supportedProfile__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_supportedProfile",
        title="Extension field for ``supportedProfile``.",
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="A resource type that is supported",
        description="A type of resource exposed via the restful interface.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    updateCreate: bool | None = Field(  # type: ignore
        None,
        alias="updateCreate",
        title="If update can commit to a new identity",
        description=(
            "A flag to indicate that the server allows or needs to allow the client"
            " to create new identities on the server (that is, the client PUTs to a"
            " location where there is no existing resource). Allowing this "
            "operation means that the server allows the client to create new "
            "identities on the server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    updateCreate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_updateCreate", title="Extension field for ``updateCreate``."
    )

    versioning: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="versioning",
        title="no-version | versioned | versioned-update",
        description=(
            "This field is set to no-version to specify that the system does not "
            "support (server) or use (client) versioning for this resource type. If"
            " this has some other value, the server must at least correctly track "
            "and populate the versionId meta-property on resources. If the value is"
            " 'versioned-update', then the server supports all the versioning "
            "features, including using e-tags for version integrity in the API."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["no-version", "versioned", "versioned-update"],
        },
    )
    versioning__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_versioning", title="Extension field for ``versioning``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementRestResource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "profile",
            "supportedProfile",
            "documentation",
            "interaction",
            "versioning",
            "readHistory",
            "updateCreate",
            "conditionalCreate",
            "conditionalRead",
            "conditionalUpdate",
            "conditionalPatch",
            "conditionalDelete",
            "referencePolicy",
            "searchInclude",
            "searchRevInclude",
            "searchParam",
            "operation",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields


class CapabilityStatementRestResourceInteraction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What operations are supported?.
    Identifies a restful operation supported by the solution.
    """

    __resource_type__ = "CapabilityStatementRestResourceInteraction"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title=(
            "read | vread | update | patch | delete | history-instance | history-"
            "type | create | search-type"
        ),
        description="Coded identifier of the operation, supported by the system resource.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "read",
                "vread",
                "update",
                "patch",
                "delete",
                "history-instance",
                "history-type",
                "create",
                "search-type",
            ],
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    documentation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Anything special about operation behavior",
        description=(
            "Guidance specific to the implementation of this operation, such as "
            "'delete is a logical delete' or 'updates are only allowed with version"
            " id' or 'creates permitted from pre-authorized certificates only'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementRestResourceInteraction`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "documentation"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
        return required_fields


class CapabilityStatementRestResourceOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of a resource operation.
    Definition of an operation or a named query together with its parameters
    and their meaning and type. Consult the definition of the operation for
    details about how to invoke the operation, and the parameters.
    """

    __resource_type__ = "CapabilityStatementRestResourceOperation"

    definition: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="definition",
        title="The defined operation/query",
        description=(
            "Where the formal definition can be found. If a server references the "
            "base definition of an Operation (i.e. from the specification itself "
            "such as ```http://hl7.org/fhir/OperationDefinition/ValueSet-"
            "expand```), that means it supports the full capabilities of the "
            "operation - e.g. both GET and POST invocation.  If it only supports a "
            "subset, it must define its own custom "
            "[OperationDefinition](operationdefinition.html#) with a 'base' of the "
            "original OperationDefinition.  The custom definition would describe "
            "the specific subset of functionality supported."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["OperationDefinition"],
        },
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_definition", title="Extension field for ``definition``."
    )

    documentation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Specific details about operation behavior",
        description=(
            "Documentation that describes anything special about the operation "
            "behavior, possibly detailing different behavior for system, type and "
            "instance-level invocation of the operation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name by which the operation/query is invoked",
        description=(
            "The name of the operation or query. For an operation, this name is "
            "prefixed with $ and used in the URL. For a query, this is the name "
            "used in the _query parameter when the query is called. This SHOULD be "
            "the same as the OperationDefinition.code of the defining "
            "OperationDefinition.  However, it can sometimes differ if necessary to"
            " disambiguate when a server supports multiple OperationDefinition that"
            " happen to share the same code."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementRestResourceOperation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "definition",
            "documentation",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("definition", "definition__ext"), ("name", "name__ext")]
        return required_fields


class CapabilityStatementRestResourceSearchParam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Search parameters supported by implementation.
    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """

    __resource_type__ = "CapabilityStatementRestResourceSearchParam"

    definition: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="definition",
        title="Source of definition for parameter",
        description=(
            "An absolute URI that is a formal reference to where this parameter was"
            " first defined, so that a client can be confident of the meaning of "
            "the search parameter (a reference to "
            "[SearchParameter.url](searchparameter-"
            "definitions.html#SearchParameter.url)). This element SHALL be "
            "populated if the search parameter refers to a SearchParameter defined "
            "by the FHIR core specification or externally defined IGs."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SearchParameter"],
        },
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_definition", title="Extension field for ``definition``."
    )

    documentation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Server-specific usage",
        description=(
            "This allows documentation of any distinct behaviors about how the "
            "search parameter is used.  For example, text matching algorithms."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for parameter in search url",
        description=(
            "The label used for the search parameter in this particular system's "
            "API - i.e. the 'name' portion of the name-value pair that will appear "
            "as part of the search URL.  This SHOULD be the same as the "
            "SearchParameter.code of the defining SearchParameter.  However, it can"
            " sometimes differ if necessary to disambiguate when a server supports "
            "multiple SearchParameters that happen to share the same code."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title=(
            "number | date | string | token | reference | composite | quantity | "
            "uri | special"
        ),
        description=(
            "The type of value a search parameter refers to, and how the content is"
            " interpreted."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "number",
                "date",
                "string",
                "token",
                "reference",
                "composite",
                "quantity",
                "uri",
                "special",
            ],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementRestResourceSearchParam`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "definition",
            "type",
            "documentation",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext"), ("type", "type__ext")]
        return required_fields


class CapabilityStatementRestSecurity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about security of implementation.
    Information about security implementation from an interface perspective -
    what a client needs to know.
    """

    __resource_type__ = "CapabilityStatementRestSecurity"

    cors: bool | None = Field(  # type: ignore
        None,
        alias="cors",
        title="Adds CORS Headers (http://enable-cors.org/)",
        description=(
            "Server adds CORS headers when responding to requests - this enables "
            "Javascript applications to use the server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    cors__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_cors", title="Extension field for ``cors``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="General description of how security works",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    service: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="service",
        title="OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates",
        description="Types of security services that are supported/required by the system.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CapabilityStatementRestSecurity`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "cors",
            "service",
            "description",
        ]


class CapabilityStatementSoftware(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Software that is covered by this capability statement.
    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """

    __resource_type__ = "CapabilityStatementSoftware"

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="A name the software is known by",
        description="Name the software is known by.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    releaseDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="releaseDate",
        title="Date this version was released",
        description="Date this version of the software was released.",
        json_schema_extra={
            "element_property": True,
        },
    )
    releaseDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_releaseDate", title="Extension field for ``releaseDate``."
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Version covered by this statement",
        description="The version identifier for the software covered by this statement.",
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
        ``CapabilityStatementSoftware`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "version",
            "releaseDate",
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
