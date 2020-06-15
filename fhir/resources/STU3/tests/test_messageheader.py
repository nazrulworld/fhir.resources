# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageHeader
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import messageheader


def impl_messageheader_1(inst):
    assert inst.author.reference == "Practitioner/example"
    assert inst.destination[0].endpoint == "llp:10.11.12.14:5432"
    assert inst.destination[0].name == "Acme Message Gateway"
    assert inst.destination[0].target.reference == "Device/example"
    assert inst.enterer.reference == "Practitioner/example"
    assert inst.event.code == "admin-notify"
    assert inst.event.system == "http://hl7.org/fhir/message-events"
    assert inst.focus[0].reference == "Patient/example"
    assert inst.id == "1cbdfb97-5859-48a4-8301-d54eab818d68"
    assert inst.reason.coding[0].code == "admit"
    assert (
        inst.reason.coding[0].system == "http://hl7.org/fhir/message-reasons-encounter"
    )
    assert inst.response.code == "ok"
    assert inst.response.identifier == "5015fe84-8e76-4526-89d8-44b322e8d4fb"
    assert inst.sender.reference == "Organization/1"
    assert inst.source.contact.system == "phone"
    assert inst.source.contact.value == "+1 (555) 123 4567"
    assert inst.source.endpoint == "llp:10.11.12.13:5432"
    assert inst.source.name == "Acme Central Patient Registry"
    assert inst.source.software == "FooBar Patient Manager"
    assert inst.source.version == "3.1.45.AABB"
    assert inst.text.status == "generated"
    assert inst.timestamp == fhirtypes.Instant.validate("2012-01-04T09:10:14Z")


def test_messageheader_1(base_settings):
    """No. 1 tests collection for MessageHeader.
    Test File: messageheader-example.json
    """
    filename = base_settings["unittest_data_dir"] / "messageheader-example.json"
    inst = messageheader.MessageHeader.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MessageHeader" == inst.resource_type

    impl_messageheader_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MessageHeader" == data["resourceType"]

    inst2 = messageheader.MessageHeader(**data)
    impl_messageheader_1(inst2)
