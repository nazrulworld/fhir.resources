# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubscriptionTopic
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import subscriptiontopic


def impl_subscriptiontopic_1(inst):
    assert inst.canFilterBy[0].description == (
        "Matching based on the Patient (subject) of an Encounter or "
        "based on the Patient's group membership (in/not-in)."
    )
    assert inst.canFilterBy[0].filterParameter == "patient"
    assert inst.canFilterBy[0].modifier[0] == "="
    assert inst.canFilterBy[0].modifier[1] == "in"
    assert inst.canFilterBy[0].modifier[2] == "not-in"
    assert inst.canFilterBy[0].resource == "Encounter"
    assert inst.description == "Example admission topic"
    assert (
        inst.eventTrigger[0].description
        == "Patient admission is covered by HL7v2 ADT^A01"
    )
    assert inst.eventTrigger[0].event.coding[0].code == "A01"
    assert (
        inst.eventTrigger[0].event.coding[0].display
        == "ADT/ACK - Admit/visit notification"
    )
    assert (
        inst.eventTrigger[0].event.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0003"
    )
    assert (
        inst.eventTrigger[0].resource
        == "http://hl7.org/fhir/StructureDefinition/Encounter"
    )
    assert inst.id == "admission"
    assert inst.notificationShape[0].include[0] == "Encounter:patient"
    assert inst.notificationShape[0].include[1] == "Encounter:practitioner"
    assert inst.notificationShape[0].include[2] == "Encounter:service-provider"
    assert inst.notificationShape[0].include[3] == "Encounter:account"
    assert inst.notificationShape[0].include[4] == "Encounter:diagnosis"
    assert inst.notificationShape[0].include[5] == "Encounter:observation"
    assert inst.notificationShape[0].include[6] == "Encounter:location"
    assert inst.notificationShape[0].resource == "Encounter"
    assert (
        inst.resourceTrigger[0].description
        == "Encounter resource moving to state 'in-progress'"
    )
    assert inst.resourceTrigger[0].fhirPathCriteria == (
        "%previous.status!='in-progress' and %current.status='in-" "progress'"
    )
    assert inst.resourceTrigger[0].queryCriteria.current == "status=in-progress"
    assert inst.resourceTrigger[0].queryCriteria.previous == "status:not=in-progress"
    assert inst.resourceTrigger[0].queryCriteria.requireBoth is True
    assert inst.resourceTrigger[0].queryCriteria.resultForCreate == "test-passes"
    assert inst.resourceTrigger[0].queryCriteria.resultForDelete == "test-fails"
    assert (
        inst.resourceTrigger[0].resource
        == "http://hl7.org/fhir/StructureDefinition/Encounter"
    )
    assert inst.resourceTrigger[0].supportedInteraction[0] == "create"
    assert inst.resourceTrigger[0].supportedInteraction[1] == "update"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "admission"
    assert inst.url == "http://example.org/FHIR/R4B/SubscriptionTopic/admission"


def test_subscriptiontopic_1(base_settings):
    """No. 1 tests collection for SubscriptionTopic.
    Test File: subscriptiontopic-example-admission.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "subscriptiontopic-example-admission.json"
    )
    inst = subscriptiontopic.SubscriptionTopic.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubscriptionTopic" == inst.resource_type

    impl_subscriptiontopic_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubscriptionTopic" == data["resourceType"]

    inst2 = subscriptiontopic.SubscriptionTopic(**data)
    impl_subscriptiontopic_1(inst2)
