# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicinalproductmanufactured


def impl_medicinalproductmanufactured_1(inst):
    assert inst.id == "example"
    assert inst.ingredient[0].reference == "MedicinalProductIngredient/example"
    assert inst.manufacturedDoseForm.coding[0].code == "Film-coatedtablet"
    assert (
        inst.manufacturedDoseForm.coding[0].system
        == "http://ema.europa.eu/example/manufactureddoseform"
    )
    assert inst.manufacturer[0].reference == "Organization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.physicalCharacteristics.color[0] == "Pink"
    assert inst.physicalCharacteristics.imprint[0] == "894"
    assert inst.physicalCharacteristics.shape == "Oval"
    assert inst.quantity.unit == "1"
    assert float(inst.quantity.value) == float(10)
    assert inst.text.status == "generated"
    assert inst.unitOfPresentation.coding[0].code == "Tablet"
    assert (
        inst.unitOfPresentation.coding[0].system
        == "http://ema.europa.eu/example/unitofpresentation"
    )


def test_medicinalproductmanufactured_1(base_settings):
    """No. 1 tests collection for MedicinalProductManufactured.
    Test File: medicinalproductmanufactured-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicinalproductmanufactured-example.json"
    )
    inst = medicinalproductmanufactured.MedicinalProductManufactured.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductManufactured" == inst.resource_type

    impl_medicinalproductmanufactured_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductManufactured" == data["resourceType"]

    inst2 = medicinalproductmanufactured.MedicinalProductManufactured(**data)
    impl_medicinalproductmanufactured_1(inst2)
