# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SearchParameter
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SearchParameter(domainresource.DomainResource):
    """ Search parameter for a resource.
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """

    resource_type = Field("SearchParameter", const=True)

    base: ListType[fhirtypes.Code] = Field(
        ...,
        alias="base",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="The resource type(s) this search parameter applies to",
    )

    chain: ListType[fhirtypes.String] = Field(
        None,
        alias="chain",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Chained names supported",
    )

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Code used in URL",
    )

    comparator: ListType[fhirtypes.Code] = Field(
        None,
        alias="comparator",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="eq | ne | gt | lt | ge | le | sa | eb | ap",
    )

    component: ListType[fhirtypes.SearchParameterComponentType] = Field(
        None,
        alias="component",
        title=(
            "List of `SearchParameterComponent` items (represented as `dict` in "
            "JSON)"
        ),
        description="For Composite resources to define the parts",
    )

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

    derivedFrom: fhirtypes.Canonical = Field(
        None,
        alias="derivedFrom",
        title=(
            "Type `Canonical` referencing `SearchParameter` (represented as `dict` "
            "in JSON)"
        ),
        description="Original definition for the search parameter",
    )

    description: fhirtypes.Markdown = Field(
        ...,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the search parameter",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String` (represented as `dict` in JSON)",
        description="FHIRPath expression that extracts the values",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for search parameter (if applicable)",
    )

    modifier: ListType[fhirtypes.Code] = Field(
        None,
        alias="modifier",
        title="List of `Code` items (represented as `dict` in JSON)",
        description=(
            "missing | exact | contains | not | text | in | not-in | below | above "
            "| type | identifier | ofType"
        ),
    )

    multipleAnd: bool = Field(
        None,
        alias="multipleAnd",
        title="Type `bool`",
        description="Allow multiple parameters (and)",
    )

    multipleOr: bool = Field(
        None,
        alias="multipleOr",
        title="Type `bool`",
        description="Allow multiple values per parameter (or)",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this search parameter (computer friendly)",
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
        description="Why this search parameter is defined",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    target: ListType[fhirtypes.Code] = Field(
        None,
        alias="target",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="Types of resource (if a resource reference)",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "number | date | string | token | reference | composite | quantity | "
            "uri | special"
        ),
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description=(
            "Canonical identifier for this search parameter, represented as a URI "
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
        description="Business version of the search parameter",
    )

    xpath: fhirtypes.String = Field(
        None,
        alias="xpath",
        title="Type `String` (represented as `dict` in JSON)",
        description="XPath that extracts the values",
    )

    xpathUsage: fhirtypes.Code = Field(
        None,
        alias="xpathUsage",
        title="Type `Code` (represented as `dict` in JSON)",
        description="normal | phonetic | nearby | distance | other",
    )


class SearchParameterComponent(backboneelement.BackboneElement):
    """ For Composite resources to define the parts.
    Used to define the parts of a composite search parameter.
    """

    resource_type = Field("SearchParameterComponent", const=True)

    definition: fhirtypes.Canonical = Field(
        ...,
        alias="definition",
        title=(
            "Type `Canonical` referencing `SearchParameter` (represented as `dict` "
            "in JSON)"
        ),
        description="Defines how the part works",
    )

    expression: fhirtypes.String = Field(
        ...,
        alias="expression",
        title="Type `String` (represented as `dict` in JSON)",
        description="Subexpression relative to main expression",
    )
