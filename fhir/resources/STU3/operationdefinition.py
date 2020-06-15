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

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class OperationDefinition(domainresource.DomainResource):
    """ Definition of an operation or a named query.
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
        title="Type `Code` (represented as `dict` in JSON)",
        description="Name used to invoke the operation",
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Type `String` (represented as `dict` in JSON)",
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
        description="Date this was last changed",
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

    idempotent: bool = Field(
        None,
        alias="idempotent",
        title="Type `bool`",
        description="Whether content is unchanged by the operation",
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

    type: bool = Field(
        ..., alias="type", title="Type `bool`", description="Invole at the type level?"
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Logical URI to reference this operation definition (globally unique)",
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
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "number | date | string | token | reference | composite | quantity | " "uri"
        ),
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
        title="Type `Uri` (represented as `dict` in JSON)",
        description="Source of value set",
        one_of_many="valueSet",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
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
