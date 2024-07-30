# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
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

    affectsState: bool = Field(  # type: ignore
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
    affectsState__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_affectsState", title="Extension field for ``affectsState``."
    )

    base: fhirtypes.CanonicalType = Field(  # type: ignore
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
    base__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_base", title="Extension field for ``base``."
    )

    code: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="code",
        title="Name used to invoke the operation",
        description="The name used to invoke the operation.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    comment: fhirtypes.MarkdownType = Field(  # type: ignore
        None,
        alias="comment",
        title="Additional information about use",
        description="Additional information about how to use this operation or named query.",
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    contact: typing.List[fhirtypes.ContactDetailType] = Field(  # type: ignore
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

    date: fhirtypes.DateTimeType = Field(  # type: ignore
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the operation definition was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the operation definition "
            "changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.MarkdownType = Field(  # type: ignore
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
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this operation definition is authored"
            " for testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    inputProfile: fhirtypes.CanonicalType = Field(  # type: ignore
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
    inputProfile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_inputProfile", title="Extension field for ``inputProfile``."
    )

    instance: bool = Field(  # type: ignore
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
    instance__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_instance", title="Extension field for ``instance``."
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(  # type: ignore
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

    kind: fhirtypes.CodeType = Field(  # type: ignore
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
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_kind", title="Extension field for ``kind``."
    )

    name: fhirtypes.StringType = Field(  # type: ignore
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
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    outputProfile: fhirtypes.CanonicalType = Field(  # type: ignore
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
    outputProfile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_outputProfile", title="Extension field for ``outputProfile``."
    )

    overload: typing.List[fhirtypes.OperationDefinitionOverloadType] = Field(  # type: ignore
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

    parameter: typing.List[fhirtypes.OperationDefinitionParameterType] = Field(  # type: ignore
        None,
        alias="parameter",
        title="Parameters for the operation/query",
        description="The parameters for the operation/query.",
        json_schema_extra={
            "element_property": True,
        },
    )

    publisher: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the "
            "operation definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.MarkdownType = Field(  # type: ignore
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
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    resource: typing.List[typing.Optional[fhirtypes.CodeType]] = Field(  # type: ignore
        None,
        alias="resource",
        title="Types this operation applies to",
        description="The types on which this operation can be executed.",
        json_schema_extra={
            "element_property": True,
        },
    )
    resource__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(  # type: ignore
        None, alias="_resource", title="Extension field for ``resource``."
    )

    status: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this operation definition. Enables tracking the life-"
            "cycle of the content."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    system: bool = Field(  # type: ignore
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
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_system", title="Extension field for ``system``."
    )

    title: fhirtypes.StringType = Field(  # type: ignore
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
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_title", title="Extension field for ``title``."
    )

    type: bool = Field(  # type: ignore
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
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.UriType = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this operation definition, represented as a "
            "URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this operation definition "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which at which an "
            "authoritative instance of this operation definition is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the operation definition is stored on "
            "different servers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] = Field(  # type: ignore
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate operation definition instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType = Field(  # type: ignore
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
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
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
            "version",
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

    comment: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="comment",
        title="Comments to go on overload",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_comment", title="Extension field for ``comment``."
    )

    parameterName: typing.List[typing.Optional[fhirtypes.StringType]] = Field(  # type: ignore
        None,
        alias="parameterName",
        title="Name of parameter to include in overload",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    parameterName__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(  # type: ignore
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

    binding: fhirtypes.OperationDefinitionParameterBindingType = Field(  # type: ignore
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

    documentation: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="documentation",
        title="Description of meaning/use",
        description="Describes the meaning or use of this parameter.",
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    max: fhirtypes.StringType = Field(  # type: ignore
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
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.IntegerType = Field(  # type: ignore
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
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_min", title="Extension field for ``min``."
    )

    name: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="name",
        title="Name in Parameters.parameter.name or in URL",
        description="The name of used to identify the parameter.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    part: typing.List[fhirtypes.OperationDefinitionParameterType] = Field(  # type: ignore
        None,
        alias="part",
        title="Parts of a nested Parameter",
        description="The parts of a nested Parameter.",
        json_schema_extra={
            "element_property": True,
        },
    )

    referencedFrom: typing.List[fhirtypes.OperationDefinitionParameterReferencedFromType] = Field(  # type: ignore
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

    searchType: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="searchType",
        title=(
            "number | date | string | token | reference | composite | quantity | "
            "uri | special"
        ),
        description=(
            "How the parameter is understood as a search parameter. This is only "
            "used if the parameter type is 'string'."
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
    searchType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_searchType", title="Extension field for ``searchType``."
    )

    targetProfile: typing.List[typing.Optional[fhirtypes.CanonicalType]] = Field(  # type: ignore
        None,
        alias="targetProfile",
        title="If type is Reference | canonical, allowed targets",
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
    targetProfile__ext: typing.List[typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(  # type: ignore
        None, alias="_targetProfile", title="Extension field for ``targetProfile``."
    )

    type: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="type",
        title="What type this parameter has",
        description="The type for this parameter.",
        json_schema_extra={
            "element_property": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    use: fhirtypes.CodeType = Field(  # type: ignore
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
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
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
            "min",
            "max",
            "documentation",
            "type",
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

    strength: fhirtypes.CodeType = Field(  # type: ignore
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
    strength__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_strength", title="Extension field for ``strength``."
    )

    valueSet: fhirtypes.CanonicalType = Field(  # type: ignore
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
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
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

    source: fhirtypes.StringType = Field(  # type: ignore
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
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_source", title="Extension field for ``source``."
    )

    sourceId: fhirtypes.StringType = Field(  # type: ignore
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
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
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
