# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NutritionProduct
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import nutritionproduct
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_nutritionproduct_1(inst):
    assert inst.category[0].coding[0].code == "227313005"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.code.coding[0].code == "227507002"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.id == "example"
    assert (
        inst.instance[0].identifier[0].system
        == ExternalValidatorModel(valueUri="http://example.org/foodserials").valueUri
    )
    assert inst.instance[0].identifier[0].value == "77239487"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_nutritionproduct_1(base_settings):
    """No. 1 tests collection for NutritionProduct.
    Test File: nutritionproduct-example.json
    """
    filename = base_settings["unittest_data_dir"] / "nutritionproduct-example.json"
    inst = nutritionproduct.NutritionProduct.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "NutritionProduct" == inst.get_resource_type()

    impl_nutritionproduct_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "NutritionProduct" == data["resourceType"]

    inst2 = nutritionproduct.NutritionProduct(**data)
    impl_nutritionproduct_1(inst2)
