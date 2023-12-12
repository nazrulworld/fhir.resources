# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/InventoryReport
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class InventoryReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A report of inventory or stock items.
    """

    resource_type = Field("InventoryReport", const=True)

    countType: fhirtypes.Code = Field(
        None,
        alias="countType",
        title="snapshot | difference",
        description=(
            "Whether the report is about the current inventory count (snapshot) or "
            "a differential change in inventory (change)."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["snapshot", "difference"],
    )
    countType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_countType", title="Extension field for ``countType``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for the report",
        description="Business identifier for the InventoryReport.",
        # if property is element of this resource.
        element_property=True,
    )

    inventoryListing: typing.List[
        fhirtypes.InventoryReportInventoryListingType
    ] = Field(
        None,
        alias="inventoryListing",
        title="An inventory listing section (grouped by any of the attributes)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="A note associated with the InventoryReport",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    operationType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="operationType",
        title="addition | subtraction",
        description="What type of operation is being performed - addition or subtraction.",
        # if property is element of this resource.
        element_property=True,
    )

    operationTypeReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="operationTypeReason",
        title=(
            "The reason for this count - regular count, ad-hoc count, new arrivals,"
            " etc"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    reportedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="reportedDateTime",
        title="When the report has been submitted",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    reportedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_reportedDateTime",
        title="Extension field for ``reportedDateTime``.",
    )

    reporter: fhirtypes.ReferenceType = Field(
        None,
        alias="reporter",
        title="Who submits the report",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Patient", "RelatedPerson", "Device"],
    )

    reportingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="reportingPeriod",
        title="The period the report refers to",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | requested | active | entered-in-error",
        description=(
            "The status of the inventory check or notification - whether this is "
            "draft (e.g. the report is still pending some updates) or active."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "requested", "active", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1799(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class InventoryReportInventoryListing(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An inventory listing section (grouped by any of the attributes).
    """

    resource_type = Field("InventoryReportInventoryListing", const=True)

    countingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="countingDateTime",
        title="The date and time when the items were counted",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    countingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_countingDateTime",
        title="Extension field for ``countingDateTime``.",
    )

    item: typing.List[fhirtypes.InventoryReportInventoryListingItemType] = Field(
        None,
        alias="item",
        title="The item or items in this listing",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    itemStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemStatus",
        title="The status of the items that are being reported",
        description="The status of the items.",
        # if property is element of this resource.
        element_property=True,
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Location of the inventory items",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
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

    resource_type = Field("InventoryReportInventoryListingItem", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="The inventory category or classification of the items being reported",
        description=(
            "The inventory category or classification of the items being reported. "
            "This is meant not for defining the product, but for inventory "
            "categories e.g. 'pending recount' or 'damaged'."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    item: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="item",
        title="The code or reference to the item type",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Medication",
            "Device",
            "Medication",
            "NutritionProduct",
            "InventoryItem",
            "BiologicallyDerivedProduct",
            "InventoryItem",
        ],
    )

    quantity: fhirtypes.QuantityType = Field(
        ...,
        alias="quantity",
        title="The quantity of the item or items being reported",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InventoryReportInventoryListingItem`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "category", "quantity", "item"]
