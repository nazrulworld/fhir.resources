from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/SearchParameter
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SearchParameter(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Search parameter for a resource.
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """

    __resource_type__ = "SearchParameter"

    base: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="base",
        title="The resource type(s) this search parameter applies to",
        description=(
            "The base resource type(s) that this search parameter can be used "
            "against."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    base__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_base", title="Extension field for ``base``."
    )

    chain: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )
    chain__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_chain", title="Extension field for ``chain``."
    )

    code: fhirtypes.CodeType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    comparator: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="comparator",
        title="eq | ne | gt | lt | ge | le | sa | eb | ap",
        description="Comparators supported for the search parameter.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["eq", "ne", "gt", "lt", "ge", "le", "sa", "eb", "ap"],
        },
    )
    comparator__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_comparator", title="Extension field for ``comparator``."
    )

    component: typing.List[fhirtypes.SearchParameterComponentType] | None = Field(  # type: ignore
        None,
        alias="component",
        title="For Composite resources to define the parts",
        description="Used to define the parts of a composite search parameter.",
        json_schema_extra={
            "element_property": True,
        },
    )

    constraint: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="constraint",
        title="FHIRPath expression that constraints the usage of this SearchParamete",
        description=(
            "FHIRPath expression that defines/sets a complex constraint for when "
            "this SearchParameter is applicable."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    constraint__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_constraint", title="Extension field for ``constraint``."
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

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the search parameter and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the search parameter."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    copyrightLabel: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="copyrightLabel",
        title="Copyright holder and year(s)",
        description=(
            "A short string (<50 characters), suitable for inclusion in a page "
            "footer that identifies the copyright holder, effective period, and "
            "optionally whether rights are resctricted. (e.g. 'All rights "
            "reserved', 'Some rights reserved')."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_copyrightLabel", title="Extension field for ``copyrightLabel``."
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFrom: fhirtypes.CanonicalType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SearchParameter"],
        },
    )
    derivedFrom__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_derivedFrom", title="Extension field for ``derivedFrom``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the search parameter",
        description="And how it used.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this search parameter is authored for"
            " testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    expression: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="expression",
        title="FHIRPath expression that extracts the values",
        description=(
            "A FHIRPath expression that returns a set of elements for the search "
            "parameter."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_expression", title="Extension field for ``expression``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Additional identifier for the search parameter (business identifier)",
        description=(
            "A formal identifier that is used to identify this search parameter "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for search parameter (if applicable)",
        description=(
            "A legal or geographic region in which the search parameter is intended"
            " to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    modifier: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="modifier",
        title=(
            "missing | exact | contains | not | text | in | not-in | below | above "
            "| type | identifier | of-type | code-text | text-advanced | iterate"
        ),
        description="A modifier supported for the search parameter.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
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
        },
    )
    modifier__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_modifier", title="Extension field for ``modifier``."
    )

    multipleAnd: bool | None = Field(  # type: ignore
        None,
        alias="multipleAnd",
        title="Allow multiple parameters (and)",
        description=(
            "Whether multiple parameters are allowed - e.g. more than one parameter"
            " with the same name. The search matches if all the parameters match."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    multipleAnd__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_multipleAnd", title="Extension field for ``multipleAnd``."
    )

    multipleOr: bool | None = Field(  # type: ignore
        None,
        alias="multipleOr",
        title="Allow multiple values per parameter (or)",
        description=(
            "Whether multiple values are allowed for each time the parameter "
            "exists. Values are separated by commas, and the parameter matches if "
            "any of the values match."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    multipleOr__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_multipleOr", title="Extension field for ``multipleOr``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this search parameter (computer friendly)",
        description=(
            "A natural language name identifying the search parameter. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    processingMode: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="processingMode",
        title="normal | phonetic | other",
        description=(
            "How the search parameter relates to the set of elements returned by "
            "evaluating the expression query."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["normal", "phonetic", "other"],
        },
    )
    processingMode__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_processingMode", title="Extension field for ``processingMode``."
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual tresponsible for the "
            "release and ongoing maintenance of the search parameter."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="Why this search parameter is defined",
        description=(
            "Explanation of why this search parameter is needed and why it has been"
            " designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this search parameter. Enables tracking the life-cycle "
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

    target: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="target",
        title="Types of resource (if a resource reference)",
        description="Types of resource (if a resource is referenced).",
        json_schema_extra={
            "element_property": True,
        },
    )
    target__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_target", title="Extension field for ``target``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this search parameter (human friendly)",
        description="A short, descriptive, user-friendly title for the search parameter.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
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
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    versionAlgorithmCoding: fhirtypes.CodingType | None = Field(  # type: ignore
        None,
        alias="versionAlgorithmCoding",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )

    versionAlgorithmString: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="versionAlgorithmString",
        title="How to compare versions",
        description=(
            "Indicates the mechanism used to compare versions to determine which is"
            " more current."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e versionAlgorithm[x]
            "one_of_many": "versionAlgorithm",
            "one_of_many_required": False,
        },
    )
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
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

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
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
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields


class SearchParameterComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    For Composite resources to define the parts.
    Used to define the parts of a composite search parameter.
    """

    __resource_type__ = "SearchParameterComponent"

    definition: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="definition",
        title="Defines how the part works",
        description="The definition of the search parameter that describes this part.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SearchParameter"],
        },
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_definition", title="Extension field for ``definition``."
    )

    expression: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="expression",
        title="Subexpression relative to main expression",
        description=(
            "A sub-expression that defines how to extract values for this component"
            " from the output of the main SearchParameter.expression."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_expression", title="Extension field for ``expression``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SearchParameterComponent`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "definition", "expression"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
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
        return required_fields
