# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RequestOrchestration
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import requestorchestration


def impl_requestorchestration_1(inst):
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[0]
        .extension[0]
        .extension[0]
        .url
        == "day"
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[0]
        .extension[0]
        .extension[0]
        .valueInteger
        == 1
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[0]
        .extension[0]
        .extension[1]
        .url
        == "day"
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[0]
        .extension[0]
        .extension[1]
        .valueInteger
        == 8
    )
    assert (
        inst.action[0].action[0].action[0].action[0].action[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"
    )
    assert inst.action[0].action[0].action[0].action[0].action[0].id == "action-1"
    assert (
        inst.action[0].action[0].action[0].action[0].action[0].resource.reference
        == "#1111"
    )
    assert (
        inst.action[0].action[0].action[0].action[0].action[0].textEquivalent
        == "Gemcitabine 1250 mg/m² IV over 30 minutes on days 1 and 8"
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[1]
        .extension[0]
        .extension[0]
        .url
        == "day"
    )
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[1]
        .extension[0]
        .extension[0]
        .valueInteger
        == 1
    )
    assert (
        inst.action[0].action[0].action[0].action[0].action[1].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle"
    )
    assert inst.action[0].action[0].action[0].action[0].action[1].id == "action-2"
    assert (
        inst.action[0]
        .action[0]
        .action[0]
        .action[0]
        .action[1]
        .relatedAction[0]
        .relationship
        == "concurrent-with-start"
    )
    assert (
        inst.action[0].action[0].action[0].action[0].action[1].relatedAction[0].targetId
        == "action-1"
    )
    assert (
        inst.action[0].action[0].action[0].action[0].action[1].resource.reference
        == "#2222"
    )
    assert (
        inst.action[0].action[0].action[0].action[0].action[1].textEquivalent
        == "CARBOplatin AUC 5 IV over 30 minutes on Day 1"
    )
    assert inst.action[0].action[0].action[0].action[0].id == "cycle-definition-1"
    assert (
        inst.action[0].action[0].action[0].action[0].textEquivalent
        == "21-day cycle for 6 cycles"
    )
    assert inst.action[0].action[0].action[0].action[0].timingTiming.repeat.count == 6
    assert float(
        inst.action[0].action[0].action[0].action[0].timingTiming.repeat.duration
    ) == float(21)
    assert (
        inst.action[0].action[0].action[0].action[0].timingTiming.repeat.durationUnit
        == "d"
    )
    assert inst.action[0].action[0].action[0].groupingBehavior == "sentence-group"
    assert inst.action[0].action[0].action[0].selectionBehavior == "exactly-one"
    assert inst.action[0].action[0].selectionBehavior == "all"
    assert inst.action[0].selectionBehavior == "exactly-one"
    assert inst.author.reference == "Practitioner/1"
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-03-06T17:31:00Z")
    assert inst.contained[0].id == "1111"
    assert inst.contained[1].id == "2222"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "kdn5-example"
    assert inst.identifier[0].value == "requestorchestration-kdn5"
    assert (
        inst.instantiatesCanonical[0] == "http://example.org/fhir/PlanDefinition/KDN5"
    )
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.priority == "routine"
    assert inst.status == "draft"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Administer '
        "gemcitabine and carboplatin.</div>"
    )
    assert inst.text.status == "generated"


def test_requestorchestration_1(base_settings):
    """No. 1 tests collection for RequestOrchestration.
    Test File: requestorchestration-kdn5-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "requestorchestration-kdn5-example.json"
    )
    inst = requestorchestration.RequestOrchestration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RequestOrchestration" == inst.resource_type

    impl_requestorchestration_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RequestOrchestration" == data["resourceType"]

    inst2 = requestorchestration.RequestOrchestration(**data)
    impl_requestorchestration_1(inst2)


def impl_requestorchestration_2(inst):
    assert inst.action[0].action[0].description == "Administer medication 1"
    assert inst.action[0].action[0].id == "medication-action-1"
    assert inst.action[0].action[0].resource.reference == "#medicationrequest-1"
    assert inst.action[0].action[0].type.coding[0].code == "create"
    assert inst.action[0].action[1].description == "Administer medication 2"
    assert inst.action[0].action[1].id == "medication-action-2"
    assert inst.action[0].action[1].relatedAction[0].offsetDuration.unit == "h"
    assert float(
        inst.action[0].action[1].relatedAction[0].offsetDuration.value
    ) == float(1)
    assert inst.action[0].action[1].relatedAction[0].relationship == "after-end"
    assert inst.action[0].action[1].relatedAction[0].targetId == "medication-action-1"
    assert inst.action[0].action[1].resource.reference == "#medicationrequest-2"
    assert inst.action[0].action[1].type.coding[0].code == "create"
    assert inst.action[0].cardinalityBehavior == "single"
    assert (
        inst.action[0].description == "Administer medications at the appropriate time"
    )
    assert inst.action[0].groupingBehavior == "logical-group"
    assert inst.action[0].participant[0].actorReference.reference == "Practitioner/1"
    assert inst.action[0].precheckBehavior == "yes"
    assert inst.action[0].prefix == "1"
    assert inst.action[0].requiredBehavior == "must"
    assert inst.action[0].selectionBehavior == "all"
    assert inst.action[0].textEquivalent == (
        "Administer medication 1, followed an hour later by " "medication 2"
    )
    assert inst.action[0].timingDateTime == fhirtypes.DateTime.validate(
        "2017-03-06T19:00:00Z"
    )
    assert inst.action[0].title == "Administer Medications"
    assert inst.author.reference == "Practitioner/1"
    assert inst.authoredOn == fhirtypes.DateTime.validate("2017-03-06T17:31:00Z")
    assert inst.contained[0].id == "medicationrequest-1"
    assert inst.contained[1].id == "medicationrequest-2"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.groupIdentifier.system == "http://example.org/treatment-group"
    assert inst.groupIdentifier.value == "00001"
    assert inst.id == "example"
    assert inst.identifier[0].value == "requestorchestration-1"
    assert inst.intent == "plan"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "Additional notes about the request group"
    assert inst.priority == "routine"
    assert inst.reason[0].concept.text == "Treatment"
    assert inst.status == "draft"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Example '
        "RequestOrchestration illustrating related actions to "
        "administer medications in sequence with time delay.</div>"
    )
    assert inst.text.status == "generated"


def test_requestorchestration_2(base_settings):
    """No. 2 tests collection for RequestOrchestration.
    Test File: requestorchestration-example.json
    """
    filename = base_settings["unittest_data_dir"] / "requestorchestration-example.json"
    inst = requestorchestration.RequestOrchestration.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RequestOrchestration" == inst.resource_type

    impl_requestorchestration_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RequestOrchestration" == data["resourceType"]

    inst2 = requestorchestration.RequestOrchestration(**data)
    impl_requestorchestration_2(inst2)
