from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SupplyRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Request for a medication, substance or device.
    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """

    __resource_type__ = "SupplyRequest"

    authoredOn: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="authoredOn",
        title="When the request was made",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="The kind of supply (central, non-stock, etc.)",
        description=(
            "Category of supply, e.g.  central, non-stock, etc. This is used to "
            "support work flows associated with the supply process."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    deliverFrom: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="deliverFrom",
        title="The origin of the supply",
        description="Where the supply is expected to come from.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization", "Location"],
        },
    )

    deliverTo: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="deliverTo",
        title="The destination of the supply",
        description="Where the supply is destined to go.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization", "Location", "Patient"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business Identifier for SupplyRequest",
        description=(
            "Business identifiers assigned to this SupplyRequest by the author "
            "and/or other systems. These identifiers remain constant as the "
            "resource is updated and propagates from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    itemCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="itemCodeableConcept",
        title="Medication, Substance, or Device requested to be supplied",
        description=(
            "The item that is requested to be supplied. This is either a link to a "
            "resource representing the details of the item or a code that "
            "identifies the item from a known list."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": True,
        },
    )

    itemReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="itemReference",
        title="Medication, Substance, or Device requested to be supplied",
        description=(
            "The item that is requested to be supplied. This is either a link to a "
            "resource representing the details of the item or a code that "
            "identifies the item from a known list."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e item[x]
            "one_of_many": "item",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Medication", "Substance", "Device"],
        },
    )

    occurrenceDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="occurrenceDateTime",
        title="When the request should be fulfilled",
        description=None,
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
        title="When the request should be fulfilled",
        description=None,
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
        title="When the request should be fulfilled",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    parameter: typing.List[fhirtypes.SupplyRequestParameterType] | None = Field(  # type: ignore
        None,
        alias="parameter",
        title="Ordered item details",
        description=(
            "Specific parameters for the ordered item.  For example, the size of "
            "the indicated item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly this SupplyRequest should be addressed with "
            "respect to other requests."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["routine", "urgent", "asap", "stat"],
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_priority", title="Extension field for ``priority``."
    )

    quantity: fhirtypes.QuantityType = Field(  # type: ignore
        ...,
        alias="quantity",
        title="The requested amount of the item indicated",
        description="The amount that is being ordered of the indicated item.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="The reason why the supply item was requested",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="reasonReference",
        title="The reason why the supply item was requested",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Condition",
                "Observation",
                "DiagnosticReport",
                "DocumentReference",
            ],
        },
    )

    requester: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="requester",
        title="Individual making the request",
        description="The device, practitioner, etc. who initiated the request.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "Patient",
                "RelatedPerson",
                "Device",
            ],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | suspended +",
        description="Status of the supply request.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "suspended", "+"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    supplier: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="supplier",
        title="Who is intended to fulfill the request",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization", "HealthcareService"],
        },
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
            "itemCodeableConcept",
            "itemReference",
            "quantity",
            "parameter",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "authoredOn",
            "requester",
            "supplier",
            "reasonCode",
            "reasonReference",
            "deliverFrom",
            "deliverTo",
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
            "item": ["itemCodeableConcept", "itemReference"],
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
            ],
        }
        return one_of_many_fields


class SupplyRequestParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Ordered item details.
    Specific parameters for the ordered item.  For example, the size of the
    indicated item.
    """

    __resource_type__ = "SupplyRequestParameter"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Item detail",
        description="A code or string that identifies the device detail being asserted.",
        json_schema_extra={
            "element_property": True,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="Value of detail",
        description="The value of the device detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="Value of detail",
        description="The value of the device detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="Value of detail",
        description="The value of the device detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        None,
        alias="valueRange",
        title="Value of detail",
        description="The value of the device detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SupplyRequestParameter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "valueCodeableConcept",
            "valueQuantity",
            "valueRange",
            "valueBoolean",
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
            "value": [
                "valueBoolean",
                "valueCodeableConcept",
                "valueQuantity",
                "valueRange",
            ]
        }
        return one_of_many_fields
