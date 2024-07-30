# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Linkage
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import linkage
from .fixtures import ExternalValidatorModel  # noqa: F401


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
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_linkage_1(base_settings):
    """No. 1 tests collection for Linkage.
    Test File: linkage-example.json
    """
    filename = base_settings["unittest_data_dir"] / "linkage-example.json"
    inst = linkage.Linkage.model_validate_json(filename.read_bytes())
    assert "Linkage" == inst.get_resource_type()

    impl_linkage_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Linkage" == data["resourceType"]

    inst2 = linkage.Linkage(**data)
    impl_linkage_1(inst2)
