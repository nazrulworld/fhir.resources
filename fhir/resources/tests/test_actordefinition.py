# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ActorDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import actordefinition


def impl_actordefinition_1(inst):
    assert inst.date == fhirtypes.DateTime.validate("2021-11-02T14:31:30.239Z")
    assert inst.description == "Server Actor"
    assert inst.id == "server"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.27.1"
    assert inst.name == "ServerActor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Server Actor"
    assert inst.type == "system"
    assert inst.url == "http://hl7.org/fhir/ActorDefinition/server"


def test_actordefinition_1(base_settings):
    """No. 1 tests collection for ActorDefinition.
    Test File: actordefinition-server.json
    """
    filename = base_settings["unittest_data_dir"] / "actordefinition-server.json"
    inst = actordefinition.ActorDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActorDefinition" == inst.resource_type

    impl_actordefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActorDefinition" == data["resourceType"]

    inst2 = actordefinition.ActorDefinition(**data)
    impl_actordefinition_1(inst2)


def impl_actordefinition_2(inst):
    assert inst.date == fhirtypes.DateTime.validate("2021-11-02T14:31:30.239Z")
    assert inst.description == "Client Actor"
    assert inst.id == "client"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.27.2"
    assert inst.name == "ClientActor"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Client Actor"
    assert inst.type == "system"
    assert inst.url == "http://hl7.org/fhir/ActorDefinition/client"


def test_actordefinition_2(base_settings):
    """No. 2 tests collection for ActorDefinition.
    Test File: actordefinition-client.json
    """
    filename = base_settings["unittest_data_dir"] / "actordefinition-client.json"
    inst = actordefinition.ActorDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ActorDefinition" == inst.resource_type

    impl_actordefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ActorDefinition" == data["resourceType"]

    inst2 = actordefinition.ActorDefinition(**data)
    impl_actordefinition_2(inst2)
