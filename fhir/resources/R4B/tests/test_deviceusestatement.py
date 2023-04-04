# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceUseStatement
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import deviceusestatement


def impl_deviceusestatement_1(inst):
    assert inst.device.reference == "Device/example"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http:goodhealth.org/identifiers"
    assert inst.identifier[0].value == "51ebb7a9-4e3a-4360-9a05-0cc2d869086f"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
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
    inst = deviceusestatement.DeviceUseStatement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceUseStatement" == inst.resource_type

    impl_deviceusestatement_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceUseStatement" == data["resourceType"]

    inst2 = deviceusestatement.DeviceUseStatement(**data)
    impl_deviceusestatement_1(inst2)
