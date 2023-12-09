# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/operationdefinition.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
import typing
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class OperationDefinition(domainresource.DomainResource):
    """Definition of an operation or a named query



    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """

    resource_type = Field("OperationDefinition", const=True)

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Logical URL to reference this operation definition",
        description=(
            "An absolute URL that is used to identify "
            "this operation definition when it is referenced in a "
            "specification, model, design or an instance. This SHALL "
            "be a URL, SHOULD be globally unique, and SHOULD be an "
            "address at which this operation definition is "
            "(or will be) published."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Type `String` (represented as `dict` in JSON)",
        description="Logical id for this version of the operation definition",
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Informal name for this operation",
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON).",
        description="draft | active | retired",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired"],
        element_property=True,
    )

    kind: fhirtypes.Code = Field(
        None,
        alias="kind",
        title="Type `Code` (represented as `dict` in JSON).",
        description="operation | query",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["operation", "query"],
        element_property=True,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="If for testing purposes, not real usage",
        description=(
            "This profile was authored for testing purposes "
            "(or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of the publisher (Organization or individual)",
        element_property=True,
    )

    contact: ListType[fhirtypes.OperationDefinitionContactType] = Field(
        None,
        alias="contact",
        title="Contact details of the publisher",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date for this version of the operation definition",
        description=(
            "The date this version of the operation definition"
            " was published. The date must change when the business "
            "version changes, if it does, and it must change if the "
            "status code changes. In addition, it should change when "
            "the substantive content of the Operation Definition changes."
        ),
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Natural language description of the operation",
        element_property=True,
    )

    requirements: fhirtypes.String = Field(
        None,
        alias="requirements",
        title="Type `String` (represented as `dict` in JSON)",
        description="Why is this needed?",
        element_property=True,
    )

    idempotent: bool = Field(
        None,
        alias="idempotent",
        title="Whether content is unchanged by operation",
        description=(
            "Operations that are idempotent (see HTTP specification "
            "definition of idempotent ) may be invoked by performing "
            "an HTTP GET operation instead of a POST."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.Code = Field(
        None,
        alias="code",
        title="Type `Code` (represented as `dict` in JSON).",
        description="Name used to invoke the operation",
        element_property=True,
    )

    notes: fhirtypes.String = Field(
        None,
        alias="notes",
        title="Type `String` (represented as `dict` in JSON)",
        description="Additional information about use",
        element_property=True,
    )

    base: fhirtypes.ReferenceType = Field(
        None,
        alias="base",
        title=(
            "Type 'Reference' referencing 'OperationDefinition'  "
            "(represented as 'dict' in JSON)."
        ),
        description="Marks this as a profile of the base",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["OperationDefinition"],
        element_property=True,
    )

    system: bool = Field(
        None,
        alias="system",
        title="Invoke at the system level?",
        description=(
            "Indicates whether this operation or named "
            "query can be invoked at the system level (e.g. without "
            "needing to choose a resource type for the context)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: ListType[fhirtypes.Code] = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON).",
        description="Invoke at resource level for these type",
        element_property=True,
    )

    instance: bool = Field(
        None,
        alias="instance",
        title="Invoke on an instance?",
        description=(
            "Indicates whether this operation can be "
            "invoked on a particular instance of one of the given types."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    parameter: ListType[fhirtypes.OperationDefinitionParameterType] = Field(
        None,
        alias="parameter",
        title="Contact details of the publisher",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class OperationDefinitionContact(BackboneElement):
    """Contact details of the publisher


    Contacts to assist a user in finding and communicating with the publisher.
    """

    resource_type = Field("OperationDefinitionContact", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Name of a individual to contact",
        element_property=True,
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="List of `ContactPoint` items (represented as `dict` in JSON).",
        description="Contact details for individual or publisher",
        element_property=True,
    )


class OperationDefinitionParameter(BackboneElement):
    """Parameters for the operation/query


    The parameters for the operation/query.
    """

    resource_type = Field("OperationDefinitionParameter", const=True)

    name: fhirtypes.Code = Field(
        None,
        alias="name",
        title="Type `Code` (represented as `dict` in JSON).",
        description="Name in Parameters.parameter.name or in URL",
        element_property=True,
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="Type `Code` (represented as `dict` in JSON).",
        description="in | out",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["in", "out"],
        element_property=True,
    )

    min: fhirtypes.Integer = Field(
        None,
        alias="min",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Minimum Cardinality",
        element_property=True,
    )

    max: fhirtypes.String = Field(
        None,
        alias="max",
        title="Type `String` (represented as `dict` in JSON)",
        description="Maximum Cardinality (a number or *)",
        element_property=True,
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Type `String` (represented as `dict` in JSON)",
        description="Description of meaning/use",
        element_property=True,
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code` (represented as `dict` in JSON).",
        description="What type this parameter has",
        element_property=True,
    )

    profile: fhirtypes.ReferenceType = Field(
        None,
        alias="profile",
        title=(
            "Type 'Reference' referencing 'StructureDefinition'"
            "  (represented as 'dict' in JSON)."
        ),
        description="Profile on the type",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
        element_property=True,
    )

    binding: ListType[fhirtypes.OperationDefinitionParameterBindingType] = Field(
        None,
        alias="binding",
        title="ValueSet details if this is coded",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    part: typing.List[fhirtypes.ParametersParameterType] = Field(
        None,
        alias="part",
        title="Named part of a parameter (e.g. Tuple)",
        description="Parts of a Tuple Parameter",
        # if property is element of this resource.
        element_property=True,
    )


class OperationDefinitionParameterBinding(BackboneElement):
    """ValueSet details if this is coded


    Binds to a value set if this parameter is coded (code, Coding, CodeableConcept).
    """

    resource_type = Field("OperationDefinitionParameterBinding", const=True)

    strength: fhirtypes.Code = Field(
        None,
        alias="strength",
        title="Type `Code` (represented as `dict` in JSON).",
        description="required | extensible | preferred | example",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["required", "extensible", "preferred", "example"],
        element_property=True,
    )

    valueSetUri: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Source of value set",
        description=(
            "Points to the value set or external definition "
            "(e.g. implicit value set) that identifies the set "
            "of codes to be used."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="valueSet",
        one_of_many_required=False,
    )

    valueSetReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueSetReference",
        title="Type 'Reference' referencing 'ValueSet'  (represented as 'dict' in JSON).",
        description=(
            "Points to the value set or external definition "
            "(e.g. implicit value set) that identifies the set "
            "of codes to be used."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="valueSet",
        one_of_many_required=False,
    )

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2167(
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
            "valueSet": [
                "valueSetUri",
                "valueSetReference",
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
