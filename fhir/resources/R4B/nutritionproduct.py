# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NutritionProduct
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class NutritionProduct(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A product used for nutritional purposes.
    A food or fluid product that is consumed by patients.
    """

    resource_type = Field("NutritionProduct", const=True)

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title=(
            "A category or class of the nutrition product (halal, kosher, gluten "
            "free, vegan, etc)"
        ),
        description=(
            "Nutrition products can have different classifications - according to "
            "its nutritional properties, preparation methods, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="A code designating a specific type of nutritional product",
        description=(
            "The code assigned to the product, for example a manufacturer number or"
            " other terminology."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    ingredient: typing.List[fhirtypes.NutritionProductIngredientType] = Field(
        None,
        alias="ingredient",
        title="Ingredients contained in this product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    instance: fhirtypes.NutritionProductInstanceType = Field(
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
        # if property is element of this resource.
        element_property=True,
    )

    knownAllergen: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="knownAllergen",
        title="Known or suspected allergens that are a part of this product",
        description=(
            "Allergens that are known or suspected to be a part of this nutrition "
            "product."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title="Manufacturer, representative or officially responsible for the product",
        description=(
            "The organisation (manufacturer, representative or legal authorisation "
            "holder) that is responsible for the device."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about the product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    nutrient: typing.List[fhirtypes.NutritionProductNutrientType] = Field(
        None,
        alias="nutrient",
        title="The product's nutritional information expressed by the nutrients",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    productCharacteristic: typing.List[
        fhirtypes.NutritionProductProductCharacteristicType
    ] = Field(
        None,
        alias="productCharacteristic",
        title="Specifies descriptive properties of the nutrition product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description="The current state of the product.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "inactive", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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
            "status",
            "category",
            "code",
            "manufacturer",
            "nutrient",
            "ingredient",
            "knownAllergen",
            "productCharacteristic",
            "instance",
            "note",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1903(
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


class NutritionProductIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Ingredients contained in this product.
    """

    resource_type = Field("NutritionProductIngredient", const=True)

    amount: typing.List[fhirtypes.RatioType] = Field(
        None,
        alias="amount",
        title="The amount of ingredient that is in the product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    item: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="item",
        title="The ingredient contained in the product",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["NutritionProduct"],
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

    resource_type = Field("NutritionProductInstance", const=True)

    expiry: fhirtypes.DateTime = Field(
        None,
        alias="expiry",
        title="The expiry date or date and time for the product",
        description=(
            "The time after which the product is no longer expected to be in proper"
            " condition, or its use is not advised or not allowed."
        ),
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

    lotNumber: fhirtypes.String = Field(
        None,
        alias="lotNumber",
        title="The identification of the batch or lot of the product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lotNumber", title="Extension field for ``lotNumber``."
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="The amount of items or instances",
        description=(
            "The amount of items or instances that the resource considers, for "
            "instance when referring to 2 identical units together."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    useBy: fhirtypes.DateTime = Field(
        None,
        alias="useBy",
        title=(
            "The date until which the product is expected to be good for " "consumption"
        ),
        description=(
            "The time after which the product is no longer expected to be in proper"
            " condition, or its use is not advised or not allowed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    useBy__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
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
            "lotNumber",
            "expiry",
            "useBy",
        ]


class NutritionProductNutrient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The product's nutritional information expressed by the nutrients.
    """

    resource_type = Field("NutritionProductNutrient", const=True)

    amount: typing.List[fhirtypes.RatioType] = Field(
        None,
        alias="amount",
        title=(
            "The amount of nutrient expressed in one or more units: X per pack / "
            "per serving / per dose"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    item: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="item",
        title="The (relevant) nutrients in the product",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionProductNutrient`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "item", "amount"]


class NutritionProductProductCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specifies descriptive properties of the nutrition product.
    """

    resource_type = Field("NutritionProductProductCharacteristic", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Code specifying the type of characteristic",
        description=(
            "A code specifying which characteristic of the product is being "
            "described (for example, colour, shape)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueBase64Binary: fhirtypes.Base64Binary = Field(
        None,
        alias="valueBase64Binary",
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_valueBase64Binary",
        title="Extension field for ``valueBase64Binary``.",
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
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
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="The value of the characteristic",
        description="The actual characteristic value corresponding to the type.",
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``NutritionProductProductCharacteristic`` according specification,
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4072(
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
                "valueAttachment",
                "valueBase64Binary",
                "valueBoolean",
                "valueCodeableConcept",
                "valueQuantity",
                "valueString",
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
