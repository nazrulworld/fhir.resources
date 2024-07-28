# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import clinicalusedefinition
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_clinicalusedefinition_1(inst):
    assert (
        inst.contraindication.comorbidity[0].concept.coding[0].code == "Hepaticdisease"
    )
    assert (
        inst.contraindication.comorbidity[0].concept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://ema.europa.eu/example/comorbidity"
        ).valueUri
    )
    assert (
        inst.contraindication.diseaseSymptomProcedure.concept.coding[0].code
        == "Coagulopathiesandbleedingdiatheses(exclthrombocytopenic)"
    )
    assert (
        inst.contraindication.diseaseSymptomProcedure.concept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://ema.europa.eu/example/contraindicationsasdisease-symptom-procedure"
        ).valueUri
    )
    assert inst.contraindication.diseaseSymptomProcedure.concept.text == (
        "Hepatic disease associated with coagulopathy and clinically "
        "relevant bleeding risk"
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
    assert inst.text.status == "generated"
    assert inst.type == "contraindication"


def test_clinicalusedefinition_1(base_settings):
    """No. 1 tests collection for ClinicalUseDefinition.
    Test File: clinicalusedefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "clinicalusedefinition-example.json"
    inst = clinicalusedefinition.ClinicalUseDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "ClinicalUseDefinition" == inst.get_resource_type()

    impl_clinicalusedefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ClinicalUseDefinition" == data["resourceType"]

    inst2 = clinicalusedefinition.ClinicalUseDefinition(**data)
    impl_clinicalusedefinition_1(inst2)
