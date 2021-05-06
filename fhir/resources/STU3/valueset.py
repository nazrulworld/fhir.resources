# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class ValueSet(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of codes drawn from one or more code systems.
    A value set specifies a set of codes drawn from one or more code systems.
    """

    resource_type = Field("ValueSet", const=True)

    compose: fhirtypes.ValueSetComposeType = Field(
        None,
        alias="compose",
        title="Definition of the content of the value set (CLD)",
        description=(
            "A set of criteria that define the content logical definition of the "
            "value set by including or excluding codes from outside this value set."
            ' This I also known as the "Content Logical Definition" (CLD).'
        ),
        # if property is element of this resource.
        element_property=True,
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

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the value set and/or its contents. "
            "Copyright statements are generally legal restrictions on the use and "
            "publishing of the value set."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the value set was published. The "
            "date must change if and when the business version changes and it must "
            "change if the status code changes. In addition, it should change when "
            "the substantive content of the value set changes. (e.g. the 'content "
            "logical definition')."
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
        title="Natural language description of the value set",
        description=(
            "A free text natural language description of the value set from a "
            "consumer's perspective."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expansion: fhirtypes.ValueSetExpansionType = Field(
        None,
        alias="expansion",
        title='Used when the value set is "expanded"',
        description=(
            'A value set can also be "expanded", where the value set is turned into'
            " a simple collection of enumerated codes. This element holds the "
            "expansion, if it has been performed."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this value set is authored for "
            "testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    extensible: bool = Field(
        None,
        alias="extensible",
        title="Whether this is intended to be used with an extensible binding",
        description="Whether this is intended to be used with an extensible binding or not.",
        # if property is element of this resource.
        element_property=True,
    )
    extensible__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_extensible", title="Extension field for ``extensible``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the value set",
        description=(
            "A formal identifier that is used to identify this value set when it is"
            " represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    immutable: bool = Field(
        None,
        alias="immutable",
        title=(
            "Indicates whether or not any change to the content logical definition "
            "may occur"
        ),
        description=(
            "If this is set to 'true', then no new versions of the content logical "
            "definition can be created.  Note: Other metadata might still change."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    immutable__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_immutable", title="Extension field for ``immutable``."
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for value set (if applicable)",
        description=(
            "A legal or geographic region in which the value set is intended to be "
            "used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this value set (computer friendly)",
        description=(
            "A natural language name identifying the value set. This name should be"
            " usable as an identifier for the module by machine processing "
            "applications such as code generation."
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
            "The name of the individual or organization that published the value "
            "set."
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
        title="Why this value set is defined",
        description=(
            "Explaination of why this value set is needed and why it has been "
            "designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this value set. Enables tracking the life-cycle of the "
            "content."
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

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this value set (human friendly)",
        description="A short, descriptive, user-friendly title for the value set.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Logical URI to reference this value set (globally unique)",
        description=(
            "An absolute URI that is used to identify this value set when it is "
            "referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this value set is (or will be) published. The URL SHOULD "
            "include the major version of the value set. For more information see "
            "[Technical and Business Versions](resource.html#versions)."
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
            "indexing and searching for appropriate value set instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the value set",
        description=(
            "The identifier that is used to identify this version of the value set "
            "when it is referenced in a specification, model, design or instance. "
            "This is an arbitrary value managed by the value set author and is not "
            "expected to be globally unique. For example, it might be a timestamp "
            "(e.g. yyyymmdd) if a managed version is not available. There is also "
            "no expectation that versions can be placed in a lexicographical "
            "sequence."
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
        ``ValueSet`` according specification,
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
            "title",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "immutable",
            "purpose",
            "copyright",
            "extensible",
            "compose",
            "expansion",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1011(
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


class ValueSetCompose(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of the content of the value set (CLD).
    A set of criteria that define the content logical definition of the value
    set by including or excluding codes from outside this value set. This I
    also known as the "Content Logical Definition" (CLD).
    """

    resource_type = Field("ValueSetCompose", const=True)

    exclude: typing.List[fhirtypes.ValueSetComposeIncludeType] = Field(
        None,
        alias="exclude",
        title="Explicitly exclude codes from a code system or other value sets",
        description=(
            "Exclude one or more codes from the value set based on code system "
            "filters and/or other value sets."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    inactive: bool = Field(
        None,
        alias="inactive",
        title="Whether inactive codes are in the value set",
        description=(
            "Whether inactive codes - codes that are not approved for current use -"
            " are in the value set. If inactive = true, inactive codes are to be "
            "included in the expansion, if inactive = false, the inactive codes "
            "will not be included in the expansion. If absent, the behavior is "
            "determined by the implementation, or by the applicable "
            "ExpansionProfile (but generally, inactive codes would be expected to "
            "be included)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    inactive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_inactive", title="Extension field for ``inactive``."
    )

    include: typing.List[fhirtypes.ValueSetComposeIncludeType] = Field(
        ...,
        alias="include",
        title="Include one or more codes from a code system or other value set(s)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    lockedDate: fhirtypes.Date = Field(
        None,
        alias="lockedDate",
        title="Fixed date for version-less references (transitive)",
        description=(
            "If a locked date is defined, then the Content Logical Definition must "
            "be evaluated using the current version as of the locked date for "
            "referenced code system(s) and value set instances where "
            "ValueSet.compose.include.version is not defined."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lockedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lockedDate", title="Extension field for ``lockedDate``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetCompose`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "lockedDate",
            "inactive",
            "include",
            "exclude",
        ]


class ValueSetComposeInclude(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Include one or more codes from a code system or other value set(s).
    """

    resource_type = Field("ValueSetComposeInclude", const=True)

    concept: typing.List[fhirtypes.ValueSetComposeIncludeConceptType] = Field(
        None,
        alias="concept",
        title="A concept defined in the system",
        description="Specifies a concept to be included or excluded.",
        # if property is element of this resource.
        element_property=True,
    )

    filter: typing.List[fhirtypes.ValueSetComposeIncludeFilterType] = Field(
        None,
        alias="filter",
        title="Select codes/concepts by their properties (including relationships)",
        description=(
            "Select concepts by specify a matching criteria based on the properties"
            " (including relationships) defined by the system. If multiple filters "
            "are specified, they SHALL all be true."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="The system the codes come from",
        description=(
            "An absolute URI which is the code system from which the selected codes"
            " come from."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    valueSet: typing.List[fhirtypes.Uri] = Field(
        None,
        alias="valueSet",
        title="Select only contents included in this value set",
        description=(
            "Selects concepts found in this value set. This is an absolute URI that"
            " is a reference to ValueSet.url."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    valueSet__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_valueSet", title="Extension field for ``valueSet``.")

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Specific version of the code system referred to",
        description="The version of the code system that the codes are selected from.",
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetComposeInclude`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "system",
            "version",
            "concept",
            "filter",
            "valueSet",
        ]


class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A concept defined in the system.
    Specifies a concept to be included or excluded.
    """

    resource_type = Field("ValueSetComposeIncludeConcept", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Code or expression from system",
        description="Specifies a code for the concept to be included or excluded.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    designation: typing.List[
        fhirtypes.ValueSetComposeIncludeConceptDesignationType
    ] = Field(
        None,
        alias="designation",
        title="Additional representations for this concept",
        description=(
            "Additional representations for this concept when used in this value "
            "set - other languages, aliases, specialized purposes, used for "
            "particular purposes, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Text to display for this code for this value set in this valueset",
        description=(
            "The text to display to the user for this concept in the context of "
            "this valueset. If no display is provided, then applications using the "
            "value set use the display specified for the code by the system."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetComposeIncludeConcept`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "display",
            "designation",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3161(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
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


class ValueSetComposeIncludeConceptDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional representations for this concept.
    Additional representations for this concept when used in this value set -
    other languages, aliases, specialized purposes, used for particular
    purposes, etc.
    """

    resource_type = Field("ValueSetComposeIncludeConceptDesignation", const=True)

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Human language of the designation",
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
        title="Details how this designation would be used",
        description="A code that details how this designation would be used.",
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The text value for this designation",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetComposeIncludeConceptDesignation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "use", "value"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4296(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("value", "value__ext")]
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


class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Select codes/concepts by their properties (including relationships).
    Select concepts by specify a matching criteria based on the properties
    (including relationships) defined by the system. If multiple filters are
    specified, they SHALL all be true.
    """

    resource_type = Field("ValueSetComposeIncludeFilter", const=True)

    op: fhirtypes.Code = Field(
        None,
        alias="op",
        title=(
            "= | is-a | descendent-of | is-not-a | regex | in | not-in | "
            "generalizes | exists"
        ),
        description="The kind of operation to perform as a part of the filter criteria.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "=",
            "is-a",
            "descendent-of",
            "is-not-a",
            "regex",
            "in",
            "not-in",
            "generalizes",
            "exists",
        ],
    )
    op__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_op", title="Extension field for ``op``."
    )

    property: fhirtypes.Code = Field(
        None,
        alias="property",
        title="A property defined by the code system",
        description="A code that identifies a property defined in the code system.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    property__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_property", title="Extension field for ``property``."
    )

    value: fhirtypes.Code = Field(
        None,
        alias="value",
        title="Code from the system, or regex criteria, or boolean value for exists",
        description=(
            "The match value may be either a code defined by the system, or a "
            "string value, which is a regex match on the literal string of the "
            "property value when the operation is 'regex', or one of the values "
            "(true and false), when the operation is 'exists'."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetComposeIncludeFilter`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "property", "op", "value"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3057(
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
            ("op", "op__ext"),
            ("property", "property__ext"),
            ("value", "value__ext"),
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


class ValueSetExpansion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Used when the value set is "expanded".
    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """

    resource_type = Field("ValueSetExpansion", const=True)

    contains: typing.List[fhirtypes.ValueSetExpansionContainsType] = Field(
        None,
        alias="contains",
        title="Codes in the value set",
        description="The codes that are contained in the value set expansion.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: fhirtypes.Uri = Field(
        None,
        alias="identifier",
        title="Uniquely identifies this expansion",
        description=(
            "An identifier that uniquely identifies this expansion of the valueset."
            " Systems may re-use the same identifier as long as the expansion and "
            "the definition remain the same, but are not required to do so."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    identifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_identifier", title="Extension field for ``identifier``."
    )

    offset: fhirtypes.Integer = Field(
        None,
        alias="offset",
        title="Offset at which this resource starts",
        description=(
            "If paging is being used, the offset at which this resource starts.  "
            "I.e. this resource is a partial view into the expansion. If paging is "
            "not being used, this element SHALL not be present."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    offset__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_offset", title="Extension field for ``offset``."
    )

    parameter: typing.List[fhirtypes.ValueSetExpansionParameterType] = Field(
        None,
        alias="parameter",
        title="Parameter that controlled the expansion process",
        description=(
            "A parameter that controlled the expansion process. These parameters "
            "may be used by users of expanded value sets to check whether the "
            "expansion is suitable for a particular purpose, or to pick the correct"
            " expansion."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    timestamp: fhirtypes.DateTime = Field(
        None,
        alias="timestamp",
        title="Time ValueSet expansion happened",
        description="The time at which the expansion was produced by the expanding system.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    timestamp__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timestamp", title="Extension field for ``timestamp``."
    )

    total: fhirtypes.Integer = Field(
        None,
        alias="total",
        title="Total number of codes in the expansion",
        description=(
            "The total number of concepts in the expansion. If the number of "
            "concept nodes in this resource is less than the stated number, then "
            "the server can return more using the offset parameter."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    total__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_total", title="Extension field for ``total``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetExpansion`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "timestamp",
            "total",
            "offset",
            "parameter",
            "contains",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1954(
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
            ("identifier", "identifier__ext"),
            ("timestamp", "timestamp__ext"),
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


class ValueSetExpansionContains(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Codes in the value set.
    The codes that are contained in the value set expansion.
    """

    resource_type = Field("ValueSetExpansionContains", const=True)

    abstract: bool = Field(
        None,
        alias="abstract",
        title="If user cannot select this entry",
        description=(
            "If true, this entry is included in the expansion for navigational "
            "purposes, and the user cannot select the code directly as a proper "
            "value."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    abstract__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_abstract", title="Extension field for ``abstract``."
    )

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Code - if blank, this is not a selectable code",
        description=(
            "The code for this item in the expansion hierarchy. If this code is "
            "missing the entry in the hierarchy is a place holder (abstract) and "
            "does not represent a valid code in the value set."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    contains: typing.List[fhirtypes.ValueSetExpansionContainsType] = Field(
        None,
        alias="contains",
        title="Codes contained under this entry",
        description="Other codes and entries contained under this entry in the hierarchy.",
        # if property is element of this resource.
        element_property=True,
    )

    designation: typing.List[
        fhirtypes.ValueSetComposeIncludeConceptDesignationType
    ] = Field(
        None,
        alias="designation",
        title="Additional representations for this item",
        description=(
            "Additional representations for this item - other languages, aliases, "
            "specialized purposes, used for particular purposes, etc. These are "
            "relevant when the conditions of the expansion do not fix to a single "
            "correct representation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="User display for the concept",
        description="The recommended display for this item in the expansion.",
        # if property is element of this resource.
        element_property=True,
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    inactive: bool = Field(
        None,
        alias="inactive",
        title="If concept is inactive in the code system",
        description=(
            "If the concept is inactive in the code system that defines it. "
            "Inactive codes are those that are no longer to be used, but are "
            "maintained by the code system for understanding legacy data."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    inactive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_inactive", title="Extension field for ``inactive``."
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="System value for the code",
        description=(
            "An absolute URI which is the code system in which the code for this "
            "item in the expansion is defined."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Version in which this code/display is defined",
        description=(
            "The version of this code system that defined this code and/or display."
            " This should only be used with code systems that do not enforce "
            "concept permanence."
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
        ``ValueSetExpansionContains`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "system",
            "abstract",
            "inactive",
            "version",
            "code",
            "display",
            "designation",
            "contains",
        ]


class ValueSetExpansionParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Parameter that controlled the expansion process.
    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """

    resource_type = Field("ValueSetExpansionParameter", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name as assigned by the server",
        description="The name of the parameter.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Value of the named parameter",
        description="The value of the parameter.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Value of the named parameter",
        description="The value of the parameter.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Value of the named parameter",
        description="The value of the parameter.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Value of the named parameter",
        description="The value of the parameter.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Value of the named parameter",
        description="The value of the parameter.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueUri: fhirtypes.Uri = Field(
        None,
        alias="valueUri",
        title="Value of the named parameter",
        description="The value of the parameter.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ValueSetExpansionParameter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "valueString",
            "valueBoolean",
            "valueInteger",
            "valueDecimal",
            "valueUri",
            "valueCode",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2887(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2887(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "value": [
                "valueBoolean",
                "valueCode",
                "valueDecimal",
                "valueInteger",
                "valueString",
                "valueUri",
            ]
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
