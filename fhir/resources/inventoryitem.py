from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/InventoryItem
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class InventoryItem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A functional description of an inventory item used in inventory and supply-
    related workflows.
    """

    __resource_type__ = "InventoryItem"

    association: typing.List[fhirtypes.InventoryItemAssociationType] | None = Field(  # type: ignore
        default=None,
        alias="association",
        title="Association with other items or products",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    baseUnit: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="baseUnit",
        title=(
            "The base unit of measure - the unit in which the product is used or "
            "counted"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="category",
        title="Category or class of the item",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    characteristic: typing.List[fhirtypes.InventoryItemCharacteristicType] | None = Field(  # type: ignore
        default=None,
        alias="characteristic",
        title="Characteristic of the item",
        description="The descriptive or identifying characteristics of the item.",
        json_schema_extra={
            "element_property": True,
        },
    )

    code: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="code",
        title="Code designating the specific type of item",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    description: fhirtypes.InventoryItemDescriptionType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Descriptive characteristics of the item",
        description="The descriptive characteristics of the inventory item.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Business identifier for the inventory item",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    instance: fhirtypes.InventoryItemInstanceType | None = Field(  # type: ignore
        default=None,
        alias="instance",
        title="Instances or occurrences of the product",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    inventoryStatus: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="inventoryStatus",
        title="The usage status like recalled, in use, discarded",
        description=(
            "The usage status e.g. recalled, in use, discarded... This can be used "
            "to indicate that the items have been taken out of inventory, or are in"
            " use, etc."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    name: typing.List[fhirtypes.InventoryItemNameType] | None = Field(  # type: ignore
        default=None,
        alias="name",
        title=(
            "The item name(s) - the brand name, or common name, functional name, "
            "generic name or others"
        ),
        description=(
            "The item name(s) - the brand name, or common name, functional name, "
            "generic name."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    netContent: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="netContent",
        title="Net content or amount present in the item",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    productReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="productReference",
        title="Link to a product resource used in clinical workflows",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Medication",
                "Device",
                "NutritionProduct",
                "BiologicallyDerivedProduct",
            ],
        },
    )

    responsibleOrganization: typing.List[fhirtypes.InventoryItemResponsibleOrganizationType] | None = Field(  # type: ignore
        default=None,
        alias="responsibleOrganization",
        title="Organization(s) responsible for the product",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="active | inactive | entered-in-error | unknown",
        description="Status of the item entry.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "inactive", "entered-in-error", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``InventoryItem`` according to specification,
        with preserving the original sequence order.
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
            "code",
            "name",
            "responsibleOrganization",
            "description",
            "inventoryStatus",
            "baseUnit",
            "netContent",
            "association",
            "characteristic",
            "instance",
            "productReference",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``InventoryItem`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "modifierExtension",
            "identifier",
            "status",
            "category",
            "code",
            "name",
            "inventoryStatus",
            "baseUnit",
            "netContent",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class InventoryItemAssociation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Association with other items or products.
    """

    __resource_type__ = "InventoryItemAssociation"

    associationType: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="associationType",
        title="The type of association between the device and the other item",
        description=(
            "This attribute defined the type of association when establishing "
            "associations or relations between items, e.g. 'packaged within' or "
            "'used with' or 'to be mixed with."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    quantity: fhirtypes.RatioType = Field(  # type: ignore
        default=...,
        alias="quantity",
        title="The quantity of the product in this product",
        description=(
            "The quantity of the related product in this product - Numerator is the"
            " quantity of the related product. Denominator is the quantity of the "
            "present product. For example a value of 20 means that this product "
            "contains 20 units of the related product; a value of 1:20 means the "
            "inverse - that the contained product contains 20 units of the present "
            "product."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    relatedItem: fhirtypes.ReferenceType = Field(  # type: ignore
        default=...,
        alias="relatedItem",
        title="The related item or product",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "InventoryItem",
                "Medication",
                "MedicationKnowledge",
                "Device",
                "DeviceDefinition",
                "NutritionProduct",
                "BiologicallyDerivedProduct",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``InventoryItemAssociation`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "associationType",
            "relatedItem",
            "quantity",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``InventoryItemAssociation`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "associationType", "relatedItem", "quantity"]


class InventoryItemCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Characteristic of the item.
    The descriptive or identifying characteristics of the item.
    """

    __resource_type__ = "InventoryItemCharacteristic"

    characteristicType: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="characteristicType",
        title="The characteristic that is being defined",
        description="The type of characteristic that is being defined.",
        json_schema_extra={
            "element_property": True,
        },
    )

    valueAddress: fhirtypes.AddressType | None = Field(  # type: ignore
        default=None,
        alias="valueAddress",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueAnnotation: fhirtypes.AnnotationType | None = Field(  # type: ignore
        default=None,
        alias="valueAnnotation",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        default=None,
        alias="valueBoolean",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_valueBoolean",
        title="Extension field for ``valueBoolean``.",
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="valueCodeableConcept",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="valueDateTime",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_valueDateTime",
        title="Extension field for ``valueDateTime``.",
    )

    valueDecimal: fhirtypes.DecimalType | None = Field(  # type: ignore
        default=None,
        alias="valueDecimal",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_valueDecimal",
        title="Extension field for ``valueDecimal``.",
    )

    valueDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        default=None,
        alias="valueDuration",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueInteger: fhirtypes.IntegerType | None = Field(  # type: ignore
        default=None,
        alias="valueInteger",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_valueInteger",
        title="Extension field for ``valueInteger``.",
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="valueQuantity",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        default=None,
        alias="valueRange",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        default=None,
        alias="valueRatio",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="valueString",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueUrl: fhirtypes.UrlType | None = Field(  # type: ignore
        default=None,
        alias="valueUrl",
        title="The value of the attribute",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_valueUrl", title="Extension field for ``valueUrl``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``InventoryItemCharacteristic`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "characteristicType",
            "valueString",
            "valueInteger",
            "valueDecimal",
            "valueBoolean",
            "valueUrl",
            "valueDateTime",
            "valueQuantity",
            "valueRange",
            "valueRatio",
            "valueAnnotation",
            "valueAddress",
            "valueDuration",
            "valueCodeableConcept",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``InventoryItemCharacteristic`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

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
                "valueAddress",
                "valueAnnotation",
                "valueBoolean",
                "valueCodeableConcept",
                "valueDateTime",
                "valueDecimal",
                "valueDuration",
                "valueInteger",
                "valueQuantity",
                "valueRange",
                "valueRatio",
                "valueString",
                "valueUrl",
            ]
        }
        return one_of_many_fields


class InventoryItemDescription(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Descriptive characteristics of the item.
    The descriptive characteristics of the inventory item.
    """

    __resource_type__ = "InventoryItemDescription"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Textual description of the item",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    language: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="language",
        title="The language that is used in the item description",
        description=(
            "The language for the item description, when an item must be described "
            "in different languages and those languages may be authoritative and "
            "not translations of a 'main' language."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_language", title="Extension field for ``language``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``InventoryItemDescription`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "description"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``InventoryItemDescription`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]


class InventoryItemInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Instances or occurrences of the product.
    """

    __resource_type__ = "InventoryItemInstance"

    expiry: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="expiry",
        title="The expiry date or date and time for the product",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    expiry__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_expiry", title="Extension field for ``expiry``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="The identifier for the physical instance, typically a serial number",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="location",
        title="The location that the item is associated with",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    lotNumber: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="lotNumber",
        title="The lot or batch number of the item",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_lotNumber", title="Extension field for ``lotNumber``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="subject",
        title="The subject that the item is associated with",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Organization"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``InventoryItemInstance`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "lotNumber",
            "expiry",
            "subject",
            "location",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``InventoryItemInstance`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]


class InventoryItemName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The item name(s) - the brand name, or common name, functional name, generic
    name or others.
    The item name(s) - the brand name, or common name, functional name, generic
    name.
    """

    __resource_type__ = "InventoryItemName"

    language: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="language",
        title="The language used to express the item name",
        description="The language that the item name is expressed in.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
        },
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_language", title="Extension field for ``language``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="The name or designation of the item",
        description="The name or designation that the item is given.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    nameType: fhirtypes.CodingType = Field(  # type: ignore
        default=...,
        alias="nameType",
        title="The type of name e.g. 'brand-name', 'functional-name', 'common-name'",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``InventoryItemName`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "nameType", "language", "name"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``InventoryItemName`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "nameType", "language", "name"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("language", "language__ext"), ("name", "name__ext")]
        return required_fields


class InventoryItemResponsibleOrganization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Organization(s) responsible for the product.
    """

    __resource_type__ = "InventoryItemResponsibleOrganization"

    organization: fhirtypes.ReferenceType = Field(  # type: ignore
        default=...,
        alias="organization",
        title="An organization that is associated with the item",
        description=(
            "An organization that has an association with the item, e.g. "
            "manufacturer, distributor, responsible, etc."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    role: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="role",
        title="The role of the organization e.g. manufacturer, distributor, or other",
        description="The role of the organization e.g. manufacturer, distributor, etc.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``InventoryItemResponsibleOrganization`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "role", "organization"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``InventoryItemResponsibleOrganization`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]
