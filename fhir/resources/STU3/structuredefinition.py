# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
        title="Type `bool`",
        description="Whether the structure is abstract",
    )
    abstract__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_abstract", title="Extension field for ``abstract``."
    )

    baseDefinition: fhirtypes.Uri = Field(
        None,
        alias="baseDefinition",
        title="Type `Uri`",
        description="Definition that this type is constrained/specialized from",
    )
    baseDefinition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_baseDefinition", title="Extension field for ``baseDefinition``."
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    context: ListType[fhirtypes.String] = Field(
        None,
        alias="context",
        title="List of `String` items",
        description="Where the extension can be used in instances",
    )
    context__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_context", title="Extension field for ``context``."
    )

    contextInvariant: ListType[fhirtypes.String] = Field(
        None,
        alias="contextInvariant",
        title="List of `String` items",
        description="FHIRPath invariants - when the extension can be used",
    )
    contextInvariant__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_contextInvariant",
        title="Extension field for ``contextInvariant``.",
    )

    contextType: fhirtypes.Code = Field(
        None,
        alias="contextType",
        title="Type `Code`",
        description="resource | datatype | extension",
    )
    contextType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contextType", title="Extension field for ``contextType``."
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown`",
        description="Use and/or publishing restrictions",
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime`",
        description="Date this was last changed",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    derivation: fhirtypes.Code = Field(
        None,
        alias="derivation",
        title="Type `Code`",
        description="specialization | constraint - How relates to base definition",
    )
    derivation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_derivation", title="Extension field for ``derivation``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the structure definition",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    differential: fhirtypes.StructureDefinitionDifferentialType = Field(
        None,
        alias="differential",
        title="Type `StructureDefinitionDifferential` (represented as `dict` in JSON)",
        description="Differential view of the structure",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fhirVersion: fhirtypes.Id = Field(
        None,
        alias="fhirVersion",
        title="Type `Id`",
        description="FHIR Version this StructureDefinition targets",
    )
    fhirVersion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fhirVersion", title="Extension field for ``fhirVersion``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Additional identifier for the structure definition",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for structure definition (if applicable)",
    )

    keyword: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="keyword",
        title="List of `Coding` items (represented as `dict` in JSON)",
        description="Assist with indexing and finding",
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="Type `Code`",
        description="primitive-type | complex-type | resource | logical",
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    mapping: ListType[fhirtypes.StructureDefinitionMappingType] = Field(
        None,
        alias="mapping",
        title=(
            "List of `StructureDefinitionMapping` items (represented as `dict` in "
            "JSON)"
        ),
        description="External specification that the content is mapped to",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Name for this structure definition (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String`",
        description="Name of the publisher (organization or individual)",
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown`",
        description="Why this structure definition is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    snapshot: fhirtypes.StructureDefinitionSnapshotType = Field(
        None,
        alias="snapshot",
        title="Type `StructureDefinitionSnapshot` (represented as `dict` in JSON)",
        description="Snapshot view of the structure",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code`",
        description="draft | active | retired | unknown",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String`",
        description="Name for this structure definition (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="Type defined or constrained by this structure",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this structure definition (globally unique)",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="Context the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Business version of the structure definition",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
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
        title="List of `ElementDefinition` items (represented as `dict` in JSON)",
        description="Definition of elements in the resource (if no StructureDefinition)",
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
        title="Type `String`",
        description="Versions, Issues, Scope limitations etc.",
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    identity: fhirtypes.Id = Field(
        ...,
        alias="identity",
        title="Type `Id`",
        description="Internal id when this mapping is used",
    )
    identity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_identity", title="Extension field for ``identity``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Names what this mapping refers to",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Type `Uri`",
        description="Identifies what this mapping refers to",
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )


class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Snapshot view of the structure.
    A snapshot view is expressed in a stand alone form that can be used and
    interpreted without considering the base StructureDefinition.
    """

    resource_type = Field("StructureDefinitionSnapshot", const=True)

    element: ListType[fhirtypes.ElementDefinitionType] = Field(
        ...,
        alias="element",
        title="List of `ElementDefinition` items (represented as `dict` in JSON)",
        description="Definition of elements in the resource (if no StructureDefinition)",
    )
