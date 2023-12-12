# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ManufacturedItemDefinition
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


class ManufacturedItemDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The definition and characteristics of a medicinal manufactured item, such
    as a tablet or capsule, as contained in a packaged medicinal product.
    """

    resource_type = Field("ManufacturedItemDefinition", const=True)

    component: typing.List[fhirtypes.ManufacturedItemDefinitionComponentType] = Field(
        None,
        alias="component",
        title=(
            "Physical parts of the manufactured item, that it is intrisically made "
            "from. This is distinct from the ingredients that are part of its "
            "chemical makeup"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    ingredient: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="ingredient",
        title=(
            "The ingredients of this manufactured item. Only needed if these are "
            "not specified by incoming references from the Ingredient resource"
        ),
        description=(
            "The ingredients of this manufactured item. This is only needed if the "
            "ingredients are not specified by incoming references from the "
            "Ingredient resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    manufacturedDoseForm: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="manufacturedDoseForm",
        title="Dose form as manufactured (before any necessary transformation)",
        description=(
            "Dose form as manufactured and before any transformation into the "
            "pharmaceutical product."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title="Manufacturer of the item, one of several possible",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    marketingStatus: typing.List[fhirtypes.MarketingStatusType] = Field(
        None,
        alias="marketingStatus",
        title=(
            "Allows specifying that an item is on the market for sale, or that it "
            "is not available, and the dates and locations associated"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="A descriptive name applied to this item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    property: typing.List[fhirtypes.ManufacturedItemDefinitionPropertyType] = Field(
        None,
        alias="property",
        title="General characteristics of this item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this item. Enables tracking the life-cycle of the "
            "content."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    unitOfPresentation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unitOfPresentation",
        title="The \u201creal-world\u201d units in which the quantity of the item is described",
        description=(
            "The \u201creal-world\u201d units in which the quantity of the manufactured item "
            "is described."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ManufacturedItemDefinition`` according specification,
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
            "name",
            "manufacturedDoseForm",
            "unitOfPresentation",
            "manufacturer",
            "marketingStatus",
            "ingredient",
            "property",
            "component",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2866(
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


class ManufacturedItemDefinitionComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Physical parts of the manufactured item, that it is intrisically made from.
    This is distinct from the ingredients that are part of its chemical makeup.
    """

    resource_type = Field("ManufacturedItemDefinitionComponent", const=True)

    amount: typing.List[fhirtypes.QuantityType] = Field(
        None,
        alias="amount",
        title=(
            "The measurable amount of total quantity of all substances in the "
            "component, expressable in different ways (e.g. by mass or volume)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    component: typing.List[fhirtypes.ManufacturedItemDefinitionComponentType] = Field(
        None,
        alias="component",
        title="A component that this component contains or is made from",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    constituent: typing.List[
        fhirtypes.ManufacturedItemDefinitionComponentConstituentType
    ] = Field(
        None,
        alias="constituent",
        title=(
            "A reference to a constituent of the manufactured item as a whole, "
            "linked here so that its component location within the item can be "
            "indicated. This not where the item's ingredient are primarily stated "
            "(for which see Ingredient.for or "
            "ManufacturedItemDefinition.ingredient)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    function: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="function",
        title=(
            "The function of this component within the item e.g. delivers active "
            "ingredient, masks taste"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    property: typing.List[fhirtypes.ManufacturedItemDefinitionPropertyType] = Field(
        None,
        alias="property",
        title="General characteristics of this component",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Defining type of the component e.g. shell, layer, ink",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ManufacturedItemDefinitionComponent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "function",
            "amount",
            "constituent",
            "property",
            "component",
        ]


class ManufacturedItemDefinitionComponentConstituent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A reference to a constituent of the manufactured item as a whole, linked
    here so that its component location within the item can be indicated. This
    not where the item's ingredient are primarily stated (for which see
    Ingredient.for or ManufacturedItemDefinition.ingredient).
    """

    resource_type = Field("ManufacturedItemDefinitionComponentConstituent", const=True)

    amount: typing.List[fhirtypes.QuantityType] = Field(
        None,
        alias="amount",
        title=(
            "The measurable amount of the substance, expressable in different ways "
            "(e.g. by mass or volume)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    function: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="function",
        title="The function of this constituent within the component e.g. binder",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    hasIngredient: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="hasIngredient",
        title="The ingredient that is the constituent of the given component",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Ingredient"],
    )

    location: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="location",
        title=(
            "The physical location of the constituent/ingredient within the "
            "component"
        ),
        description=(
            "The physical location of the constituent/ingredient within the "
            "component. Example \u2013 if the component is the bead in the capsule, then"
            " the location would be where the ingredient resides within the product"
            " part \u2013 intragranular, extra-granular, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ManufacturedItemDefinitionComponentConstituent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "amount",
            "location",
            "function",
            "hasIngredient",
        ]


class ManufacturedItemDefinitionProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    General characteristics of this item.
    """

    resource_type = Field("ManufacturedItemDefinitionProperty", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="A code expressing the type of characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueMarkdown: fhirtypes.Markdown = Field(
        None,
        alias="valueMarkdown",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueMarkdown", title="Extension field for ``valueMarkdown``."
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Binary"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ManufacturedItemDefinitionProperty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueCodeableConcept",
            "valueQuantity",
            "valueDate",
            "valueBoolean",
            "valueMarkdown",
            "valueAttachment",
            "valueReference",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_3746(
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
                "valueBoolean",
                "valueCodeableConcept",
                "valueDate",
                "valueMarkdown",
                "valueQuantity",
                "valueReference",
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
