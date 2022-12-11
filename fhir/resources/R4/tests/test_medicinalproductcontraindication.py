# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductContraindication
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicinalproductcontraindication


def impl_medicinalproductcontraindication_1(inst):
    assert inst.comorbidity[0].coding[0].code == "Hepaticdisease"
    assert (
        inst.comorbidity[0].coding[0].system
        == "http://ema.europa.eu/example/comorbidity"
    )
    assert (
        inst.disease.coding[0].code
        == "Coagulopathiesandbleedingdiatheses(exclthrombocytopenic)"
    )
    assert inst.disease.coding[0].system == (
        "http://ema.europa.eu/example/contraindicationsasdisease-" "symptom-procedure"
    )
    assert inst.disease.text == (
        "Hepatic disease associated with coagulopathy and clinically "
        "relevant bleeding risk"
    )
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_medicinalproductcontraindication_1(base_settings):
    """No. 1 tests collection for MedicinalProductContraindication.
    Test File: medicinalproductcontraindication-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "medicinalproductcontraindication-example.json"
    )
    inst = medicinalproductcontraindication.MedicinalProductContraindication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductContraindication" == inst.resource_type

    impl_medicinalproductcontraindication_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductContraindication" == data["resourceType"]

    inst2 = medicinalproductcontraindication.MedicinalProductContraindication(**data)
    impl_medicinalproductcontraindication_1(inst2)
