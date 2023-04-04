# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExampleScenario
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import examplescenario


def impl_examplescenario_1(inst):
    assert inst.actor[0].actorId == "Nurse"
    assert inst.actor[0].description == "The Nurse"
    assert inst.actor[0].name == "Nurse"
    assert inst.actor[0].type == "person"
    assert inst.actor[1].actorId == "MAP"
    assert inst.actor[1].description == (
        "The entity that receives the Administration Requests to show"
        " the nurse to perform them"
    )
    assert inst.actor[1].name == "Nurse's Tablet"
    assert inst.actor[1].type == "entity"
    assert inst.actor[2].actorId == "OP"
    assert inst.actor[2].description == "The Medication Administration Order Placer"
    assert inst.actor[2].name == "MAR / Scheduler"
    assert inst.actor[2].type == "entity"
    assert inst.actor[3].actorId == "MAC"
    assert inst.actor[3].description == (
        "The entity that receives the Medication Administration " "reports"
    )
    assert inst.actor[3].name == "MAR / EHR"
    assert inst.actor[3].type == "entity"
    assert inst.experimental is True
    assert inst.id == "example"
    assert inst.instance[0].description == (
        'The initial prescription which describes "medication X, 3 '
        'times per day" - the exact scheduling is not   in the '
        "initial prescription (it is left for the care teams to "
        "decide on the schedule)."
    )
    assert inst.instance[0].name == "Initial Prescription"
    assert inst.instance[0].resourceId == "iherx001"
    assert (
        inst.instance[1].description == "The administration request for day 1, morning"
    )
    assert inst.instance[1].name == "Request for day 1, morning"
    assert inst.instance[1].resourceId == "iherx001.001"
    assert inst.instance[2].description == "The administration request for day 1, lunch"
    assert inst.instance[2].name == "Request for day 1, lunch"
    assert inst.instance[2].resourceId == "iherx001.002"
    assert (
        inst.instance[3].description == "The administration request for day 1, evening"
    )
    assert inst.instance[3].name == "Request for day 1, evening"
    assert inst.instance[3].resourceId == "iherx001.003"
    assert (
        inst.instance[4].description == "The administration request for day 2, morning"
    )
    assert inst.instance[4].name == "Request for day 2, morning"
    assert inst.instance[4].resourceId == "iherx001.004"
    assert inst.instance[5].description == "The administration request for day 2, lunch"
    assert inst.instance[5].name == "Request for day 2, lunch"
    assert inst.instance[5].resourceId == "iherx001.005"
    assert (
        inst.instance[6].description == "The administration request for day 2, evening"
    )
    assert inst.instance[6].name == "Request for day 2, evening"
    assert inst.instance[6].resourceId == "iherx001.006"
    assert (
        inst.instance[7].description
        == "Administration report for day 1, morning: Taken"
    )
    assert inst.instance[7].name == "Morning meds - taken"
    assert inst.instance[7].resourceId == "iheadm001a"
    assert (
        inst.instance[8].description
        == "Administration report for day 1, morning: NOT Taken"
    )
    assert inst.instance[8].name == "Morning meds - not taken"
    assert inst.instance[8].resourceId == "iheadm001b"
    assert inst.instance[9].containedInstance[0].resourceId == "iherx001.001"
    assert inst.instance[9].containedInstance[1].resourceId == "iherx001.002"
    assert inst.instance[9].containedInstance[2].resourceId == "iherx001.003"
    assert inst.instance[9].containedInstance[3].resourceId == "iherx001.004"
    assert inst.instance[9].containedInstance[4].resourceId == "iherx001.005"
    assert inst.instance[9].containedInstance[5].resourceId == "iherx001.006"
    assert inst.instance[9].description == "All the medication Requests for Day 1"
    assert inst.instance[9].name == "Bundle of Medication Requests"
    assert inst.instance[9].resourceId == "iherx001bundle"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.process[0].postConditions == (
        "Medication administration Reports are submitted, EHR is " "updated."
    )
    assert inst.process[0].preConditions == (
        "Medication administration requests are in the EHR / MAR, "
        "scheduled for each individual intake."
    )
    assert inst.process[0].step[0].operation.initiator == "Nurse"
    assert inst.process[0].step[0].operation.name == "1. Get today's schedule"
    assert inst.process[0].step[0].operation.number == "1"
    assert inst.process[0].step[0].operation.receiver == "MAP"
    assert inst.process[0].step[1].process[0].description == (
        "Query for medication administration orders,\\n- For today's "
        "shifts\\n- For today's patients"
    )
    assert inst.process[0].step[1].process[0].step[0].operation.initiator == "MAP"
    assert inst.process[0].step[1].process[0].step[0].operation.name == (
        "2.Query for medication administration orders,\\n- For "
        "today's shifts\\n- For today's patients"
    )
    assert inst.process[0].step[1].process[0].step[0].operation.number == "2"
    assert inst.process[0].step[1].process[0].step[0].operation.receiver == "OP"
    assert (
        inst.process[0].step[1].process[0].step[0].operation.request.resourceId
        == "iherxqry"
    )
    assert (
        inst.process[0].step[1].process[0].step[0].operation.response.resourceId
        == "iherx001bundle"
    )
    assert (
        inst.process[0].step[1].process[0].title == "P1. Query Administration Requests"
    )
    assert inst.process[0].step[2].pause is True
    assert inst.process[0].step[3].operation.initiator == "MAP"
    assert inst.process[0].step[3].operation.name == "Notify (alert)"
    assert inst.process[0].step[3].operation.number == "4"
    assert inst.process[0].step[3].operation.receiver == "Nurse"
    assert inst.process[0].step[4].operation.initiator == "Nurse"
    assert inst.process[0].step[4].operation.name == "Read orders"
    assert inst.process[0].step[4].operation.number == "5"
    assert inst.process[0].step[4].operation.receiver == "MAP"
    assert inst.process[0].step[5].pause is True
    assert inst.process[0].step[6].operation.initiator == "Nurse"
    assert inst.process[0].step[6].operation.name == "Ask if patient took meds"
    assert inst.process[0].step[6].operation.number == "5"
    assert inst.process[0].step[6].operation.receiver == "Nurse"
    assert (
        inst.process[0].step[7].alternative[0].description
        == "Invoke if patient took medications"
    )
    assert (
        inst.process[0]
        .step[7]
        .alternative[0]
        .step[0]
        .process[0]
        .step[0]
        .operation.initiator
        == "Nurse"
    )
    assert (
        inst.process[0]
        .step[7]
        .alternative[0]
        .step[0]
        .process[0]
        .step[0]
        .operation.initiatorActive
        is True
    )
    assert (
        inst.process[0].step[7].alternative[0].step[0].process[0].step[0].operation.name
        == "Register Meds taken"
    )
    assert (
        inst.process[0]
        .step[7]
        .alternative[0]
        .step[0]
        .process[0]
        .step[0]
        .operation.number
        == "1a"
    )
    assert (
        inst.process[0]
        .step[7]
        .alternative[0]
        .step[0]
        .process[0]
        .step[0]
        .operation.receiver
        == "MAP"
    )
    assert (
        inst.process[0].step[7].alternative[0].step[0].process[0].title
        == "Register Meds taken"
    )
    assert inst.process[0].step[7].alternative[0].title == "Patient took drugs"
    assert (
        inst.process[0].step[7].alternative[1].description
        == "No, patient did not take drugs"
    )
    assert (
        inst.process[0]
        .step[7]
        .alternative[1]
        .step[0]
        .process[0]
        .step[0]
        .operation.initiator
        == "Nurse"
    )
    assert (
        inst.process[0]
        .step[7]
        .alternative[1]
        .step[0]
        .process[0]
        .step[0]
        .operation.initiatorActive
        is True
    )
    assert (
        inst.process[0].step[7].alternative[1].step[0].process[0].step[0].operation.name
        == "Register Meds NOT taken"
    )
    assert (
        inst.process[0]
        .step[7]
        .alternative[1]
        .step[0]
        .process[0]
        .step[0]
        .operation.number
        == "1b"
    )
    assert (
        inst.process[0]
        .step[7]
        .alternative[1]
        .step[0]
        .process[0]
        .step[0]
        .operation.receiver
        == "MAP"
    )
    assert (
        inst.process[0].step[7].alternative[1].step[0].process[0].title
        == "Register Meds NOT taken"
    )
    assert inst.process[0].step[7].alternative[1].title == "No drugs"
    assert (
        inst.process[0].step[7].alternative[2].description
        == "Unknown whether patient took medications or not"
    )
    assert inst.process[0].step[7].alternative[2].step[0].pause is True
    assert inst.process[0].step[7].alternative[2].title == "Not clear"
    assert inst.process[0].step[8].pause is True
    assert inst.process[0].step[9].operation.initiator == "Nurse"
    assert inst.process[0].step[9].operation.name == "Administer drug"
    assert inst.process[0].step[9].operation.number == "6"
    assert inst.process[0].step[9].operation.receiver == "Nurse"
    assert inst.process[0].title == "Mobile Medication Administration"
    assert inst.status == "draft"
    assert inst.text.status == "generated"


def test_examplescenario_1(base_settings):
    """No. 1 tests collection for ExampleScenario.
    Test File: examplescenario-example.json
    """
    filename = base_settings["unittest_data_dir"] / "examplescenario-example.json"
    inst = examplescenario.ExampleScenario.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ExampleScenario" == inst.resource_type

    impl_examplescenario_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ExampleScenario" == data["resourceType"]

    inst2 = examplescenario.ExampleScenario(**data)
    impl_examplescenario_1(inst2)
