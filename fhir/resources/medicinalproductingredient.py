# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MedicinalProductIngredient(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An ingredient of a manufactured item or pharmaceutical product.
    """

    resource_type = Field("MedicinalProductIngredient", const=True)

    allergenicIndicator: bool = Field(
        None,
        alias="allergenicIndicator",
        title="If the ingredient is a known or suspected allergen",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_allergenicIndicator",
        title="Extension field for ``allergenicIndicator``.",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier for the ingredient",
        description=(
            "The identifier(s) of this Ingredient that are assigned by business "
            "processes and/or used to refer to it when a direct URL reference to "
            "the resource itself is not appropriate."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title="Manufacturer of this Ingredient",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="Ingredient role e.g. Active ingredient, excipient",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    specifiedSubstance: typing.List[
        fhirtypes.MedicinalProductIngredientSpecifiedSubstanceType
    ] = Field(
        None,
        alias="specifiedSubstance",
        title="A specified substance that comprises this ingredient",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    substance: fhirtypes.MedicinalProductIngredientSubstanceType = Field(
        None,
        alias="substance",
        title="The ingredient substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class MedicinalProductIngredientSpecifiedSubstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A specified substance that comprises this ingredient.
    """

    resource_type = Field("MedicinalProductIngredientSpecifiedSubstance", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="The specified substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    confidentiality: fhirtypes.CodeableConceptType = Field(
        None,
        alias="confidentiality",
        title="Confidentiality level of the specified substance as the ingredient",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    group: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="group",
        title="The group of specified substance, e.g. group 1 to 4",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    strength: typing.List[
        fhirtypes.MedicinalProductIngredientSpecifiedSubstanceStrengthType
    ] = Field(
        None,
        alias="strength",
        title=(
            "Quantity of the substance or specified substance present in the "
            "manufactured item or pharmaceutical product"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class MedicinalProductIngredientSpecifiedSubstanceStrength(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Quantity of the substance or specified substance present in the
    manufactured item or pharmaceutical product.
    """

    resource_type = Field(
        "MedicinalProductIngredientSpecifiedSubstanceStrength", const=True
    )

    concentration: fhirtypes.RatioType = Field(
        None,
        alias="concentration",
        title="The strength per unitary volume (or mass)",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    concentrationLowLimit: fhirtypes.RatioType = Field(
        None,
        alias="concentrationLowLimit",
        title=(
            "A lower limit for the strength per unitary volume (or mass), for when "
            "there is a range. The concentration attribute then becomes the upper "
            "limit"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    country: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="country",
        title="The country or countries for which the strength range applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    measurementPoint: fhirtypes.String = Field(
        None,
        alias="measurementPoint",
        title="For when strength is measured at a particular point or distance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_measurementPoint",
        title="Extension field for ``measurementPoint``.",
    )

    presentation: fhirtypes.RatioType = Field(
        ...,
        alias="presentation",
        title=(
            "The quantity of substance in the unit of presentation, or in the "
            "volume (or mass) of the single pharmaceutical product or manufactured "
            "item"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    presentationLowLimit: fhirtypes.RatioType = Field(
        None,
        alias="presentationLowLimit",
        title=(
            "A lower limit for the quantity of substance in the unit of "
            "presentation. For use when there is a range of strengths, this is the "
            "lower limit, with the presentation attribute becoming the upper limit"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    referenceStrength: typing.List[
        fhirtypes.MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrengthType
    ] = Field(
        None,
        alias="referenceStrength",
        title="Strength expressed in terms of a reference substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Strength expressed in terms of a reference substance.
    """

    resource_type = Field(
        "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength",
        const=True,
    )

    country: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="country",
        title="The country or countries for which the strength range applies",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    measurementPoint: fhirtypes.String = Field(
        None,
        alias="measurementPoint",
        title="For when strength is measured at a particular point or distance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_measurementPoint",
        title="Extension field for ``measurementPoint``.",
    )

    strength: fhirtypes.RatioType = Field(
        ...,
        alias="strength",
        title="Strength expressed in terms of a reference substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    strengthLowLimit: fhirtypes.RatioType = Field(
        None,
        alias="strengthLowLimit",
        title="Strength expressed in terms of a reference substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    substance: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substance",
        title="Relevant reference substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class MedicinalProductIngredientSubstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The ingredient substance.
    """

    resource_type = Field("MedicinalProductIngredientSubstance", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="The ingredient substance",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    strength: typing.List[
        fhirtypes.MedicinalProductIngredientSpecifiedSubstanceStrengthType
    ] = Field(
        None,
        alias="strength",
        title=(
            "Quantity of the substance or specified substance present in the "
            "manufactured item or pharmaceutical product"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
