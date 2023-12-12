# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import researchsubject


def impl_researchsubject_1(inst):
    assert inst.actualComparisonGroup == "ap303"
    assert inst.assignedComparisonGroup == "placebo"
    assert inst.id == "example-crossover-placebo-to-drug"
    assert inst.identifier[0].value == "ecsr45"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.start == fhirtypes.DateTime.validate("2022-06-10")
    assert inst.progress[0].type.coding[0].code == "Enrollment"
    assert inst.progress[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/research-subject-" "state-type"
    )
    assert inst.progress[0].type.text == "Enrollment status"
    assert inst.progress[1].reason.coding[0].code == "informedConsentSigned"
    assert inst.progress[1].reason.text == "Informed consent signed"
    assert inst.progress[1].startDate == fhirtypes.DateTime.validate("2022-06-10")
    assert inst.progress[1].subjectState.coding[0].code == "on-study"
    assert (
        inst.progress[1].subjectState.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/research-subject-state"
    )
    assert inst.progress[1].subjectState.text == "On-study"
    assert inst.progress[1].type.coding[0].code == "Enrollment"
    assert inst.progress[1].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/research-subject-" "state-type"
    )
    assert inst.progress[1].type.text == "Enrollment status"
    assert inst.status == "active"
    assert inst.study.reference == "example-ctgov-study-record"
    assert inst.subject.reference == "cfsb1676546565857"
    assert inst.text.status == "generated"


def test_researchsubject_1(base_settings):
    """No. 1 tests collection for ResearchSubject.
    Test File: researchsubject-example-crossover-placebo-to-drug.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "researchsubject-example-crossover-placebo-to-drug.json"
    )
    inst = researchsubject.ResearchSubject.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ResearchSubject" == inst.resource_type

    impl_researchsubject_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ResearchSubject" == data["resourceType"]

    inst2 = researchsubject.ResearchSubject(**data)
    impl_researchsubject_1(inst2)
