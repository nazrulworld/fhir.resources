# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicinalproductpharmaceutical


def impl_medicinalproductpharmaceutical_1(inst):
    assert inst.administrableDoseForm.coding[0].code == "Film-coatedtablet"
    assert (
        inst.administrableDoseForm.coding[0].system
        == "http://ema.europa.eu/example/administrabledoseform"
    )
    assert inst.id == "example"
    assert (
        inst.identifier[0].system == "http://ema.europa.eu/example/phpididentifiersets"
    )
    assert inst.identifier[0].value == "{PhPID}"
    assert inst.ingredient[0].reference == "MedicinalProductIngredient/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.routeOfAdministration[0].code.coding[0].code == "OralUse"
    assert (
        inst.routeOfAdministration[0].code.coding[0].system
        == "http://ema.europa.eu/example/routeofadministration"
    )
    assert inst.text.status == "generated"
    assert inst.unitOfPresentation.coding[0].code == "Tablet"
    assert (
        inst.unitOfPresentation.coding[0].system
        == "http://ema.europa.eu/example/unitofpresentation"
    )


def test_medicinalproductpharmaceutical_1(base_settings):
    """No. 1 tests collection for MedicinalProductPharmaceutical.
    Test File: medicinalproductpharmaceutical-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "medicinalproductpharmaceutical-example.json"
    )
    inst = medicinalproductpharmaceutical.MedicinalProductPharmaceutical.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductPharmaceutical" == inst.resource_type

    impl_medicinalproductpharmaceutical_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductPharmaceutical" == data["resourceType"]

    inst2 = medicinalproductpharmaceutical.MedicinalProductPharmaceutical(**data)
    impl_medicinalproductpharmaceutical_1(inst2)
