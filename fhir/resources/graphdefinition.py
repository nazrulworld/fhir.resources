# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GraphDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class GraphDefinition(domainresource.DomainResource):
    """ Definition of a graph of resources.
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """

    resource_type = Field("GraphDefinition", const=True)

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the graph definition",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for graph definition (if applicable)",
    )

    link: ListType[fhirtypes.GraphDefinitionLinkType] = Field(
        None,
        alias="link",
        title="List of `GraphDefinitionLink` items (represented as `dict` in JSON)",
        description="Links this graph makes rules about",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this graph definition (computer friendly)",
    )

    profile: fhirtypes.Canonical = Field(
        None,
        alias="profile",
        title=(
            "Type `Canonical` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Profile on base resource",
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
        description="Why this graph definition is defined",
    )

    start: fhirtypes.Code = Field(
        ...,
        alias="start",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Type of resource at which the graph starts",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description=(
            "Canonical identifier for this graph definition, represented as a URI "
            "(globally unique)"
        ),
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="The context that the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the graph definition",
    )


class GraphDefinitionLink(backboneelement.BackboneElement):
    """ Links this graph makes rules about.
    """

    resource_type = Field("GraphDefinitionLink", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Why this link is specified",
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Type `String` (represented as `dict` in JSON)",
        description="Maximum occurrences for this link",
    )

    min: fhirtypes.Integer = Field(
        None,
        alias="min",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Minimum occurrences for this link",
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="Type `String` (represented as `dict` in JSON)",
        description="Path in the resource that contains the link",
    )

    sliceName: fhirtypes.String = Field(
        None,
        alias="sliceName",
        title="Type `String` (represented as `dict` in JSON)",
        description="Which slice (if profiled)",
    )

    target: ListType[fhirtypes.GraphDefinitionLinkTargetType] = Field(
        None,
        alias="target",
        title=(
            "List of `GraphDefinitionLinkTarget` items (represented as `dict` in "
            "JSON)"
        ),
        description="Potential target for the link",
    )


class GraphDefinitionLinkTarget(backboneelement.BackboneElement):
    """ Potential target for the link.
    """

    resource_type = Field("GraphDefinitionLinkTarget", const=True)

    compartment: ListType[fhirtypes.GraphDefinitionLinkTargetCompartmentType] = Field(
        None,
        alias="compartment",
        title=(
            "List of `GraphDefinitionLinkTargetCompartment` items (represented as "
            "`dict` in JSON)"
        ),
        description="Compartment Consistency Rules",
    )

    link: ListType[fhirtypes.GraphDefinitionLinkType] = Field(
        None,
        alias="link",
        title="List of `GraphDefinitionLink` items (represented as `dict` in JSON)",
        description="Additional links from target resource",
    )

    params: fhirtypes.String = Field(
        None,
        alias="params",
        title="Type `String` (represented as `dict` in JSON)",
        description="Criteria for reverse lookup",
    )

    profile: fhirtypes.Canonical = Field(
        None,
        alias="profile",
        title=(
            "Type `Canonical` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Profile for the target resource",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Type of resource this link refers to",
    )


class GraphDefinitionLinkTargetCompartment(backboneelement.BackboneElement):
    """ Compartment Consistency Rules.
    """

    resource_type = Field("GraphDefinitionLinkTargetCompartment", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Patient | Encounter | RelatedPerson | Practitioner | Device",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Documentation for FHIRPath expression",
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String` (represented as `dict` in JSON)",
        description="Custom rule, as a FHIRPath expression",
    )

    rule: fhirtypes.Code = Field(
        ...,
        alias="rule",
        title="Type `Code` (represented as `dict` in JSON)",
        description="identical | matching | different | custom",
    )

    use: fhirtypes.Code = Field(
        ...,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="condition | requirement",
    )
