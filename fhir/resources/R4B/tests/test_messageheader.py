# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MessageHeader
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import messageheader


def impl_messageheader_1(inst):
    assert inst.author.reference == "Practitioner/example"
    assert (
        inst.definition == "http:////acme.com/ehr/fhir/messagedefinition/patientrequest"
    )
    assert inst.destination[0].endpoint == "llp:10.11.12.14:5432"
    assert inst.destination[0].name == "Acme Message Gateway"
    assert (
        inst.destination[0].receiver.reference
        == "http://acme.com/ehr/fhir/Practitioner/2323-33-4"
    )
    assert inst.destination[0].target.reference == "Device/example"
    assert inst.enterer.reference == "Practitioner/example"
    assert inst.eventCoding.code == "admin-notify"
    assert inst.eventCoding.system == "http://example.org/fhir/message-events"
    assert inst.focus[0].reference == "Patient/example"
    assert inst.id == "1cbdfb97-5859-48a4-8301-d54eab818d68"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reason.coding[0].code == "admit"
    assert inst.reason.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/message-reasons-" "encounter"
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
