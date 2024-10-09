from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyDelivery
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SupplyDelivery(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Delivery of bulk Supplies.
    Record of delivery of what is supplied.
    """

    __resource_type__ = "SupplyDelivery"

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="basedOn",
        title="Fulfills plan, proposal or order",
        description=(
            "A plan, proposal or order that is fulfilled in whole or in part by "
            "this event."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SupplyRequest"],
        },
    )

    destination: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="destination",
        title="Where the delivery was sent",
        description=(
            "Identification of the facility/location where the delivery was shipped"
            " to."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifier for the supply delivery event that is used to identify it "
            "across multiple disparate systems."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    occurrenceDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="occurrenceDateTime",
        title="When event occurred",
        description="The date or time(s) the activity occurred.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="occurrencePeriod",
        title="When event occurred",
        description="The date or time(s) the activity occurred.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    occurrenceTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        None,
        alias="occurrenceTiming",
        title="When event occurred",
        description="The date or time(s) the activity occurred.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="partOf",
        title="Part of referenced event",
        description="A larger event of which this particular event is a component or step.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SupplyDelivery", "Contract"],
        },
    )

    patient: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="patient",
        title="Patient for whom the item is supplied",
        description=(
            "A link to a resource representing the person whom the delivered item "
            "is for."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    receiver: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="receiver",
        title="Who received the delivery",
        description="Identifies the individual or organization that received the delivery.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="in-progress | completed | abandoned | entered-in-error",
        description="A code specifying the state of the dispense event.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "in-progress",
                "completed",
                "abandoned",
                "entered-in-error",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    suppliedItem: typing.List[fhirtypes.SupplyDeliverySuppliedItemType] | None = Field(  # type: ignore
        None,
        alias="suppliedItem",
        title="The item that is delivered or supplied",
        description="The item that is being delivered or has been supplied.",
        json_schema_extra={
            "element_property": True,
        },
    )

    supplier: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="supplier",
        title="The item supplier",
        description="The individual or organization responsible for supplying the delivery.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="type",
        title="Category of supply event",
        description=(
            "Indicates the type of supply being provided.  Examples include: "
            "Medication, Device, Biologically Derived Product."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SupplyDelivery`` according specification,
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
            "basedOn",
            "partOf",
            "status",
            "patient",
            "type",
            "suppliedItem",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "supplier",
            "destination",
            "receiver",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
            "occurrence": ["occurrenceDateTime", "occurrencePeriod", "occurrenceTiming"]
        }
        return one_of_many_fields


class SupplyDeliverySuppliedItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The item that is delivered or supplied.
    The item that is being delivered or has been supplied.
    """

    __resource_type__ = "SupplyDeliverySuppliedItem"

    itemCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="itemCodeableConcept",
        title="Medication, Substance, Device or Biologically Derived Product supplied",
        description=(
            "Identifies the medication, substance, device or biologically derived "
            "product being supplied. This is either a link to a resource "
            "representing the details of the item or a code that identifies the "
            "item from a known list."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": False,
        },
    )

    itemReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="itemReference",
        title="Medication, Substance, Device or Biologically Derived Product supplied",
        description=(
            "Identifies the medication, substance, device or biologically derived "
            "product being supplied. This is either a link to a resource "
            "representing the details of the item or a code that identifies the "
            "item from a known list."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Medication",
                "Substance",
                "Device",
                "BiologicallyDerivedProduct",
                "NutritionProduct",
                "InventoryItem",
            ],
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="quantity",
        title="Amount supplied",
        description=(
            "The amount of the item that has been supplied.  Unit of measure may be"
            " included."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SupplyDeliverySuppliedItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "quantity",
            "itemCodeableConcept",
            "itemReference",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
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
        return one_of_many_fields
