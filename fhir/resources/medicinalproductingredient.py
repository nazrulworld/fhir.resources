# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

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
        title="Type `bool`",
        description="If the ingredient is a known or suspected allergen",
    )
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_allergenicIndicator",
        title="Extension field for ``allergenicIndicator``.",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Identifier for the ingredient",
    )

    manufacturer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title=(
            "List of `Reference` items referencing `Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="Manufacturer of this Ingredient",
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Ingredient role e.g. Active ingredient, excipient",
    )

    specifiedSubstance: ListType[
        fhirtypes.MedicinalProductIngredientSpecifiedSubstanceType
    ] = Field(
        None,
        alias="specifiedSubstance",
        title=(
            "List of `MedicinalProductIngredientSpecifiedSubstance` items "
            "(represented as `dict` in JSON)"
        ),
        description="A specified substance that comprises this ingredient",
    )

    substance: fhirtypes.MedicinalProductIngredientSubstanceType = Field(
        None,
        alias="substance",
        title=(
            "Type `MedicinalProductIngredientSubstance` (represented as `dict` in "
            "JSON)"
        ),
        description="The ingredient substance",
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
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The specified substance",
    )

    confidentiality: fhirtypes.CodeableConceptType = Field(
        None,
        alias="confidentiality",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Confidentiality level of the specified substance as the ingredient",
    )

    group: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="group",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The group of specified substance, e.g. group 1 to 4",
    )

    strength: ListType[
        fhirtypes.MedicinalProductIngredientSpecifiedSubstanceStrengthType
    ] = Field(
        None,
        alias="strength",
        title=(
            "List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items "
            "(represented as `dict` in JSON)"
        ),
        description=(
            "Quantity of the substance or specified substance present in the "
            "manufactured item or pharmaceutical product"
        ),
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
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="The strength per unitary volume (or mass)",
    )

    concentrationLowLimit: fhirtypes.RatioType = Field(
        None,
        alias="concentrationLowLimit",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description=(
            "A lower limit for the strength per unitary volume (or mass), for when "
            "there is a range. The concentration attribute then becomes the upper "
            "limit"
        ),
    )

    country: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="country",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The country or countries for which the strength range applies",
    )

    measurementPoint: fhirtypes.String = Field(
        None,
        alias="measurementPoint",
        title="Type `String`",
        description="For when strength is measured at a particular point or distance",
    )
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_measurementPoint",
        title="Extension field for ``measurementPoint``.",
    )

    presentation: fhirtypes.RatioType = Field(
        ...,
        alias="presentation",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description=(
            "The quantity of substance in the unit of presentation, or in the "
            "volume (or mass) of the single pharmaceutical product or manufactured "
            "item"
        ),
    )

    presentationLowLimit: fhirtypes.RatioType = Field(
        None,
        alias="presentationLowLimit",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description=(
            "A lower limit for the quantity of substance in the unit of "
            "presentation. For use when there is a range of strengths, this is the "
            "lower limit, with the presentation attribute becoming the upper limit"
        ),
    )

    referenceStrength: ListType[
        fhirtypes.MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrengthType
    ] = Field(
        None,
        alias="referenceStrength",
        title=(
            "List of `MedicinalProductIngredientSpecifiedSubstanceStrengthReference"
            "Strength` items (represented as `dict` in JSON)"
        ),
        description="Strength expressed in terms of a reference substance",
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

    country: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="country",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The country or countries for which the strength range applies",
    )

    measurementPoint: fhirtypes.String = Field(
        None,
        alias="measurementPoint",
        title="Type `String`",
        description="For when strength is measured at a particular point or distance",
    )
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_measurementPoint",
        title="Extension field for ``measurementPoint``.",
    )

    strength: fhirtypes.RatioType = Field(
        ...,
        alias="strength",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Strength expressed in terms of a reference substance",
    )

    strengthLowLimit: fhirtypes.RatioType = Field(
        None,
        alias="strengthLowLimit",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Strength expressed in terms of a reference substance",
    )

    substance: fhirtypes.CodeableConceptType = Field(
        None,
        alias="substance",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Relevant reference substance",
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
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="The ingredient substance",
    )

    strength: ListType[
        fhirtypes.MedicinalProductIngredientSpecifiedSubstanceStrengthType
    ] = Field(
        None,
        alias="strength",
        title=(
            "List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items "
            "(represented as `dict` in JSON)"
        ),
        description=(
            "Quantity of the substance or specified substance present in the "
            "manufactured item or pharmaceutical product"
        ),
    )
