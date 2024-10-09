from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class OperationDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of an operation or a named query.
    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """

    __resource_type__ = "OperationDefinition"

    affectsState: bool | None = Field(  # type: ignore
        None,
        alias="affectsState",
        title="Whether content is changed by the operation",
        description=(
            "Whether the operation affects state. Side effects such as producing "
            "audit trail entries do not count as 'affecting  state'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    affectsState__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_affectsState", title="Extension field for ``affectsState``."
    )

    base: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="base",
        title="Marks this as a profile of the base",
        description=(
            "Indicates that this operation definition is a constraining profile on "
            "the base."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["OperationDefinition"],
        },
    )
    base__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_base", title="Extension field for ``base``."
    )

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Recommended name for operation in search url",
        description=(
            "The label that is recommended to be used in the URL for this "
            "operation. In some cases, servers may need to use a different "
            "CapabilityStatement operation.name to differentiate between multiple "
            "SearchParameters that happen to have the same code."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    comment: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Additional information about use",
        description="Additional information about how to use this operation or named query.",
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
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
            "A copyright statement relating to the operation definition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the operation definition."
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
            "The date  (and optionally time) when the operation definition was last"
            " significantly changed. The date must change when the business version"
            " changes and it must change if the status code changes. In addition, "
            "it should change when the substantive content of the operation "
            "definition changes."
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
        title="Natural language description of the operation definition",
        description=(
            "A free text natural language description of the operation definition "
            "from a consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
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
            "A Boolean value to indicate that this operation definition is authored"
            " for testing purposes (or education/evaluation/marketing) and is not "
            "intended for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title=(
            "Additional identifier for the implementation guide (business "
            "identifier)"
        ),
        description=(
            "A formal identifier that is used to identify this implementation guide"
            " when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    inputProfile: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="inputProfile",
        title="Validation information for in parameters",
        description=(
            "Additional validation information for the in parameters - a single "
            "profile that covers all the parameters. The profile is a constraint on"
            " the parameters resource as a whole."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    inputProfile__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_inputProfile", title="Extension field for ``inputProfile``."
    )

    instance: bool | None = Field(  # type: ignore
        None,
        alias="instance",
        title="Invoke on an instance?",
        description=(
            "Indicates whether this operation can be invoked on a particular "
            "instance of one of the given types."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    instance__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_instance", title="Extension field for ``instance``."
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for operation definition (if applicable)",
        description=(
            "A legal or geographic region in which the operation definition is "
            "intended to be used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    kind: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="kind",
        title="operation | query",
        description="Whether this is an operation or a named query.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["operation", "query"],
        },
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_kind", title="Extension field for ``kind``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this operation definition (computer friendly)",
        description=(
            "A natural language name identifying the operation definition. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    outputProfile: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="outputProfile",
        title="Validation information for out parameters",
        description=(
            "Additional validation information for the out parameters - a single "
            "profile that covers all the parameters. The profile is a constraint on"
            " the parameters resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    outputProfile__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_outputProfile", title="Extension field for ``outputProfile``."
    )

    overload: typing.List[fhirtypes.OperationDefinitionOverloadType] | None = Field(  # type: ignore
        None,
        alias="overload",
        title="Define overloaded variants for when  generating code",
        description=(
            "Defines an appropriate combination of parameters to use when invoking "
            "this operation, to help code generators when generating overloaded "
            "parameter sets for this operation."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    parameter: typing.List[fhirtypes.OperationDefinitionParameterType] | None = Field(  # type: ignore
        None,
        alias="parameter",
        title="Parameters for the operation/query",
        description="The parameters for the operation/query.",
        json_schema_extra={
            "element_property": True,
        },
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher/steward (organization or individual)",
        description=(
            "The name of the organization or individual responsible for the release"
            " and ongoing maintenance of the operation definition."
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
        title="Why this operation definition is defined",
        description=(
            "Explanation of why this operation definition is needed and why it has "
            "been designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    resource: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="resource",
        title="Types this operation applies to",
        description="The types on which this operation can be executed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    resource__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_resource", title="Extension field for ``resource``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description="The current state of this operation definition.",
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

    system: bool | None = Field(  # type: ignore
        None,
        alias="system",
        title="Invoke at the system level?",
        description=(
            "Indicates whether this operation or named query can be invoked at the "
            "system level (e.g. without needing to choose a resource type for the "
            "context)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_system", title="Extension field for ``system``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="title",
        title="Name for this operation definition (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the operation " "definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    type: bool | None = Field(  # type: ignore
        None,
        alias="type",
        title="Invoke at the type level?",
        description=(
            "Indicates whether this operation or named query can be invoked at the "
            "resource type level for any given resource type level (e.g. without "
            "needing to choose a specific resource id for the context)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this operation definition, represented as an "
            "absolute URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this operation definition "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which an "
            "authoritative instance of this operation definition is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the operation definition is stored on "
            "different servers."
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
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate operation definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the operation definition",
        description=(
            "The identifier that is used to identify this version of the operation "
            "definition when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the operation "
            "definition author and is not expected to be globally unique. For "
            "example, it might be a timestamp (e.g. yyyymmdd) if a managed version "
            "is not available. There is also no expectation that versions can be "
            "placed in a lexicographical sequence."
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
        ``OperationDefinition`` according specification,
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
            "status",
            "kind",
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
            "affectsState",
            "code",
            "comment",
            "base",
            "resource",
            "system",
            "type",
            "instance",
            "inputProfile",
            "outputProfile",
            "parameter",
            "overload",
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
            ("code", "code__ext"),
            ("instance", "instance__ext"),
            ("kind", "kind__ext"),
            ("name", "name__ext"),
            ("status", "status__ext"),
            ("system", "system__ext"),
            ("type", "type__ext"),
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


class OperationDefinitionOverload(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Define overloaded variants for when  generating code.
    Defines an appropriate combination of parameters to use when invoking this
    operation, to help code generators when generating overloaded parameter
    sets for this operation.
    """

    __resource_type__ = "OperationDefinitionOverload"

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="comment",
        title="Comments to go on overload",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    parameterName: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="parameterName",
        title="Name of parameter to include in overload",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    parameterName__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_parameterName", title="Extension field for ``parameterName``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``OperationDefinitionOverload`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "parameterName", "comment"]


class OperationDefinitionParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Parameters for the operation/query.
    The parameters for the operation/query.
    """

    __resource_type__ = "OperationDefinitionParameter"

    allowedType: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="allowedType",
        title="Allowed sub-type this parameter can have (if type is abstract)",
        description=(
            "Support for polymorphic types. If the parameter type is abstract, this"
            " element lists allowed sub-types for the parameter."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    allowedType__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_allowedType", title="Extension field for ``allowedType``."
    )

    binding: fhirtypes.OperationDefinitionParameterBindingType | None = Field(  # type: ignore
        None,
        alias="binding",
        title="ValueSet details if this is coded",
        description=(
            "Binds to a value set if this parameter is coded (code, Coding, "
            "CodeableConcept)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    documentation: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Description of meaning/use",
        description="Describes the meaning or use of this parameter.",
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    max: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="max",
        title="Maximum Cardinality (a number or *)",
        description=(
            "The maximum number of times this element is permitted to appear in the"
            " request or response."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.IntegerType | None = Field(  # type: ignore
        None,
        alias="min",
        title="Minimum Cardinality",
        description=(
            "The minimum number of times this parameter SHALL appear in the request"
            " or response."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_min", title="Extension field for ``min``."
    )

    name: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name in Parameters.parameter.name or in URL",
        description="The name of used to identify the parameter.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    part: typing.List[fhirtypes.OperationDefinitionParameterType] | None = Field(  # type: ignore
        None,
        alias="part",
        title="Parts of a nested Parameter",
        description="The parts of a nested Parameter.",
        json_schema_extra={
            "element_property": True,
        },
    )

    referencedFrom: typing.List[fhirtypes.OperationDefinitionParameterReferencedFromType] | None = Field(  # type: ignore
        None,
        alias="referencedFrom",
        title="References to this parameter",
        description=(
            "Identifies other resource parameters within the operation invocation "
            "that are expected to resolve to this resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    scope: typing.List[fhirtypes.CodeType | None] | None = Field(  # type: ignore
        None,
        alias="scope",
        title="instance | type | system",
        description=(
            "If present, indicates that the parameter applies when the operation is"
            " being invoked at the specified level."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["instance", "type", "system"],
        },
    )
    scope__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_scope", title="Extension field for ``scope``."
    )

    searchType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="searchType",
        title=(
            "number | date | string | token | reference | composite | quantity | "
            "uri | special"
        ),
        description=(
            "How the parameter is understood if/when it used as search parameter. "
            "This is only used if the parameter is a string."
        ),
        json_schema_extra={
            "element_property": True,
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
    searchType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_searchType", title="Extension field for ``searchType``."
    )

    targetProfile: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        None,
        alias="targetProfile",
        title=(
            "If type is Reference | canonical, allowed targets. If type is "
            "'Resource', then this constrains the allowed resource types"
        ),
        description=(
            'Used when the type is "Reference" or "canonical", and identifies a '
            "profile structure or implementation Guide that applies to the target "
            "of the reference this parameter refers to. If any profiles are "
            "specified, then the content must conform to at least one of them. The "
            "URL can be a local reference - to a contained StructureDefinition, or "
            "a reference to another StructureDefinition or Implementation Guide by "
            "a canonical URL. When an implementation guide is specified, the target"
            " resource SHALL conform to at least one profile defined in the "
            "implementation guide."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    targetProfile__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_targetProfile", title="Extension field for ``targetProfile``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="type",
        title="What type this parameter has",
        description="The type for this parameter.",
        json_schema_extra={
            "element_property": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    use: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="use",
        title="in | out",
        description="Whether this is an input or an output parameter.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["in", "out"],
        },
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_use", title="Extension field for ``use``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``OperationDefinitionParameter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "use",
            "scope",
            "min",
            "max",
            "documentation",
            "type",
            "allowedType",
            "targetProfile",
            "searchType",
            "binding",
            "referencedFrom",
            "part",
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
            ("max", "max__ext"),
            ("min", "min__ext"),
            ("name", "name__ext"),
            ("use", "use__ext"),
        ]
        return required_fields


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    ValueSet details if this is coded.
    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """

    __resource_type__ = "OperationDefinitionParameterBinding"

    strength: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="strength",
        title="required | extensible | preferred | example",
        description=(
            "Indicates the degree of conformance expectations associated with this "
            "binding - that is, the degree to which the provided value set must be "
            "adhered to in the instances."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["required", "extensible", "preferred", "example"],
        },
    )
    strength__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_strength", title="Extension field for ``strength``."
    )

    valueSet: fhirtypes.CanonicalType | None = Field(  # type: ignore
        None,
        alias="valueSet",
        title="Source of value set",
        description=(
            "Points to the value set or external definition (e.g. implicit value "
            "set) that identifies the set of codes to be used."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ValueSet"],
        },
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``OperationDefinitionParameterBinding`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "strength", "valueSet"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("strength", "strength__ext"), ("valueSet", "valueSet__ext")]
        return required_fields


class OperationDefinitionParameterReferencedFrom(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    References to this parameter.
    Identifies other resource parameters within the operation invocation that
    are expected to resolve to this resource.
    """

    __resource_type__ = "OperationDefinitionParameterReferencedFrom"

    source: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="source",
        title="Referencing parameter",
        description=(
            "The name of the parameter or dot-separated path of parameter names "
            "pointing to the resource parameter that is expected to contain a "
            "reference to this resource."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_source", title="Extension field for ``source``."
    )

    sourceId: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="sourceId",
        title="Element id of reference",
        description=(
            "The id of the element in the referencing resource that is expected to "
            "resolve to this resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_sourceId", title="Extension field for ``sourceId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``OperationDefinitionParameterReferencedFrom`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "source", "sourceId"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("source", "source__ext")]
        return required_fields
