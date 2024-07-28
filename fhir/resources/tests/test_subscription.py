# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Subscription
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import subscription
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_subscription_1(inst):
    assert inst.channelType.code == "rest-hook"
    assert inst.content == "id-only"
    assert inst.contentType == "application/fhir+json"
    assert (
        inst.end
        == ExternalValidatorModel(valueInstant="2019-08-07T11:15:18Z").valueInstant
    )
    assert (
        inst.endpoint
        == ExternalValidatorModel(
            valueUrl="https://example.org/Endpoints/P123"
        ).valueUrl
    )
    assert inst.filterBy[0].filterParameter == "patient"
    assert inst.filterBy[0].value == "Patient/123"
    assert inst.heartbeatPeriod == 60
    assert inst.id == "admission"
    assert inst.maxCount == 100
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "AdmissionExample"
    assert inst.parameter[0].name == "Authorization"
    assert inst.parameter[0].value == "Bearer secret-token-abc-123"
    assert inst.reason == (
        "subscription for beginning of a clinical encounter for " "patient 123"
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.timeout == 5
    assert inst.topic == "http://example.org/R5/SubscriptionTopic/admission"


def test_subscription_1(base_settings):
    """No. 1 tests collection for Subscription.
    Test File: subscription-admission.json
    """
    filename = base_settings["unittest_data_dir"] / "subscription-admission.json"
    inst = subscription.Subscription.model_validate_json(filename.read_bytes())
    assert "Subscription" == inst.get_resource_type()

    impl_subscription_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Subscription" == data["resourceType"]

    inst2 = subscription.Subscription(**data)
    impl_subscription_1(inst2)


def impl_subscription_2(inst):
    assert inst.channelType.code == "rest-hook"
    assert inst.contact[0].system == "phone"
    assert inst.contact[0].use == "work"
    assert inst.contact[0].value == "(555) 555-1212"
    assert inst.filterBy[0].filterParameter == "patient"
    assert inst.filterBy[0].value == "Patient/123"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="urn:ietf:rfc:3986").valueUri
    )
    assert inst.identifier[0].value == "urn:uuid:97e5aa1e-5916-4512-a36e-24eef784e3cc"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "Example"
    assert inst.reason == "Example subscription for example topic"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.topic == "http://example.org/R5/SubscriptionTopic/example"


def test_subscription_2(base_settings):
    """No. 2 tests collection for Subscription.
    Test File: subscription-example.json
    """
    filename = base_settings["unittest_data_dir"] / "subscription-example.json"
    inst = subscription.Subscription.model_validate_json(filename.read_bytes())
    assert "Subscription" == inst.get_resource_type()

    impl_subscription_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Subscription" == data["resourceType"]

    inst2 = subscription.Subscription(**data)
    impl_subscription_2(inst2)
