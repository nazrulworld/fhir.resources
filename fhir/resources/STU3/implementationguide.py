from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ImplementationGuide(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of rules about how FHIR is used.
    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into a
    logical whole and to publish a computable definition of all the parts.
    """

    __resource_type__ = "ImplementationGuide"

    binary: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        None,
        alias="binary",
        title="Image, css, script, etc.",
        description=(
            "A binary file that is included in the  implementation guide when it is"
            " published."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    binary__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_binary", title="Extension field for ``binary``."
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

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the implementation guide was "
            "published. The date must change if and when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the implementation "
            "guide changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    dependency: typing.List[fhirtypes.ImplementationGuideDependencyType] | None = Field(  # type: ignore
        None,
        alias="dependency",
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
            "A boolean value to indicate that this implementation guide is authored"
            " for testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fhirVersion: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="fhirVersion",
        title="FHIR Version this Implementation Guide targets",
        description=(
            "The version of the FHIR specification on which this "
            "ImplementationGuide is based - this is the formal version of the "
            "specification, without the revision number, e.g. "
            "[publication].[major].[minor], which is 3.0.2 for this version."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    fhirVersion__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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

    package: typing.List[fhirtypes.ImplementationGuidePackageType] | None = Field(  # type: ignore
        None,
        alias="package",
        title="Group of resources as used in .page.package",
        description=(
            "A logical group of resources. Logical groups can be used when building"
            " pages."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    page: fhirtypes.ImplementationGuidePageType | None = Field(  # type: ignore
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

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the "
            "implementation guide."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
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

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Logical URI to reference this implementation guide (globally unique)",
        description=(
            "An absolute URI that is used to identify this implementation guide "
            "when it is referenced in a specification, model, design or an "
            "instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD "
            "be an address at which this implementation guide is (or will be) "
            "published. The URL SHOULD include the major version of the "
            "implementation guide. For more information see [Technical and Business"
            " Versions](resource.html#versions)."
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
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
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
            "version",
            "name",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "copyright",
            "fhirVersion",
            "dependency",
            "package",
            "global",
            "binary",
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
            ("name", "name__ext"),
            ("status", "status__ext"),
            ("url", "url__ext"),
        ]
        return required_fields


class ImplementationGuideDependency(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Another Implementation guide this depends on.
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """

    __resource_type__ = "ImplementationGuideDependency"

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="reference | inclusion",
        description="How the dependency is represented when the guide is published.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["reference", "inclusion"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    uri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="uri",
        title="Where to find dependency",
        description="Where the dependency is located.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_uri", title="Extension field for ``uri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuideDependency`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "uri"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext"), ("uri", "uri__ext")]
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

    profile: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="profile",
        title="Profile that all resources must conform to",
        description="A reference to the profile that all instances must conform to.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type this profiles applies to",
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
        required_fields = [("type", "type__ext")]
        return required_fields


class ImplementationGuidePackage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Group of resources as used in .page.package.
    A logical group of resources. Logical groups can be used when building
    pages.
    """

    __resource_type__ = "ImplementationGuidePackage"

    description: fhirtypes.StringType | None = Field(  # type: ignore
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
        title="Name used .page.package",
        description="The name for the group, as used in page.package.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    resource: typing.List[fhirtypes.ImplementationGuidePackageResourceType] = Field(  # type: ignore
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
        ``ImplementationGuidePackage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "description",
            "resource",
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


class ImplementationGuidePackageResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource in the implementation guide.
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    __resource_type__ = "ImplementationGuidePackageResource"

    acronym: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="acronym",
        title="Short code to identify the resource",
        description=(
            "A short code that may be used to identify the resource throughout the "
            "implementation guide."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    acronym__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_acronym", title="Extension field for ``acronym``."
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
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

    example: bool | None = Field(  # type: ignore
        None,
        alias="example",
        title="If not an example, has its normal meaning",
        description=(
            "Whether a resource is included in the guide as part of the rules "
            "defined by the guide, or just as an example of a resource that "
            "conforms to the rules and/or help implementers understand the intent "
            "of the guide."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    example__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_example", title="Extension field for ``example``."
    )

    exampleFor: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="exampleFor",
        title="Resource this is an example of (if applicable)",
        description=(
            "Another resource that this resource is an example for. This is mostly "
            "used for resources that are included as examples of "
            "StructureDefinitions."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Human Name for the resource",
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

    sourceReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="sourceReference",
        title="Location of the resource",
        description="Where this resource is found.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e source[x]
            "one_of_many": "source",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    sourceUri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="sourceUri",
        title="Location of the resource",
        description="Where this resource is found.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e source[x]
            "one_of_many": "source",
            "one_of_many_required": True,
        },
    )
    sourceUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sourceUri", title="Extension field for ``sourceUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuidePackageResource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "example",
            "name",
            "description",
            "acronym",
            "sourceUri",
            "sourceReference",
            "exampleFor",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("example", "example__ext")]
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
        one_of_many_fields = {"source": ["sourceReference", "sourceUri"]}
        return one_of_many_fields


class ImplementationGuidePage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Page/Section in the Guide.
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """

    __resource_type__ = "ImplementationGuidePage"

    format: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="format",
        title="Format of the page (e.g. html, markdown, etc.)",
        description="The format of the page.",
        json_schema_extra={
            "element_property": True,
        },
    )
    format__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_format", title="Extension field for ``format``."
    )

    kind: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="kind",
        title=(
            "page | example | list | include | directory | dictionary | toc | "
            "resource"
        ),
        description=(
            "The kind of page that this is. Some pages are autogenerated (list, "
            "example), and other kinds are of interest so that tools can navigate "
            "the user to the page of interest."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "page",
                "example",
                "list",
                "include",
                "directory",
                "dictionary",
                "toc",
                "resource",
            ],
        },
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_kind", title="Extension field for ``kind``."
    )

    package: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="package",
        title="Name of package to include",
        description=(
            "For constructed pages, a list of packages to include in the page (or "
            "else empty for everything)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    package__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_package", title="Extension field for ``package``."
    )

    page: typing.List[fhirtypes.ImplementationGuidePageType] | None = Field(  # type: ignore
        None,
        alias="page",
        title="Nested Pages / Sections",
        description="Nested Pages/Sections under this page.",
        json_schema_extra={
            "element_property": True,
        },
    )

    source: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="source",
        title="Where to find that page",
        description="The source address for the page.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_source", title="Extension field for ``source``."
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

    type: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="type",
        title="Kind of resource to include in the list",
        description="For constructed pages, what kind of resources to include in the list.",
        json_schema_extra={
            "element_property": True,
        },
    )
    type__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImplementationGuidePage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "source",
            "title",
            "kind",
            "type",
            "package",
            "format",
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
            ("kind", "kind__ext"),
            ("source", "source__ext"),
            ("title", "title__ext"),
        ]
        return required_fields
