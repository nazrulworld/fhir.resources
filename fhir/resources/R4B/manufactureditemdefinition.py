from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ManufacturedItemDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
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
        title=(
            "Manufacturer of the item (Note that this should be named "
            '"manufacturer" but it currently causes technical issues)'
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
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
        title="The \u201creal world\u201d units in which the quantity of the item is described",
        description=(
            "The \u201creal world\u201d units in which the quantity of the manufactured item "
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
            "manufacturedDoseForm",
            "unitOfPresentation",
            "manufacturer",
            "ingredient",
            "property",
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
            "valueAttachment",
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
                "valueQuantity",
            ]
        }
        return one_of_many_fields
