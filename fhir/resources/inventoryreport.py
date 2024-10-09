from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/InventoryReport
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class InventoryReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A report of inventory or stock items.
    """

    __resource_type__ = "InventoryReport"

    countType: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="countType",
        title="snapshot | difference",
        description=(
            "Whether the report is about the current inventory count (snapshot) or "
            "a differential change in inventory (change)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["snapshot", "difference"],
        },
    )
    countType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_countType", title="Extension field for ``countType``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier for the report",
        description="Business identifier for the InventoryReport.",
        json_schema_extra={
            "element_property": True,
        },
    )

    inventoryListing: typing.List[fhirtypes.InventoryReportInventoryListingType] | None = Field(  # type: ignore
        None,
        alias="inventoryListing",
        title="An inventory listing section (grouped by any of the attributes)",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        None,
        alias="note",
        title="A note associated with the InventoryReport",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    operationType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="operationType",
        title="addition | subtraction",
        description="What type of operation is being performed - addition or subtraction.",
        json_schema_extra={
            "element_property": True,
        },
    )

    operationTypeReason: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="operationTypeReason",
        title=(
            "The reason for this count - regular count, ad-hoc count, new arrivals,"
            " etc"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    reportedDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="reportedDateTime",
        title="When the report has been submitted",
        description=None,
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    reportedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_reportedDateTime",
        title="Extension field for ``reportedDateTime``.",
    )

    reporter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="reporter",
        title="Who submits the report",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "Patient",
                "RelatedPerson",
                "Device",
            ],
        },
    )

    reportingPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        None,
        alias="reportingPeriod",
        title="The period the report refers to",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | requested | active | entered-in-error",
        description=(
            "The status of the inventory check or notification - whether this is "
            "draft (e.g. the report is still pending some updates) or active."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "requested", "active", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InventoryReport`` according specification,
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
            "countType",
            "operationType",
            "operationTypeReason",
            "reportedDateTime",
            "reporter",
            "reportingPeriod",
            "inventoryListing",
            "note",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("countType", "countType__ext"),
            ("reportedDateTime", "reportedDateTime__ext"),
            ("status", "status__ext"),
        ]
        return required_fields


class InventoryReportInventoryListing(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An inventory listing section (grouped by any of the attributes).
    """

    __resource_type__ = "InventoryReportInventoryListing"

    countingDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="countingDateTime",
        title="The date and time when the items were counted",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    countingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None,
        alias="_countingDateTime",
        title="Extension field for ``countingDateTime``.",
    )

    item: typing.List[fhirtypes.InventoryReportInventoryListingItemType] | None = Field(  # type: ignore
        None,
        alias="item",
        title="The item or items in this listing",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    itemStatus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="itemStatus",
        title="The status of the items that are being reported",
        description="The status of the items.",
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="location",
        title="Location of the inventory items",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InventoryReportInventoryListing`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "location",
            "itemStatus",
            "countingDateTime",
            "item",
        ]


class InventoryReportInventoryListingItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The item or items in this listing.
    """

    __resource_type__ = "InventoryReportInventoryListingItem"

    category: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="category",
        title="The inventory category or classification of the items being reported",
        description=(
            "The inventory category or classification of the items being reported. "
            "This is meant not for defining the product, but for inventory "
            "categories e.g. 'pending recount' or 'damaged'."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    item: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        ...,
        alias="item",
        title="The code or reference to the item type",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Medication",
                "Device",
                "Medication",
                "NutritionProduct",
                "InventoryItem",
                "BiologicallyDerivedProduct",
                "InventoryItem",
            ],
        },
    )

    quantity: fhirtypes.QuantityType = Field(  # type: ignore
        ...,
        alias="quantity",
        title="The quantity of the item or items being reported",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InventoryReportInventoryListingItem`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "category", "quantity", "item"]
