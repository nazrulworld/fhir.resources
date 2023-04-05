# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExampleScenario
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import examplescenario


def impl_examplescenario_1(inst):
    assert inst.actor[0].description == "The Nurse"
    assert inst.actor[0].key == "Nurse"
    assert inst.actor[0].title == "Nurse"
    assert inst.actor[0].type == "person"
    assert inst.actor[1].description == (
        "The entity that receives the Administration Requests to show"
        " the nurse to perform them"
    )
    assert inst.actor[1].key == "MAP"
    assert inst.actor[1].title == "Nurse's Tablet"
    assert inst.actor[1].type == "system"
    assert inst.actor[2].description == "The Medication Administration Order Placer"
    assert inst.actor[2].key == "OP"
    assert inst.actor[2].title == "MAR / Scheduler"
    assert inst.actor[2].type == "system"
    assert inst.actor[3].description == (
        "The entity that receives the Medication Administration " "reports"
    )
    assert inst.actor[3].key == "MAC"
    assert inst.actor[3].title == "MAR / EHR"
    assert inst.actor[3].type == "system"
    assert inst.id == "example"
    assert inst.instance[0].description == (
        'The initial prescription which describes "medication X, 3 '
        'times per day" - the exact scheduling is not   in the '
        "initial prescription (it is left for the care teams to "
        "decide on the schedule)."
    )
    assert inst.instance[0].key == "iherx001"
    assert inst.instance[0].structureType.code == "MedicationRequest"
    assert inst.instance[0].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[0].title == "Initial Prescription"
    assert (
        inst.instance[1].description == "The administration request for day 1, morning"
    )
    assert inst.instance[1].key == "iherx001.001"
    assert inst.instance[1].structureType.code == "MedicationRequest"
    assert inst.instance[1].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[1].title == "Request for day 1, morning"
    assert inst.instance[2].description == "The administration request for day 1, lunch"
    assert inst.instance[2].key == "iherx001.002"
    assert inst.instance[2].structureType.code == "MedicationRequest"
    assert inst.instance[2].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[2].title == "Request for day 1, lunch"
    assert (
        inst.instance[3].description == "The administration request for day 1, evening"
    )
    assert inst.instance[3].key == "iherx001.003"
    assert inst.instance[3].structureType.code == "MedicationRequest"
    assert inst.instance[3].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[3].title == "Request for day 1, evening"
    assert (
        inst.instance[4].description == "The administration request for day 2, morning"
    )
    assert inst.instance[4].key == "iherx001.004"
    assert inst.instance[4].structureType.code == "MedicationRequest"
    assert inst.instance[4].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[4].title == "Request for day 2, morning"
    assert inst.instance[5].description == "The administration request for day 2, lunch"
    assert inst.instance[5].key == "iherx001.005"
    assert inst.instance[5].structureType.code == "MedicationRequest"
    assert inst.instance[5].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[5].title == "Request for day 2, lunch"
    assert (
        inst.instance[6].description == "The administration request for day 2, evening"
    )
    assert inst.instance[6].key == "iherx001.006"
    assert inst.instance[6].structureType.code == "MedicationRequest"
    assert inst.instance[6].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[6].title == "Request for day 2, evening"
    assert (
        inst.instance[7].description
        == "Administration report for day 1, morning: Taken"
    )
    assert inst.instance[7].key == "iheadm001a"
    assert inst.instance[7].structureType.code == "MedicationAdministration"
    assert inst.instance[7].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[7].title == "Morning meds - taken"
    assert (
        inst.instance[8].description
        == "Administration report for day 1, morning: NOT Taken"
    )
    assert inst.instance[8].key == "iheadm001b"
    assert inst.instance[8].structureType.code == "MedicationAdministration"
    assert inst.instance[8].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[8].title == "Morning meds - not taken"
    assert inst.instance[9].containedInstance[0].instanceReference == "iherx001.001"
    assert inst.instance[9].containedInstance[1].instanceReference == "iherx001.002"
    assert inst.instance[9].containedInstance[2].instanceReference == "iherx001.003"
    assert inst.instance[9].containedInstance[3].instanceReference == "iherx001.004"
    assert inst.instance[9].containedInstance[4].instanceReference == "iherx001.005"
    assert inst.instance[9].containedInstance[5].instanceReference == "iherx001.006"
    assert inst.instance[9].description == "All the medication Requests for Day 1"
    assert inst.instance[9].key == "iherx001bundle"
    assert inst.instance[9].structureType.code == "MedicationRequest"
    assert inst.instance[9].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[9].title == "Bundle of Medication Requests"
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
    assert inst.process[0].step[0].number == "1"
    assert inst.process[0].step[0].operation.initiator == "Nurse"
    assert inst.process[0].step[0].operation.receiver == "MAP"
    assert inst.process[0].step[0].operation.title == "Get today's schedule"
    assert inst.process[0].step[1].number == "2"
    assert inst.process[0].step[1].operation.description == (
        "Query for medication administration orders,\\n- For today's "
        "shifts\\n- For today's patients"
    )
    assert inst.process[0].step[1].operation.initiator == "MAP"
    assert inst.process[0].step[1].operation.receiver == "OP"
    assert inst.process[0].step[1].operation.request.instanceReference == "iherxqry"
    assert (
        inst.process[0].step[1].operation.response.instanceReference == "iherx001bundle"
    )
    assert inst.process[0].step[1].operation.title == "Query administration orders"
    assert inst.process[0].step[1].pause is True
    assert inst.process[0].step[2].number == "3"
    assert inst.process[0].step[2].operation.initiator == "MAP"
    assert inst.process[0].step[2].operation.receiver == "Nurse"
    assert inst.process[0].step[2].operation.title == "Notify (alert)"
    assert inst.process[0].step[3].number == "4"
    assert inst.process[0].step[3].operation.initiator == "Nurse"
    assert inst.process[0].step[3].operation.receiver == "MAP"
    assert inst.process[0].step[3].operation.title == "Read orders"
    assert inst.process[0].step[3].pause is True
    assert inst.process[0].step[4].number == "5"
    assert inst.process[0].step[4].operation.initiator == "Nurse"
    assert inst.process[0].step[4].operation.receiver == "Nurse"
    assert inst.process[0].step[4].operation.title == "Ask if patient took meds"
    assert (
        inst.process[0].step[5].alternative[0].description
        == "Invoke if patient took medications"
    )
    assert inst.process[0].step[5].alternative[0].step[0].number == "6a"
    assert inst.process[0].step[5].alternative[0].step[0].operation.initiator == "Nurse"
    assert (
        inst.process[0].step[5].alternative[0].step[0].operation.initiatorActive is True
    )
    assert inst.process[0].step[5].alternative[0].step[0].operation.receiver == "MAP"
    assert (
        inst.process[0].step[5].alternative[0].step[0].operation.title
        == "Register meds taken"
    )
    assert inst.process[0].step[5].alternative[0].title == "Patient took meds"
    assert (
        inst.process[0].step[5].alternative[1].description
        == "No, patient did not take meds"
    )
    assert inst.process[0].step[5].alternative[1].step[0].number == "6b"
    assert inst.process[0].step[5].alternative[1].step[0].operation.initiator == "Nurse"
    assert (
        inst.process[0].step[5].alternative[1].step[0].operation.initiatorActive is True
    )
    assert inst.process[0].step[5].alternative[1].step[0].operation.receiver == "MAP"
    assert (
        inst.process[0].step[5].alternative[1].step[0].operation.title
        == "Register meds NOT taken"
    )
    assert inst.process[0].step[5].alternative[1].title == "No drugs"
    assert (
        inst.process[0].step[5].alternative[2].description
        == "Unknown whether patient took medications or not"
    )
    assert inst.process[0].step[5].alternative[2].title == "Not clear"
    assert inst.process[0].step[5].pause is True
    assert inst.process[0].step[6].number == "7"
    assert inst.process[0].step[6].operation.initiator == "Nurse"
    assert inst.process[0].step[6].operation.receiver == "Nurse"
    assert inst.process[0].step[6].operation.title == "Administer drug"
    assert inst.process[0].step[7].number == "8"
    assert inst.process[0].step[7].operation.initiator == "Nurse"
    assert inst.process[0].step[7].operation.initiatorActive is True
    assert inst.process[0].step[7].operation.receiver == "MAP"
    assert inst.process[0].step[7].operation.title == "Record administration"
    assert inst.process[0].step[7].pause is True
    assert inst.process[0].step[8].number == "9"
    assert inst.process[0].step[8].operation.initiator == "Nurse"
    assert inst.process[0].step[8].operation.initiatorActive is True
    assert inst.process[0].step[8].operation.receiver == "MAP"
    assert inst.process[0].step[8].operation.request.instanceReference == "iheadm002"
    assert inst.process[0].step[8].operation.request.versionReference == "iheadm002v1"
    assert inst.process[0].step[8].operation.title == "Upload administration reports"
    assert inst.process[0].step[8].pause is True
    assert inst.process[0].step[9].number == "10"
    assert inst.process[0].step[9].operation.description == (
        "The nurse's system uploads the administration results to the" " server"
    )
    assert inst.process[0].step[9].operation.initiator == "MAP"
    assert inst.process[0].step[9].operation.receiver == "MAC"
    assert inst.process[0].step[9].operation.request.instanceReference == "iheadm001a"
    assert inst.process[0].step[9].operation.title == "Upload administration reports"
    assert inst.process[0].title == "Mobile Medication Administration"
    assert inst.status == "draft"
    assert inst.text.status == "additional"


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


