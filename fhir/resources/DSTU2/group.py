# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Group
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Group(DomainResource):
    """Group of multiple entities.

    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively and are
    not formally or legally recognized; i.e. a collection of entities that
    isn't an Organization.
    """

    resource_type = Field("Group", const=True)

    actual: fhirtypes.Boolean = Field(
        None, alias="actual", title="Type `bool`.", description="Descriptive or actual."
    )
    name: fhirtypes.String = Field(
        None, alias="name", title="Type `String`.", description="Label for Group."
    )

    quantity: fhirtypes.UnsignedInt = Field(
        None,
        alias="quantity",
        title="Type `Interger`.",
        description="Number of members.",
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Type `Code`.",
        description="person | animal | practitioner | device | medication | substance.",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Kind of Group members.",
    )

    characteristic: ListType[fhirtypes.GroupCharacteristicType] = Field(
        None,
        alias="characteristic",
        title="List of `GroupCharacteristic` items (represented as `dict` in JSON).",
        description="Trait of group members.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Unique id.",
    )

    member: ListType[fhirtypes.GroupMemberType] = Field(
        None,
        alias="member",
        title="List of `GroupMember` items (represented as `dict` in JSON).",
        description="Who or what is in group.",
    )


class GroupCharacteristic(BackboneElement):
    """Trait of group members.

    Identifies the traits shared by members of the group.
    """

    resource_type = Field("GroupCharacteristic", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Kind of characteristic.",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Period over which characteristic is tested.",
    )
    exclude: fhirtypes.Boolean = Field(
        None,
        alias="exclude",
        title="Type `bool`.",
        description="Group includes or excludes.",
    )

    valueBoolean: fhirtypes.Boolean = Field(
        None,
        alias="valueBoolean",
        title="Type `bool`.",
        description="Value held by characteristic.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Value held by characteristic.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Type `Quantity` (represented as `dict` in JSON).",
        description="Value held by characteristic.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Type `Range` (represented as `dict` in JSON).",
        description="Value held by characteristic.",
        one_of_many="value",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
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
        one_of_many_fields = {
            "value": [
                "valueCodeableConcept",
                "valueBoolean",
                "valueQuantity",
                "valueRange",
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


class GroupMember(BackboneElement):
    """Who or what is in group.

    Identifies the resource instances that are members of the group.
    """

    resource_type = Field("GroupMember", const=True)

    entity: fhirtypes.ReferenceType = Field(
        None,
        alias="entity",
        title=(
            "Type `Reference` referencing `Patient, Practitioner, "
            "Device, Medication, Substance` (represented as `dict` in JSON)."
        ),
        description="Reference to the group member.",
    )
    inactive: fhirtypes.Boolean = Field(
        None,
        alias="inactive",
        title="Type `bool`.",
        description="If member is no longer in group.",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON).",
        description="Period member belonged to the group.",
    )
