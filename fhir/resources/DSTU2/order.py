# -*- coding: utf-8 -*-
"""
Profile: None
Release: DSTU2
Version: 1.0.2
Revision: None
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic.v1 import Field, root_validator

from . import fhirtypes
from .backboneelement import BackboneElement
from .domainresource import DomainResource


class Order(DomainResource):
    """
    An order resource describes a request that an action be performed. An
    order is expected to lead to one or more responses that describe the
    outcome of processing/handling the order. The order resource is focused
    on the process of actually requesting an action be performed; the actual
    action to be performed is detailed in a separate resource that contains
    the details. Note that orders are often called "requests", but this name
    is not used here since the word "request" is used differently elsewhere in
    this specification.

    Note that there are a variety of processes associated with making and
    processing orders. Some orders may be handled immediately by automated
    systems but most require real world actions by one or more humans. Some
    orders can only be processed when other real world actions happen, such as
    a patient actually presenting themselves so that the action to be
    performed can actually be performed. Often these real world dependencies
    are only implicit in the order details.
    """

    resource_type = Field("Order", const=True)

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON).",
        description="Identifiers assigned to this order by the orderer or by the receiver.",
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="date",
        description="When the order was made.",
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="subject",
        description="Patient this order is about.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group", "Device", "Substance"],
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title="source",
        description="Who initiated this order.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    target: fhirtypes.ReferenceType = Field(
        None,
        alias="target",
        title="target",
        description="Who is intended to fulfill the order.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization", "Device"],
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCodeableConcept",
        title="reasonCodeableConcept",
        description="Why the order was made.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e reason[x]
        one_of_many="reason",
        one_of_many_required=False,
    )

    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title="reasonReference",
        description="Why the order was made.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e reason[x]
        one_of_many="reason",
        one_of_many_required=False,
    )

    when: fhirtypes.OrderWhenType = Field(
        None,
        alias="when",
        title="when",
        description=(
            "When order should be fulfilled. "
            "Provide a code or a schedule, but not both."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    detail: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="detail",
        title="detail",
        description="What action is being ordered.",
        # if property is element of this resource.
        element_property=True,
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
            "reason": ["reasonCodeableConcept", "reasonReference"],
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


class OrderWhen(BackboneElement):
    """
    When order should be fulfilled.
    Provide a code or a schedule, but not both
    """

    resource_type = Field("OrderWhen", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="code",
        description=(
            "Code specifies when request should be done. "
            "The code may simply be a priority code."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    schedule: fhirtypes.TimingType = Field(
        None,
        alias="schedule",
        title="schedule",
        description="   A formal schedule.",
        # if property is element of this resource.
        element_property=True,
    )
