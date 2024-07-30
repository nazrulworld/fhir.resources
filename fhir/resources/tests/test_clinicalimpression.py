# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalImpression
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import clinicalimpression
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_clinicalimpression_1(inst):
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-12-06T22:33:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "This 26 yo male patient is brought into ER by ambulance "
        "after being involved in a motor vehicle accident"
    )
    assert (
        inst.effectivePeriod.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-12-06T22:33:00+11:00"}
        ).valueDateTime
    )
    assert (
        inst.effectivePeriod.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-12-06T20:00:00+11:00"}
        ).valueDateTime
    )
    assert inst.encounter.reference == "Encounter/example"
    assert inst.finding[0].item.concept.coding[0].code == "850.0"
    assert (
        inst.finding[0].item.concept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/sid/icd-9"}
        ).valueUri
    )
    assert inst.id == "example"
    assert inst.identifier[0].value == "12345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.performer.reference == "Practitioner/example"
    assert inst.problem[0].display == "MVA"
    assert inst.status == "completed"
    assert inst.subject.reference == "Patient/example"
    assert inst.summary == (
        "provisional diagnoses of laceration of head and traumatic "
        "brain injury (TBI)"
    )
    assert inst.text.status == "generated"


def test_clinicalimpression_1(base_settings):
    """No. 1 tests collection for ClinicalImpression.
    Test File: clinicalimpression-example.json
    """
    filename = base_settings["unittest_data_dir"] / "clinicalimpression-example.json"
    inst = clinicalimpression.ClinicalImpression.model_validate_json(
        filename.read_bytes()
    )
    assert "ClinicalImpression" == inst.get_resource_type()

    impl_clinicalimpression_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ClinicalImpression" == data["resourceType"]

    inst2 = clinicalimpression.ClinicalImpression(**data)
    impl_clinicalimpression_1(inst2)
