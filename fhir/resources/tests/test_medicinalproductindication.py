# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIndication
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicinalproductindication


def impl_medicinalproductindication_1(inst):
    assert inst.comorbidity[0].coding[0].code == "Hipsurgery"
    assert (
        inst.comorbidity[0].coding[0].system
        == "http://ema.europa.eu/example/comorbidity"
    )
    assert (
        inst.diseaseSymptomProcedure.coding[0].code
        == "Venousthromboembolismprophylaxis"
    )
    assert inst.diseaseSymptomProcedure.coding[0].system == (
        "http://ema.europa.eu/example/indicationasdisease-symptom-" "procedure"
    )
    assert inst.id == "example"
    assert inst.intendedEffect.coding[0].code == "PRYLX"
    assert (
        inst.intendedEffect.coding[0].system
        == "http://ema.europa.eu/example/intendedeffect"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.population[0].ageRange.low.unit == "a"
    assert float(inst.population[0].ageRange.low.value) == float(18)
    assert inst.text.status == "generated"


def test_medicinalproductindication_1(base_settings):
    """No. 1 tests collection for MedicinalProductIndication.
    Test File: medicinalproductindication-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicinalproductindication-example.json"
    )
    inst = medicinalproductindication.MedicinalProductIndication.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductIndication" == inst.resource_type

    impl_medicinalproductindication_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductIndication" == data["resourceType"]

    inst2 = medicinalproductindication.MedicinalProductIndication(**data)
    impl_medicinalproductindication_1(inst2)
