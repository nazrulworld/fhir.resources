# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubscriptionStatus
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import subscriptionstatus
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_subscriptionstatus_1(inst):
    # Don't know how to create unit test
    # for "eventsSinceSubscriptionStart",
    # which is a Integer64
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    # Don't know how to create unit test
    # for "notificationEvent[0].eventNumber",
    # which is a Integer64
    assert inst.status == "active"
    assert inst.subscription.reference == "http://example.org/FHIR/R5/Subscription/123"
    assert inst.text.status == "generated"
    assert inst.topic == "http://example.org/FHIR/R5/SubscriptionTopic/admission"
    assert inst.type == "event-notification"


def test_subscriptionstatus_1(base_settings):
    """No. 1 tests collection for SubscriptionStatus.
    Test File: subscriptionstatus-example.json
    """
    filename = base_settings["unittest_data_dir"] / "subscriptionstatus-example.json"
    inst = subscriptionstatus.SubscriptionStatus.model_validate_json(
        filename.read_bytes()
    )
    assert "SubscriptionStatus" == inst.get_resource_type()

    impl_subscriptionstatus_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SubscriptionStatus" == data["resourceType"]

    inst2 = subscriptionstatus.SubscriptionStatus(**data)
    impl_subscriptionstatus_1(inst2)
