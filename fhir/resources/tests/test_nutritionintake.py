# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NutritionIntake
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import nutritionintake
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_nutritionintake_1(inst):
    assert inst.code.text == "Inpatient"
    assert inst.consumedItem[0].amount.code == "%"
    assert (
        inst.consumedItem[0].amount.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.consumedItem[0].amount.unit == "percent"
    assert float(inst.consumedItem[0].amount.value) == float(100)
    assert inst.consumedItem[0].nutritionProduct.concept.text == "Grill Sandwich"
    assert inst.consumedItem[0].type.text == "food"
    assert inst.consumedItem[1].amount.code == "%"
    assert (
        inst.consumedItem[1].amount.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.consumedItem[1].amount.unit == "percent"
    assert float(inst.consumedItem[1].amount.value) == float(100)
    assert (
        inst.consumedItem[1].nutritionProduct.concept.text
        == "French Fries Spiral Battered"
    )
    assert inst.consumedItem[1].type.text == "food"
    assert inst.consumedItem[2].amount.code == "%"
    assert (
        inst.consumedItem[2].amount.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.consumedItem[2].amount.unit == "percent"
    assert float(inst.consumedItem[2].amount.value) == float(50)
    assert (
        inst.consumedItem[2].nutritionProduct.concept.text
        == "Tomato Soup Healthy Request"
    )
    assert inst.consumedItem[2].type.text == "food"
    assert inst.consumedItem[3].amount.code == "%"
    assert (
        inst.consumedItem[3].amount.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.consumedItem[3].amount.unit == "percent"
    assert float(inst.consumedItem[3].amount.value) == float(50)
    assert inst.consumedItem[3].nutritionProduct.concept.text == "Side Garden Salad"
    assert inst.consumedItem[3].type.text == "food"
    assert inst.consumedItem[4].amount.code == "%"
    assert (
        inst.consumedItem[4].amount.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.consumedItem[4].amount.unit == "percent"
    assert float(inst.consumedItem[4].amount.value) == float(100)
    assert inst.consumedItem[4].nutritionProduct.concept.text == "Ice Tea Unsweetened"
    assert inst.consumedItem[4].type.text == "fluid"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="http://example.org").valueUri
    )
    assert inst.identifier[0].value == "1144223344"
    assert inst.ingredientLabel[0].amount.code == "kcal"
    assert (
        inst.ingredientLabel[0].amount.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.ingredientLabel[0].amount.unit == "kilocalorie"
    assert float(inst.ingredientLabel[0].amount.value) == float(313)
    assert inst.ingredientLabel[0].nutrient.concept.text == "Total Calories"
    assert inst.ingredientLabel[1].amount.code == "g"
    assert (
        inst.ingredientLabel[1].amount.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.ingredientLabel[1].amount.unit == "grams"
    assert float(inst.ingredientLabel[1].amount.value) == float(10.4)
    assert inst.ingredientLabel[1].nutrient.concept.text == "Protein"
    assert inst.ingredientLabel[2].amount.code == "g"
    assert (
        inst.ingredientLabel[2].amount.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.ingredientLabel[2].amount.unit == "grams"
    assert float(inst.ingredientLabel[2].amount.value) == float(18.0)
    assert inst.ingredientLabel[2].nutrient.concept.text == "Fat (Total)"
    assert inst.ingredientLabel[3].amount.code == "g"
    assert (
        inst.ingredientLabel[3].amount.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.ingredientLabel[3].amount.unit == "grams"
    assert float(inst.ingredientLabel[3].amount.value) == float(26.47)
    assert inst.ingredientLabel[3].nutrient.concept.text == "Carbohydrate"
    assert inst.ingredientLabel[4].amount.code == "mg"
    assert (
        inst.ingredientLabel[4].amount.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.ingredientLabel[4].amount.unit == "Milligrams"
    assert float(inst.ingredientLabel[4].amount.value) == float(770)
    assert inst.ingredientLabel[4].nutrient.concept.text == "Sodium"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert (
        inst.occurrenceDateTime
        == ExternalValidatorModel(
            valueDateTime="2019-08-02T12:45:18+04:00"
        ).valueDateTime
    )
    assert inst.reportedReference.reference == "PractitionerRole/example"
    assert inst.status == "completed"
    assert inst.subject.display == "Paula Patient Chalmers"
    assert inst.text.status == "generated"


def test_nutritionintake_1(base_settings):
    """No. 1 tests collection for NutritionIntake.
    Test File: nutritionintake-example.json
    """
    filename = base_settings["unittest_data_dir"] / "nutritionintake-example.json"
    inst = nutritionintake.NutritionIntake.model_validate_json(filename.read_bytes())
    assert "NutritionIntake" == inst.get_resource_type()

    impl_nutritionintake_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "NutritionIntake" == data["resourceType"]

    inst2 = nutritionintake.NutritionIntake(**data)
    impl_nutritionintake_1(inst2)
