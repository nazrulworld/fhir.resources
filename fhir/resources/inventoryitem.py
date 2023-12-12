# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/InventoryItem
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


class InventoryItem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A functional description of an inventory item used in inventory and supply-
    related workflows.
    """

    resource_type = Field("InventoryItem", const=True)

    association: typing.List[fhirtypes.InventoryItemAssociationType] = Field(
        None,
        alias="association",
        title="Association with other items or products",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    baseUnit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="baseUnit",
        title=(
            "The base unit of measure - the unit in which the product is used or "
            "counted"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Category or class of the item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    characteristic: typing.List[fhirtypes.InventoryItemCharacteristicType] = Field(
        None,
        alias="characteristic",
        title="Characteristic of the item",
        description="The descriptive or identifying characteristics of the item.",
        # if property is element of this resource.
        element_property=True,
    )

    code: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="Code designating the specific type of item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.InventoryItemDescriptionType = Field(
        None,
        alias="description",
        title="Descriptive characteristics of the item",
        description="The descriptive characteristics of the inventory item.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for the inventory item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    instance: fhirtypes.InventoryItemInstanceType = Field(
        None,
        alias="instance",
        title="Instances or occurrences of the product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    inventoryStatus: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="inventoryStatus",
        title="The usage status like recalled, in use, discarded",
        description=(
            "The usage status e.g. recalled, in use, discarded... This can be used "
            "to indicate that the items have been taken out of inventory, or are in"
            " use, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: typing.List[fhirtypes.InventoryItemNameType] = Field(
        None,
        alias="name",
        title=(
            "The item name(s) - the brand name, or common name, functional name, "
            "generic name or others"
        ),
        description=(
            "The item name(s) - the brand name, or common name, functional name, "
            "generic name."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    netContent: fhirtypes.QuantityType = Field(
        None,
        alias="netContent",
        title="Net content or amount present in the item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    productReference: fhirtypes.ReferenceType = Field(
        None,
        alias="productReference",
        title="Link to a product resource used in clinical workflows",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Medication",
            "Device",
            "NutritionProduct",
            "BiologicallyDerivedProduct",
        ],
    )

    responsibleOrganization: typing.List[
        fhirtypes.InventoryItemResponsibleOrganizationType
    ] = Field(
        None,
        alias="responsibleOrganization",
        title="Organization(s) responsible for the product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | inactive | entered-in-error | unknown",
        description="Status of the item entry.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "inactive", "entered-in-error", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InventoryItem`` according specification,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1555(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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


class InventoryItemAssociation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Association with other items or products.
    """

    resource_type = Field("InventoryItemAssociation", const=True)

    associationType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="associationType",
        title="The type of association between the device and the other item",
        description=(
            "This attribute defined the type of association when establishing "
            "associations or relations between items, e.g. 'packaged within' or "
            "'used with' or 'to be mixed with."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.RatioType = Field(
        ...,
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
        # if property is element of this resource.
        element_property=True,
    )

    relatedItem: fhirtypes.ReferenceType = Field(
        ...,
        alias="relatedItem",
        title="The related item or product",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "InventoryItem",
            "Medication",
            "MedicationKnowledge",
            "Device",
            "DeviceDefinition",
            "NutritionProduct",
            "BiologicallyDerivedProduct",
        ],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InventoryItemAssociation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "associationType",
            "relatedItem",
            "quantity",
        ]


class InventoryItemCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Characteristic of the item.
    The descriptive or identifying characteristics of the item.
    """

    resource_type = Field("InventoryItemCharacteristic", const=True)

    characteristicType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="characteristicType",
        title="The characteristic that is being defined",
        description="The type of characteristic that is being defined.",
        # if property is element of this resource.
        element_property=True,
    )

    valueAddress: fhirtypes.AddressType = Field(
        None,
        alias="valueAddress",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="valueAnnotation",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueDuration: fhirtypes.DurationType = Field(
        None,
        alias="valueDuration",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueUrl: fhirtypes.Url = Field(
        None,
        alias="valueUrl",
        title="The value of the attribute",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUrl", title="Extension field for ``valueUrl``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InventoryItemCharacteristic`` according specification,
        with preserving original sequence order.
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2994(
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


class InventoryItemDescription(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Descriptive characteristics of the item.
    The descriptive characteristics of the inventory item.
    """

    resource_type = Field("InventoryItemDescription", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Textual description of the item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="The language that is used in the item description",
        description=(
            "The language for the item description, when an item must be described "
            "in different languages and those languages may be authoritative and "
            "not translations of a 'main' language."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InventoryItemDescription`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "language", "description"]


class InventoryItemInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Instances or occurrences of the product.
    """

    resource_type = Field("InventoryItemInstance", const=True)

    expiry: fhirtypes.DateTime = Field(
        None,
        alias="expiry",
        title="The expiry date or date and time for the product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    expiry__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expiry", title="Extension field for ``expiry``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="The identifier for the physical instance, typically a serial number",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="The location that the item is associated with",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    lotNumber: fhirtypes.String = Field(
        None,
        alias="lotNumber",
        title="The lot or batch number of the item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lotNumber", title="Extension field for ``lotNumber``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="The subject that the item is associated with",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Organization"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InventoryItemInstance`` according specification,
        with preserving original sequence order.
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


class InventoryItemName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The item name(s) - the brand name, or common name, functional name, generic
    name or others.
    The item name(s) - the brand name, or common name, functional name, generic
    name.
    """

    resource_type = Field("InventoryItemName", const=True)

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="The language used to express the item name",
        description="The language that the item name is expressed in.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="The name or designation of the item",
        description="The name or designation that the item is given.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    nameType: fhirtypes.CodingType = Field(
        ...,
        alias="nameType",
        title="The type of name e.g. 'brand-name', 'functional-name', 'common-name'",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InventoryItemName`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "nameType", "language", "name"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1932(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("language", "language__ext"), ("name", "name__ext")]
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


class InventoryItemResponsibleOrganization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Organization(s) responsible for the product.
    """

    resource_type = Field("InventoryItemResponsibleOrganization", const=True)

    organization: fhirtypes.ReferenceType = Field(
        ...,
        alias="organization",
        title="An organization that is associated with the item",
        description=(
            "An organization that has an association with the item, e.g. "
            "manufacturer, distributor, responsible, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="The role of the organization e.g. manufacturer, distributor, or other",
        description="The role of the organization e.g. manufacturer, distributor, etc.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``InventoryItemResponsibleOrganization`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "role", "organization"]
