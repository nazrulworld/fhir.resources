# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationKnowledge
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import medicationknowledge
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_medicationknowledge_1(inst):
    assert inst.amount.unit == "mg/ml"
    assert float(inst.amount.value) == float(50)
    assert inst.code.coding[0].code == "0409-6531-02"
    assert (
        inst.code.coding[0].display
        == "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"
    )
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/sid/ndc"}
        ).valueUri
    )
    assert inst.contained[0].id == "org4"
    assert inst.doseForm.coding[0].code == "385268001"
    assert inst.doseForm.coding[0].display == "Oral Dose Form (qualifier value)"
    assert (
        inst.doseForm.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.id == "example"
    assert inst.manufacturer.reference == "#org4"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.synonym[0] == "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"
    assert inst.text.status == "generated"


def test_medicationknowledge_1(base_settings):
    """No. 1 tests collection for MedicationKnowledge.
    Test File: medicationknowledge-example.json
    """
    filename = base_settings["unittest_data_dir"] / "medicationknowledge-example.json"
    inst = medicationknowledge.MedicationKnowledge.model_validate_json(
        filename.read_bytes()
    )
    assert "MedicationKnowledge" == inst.get_resource_type()

    impl_medicationknowledge_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "MedicationKnowledge" == data["resourceType"]

    inst2 = medicationknowledge.MedicationKnowledge(**data)
    impl_medicationknowledge_1(inst2)
