from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ExpansionProfile
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ExpansionProfile(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines behaviour and contraints on the ValueSet Expansion operation.
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    __resource_type__ = "ExpansionProfile"

    activeOnly: bool | None = Field(  # type: ignore
        None,
        alias="activeOnly",
        title="Include or exclude inactive concepts in the expansion",
        description=(
            "Controls whether inactive concepts are included or excluded in value "
            "set expansions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    activeOnly__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_activeOnly", title="Extension field for ``activeOnly``."
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the expansion profile was "
            "published. The date must change if and when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the expansion profile "
            "changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the expansion profile",
        description=(
            "A free text natural language description of the expansion profile from"
            " a consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    designation: fhirtypes.ExpansionProfileDesignationType | None = Field(  # type: ignore
        None,
        alias="designation",
        title="When the expansion profile imposes designation contraints",
        description=(
            "A set of criteria that provide the constraints imposed on the value "
            "set expansion by including or excluding designations."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    displayLanguage: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="displayLanguage",
        title=(
            "Specify the language for the display element of codes in the value set"
            " expansion"
        ),
        description=(
            "Specifies the language to be used for description in the expansions "
            "i.e. the language to be used for ValueSet.expansion.contains.display."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    displayLanguage__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_displayLanguage", title="Extension field for ``displayLanguage``."
    )

    excludeNested: bool | None = Field(  # type: ignore
        None,
        alias="excludeNested",
        title="Nested codes in the expansion or not",
        description=(
            "Controls whether or not the value set expansion nests codes or not "
            "(i.e. ValueSet.expansion.contains.contains)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    excludeNested__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_excludeNested", title="Extension field for ``excludeNested``."
    )

    excludeNotForUI: bool | None = Field(  # type: ignore
        None,
        alias="excludeNotForUI",
        title=(
            "Include or exclude codes which cannot be rendered in user interfaces "
            "in the value set expansion"
        ),
        description=(
            "Controls whether or not the value set expansion includes codes which "
            "cannot be displayed in user interfaces."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    excludeNotForUI__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_excludeNotForUI", title="Extension field for ``excludeNotForUI``."
    )

    excludePostCoordinated: bool | None = Field(  # type: ignore
        None,
        alias="excludePostCoordinated",
        title=(
            "Include or exclude codes which are post coordinated expressions in the"
            " value set expansion"
        ),
        description=(
            "Controls whether or not the value set expansion includes post "
            "coordinated codes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    excludePostCoordinated__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_excludePostCoordinated",
        title="Extension field for ``excludePostCoordinated``.",
    )

    excludedSystem: fhirtypes.ExpansionProfileExcludedSystemType | None = Field(  # type: ignore
        None,
        alias="excludedSystem",
        title="Systems/Versions to be exclude",
        description=(
            "Code system, or a particular version of a code system to be excluded "
            "from value set expansions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this expansion profile is authored "
            "for testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fixedVersion: typing.List[fhirtypes.ExpansionProfileFixedVersionType] | None = Field(  # type: ignore
        None,
        alias="fixedVersion",
        title="Fix use of a code system to a particular version",
        description="Fix use of a particular code system to a particular version.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the expansion profile",
        description=(
            "A formal identifier that is used to identify this expansion profile "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    includeDefinition: bool | None = Field(  # type: ignore
        None,
        alias="includeDefinition",
        title="Include or exclude the value set definition in the expansion",
        description=(
            "Controls whether the value set definition is included or excluded in "
            "value set expansions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    includeDefinition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_includeDefinition",
        title="Extension field for ``includeDefinition``.",
    )

    includeDesignations: bool | None = Field(  # type: ignore
        None,
        alias="includeDesignations",
        title="Whether the expansion should include concept designations",
        description=(
            "Controls whether concept designations are to be included or excluded "
            "in value set expansions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    includeDesignations__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_includeDesignations",
        title="Extension field for ``includeDesignations``.",
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for expansion profile (if applicable)",
        description=(
            "A legal or geographic region in which the expansion profile is "
            "intended to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    limitedExpansion: bool | None = Field(  # type: ignore
        None,
        alias="limitedExpansion",
        title=(
            "Controls behaviour of the value set expand operation when value sets "
            "are too large to be completely expanded"
        ),
        description=(
            "If the value set being expanded is incomplete (because it is too big "
            "to expand), return a limited expansion (a subset) with an indicator "
            "that expansion is incomplete, using the extension "
            "[http://hl7.org/fhir/StructureDefinition/valueset-"
            "toocostly](extension-valueset-toocostly.html)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    limitedExpansion__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_limitedExpansion",
        title="Extension field for ``limitedExpansion``.",
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this expansion profile (computer friendly)",
        description=(
            "A natural language name identifying the expansion profile. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the "
            "expansion profile."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this expansion profile. Enables tracking the life-cycle "
            "of the content."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title="Logical URI to reference this expansion profile (globally unique)",
        description=(
            "An absolute URI that is used to identify this expansion profile when "
            "it is referenced in a specification, model, design or an instance. "
            "This SHALL be a URL, SHOULD be globally unique, and SHOULD be an "
            "address at which this expansion profile is (or will be) published. The"
            " URL SHOULD include the major version of the expansion profile. For "
            "more information see [Technical and Business "
            "Versions](resource.html#versions)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        None,
        alias="useContext",
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching for appropriate expansion profile instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the expansion profile",
        description=(
            "The identifier that is used to identify this version of the expansion "
            "profile when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the expansion profile "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExpansionProfile`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "url",
            "identifier",
            "version",
            "name",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "fixedVersion",
            "excludedSystem",
            "includeDesignations",
            "designation",
            "includeDefinition",
            "activeOnly",
            "excludeNested",
            "excludeNotForUI",
            "excludePostCoordinated",
            "displayLanguage",
            "limitedExpansion",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class ExpansionProfileDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    When the expansion profile imposes designation contraints.
    A set of criteria that provide the constraints imposed on the value set
    expansion by including or excluding designations.
    """

    __resource_type__ = "ExpansionProfileDesignation"

    exclude: fhirtypes.ExpansionProfileDesignationExcludeType | None = Field(  # type: ignore
        None,
        alias="exclude",
        title="Designations to be excluded",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    include: fhirtypes.ExpansionProfileDesignationIncludeType | None = Field(  # type: ignore
        None,
        alias="include",
        title="Designations to be included",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExpansionProfileDesignation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "include", "exclude"]


class ExpansionProfileDesignationExclude(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Designations to be excluded.
    """

    __resource_type__ = "ExpansionProfileDesignationExclude"

    designation: typing.List[fhirtypes.ExpansionProfileDesignationExcludeDesignationType] | None = Field(  # type: ignore
        None,
        alias="designation",
        title="The designation to be excluded",
        description="A data group for each designation to be excluded.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExpansionProfileDesignationExclude`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "designation"]


class ExpansionProfileDesignationExcludeDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The designation to be excluded.
    A data group for each designation to be excluded.
    """

    __resource_type__ = "ExpansionProfileDesignationExcludeDesignation"

    language: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="language",
        title="Human language of the designation to be excluded",
        description="The language this designation is defined for.",
        json_schema_extra={
            "element_property": True,
        },
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_language", title="Extension field for ``language``."
    )

    use: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="use",
        title="What kind of Designation to exclude",
        description="Which kinds of designation to exclude from the expansion.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExpansionProfileDesignationExcludeDesignation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "use"]


class ExpansionProfileDesignationInclude(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Designations to be included.
    """

    __resource_type__ = "ExpansionProfileDesignationInclude"

    designation: typing.List[fhirtypes.ExpansionProfileDesignationIncludeDesignationType] | None = Field(  # type: ignore
        None,
        alias="designation",
        title="The designation to be included",
        description="A data group for each designation to be included.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExpansionProfileDesignationInclude`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "designation"]


class ExpansionProfileDesignationIncludeDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The designation to be included.
    A data group for each designation to be included.
    """

    __resource_type__ = "ExpansionProfileDesignationIncludeDesignation"

    language: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="language",
        title="Human language of the designation to be included",
        description="The language this designation is defined for.",
        json_schema_extra={
            "element_property": True,
        },
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_language", title="Extension field for ``language``."
    )

    use: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="use",
        title="What kind of Designation to include",
        description="Which kinds of designation to include in the expansion.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExpansionProfileDesignationIncludeDesignation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "use"]


class ExpansionProfileExcludedSystem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Systems/Versions to be exclude.
    Code system, or a particular version of a code system to be excluded from
    value set expansions.
    """

    __resource_type__ = "ExpansionProfileExcludedSystem"

    system: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="system",
        title="The specific code system to be excluded",
        description="An absolute URI which is the code system to be excluded.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_system", title="Extension field for ``system``."
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Specific version of the code system referred to",
        description=(
            "The version of the code system from which codes in the expansion "
            "should be excluded."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExpansionProfileExcludedSystem`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "system", "version"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("system", "system__ext")]
        return required_fields


class ExpansionProfileFixedVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Fix use of a code system to a particular version.
    Fix use of a particular code system to a particular version.
    """

    __resource_type__ = "ExpansionProfileFixedVersion"

    mode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="mode",
        title="default | check | override",
        description=(
            "How to manage the intersection between a fixed version in a value set,"
            " and this fixed version of the system in the expansion profile."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["default", "check", "override"],
        },
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_mode", title="Extension field for ``mode``."
    )

    system: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="system",
        title="System to have its version fixed",
        description="The specific system for which to fix the version.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_system", title="Extension field for ``system``."
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Specific version of the code system referred to",
        description=(
            "The version of the code system from which codes in the expansion "
            "should be included."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExpansionProfileFixedVersion`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "system", "version", "mode"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("mode", "mode__ext"),
            ("system", "system__ext"),
            ("version", "version__ext"),
        ]
        return required_fields
