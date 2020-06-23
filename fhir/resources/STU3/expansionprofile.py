# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExpansionProfile
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ExpansionProfile(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines behaviour and contraints on the ValueSet Expansion operation.
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    resource_type = Field("ExpansionProfile", const=True)

    activeOnly: bool = Field(
        None,
        alias="activeOnly",
        title="Type `bool`",
        description="Include or exclude inactive concepts in the expansion",
    )
    activeOnly__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_activeOnly", title="Extension field for ``activeOnly``."
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
        description="Natural language description of the expansion profile",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    designation: fhirtypes.ExpansionProfileDesignationType = Field(
        None,
        alias="designation",
        title="Type `ExpansionProfileDesignation` (represented as `dict` in JSON)",
        description="When the expansion profile imposes designation contraints",
    )

    displayLanguage: fhirtypes.Code = Field(
        None,
        alias="displayLanguage",
        title="Type `Code`",
        description=(
            "Specify the language for the display element of codes in the value set"
            " expansion"
        ),
    )
    displayLanguage__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_displayLanguage", title="Extension field for ``displayLanguage``."
    )

    excludeNested: bool = Field(
        None,
        alias="excludeNested",
        title="Type `bool`",
        description="Nested codes in the expansion or not",
    )
    excludeNested__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_excludeNested", title="Extension field for ``excludeNested``."
    )

    excludeNotForUI: bool = Field(
        None,
        alias="excludeNotForUI",
        title="Type `bool`",
        description=(
            "Include or exclude codes which cannot be rendered in user interfaces "
            "in the value set expansion"
        ),
    )
    excludeNotForUI__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_excludeNotForUI", title="Extension field for ``excludeNotForUI``."
    )

    excludePostCoordinated: bool = Field(
        None,
        alias="excludePostCoordinated",
        title="Type `bool`",
        description=(
            "Include or exclude codes which are post coordinated expressions in the"
            " value set expansion"
        ),
    )
    excludePostCoordinated__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_excludePostCoordinated",
        title="Extension field for ``excludePostCoordinated``.",
    )

    excludedSystem: fhirtypes.ExpansionProfileExcludedSystemType = Field(
        None,
        alias="excludedSystem",
        title="Type `ExpansionProfileExcludedSystem` (represented as `dict` in JSON)",
        description="Systems/Versions to be exclude",
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

    fixedVersion: ListType[fhirtypes.ExpansionProfileFixedVersionType] = Field(
        None,
        alias="fixedVersion",
        title=(
            "List of `ExpansionProfileFixedVersion` items (represented as `dict` in"
            " JSON)"
        ),
        description="Fix use of a code system to a particular version",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Additional identifier for the expansion profile",
    )

    includeDefinition: bool = Field(
        None,
        alias="includeDefinition",
        title="Type `bool`",
        description="Include or exclude the value set definition in the expansion",
    )
    includeDefinition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_includeDefinition",
        title="Extension field for ``includeDefinition``.",
    )

    includeDesignations: bool = Field(
        None,
        alias="includeDesignations",
        title="Type `bool`",
        description="Whether the expansion should include concept designations",
    )
    includeDesignations__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_includeDesignations",
        title="Extension field for ``includeDesignations``.",
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for expansion profile (if applicable)",
    )

    limitedExpansion: bool = Field(
        None,
        alias="limitedExpansion",
        title="Type `bool`",
        description=(
            "Controls behaviour of the value set expand operation when value sets "
            "are too large to be completely expanded"
        ),
    )
    limitedExpansion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_limitedExpansion",
        title="Extension field for ``limitedExpansion``.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String`",
        description="Name for this expansion profile (computer friendly)",
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
        description="Logical URI to reference this expansion profile (globally unique)",
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
        description="Business version of the expansion profile",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class ExpansionProfileDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    When the expansion profile imposes designation contraints.
    A set of criteria that provide the constraints imposed on the value set
    expansion by including or excluding designations.
    """

    resource_type = Field("ExpansionProfileDesignation", const=True)

    exclude: fhirtypes.ExpansionProfileDesignationExcludeType = Field(
        None,
        alias="exclude",
        title=(
            "Type `ExpansionProfileDesignationExclude` (represented as `dict` in "
            "JSON)"
        ),
        description="Designations to be excluded",
    )

    include: fhirtypes.ExpansionProfileDesignationIncludeType = Field(
        None,
        alias="include",
        title=(
            "Type `ExpansionProfileDesignationInclude` (represented as `dict` in "
            "JSON)"
        ),
        description="Designations to be included",
    )


class ExpansionProfileDesignationExclude(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Designations to be excluded.
    """

    resource_type = Field("ExpansionProfileDesignationExclude", const=True)

    designation: ListType[
        fhirtypes.ExpansionProfileDesignationExcludeDesignationType
    ] = Field(
        None,
        alias="designation",
        title=(
            "List of `ExpansionProfileDesignationExcludeDesignation` items "
            "(represented as `dict` in JSON)"
        ),
        description="The designation to be excluded",
    )


class ExpansionProfileDesignationExcludeDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The designation to be excluded.
    A data group for each designation to be excluded.
    """

    resource_type = Field("ExpansionProfileDesignationExcludeDesignation", const=True)

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Type `Code`",
        description="Human language of the designation to be excluded",
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    use: fhirtypes.CodingType = Field(
        None,
        alias="use",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="What kind of Designation to exclude",
    )


class ExpansionProfileDesignationInclude(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Designations to be included.
    """

    resource_type = Field("ExpansionProfileDesignationInclude", const=True)

    designation: ListType[
        fhirtypes.ExpansionProfileDesignationIncludeDesignationType
    ] = Field(
        None,
        alias="designation",
        title=(
            "List of `ExpansionProfileDesignationIncludeDesignation` items "
            "(represented as `dict` in JSON)"
        ),
        description="The designation to be included",
    )


class ExpansionProfileDesignationIncludeDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The designation to be included.
    A data group for each designation to be included.
    """

    resource_type = Field("ExpansionProfileDesignationIncludeDesignation", const=True)

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Type `Code`",
        description="Human language of the designation to be included",
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    use: fhirtypes.CodingType = Field(
        None,
        alias="use",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="What kind of Designation to include",
    )


class ExpansionProfileExcludedSystem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Systems/Versions to be exclude.
    Code system, or a particular version of a code system to be excluded from
    value set expansions.
    """

    resource_type = Field("ExpansionProfileExcludedSystem", const=True)

    system: fhirtypes.Uri = Field(
        ...,
        alias="system",
        title="Type `Uri`",
        description="The specific code system to be excluded",
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String`",
        description="Specific version of the code system referred to",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class ExpansionProfileFixedVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Fix use of a code system to a particular version.
    Fix use of a particular code system to a particular version.
    """

    resource_type = Field("ExpansionProfileFixedVersion", const=True)

    mode: fhirtypes.Code = Field(
        ..., alias="mode", title="Type `Code`", description="default | check | override"
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    system: fhirtypes.Uri = Field(
        ...,
        alias="system",
        title="Type `Uri`",
        description="System to have its version fixed",
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    version: fhirtypes.String = Field(
        ...,
        alias="version",
        title="Type `String`",
        description="Specific version of the code system referred to",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )
