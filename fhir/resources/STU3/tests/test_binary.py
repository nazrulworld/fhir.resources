# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Binary
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import binary


def impl_binary_1(inst):
    assert inst.contentType == "application/pdf"
    assert inst.id == "example"
    assert inst.securityContext.reference == "DocumentReference/example"


def test_binary_1(base_settings):
    """No. 1 tests collection for Binary.
    Test File: binary-example.json
    """
    filename = base_settings["unittest_data_dir"] / "binary-example.json"
    inst = binary.Binary.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Binary" == inst.resource_type

    impl_binary_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Binary" == data["resourceType"]

    inst2 = binary.Binary(**data)
    impl_binary_1(inst2)


def impl_binary_2(inst):
    assert inst.contentType == "image/jpeg"
    assert inst.id == "f006"


def test_binary_2(base_settings):
    """No. 2 tests collection for Binary.
    Test File: binary-f006.json
    """
    filename = base_settings["unittest_data_dir"] / "binary-f006.json"
    inst = binary.Binary.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Binary" == inst.resource_type

    impl_binary_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Binary" == data["resourceType"]

    inst2 = binary.Binary(**data)
    impl_binary_2(inst2)
