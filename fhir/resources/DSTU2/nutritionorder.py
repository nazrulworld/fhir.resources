# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/DSTU2/nutritionorder.html
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
import typing
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes
from .backboneelement import BackboneElement


class NutritionOrder(domainresource.DomainResource):
    """A request for a diet, formula or nutritional supplement


    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """

    resource_type = Field("NutritionOrder", const=True)

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Type 'Reference' referencing 'Patient'  (represented as 'dict' in JSON).",
        description="The person who requires the diet, formula or nutritional supplement",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
        element_property=True,
    )

    orderer: fhirtypes.ReferenceType = Field(
        None,
        alias="orderer",
        title="Type 'Reference' referencing 'Practitioner'  (represented as 'dict' in JSON).",
        description="Who ordered the diet, formula or nutritional supplement",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
        element_property=True,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifiers assigned to this order",
        description=(
            "Identifiers assigned to this order by "
            "the order sender or by the order receiver."
        ),
        element_property=True,
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type 'Reference' referencing 'Encounter'  (represented as 'dict' in JSON).",
        description="The encounter associated with this nutrition order",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
        element_property=True,
    )

    dateTime: fhirtypes.DateTime = Field(
        None,
        alias="dateTime",
        title="Date and time the nutrition order was requested",
        description="The date and time that this nutrition order was requested.",
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON).",
        description=(
            "proposed | draft | planned "
            "| requested | active | on-hold | completed | cancelled"
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "proposed",
            "draft",
            "planned",
            "requested",
            "active",
            "on-hold",
            "completed",
            "cancelled",
        ],
        element_property=True,
    )

    allergyIntolerance: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="allergyIntolerance",
        title=(
            "Type 'Reference' referencing 'AllergyIntolerance'  "
            "(represented as 'dict' in JSON)."
        ),
        description=(
            "List of the patient's food and "
            "nutrition-related allergies and intolerances"
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["AllergyIntolerance"],
        element_property=True,
    )

    foodPreferenceModifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="foodPreferenceModifier",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Order-specific modifier about the type of food that should be given",
        element_property=True,
    )

    excludeFoodModifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="excludeFoodModifier",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="Order-specific modifier about the type of food that should not be given",
        element_property=True,
    )

    oralDiet: fhirtypes.NutritionOrderOralDietType = Field(
        None,
        alias="oralDiet",
        title="Oral diet components",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    supplement: ListType[fhirtypes.NutritionOrderSupplementType] = Field(
        None,
        alias="supplement",
        title="Supplement components",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    enteralFormula: fhirtypes.NutritionOrderEnteralFormulaType = Field(
        None,
        alias="enteralFormula",
        title="Enteral formula components",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class NutritionOrderOralDiet(BackboneElement):
    """Oral diet components


    Diet given orally in contrast to enteral (tube) feeding.
    """

    resource_type = Field("NutritionOrderOralDiet", const=True)

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description=(
            "Type of oral diet or diet restrictions that "
            "describe what can be consumed orally"
        ),
        element_property=True,
    )

    schedule: ListType[fhirtypes.TimingType] = Field(
        None,
        alias="schedule",
        title="Type `Timing` (represented as `dict` in JSON).",
        description="Scheduled frequency of diet",
        element_property=True,
    )

    nutrient: ListType[fhirtypes.NutritionOrderOralDietNutrientType] = Field(
        None,
        alias="nutrient",
        title="Required nutrient modifications",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    texture: ListType[fhirtypes.NutritionOrderOralDietTextureType] = Field(
        None,
        alias="texture",
        title="Required texture modifications",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    fluidConsistencyType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="fluidConsistencyType",
        title="Type `CodeableConcept` (represented as `dict` in JSON).",
        description="The required consistency of fluids and liquids provided to the patient",
        element_property=True,
    )

    instruction: fhirtypes.String = Field(
        None,
        alias="instruction",
        title="Type `String` (represented as `dict` in JSON)",
        description="Instructions or additional information about the oral diet",
        element_property=True,
    )


class NutritionOrderSupplement(BackboneElement):
    """Supplement components

    Oral nutritional products given in order to add further
    nutritional value to the patient's diet.
    """

    resource_type = Field("NutritionOrderSupplement", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of supplement product requested",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    productName: fhirtypes.String = Field(
        None,
        alias="productName",
        title="Type `String` (represented as `dict` in JSON)",
        description="Product or brand name of the nutritional supplement",
        element_property=True,
    )

    schedule: ListType[fhirtypes.TimingType] = Field(
        None,
        alias="schedule",
        title="Type `Timing` (represented as `dict` in JSON).",
        description="Scheduled frequency of supplement",
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Amount of the nutritional supplement",
        element_property=True,
    )

    instruction: fhirtypes.String = Field(
        None,
        alias="instruction",
        title="Type `String` (represented as `dict` in JSON)",
        description="Instructions or additional information about the oral supplement",
        element_property=True,
    )


class NutritionOrderEnteralFormula(BackboneElement):
    """Enteral formula components


    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """

    resource_type = Field("NutritionOrderEnteralFormula", const=True)

    baseFormulaType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="baseFormulaType",
        title="Type of enteral or infant formula",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    baseFormulaProductName: fhirtypes.String = Field(
        None,
        alias="baseFormulaProductName",
        title="Type `String` (represented as `dict` in JSON)",
        description="Product or brand name of the enteral or infant formula",
        element_property=True,
    )

    additiveType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additiveType",
        title="Type of modular component to add to the feeding",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    additiveProductName: fhirtypes.String = Field(
        None,
        alias="additiveProductName",
        title="Type `String` (represented as `dict` in JSON)",
        description="Product or brand name of the modular additive",
        element_property=True,
    )

    caloricDensity: fhirtypes.QuantityType = Field(
        None,
        alias="caloricDensity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Amount of energy per specified volume that is required",
        element_property=True,
    )

    routeofAdministration: fhirtypes.CodeableConceptType = Field(
        None,
        alias="routeofAdministration",
        title="How the formula should enter the patient's gastrointestinal tract",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    administration: ListType[
        fhirtypes.NutritionOrderEnteralFormulaAdministrationType
    ] = Field(
        None,
        alias="administration",
        title="Formula feeding instruction as structured data",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    maxVolumeToDeliver: fhirtypes.QuantityType = Field(
        None,
        alias="maxVolumeToDeliver",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Upper limit on formula volume per unit of time",
        element_property=True,
    )

    administrationInstruction: fhirtypes.String = Field(
        None,
        alias="administrationInstruction",
        title="Type `String` (represented as `dict` in JSON)",
        description="Formula feeding instructions expressed as text",
        element_property=True,
    )


class NutritionOrderOralDietNutrient(BackboneElement):
    """Required nutrient modifications


    Class that defines the quantity and type of nutrient modifications required
    for the oral diet.
    """

    resource_type = Field("NutritionOrderOralDietNutrient", const=True)

    modifier: fhirtypes.CodeableConceptType = Field(
        None,
        alias="modifier",
        title="Type of nutrient that is being modified",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Quantity of the specified nutrient",
        element_property=True,
    )


class NutritionOrderOralDietTexture(BackboneElement):
    """Required texture modifications



    Class that describes any texture modifications required for the patient
    to safely consume various types of solid foods.
    """

    resource_type = Field("NutritionOrderOralDietTexture", const=True)

    modifier: fhirtypes.CodeableConceptType = Field(
        None,
        alias="modifier",
        title="Code to indicate how to alter the texture of the foods, e.g. pureed",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    foodType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="foodType",
        title=(
            "Concepts that are used to identify an "
            "entity that is ingested for nutritional purposes"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class NutritionOrderEnteralFormulaAdministration(BackboneElement):
    """Formula feeding instruction as structured data


    Formula administration instructions as structured data. This repeating
    structure allows for changing the administration rate or volume over time
    for both bolus and continuous feeding. An example of this would be an
    instruction to increase the rate of continuous feeding every 2 hours.
    """

    resource_type = Field("NutritionOrderEnteralFormulaAdministration", const=True)

    schedule: fhirtypes.TimingType = Field(
        None,
        alias="schedule",
        title="Type `Timing` (represented as `dict` in JSON).",
        description="Scheduled frequency of enteral feeding",
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="The volume of formula to provide",
        element_property=True,
    )

    rateQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="rateQuantity",
        title=(
            "Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in "
            "JSON)."
        ),
        description="Speed with which the formula is provided per period of time",
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    rateRatio: fhirtypes.RatioType = Field(
        None,
        alias="rateRatio",
        title="Type `Ratio` (represented as `dict` in JSON).",
        description="Speed with which the formula is provided per period of time",
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2167(
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
            "rate": [
                "rateQuantity",
                "rateRatio",
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
