# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class OperationDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        title=(
            "Type `Reference` referencing `OperationDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Marks this as a profile of the base",
    )

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code`",
        description="Name used to invoke the operation",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String`",
        description="Additional information about use",
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
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
        description="Natural language description of the operation definition",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
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

    idempotent: bool = Field(
        None,
        alias="idempotent",
        title="Type `bool`",
        description="Whether content is unchanged by the operation",
    )
    idempotent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_idempotent", title="Extension field for ``idempotent``."
    )

    instance: bool = Field(
        ..., alias="instance", title="Type `bool`", description="Invoke on an instance?"
    )
    instance__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_instance", title="Extension field for ``instance``."
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for operation definition (if applicable)",
    )

    kind: fhirtypes.Code = Field(
        ..., alias="kind", title="Type `Code`", description="operation | query"
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String`",
        description="Name for this operation definition (computer friendly)",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    overload: ListType[fhirtypes.OperationDefinitionOverloadType] = Field(
        None,
        alias="overload",
        title=(
            "List of `OperationDefinitionOverload` items (represented as `dict` in "
            "JSON)"
        ),
        description="Define overloaded variants for when  generating code",
    )

    parameter: ListType[fhirtypes.OperationDefinitionParameterType] = Field(
        None,
        alias="parameter",
        title=(
            "List of `OperationDefinitionParameter` items (represented as `dict` in"
            " JSON)"
        ),
        description="Parameters for the operation/query",
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

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown`",
        description="Why this operation definition is defined",
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    resource: ListType[fhirtypes.Code] = Field(
        None,
        alias="resource",
        title="List of `Code` items",
        description="Types this operation applies to",
    )
    resource__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_resource", title="Extension field for ``resource``."
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

    system: bool = Field(
        ...,
        alias="system",
        title="Type `bool`",
        description="Invoke at the system level?",
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    type: bool = Field(
        ..., alias="type", title="Type `bool`", description="Invole at the type level?"
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri`",
        description="Logical URI to reference this operation definition (globally unique)",
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
        description="Business version of the operation definition",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class OperationDefinitionOverload(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
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
        title="Type `String`",
        description="Comments to go on overload",
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    parameterName: ListType[fhirtypes.String] = Field(
        None,
        alias="parameterName",
        title="List of `String` items",
        description="Name of parameter to include in overload",
    )
    parameterName__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_parameterName", title="Extension field for ``parameterName``."
    )


class OperationDefinitionParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Parameters for the operation/query.
    The parameters for the operation/query.
    """

    resource_type = Field("OperationDefinitionParameter", const=True)

    binding: fhirtypes.OperationDefinitionParameterBindingType = Field(
        None,
        alias="binding",
        title=(
            "Type `OperationDefinitionParameterBinding` (represented as `dict` in "
            "JSON)"
        ),
        description="ValueSet details if this is coded",
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String`",
        description="Description of meaning/use",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    max: fhirtypes.String = Field(
        ...,
        alias="max",
        title="Type `String`",
        description="Maximum Cardinality (a number or *)",
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.Integer = Field(
        ..., alias="min", title="Type `Integer`", description="Minimum Cardinality"
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    name: fhirtypes.Code = Field(
        ...,
        alias="name",
        title="Type `Code`",
        description="Name in Parameters.parameter.name or in URL",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    part: ListType[fhirtypes.OperationDefinitionParameterType] = Field(
        None,
        alias="part",
        title=(
            "List of `OperationDefinitionParameter` items (represented as `dict` in"
            " JSON)"
        ),
        description="Parts of a nested Parameter",
    )

    profile: fhirtypes.ReferenceType = Field(
        None,
        alias="profile",
        title=(
            "Type `Reference` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Profile on the type",
    )

    searchType: fhirtypes.Code = Field(
        None,
        alias="searchType",
        title="Type `Code`",
        description=(
            "number | date | string | token | reference | composite | quantity | " "uri"
        ),
    )
    searchType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_searchType", title="Extension field for ``searchType``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code`",
        description="What type this parameter has",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    use: fhirtypes.Code = Field(
        ..., alias="use", title="Type `Code`", description="in | out"
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    ValueSet details if this is coded.
    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """

    resource_type = Field("OperationDefinitionParameterBinding", const=True)

    strength: fhirtypes.Code = Field(
        ...,
        alias="strength",
        title="Type `Code`",
        description="required | extensible | preferred | example",
    )
    strength__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_strength", title="Extension field for ``strength``."
    )

    valueSetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueSetReference",
        title=(
            "Type `Reference` referencing `ValueSet` (represented as `dict` in " "JSON)"
        ),
        description="Source of value set",
        one_of_many="valueSet",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    valueSetUri: fhirtypes.Uri = Field(
        None,
        alias="valueSetUri",
        title="Type `Uri`",
        description="Source of value set",
        one_of_many="valueSet",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )
    valueSetUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSetUri", title="Extension field for ``valueSetUri``."
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
