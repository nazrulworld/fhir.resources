# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClinicalImpression
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import clinicalimpression


def impl_clinicalimpression_1(inst):
    assert inst.assessor.reference == "Practitioner/example"
    assert inst.date == fhirtypes.DateTime.validate("2014-12-06T22:33:00+11:00")
    assert inst.description == (
        "This 26 yo male patient is brought into ER by ambulance "
        "after being involved in a motor vehicle accident"
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate(
        "2014-12-06T22:33:00+11:00"
    )
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate(
        "2014-12-06T20:00:00+11:00"
    )
    assert inst.encounter.reference == "Encounter/example"
    assert inst.finding[0].itemCodeableConcept.coding[0].code == "850.0"
    assert (
        inst.finding[0].itemCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/sid/icd-9"
    )
    assert inst.id == "example"
    assert inst.identifier[0].value == "12345"
    assert inst.investigation[0].code.text == "Initial Examination"
    assert (
        inst.investigation[0].item[0].display
        == "deep laceration of the scalp (left temporo-occipital)"
    )
    assert inst.investigation[0].item[1].display == "decreased level of consciousness"
    assert inst.investigation[0].item[2].display == "disoriented to time and place"
    assert inst.investigation[0].item[3].display == "restless"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
    inst = clinicalimpression.ClinicalImpression.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ClinicalImpression" == inst.resource_type

    impl_clinicalimpression_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ClinicalImpression" == data["resourceType"]

    inst2 = clinicalimpression.ClinicalImpression(**data)
    impl_clinicalimpression_1(inst2)
