# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Ingredient
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import ingredient
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_ingredient_1(inst):
    assert inst.id == "example"
    assert inst.manufacturer[0].manufacturer.reference == "Organization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.role.coding[0].code == "ActiveBase"
    assert (
        inst.role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ema.europa.eu/example/ingredientRole"}
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.substance.code.concept.coding[0].code == "Wizzohaler"
    assert (
        inst.substance.code.concept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ema.europa.eu/example/substance"}
        ).valueUri
    )
    assert inst.substance.strength[0].measurementPoint == "2cm"
    assert (
        inst.substance.strength[0].presentationRatio.denominator.code
        == "{delivered dose}"
    )
    assert (
        inst.substance.strength[0].presentationRatio.denominator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert (
        inst.substance.strength[0].presentationRatio.denominator.unit
        == "delivered dose"
    )
    assert float(
        inst.substance.strength[0].presentationRatio.denominator.value
    ) == float(1)
    assert inst.substance.strength[0].presentationRatio.numerator.code == "ug"
    assert (
        inst.substance.strength[0].presentationRatio.numerator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.substance.strength[0].presentationRatio.numerator.unit == "mcg"
    assert float(inst.substance.strength[0].presentationRatio.numerator.value) == float(
        730
    )
    assert inst.substance.strength[1].measurementPoint == "5cm"
    assert (
        inst.substance.strength[1].presentationRatio.denominator.code
        == "{delivered dose}"
    )
    assert (
        inst.substance.strength[1].presentationRatio.denominator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert (
        inst.substance.strength[1].presentationRatio.denominator.unit
        == "delivered dose"
    )
    assert float(
        inst.substance.strength[1].presentationRatio.denominator.value
    ) == float(1)
    assert inst.substance.strength[1].presentationRatio.numerator.code == "ug"
    assert (
        inst.substance.strength[1].presentationRatio.numerator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.substance.strength[1].presentationRatio.numerator.unit == "mcg"
    assert float(inst.substance.strength[1].presentationRatio.numerator.value) == float(
        460
    )
    assert inst.text.status == "generated"


def test_ingredient_1(base_settings):
    """No. 1 tests collection for Ingredient.
    Test File: ingredient-example-strength-repeat.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "ingredient-example-strength-repeat.json"
    )
    inst = ingredient.Ingredient.model_validate_json(filename.read_bytes())
    assert "Ingredient" == inst.get_resource_type()

    impl_ingredient_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Ingredient" == data["resourceType"]

    inst2 = ingredient.Ingredient(**data)
    impl_ingredient_1(inst2)


def impl_ingredient_2(inst):
    assert inst.id == "example"
    assert inst.manufacturer[0].manufacturer.reference == "Organization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.role.coding[0].code == "ActiveBase"
    assert (
        inst.role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ema.europa.eu/example/ingredientRole"}
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.substance.code.concept.coding[0].code == "EQUIXABAN"
    assert (
        inst.substance.code.concept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ema.europa.eu/example/substance"}
        ).valueUri
    )
    assert inst.substance.strength[0].concentrationRatio.denominator.code == "mg"
    assert (
        inst.substance.strength[0].concentrationRatio.denominator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.substance.strength[0].concentrationRatio.denominator.unit == "mg"
    assert float(
        inst.substance.strength[0].concentrationRatio.denominator.value
    ) == float(1)
    assert inst.substance.strength[0].concentrationRatio.numerator.code == "mg"
    assert (
        inst.substance.strength[0].concentrationRatio.numerator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.substance.strength[0].concentrationRatio.numerator.unit == "mg"
    assert float(
        inst.substance.strength[0].concentrationRatio.numerator.value
    ) == float(5)
    assert inst.substance.strength[0].presentationRatio.denominator.code == "{tablet}"
    assert (
        inst.substance.strength[0].presentationRatio.denominator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.substance.strength[0].presentationRatio.denominator.unit == "tablet"
    assert float(
        inst.substance.strength[0].presentationRatio.denominator.value
    ) == float(1)
    assert inst.substance.strength[0].presentationRatio.numerator.code == "mg"
    assert (
        inst.substance.strength[0].presentationRatio.numerator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.substance.strength[0].presentationRatio.numerator.unit == "mg"
    assert float(inst.substance.strength[0].presentationRatio.numerator.value) == float(
        50
    )
    assert (
        inst.substance.strength[0].referenceStrength[0].strengthRatio.denominator.code
        == "mg"
    )
    assert (
        inst.substance.strength[0].referenceStrength[0].strengthRatio.denominator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert (
        inst.substance.strength[0].referenceStrength[0].strengthRatio.denominator.unit
        == "mg"
    )
    assert float(
        inst.substance.strength[0].referenceStrength[0].strengthRatio.denominator.value
    ) == float(1)
    assert (
        inst.substance.strength[0].referenceStrength[0].strengthRatio.numerator.code
        == "mg"
    )
    assert (
        inst.substance.strength[0].referenceStrength[0].strengthRatio.numerator.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert (
        inst.substance.strength[0].referenceStrength[0].strengthRatio.numerator.unit
        == "mg"
    )
    assert float(
        inst.substance.strength[0].referenceStrength[0].strengthRatio.numerator.value
    ) == float(5.03)
    assert (
        inst.substance.strength[0].referenceStrength[0].substance.concept.coding[0].code
        == "EQUIXABAN-SULPHATE"
    )
    assert (
        inst.substance.strength[0]
        .referenceStrength[0]
        .substance.concept.coding[0]
        .system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ema.europa.eu/example/substance"}
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_ingredient_2(base_settings):
    """No. 2 tests collection for Ingredient.
    Test File: ingredient-example.json
    """
    filename = base_settings["unittest_data_dir"] / "ingredient-example.json"
    inst = ingredient.Ingredient.model_validate_json(filename.read_bytes())
    assert "Ingredient" == inst.get_resource_type()

    impl_ingredient_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Ingredient" == data["resourceType"]

    inst2 = ingredient.Ingredient(**data)
    impl_ingredient_2(inst2)
