# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Goal
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import goal
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_goal_1(inst):
    assert inst.addresses[0].display == "obesity condition"
    assert inst.category[0].coding[0].code == "dietary"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/goal-category"}
        ).valueUri
    )
    assert inst.description.text == "Target weight is 160 to 180 lbs."
    assert inst.expressedBy.display == "Peter James Chalmers"
    assert inst.expressedBy.reference == "Patient/example"
    assert inst.id == "example"
    assert inst.identifier[0].value == "123"
    assert inst.lifecycleStatus == "on-hold"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.outcomeReference[0].display == "Body Weight Measured"
    assert inst.outcomeReference[0].reference == "Observation/example"
    assert inst.priority.coding[0].code == "high-priority"
    assert inst.priority.coding[0].display == "High Priority"
    assert (
        inst.priority.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/goal-priority"}
        ).valueUri
    )
    assert inst.priority.text == "high"
    assert (
        inst.startDate
        == ExternalValidatorModel.model_validate({"valueDate": "2015-04-05"}).valueDate
    )
    assert (
        inst.statusDate
        == ExternalValidatorModel.model_validate({"valueDate": "2016-02-14"}).valueDate
    )
    assert (
        inst.statusReason == "Patient wants to defer weight loss until after honeymoon."
    )
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.target[0].detailRange.high.code == "[lb_av]"
    assert (
        inst.target[0].detailRange.high.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.target[0].detailRange.high.unit == "lbs"
    assert float(inst.target[0].detailRange.high.value) == float(180)
    assert inst.target[0].detailRange.low.code == "[lb_av]"
    assert (
        inst.target[0].detailRange.low.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.target[0].detailRange.low.unit == "lbs"
    assert float(inst.target[0].detailRange.low.value) == float(160)
    assert (
        inst.target[0].dueDate
        == ExternalValidatorModel.model_validate({"valueDate": "2016-04-05"}).valueDate
    )
    assert inst.target[0].measure.coding[0].code == "3141-9"
    assert inst.target[0].measure.coding[0].display == "Weight Measured"
    assert (
        inst.target[0].measure.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.text.status == "additional"


def test_goal_1(base_settings):
    """No. 1 tests collection for Goal.
    Test File: goal-example.json
    """
    filename = base_settings["unittest_data_dir"] / "goal-example.json"
    inst = goal.Goal.model_validate_json(filename.read_bytes())
    assert "Goal" == inst.get_resource_type()

    impl_goal_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Goal" == data["resourceType"]

    inst2 = goal.Goal(**data)
    impl_goal_1(inst2)


def impl_goal_2(inst):
    assert inst.achievementStatus.coding[0].code == "achieved"
    assert inst.achievementStatus.coding[0].display == "Achieved"
    assert (
        inst.achievementStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/goal-achievement"}
        ).valueUri
    )
    assert inst.achievementStatus.text == "Achieved"
    assert inst.description.text == "Stop smoking"
    assert inst.id == "stop-smoking"
    assert inst.identifier[0].value == "123"
    assert inst.lifecycleStatus == "completed"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.outcomeCode[0].coding[0].code == "8517006"
    assert inst.outcomeCode[0].coding[0].display == "Ex-smoker (finding)"
    assert (
        inst.outcomeCode[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.outcomeCode[0].text == "Former smoker"
    assert (
        inst.startDate
        == ExternalValidatorModel.model_validate({"valueDate": "2015-04-05"}).valueDate
    )
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "additional"


def test_goal_2(base_settings):
    """No. 2 tests collection for Goal.
    Test File: goal-example-stop-smoking.json
    """
    filename = base_settings["unittest_data_dir"] / "goal-example-stop-smoking.json"
    inst = goal.Goal.model_validate_json(filename.read_bytes())
    assert "Goal" == inst.get_resource_type()

    impl_goal_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Goal" == data["resourceType"]

    inst2 = goal.Goal(**data)
    impl_goal_2(inst2)
