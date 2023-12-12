# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceUseStatement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import deviceusestatement


def impl_deviceusestatement_1(inst):
    assert inst.device.reference == "Device/example"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http:goodhealth.org/identifiers"
    assert inst.identifier[0].value == "51ebb7a9-4e3a-4360-9a05-0cc2d869086f"
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
