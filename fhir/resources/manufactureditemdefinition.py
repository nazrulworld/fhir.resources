from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ManufacturedItemDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ManufacturedItemDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The definition and characteristics of a medicinal manufactured item, such
    as a tablet or capsule, as contained in a packaged medicinal product.
    """

    __resource_type__ = "ManufacturedItemDefinition"

    component: typing.List[fhirtypes.ManufacturedItemDefinitionComponentType] | None = Field(  # type: ignore
        None,
        alias="component",
        title=(
            "Physical parts of the manufactured item, that it is intrisically made "
            "from. This is distinct from the ingredients that are part of its "
            "chemical makeup"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique identifier",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    ingredient: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    manufacturedDoseForm: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="manufacturedDoseForm",
        title="Dose form as manufactured (before any necessary transformation)",
        description=(
            "Dose form as manufactured and before any transformation into the "
            "pharmaceutical product."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        None,
        alias="manufacturer",
        title="Manufacturer of the item, one of several possible",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    marketingStatus: typing.List[fhirtypes.MarketingStatusType] | None = Field(  # type: ignore
        None,
        alias="marketingStatus",
        title=(
            "Allows specifying that an item is on the market for sale, or that it "
            "is not available, and the dates and locations associated"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="A descriptive name applied to this item",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    property: typing.List[fhirtypes.ManufacturedItemDefinitionPropertyType] | None = Field(  # type: ignore
        None,
        alias="property",
        title="General characteristics of this item",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this item. Enables tracking the life-cycle of the "
            "content."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    unitOfPresentation: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        None,
        alias="unitOfPresentation",
        title="The \u201creal-world\u201d units in which the quantity of the item is described",
        description=(
            "The \u201creal-world\u201d units in which the quantity of the manufactured item "
            "is described."
        ),
        json_schema_extra={
            "element_property": True,
        },
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


class ManufacturedItemDefinitionComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Physical parts of the manufactured item, that it is intrisically made from.
    This is distinct from the ingredients that are part of its chemical makeup.
    """

    __resource_type__ = "ManufacturedItemDefinitionComponent"

    amount: typing.List[fhirtypes.QuantityType] | None = Field(  # type: ignore
        None,
        alias="amount",
        title=(
            "The measurable amount of total quantity of all substances in the "
            "component, expressable in different ways (e.g. by mass or volume)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    component: typing.List[fhirtypes.ManufacturedItemDefinitionComponentType] | None = Field(  # type: ignore
        None,
        alias="component",
        title="A component that this component contains or is made from",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    constituent: typing.List[fhirtypes.ManufacturedItemDefinitionComponentConstituentType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
    )

    function: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="function",
        title=(
            "The function of this component within the item e.g. delivers active "
            "ingredient, masks taste"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    property: typing.List[fhirtypes.ManufacturedItemDefinitionPropertyType] | None = Field(  # type: ignore
        None,
        alias="property",
        title="General characteristics of this component",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="Defining type of the component e.g. shell, layer, ink",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "ManufacturedItemDefinitionComponentConstituent"

    amount: typing.List[fhirtypes.QuantityType] | None = Field(  # type: ignore
        None,
        alias="amount",
        title=(
            "The measurable amount of the substance, expressable in different ways "
            "(e.g. by mass or volume)"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    function: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        None,
        alias="function",
        title="The function of this constituent within the component e.g. binder",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    hasIngredient: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        None,
        alias="hasIngredient",
        title="The ingredient that is the constituent of the given component",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Ingredient"],
        },
    )

    location: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
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
        json_schema_extra={
            "element_property": True,
        },
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

    __resource_type__ = "ManufacturedItemDefinitionProperty"

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="type",
        title="A code expressing the type of characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        None,
        alias="valueAttachment",
        title="A value for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        None,
        alias="valueBoolean",
        title="A value for the characteristic",
        description=None,
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
        title="A value for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDate: fhirtypes.DateType | None = Field(  # type: ignore
        None,
        alias="valueDate",
        title="A value for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueMarkdown: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="valueMarkdown",
        title="A value for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_valueMarkdown", title="Extension field for ``valueMarkdown``."
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="valueQuantity",
        title="A value for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        None,
        alias="valueReference",
        title="A value for the characteristic",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Binary"],
        },
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
                "valueBoolean",
                "valueCodeableConcept",
                "valueDate",
                "valueMarkdown",
                "valueQuantity",
                "valueReference",
            ]
        }
        return one_of_many_fields
