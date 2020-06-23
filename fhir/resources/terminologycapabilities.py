# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class TerminologyCapabilities(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A statement of system capabilities.
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
        None, alias="codeSearch", title="Type `Code`", description="explicit | all"
    )
    codeSearch__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_codeSearch", title="Extension field for ``codeSearch``."
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
        title="Type `Markdown`",
        description="Use and/or publishing restrictions",
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        ..., alias="date", title="Type `DateTime`", description="Date last changed"
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown`",
        description="Natural language description of the terminology capabilities",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
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
        title="Type `Code`",
        description="instance | capability | requirements",
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    lockedDate: bool = Field(
        None,
        alias="lockedDate",
        title="Type `bool`",
        description="Whether lockedDate is supported",
    )
    lockedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lockedDate", title="Extension field for ``lockedDate``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this terminology capabilities (computer friendly)",
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
        description="Why this terminology capabilities is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
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
        description="Name for this terminology capabilities (human friendly)",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
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
        title="Type `Uri`",
        description=(
            "Canonical identifier for this terminology capabilities, represented as"
            " a URI (globally unique)"
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
        title="Type `String`",
        description="Business version of the terminology capabilities",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class TerminologyCapabilitiesClosure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ConceptMap/$closure](conceptmap-operation-
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
    translation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_translation", title="Extension field for ``translation``."
    )


class TerminologyCapabilitiesCodeSystem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A code system supported by the server.
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
    subsumption__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subsumption", title="Extension field for ``subsumption``."
    )

    uri: fhirtypes.Canonical = Field(
        None,
        alias="uri",
        title="Type `Canonical` referencing `CodeSystem`",
        description="URI for the Code System",
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
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
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Version of Code System supported.
    For the code system, a list of versions that are supported by the server.
    """

    resource_type = Field("TerminologyCapabilitiesCodeSystemVersion", const=True)

    code: fhirtypes.String = Field(
        None,
        alias="code",
        title="Type `String`",
        description="Version identifier for this version",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    compositional: bool = Field(
        None,
        alias="compositional",
        title="Type `bool`",
        description="If compositional grammar is supported",
    )
    compositional__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_compositional", title="Extension field for ``compositional``."
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
    isDefault__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isDefault", title="Extension field for ``isDefault``."
    )

    language: ListType[fhirtypes.Code] = Field(
        None,
        alias="language",
        title="List of `Code` items",
        description="Language Displays supported",
    )
    language__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    property: ListType[fhirtypes.Code] = Field(
        None,
        alias="property",
        title="List of `Code` items",
        description="Properties supported for $lookup",
    )
    property__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_property", title="Extension field for ``property``."
    )


class TerminologyCapabilitiesCodeSystemVersionFilter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Filter Properties supported.
    """

    resource_type = Field("TerminologyCapabilitiesCodeSystemVersionFilter", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description="Code of the property supported",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    op: ListType[fhirtypes.Code] = Field(
        ...,
        alias="op",
        title="List of `Code` items",
        description="Operations supported for the property",
    )
    op__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_op", title="Extension field for ``op``."
    )


class TerminologyCapabilitiesExpansion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ValueSet/$expand](valueset-operation-expand.html)
    operation.
    """

    resource_type = Field("TerminologyCapabilitiesExpansion", const=True)

    hierarchical: bool = Field(
        None,
        alias="hierarchical",
        title="Type `bool`",
        description="Whether the server can return nested value sets",
    )
    hierarchical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_hierarchical", title="Extension field for ``hierarchical``."
    )

    incomplete: bool = Field(
        None,
        alias="incomplete",
        title="Type `bool`",
        description="Allow request for incomplete expansions?",
    )
    incomplete__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_incomplete", title="Extension field for ``incomplete``."
    )

    paging: bool = Field(
        None,
        alias="paging",
        title="Type `bool`",
        description="Whether the server supports paging on expansion",
    )
    paging__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_paging", title="Extension field for ``paging``."
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
        title="Type `Markdown`",
        description="Documentation about text searching works",
    )
    textFilter__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_textFilter", title="Extension field for ``textFilter``."
    )


class TerminologyCapabilitiesExpansionParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supported expansion parameter.
    """

    resource_type = Field("TerminologyCapabilitiesExpansionParameter", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Description of support for parameter",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    name: fhirtypes.Code = Field(
        ..., alias="name", title="Type `Code`", description="Expansion Parameter name"
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )


class TerminologyCapabilitiesImplementation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If this describes a specific instance.
    Identifies a specific implementation instance that is described by the
    terminology capability statement - i.e. a particular installation, rather
    than the capabilities of a software program.
    """

    resource_type = Field("TerminologyCapabilitiesImplementation", const=True)

    description: fhirtypes.String = Field(
        ...,
        alias="description",
        title="Type `String`",
        description="Describes this specific instance",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    url: fhirtypes.Url = Field(
        None,
        alias="url",
        title="Type `Url`",
        description="Base URL for the implementation",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )


class TerminologyCapabilitiesSoftware(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Software that is covered by this terminology capability statement.
    Software that is covered by this terminology capability statement.  It is
    used when the statement describes the capabilities of a particular software
    version, independent of an installation.
    """

    resource_type = Field("TerminologyCapabilitiesSoftware", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="A name the software is known by",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Version covered by this statement",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class TerminologyCapabilitiesTranslation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ConceptMap/$translate](conceptmap-operation-
    translate.html) operation.
    """

    resource_type = Field("TerminologyCapabilitiesTranslation", const=True)

    needsMap: bool = Field(
        ...,
        alias="needsMap",
        title="Type `bool`",
        description="Whether the client must identify the map",
    )
    needsMap__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_needsMap", title="Extension field for ``needsMap``."
    )


class TerminologyCapabilitiesValidateCode(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ValueSet/$validate-code](valueset-operation-
    validate-code.html) operation.
    """

    resource_type = Field("TerminologyCapabilitiesValidateCode", const=True)

    translations: bool = Field(
        ...,
        alias="translations",
        title="Type `bool`",
        description="Whether translations are validated",
    )
    translations__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_translations", title="Extension field for ``translations``."
    )
