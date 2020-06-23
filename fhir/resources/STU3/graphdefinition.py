# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GraphDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class GraphDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of an graph of resources.
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
        title="Type `DateTime`",
        description="Date this was last changed",
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the graph definition",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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
        title="Type `String`",
        description="Name for this graph definition (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    profile: fhirtypes.Uri = Field(
        None,
        alias="profile",
        title="Type `Uri`",
        description="Profile on base resource",
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_profile", title="Extension field for ``profile``."
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
        description="Why this graph definition is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    start: fhirtypes.Code = Field(
        ...,
        alias="start",
        title="Type `Code`",
        description="Type of resource at which the graph starts",
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
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

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this graph definition (globally unique)",
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
        description="Business version of the graph definition",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class GraphDefinitionLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links this graph makes rules about.
    """

    resource_type = Field("GraphDefinitionLink", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Why this link is specified",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Type `String`",
        description="Maximum occurrences for this link",
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.Integer = Field(
        None,
        alias="min",
        title="Type `Integer`",
        description="Minimum occurrences for this link",
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Type `String`",
        description="Path in the resource that contains the link",
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    sliceName: fhirtypes.String = Field(
        None,
        alias="sliceName",
        title="Type `String`",
        description="Which slice (if profiled)",
    )
    sliceName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sliceName", title="Extension field for ``sliceName``."
    )

    target: ListType[fhirtypes.GraphDefinitionLinkTargetType] = Field(
        ...,
        alias="target",
        title=(
            "List of `GraphDefinitionLinkTarget` items (represented as `dict` in "
            "JSON)"
        ),
        description="Potential target for the link",
    )


class GraphDefinitionLinkTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Potential target for the link.
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

    profile: fhirtypes.Uri = Field(
        None,
        alias="profile",
        title="Type `Uri`",
        description="Profile for the target resource",
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description="Type of resource this link refers to",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class GraphDefinitionLinkTargetCompartment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Compartment Consistency Rules.
    """

    resource_type = Field("GraphDefinitionLinkTargetCompartment", const=True)

    code: fhirtypes.Code = Field(
        ..., alias="code", title="Type `Code`", description="Identifies the compartment"
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String`",
        description="Documentation for FHIRPath expression",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String`",
        description="Custom rule, as a FHIRPath expression",
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    rule: fhirtypes.Code = Field(
        ...,
        alias="rule",
        title="Type `Code`",
        description="identical | matching | different | custom",
    )
    rule__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rule", title="Extension field for ``rule``."
    )
