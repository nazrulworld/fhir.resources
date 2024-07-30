# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import device
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_device_1(inst):
    assert inst.id == "f001"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http:/goodhealthhospital/identifier/devices"}
        ).valueUri
    )
    assert inst.identifier[0].value == "12345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
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
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_1(inst2)


def impl_device_2(inst):
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://goodcare.org/devices/id"}
        ).valueUri
    )
    assert inst.identifier[0].value == "345675"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_device_2(base_settings):
    """No. 2 tests collection for Device.
    Test File: device-example.json
    """
    filename = base_settings["unittest_data_dir"] / "device-example.json"
    inst = device.Device.model_validate_json(filename.read_bytes())
    assert "Device" == inst.get_resource_type()

    impl_device_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Device" == data["resourceType"]

    inst2 = device.Device(**data)
    impl_device_2(inst2)
