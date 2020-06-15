# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class TerminologyCapabilities(domainresource.DomainResource):
    """ A statement of system capabilities.
    A TerminologyCapabilities resource documents a set of capabilities
    (behaviors) of a FHIR Terminology Server that may be used as a statement of
    actual server functionality or a statement of required or desired server
    implementation.
    """

    resource_type = Field("TerminologyCapabilities", const=True)

    closure: fhirtypes.TerminologyCapabilitiesClosureType = Field(
        None,
        alias="closure",
        title="Type `TerminologyCapabilitiesClosure` (represented as `dict` in JSON)",
        description=(
            "Information about the [ConceptMap/$closure](conceptmap-operation-"
            "closure.html) operation"
        ),
    )

    codeSearch: fhirtypes.Code = Field(
        None,
        alias="codeSearch",
        title="Type `Code` (represented as `dict` in JSON)",
        description="explicit | all",
    )

    codeSystem: ListType[fhirtypes.TerminologyCapabilitiesCodeSystemType] = Field(
        None,
        alias="codeSystem",
        title=(
            "List of `TerminologyCapabilitiesCodeSystem` items (represented as "
            "`dict` in JSON)"
        ),
        description="A code system supported by the server",
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="List of `ContactDetail` items (represented as `dict` in JSON)",
        description="Contact details for the publisher",
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Use and/or publishing restrictions",
    )

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the terminology capabilities",
    )

    expansion: fhirtypes.TerminologyCapabilitiesExpansionType = Field(
        None,
        alias="expansion",
        title=(
            "Type `TerminologyCapabilitiesExpansion` (represented as `dict` in " "JSON)"
        ),
        description=(
            "Information about the [ValueSet/$expand](valueset-operation-"
            "expand.html) operation"
        ),
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )

    implementation: fhirtypes.TerminologyCapabilitiesImplementationType = Field(
        None,
        alias="implementation",
        title=(
            "Type `TerminologyCapabilitiesImplementation` (represented as `dict` in"
            " JSON)"
        ),
        description="If this describes a specific instance",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for terminology capabilities (if applicable)",
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="Type `Code` (represented as `dict` in JSON)",
        description="instance | capability | requirements",
    )

    lockedDate: bool = Field(
        None,
        alias="lockedDate",
        title="Type `bool`",
        description="Whether lockedDate is supported",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this terminology capabilities (computer friendly)",
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
        description="Why this terminology capabilities is defined",
    )

    software: fhirtypes.TerminologyCapabilitiesSoftwareType = Field(
        None,
        alias="software",
        title="Type `TerminologyCapabilitiesSoftware` (represented as `dict` in JSON)",
        description="Software that is covered by this terminology capability statement",
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
        description="Name for this terminology capabilities (human friendly)",
    )

    translation: fhirtypes.TerminologyCapabilitiesTranslationType = Field(
        None,
        alias="translation",
        title=(
            "Type `TerminologyCapabilitiesTranslation` (represented as `dict` in "
            "JSON)"
        ),
        description=(
            "Information about the [ConceptMap/$translate](conceptmap-operation-"
            "translate.html) operation"
        ),
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description=(
            "Canonical identifier for this terminology capabilities, represented as"
            " a URI (globally unique)"
        ),
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="The context that the content is intended to support",
    )

    validateCode: fhirtypes.TerminologyCapabilitiesValidateCodeType = Field(
        None,
        alias="validateCode",
        title=(
            "Type `TerminologyCapabilitiesValidateCode` (represented as `dict` in "
            "JSON)"
        ),
        description=(
            "Information about the [ValueSet/$validate-code](valueset-operation-"
            "validate-code.html) operation"
        ),
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the terminology capabilities",
    )


class TerminologyCapabilitiesClosure(backboneelement.BackboneElement):
    """ Information about the [ConceptMap/$closure](conceptmap-operation-
    closure.html) operation.
    Whether the $closure operation is supported.
    """

    resource_type = Field("TerminologyCapabilitiesClosure", const=True)

    translation: bool = Field(
        None,
        alias="translation",
        title="Type `bool`",
        description="If cross-system closure is supported",
    )


class TerminologyCapabilitiesCodeSystem(backboneelement.BackboneElement):
    """ A code system supported by the server.
    Identifies a code system that is supported by the server. If there is a no
    code system URL, then this declares the general assumptions a client can
    make about support for any CodeSystem resource.
    """

    resource_type = Field("TerminologyCapabilitiesCodeSystem", const=True)

    subsumption: bool = Field(
        None,
        alias="subsumption",
        title="Type `bool`",
        description="Whether subsumption is supported",
    )

    uri: fhirtypes.Canonical = Field(
        None,
        alias="uri",
        title=(
            "Type `Canonical` referencing `CodeSystem` (represented as `dict` in "
            "JSON)"
        ),
        description="URI for the Code System",
    )

    version: ListType[fhirtypes.TerminologyCapabilitiesCodeSystemVersionType] = Field(
        None,
        alias="version",
        title=(
            "List of `TerminologyCapabilitiesCodeSystemVersion` items (represented "
            "as `dict` in JSON)"
        ),
        description="Version of Code System supported",
    )


