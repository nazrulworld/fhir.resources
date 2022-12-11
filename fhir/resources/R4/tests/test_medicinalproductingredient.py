# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicinalproductingredient


def impl_medicinalproductingredient_1(inst):
    assert inst.id == "example"
    assert inst.manufacturer[0].reference == "Organization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.role.coding[0].code == "ActiveBase"
    assert inst.role.coding[0].system == "http://ema.europa.eu/example/ingredientRole"
    assert (
        inst.specifiedSubstance[0].code.coding[0].code == "equixabanCompanyequixaban1"
    )
    assert (
        inst.specifiedSubstance[0].code.coding[0].system
        == "http://ema.europa.eu/example/specifiedSubstance"
    )
    assert inst.specifiedSubstance[0].group.coding[0].code == "2"
    assert (
        inst.specifiedSubstance[0].group.coding[0].system
        == "http://ema.europa.eu/example/specifiedSubstanceGroup"
    )
    assert inst.substance.code.coding[0].code == "EQUIXABAN"
    assert (
        inst.substance.code.coding[0].system == "http://ema.europa.eu/example/substance"
    )
    assert inst.substance.strength[0].presentation.denominator.unit == "{tablet}"
    assert float(inst.substance.strength[0].presentation.denominator.value) == float(1)
    assert inst.substance.strength[0].presentation.numerator.unit == "mg"
    assert float(inst.substance.strength[0].presentation.numerator.value) == float(2.5)
    assert inst.text.status == "generated"


def test_medicinalproductingredient_1(base_settings):
    """No. 1 tests collection for MedicinalProductIngredient.
    Test File: medicinalproductingredient-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicinalproductingredient-example.json"
    )
    inst = medicinalproductingredient.MedicinalProductIngredient.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductIngredient" == inst.resource_type

    impl_medicinalproductingredient_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductIngredient" == data["resourceType"]

    inst2 = medicinalproductingredient.MedicinalProductIngredient(**data)
    impl_medicinalproductingredient_1(inst2)
