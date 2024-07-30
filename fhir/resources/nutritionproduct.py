# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NutritionProduct
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class NutritionProduct(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A product used for nutritional purposes (i.e. food or supplement).
    A food or supplement that is consumed by patients.
    """

    __resource_type__ = "NutritionProduct"

    category: typing.List[fhirtypes.CodeableConceptType] = Field(  # type: ignore
        None,
        alias="category",
        title=(
            "Broad product groups or categories used to classify the product, such "
            "as Legume and Legume Products, Beverages, or Beef Products"
        ),
        description=(
            "Nutrition products can have different classifications - according to "
            "its nutritional properties, preparation methods, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    characteristic: typing.List[fhirtypes.NutritionProductCharacteristicType] = Field(  # type: ignore
        None,
        alias="characteristic",
        title="Specifies descriptive properties of the nutrition product",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="code",
        title=(
            "A code that can identify the detailed nutrients and ingredients in a "
            "specific food product"
        ),
        description=(
            "The code assigned to the product, for example a USDA NDB number, a "
            "USDA FDC ID number, or a Langual code."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    ingredient: typing.List[fhirtypes.NutritionProductIngredientType] = Field(  # type: ignore
        None,
        alias="ingredient",
        title="Ingredients contained in this product",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    instance: typing.List[fhirtypes.NutritionProductInstanceType] = Field(  # type: ignore
        None,
        alias="instance",
        title=(
            "One or several physical instances or occurrences of the nutrition "
            "product"
        ),
        description=(
            "Conveys instance-level information about this product item. One or "
            "several physical, countable instances or occurrences of the product."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    knownAllergen: typing.List[fhirtypes.CodeableReferenceType] = Field(  # type: ignore
        None,
        alias="knownAllergen",
        title="Known or suspected allergens that are a part of this product",
        description=(
            "Allergens that are known or suspected to be a part of this nutrition "
            "product."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Substance"],
        },
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        None,
        alias="manufacturer",
        title="Manufacturer, representative or officially responsible for the product",
        description=(
            "The organisation (manufacturer, representative or legal authorization "
            "holder) that is responsible for the device."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(  # type: ignore
        None,
        alias="note",
        title="Comments made about the product",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    nutrient: typing.List[fhirtypes.NutritionProductNutrientType] = Field(  # type: ignore
        None,
        alias="nutrient",
        title="The product's nutritional information expressed by the nutrients",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description="The current state of the product.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "inactive", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionProduct`` according specification,
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
            "code",
            "status",
            "category",
            "manufacturer",
            "nutrient",
            "ingredient",
            "knownAllergen",
            "characteristic",
            "instance",
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
        required_fields = [("status", "status__ext")]
        return required_fields


class NutritionProductCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifies descriptive properties of the nutrition product.
    """

    __resource_type__ = "NutritionProductCharacteristic"

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Code specifying the type of characteristic",
        description=(
            "A code specifying which characteristic of the product is being "
            "described (for example, colour, shape)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    valueAttachment: fhirtypes.AttachmentType = Field(  # type: ignore
        None,
        alias="valueAttachment",
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueBase64Binary: fhirtypes.Base64BinaryType = Field(  # type: ignore
        None,
        alias="valueBase64Binary",
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None,
        alias="_valueBase64Binary",
        title="Extension field for ``valueBase64Binary``.",
    )

    valueBoolean: bool = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="valueCodeableConcept",
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueQuantity: fhirtypes.QuantityType = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueString: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="valueString",
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionProductCharacteristic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueCodeableConcept",
            "valueString",
            "valueQuantity",
            "valueBase64Binary",
            "valueAttachment",
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
                "valueAttachment",
                "valueBase64Binary",
                "valueBoolean",
                "valueCodeableConcept",
                "valueQuantity",
                "valueString",
            ]
        }
        return one_of_many_fields


class NutritionProductIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Ingredients contained in this product.
    """

    __resource_type__ = "NutritionProductIngredient"

    amount: typing.List[fhirtypes.RatioType] = Field(  # type: ignore
        None,
        alias="amount",
        title="The amount of ingredient that is in the product",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    item: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        ...,
        alias="item",
        title="The ingredient contained in the product",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["NutritionProduct"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionProductIngredient`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "item", "amount"]


class NutritionProductInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    One or several physical instances or occurrences of the nutrition product.
    Conveys instance-level information about this product item. One or several
    physical, countable instances or occurrences of the product.
    """

    __resource_type__ = "NutritionProductInstance"

    biologicalSourceEvent: fhirtypes.IdentifierType = Field(  # type: ignore
        None,
        alias="biologicalSourceEvent",
        title=(
            "An identifier that supports traceability to the event during which "
            "material in this product from one or more biological entities was "
            "obtained or pooled"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    expiry: fhirtypes.DateTimeType = Field(  # type: ignore
        None,
        alias="expiry",
        title="The expiry date or date and time for the product",
        description=(
            "The time after which the product is no longer expected to be in proper"
            " condition, or its use is not advised or not allowed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    expiry__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_expiry", title="Extension field for ``expiry``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(  # type: ignore
        None,
        alias="identifier",
        title=(
            "The identifier for the physical instance, typically a serial number or"
            " manufacturer number"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    lotNumber: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="lotNumber",
        title="The identification of the batch or lot of the product",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_lotNumber", title="Extension field for ``lotNumber``."
    )

    name: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="name",
        title="The name for the specific product",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    quantity: fhirtypes.QuantityType = Field(  # type: ignore
        None,
        alias="quantity",
        title="The amount of items or instances",
        description=(
            "The amount of items or instances that the resource considers, for "
            "instance when referring to 2 identical units together."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    useBy: fhirtypes.DateTimeType = Field(  # type: ignore
        None,
        alias="useBy",
        title=(
            "The date until which the product is expected to be good for " "consumption"
        ),
        description=(
            "The time after which the product is no longer expected to be in proper"
            " condition, or its use is not advised or not allowed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    useBy__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_useBy", title="Extension field for ``useBy``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionProductInstance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "quantity",
            "identifier",
            "name",
            "lotNumber",
            "expiry",
            "useBy",
            "biologicalSourceEvent",
        ]


class NutritionProductNutrient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The product's nutritional information expressed by the nutrients.
    """

    __resource_type__ = "NutritionProductNutrient"

    amount: typing.List[fhirtypes.RatioType] = Field(  # type: ignore
        None,
        alias="amount",
        title=(
            "The amount of nutrient expressed in one or more units: X per pack / "
            "per serving / per dose"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    item: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        None,
        alias="item",
        title="The (relevant) nutrients in the product",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Substance"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionProductNutrient`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "item", "amount"]
