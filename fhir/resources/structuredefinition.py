# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class StructureDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structural Definition.
    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
    """

    resource_type = Field("StructureDefinition", const=True)

    abstract: bool = Field(
        ...,
        alias="abstract",
        title="Whether the structure is abstract",
        description=(
            "Whether structure this definition describes is abstract or not  - that"
            " is, whether the structure is not intended to be instantiated. For "
            "Resources and Data types, abstract types will never be exchanged  "
            "between systems."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    abstract__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_abstract", title="Extension field for ``abstract``."
    )

    baseDefinition: fhirtypes.Canonical = Field(
        None,
        alias="baseDefinition",
        title="Definition that this type is constrained/specialized from",
        description=(
            "An absolute URI that is the base structure from which this type is "
            "derived, either by specialization or constraint."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    baseDefinition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_baseDefinition", title="Extension field for ``baseDefinition``."
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    context: ListType[fhirtypes.StructureDefinitionContextType] = Field(
        None,
        alias="context",
        title="If an extension, where it can be used in instances",
        description=(
            "Identifies the types of resource or data type elements to which the "
            "extension can be applied."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contextInvariant: ListType[fhirtypes.String] = Field(
        None,
        alias="contextInvariant",
        title="FHIRPath invariants - when the extension can be used",
        description=(
            "A set of rules as FHIRPath Invariants about when the extension can be "
            "used (e.g. co-occurrence variants for the extension). All the rules "
            "must be true."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contextInvariant__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_contextInvariant",
        title="Extension field for ``contextInvariant``.",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the structure definition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the structure definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the structure definition was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the structure definition "
            "changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    derivation: fhirtypes.Code = Field(
        None,
        alias="derivation",
        title="specialization | constraint - How relates to base definition",
        description="How the type relates to the baseDefinition.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["specialization", "constraint"],
    )
    derivation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_derivation", title="Extension field for ``derivation``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the structure definition",
        description=(
            "A free text natural language description of the structure definition "
            "from a consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    differential: fhirtypes.StructureDefinitionDifferentialType = Field(
        None,
        alias="differential",
        title="Differential view of the structure",
        description=(
            "A differential view is expressed relative to the base "
            "StructureDefinition - a statement of differences that it applies."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this structure definition is authored"
            " for testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fhirVersion: fhirtypes.Code = Field(
        None,
        alias="fhirVersion",
        title="FHIR Version this StructureDefinition targets",
        description=(
            "The version of the FHIR specification on which this "
            "StructureDefinition is based - this is the formal version of the "
            "specification, without the revision number, e.g. "
            "[publication].[major].[minor], which is 4.0.1. for this version."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    fhirVersion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fhirVersion", title="Extension field for ``fhirVersion``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the structure definition",
        description=(
            "A formal identifier that is used to identify this structure definition"
            " when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for structure definition (if applicable)",
        description=(
            "A legal or geographic region in which the structure definition is "
            "intended to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    keyword: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="keyword",
        title="Assist with indexing and finding",
        description=(
            "A set of key words or terms from external terminologies that may be "
            "used to assist with indexing and searching of templates nby describing"
            " the use of this structure definition, or the content it describes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="primitive-type | complex-type | resource | logical",
        description="Defines the kind of structure that this definition is describing.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["primitive-type", "complex-type", "resource", "logical"],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    mapping: ListType[fhirtypes.StructureDefinitionMappingType] = Field(
        None,
        alias="mapping",
        title="External specification that the content is mapped to",
        description="An external specification that the content is mapped to.",
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name for this structure definition (computer friendly)",
        description=(
            "A natural language name identifying the structure definition. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the "
            "structure definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this structure definition is defined",
        description=(
            "Explanation of why this structure definition is needed and why it has "
            "been designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    snapshot: fhirtypes.StructureDefinitionSnapshotType = Field(
        None,
        alias="snapshot",
        title="Snapshot view of the structure",
        description=(
            "A snapshot view is expressed in a standalone form that can be used and"
            " interpreted without considering the base StructureDefinition."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this structure definition. Enables tracking the life-"
            "cycle of the content."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this structure definition (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the structure " "definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.Uri = Field(
        ...,
        alias="type",
        title="Type defined or constrained by this structure",
        description=(
            "The type this structure describes. If the derivation kind is "
            "'specialization' then this is the master definition for a type, and "
            "there is always one of these (a data type, an extension, a resource, "
            "including abstract ones). Otherwise the structure definition is a "
            "constraint on the stated type (and in this case, the type cannot be an"
            " abstract type).  References are URLs that are relative to "
            'http://hl7.org/fhir/StructureDefinition e.g. "string" is a reference '
            "to http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are "
            "only allowed in logical models."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title=(
            "Canonical identifier for this structure definition, represented as a "
            "URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this structure definition "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which at which an "
            "authoritative instance of this structure definition is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the structure definition is stored on "
            "different servers."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate structure definition instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class StructureDefinitionContext(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If an extension, where it can be used in instances.
    Identifies the types of resource or data type elements to which the
    extension can be applied.
    """

    resource_type = Field("StructureDefinitionContext", const=True)

    expression: fhirtypes.String = Field(
        ...,
        alias="expression",
        title="Where the extension can be used in instances",
        description=(
            "An expression that defines where an extension can be used in " "resources."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="fhirpath | element | extension",
        description=(
            "Defines how to interpret the expression that defines what the context "
            "of the extension is."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["fhirpath", "element", "extension"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Differential view of the structure.
    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """

    resource_type = Field("StructureDefinitionDifferential", const=True)

    element: ListType[fhirtypes.ElementDefinitionType] = Field(
        ...,
        alias="element",
        title="Definition of elements in the resource (if no StructureDefinition)",
        description="Captures constraints on each element within the resource.",
        # if property is element of this resource.
        element_property=True,
    )


class StructureDefinitionMapping(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    External specification that the content is mapped to.
    An external specification that the content is mapped to.
    """

    resource_type = Field("StructureDefinitionMapping", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Versions, Issues, Scope limitations etc.",
        description=(
            "Comments about this mapping, including version notes, issues, scope "
            "limitations, and other important notes for usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    identity: fhirtypes.Id = Field(
        ...,
        alias="identity",
        title="Internal id when this mapping is used",
        description=(
            "An Internal id that is used to identify this mapping set when specific"
            " mappings are made."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    identity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_identity", title="Extension field for ``identity``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Names what this mapping refers to",
        description="A name for the specification that is being mapped to.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Identifies what this mapping refers to",
        description=(
            "An absolute URI that identifies the specification that this mapping is"
            " expressed to."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )


class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Snapshot view of the structure.
    A snapshot view is expressed in a standalone form that can be used and
    interpreted without considering the base StructureDefinition.
    """

    resource_type = Field("StructureDefinitionSnapshot", const=True)

    element: ListType[fhirtypes.ElementDefinitionType] = Field(
        ...,
        alias="element",
        title="Definition of elements in the resource (if no StructureDefinition)",
        description="Captures constraints on each element within the resource.",
        # if property is element of this resource.
        element_property=True,
    )
