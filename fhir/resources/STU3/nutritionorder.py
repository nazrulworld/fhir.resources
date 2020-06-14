# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NutritionOrder
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class NutritionOrder(domainresource.DomainResource):
    """ Diet, formula or nutritional supplement request.
    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """

    resource_type = Field("NutritionOrder", const=True)

    allergyIntolerance: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="allergyIntolerance",
        title="List of `Reference` items referencing `AllergyIntolerance` (represented as `dict` in JSON)",
        description="List of the patient\u0027s food and nutrition-related allergies and intolerances",
    )

    dateTime: fhirtypes.DateTime = Field(
        ...,
        alias="dateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="Date and time the nutrition order was requested",
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Type `Reference` referencing `Encounter` (represented as `dict` in JSON)",
        description="The encounter associated with this nutrition order",
    )

    enteralFormula: fhirtypes.NutritionOrderEnteralFormulaType = Field(
        None,
        alias="enteralFormula",
        title="Type `NutritionOrderEnteralFormula` (represented as `dict` in JSON)",
        description="Enteral formula components",
    )

    excludeFoodModifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="excludeFoodModifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Order-specific modifier about the type of food that should not be given",
    )

    foodPreferenceModifier: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="foodPreferenceModifier",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Order-specific modifier about the type of food that should be given",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Identifiers assigned to this order",
    )

    oralDiet: fhirtypes.NutritionOrderOralDietType = Field(
        None,
        alias="oralDiet",
        title="Type `NutritionOrderOralDiet` (represented as `dict` in JSON)",
        description="Oral diet components",
    )

    orderer: fhirtypes.ReferenceType = Field(
        None,
        alias="orderer",
        title="Type `Reference` referencing `Practitioner` (represented as `dict` in JSON)",
        description="Who ordered the diet, formula or nutritional supplement",
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Type `Reference` referencing `Patient` (represented as `dict` in JSON)",
        description="The person who requires the diet, formula or nutritional supplement",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="proposed | draft | planned | requested | active | on-hold | completed | cancelled | entered-in-error",
    )

    supplement: ListType[fhirtypes.NutritionOrderSupplementType] = Field(
        None,
        alias="supplement",
        title="List of `NutritionOrderSupplement` items (represented as `dict` in JSON)",
        description="Supplement components",
    )


class NutritionOrderEnteralFormula(backboneelement.BackboneElement):
    """ Enteral formula components.
    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """

    resource_type = Field("NutritionOrderEnteralFormula", const=True)

    additiveProductName: fhirtypes.String = Field(
        None,
        alias="additiveProductName",
        title="Type `String` (represented as `dict` in JSON)",
        description="Product or brand name of the modular additive",
    )

    additiveType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additiveType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of modular component to add to the feeding",
    )

    administration: ListType[
        fhirtypes.NutritionOrderEnteralFormulaAdministrationType
    ] = Field(
        None,
        alias="administration",
        title="List of `NutritionOrderEnteralFormulaAdministration` items (represented as `dict` in JSON)",
        description="Formula feeding instruction as structured data",
    )

    administrationInstruction: fhirtypes.String = Field(
        None,
        alias="administrationInstruction",
        title="Type `String` (represented as `dict` in JSON)",
        description="Formula feeding instructions expressed as text",
    )

    baseFormulaProductName: fhirtypes.String = Field(
        None,
        alias="baseFormulaProductName",
        title="Type `String` (represented as `dict` in JSON)",
        description="Product or brand name of the enteral or infant formula",
    )

    baseFormulaType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="baseFormulaType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of enteral or infant formula",
    )

    caloricDensity: fhirtypes.QuantityType = Field(
        None,
        alias="caloricDensity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount of energy per specified volume that is required",
    )

    maxVolumeToDeliver: fhirtypes.QuantityType = Field(
        None,
        alias="maxVolumeToDeliver",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Upper limit on formula volume per unit of time",
    )

    routeofAdministration: fhirtypes.CodeableConceptType = Field(
        None,
        alias="routeofAdministration",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="How the formula should enter the patient\u0027s gastrointestinal tract",
    )


