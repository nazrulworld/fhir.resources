# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class SupplyRequest(domainresource.DomainResource):
    """ Request for a medication, substance or device.
    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """

    resource_type = Field("SupplyRequest", const=True)

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the request was made",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The kind of supply (central, non-stock, etc.)",
    )

    deliverFrom: fhirtypes.ReferenceType = Field(
        None,
        alias="deliverFrom",
        title="Type `Reference` referencing `Organization, Location` (represented as `dict` in JSON)",
        description="The origin of the supply",
    )

    deliverTo: fhirtypes.ReferenceType = Field(
        None,
        alias="deliverTo",
        title="Type `Reference` referencing `Organization, Location, Patient` (represented as `dict` in JSON)",
        description="The destination of the supply",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Unique identifier",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When the request should be fulfilled",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When the request should be fulfilled",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="When the request should be fulfilled",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    orderedItem: fhirtypes.SupplyRequestOrderedItemType = Field(
        None,
        alias="orderedItem",
        title="Type `SupplyRequestOrderedItem` (represented as `dict` in JSON)",
        description="The item being requested",
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `Code` (represented as `dict` in JSON)",
        description="routine | urgent | asap | stat",
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Why the supply item was requested",
        one_of_many="reason",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Why the supply item was requested",
        one_of_many="reason",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    requester: fhirtypes.SupplyRequestRequesterType = Field(
        None,
        alias="requester",
        title="Type `SupplyRequestRequester` (represented as `dict` in JSON)",
        description="Who/what is requesting service",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | suspended +",
    )

    supplier: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supplier",
        title="List of `Reference` items referencing `Organization` (represented as `dict` in JSON)",
        description="Who is intended to fulfill the request",
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
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
            ],
            "reason": ["reasonCodeableConcept", "reasonReference",],
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


class SupplyRequestOrderedItem(backboneelement.BackboneElement):
    """ The item being requested.
    """

    resource_type = Field("SupplyRequestOrderedItem", const=True)

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Medication, Substance, or Device requested to be supplied",
        one_of_many="item",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="Type `Reference` referencing `Medication, Substance, Device` (represented as `dict` in JSON)",
        description="Medication, Substance, or Device requested to be supplied",
        one_of_many="item",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    quantity: fhirtypes.QuantityType = Field(
        ...,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="The requested amount of the item indicated",
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
            "item": ["itemCodeableConcept", "itemReference",],
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


class SupplyRequestRequester(backboneelement.BackboneElement):
    """ Who/what is requesting service.
    The individual who initiated the request and has responsibility for its
    activation.
    """

    resource_type = Field("SupplyRequestRequester", const=True)

    agent: fhirtypes.ReferenceType = Field(
        ...,
        alias="agent",
        title="Type `Reference` referencing `Practitioner, Organization, Patient, RelatedPerson, Device` (represented as `dict` in JSON)",
        description="Individual making the request",
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization agent is acting for",
    )
