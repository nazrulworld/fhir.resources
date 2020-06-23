# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SearchParameter
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SearchParameter(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Search parameter for a resource.
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """

    resource_type = Field("SearchParameter", const=True)

    base: ListType[fhirtypes.Code] = Field(
        ...,
        alias="base",
        title="List of `Code` items",
        description="The resource type(s) this search parameter applies to",
    )
    base__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_base", title="Extension field for ``base``."
    )

    chain: ListType[fhirtypes.String] = Field(
        None,
        alias="chain",
        title="List of `String` items",
        description="Chained names supported",
    )
    chain__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_chain", title="Extension field for ``chain``."
    )

    code: fhirtypes.Code = Field(
        ..., alias="code", title="Type `Code`", description="Code used in URL"
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    comparator: ListType[fhirtypes.Code] = Field(
        None,
        alias="comparator",
        title="List of `Code` items",
        description="eq | ne | gt | lt | ge | le | sa | eb | ap",
    )
    comparator__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_comparator", title="Extension field for ``comparator``.")

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
        None, alias="date", title="Type `DateTime`", description="Date last changed"
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFrom: fhirtypes.Canonical = Field(
        None,
        alias="derivedFrom",
        title="Type `Canonical` referencing `SearchParameter`",
        description="Original definition for the search parameter",
    )
    derivedFrom__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_derivedFrom", title="Extension field for ``derivedFrom``."
    )

    description: fhirtypes.Markdown = Field(
        ...,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the search parameter",
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

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Type `String`",
        description="FHIRPath expression that extracts the values",
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
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
        title="List of `Code` items",
        description=(
            "missing | exact | contains | not | text | in | not-in | below | above "
            "| type | identifier | ofType"
        ),
    )
    modifier__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_modifier", title="Extension field for ``modifier``."
    )

    multipleAnd: bool = Field(
        None,
        alias="multipleAnd",
        title="Type `bool`",
        description="Allow multiple parameters (and)",
    )
    multipleAnd__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_multipleAnd", title="Extension field for ``multipleAnd``."
    )

    multipleOr: bool = Field(
        None,
        alias="multipleOr",
        title="Type `bool`",
        description="Allow multiple values per parameter (or)",
    )
    multipleOr__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_multipleOr", title="Extension field for ``multipleOr``."
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Name for this search parameter (computer friendly)",
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
        description="Why this search parameter is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
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

    target: ListType[fhirtypes.Code] = Field(
        None,
        alias="target",
        title="List of `Code` items",
        description="Types of resource (if a resource reference)",
    )
    target__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_target", title="Extension field for ``target``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type `Code`",
        description=(
            "number | date | string | token | reference | composite | quantity | "
            "uri | special"
        ),
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Type `Uri`",
        description=(
            "Canonical identifier for this search parameter, represented as a URI "
            "(globally unique)"
        ),
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
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
        title="Type `String`",
        description="Business version of the search parameter",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    xpath: fhirtypes.String = Field(
        None,
        alias="xpath",
        title="Type `String`",
        description="XPath that extracts the values",
    )
    xpath__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_xpath", title="Extension field for ``xpath``."
    )

    xpathUsage: fhirtypes.Code = Field(
        None,
        alias="xpathUsage",
        title="Type `Code`",
        description="normal | phonetic | nearby | distance | other",
    )
    xpathUsage__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_xpathUsage", title="Extension field for ``xpathUsage``."
    )


class SearchParameterComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    For Composite resources to define the parts.
    Used to define the parts of a composite search parameter.
    """

    resource_type = Field("SearchParameterComponent", const=True)

    definition: fhirtypes.Canonical = Field(
        ...,
        alias="definition",
        title="Type `Canonical` referencing `SearchParameter`",
        description="Defines how the part works",
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    expression: fhirtypes.String = Field(
        ...,
        alias="expression",
        title="Type `String`",
        description="Subexpression relative to main expression",
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )
