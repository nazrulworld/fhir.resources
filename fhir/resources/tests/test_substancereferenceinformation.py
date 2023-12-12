# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import substancereferenceinformation


def impl_substancereferenceinformation_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_substancereferenceinformation_1(base_settings):
    """No. 1 tests collection for SubstanceReferenceInformation.
    Test File: substancereferenceinformation-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "substancereferenceinformation-example.json"
    )
    inst = substancereferenceinformation.SubstanceReferenceInformation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SubstanceReferenceInformation" == inst.resource_type

    impl_substancereferenceinformation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SubstanceReferenceInformation" == data["resourceType"]

    inst2 = substancereferenceinformation.SubstanceReferenceInformation(**data)
    impl_substancereferenceinformation_1(inst2)
