# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SearchParameter
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class SearchParameter(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Search parameter for a resource.
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """

    resource_type = Field("SearchParameter", const=True)

    base: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="base",
        title="The resource type(s) this search parameter applies to",
        description=(
            "The base resource type(s) that this search parameter can be used "
            "against."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    base__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_base", title="Extension field for ``base``.")

    chain: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="chain",
        title="Chained names supported",
        description=(
            "Contains the names of any search parameters which may be chained to "
            "the containing search parameter. Chained parameters may be added to "
            "search parameters of type reference and specify that resources will "
            "only be returned if they contain a reference to a resource which "
            "matches the chained parameter value. Values for this field should be "
            "drawn from SearchParameter.code for a parameter on the target resource"
            " type."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    chain__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_chain", title="Extension field for ``chain``.")

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Recommended name for parameter in search url",
        description=(
            "The label that is recommended to be used in the URL or the parameter "
            "name in a parameters resource for this search parameter.  In some "
            "cases, servers may need to use a different CapabilityStatement "
            "searchParam.name to differentiate between multiple SearchParameters "
            "that happen to have the same code."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    comparator: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="comparator",
        title="eq | ne | gt | lt | ge | le | sa | eb | ap",
        description="Comparators supported for the search parameter.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["eq", "ne", "gt", "lt", "ge", "le", "sa", "eb", "ap"],
    )
    comparator__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_comparator", title="Extension field for ``comparator``.")

    component: typing.List[fhirtypes.SearchParameterComponentType] = Field(
        None,
        alias="component",
        title="For Composite resources to define the parts",
        description="Used to define the parts of a composite search parameter.",
        # if property is element of this resource.
        element_property=True,
    )

    constraint: fhirtypes.String = Field(
        None,
        alias="constraint",
        title="FHIRPath expression that constraints the usage of this SearchParamete",
        description=(
            "FHIRPath expression that defines/sets a complex constraint for when "
            "this SearchParameter is applicable."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    constraint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_constraint", title="Extension field for ``constraint``."
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
            "A copyright statement relating to the search parameter and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the search parameter."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    copyrightLabel: fhirtypes.String = Field(
        None,
        alias="copyrightLabel",
        title="Copyright holder and year(s)",
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyrightLabel", title="Extension field for ``copyrightLabel``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the search parameter was last "
            "significantly changed. The date must change when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the search parameter "
            "changes."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFrom: fhirtypes.Canonical = Field(
        None,
        alias="derivedFrom",
        title="Original definition for the search parameter",
        description=(
            "Where this search parameter is originally defined. If a derivedFrom is"
            " provided, then the details in the search parameter must be consistent"
            " with the definition from which it is defined. i.e. the parameter "
            "should have the same meaning, and (usually) the functionality should "
            "be a proper subset of the underlying search parameter."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SearchParameter"],
    )
    derivedFrom__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_derivedFrom", title="Extension field for ``derivedFrom``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the search parameter",
        description="And how it used.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this search parameter is authored for"
            " testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="FHIRPath expression that extracts the values",
        description=(
            "A FHIRPath expression that returns a set of elements for the search "
            "parameter."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the search parameter (business identifier)",
        description=(
            "A formal identifier that is used to identify this search parameter "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for search parameter (if applicable)",
        description=(
            "A legal or geographic region in which the search parameter is intended"
            " to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    modifier: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="modifier",
        title=(
            "missing | exact | contains | not | text | in | not-in | below | above "
            "| type | identifier | of-type | code-text | text-advanced | iterate"
        ),
        description="A modifier supported for the search parameter.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "missing",
            "exact",
            "contains",
            "not",
            "text",
            "in",
            "not-in",
            "below",
            "above",
            "type",
            "identifier",
            "of-type",
            "code-text",
            "text-advanced",
            "iterate",
        ],
    )
    modifier__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_modifier", title="Extension field for ``modifier``.")

    multipleAnd: bool = Field(
        None,
        alias="multipleAnd",
        title="Allow multiple parameters (and)",
        description=(
            "Whether multiple parameters are allowed - e.g. more than one parameter"
            " with the same name. The search matches if all the parameters match."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    multipleAnd__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_multipleAnd", title="Extension field for ``multipleAnd``."
    )

    multipleOr: bool = Field(
        None,
        alias="multipleOr",
        title="Allow multiple values per parameter (or)",
        description=(
            "Whether multiple values are allowed for each time the parameter "
            "exists. Values are separated by commas, and the parameter matches if "
            "any of the values match."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    multipleOr__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_multipleOr", title="Extension field for ``multipleOr``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this search parameter (computer friendly)",
        description=(
            "A natural language name identifying the search parameter. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    processingMode: fhirtypes.Code = Field(
        None,
        alias="processingMode",
        title="normal | phonetic | other",
        description=(
            "How the search parameter relates to the set of elements returned by "
            "evaluating the expression query."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["normal", "phonetic", "other"],
    )
    processingMode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_processingMode", title="Extension field for ``processingMode``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual tresponsible for the "
            "release and ongoing maintenance of the search parameter."
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
        title="Why this search parameter is defined",
        description=(
            "Explanation of why this search parameter is needed and why it has been"
            " designed as it has."
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
            "The status of this search parameter. Enables tracking the life-cycle "
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

    target: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="target",
        title="Types of resource (if a resource reference)",
        description="Types of resource (if a resource is referenced).",
        # if property is element of this resource.
        element_property=True,
    )
    target__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_target", title="Extension field for ``target``.")

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this search parameter (human friendly)",
        description="A short, descriptive, user-friendly title for the search parameter.",
        # if property is element of this resource.
        element_property=True,
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title=(
            "number | date | string | token | reference | composite | quantity | "
            "uri | special"
        ),
        description=(
            "The type of value that a search parameter may contain, and how the "
            "content is interpreted."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "number",
            "date",
            "string",
            "token",
            "reference",
            "composite",
            "quantity",
            "uri",
            "special",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this search parameter, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this search parameter when it"
            " is referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which an authoritative instance of this"
            " search parameter is (or will be) published. This URL can be the "
            "target of a canonical reference. It SHALL remain the same when the "
            "search parameter is stored on different servers."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate search parameter instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the search parameter",
        description=(
            "The identifier that is used to identify this version of the search "
            "parameter when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the search parameter "
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

    versionAlgorithmCoding: fhirtypes.CodingType = Field(
        None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )

    versionAlgorithmString: fhirtypes.String = Field(
        None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e versionAlgorithm[x]
        one_of_many="versionAlgorithm",
        one_of_many_required=False,
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_versionAlgorithmString",
        title="Extension field for ``versionAlgorithmString``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SearchParameter`` according specification,
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
            "versionAlgorithmString",
            "versionAlgorithmCoding",
            "name",
            "title",
            "derivedFrom",
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
            "copyrightLabel",
            "code",
            "base",
            "type",
            "expression",
            "processingMode",
            "constraint",
            "target",
            "multipleOr",
            "multipleAnd",
            "comparator",
            "modifier",
            "chain",
            "component",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1724(
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
            ("base", "base__ext"),
            ("code", "code__ext"),
            ("description", "description__ext"),
            ("name", "name__ext"),
            ("status", "status__ext"),
            ("type", "type__ext"),
            ("url", "url__ext"),
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1724(
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
            "versionAlgorithm": ["versionAlgorithmCoding", "versionAlgorithmString"]
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


class SearchParameterComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    For Composite resources to define the parts.
    Used to define the parts of a composite search parameter.
    """

    resource_type = Field("SearchParameterComponent", const=True)

    definition: fhirtypes.Canonical = Field(
        None,
        alias="definition",
        title="Defines how the part works",
        description="The definition of the search parameter that describes this part.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SearchParameter"],
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Subexpression relative to main expression",
        description=(
            "A sub-expression that defines how to extract values for this component"
            " from the output of the main SearchParameter.expression."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SearchParameterComponent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "definition", "expression"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2673(
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
            ("definition", "definition__ext"),
            ("expression", "expression__ext"),
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
