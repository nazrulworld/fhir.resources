# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Goal
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import goal


def impl_goal_1(inst):
    assert inst.addresses[0].display == "obesity condition"
    assert inst.category[0].coding[0].code == "dietary"
    assert inst.category[0].coding[0].system == "http://hl7.org/fhir/goal-category"
    assert inst.description.text == "Target weight is 160 to 180 lbs."
    assert inst.expressedBy.display == "Peter James Chalmers"
    assert inst.expressedBy.reference == "Patient/example"
    assert inst.id == "example"
    assert inst.identifier[0].value == "123"
    assert inst.outcomeReference[0].display == "Body Weight Measured"
    assert inst.outcomeReference[0].reference == "Observation/example"
    assert inst.priority.coding[0].code == "high-priority"
    assert inst.priority.coding[0].display == "High Priority"
    assert inst.priority.coding[0].system == "http://hl7.org/fhir/goal-priority"
    assert inst.priority.text == "high"
    assert inst.startDate == fhirtypes.Date.validate("2015-04-05")
    assert inst.status == "on-hold"
    assert inst.statusDate == fhirtypes.Date.validate("2016-02-14")
    assert (
        inst.statusReason == "Patient wants to defer weight loss until after honeymoon."
    )
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.target.detailRange.high.code == "[lb_av]"
    assert inst.target.detailRange.high.system == "http://unitsofmeasure.org"
    assert inst.target.detailRange.high.unit == "lbs"
    assert float(inst.target.detailRange.high.value) == float(180)
    assert inst.target.detailRange.low.code == "[lb_av]"
    assert inst.target.detailRange.low.system == "http://unitsofmeasure.org"
    assert inst.target.detailRange.low.unit == "lbs"
    assert float(inst.target.detailRange.low.value) == float(160)
    assert inst.target.dueDate == fhirtypes.Date.validate("2016-04-05")
    assert inst.target.measure.coding[0].code == "3141-9"
    assert inst.target.measure.coding[0].display == "Weight Measured"
    assert inst.target.measure.coding[0].system == "http://loinc.org"
    assert inst.text.status == "additional"


def test_goal_1(base_settings):
    """No. 1 tests collection for Goal.
    Test File: goal-example.json
    """
    filename = base_settings["unittest_data_dir"] / "goal-example.json"
    inst = goal.Goal.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Goal" == inst.resource_type

    impl_goal_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Goal" == data["resourceType"]

    inst2 = goal.Goal(**data)
    impl_goal_1(inst2)


def impl_goal_2(inst):
    assert inst.description.text == "Stop smoking"
    assert inst.id == "stop-smoking"
    assert inst.identifier[0].value == "123"
    assert inst.outcomeCode[0].coding[0].code == "8517006"
    assert inst.outcomeCode[0].coding[0].display == "Ex-smoker (finding)"
    assert inst.outcomeCode[0].coding[0].system == "http://snomed.info/sct"
    assert inst.outcomeCode[0].text == "Former smoker"
    assert inst.startDate == fhirtypes.Date.validate("2015-04-05")
    assert inst.status == "achieved"
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "additional"


def test_goal_2(base_settings):
    """No. 2 tests collection for Goal.
    Test File: goal-example-stop-smoking.json
    """
    filename = base_settings["unittest_data_dir"] / "goal-example-stop-smoking.json"
    inst = goal.Goal.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Goal" == inst.resource_type

    impl_goal_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Goal" == data["resourceType"]

    inst2 = goal.Goal(**data)
    impl_goal_2(inst2)