class TerminologyCapabilitiesCodeSystemVersion(backboneelement.BackboneElement):
    """ Version of Code System supported.
    For the code system, a list of versions that are supported by the server.
    """

    resource_type = Field("TerminologyCapabilitiesCodeSystemVersion", const=True)

    code: fhirtypes.String = Field(
        None,
        alias="code",
        title="Type `String` (represented as `dict` in JSON)",
        description="Version identifier for this version",
    )

    compositional: bool = Field(
        None,
        alias="compositional",
        title="Type `bool`",
        description="If compositional grammar is supported",
    )

    filter: ListType[
        fhirtypes.TerminologyCapabilitiesCodeSystemVersionFilterType
    ] = Field(
        None,
        alias="filter",
        title=(
            "List of `TerminologyCapabilitiesCodeSystemVersionFilter` items "
            "(represented as `dict` in JSON)"
        ),
        description="Filter Properties supported",
    )

    isDefault: bool = Field(
        None,
        alias="isDefault",
        title="Type `bool`",
        description="If this is the default version for this code system",
    )

    language: ListType[fhirtypes.Code] = Field(
        None,
        alias="language",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="Language Displays supported",
    )

    property: ListType[fhirtypes.Code] = Field(
        None,
        alias="property",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="Properties supported for $lookup",
    )


class TerminologyCapabilitiesCodeSystemVersionFilter(backboneelement.BackboneElement):
    """ Filter Properties supported.
    """

    resource_type = Field("TerminologyCapabilitiesCodeSystemVersionFilter", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Code of the property supported",
    )

    op: ListType[fhirtypes.Code] = Field(
        ...,
        alias="op",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="Operations supported for the property",
    )


class TerminologyCapabilitiesExpansion(backboneelement.BackboneElement):
    """ Information about the [ValueSet/$expand](valueset-operation-expand.html)
    operation.
    """

    resource_type = Field("TerminologyCapabilitiesExpansion", const=True)

    hierarchical: bool = Field(
        None,
        alias="hierarchical",
        title="Type `bool`",
        description="Whether the server can return nested value sets",
    )

    incomplete: bool = Field(
        None,
        alias="incomplete",
        title="Type `bool`",
        description="Allow request for incomplete expansions?",
    )

    paging: bool = Field(
        None,
        alias="paging",
        title="Type `bool`",
        description="Whether the server supports paging on expansion",
    )

    parameter: ListType[
        fhirtypes.TerminologyCapabilitiesExpansionParameterType
    ] = Field(
        None,
        alias="parameter",
        title=(
            "List of `TerminologyCapabilitiesExpansionParameter` items (represented"
            " as `dict` in JSON)"
        ),
        description="Supported expansion parameter",
    )

    textFilter: fhirtypes.Markdown = Field(
        None,
        alias="textFilter",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Documentation about text searching works",
    )


class TerminologyCapabilitiesExpansionParameter(backboneelement.BackboneElement):
    """ Supported expansion parameter.
    """

    resource_type = Field("TerminologyCapabilitiesExpansionParameter", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of support for parameter",
    )

    name: fhirtypes.Code = Field(
        ...,
        alias="name",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Expansion Parameter name",
    )


class TerminologyCapabilitiesImplementation(backboneelement.BackboneElement):
    """ If this describes a specific instance.
    Identifies a specific implementation instance that is described by the
    terminology capability statement - i.e. a particular installation, rather
    than the capabilities of a software program.
    """

    resource_type = Field("TerminologyCapabilitiesImplementation", const=True)

    description: fhirtypes.String = Field(
        ...,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Describes this specific instance",
    )

    url: fhirtypes.Url = Field(
        None,
        alias="url",
        title="Type `Url` (represented as `dict` in JSON)",
        description="Base URL for the implementation",
    )


class TerminologyCapabilitiesSoftware(backboneelement.BackboneElement):
    """ Software that is covered by this terminology capability statement.
    Software that is covered by this terminology capability statement.  It is
    used when the statement describes the capabilities of a particular software
    version, independent of an installation.
    """

    resource_type = Field("TerminologyCapabilitiesSoftware", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="A name the software is known by",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Version covered by this statement",
    )


class TerminologyCapabilitiesTranslation(backboneelement.BackboneElement):
    """ Information about the [ConceptMap/$translate](conceptmap-operation-
    translate.html) operation.
    """

    resource_type = Field("TerminologyCapabilitiesTranslation", const=True)

    needsMap: bool = Field(
        ...,
        alias="needsMap",
        title="Type `bool`",
        description="Whether the client must identify the map",
    )


class TerminologyCapabilitiesValidateCode(backboneelement.BackboneElement):
    """ Information about the [ValueSet/$validate-code](valueset-operation-
    validate-code.html) operation.
    """

    resource_type = Field("TerminologyCapabilitiesValidateCode", const=True)

    translations: bool = Field(
        ...,
        alias="translations",
        title="Type `bool`",
        description="Whether translations are validated",
    )
