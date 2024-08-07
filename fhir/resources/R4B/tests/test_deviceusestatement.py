# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceUseStatement
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import deviceusestatement
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_deviceusestatement_1(inst):
    assert inst.device.reference == "Device/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http:goodhealth.org/identifiers"}
        ).valueUri
    )
    assert inst.identifier[0].value == "51ebb7a9-4e3a-4360-9a05-0cc2d869086f"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.reasonReference[0].display == "PHx of Appendectomy (surgery)"
    assert inst.reasonReference[0].reference == "Condition/example"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_deviceusestatement_1(base_settings):
    """No. 1 tests collection for DeviceUseStatement.
    Test File: deviceusestatement-example.json
    """
    filename = base_settings["unittest_data_dir"] / "deviceusestatement-example.json"
    inst = deviceusestatement.DeviceUseStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "DeviceUseStatement" == inst.get_resource_type()

    impl_deviceusestatement_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "DeviceUseStatement" == data["resourceType"]

    inst2 = deviceusestatement.DeviceUseStatement(**data)
    impl_deviceusestatement_1(inst2)
