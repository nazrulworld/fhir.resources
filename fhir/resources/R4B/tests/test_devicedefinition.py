# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import devicedefinition
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_devicedefinition_1(inst):
    assert inst.id == "example"
    assert inst.identifier[0].value == "0"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_devicedefinition_1(base_settings):
    """No. 1 tests collection for DeviceDefinition.
    Test File: devicedefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "devicedefinition-example.json"
    inst = devicedefinition.DeviceDefinition.model_validate_json(filename.read_bytes())
    assert "DeviceDefinition" == inst.get_resource_type()

    impl_devicedefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "DeviceDefinition" == data["resourceType"]

    inst2 = devicedefinition.DeviceDefinition(**data)
    impl_devicedefinition_1(inst2)
