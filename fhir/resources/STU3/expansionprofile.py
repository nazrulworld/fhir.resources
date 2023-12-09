# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExpansionProfile
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class ExpansionProfile(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defines behaviour and contraints on the ValueSet Expansion operation.
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    resource_type = Field("ExpansionProfile", const=True)

    activeOnly: bool = Field(
        None,
        alias="activeOnly",
        title="Include or exclude inactive concepts in the expansion",
        description=(
            "Controls whether inactive concepts are included or excluded in value "
            "set expansions."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    activeOnly__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_activeOnly", title="Extension field for ``activeOnly``."
    )

    contact: typing.List[fhirtypes.ContactDetailType] = Field(
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
            "The date  (and optionally time) when the expansion profile was "
            "published. The date must change if and when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the expansion profile "
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
        title="Natural language description of the expansion profile",
        description=(
            "A free text natural language description of the expansion profile from"
            " a consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    designation: fhirtypes.ExpansionProfileDesignationType = Field(
        None,
        alias="designation",
        title="When the expansion profile imposes designation contraints",
        description=(
            "A set of criteria that provide the constraints imposed on the value "
            "set expansion by including or excluding designations."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    displayLanguage: fhirtypes.Code = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    displayLanguage__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_displayLanguage", title="Extension field for ``displayLanguage``."
    )

    excludeNested: bool = Field(
        None,
        alias="excludeNested",
        title="Nested codes in the expansion or not",
        description=(
            "Controls whether or not the value set expansion nests codes or not "
            "(i.e. ValueSet.expansion.contains.contains)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    excludeNested__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_excludeNested", title="Extension field for ``excludeNested``."
    )

    excludeNotForUI: bool = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    excludeNotForUI__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_excludeNotForUI", title="Extension field for ``excludeNotForUI``."
    )

    excludePostCoordinated: bool = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    excludePostCoordinated__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_excludePostCoordinated",
        title="Extension field for ``excludePostCoordinated``.",
    )

    excludedSystem: fhirtypes.ExpansionProfileExcludedSystemType = Field(
        None,
        alias="excludedSystem",
        title="Systems/Versions to be exclude",
        description=(
            "Code system, or a particular version of a code system to be excluded "
            "from value set expansions."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this expansion profile is authored "
            "for testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fixedVersion: typing.List[fhirtypes.ExpansionProfileFixedVersionType] = Field(
        None,
        alias="fixedVersion",
        title="Fix use of a code system to a particular version",
        description="Fix use of a particular code system to a particular version.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Additional identifier for the expansion profile",
        description=(
            "A formal identifier that is used to identify this expansion profile "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    includeDefinition: bool = Field(
        None,
        alias="includeDefinition",
        title="Include or exclude the value set definition in the expansion",
        description=(
            "Controls whether the value set definition is included or excluded in "
            "value set expansions."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    includeDefinition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_includeDefinition",
        title="Extension field for ``includeDefinition``.",
    )

    includeDesignations: bool = Field(
        None,
        alias="includeDesignations",
        title="Whether the expansion should include concept designations",
        description=(
            "Controls whether concept designations are to be included or excluded "
            "in value set expansions."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    includeDesignations__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_includeDesignations",
        title="Extension field for ``includeDesignations``.",
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for expansion profile (if applicable)",
        description=(
            "A legal or geographic region in which the expansion profile is "
            "intended to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    limitedExpansion: bool = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    limitedExpansion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_limitedExpansion",
        title="Extension field for ``limitedExpansion``.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this expansion profile (computer friendly)",
        description=(
            "A natural language name identifying the expansion profile. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the "
            "expansion profile."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this expansion profile. Enables tracking the life-cycle "
            "of the content."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
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
        # if property is element of this resource.
        element_property=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching for appropriate expansion profile instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1840(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ExpansionProfileDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
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
        title="Designations to be excluded",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    include: fhirtypes.ExpansionProfileDesignationIncludeType = Field(
        None,
        alias="include",
        title="Designations to be included",
        description=None,
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExpansionProfileDesignationExclude", const=True)

    designation: typing.List[
        fhirtypes.ExpansionProfileDesignationExcludeDesignationType
    ] = Field(
        None,
        alias="designation",
        title="The designation to be excluded",
        description="A data group for each designation to be excluded.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExpansionProfileDesignationExcludeDesignation", const=True)

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Human language of the designation to be excluded",
        description="The language this designation is defined for.",
        # if property is element of this resource.
        element_property=True,
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    use: fhirtypes.CodingType = Field(
        None,
        alias="use",
        title="What kind of Designation to exclude",
        description="Which kinds of designation to exclude from the expansion.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExpansionProfileDesignationInclude", const=True)

    designation: typing.List[
        fhirtypes.ExpansionProfileDesignationIncludeDesignationType
    ] = Field(
        None,
        alias="designation",
        title="The designation to be included",
        description="A data group for each designation to be included.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExpansionProfileDesignationIncludeDesignation", const=True)

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Human language of the designation to be included",
        description="The language this designation is defined for.",
        # if property is element of this resource.
        element_property=True,
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    use: fhirtypes.CodingType = Field(
        None,
        alias="use",
        title="What kind of Designation to include",
        description="Which kinds of designation to include in the expansion.",
        # if property is element of this resource.
        element_property=True,
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

    resource_type = Field("ExpansionProfileExcludedSystem", const=True)

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="The specific code system to be excluded",
        description="An absolute URI which is the code system to be excluded.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Specific version of the code system referred to",
        description=(
            "The version of the code system from which codes in the expansion "
            "should be excluded."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExpansionProfileExcludedSystem`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "system", "version"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3307(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("system", "system__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ExpansionProfileFixedVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Fix use of a code system to a particular version.
    Fix use of a particular code system to a particular version.
    """

    resource_type = Field("ExpansionProfileFixedVersion", const=True)

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="default | check | override",
        description=(
            "How to manage the intersection between a fixed version in a value set,"
            " and this fixed version of the system in the expansion profile."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["default", "check", "override"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="System to have its version fixed",
        description="The specific system for which to fix the version.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Specific version of the code system referred to",
        description=(
            "The version of the code system from which codes in the expansion "
            "should be included."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ExpansionProfileFixedVersion`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "system", "version", "mode"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3087(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