class NutritionOrderEnteralFormulaAdministration(backboneelement.BackboneElement):
    """ Formula feeding instruction as structured data.
    Formula administration instructions as structured data.  This repeating
    structure allows for changing the administration rate or volume over time
    for both bolus and continuous feeding.  An example of this would be an
    instruction to increase the rate of continuous feeding every 2 hours.
    """

    resource_type = Field("NutritionOrderEnteralFormulaAdministration", const=True)

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="The volume of formula to provide",
    )

    rateQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="rateQuantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Speed with which the formula is provided per period of time",
        one_of_many="rate",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    rateRatio: fhirtypes.RatioType = Field(
        None,
        alias="rateRatio",
        title="Type `Ratio` (represented as `dict` in JSON)",
        description="Speed with which the formula is provided per period of time",
        one_of_many="rate",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    schedule: fhirtypes.TimingType = Field(
        None,
        alias="schedule",
        title="Type `Timing` (represented as `dict` in JSON)",
        description="Scheduled frequency of enteral feeding",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
            "rate": ["rateQuantity", "rateRatio",],
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


class NutritionOrderOralDiet(backboneelement.BackboneElement):
    """ Oral diet components.
    Diet given orally in contrast to enteral (tube) feeding.
    """

    resource_type = Field("NutritionOrderOralDiet", const=True)

    fluidConsistencyType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="fluidConsistencyType",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="The required consistency of fluids and liquids provided to the patient",
    )

    instruction: fhirtypes.String = Field(
        None,
        alias="instruction",
        title="Type `String` (represented as `dict` in JSON)",
        description="Instructions or additional information about the oral diet",
    )

    nutrient: ListType[fhirtypes.NutritionOrderOralDietNutrientType] = Field(
        None,
        alias="nutrient",
        title="List of `NutritionOrderOralDietNutrient` items (represented as `dict` in JSON)",
        description="Required  nutrient modifications",
    )

    schedule: ListType[fhirtypes.TimingType] = Field(
        None,
        alias="schedule",
        title="List of `Timing` items (represented as `dict` in JSON)",
        description="Scheduled frequency of diet",
    )

    texture: ListType[fhirtypes.NutritionOrderOralDietTextureType] = Field(
        None,
        alias="texture",
        title="List of `NutritionOrderOralDietTexture` items (represented as `dict` in JSON)",
        description="Required  texture modifications",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Type of oral diet or diet restrictions that describe what can be consumed orally",
    )


class NutritionOrderOralDietNutrient(backboneelement.BackboneElement):
    """ Required  nutrient modifications.
    Class that defines the quantity and type of nutrient modifications (for
    example carbohydrate, fiber or sodium) required for the oral diet.
    """

    resource_type = Field("NutritionOrderOralDietNutrient", const=True)

    amount: fhirtypes.QuantityType = Field(
        None,
        alias="amount",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Quantity of the specified nutrient",
    )

    modifier: fhirtypes.CodeableConceptType = Field(
        None,
        alias="modifier",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of nutrient that is being modified",
    )


class NutritionOrderOralDietTexture(backboneelement.BackboneElement):
    """ Required  texture modifications.
    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """

    resource_type = Field("NutritionOrderOralDietTexture", const=True)

    foodType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="foodType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Concepts that are used to identify an entity that is ingested for nutritional purposes",
    )

    modifier: fhirtypes.CodeableConceptType = Field(
        None,
        alias="modifier",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Code to indicate how to alter the texture of the foods, e.g. pureed",
    )


class NutritionOrderSupplement(backboneelement.BackboneElement):
    """ Supplement components.
    Oral nutritional products given in order to add further nutritional value
    to the patient's diet.
    """

    resource_type = Field("NutritionOrderSupplement", const=True)

    instruction: fhirtypes.String = Field(
        None,
        alias="instruction",
        title="Type `String` (represented as `dict` in JSON)",
        description="Instructions or additional information about the oral supplement",
    )

    productName: fhirtypes.String = Field(
        None,
        alias="productName",
        title="Type `String` (represented as `dict` in JSON)",
        description="Product or brand name of the nutritional supplement",
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Amount of the nutritional supplement",
    )

    schedule: ListType[fhirtypes.TimingType] = Field(
        None,
        alias="schedule",
        title="List of `Timing` items (represented as `dict` in JSON)",
        description="Scheduled frequency of supplement",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of supplement product requested",
    )
