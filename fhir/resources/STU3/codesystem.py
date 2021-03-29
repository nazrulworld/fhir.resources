# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
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


class CodeSystem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of codes drawn from one or more code systems.
    A code system resource specifies a set of codes drawn from one or more code
    systems.
    """

    resource_type = Field("CodeSystem", const=True)

    caseSensitive: bool = Field(
        None,
        alias="caseSensitive",
        title="If code comparison is case sensitive",
        description=(
            "If code comparison is case sensitive when codes within this system are"
            " compared to each other."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    caseSensitive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_caseSensitive", title="Extension field for ``caseSensitive``."
    )

    compositional: bool = Field(
        None,
        alias="compositional",
        title="If code system defines a post-composition grammar",
        description="True If code system defines a post-composition grammar.",
        # if property is element of this resource.
        element_property=True,
    )
    compositional__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_compositional", title="Extension field for ``compositional``."
    )

    concept: typing.List[fhirtypes.CodeSystemConceptType] = Field(
        None,
        alias="concept",
        title="Concepts in the code system",
        description=(
            "Concepts that are in the code system. The concept definitions are "
            "inherently hierarchical, but the definitions must be consulted to "
            "determine what the meaning of the hierarchical relationships are."
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

    content: fhirtypes.Code = Field(
        None,
        alias="content",
        title="not-present | example | fragment | complete",
        description=(
            "How much of the content of the code system - the concepts and codes it"
            " defines - are represented in this resource."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["not-present", "example", "fragment", "complete"],
    )
    content__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_content", title="Extension field for ``content``."
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the code system and/or its contents."
            " Copyright statements are generally legal restrictions on the use and "
            "publishing of the code system."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    count: fhirtypes.UnsignedInt = Field(
        None,
        alias="count",
        title="Total concepts in the code system",
        description=(
            "The total number of concepts defined by the code system. Where the "
            "code system has a compositional grammar, the count refers to the "
            "number of base (primitive) concepts."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_count", title="Extension field for ``count``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the code system was published. "
            "The date must change if and when the business version changes and it "
            "must change if the status code changes. In addition, it should change "
            "when the substantive content of the code system changes."
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
        title="Natural language description of the code system",
        description=(
            "A free text natural language description of the code system from a "
            "consumer's perspective."
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
            "A boolean value to indicate that this code system is authored for "
            "testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    filter: typing.List[fhirtypes.CodeSystemFilterType] = Field(
        None,
        alias="filter",
        title="Filter that can be used in a value set",
        description=(
            "A filter that can be used in a value set compose statement when "
            "selecting concepts using a filter."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    hierarchyMeaning: fhirtypes.Code = Field(
        None,
        alias="hierarchyMeaning",
        title="grouped-by | is-a | part-of | classified-with",
        description="The meaning of the hierarchy of concepts.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["grouped-by", "is-a", "part-of", "classified-with"],
    )
    hierarchyMeaning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_hierarchyMeaning",
        title="Extension field for ``hierarchyMeaning``.",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Additional identifier for the code system",
        description=(
            "A formal identifier that is used to identify this code system when it "
            "is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for code system (if applicable)",
        description=(
            "A legal or geographic region in which the code system is intended to "
            "be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this code system (computer friendly)",
        description=(
            "A natural language name identifying the code system. This name should "
            "be usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    property: typing.List[fhirtypes.CodeSystemPropertyType] = Field(
        None,
        alias="property",
        title="Additional information supplied about each concept",
        description=(
            "A property defines an additional slot through which additional "
            "information can be provided about a concept."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the code "
            "system."
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
        title="Why this code system is defined",
        description=(
            "Explaination of why this code system is needed and why it has been "
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
            "The status of this code system. Enables tracking the life-cycle of the"
            " content."
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
        title="Name for this code system (human friendly)",
        description="A short, descriptive, user-friendly title for the code system.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Logical URI to reference this code system (globally unique) "
            "(Coding.system)"
        ),
        description=(
            "An absolute URI that is used to identify this code system when it is "
            "referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this code system is (or will be) published. The URL SHOULD "
            "include the major version of the code system. For more information see"
            " [Technical and Business Versions](resource.html#versions). This is "
            "used in [Coding]{datatypes.html#Coding}.system."
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
            "indexing and searching for appropriate code system instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueSet: fhirtypes.Uri = Field(
        None,
        alias="valueSet",
        title="Canonical URL for value set with entire code system",
        description="Canonical URL of value set that contains the entire code system.",
        # if property is element of this resource.
        element_property=True,
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the code system (Coding.version)",
        description=(
            "The identifier that is used to identify this version of the code "
            "system when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the code system author"
            " and is not expected to be globally unique. For example, it might be a"
            " timestamp (e.g. yyyymmdd) if a managed version is not available. "
            "There is also no expectation that versions can be placed in a "
            "lexicographical sequence. This is used in "
            "[Coding]{datatypes.html#Coding}.version."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    versionNeeded: bool = Field(
        None,
        alias="versionNeeded",
        title="If definitions are not stable",
        description=(
            "This flag is used to signify that the code system has not (or does "
            "not) maintain the definitions, and a version must be specified when "
            "referencing this code system."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    versionNeeded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_versionNeeded", title="Extension field for ``versionNeeded``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CodeSystem`` according specification,
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
            "purpose",
            "copyright",
            "caseSensitive",
            "valueSet",
            "hierarchyMeaning",
            "compositional",
            "versionNeeded",
            "content",
            "count",
            "filter",
            "property",
            "concept",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1200(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("content", "content__ext"), ("status", "status__ext")]
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


class CodeSystemConcept(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Concepts in the code system.
    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meaning of the hierarchical relationships are.
    """

    resource_type = Field("CodeSystemConcept", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Code that identifies concept",
        description=(
            "A code - a text symbol - that uniquely identifies the concept within "
            "the code system."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    concept: typing.List[fhirtypes.CodeSystemConceptType] = Field(
        None,
        alias="concept",
        title="Child Concepts (is-a/contains/categorizes)",
        description=(
            "Defines children of a concept to produce a hierarchy of concepts. The "
            "nature of the relationships is variable (is-a/contains/categorizes) - "
            "see hierarchyMeaning."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    definition: fhirtypes.String = Field(
        None,
        alias="definition",
        title="Formal definition",
        description=(
            "The formal definition of the concept. The code system resource does "
            "not make formal definitions required, because of the prevalence of "
            "legacy systems. However, they are highly recommended, as without them "
            "there is no formal meaning associated with the concept."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    designation: typing.List[fhirtypes.CodeSystemConceptDesignationType] = Field(
        None,
        alias="designation",
        title="Additional representations for the concept",
        description=(
            "Additional representations for the concept - other languages, aliases,"
            " specialized purposes, used for particular purposes, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Text to display to the user",
        description=(
            "A human readable string that is the recommended default way to present"
            " this concept to a user."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    property: typing.List[fhirtypes.CodeSystemConceptPropertyType] = Field(
        None,
        alias="property",
        title="Property value for the concept",
        description="A property value for this concept.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CodeSystemConcept`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "display",
            "definition",
            "designation",
            "property",
            "concept",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1923(
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


class CodeSystemConceptDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional representations for the concept.
    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """

    resource_type = Field("CodeSystemConceptDesignation", const=True)

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
        ``CodeSystemConceptDesignation`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "use", "value"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3058(
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


class CodeSystemConceptProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Property value for the concept.
    A property value for this concept.
    """

    resource_type = Field("CodeSystemConceptProperty", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Reference to CodeSystem.property.code",
        description="A code that is a reference to CodeSystem.property.code.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Value of the property for this concept",
        description="The value of this property.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Value of the property for this concept",
        description="The value of this property.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Value of the property for this concept",
        description="The value of this property.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Value of the property for this concept",
        description="The value of this property.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Value of the property for this concept",
        description="The value of this property.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Value of the property for this concept",
        description="The value of this property.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CodeSystemConceptProperty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "valueCode",
            "valueCoding",
            "valueString",
            "valueInteger",
            "valueBoolean",
            "valueDateTime",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2797(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2797(
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
                "valueCoding",
                "valueDateTime",
                "valueInteger",
                "valueString",
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


class CodeSystemFilter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Filter that can be used in a value set.
    A filter that can be used in a value set compose statement when selecting
    concepts using a filter.
    """

    resource_type = Field("CodeSystemFilter", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Code that identifies the filter",
        description="The code that identifies this filter when it is used in the instance.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="How or why the filter is used",
        description="A description of how or why the filter is used.",
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    operator: typing.List[fhirtypes.Code] = Field(
        None,
        alias="operator",
        title="Operators that can be used with filter",
        description="A list of operators that can be used with the filter.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    operator__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_operator", title="Extension field for ``operator``.")

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="What to use for the value",
        description="A description of what the value for the filter should be.",
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
        ``CodeSystemFilter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "description",
            "operator",
            "value",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1819(
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
            ("code", "code__ext"),
            ("operator", "operator__ext"),
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


class CodeSystemProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional information supplied about each concept.
    A property defines an additional slot through which additional information
    can be provided about a concept.
    """

    resource_type = Field("CodeSystemProperty", const=True)

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title=(
            "Identifies the property on the concepts, and when referred to in "
            "operations"
        ),
        description=(
            "A code that is used to identify the property. The code is used "
            "internally (in CodeSystem.concept.property.code) and also externally, "
            "such as in property filters."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Why the property is defined, and/or what it conveys",
        description=(
            "A description of the property- why it is defined, and how its value "
            "might be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="code | Coding | string | integer | boolean | dateTime",
        description=(
            'The type of the property value. Properties of type "code" contain a '
            "code defined by the code system (e.g. a reference to anotherr defined "
            "concept)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["code", "Coding", "string", "integer", "boolean", "dateTime"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Formal identifier for the property",
        description=(
            "Reference to the formal meaning of the property. One possible source "
            "of meaning is the [Concept Properties](codesystem-concept-"
            "properties.html) code system."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CodeSystemProperty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "uri",
            "description",
            "type",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2081(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext"), ("type", "type__ext")]
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
