# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Linkage
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import linkage


def impl_linkage_1(inst):
    assert inst.author.reference == "Practitioner/f201"
    assert inst.id == "example"
    assert (
        inst.item[0].resource.display == "Severe burn of left ear (Date: 24-May 2012)"
    )
    assert inst.item[0].resource.reference == "Condition/example"
    assert inst.item[0].type == "source"
    assert (
        inst.item[1].resource.display == "Severe burn of left ear (Date: 24-May 2012)"
    )
    assert inst.item[1].resource.reference == "Condition/condition-example"
    assert inst.item[1].type == "alternate"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_linkage_1(base_settings):
    """No. 1 tests collection for Linkage.
    Test File: linkage-example.json
    """
    filename = base_settings["unittest_data_dir"] / "linkage-example.json"
    inst = linkage.Linkage.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Linkage" == inst.resource_type

    impl_linkage_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Linkage" == data["resourceType"]

    inst2 = linkage.Linkage(**data)
    impl_linkage_1(inst2)
