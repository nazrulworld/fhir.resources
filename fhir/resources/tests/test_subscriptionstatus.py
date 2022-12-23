# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubscriptionStatus
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import subscriptionstatus


def impl_subscriptionstatus_1(inst):
    assert inst.eventsSinceSubscriptionStart == "1000"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.notificationEvent[0].eventNumber == "1000"
    assert (
        inst.notificationEvent[0].focus.reference
        == "urn:uuid:9986fc11-a845-4965-af24-45312fd0cc4e"
    )
    assert inst.status == "active"
    assert inst.subscription.reference == "http://example.org/FHIR/R4B/Subscription/123"
    assert inst.text.status == "generated"
    assert inst.topic == "http://example.org/FHIR/R4B/SubscriptionTopic/admission"
    assert inst.type == "event-notification"


def test_subscriptionstatus_1(base_settings):
    """No. 1 tests collection for SubscriptionStatus.
    Test File: subscriptionstatus-example.json
    """
    filename = base_settings["unittest_data_dir"] / "subscriptionstatus-example.json"
    inst = subscriptionstatus.SubscriptionStatus.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubscriptionStatus" == inst.resource_type

    impl_subscriptionstatus_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubscriptionStatus" == data["resourceType"]

    inst2 = subscriptionstatus.SubscriptionStatus(**data)
    impl_subscriptionstatus_1(inst2)
