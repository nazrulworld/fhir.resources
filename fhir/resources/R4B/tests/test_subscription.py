# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Subscription
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import subscription


def impl_subscription_1(inst):
    assert (
        inst.channel.endpoint
        == "https://biliwatch.com/customers/mount-auburn-miu/on-result"
    )
    assert inst.channel.header[0] == "Authorization: Bearer secret-token-abc-123"
    assert inst.channel.payload == "application/fhir+json"
    assert inst.channel.type == "rest-hook"
    assert inst.contact[0].system == "phone"
    assert inst.contact[0].value == "ext 4123"
    assert inst.criteria == "Observation?code=http://loinc.org|1975-2"
    assert inst.end == fhirtypes.Instant.validate("2021-01-01T00:00:00Z")
    assert inst.error == "Socket Error 10060 - can't connect to host"
    assert inst.id == "example-error"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reason == "Monitor new neonatal function"
    assert inst.status == "error"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_subscription_1(base_settings):
    """No. 1 tests collection for Subscription.
    Test File: subscription-example-error.json
    """
    filename = base_settings["unittest_data_dir"] / "subscription-example-error.json"
    inst = subscription.Subscription.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Subscription" == inst.resource_type

    impl_subscription_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Subscription" == data["resourceType"]

    inst2 = subscription.Subscription(**data)
    impl_subscription_1(inst2)


def impl_subscription_2(inst):
    assert (
        inst.channel.endpoint
        == "https://biliwatch.com/customers/mount-auburn-miu/on-result"
    )
    assert inst.channel.header[0] == "Authorization: Bearer secret-token-abc-123"
    assert inst.channel.payload == "application/fhir+json"
    assert inst.channel.type == "rest-hook"
    assert inst.contact[0].system == "phone"
    assert inst.contact[0].value == "ext 4123"
    assert inst.criteria == "Observation?code=http://loinc.org|1975-2"
    assert inst.end == fhirtypes.Instant.validate("2021-01-01T00:00:00Z")
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reason == "Monitor new neonatal function"
    assert inst.status == "requested"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_subscription_2(base_settings):
    """No. 2 tests collection for Subscription.
    Test File: subscription-example.json
    """
    filename = base_settings["unittest_data_dir"] / "subscription-example.json"
    inst = subscription.Subscription.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Subscription" == inst.resource_type

    impl_subscription_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Subscription" == data["resourceType"]

    inst2 = subscription.Subscription(**data)
    impl_subscription_2(inst2)
