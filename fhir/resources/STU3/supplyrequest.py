# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class SupplyRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Request for a medication, substance or device.
    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """

    resource_type = Field("SupplyRequest", const=True)

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="When the request was made",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="The kind of supply (central, non-stock, etc.)",
        description=(
            "Category of supply, e.g.  central, non-stock, etc. This is used to "
            "support work flows associated with the supply process."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    deliverFrom: fhirtypes.ReferenceType = Field(
        None,
        alias="deliverFrom",
        title="The origin of the supply",
        description="Where the supply is expected to come from.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "Location"],
    )

    deliverTo: fhirtypes.ReferenceType = Field(
        None,
        alias="deliverTo",
        title="The destination of the supply",
        description="Where the supply is destined to go.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "Location", "Patient"],
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description="Unique identifier for this supply request.",
        # if property is element of this resource.
        element_property=True,
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When the request should be fulfilled",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="When the request should be fulfilled",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="When the request should be fulfilled",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    orderedItem: fhirtypes.SupplyRequestOrderedItemType = Field(
        None,
        alias="orderedItem",
        title="The item being requested",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly this SupplyRequest should be addressed with "
            "respect to other requests."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["routine", "urgent", "asap", "stat"],
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reasonCodeableConcept",
        title="Why the supply item was requested",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e reason[x]
        one_of_many="reason",
        one_of_many_required=False,
    )

    reasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="reasonReference",
        title="Why the supply item was requested",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e reason[x]
        one_of_many="reason",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    requester: fhirtypes.SupplyRequestRequesterType = Field(
        None,
        alias="requester",
        title="Who/what is requesting service",
        description=(
            "The individual who initiated the request and has responsibility for "
            "its activation."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | suspended +",
        description="Status of the supply request.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "suspended", "+"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    supplier: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="supplier",
        title="Who is intended to fulfill the request",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SupplyRequest`` according specification,
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
            "identifier",
            "status",
            "category",
            "priority",
            "orderedItem",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "authoredOn",
            "requester",
            "supplier",
            "reasonCodeableConcept",
            "reasonReference",
            "deliverFrom",
            "deliverTo",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_1597(
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
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
            ],
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


class SupplyRequestOrderedItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The item being requested.
    """

    resource_type = Field("SupplyRequestOrderedItem", const=True)

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="Medication, Substance, or Device requested to be supplied",
        description=(
            "The item that is requested to be supplied. This is either a link to a "
            "resource representing the details of the item or a code that "
            "identifies the item from a known list."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=False,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="Medication, Substance, or Device requested to be supplied",
        description=(
            "The item that is requested to be supplied. This is either a link to a "
            "resource representing the details of the item or a code that "
            "identifies the item from a known list."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication", "Substance", "Device"],
    )

    quantity: fhirtypes.QuantityType = Field(
        ...,
        alias="quantity",
        title="The requested amount of the item indicated",
        description="The amount that is being ordered of the indicated item.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SupplyRequestOrderedItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "quantity",
            "itemCodeableConcept",
            "itemReference",
            "itemReference",
            "itemReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2698(
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who/what is requesting service.
    The individual who initiated the request and has responsibility for its
    activation.
    """

    resource_type = Field("SupplyRequestRequester", const=True)

    agent: fhirtypes.ReferenceType = Field(
        ...,
        alias="agent",
        title="Individual making the request",
        description="The device, practitioner, etc. who initiated the request.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Organization",
            "Patient",
            "RelatedPerson",
            "Device",
        ],
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Organization agent is acting for",
        description="The organization the device or practitioner was acting on behalf of.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SupplyRequestRequester`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "agent", "onBehalfOf"]
