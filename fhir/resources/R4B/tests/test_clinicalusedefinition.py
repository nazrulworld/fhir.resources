# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import clinicalusedefinition


def impl_clinicalusedefinition_1(inst):
    assert (
        inst.contraindication.comorbidity[0].concept.coding[0].code == "Hepaticdisease"
    )
    assert (
        inst.contraindication.comorbidity[0].concept.coding[0].system
        == "http://ema.europa.eu/example/comorbidity"
    )
    assert (
        inst.contraindication.diseaseSymptomProcedure.concept.coding[0].code
        == "Coagulopathiesandbleedingdiatheses(exclthrombocytopenic)"
    )
    assert inst.contraindication.diseaseSymptomProcedure.concept.coding[0].system == (
        "http://ema.europa.eu/example/contraindicationsasdisease-" "symptom-procedure"
    )
    assert inst.contraindication.diseaseSymptomProcedure.concept.text == (
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
    assert inst.type == "contraindication"


def test_clinicalusedefinition_1(base_settings):
    """No. 1 tests collection for ClinicalUseDefinition.
    Test File: clinicalusedefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "clinicalusedefinition-example.json"
    inst = clinicalusedefinition.ClinicalUseDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ClinicalUseDefinition" == inst.resource_type

    impl_clinicalusedefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ClinicalUseDefinition" == data["resourceType"]

    inst2 = clinicalusedefinition.ClinicalUseDefinition(**data)
    impl_clinicalusedefinition_1(inst2)
