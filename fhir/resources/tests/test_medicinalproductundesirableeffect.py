# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicinalproductundesirableeffect


def impl_medicinalproductundesirableeffect_1(inst):
    assert inst.classification.coding[0].code == "Bloodandlymphaticsystemdisorders"
    assert inst.classification.coding[0].system == (
        "http://ema.europa.eu/example/symptom-condition-" "effectclassification"
    )
    assert inst.frequencyOfOccurrence.coding[0].code == "Common"
    assert (
        inst.frequencyOfOccurrence.coding[0].system
        == "http://ema.europa.eu/example/frequencyofoccurrence"
    )
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.symptomConditionEffect.coding[0].code == "Anaemia"
    assert inst.symptomConditionEffect.coding[0].system == (
        "http://ema.europa.eu/example/undesirableeffectassymptom-" "condition-effect"
    )
    assert inst.symptomConditionEffect.text == (
        "Prevention of\\nVTE in adult\\npatients who "
        "have\\nundergone\\nelective hip or\\nknee "
        "replacement\\nsurgery (VTEp)"
    )
    assert inst.text.status == "generated"


def test_medicinalproductundesirableeffect_1(base_settings):
    """No. 1 tests collection for MedicinalProductUndesirableEffect.
    Test File: medicinalproductundesirableeffect-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "medicinalproductundesirableeffect-example.json"
    )
    inst = (
        medicinalproductundesirableeffect.MedicinalProductUndesirableEffect.parse_file(
            filename, content_type="application/json", encoding="utf-8"
        )
    )
    assert "MedicinalProductUndesirableEffect" == inst.resource_type

    impl_medicinalproductundesirableeffect_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductUndesirableEffect" == data["resourceType"]

    inst2 = medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(**data)
    impl_medicinalproductundesirableeffect_1(inst2)
