# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Ingredient
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import ingredient


def impl_ingredient_1(inst):
    assert inst.id == "example"
    assert inst.manufacturer[0].manufacturer.reference == "Organization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.role.coding[0].code == "ActiveBase"
    assert inst.role.coding[0].system == "http://ema.europa.eu/example/ingredientRole"
    assert inst.status == "active"
    assert inst.substance.code.concept.coding[0].code == "EQUIXABAN"
    assert (
        inst.substance.code.concept.coding[0].system
        == "http://ema.europa.eu/example/substance"
    )
    assert inst.substance.strength[0].presentationRatio.denominator.code == "{tablet}"
    assert (
        inst.substance.strength[0].presentationRatio.denominator.system
        == "http://unitsofmeasure.org"
    )
    assert inst.substance.strength[0].presentationRatio.denominator.unit == "tablet"
    assert float(
        inst.substance.strength[0].presentationRatio.denominator.value
    ) == float(1)
    assert inst.substance.strength[0].presentationRatio.numerator.code == "mg"
    assert (
        inst.substance.strength[0].presentationRatio.numerator.system
        == "http://unitsofmeasure.org"
    )
    assert inst.substance.strength[0].presentationRatio.numerator.unit == "mg"
    assert float(inst.substance.strength[0].presentationRatio.numerator.value) == float(
        2.5
    )
    assert inst.text.status == "generated"


def test_ingredient_1(base_settings):
    """No. 1 tests collection for Ingredient.
    Test File: ingredient-example.json
    """
    filename = base_settings["unittest_data_dir"] / "ingredient-example.json"
    inst = ingredient.Ingredient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Ingredient" == inst.resource_type

    impl_ingredient_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Ingredient" == data["resourceType"]

    inst2 = ingredient.Ingredient(**data)
    impl_ingredient_1(inst2)
