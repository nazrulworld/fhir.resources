# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceDispense
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import devicedispense


def impl_devicedispense_1(inst):
    assert inst.device.concept.coding[0].code == "00613994223838"
    assert inst.device.concept.coding[0].display == "ADAPTA (TM) Pacemaker"
    assert inst.device.concept.coding[0].system == "https://www.gs1.org/gtin"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "completed"
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_devicedispense_1(base_settings):
    """No. 1 tests collection for DeviceDispense.
    Test File: devicedispense-example.json
    """
    filename = base_settings["unittest_data_dir"] / "devicedispense-example.json"
    inst = devicedispense.DeviceDispense.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceDispense" == inst.resource_type

    impl_devicedispense_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceDispense" == data["resourceType"]

    inst2 = devicedispense.DeviceDispense(**data)
    impl_devicedispense_1(inst2)
