from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class TerminologyCapabilities(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A statement of system capabilities.
    A TerminologyCapabilities resource documents a set of capabilities
    (behaviors) of a FHIR Terminology Server that may be used as a statement of
    actual server functionality or a statement of required or desired server
    implementation.
    """

    __resource_type__ = "TerminologyCapabilities"

    closure: fhirtypes.TerminologyCapabilitiesClosureType | None = Field(  # type: ignore
        None,
        alias="closure",
        title=(
            "Information about the [ConceptMap/$closure](conceptmap-operation-"
            "closure.html) operation"
        ),
        description="Whether the $closure operation is supported.",
        json_schema_extra={
            "element_property": True,
        },
    )

    codeSearch: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="codeSearch",
        title="in-compose | in-expansion | in-compose-or-expansion",
        description=(
            "The degree to which the server supports the code search parameter on "
            "ValueSet, if it is supported."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["in-compose", "in-expansion", "in-compose-or-expansion"],
        },
    )
    codeSearch__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_codeSearch", title="Extension field for ``codeSearch``."
    )

    codeSystem: typing.List[fhirtypes.TerminologyCapabilitiesCodeSystemType] | None = Field(  # type: ignore
        None,
        alias="codeSystem",
        title="A code system supported by the server",
        description=(
            "Identifies a code system that is supported by the server. If there is "
            "a no code system URL, then this declares the general assumptions a "
            "client can make about support for any CodeSystem resource."
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
            "A copyright statement relating to the terminology capabilities and/or "
            "its contents. Copyright statements are generally legal restrictions on"
            " the use and publishing of the terminology capabilities."
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
            "The date  (and optionally time) when the terminology capabilities was "
            "last significantly changed. The date must change when the business "
            "version changes and it must change if the status code changes. In "
            "addition, it should change when the substantive content of the "
            "terminology capabilities changes."
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
        title="Natural language description of the terminology capabilities",
        description=(
            "A free text natural language description of the terminology "
            "capabilities from a consumer's perspective. Typically, this is used "
            "when the capability statement describes a desired rather than an "
            "actual solution, for example as a formal expression of requirements as"
            " part of an RFP."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    expansion: fhirtypes.TerminologyCapabilitiesExpansionType | None = Field(  # type: ignore
        None,
        alias="expansion",
        title=(
            "Information about the [ValueSet/$expand](valueset-operation-"
            "expand.html) operation"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this terminology capabilities is "
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
        title="Additional identifier for the terminology capabilities",
        description=(
            "A formal identifier that is used to identify this terminology "
            "capabilities when it is represented in other formats, or referenced in"
            " a specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    implementation: fhirtypes.TerminologyCapabilitiesImplementationType | None = Field(  # type: ignore
        None,
        alias="implementation",
        title="If this describes a specific instance",
        description=(
            "Identifies a specific implementation instance that is described by the"
            " terminology capability statement - i.e. a particular installation, "
            "rather than the capabilities of a software program."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for terminology capabilities (if applicable)",
        description=(
            "A legal or geographic region in which the terminology capabilities is "
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

    lockedDate: bool | None = Field(  # type: ignore
        None,
        alias="lockedDate",
        title="Whether lockedDate is supported",
        description="Whether the server supports lockedDate.",
        json_schema_extra={
            "element_property": True,
        },
    )
    lockedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_lockedDate", title="Extension field for ``lockedDate``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this terminology capabilities (computer friendly)",
        description=(
            "A natural language name identifying the terminology capabilities. This"
            " name should be usable as an identifier for the module by machine "
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
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the terminology capabilities."
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
        title="Why this terminology capabilities is defined",
        description=(
            "Explanation of why this terminology capabilities is needed and why it "
            "has been designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    software: fhirtypes.TerminologyCapabilitiesSoftwareType | None = Field(  # type: ignore
        None,
        alias="software",
        title="Software that is covered by this terminology capability statement",
        description=(
            "Software that is covered by this terminology capability statement.  It"
            " is used when the statement describes the capabilities of a particular"
            " software version, independent of an installation."
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
            "The status of this terminology capabilities. Enables tracking the "
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

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this terminology capabilities (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the terminology "
            "capabilities."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    translation: fhirtypes.TerminologyCapabilitiesTranslationType | None = Field(  # type: ignore
        None,
        alias="translation",
        title=(
            "Information about the [ConceptMap/$translate](conceptmap-operation-"
            "translate.html) operation"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this terminology capabilities, represented as"
            " a URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this terminology capabilities"
            " when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which an "
            "authoritative instance of this terminology capabilities is (or will "
            "be) published. This URL can be the target of a canonical reference. It"
            " SHALL remain the same when the terminology capabilities is stored on "
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
            "indexing and searching for appropriate terminology capabilities "
            "instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    validateCode: fhirtypes.TerminologyCapabilitiesValidateCodeType | None = Field(  # type: ignore
        None,
        alias="validateCode",
        title=(
            "Information about the [ValueSet/$validate-code](valueset-operation-"
            "validate-code.html) operation"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the terminology capabilities",
        description=(
            "The identifier that is used to identify this version of the "
            "terminology capabilities when it is referenced in a specification, "
            "model, design or instance. This is an arbitrary value managed by the "
            "terminology capabilities author and is not expected to be globally "
            "unique. For example, it might be a timestamp (e.g. yyyymmdd) if a "
            "managed version is not available. There is also no expectation that "
            "versions can be placed in a lexicographical sequence."
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
        ``TerminologyCapabilities`` according specification,
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
            "software",
            "implementation",
            "lockedDate",
            "codeSystem",
            "expansion",
            "codeSearch",
            "validateCode",
            "translation",
            "closure",
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


class TerminologyCapabilitiesClosure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ConceptMap/$closure](conceptmap-operation-
    closure.html) operation.
    Whether the $closure operation is supported.
    """

    __resource_type__ = "TerminologyCapabilitiesClosure"

    translation: bool | None = Field(  # type: ignore
        None,
        alias="translation",
        title="If cross-system closure is supported",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    translation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_translation", title="Extension field for ``translation``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TerminologyCapabilitiesClosure`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "translation"]


class TerminologyCapabilitiesCodeSystem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A code system supported by the server.
    Identifies a code system that is supported by the server. If there is a no
    code system URL, then this declares the general assumptions a client can
    make about support for any CodeSystem resource.
    """

    __resource_type__ = "TerminologyCapabilitiesCodeSystem"

    content: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="content",
        title="not-present | example | fragment | complete | supplement",
        description=(
            "The extent of the content of the code system (the concepts and codes "
            "it defines) are represented in this resource instance."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "not-present",
                "example",
                "fragment",
                "complete",
                "supplement",
            ],
        },
    )
    content__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_content", title="Extension field for ``content``."
    )

    subsumption: bool | None = Field(  # type: ignore
        None,
        alias="subsumption",
        title="Whether subsumption is supported",
        description="True if subsumption is supported for this version of the code system.",
        json_schema_extra={
            "element_property": True,
        },
    )
    subsumption__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_subsumption", title="Extension field for ``subsumption``."
    )

    uri: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="uri",
        title="Canonical identifier for the code system, represented as a URI",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CodeSystem"],
        },
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_uri", title="Extension field for ``uri``."
    )

    version: typing.List[fhirtypes.TerminologyCapabilitiesCodeSystemVersionType] | None = Field(  # type: ignore
        None,
        alias="version",
        title="Version of Code System supported",
        description=(
            "For the code system, a list of versions that are supported by the "
            "server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TerminologyCapabilitiesCodeSystem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "uri",
            "version",
            "content",
            "subsumption",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("content", "content__ext")]
        return required_fields


class TerminologyCapabilitiesCodeSystemVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Version of Code System supported.
    For the code system, a list of versions that are supported by the server.
    """

    __resource_type__ = "TerminologyCapabilitiesCodeSystemVersion"

    code: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Version identifier for this version",
        description=(
            "For version-less code systems, there should be a single version with "
            "no identifier."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    compositional: bool | None = Field(  # type: ignore
        None,
        alias="compositional",
        title="If compositional grammar is supported",
        description="If the compositional grammar defined by the code system is supported.",
        json_schema_extra={
            "element_property": True,
        },
    )
    compositional__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_compositional", title="Extension field for ``compositional``."
    )

    filter: typing.List[fhirtypes.TerminologyCapabilitiesCodeSystemVersionFilterType] | None = Field(  # type: ignore
        None,
        alias="filter",
        title="Filter Properties supported",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    isDefault: bool | None = Field(  # type: ignore
        None,
        alias="isDefault",
        title="If this is the default version for this code system",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    isDefault__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_isDefault", title="Extension field for ``isDefault``."
    )

    language: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="language",
        title="Language Displays supported",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    language__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_language", title="Extension field for ``language``."
    )

    property: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="property",
        title="Properties supported for $lookup",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    property__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_property", title="Extension field for ``property``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TerminologyCapabilitiesCodeSystemVersion`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "isDefault",
            "compositional",
            "language",
            "filter",
            "property",
        ]


class TerminologyCapabilitiesCodeSystemVersionFilter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Filter Properties supported.
    """

    __resource_type__ = "TerminologyCapabilitiesCodeSystemVersionFilter"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Code of the property supported",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    op: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="op",
        title="Operations supported for the property",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    op__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_op", title="Extension field for ``op``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TerminologyCapabilitiesCodeSystemVersionFilter`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "op"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("op", "op__ext")]
        return required_fields


class TerminologyCapabilitiesExpansion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ValueSet/$expand](valueset-operation-expand.html)
    operation.
    """

    __resource_type__ = "TerminologyCapabilitiesExpansion"

    hierarchical: bool | None = Field(  # type: ignore
        None,
        alias="hierarchical",
        title="Whether the server can return nested value sets",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    hierarchical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_hierarchical", title="Extension field for ``hierarchical``."
    )

    incomplete: bool | None = Field(  # type: ignore
        None,
        alias="incomplete",
        title="Allow request for incomplete expansions?",
        description="True if requests for incomplete expansions are allowed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    incomplete__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_incomplete", title="Extension field for ``incomplete``."
    )

    paging: bool | None = Field(  # type: ignore
        None,
        alias="paging",
        title="Whether the server supports paging on expansion",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    paging__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_paging", title="Extension field for ``paging``."
    )

    parameter: typing.List[fhirtypes.TerminologyCapabilitiesExpansionParameterType] | None = Field(  # type: ignore
        None,
        alias="parameter",
        title="Supported expansion parameter",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    textFilter: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="textFilter",
        title="Documentation about text searching works",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    textFilter__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_textFilter", title="Extension field for ``textFilter``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TerminologyCapabilitiesExpansion`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "hierarchical",
            "paging",
            "incomplete",
            "parameter",
            "textFilter",
        ]


class TerminologyCapabilitiesExpansionParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supported expansion parameter.
    """

    __resource_type__ = "TerminologyCapabilitiesExpansionParameter"

    documentation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Description of support for parameter",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    name: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name of the supported expansion parameter",
        description=None,
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
        ``TerminologyCapabilitiesExpansionParameter`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "documentation"]

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


class TerminologyCapabilitiesImplementation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If this describes a specific instance.
    Identifies a specific implementation instance that is described by the
    terminology capability statement - i.e. a particular installation, rather
    than the capabilities of a software program.
    """

    __resource_type__ = "TerminologyCapabilitiesImplementation"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Describes this specific instance",
        description=(
            "Information about the specific installation that this terminology "
            "capability statement relates to."
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
        title="Base URL for the implementation",
        description="An absolute base URL for the implementation.",
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
        ``TerminologyCapabilitiesImplementation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "description", "url"]

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


class TerminologyCapabilitiesSoftware(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Software that is covered by this terminology capability statement.
    Software that is covered by this terminology capability statement.  It is
    used when the statement describes the capabilities of a particular software
    version, independent of an installation.
    """

    __resource_type__ = "TerminologyCapabilitiesSoftware"

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
        ``TerminologyCapabilitiesSoftware`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "version"]

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


class TerminologyCapabilitiesTranslation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ConceptMap/$translate](conceptmap-operation-
    translate.html) operation.
    """

    __resource_type__ = "TerminologyCapabilitiesTranslation"

    needsMap: bool | None = Field(  # type: ignore
        None,
        alias="needsMap",
        title="Whether the client must identify the map",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    needsMap__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_needsMap", title="Extension field for ``needsMap``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TerminologyCapabilitiesTranslation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "needsMap"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("needsMap", "needsMap__ext")]
        return required_fields


class TerminologyCapabilitiesValidateCode(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ValueSet/$validate-code](valueset-operation-
    validate-code.html) operation.
    """

    __resource_type__ = "TerminologyCapabilitiesValidateCode"

    translations: bool | None = Field(  # type: ignore
        None,
        alias="translations",
        title="Whether translations are validated",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    translations__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_translations", title="Extension field for ``translations``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``TerminologyCapabilitiesValidateCode`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "translations"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("translations", "translations__ext")]
        return required_fields
