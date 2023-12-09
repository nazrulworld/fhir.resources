# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
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


class OperationDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of an operation or a named query.
    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """

    resource_type = Field("OperationDefinition", const=True)

    base: fhirtypes.ReferenceType = Field(
        None,
        alias="base",
        title="Marks this as a profile of the base",
        description=(
            "Indicates that this operation definition is a constraining profile on "
            "the base."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["OperationDefinition"],
    )

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Name used to invoke the operation",
        description="The name used to invoke the operation.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Additional information about use",
        description="Additional information about how to use this operation or named query.",
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
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
            "The date  (and optionally time) when the operation definition was "
            "published. The date must change if and when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the operation "
            "definition changes."
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
        title="Natural language description of the operation definition",
        description=(
            "A free text natural language description of the operation definition "
            "from a consumer's perspective."
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
            "A boolean value to indicate that this operation definition is authored"
            " for testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    idempotent: bool = Field(
        None,
        alias="idempotent",
        title="Whether content is unchanged by the operation",
        description=(
            "Operations that are idempotent (see [HTTP specification definition of "
            "idempotent](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)) "
            "may be invoked by performing an HTTP GET operation instead of a POST."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    idempotent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_idempotent", title="Extension field for ``idempotent``."
    )

    instance: bool = Field(
        None,
        alias="instance",
        title="Invoke on an instance?",
        description=(
            "Indicates whether this operation can be invoked on a particular "
            "instance of one of the given types."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    instance__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_instance", title="Extension field for ``instance``."
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for operation definition (if applicable)",
        description=(
            "A legal or geographic region in which the operation definition is "
            "intended to be used."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    kind: fhirtypes.Code = Field(
        None,
        alias="kind",
        title="operation | query",
        description="Whether this is an operation or a named query.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["operation", "query"],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this operation definition (computer friendly)",
        description=(
            "A natural language name identifying the operation definition. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    overload: typing.List[fhirtypes.OperationDefinitionOverloadType] = Field(
        None,
        alias="overload",
        title="Define overloaded variants for when  generating code",
        description=(
            "Defines an appropriate combination of parameters to use when invoking "
            "this operation, to help code generators when generating overloaded "
            "parameter sets for this operation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    parameter: typing.List[fhirtypes.OperationDefinitionParameterType] = Field(
        None,
        alias="parameter",
        title="Parameters for the operation/query",
        description="The parameters for the operation/query.",
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the "
            "operation definition."
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
        title="Why this operation definition is defined",
        description=(
            "Explaination of why this operation definition is needed and why it has"
            " been designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    resource: typing.List[fhirtypes.Code] = Field(
        None,
        alias="resource",
        title="Types this operation applies to",
        description="The types on which this operation can be executed.",
        # if property is element of this resource.
        element_property=True,
    )
    resource__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_resource", title="Extension field for ``resource``.")

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this operation definition. Enables tracking the life-"
            "cycle of the content."
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

    system: bool = Field(
        None,
        alias="system",
        title="Invoke at the system level?",
        description=(
            "Indicates whether this operation or named query can be invoked at the "
            "system level (e.g. without needing to choose a resource type for the "
            "context)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    type: bool = Field(
        None,
        alias="type",
        title="Invole at the type level?",
        description=(
            "Indicates whether this operation or named query can be invoked at the "
            "resource type level for any given resource type level (e.g. without "
            "needing to choose a specific resource id for the context)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Logical URI to reference this operation definition (globally unique)",
        description=(
            "An absolute URI that is used to identify this operation definition "
            "when it is referenced in a specification, model, design or an "
            "instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD "
            "be an address at which this operation definition is (or will be) "
            "published. The URL SHOULD include the major version of the operation "
            "definition. For more information see [Technical and Business "
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
            "indexing and searching for appropriate operation definition instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
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
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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
            "idempotent",
            "code",
            "comment",
            "base",
            "resource",
            "system",
            "type",
            "instance",
            "parameter",
            "overload",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2167(
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
            ("instance", "instance__ext"),
            ("kind", "kind__ext"),
            ("name", "name__ext"),
            ("status", "status__ext"),
            ("system", "system__ext"),
            ("type", "type__ext"),
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


class OperationDefinitionOverload(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Define overloaded variants for when  generating code.
    Defines an appropriate combination of parameters to use when invoking this
    operation, to help code generators when generating overloaded parameter
    sets for this operation.
    """

    resource_type = Field("OperationDefinitionOverload", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Comments to go on overload",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    parameterName: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="parameterName",
        title="Name of parameter to include in overload",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    parameterName__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
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

    resource_type = Field("OperationDefinitionParameter", const=True)

    binding: fhirtypes.OperationDefinitionParameterBindingType = Field(
        None,
        alias="binding",
        title="ValueSet details if this is coded",
        description=(
            "Binds to a value set if this parameter is coded (code, Coding, "
            "CodeableConcept)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Description of meaning/use",
        description="Describes the meaning or use of this parameter.",
        # if property is element of this resource.
        element_property=True,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Maximum Cardinality (a number or *)",
        description=(
            "The maximum number of times this element is permitted to appear in the"
            " request or response."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.Integer = Field(
        None,
        alias="min",
        title="Minimum Cardinality",
        description=(
            "The minimum number of times this parameter SHALL appear in the request"
            " or response."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    name: fhirtypes.Code = Field(
        None,
        alias="name",
        title="Name in Parameters.parameter.name or in URL",
        description="The name of used to identify the parameter.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    part: typing.List[fhirtypes.OperationDefinitionParameterType] = Field(
        None,
        alias="part",
        title="Parts of a nested Parameter",
        description="The parts of a nested Parameter.",
        # if property is element of this resource.
        element_property=True,
    )

    profile: fhirtypes.ReferenceType = Field(
        None,
        alias="profile",
        title="Profile on the type",
        description="A profile the specifies the rules that this parameter must conform to.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )

    searchType: fhirtypes.Code = Field(
        None,
        alias="searchType",
        title=(
            "number | date | string | token | reference | composite | quantity | " "uri"
        ),
        description=(
            "How the parameter is understood as a search parameter. This is only "
            "used if the parameter type is 'string'."
        ),
        # if property is element of this resource.
        element_property=True,
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
        ],
    )
    searchType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_searchType", title="Extension field for ``searchType``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="What type this parameter has",
        description="The type for this parameter.",
        # if property is element of this resource.
        element_property=True,
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="in | out",
        description="Whether this is an input or an output parameter.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["in", "out"],
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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
            "searchType",
            "profile",
            "binding",
            "part",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3100(
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
            ("max", "max__ext"),
            ("min", "min__ext"),
            ("name", "name__ext"),
            ("use", "use__ext"),
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


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    ValueSet details if this is coded.
    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """

    resource_type = Field("OperationDefinitionParameterBinding", const=True)

    strength: fhirtypes.Code = Field(
        None,
        alias="strength",
        title="required | extensible | preferred | example",
        description=(
            "Indicates the degree of conformance expectations associated with this "
            "binding - that is, the degree to which the provided value set must be "
            "adhered to in the instances."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["required", "extensible", "preferred", "example"],
    )
    strength__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_strength", title="Extension field for ``strength``."
    )

    valueSetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueSetReference",
        title="Source of value set",
        description=(
            "Points to the value set or external definition (e.g. implicit value "
            "set) that identifies the set of codes to be used."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e valueSet[x]
        one_of_many="valueSet",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )

    valueSetUri: fhirtypes.Uri = Field(
        None,
        alias="valueSetUri",
        title="Source of value set",
        description=(
            "Points to the value set or external definition (e.g. implicit value "
            "set) that identifies the set of codes to be used."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e valueSet[x]
        one_of_many="valueSet",
        one_of_many_required=True,
    )
    valueSetUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSetUri", title="Extension field for ``valueSetUri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``OperationDefinitionParameterBinding`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "strength",
            "valueSetUri",
            "valueSetReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3788(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("strength", "strength__ext")]
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
    def validate_one_of_many_3788(
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
        one_of_many_fields = {"valueSet": ["valueSetReference", "valueSetUri"]}
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