def impl_examplescenario_2(inst):
    assert inst.actor[0].description == "Clinician"
    assert inst.actor[0].key == "Clin"
    assert inst.actor[0].title == "Clinician"
    assert inst.actor[0].type == "person"
    assert inst.actor[1].description == "CPOE"
    assert inst.actor[1].key == "CPOE"
    assert inst.actor[1].title == "CPOE"
    assert inst.actor[1].type == "system"
    assert inst.actor[2].description == "EMR"
    assert inst.actor[2].key == "EMR"
    assert inst.actor[2].title == "EMR"
    assert inst.actor[2].type == "system"
    assert inst.actor[3].description == "Lab Person"
    assert inst.actor[3].key == "LabMan"
    assert inst.actor[3].title == "Lab Man"
    assert inst.actor[3].type == "person"
    assert inst.actor[4].description == "Lab"
    assert inst.actor[4].key == "Lab"
    assert inst.actor[4].title == "Lab"
    assert inst.actor[4].type == "system"
    assert inst.description == (
        "In this example, the clinician creates an order in the CPOE."
        " Then a Task is created and updated by both the CPOE and the"
        " Lab system..."
    )
    assert inst.id == "example-laborder"
    assert inst.instance[0].description == "Bla"
    assert inst.instance[0].key == "req1"
    assert inst.instance[0].structureType.code == "ServiceRequest"
    assert inst.instance[0].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[0].title == "Request for a lab procedure"
    assert inst.instance[0].version[0].description == "Initial order"
    assert inst.instance[0].version[0].key == "req1-v1"
    assert inst.instance[0].version[0].title == "v1- initial"
    assert inst.instance[0].version[1].description == "Order in progress"
    assert inst.instance[0].version[1].key == "req1-v2"
    assert inst.instance[0].version[1].title == "v2 - in progress"
    assert inst.instance[0].version[2].description == "Order completed"
    assert inst.instance[0].version[2].key == "req1-v3"
    assert inst.instance[0].version[2].title == "v3 - completed"
    assert inst.instance[1].description == "The task that handles the status updates..."
    assert inst.instance[1].key == "task1"
    assert inst.instance[1].structureType.code == "Task"
    assert inst.instance[1].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[1].title == "Task"
    assert inst.instance[1].version[0].description == "Initially created"
    assert inst.instance[1].version[0].key == "task1-v1"
    assert inst.instance[1].version[0].title == "v1 - created"
    assert inst.instance[1].version[1].description == "Accepted"
    assert inst.instance[1].version[1].key == "task1-v2"
    assert inst.instance[1].version[1].title == "v2 - accepted"
    assert inst.instance[1].version[2].description == "In progress"
    assert inst.instance[1].version[2].key == "task1-v3"
    assert inst.instance[1].version[2].title == "v3 - in progress"
    assert inst.instance[1].version[3].description == "Completed"
    assert inst.instance[1].version[3].key == "task1-v4"
    assert inst.instance[1].version[3].title == "v4 - completed"
    assert inst.instance[2].description == "Lab's internal request for the procedure"
    assert inst.instance[2].key == "req.lab1"
    assert inst.instance[2].structureType.code == "ServiceRequest"
    assert inst.instance[2].structureType.system == "http://hl7.org/fhir/fhir-types"
    assert inst.instance[2].title == "Internal lab request"
    assert inst.instance[2].version[0].description == "Order in progress"
    assert inst.instance[2].version[0].key == "req.lab1-v1"
    assert inst.instance[2].version[0].title == "v1 - created"
    assert inst.instance[2].version[1].description == "Order in progress"
    assert inst.instance[2].version[1].key == "req.lab1-v2"
    assert inst.instance[2].version[1].title == "v2 - in progress"
    assert inst.instance[2].version[2].description == "Order completed"
    assert inst.instance[2].version[2].key == "req.lab1-v3"
    assert inst.instance[2].version[2].title == "v3 - completed"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "LabOrderTrackingWithTask"
    assert inst.process[0].description == (
        "Lab order, status updates handled with Task between CPOE, "
        "EMR and Lab systems"
    )
    assert inst.process[0].step[0].number == "1"
    assert inst.process[0].step[0].pause is True
    assert inst.process[0].step[0].process.description == "New lab order"
    assert inst.process[0].step[0].process.step[0].number == "1.1"
    assert inst.process[0].step[0].process.step[0].operation.initiator == "Clin"
    assert inst.process[0].step[0].process.step[0].operation.receiver == "LabMan"
    assert inst.process[0].step[0].process.step[0].operation.title == "Make a call"
    assert inst.process[0].step[0].process.step[1].number == "1.2"
    assert inst.process[0].step[0].process.step[1].operation.initiator == "Clin"
    assert inst.process[0].step[0].process.step[1].operation.receiver == "CPOE"
    assert (
        inst.process[0].step[0].process.step[1].operation.title
        == "Create new EMR order"
    )
    assert inst.process[0].step[0].process.step[2].number == "1.3"
    assert inst.process[0].step[0].process.step[2].operation.initiator == "CPOE"
    assert inst.process[0].step[0].process.step[2].operation.receiver == "EMR"
    assert (
        inst.process[0].step[0].process.step[2].operation.request.instanceReference
        == "req1"
    )
    assert (
        inst.process[0].step[0].process.step[2].operation.request.versionReference
        == "req1-v1"
    )
    assert (
        inst.process[0].step[0].process.step[2].operation.title == "Submit order to EMR"
    )
    assert inst.process[0].step[0].process.step[3].number == "1.3"
    assert inst.process[0].step[0].process.step[3].operation.initiator == "EMR"
    assert inst.process[0].step[0].process.step[3].operation.receiver == "EMR"
    assert (
        inst.process[0].step[0].process.step[3].operation.request.instanceReference
        == "task1"
    )
    assert (
        inst.process[0].step[0].process.step[3].operation.request.versionReference
        == "task1-v1"
    )
    assert inst.process[0].step[0].process.step[3].operation.title == "Create new task "
    assert inst.process[0].step[0].process.step[4].number == "1.4"
    assert inst.process[0].step[0].process.step[4].operation.initiator == "EMR"
    assert inst.process[0].step[0].process.step[4].operation.receiver == "Lab"
    assert (
        inst.process[0].step[0].process.step[4].operation.request.instanceReference
        == "task1"
    )
    assert (
        inst.process[0].step[0].process.step[4].operation.request.versionReference
        == "task1-v1"
    )
    assert inst.process[0].step[0].process.step[4].operation.title == "Send task to Lab"
    assert inst.process[0].step[0].process.title == "Create order"
    assert inst.process[0].step[1].number == "2"
    assert (
        inst.process[0].step[1].process.description
        == "New task for handling order tracking"
    )
    assert inst.process[0].step[1].process.step[0].number == "2.1"
    assert inst.process[0].step[1].process.step[0].operation.initiator == "LabMan"
    assert inst.process[0].step[1].process.step[0].operation.receiver == "Lab"
    assert inst.process[0].step[1].process.step[0].operation.title == "Accept task"
    assert inst.process[0].step[1].process.step[1].number == "2.2"
    assert inst.process[0].step[1].process.step[1].operation.initiator == "Lab"
    assert inst.process[0].step[1].process.step[1].operation.receiver == "Lab"
    assert (
        inst.process[0].step[1].process.step[1].operation.request.instanceReference
        == "task1"
    )
    assert (
        inst.process[0].step[1].process.step[1].operation.request.versionReference
        == "task1-v2"
    )
    assert (
        inst.process[0].step[1].process.step[1].operation.title
        == "Task status = accepted"
    )
    assert inst.process[0].step[1].process.step[2].number == "2.3"
    assert inst.process[0].step[1].process.step[2].operation.initiator == "Lab"
    assert inst.process[0].step[1].process.step[2].operation.receiver == "Lab"
    assert (
        inst.process[0].step[1].process.step[2].operation.request.instanceReference
        == "req.lab1"
    )
    assert (
        inst.process[0].step[1].process.step[2].operation.request.versionReference
        == "req.lab1-v1"
    )
    assert (
        inst.process[0].step[1].process.step[2].operation.title
        == "Create internal lab request"
    )
    assert inst.process[0].step[1].process.step[3].number == "2.4"
    assert inst.process[0].step[1].process.step[3].operation.initiator == "Lab"
    assert inst.process[0].step[1].process.step[3].operation.receiver == "EMR"
    assert (
        inst.process[0].step[1].process.step[3].operation.request.instanceReference
        == "task1"
    )
    assert (
        inst.process[0].step[1].process.step[3].operation.request.versionReference
        == "task1-v2"
    )
    assert inst.process[0].step[1].process.step[3].operation.title == "Send Task to EMR"
    assert inst.process[0].step[1].process.step[4].number == "2.5"
    assert inst.process[0].step[1].process.step[4].operation.initiator == "EMR"
    assert inst.process[0].step[1].process.step[4].operation.receiver == "CPOE"
    assert (
        inst.process[0].step[1].process.step[4].operation.request.instanceReference
        == "task1"
    )
    assert (
        inst.process[0].step[1].process.step[4].operation.request.versionReference
        == "task1-v2"
    )
    assert (
        inst.process[0].step[1].process.step[4].operation.title
        == "Inform CPOE of Task status"
    )
    assert inst.process[0].step[1].process.title == "Accept order"
    assert inst.process[0].step[2].number == "3"
    assert (
        inst.process[0].step[2].process.description
        == "Procedure is initiated at the lab"
    )
    assert inst.process[0].step[2].process.step[0].number == "3.1"
    assert inst.process[0].step[2].process.step[0].operation.initiator == "LabMan"
    assert inst.process[0].step[2].process.step[0].operation.receiver == "Lab"
    assert inst.process[0].step[2].process.step[0].operation.title == "Begin procedure"
    assert inst.process[0].step[2].process.step[1].number == "3.2"
    assert inst.process[0].step[2].process.step[1].operation.initiator == "Lab"
    assert inst.process[0].step[2].process.step[1].operation.receiver == "Lab"
    assert (
        inst.process[0].step[2].process.step[1].operation.request.instanceReference
        == "task1"
    )
    assert (
        inst.process[0].step[2].process.step[1].operation.request.versionReference
        == "task1-v3"
    )
    assert (
        inst.process[0].step[2].process.step[1].operation.title
        == "Task status: in-progress"
    )
    assert inst.process[0].step[2].process.step[2].number == "4.3"
    assert inst.process[0].step[2].process.step[2].operation.initiator == "Lab"
    assert inst.process[0].step[2].process.step[2].operation.receiver == "Lab"
    assert (
        inst.process[0].step[2].process.step[2].operation.request.instanceReference
        == "req.lab1"
    )
    assert (
        inst.process[0].step[2].process.step[2].operation.request.versionReference
        == "req.lab1-v2"
    )
    assert (
        inst.process[0].step[2].process.step[2].operation.title
        == "Internal lab request: in-progress"
    )
    assert inst.process[0].step[2].process.step[3].number == "4.4"
    assert inst.process[0].step[2].process.step[3].operation.initiator == "Lab"
    assert inst.process[0].step[2].process.step[3].operation.receiver == "EMR"
    assert (
        inst.process[0].step[2].process.step[3].operation.request.instanceReference
        == "task1"
    )
    assert (
        inst.process[0].step[2].process.step[3].operation.request.versionReference
        == "task1-v3"
    )
    assert (
        inst.process[0].step[2].process.step[3].operation.title
        == "Send updated Task to EMR"
    )
    assert inst.process[0].step[2].process.step[4].number == "4.5"
    assert inst.process[0].step[2].process.step[4].operation.initiator == "EMR"
    assert inst.process[0].step[2].process.step[4].operation.receiver == "CPOE"
    assert (
        inst.process[0].step[2].process.step[4].operation.request.instanceReference
        == "task1"
    )
    assert (
        inst.process[0].step[2].process.step[4].operation.request.versionReference
        == "task1-v4"
    )
    assert (
        inst.process[0].step[2].process.step[4].operation.title
        == "Inform CPOE of Task status"
    )
    assert inst.process[0].step[2].process.step[5].number == "4.5"
    assert inst.process[0].step[2].process.step[5].operation.initiator == "CPOE"
    assert inst.process[0].step[2].process.step[5].operation.receiver == "CPOE"
    assert (
        inst.process[0].step[2].process.step[5].operation.request.instanceReference
        == "req1"
    )
    assert (
        inst.process[0].step[2].process.step[5].operation.request.versionReference
        == "req1-v2"
    )
    assert (
        inst.process[0].step[2].process.step[5].operation.title
        == "Order status: in-progress"
    )
    assert inst.process[0].step[2].process.title == "Initiate procedure"
    assert inst.process[0].step[3].number == "4"
    assert inst.process[0].step[3].process.description == "Procedure is finished"
    assert inst.process[0].step[3].process.step[0].number == "4.1"
    assert inst.process[0].step[3].process.step[0].operation.initiator == "LabMan"
    assert inst.process[0].step[3].process.step[0].operation.receiver == "Lab"
    assert inst.process[0].step[3].process.step[0].operation.title == "Finish procedure"
    assert inst.process[0].step[3].process.step[1].number == "4.2"
    assert inst.process[0].step[3].process.step[1].operation.initiator == "Lab"
    assert inst.process[0].step[3].process.step[1].operation.receiver == "Lab"
    assert (
        inst.process[0].step[3].process.step[1].operation.request.instanceReference
        == "task1"
    )
    assert (
        inst.process[0].step[3].process.step[1].operation.request.versionReference
        == "task1-v2"
    )
    assert (
        inst.process[0].step[3].process.step[1].operation.title
        == "Task status = completed"
    )
    assert inst.process[0].step[3].process.step[2].number == "4.3"
    assert inst.process[0].step[3].process.step[2].operation.initiator == "Lab"
    assert inst.process[0].step[3].process.step[2].operation.receiver == "Lab"
    assert (
        inst.process[0].step[3].process.step[2].operation.request.instanceReference
        == "req.lab1"
    )
    assert (
        inst.process[0].step[3].process.step[2].operation.request.versionReference
        == "req.lab1-v2"
    )
    assert (
        inst.process[0].step[3].process.step[2].operation.title
        == "Internal lab request: complete"
    )
    assert inst.process[0].step[3].process.step[3].number == "4.4"
    assert inst.process[0].step[3].process.step[3].operation.initiator == "Lab"
    assert inst.process[0].step[3].process.step[3].operation.receiver == "EMR"
    assert (
        inst.process[0].step[3].process.step[3].operation.request.instanceReference
        == "task1"
    )
    assert (
        inst.process[0].step[3].process.step[3].operation.request.versionReference
        == "task1-v4"
    )
    assert (
        inst.process[0].step[3].process.step[3].operation.title
        == "Send updated Task to EMR"
    )
    assert inst.process[0].step[3].process.step[4].number == "4.5"
    assert inst.process[0].step[3].process.step[4].operation.initiator == "EMR"
    assert inst.process[0].step[3].process.step[4].operation.receiver == "CPOE"
    assert (
        inst.process[0].step[3].process.step[4].operation.request.instanceReference
        == "task1"
    )
    assert (
        inst.process[0].step[3].process.step[4].operation.request.versionReference
        == "task1-v4"
    )
    assert (
        inst.process[0].step[3].process.step[4].operation.title
        == "Inform CPOE of Task status"
    )
    assert inst.process[0].step[3].process.step[5].number == "4.5"
    assert inst.process[0].step[3].process.step[5].operation.initiator == "CPOE"
    assert inst.process[0].step[3].process.step[5].operation.receiver == "CPOE"
    assert (
        inst.process[0].step[3].process.step[5].operation.request.instanceReference
        == "req1"
    )
    assert (
        inst.process[0].step[3].process.step[5].operation.request.versionReference
        == "req1-v3"
    )
    assert (
        inst.process[0].step[3].process.step[5].operation.title
        == "Order status = completed"
    )
    assert inst.process[0].step[3].process.title == "Finish procedure"
    assert inst.process[0].title == "Lab order tracking with Task"
    assert inst.purpose == (
        "Purpose: this serves to demonstrate a scenario that uses "
        "service requests and Task resources to establish a handshake"
        " for order tracking."
    )
    assert inst.status == "draft"
    assert inst.text.status == "additional"
    assert inst.title == "Lab order tracking with Task"


def test_examplescenario_2(base_settings):
    """No. 2 tests collection for ExampleScenario.
    Test File: examplescenario-example-laborder.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "examplescenario-example-laborder.json"
    )
    inst = examplescenario.ExampleScenario.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ExampleScenario" == inst.resource_type

    impl_examplescenario_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ExampleScenario" == data["resourceType"]

    inst2 = examplescenario.ExampleScenario(**data)
    impl_examplescenario_2(inst2)
