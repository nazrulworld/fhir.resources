# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationKnowledge
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import medicationknowledge
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_medicationknowledge_1(inst):
    assert inst.code.coding[0].code == "0409-6531-02"
    assert (
        inst.code.coding[0].display
        == "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"
    )
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://hl7.org/fhir/sid/ndc").valueUri
    )
    assert inst.definitional.doseForm.coding[0].code == "385268001"
    assert (
        inst.definitional.doseForm.coding[0].display
        == "Oral Dose Form (qualifier value)"
    )
    assert (
        inst.definitional.doseForm.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name[0] == "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"
    assert inst.status == "active"
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
