# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class OperationDefinition(domainresource.DomainResource):
    """ Definition of an operation or a named query.
    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """

    resource_type = Field("OperationDefinition", const=True)

    affectsState: bool = Field(
        None,
        alias="affectsState",
        title="Type `bool`",
        description="Whether content is changed by the operation",
    )

    base: fhirtypes.Canonical = Field(
        None,
        alias="base",
        title=(
            "Type `Canonical` referencing `OperationDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Marks this as a profile of the base",
    )

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Name used to invoke the operation",
    )

    comment: fhirtypes.Markdown = Field(
        None,
        alias="comment",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Additional information about use",
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
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date last changed",
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Natural language description of the operation definition",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="Type `bool`",
        description="For testing purposes, not real usage",
    )

    inputProfile: fhirtypes.Canonical = Field(
        None,
        alias="inputProfile",
        title=(
            "Type `Canonical` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Validation information for in parameters",
    )

    instance: bool = Field(
        ..., alias="instance", title="Type `bool`", description="Invoke on an instance?"
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Intended jurisdiction for operation definition (if applicable)",
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="Type `Code` (represented as `dict` in JSON)",
        description="operation | query",
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this operation definition (computer friendly)",
    )

    outputProfile: fhirtypes.Canonical = Field(
        None,
        alias="outputProfile",
        title=(
            "Type `Canonical` referencing `StructureDefinition` (represented as "
            "`dict` in JSON)"
        ),
        description="Validation information for out parameters",
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (organization or individual)",
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Type `Markdown` (represented as `dict` in JSON)",
        description="Why this operation definition is defined",
    )

    resource: ListType[fhirtypes.Code] = Field(
        None,
        alias="resource",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="Types this operation applies to",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | retired | unknown",
    )

    system: bool = Field(
        ...,
        alias="system",
        title="Type `bool`",
        description="Invoke at the system level?",
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name for this operation definition (human friendly)",
    )

    type: bool = Field(
        ..., alias="type", title="Type `bool`", description="Invoke at the type level?"
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description=(
            "Canonical identifier for this operation definition, represented as a "
            "URI (globally unique)"
        ),
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="List of `UsageContext` items (represented as `dict` in JSON)",
        description="The context that the content is intended to support",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Business version of the operation definition",
    )


class OperationDefinitionOverload(backboneelement.BackboneElement):
    """ Define overloaded variants for when  generating code.
    Defines an appropriate combination of parameters to use when invoking this
    operation, to help code generators when generating overloaded parameter
    sets for this operation.
    """

    resource_type = Field("OperationDefinitionOverload", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
        description="Comments to go on overload",
    )

    parameterName: ListType[fhirtypes.String] = Field(
        None,
        alias="parameterName",
        title="List of `String` items (represented as `dict` in JSON)",
        description="Name of parameter to include in overload",
    )


class OperationDefinitionParameter(backboneelement.BackboneElement):
    """ Parameters for the operation/query.
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
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of meaning/use",
    )

    max: fhirtypes.String = Field(
        ...,
        alias="max",
        title="Type `String` (represented as `dict` in JSON)",
        description="Maximum Cardinality (a number or *)",
    )

    min: fhirtypes.Integer = Field(
        ...,
        alias="min",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Minimum Cardinality",
    )

    name: fhirtypes.Code = Field(
        ...,
        alias="name",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Name in Parameters.parameter.name or in URL",
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

    referencedFrom: ListType[
        fhirtypes.OperationDefinitionParameterReferencedFromType
    ] = Field(
        None,
        alias="referencedFrom",
        title=(
            "List of `OperationDefinitionParameterReferencedFrom` items "
            "(represented as `dict` in JSON)"
        ),
        description="References to this parameter",
    )

    searchType: fhirtypes.Code = Field(
        None,
        alias="searchType",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "number | date | string | token | reference | composite | quantity | "
            "uri | special"
        ),
    )

    targetProfile: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="targetProfile",
        title=(
            "List of `Canonical` items referencing `StructureDefinition` "
            "(represented as `dict` in JSON)"
        ),
        description="If type is Reference | canonical, allowed targets",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON)",
        description="What type this parameter has",
    )

    use: fhirtypes.Code = Field(
        ...,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON)",
        description="in | out",
    )


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """ ValueSet details if this is coded.
    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """

    resource_type = Field("OperationDefinitionParameterBinding", const=True)

    strength: fhirtypes.Code = Field(
        ...,
        alias="strength",
        title="Type `Code` (represented as `dict` in JSON)",
        description="required | extensible | preferred | example",
    )

    valueSet: fhirtypes.Canonical = Field(
        ...,
        alias="valueSet",
        title=(
            "Type `Canonical` referencing `ValueSet` (represented as `dict` in " "JSON)"
        ),
        description="Source of value set",
    )


class OperationDefinitionParameterReferencedFrom(backboneelement.BackboneElement):
    """ References to this parameter.
    Identifies other resource parameters within the operation invocation that
    are expected to resolve to this resource.
    """

    resource_type = Field("OperationDefinitionParameterReferencedFrom", const=True)

    source: fhirtypes.String = Field(
        ...,
        alias="source",
        title="Type `String` (represented as `dict` in JSON)",
        description="Referencing parameter",
    )

    sourceId: fhirtypes.String = Field(
        None,
        alias="sourceId",
        title="Type `String` (represented as `dict` in JSON)",
        description="Element id of reference",
    )
