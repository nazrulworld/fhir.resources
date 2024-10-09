from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImplementationGuide(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of rules about how FHIR is used.
    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used
    to gather all the parts of an implementation guide into a logical whole and
    to publish a computable definition of all the parts.
    """

    __resource_type__ = "ImplementationGuide"

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
            "A copyright statement relating to the implementation guide and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the implementation guide."
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
            "The date  (and optionally time) when the implementation guide was last"
            " significantly changed. The date must change when the business version"
            " changes and it must change if the status code changes. In addition, "
            "it should change when the substantive content of the implementation "
            "guide changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    definition: fhirtypes.ImplementationGuideDefinitionType | None = Field(  # type: ignore
        None,
        alias="definition",
        title="Information needed to build the IG",
        description=(
            "The information needed by an IG publisher tool to publish the whole "
            "implementation guide."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    dependsOn: typing.List[fhirtypes.ImplementationGuideDependsOnType] | None = Field(  # type: ignore
        None,
        alias="dependsOn",
        title="Another Implementation guide this depends on",
        description=(
            "Another implementation guide that this implementation depends on. "
            "Typically, an implementation guide uses value sets, profiles "
            "etc.defined in other implementation guides."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the implementation guide",
        description=(
            "A free text natural language description of the implementation guide "
            "from a consumer's perspective."
        ),
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
            "A Boolean value to indicate that this implementation guide is authored"
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

    fhirVersion: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="fhirVersion",
        title="FHIR Version(s) this Implementation Guide targets",
        description=(
            "The version(s) of the FHIR specification that this ImplementationGuide"
            " targets - e.g. describes how to use. The value of this element is the"
            " formal version of the specification, without the revision number, "
            "e.g. [publication].[major].[minor], which is 4.6.0. for this version."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    fhirVersion__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_fhirVersion", title="Extension field for ``fhirVersion``."
    )

    global_fhir: typing.List[fhirtypes.ImplementationGuideGlobalType] | None = Field(  # type: ignore
        None,
        alias="global",
        title="Profiles that apply globally",
        description=(
            "A set of profiles that all resources covered by this implementation "
            "guide must conform to."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title=(
            "Additional identifier for the implementation guide (business "
            "identifier)"
        ),
        description=(
            "A formal identifier that is used to identify this implementation guide"
            " when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for implementation guide (if applicable)",
        description=(
            "A legal or geographic region in which the implementation guide is "
            "intended to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    license: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="license",
        title="SPDX license code for this IG (or not-open-source)",
        description=(
            "The license that applies to this Implementation Guide, using an SPDX "
            "license code, or 'not-open-source'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    license__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_license", title="Extension field for ``license``."
    )

    manifest: fhirtypes.ImplementationGuideManifestType | None = Field(  # type: ignore
        None,
        alias="manifest",
        title="Information about an assembled IG",
        description=(
            "Information about an assembled implementation guide, created by the "
            "publication tooling."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this implementation guide (computer friendly)",
        description=(
            "A natural language name identifying the implementation guide. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    packageId: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="packageId",
        title="NPM Package name for IG",
        description=(
            "The NPM package name for this Implementation Guide, used in the NPM "
            "package distribution, which is the primary mechanism by which FHIR "
            "based tooling manages IG dependencies. This value must be globally "
            "unique, and should be assigned with care."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    packageId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_packageId", title="Extension field for ``packageId``."
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the implementation guide."
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
        title="Why this implementation guide is defined",
        description=(
            "Explanation of why this implementation guide is needed and why it has "
            "been designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this implementation guide. Enables tracking the life-"
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
        title="Name for this implementation guide (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the implementation " "guide."
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
            "Canonical identifier for this implementation guide, represented as a "
            "URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this implementation guide "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which an "
            "authoritative instance of this implementation guide is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the implementation guide is stored on "
            "different servers."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
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
            "indexing and searching for appropriate implementation guide instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the implementation guide",
        description=(
            "The identifier that is used to identify this version of the "
            "implementation guide when it is referenced in a specification, model, "
            "design or instance. This is an arbitrary value managed by the "
            "implementation guide author and is not expected to be globally unique."
            " For example, it might be a timestamp (e.g. yyyymmdd) if a managed "
            "version is not available. There is also no expectation that versions "
            "can be placed in a lexicographical sequence."
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
        ``ImplementationGuide`` according specification,
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
            "packageId",
            "license",
            "fhirVersion",
            "dependsOn",
            "global",
            "definition",
            "manifest",
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
            ("fhirVersion", "fhirVersion__ext"),
            ("name", "name__ext"),
            ("packageId", "packageId__ext"),
            ("status", "status__ext"),
            ("url", "url__ext"),
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


class ImplementationGuideDefinition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information needed to build the IG.
    The information needed by an IG publisher tool to publish the whole
    implementation guide.
    """

    __resource_type__ = "ImplementationGuideDefinition"

    grouping: typing.List[fhirtypes.ImplementationGuideDefinitionGroupingType] | None = Field(  # type: ignore
        None,
        alias="grouping",
        title="Grouping used to present related resources in the IG",
        description=(
            "A logical group of resources. Logical groups can be used when building"
            " pages."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    page: fhirtypes.ImplementationGuideDefinitionPageType | None = Field(  # type: ignore
        None,
        alias="page",
        title="Page/Section in the Guide",
        description=(
            "A page / section in the implementation guide. The root page is the "
            "implementation guide home page."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    parameter: typing.List[fhirtypes.ImplementationGuideDefinitionParameterType] | None = Field(  # type: ignore
        None,
        alias="parameter",
        title="Defines how IG is built by tools",
        description=(
            "A set of parameters that defines how the implementation guide is "
            "built. The parameters are defined by the relevant tools that build the"
            " implementation guides."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    resource: typing.List[fhirtypes.ImplementationGuideDefinitionResourceType] | None = Field(  # type: ignore
        None,
        alias="resource",
        title="Resource in the implementation guide",
        description=(
            "A resource that is part of the implementation guide. Conformance "
            "resources (value set, structure definition, capability statements "
            "etc.) are obvious candidates for inclusion, but any kind of resource "
            "can be included as an example resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    template: typing.List[fhirtypes.ImplementationGuideDefinitionTemplateType] | None = Field(  # type: ignore
        None,
        alias="template",
        title="A template for building resources",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDefinition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "grouping",
            "resource",
            "page",
            "parameter",
            "template",
        ]


class ImplementationGuideDefinitionGrouping(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Grouping used to present related resources in the IG.
    A logical group of resources. Logical groups can be used when building
    pages.
    """

    __resource_type__ = "ImplementationGuideDefinitionGrouping"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Human readable text describing the package",
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
        title="Descriptive name for the package",
        description=(
            "The human-readable title to display for the package of resources when "
            "rendering the implementation guide."
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
        ``ImplementationGuideDefinitionGrouping`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "description"]

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


class ImplementationGuideDefinitionPage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Page/Section in the Guide.
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """

    __resource_type__ = "ImplementationGuideDefinitionPage"

    generation: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="generation",
        title="html | markdown | xml | generated",
        description="A code that indicates how the page is generated.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["html", "markdown", "xml", "generated"],
        },
    )
    generation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_generation", title="Extension field for ``generation``."
    )

    name: fhirtypes.UrlType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name of the page when published",
        description="The url by which the page should be known when published.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    page: typing.List[fhirtypes.ImplementationGuideDefinitionPageType] | None = Field(  # type: ignore
        None,
        alias="page",
        title="Nested Pages / Sections",
        description="Nested Pages/Sections under this page.",
        json_schema_extra={
            "element_property": True,
        },
    )

    sourceMarkdown: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="sourceMarkdown",
        title="Source for page",
        description="Indicates the URL or the actual content to provide for the page.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e source[x]
            "one_of_many": "source",
            "one_of_many_required": False,
        },
    )
    sourceMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sourceMarkdown", title="Extension field for ``sourceMarkdown``."
    )

    sourceString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="sourceString",
        title="Source for page",
        description="Indicates the URL or the actual content to provide for the page.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e source[x]
            "one_of_many": "source",
            "one_of_many_required": False,
        },
    )
    sourceString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sourceString", title="Extension field for ``sourceString``."
    )

    sourceUrl: fhirtypes.UrlType | None = Field(  # type: ignore
        None,
        alias="sourceUrl",
        title="Source for page",
        description="Indicates the URL or the actual content to provide for the page.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e source[x]
            "one_of_many": "source",
            "one_of_many_required": False,
        },
    )
    sourceUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sourceUrl", title="Extension field for ``sourceUrl``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Short title shown for navigational assistance",
        description=(
            "A short title used to represent this page in navigational structures "
            "such as table of contents, bread crumbs, etc."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDefinitionPage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sourceUrl",
            "sourceString",
            "sourceMarkdown",
            "name",
            "title",
            "generation",
            "page",
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
            ("generation", "generation__ext"),
            ("name", "name__ext"),
            ("title", "title__ext"),
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
        one_of_many_fields = {"source": ["sourceMarkdown", "sourceString", "sourceUrl"]}
        return one_of_many_fields


class ImplementationGuideDefinitionParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines how IG is built by tools.
    A set of parameters that defines how the implementation guide is built. The
    parameters are defined by the relevant tools that build the implementation
    guides.
    """

    __resource_type__ = "ImplementationGuideDefinitionParameter"

    code: fhirtypes.CodingType = Field(  # type: ignore
        ...,
        alias="code",
        title="Code that identifies parameter",
        description="A tool-specific code that defines the parameter.",
        json_schema_extra={
            "element_property": True,
        },
    )

    value: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="value",
        title="Value for named type",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDefinitionParameter`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "value"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
        return required_fields


class ImplementationGuideDefinitionResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource in the implementation guide.
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    __resource_type__ = "ImplementationGuideDefinitionResource"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Reason why included in guide",
        description=(
            "A description of the reason that a resource has been included in the "
            "implementation guide."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    fhirVersion: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="fhirVersion",
        title="Versions this applies to (if different to IG)",
        description=(
            "Indicates the FHIR Version(s) this artifact is intended to apply to. "
            "If no versions are specified, the resource is assumed to apply to all "
            "the versions stated in ImplementationGuide.fhirVersion."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    fhirVersion__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_fhirVersion", title="Extension field for ``fhirVersion``."
    )

    groupingId: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="groupingId",
        title="Grouping this is part of",
        description="Reference to the id of the grouping this resource appears in.",
        json_schema_extra={
            "element_property": True,
        },
    )
    groupingId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_groupingId", title="Extension field for ``groupingId``."
    )

    isExample: bool | None = Field(  # type: ignore
        None,
        alias="isExample",
        title="Is this an example",
        description="If true, indicates the resource is an example instance.",
        json_schema_extra={
            "element_property": True,
        },
    )
    isExample__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_isExample", title="Extension field for ``isExample``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Human readable name for the resource",
        description=(
            "A human assigned name for the resource. All resources SHOULD have a "
            "name, but the name may be extracted from the resource (e.g. "
            "ValueSet.name)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    profile: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="profile",
        title="Profile(s) this is an example of",
        description="If present, indicates profile(s) the instance is valid against.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    profile__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_profile", title="Extension field for ``profile``."
    )

    reference: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="reference",
        title="Location of the resource",
        description="Where this resource is found.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDefinitionResource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "reference",
            "fhirVersion",
            "name",
            "description",
            "isExample",
            "profile",
            "groupingId",
        ]


class ImplementationGuideDefinitionTemplate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A template for building resources.
    """

    __resource_type__ = "ImplementationGuideDefinitionTemplate"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Type of template specified",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    scope: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="scope",
        title="The scope in which the template applies",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    scope__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_scope", title="Extension field for ``scope``."
    )

    source: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="source",
        title="The source location for the template",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_source", title="Extension field for ``source``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDefinitionTemplate`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "code", "source", "scope"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("source", "source__ext")]
        return required_fields


class ImplementationGuideDependsOn(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Another Implementation guide this depends on.
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """

    __resource_type__ = "ImplementationGuideDependsOn"

    packageId: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="packageId",
        title="NPM Package name for IG this depends on",
        description=(
            "The NPM package name for the Implementation Guide that this IG depends"
            " on."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    packageId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_packageId", title="Extension field for ``packageId``."
    )

    reason: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="reason",
        title="Why dependency exists",
        description=(
            "A description explaining the nature of the dependency on the listed " "IG."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    reason__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_reason", title="Extension field for ``reason``."
    )

    uri: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="uri",
        title="Identity of the IG that this depends on",
        description="A canonical reference to the Implementation guide for the dependency.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ImplementationGuide"],
        },
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_uri", title="Extension field for ``uri``."
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Version of the IG",
        description=(
            "The version of the IG that is depended on, when the correct version is"
            " required to understand the IG correctly."
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
        ``ImplementationGuideDependsOn`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "uri",
            "packageId",
            "version",
            "reason",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("uri", "uri__ext")]
        return required_fields


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Profiles that apply globally.
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """

    __resource_type__ = "ImplementationGuideGlobal"

    profile: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="profile",
        title="Profile that all resources must conform to",
        description="A reference to the profile that all instances must conform to.",
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

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type this profile applies to",
        description="The type of resource that all instances must conform to.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideGlobal`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "profile"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("profile", "profile__ext"), ("type", "type__ext")]
        return required_fields


class ImplementationGuideManifest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about an assembled IG.
    Information about an assembled implementation guide, created by the
    publication tooling.
    """

    __resource_type__ = "ImplementationGuideManifest"

    image: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="image",
        title="Image within the IG",
        description="Indicates a relative path to an image that exists within the IG.",
        json_schema_extra={
            "element_property": True,
        },
    )
    image__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_image", title="Extension field for ``image``."
    )

    other: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="other",
        title="Additional linkable file in IG",
        description=(
            "Indicates the relative path of an additional non-page, non-image file "
            "that is part of the IG - e.g. zip, jar and similar files that could be"
            " the target of a hyperlink in a derived IG."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    other__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_other", title="Extension field for ``other``."
    )

    page: typing.List[fhirtypes.ImplementationGuideManifestPageType] | None = Field(  # type: ignore
        None,
        alias="page",
        title="HTML page within the parent IG",
        description="Information about a page within the IG.",
        json_schema_extra={
            "element_property": True,
        },
    )

    rendering: fhirtypes.UrlType | None = Field(  # type: ignore
        None,
        alias="rendering",
        title="Location of rendered implementation guide",
        description=(
            "A pointer to official web page, PDF or other rendering of the "
            "implementation guide."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    rendering__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_rendering", title="Extension field for ``rendering``."
    )

    resource: typing.List[fhirtypes.ImplementationGuideManifestResourceType] = Field(  # type: ignore
        ...,
        alias="resource",
        title="Resource in the implementation guide",
        description=(
            "A resource that is part of the implementation guide. Conformance "
            "resources (value set, structure definition, capability statements "
            "etc.) are obvious candidates for inclusion, but any kind of resource "
            "can be included as an example resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideManifest`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "rendering",
            "resource",
            "page",
            "image",
            "other",
        ]


class ImplementationGuideManifestPage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    HTML page within the parent IG.
    Information about a page within the IG.
    """

    __resource_type__ = "ImplementationGuideManifestPage"

    anchor: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="anchor",
        title="Anchor available on the page",
        description="The name of an anchor available on the page.",
        json_schema_extra={
            "element_property": True,
        },
    )
    anchor__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_anchor", title="Extension field for ``anchor``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="HTML page name",
        description="Relative path to the page.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Title of the page, for references",
        description="Label for the page intended for human display.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideManifestPage`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "title", "anchor"]

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


class ImplementationGuideManifestResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource in the implementation guide.
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    __resource_type__ = "ImplementationGuideManifestResource"

    isExample: bool | None = Field(  # type: ignore
        None,
        alias="isExample",
        title="Is this an example",
        description="If true, indicates the resource is an example instance.",
        json_schema_extra={
            "element_property": True,
        },
    )
    isExample__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_isExample", title="Extension field for ``isExample``."
    )

    profile: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="profile",
        title="Profile(s) this is an example of",
        description="If present, indicates profile(s) the instance is valid against.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    profile__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_profile", title="Extension field for ``profile``."
    )

    reference: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="reference",
        title="Location of the resource",
        description="Where this resource is found.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    relativePath: fhirtypes.UrlType | None = Field(  # type: ignore
        None,
        alias="relativePath",
        title="Relative path for page in IG",
        description="The relative path for primary page for this resource within the IG.",
        json_schema_extra={
            "element_property": True,
        },
    )
    relativePath__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_relativePath", title="Extension field for ``relativePath``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideManifestResource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "reference",
            "isExample",
            "profile",
            "relativePath",
        ]
