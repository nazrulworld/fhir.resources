# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceAssociation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import deviceassociation
from .fixtures import ExternalValidatorModel


def impl_deviceassociation_1(inst):
    assert inst.device.reference == "Device/prod1"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.status.coding[0].code == "implanted"
    assert (
        inst.status.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/deviceassociation-status"}
        ).valueUri
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
    inst = deviceassociation.DeviceAssociation.model_validate_json(
        filename.read_bytes()
    )
    assert "DeviceAssociation" == inst.get_resource_type()

    impl_deviceassociation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "DeviceAssociation" == data["resourceType"]

    inst2 = deviceassociation.DeviceAssociation(**data)
    impl_deviceassociation_1(inst2)
