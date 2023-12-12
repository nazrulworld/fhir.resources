# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceAssociation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import deviceassociation


def impl_deviceassociation_1(inst):
    assert inst.device.reference == "Device/prod1"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status.coding[0].code == "implanted"
    assert (
        inst.status.coding[0].system == "http://hl7.org/fhir/deviceassociation-status"
    )
    assert inst.subject.display == "Donald Duck"
    assert inst.subject.reference == "Patient/pat1"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_deviceassociation_1(base_settings):
    """No. 1 tests collection for DeviceAssociation.
    Test File: deviceassociation-example.json
    """
    filename = base_settings["unittest_data_dir"] / "deviceassociation-example.json"
    inst = deviceassociation.DeviceAssociation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceAssociation" == inst.resource_type

    impl_deviceassociation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceAssociation" == data["resourceType"]

    inst2 = deviceassociation.DeviceAssociation(**data)
    impl_deviceassociation_1(inst2)
