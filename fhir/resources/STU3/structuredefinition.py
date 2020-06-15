# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class StructureDefinition(domainresource.DomainResource):
    """ Structural Definition.
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

    baseDefinition: fhirtypes.Uri = Field(
        None,
        alias="baseDefinition",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Definition that this type is constrained/specialized from",
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
        title="List of `String` items (represented as `dict` in JSON)",
        description="Where the extension can be used in instances",
    )

    contextInvariant: ListType[fhirtypes.String] = Field(
        None,
        alias="contextInvariant",
        title="List of `String` items (represented as `dict` in JSON)",
        description="FHIRPath invariants - when the extension can be used",
    )

    contextType: fhirtypes.Code = Field(
        None,
        alias="contextType",
        title="Type `Code` (represented as `dict` in JSON)",
        description="resource | datatype | extension",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date this was last changed",
    )

    derivation: fhirtypes.Code = Field(
        None,
        alias="derivation",
        title="Type `Code` (represented as `dict` in JSON)",
        description="specialization | constraint - How relates to base definition",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the structure definition",
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

    fhirVersion: fhirtypes.Id = Field(
        None,
        alias="fhirVersion",
        title="Type `Id` (represented as `dict` in JSON)",
        description="FHIR Version this StructureDefinition targets",
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
        title="Type `Code` (represented as `dict` in JSON)",
        description="primitive-type | complex-type | resource | logical",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this structure definition (computer friendly)",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Why this structure definition is defined",
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
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this structure definition (human friendly)",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Type defined or constrained by this structure",
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Logical URI to reference this structure definition (globally unique)",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the structure definition",
    )


class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """ Differential view of the structure.
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
    """ External specification that the content is mapped to.
    An external specification that the content is mapped to.
    """

    resource_type = Field("StructureDefinitionMapping", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Versions, Issues, Scope limitations etc.",
    )

    identity: fhirtypes.Id = Field(
        ...,
        alias="identity",
        title="Type `Id` (represented as `dict` in JSON)",
        description="Internal id when this mapping is used",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Names what this mapping refers to",
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Identifies what this mapping refers to",
    )


class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """ Snapshot view of the structure.
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
