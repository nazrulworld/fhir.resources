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
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the graph definition was "
            "published. The date must change if and when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the graph definition "
            "changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the graph definition",
        description=(
            "A free text natural language description of the graph definition from "
            "a consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this graph definition is authored for"
            " testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for graph definition (if applicable)",
        description=(
            "A legal or geographic region in which the graph definition is intended"
            " to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    link: ListType[fhirtypes.GraphDefinitionLinkType] = Field(
        None,
        alias="link",
        title="Links this graph makes rules about",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name for this graph definition (computer friendly)",
        description=(
            "A natural language name identifying the graph definition. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    profile: fhirtypes.Uri = Field(
        None,
        alias="profile",
        title="Profile on base resource",
        description="The profile that describes the use of the base resource.",
        # if property is element of this resource.
        element_property=True,
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the graph "
            "definition."
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
        title="Why this graph definition is defined",
        description=(
            "Explaination of why this graph definition is needed and why it has "
            "been designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    start: fhirtypes.Code = Field(
        ...,
        alias="start",
        title="Type of resource at which the graph starts",
        description="The type of FHIR resource at which instances of this graph start.",
        # if property is element of this resource.
        element_property=True,
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this graph definition. Enables tracking the life-cycle "
            "of the content."
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

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Logical URI to reference this graph definition (globally unique)",
        description=(
            "An absolute URI that is used to identify this graph definition when it"
            " is referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this graph definition is (or will be) published. The URL SHOULD"
            " include the major version of the graph definition. For more "
            "information see [Technical and Business "
            "Versions](resource.html#versions)."
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
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching for appropriate graph definition instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the graph definition",
        description=(
            "The identifier that is used to identify this version of the graph "
            "definition when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the graph definition "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence."
        ),
        # if property is element of this resource.
        element_property=True,
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
        title="Why this link is specified",
        description=(
            "Information about why this link is of interest in this graph "
            "definition."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Maximum occurrences for this link",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.Integer = Field(
        None,
        alias="min",
        title="Minimum occurrences for this link",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    path: fhirtypes.String = Field(
        ...,
        alias="path",
        title="Path in the resource that contains the link",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )

    sliceName: fhirtypes.String = Field(
        None,
        alias="sliceName",
        title="Which slice (if profiled)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    sliceName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sliceName", title="Extension field for ``sliceName``."
    )

    target: ListType[fhirtypes.GraphDefinitionLinkTargetType] = Field(
        ...,
        alias="target",
        title="Potential target for the link",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        title="Compartment Consistency Rules",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    link: ListType[fhirtypes.GraphDefinitionLinkType] = Field(
        None,
        alias="link",
        title="Additional links from target resource",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    profile: fhirtypes.Uri = Field(
        None,
        alias="profile",
        title="Profile for the target resource",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_profile", title="Extension field for ``profile``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type of resource this link refers to",
        description=None,
        # if property is element of this resource.
        element_property=True,
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
        ...,
        alias="code",
        title="Identifies the compartment",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Documentation for FHIRPath expression",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Custom rule, as a FHIRPath expression",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    rule: fhirtypes.Code = Field(
        ...,
        alias="rule",
        title="identical | matching | different | custom",
        description="identical | matching | different | no-rule | custom.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["identical", "matching", "different", "custom"],
    )
    rule__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rule", title="Extension field for ``rule``."
    )
