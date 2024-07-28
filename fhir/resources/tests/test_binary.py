# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Binary
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import binary
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_binary_1(inst):
    assert inst.contentType == "application/pdf"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.securityContext.reference == "DocumentReference/example"


def test_binary_1(base_settings):
    """No. 1 tests collection for Binary.
    Test File: binary-example.json
    """
    filename = base_settings["unittest_data_dir"] / "binary-example.json"
    inst = binary.Binary.model_validate_json(filename.read_bytes())
    assert "Binary" == inst.get_resource_type()

    impl_binary_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Binary" == data["resourceType"]

    inst2 = binary.Binary(**data)
    impl_binary_1(inst2)


def impl_binary_2(inst):
    assert inst.contentType == "image/jpeg"
    assert inst.id == "f006"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )


def test_binary_2(base_settings):
    """No. 2 tests collection for Binary.
    Test File: binary-f006.json
    """
    filename = base_settings["unittest_data_dir"] / "binary-f006.json"
    inst = binary.Binary.model_validate_json(filename.read_bytes())
    assert "Binary" == inst.get_resource_type()

    impl_binary_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Binary" == data["resourceType"]

    inst2 = binary.Binary(**data)
    impl_binary_2(inst2)
