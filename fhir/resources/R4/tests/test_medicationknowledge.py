# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationKnowledge
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicationknowledge


def impl_medicationknowledge_1(inst):
    assert inst.amount.unit == "mg/ml"
    assert float(inst.amount.value) == float(50)
    assert inst.code.coding[0].code == "0069-2587-10"
    assert (
        inst.code.coding[0].display
        == "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"
    )
    assert inst.code.coding[0].system == "http://hl7.org/fhir/sid/ndc"
    assert inst.contained[0].id == "org4"
    assert inst.doseForm.coding[0].code == "385219001"
    assert inst.doseForm.coding[0].display == "Injection Solution (qualifier value)"
    assert inst.doseForm.coding[0].system == "http://snomed.info/sct"
    assert inst.id == "example"
    assert inst.manufacturer.reference == "#org4"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "active"
    assert inst.synonym[0] == "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"
    assert inst.text.status == "generated"


def test_medicationknowledge_1(base_settings):
    """No. 1 tests collection for MedicationKnowledge.
    Test File: medicationknowledge-example.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationknowledge-example.json"
    inst = medicationknowledge.MedicationKnowledge.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicationKnowledge" == inst.resource_type

    impl_medicationknowledge_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicationKnowledge" == data["resourceType"]

    inst2 = medicationknowledge.MedicationKnowledge(**data)
    impl_medicationknowledge_1(inst2)
