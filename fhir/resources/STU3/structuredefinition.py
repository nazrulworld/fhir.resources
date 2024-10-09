from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class StructureDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structural Definition.
    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
    """

    __resource_type__ = "StructureDefinition"

    abstract: bool | None = Field(  # type: ignore
        None,
        alias="abstract",
        title="Whether the structure is abstract",
        description=(
            "Whether structure this definition describes is abstract or not  - that"
            " is, whether the structure is not intended to be instantiated. For "
            "Resources and Data types, abstract types will never be exchanged  "
            "between systems."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    abstract__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_abstract", title="Extension field for ``abstract``."
    )

    baseDefinition: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="baseDefinition",
        title="Definition that this type is constrained/specialized from",
        description=(
            "An absolute URI that is the base structure from which this type is "
            "derived, either by specialization or constraint."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    baseDefinition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_baseDefinition", title="Extension field for ``baseDefinition``."
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

    context: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="context",
        title="Where the extension can be used in instances",
        description=(
            "Identifies the types of resource or data type elements to which the "
            "extension can be applied."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    context__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_context", title="Extension field for ``context``."
    )

    contextInvariant: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="contextInvariant",
        title="FHIRPath invariants - when the extension can be used",
        description=(
            "A set of rules as Fluent Invariants about when the extension can be "
            "used (e.g. co-occurrence variants for the extension)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    contextInvariant__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None,
        alias="_contextInvariant",
        title="Extension field for ``contextInvariant``.",
    )

    contextType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="contextType",
        title="resource | datatype | extension",
        description=(
            "If this is an extension, Identifies the context within FHIR resources "
            "where the extension can be used."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["resource", "datatype", "extension"],
        },
    )
    contextType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_contextType", title="Extension field for ``contextType``."
    )

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the structure definition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the structure definition."
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
            "The date  (and optionally time) when the structure definition was "
            "published. The date must change if and when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the structure "
            "definition changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    derivation: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="derivation",
        title="specialization | constraint - How relates to base definition",
        description="How the type relates to the baseDefinition.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["specialization", "constraint"],
        },
    )
    derivation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_derivation", title="Extension field for ``derivation``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the structure definition",
        description=(
            "A free text natural language description of the structure definition "
            "from a consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    differential: fhirtypes.StructureDefinitionDifferentialType | None = Field(  # type: ignore
        None,
        alias="differential",
        title="Differential view of the structure",
        description=(
            "A differential view is expressed relative to the base "
            "StructureDefinition - a statement of differences that it applies."
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
            "A boolean value to indicate that this structure definition is authored"
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
        title="FHIR Version this StructureDefinition targets",
        description=(
            "The version of the FHIR specification on which this "
            "StructureDefinition is based - this is the formal version of the "
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

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the structure definition",
        description=(
            "A formal identifier that is used to identify this structure definition"
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
        title="Intended jurisdiction for structure definition (if applicable)",
        description=(
            "A legal or geographic region in which the structure definition is "
            "intended to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    keyword: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        None,
        alias="keyword",
        title="Assist with indexing and finding",
        description=(
            "A set of key words or terms from external terminologies that may be "
            "used to assist with indexing and searching of templates."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    kind: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="kind",
        title="primitive-type | complex-type | resource | logical",
        description="Defines the kind of structure that this definition is describing.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["primitive-type", "complex-type", "resource", "logical"],
        },
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_kind", title="Extension field for ``kind``."
    )

    mapping: typing.List[fhirtypes.StructureDefinitionMappingType] | None = Field(  # type: ignore
        None,
        alias="mapping",
        title="External specification that the content is mapped to",
        description="An external specification that the content is mapped to.",
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this structure definition (computer friendly)",
        description=(
            "A natural language name identifying the structure definition. This "
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

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the "
            "structure definition."
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
        title="Why this structure definition is defined",
        description=(
            "Explaination of why this structure definition is needed and why it has"
            " been designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    snapshot: fhirtypes.StructureDefinitionSnapshotType | None = Field(  # type: ignore
        None,
        alias="snapshot",
        title="Snapshot view of the structure",
        description=(
            "A snapshot view is expressed in a stand alone form that can be used "
            "and interpreted without considering the base StructureDefinition."
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
            "The status of this structure definition. Enables tracking the life-"
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
        title="Name for this structure definition (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the structure " "definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Type defined or constrained by this structure",
        description=(
            "The type this structure describes. If the derivation kind is "
            "'specialization' then this is the master definition for a type, and "
            "there is always one of these (a data type, an extension, a resource, "
            "including abstract ones). Otherwise the structure definition is a "
            "constraint on the stated type (and in this case, the type cannot be an"
            " abstract type)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Logical URI to reference this structure definition (globally unique)",
        description=(
            "An absolute URI that is used to identify this structure definition "
            "when it is referenced in a specification, model, design or an "
            "instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD "
            "be an address at which this structure definition is (or will be) "
            "published. The URL SHOULD include the major version of the structure "
            "definition. For more information see [Technical and Business "
            "Versions](resource.html#versions)."
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
            "indexing and searching for appropriate structure definition instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the structure definition",
        description=(
            "The identifier that is used to identify this version of the structure "
            "definition when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the structure "
            "definition author and is not expected to be globally unique. For "
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

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureDefinition`` according specification,
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
            "keyword",
            "fhirVersion",
            "mapping",
            "kind",
            "abstract",
            "contextType",
            "context",
            "contextInvariant",
            "type",
            "baseDefinition",
            "derivation",
            "snapshot",
            "differential",
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
            ("abstract", "abstract__ext"),
            ("kind", "kind__ext"),
            ("name", "name__ext"),
            ("status", "status__ext"),
            ("type", "type__ext"),
            ("url", "url__ext"),
        ]
        return required_fields


class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Differential view of the structure.
    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """

    __resource_type__ = "StructureDefinitionDifferential"

    element: typing.List[fhirtypes.ElementDefinitionType] = Field(  # type: ignore
        ...,
        alias="element",
        title="Definition of elements in the resource (if no StructureDefinition)",
        description="Captures constraints on each element within the resource.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureDefinitionDifferential`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "element"]


class StructureDefinitionMapping(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    External specification that the content is mapped to.
    An external specification that the content is mapped to.
    """

    __resource_type__ = "StructureDefinitionMapping"

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Versions, Issues, Scope limitations etc.",
        description=(
            "Comments about this mapping, including version notes, issues, scope "
            "limitations, and other important notes for usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    identity: fhirtypes.IdType | None = Field(  # type: ignore
        None,
        alias="identity",
        title="Internal id when this mapping is used",
        description=(
            "An Internal id that is used to identify this mapping set when specific"
            " mappings are made."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    identity__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_identity", title="Extension field for ``identity``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Names what this mapping refers to",
        description="A name for the specification that is being mapped to.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    uri: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="uri",
        title="Identifies what this mapping refers to",
        description=(
            "An absolute URI that identifies the specification that this mapping is"
            " expressed to."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_uri", title="Extension field for ``uri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureDefinitionMapping`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identity",
            "uri",
            "name",
            "comment",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("identity", "identity__ext")]
        return required_fields


class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Snapshot view of the structure.
    A snapshot view is expressed in a stand alone form that can be used and
    interpreted without considering the base StructureDefinition.
    """

    __resource_type__ = "StructureDefinitionSnapshot"

    element: typing.List[fhirtypes.ElementDefinitionType] = Field(  # type: ignore
        ...,
        alias="element",
        title="Definition of elements in the resource (if no StructureDefinition)",
        description="Captures constraints on each element within the resource.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``StructureDefinitionSnapshot`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "element"]
