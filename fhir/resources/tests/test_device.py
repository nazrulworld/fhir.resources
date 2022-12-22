# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import device


def impl_device_1(inst):
    assert inst.id == "f001"
    assert inst.identifier[0].system == "http:/goodhealthhospital/identifier/devices"
    assert inst.identifier[0].value == "12345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_device_1(base_settings):
    """No. 1 tests collection for Device.
    Test File: device-example-f001-feedingtube.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "device-example-f001-feedingtube.json"
    )
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_1(inst2)


def impl_device_2(inst):
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://goodcare.org/devices/id"
    assert inst.identifier[0].value == "345675"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_device_2(base_settings):
    """No. 2 tests collection for Device.
    Test File: device-example.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example.json"
    inst = device.Device.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Device" == inst.resource_type

    impl_device_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_2(inst2)
