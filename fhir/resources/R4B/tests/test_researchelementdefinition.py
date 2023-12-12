# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import researchelementdefinition


def impl_researchelementdefinition_1(inst):
    assert (
        inst.characteristic[0].definitionCodeableConcept.text
        == "Diabetic patients over 65"
    )
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type == "population"


def test_researchelementdefinition_1(base_settings):
    """No. 1 tests collection for ResearchElementDefinition.
    Test File: researchelementdefinition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "researchelementdefinition-example.json"
    )
    inst = researchelementdefinition.ResearchElementDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ResearchElementDefinition" == inst.resource_type

    impl_researchelementdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ResearchElementDefinition" == data["resourceType"]

    inst2 = researchelementdefinition.ResearchElementDefinition(**data)
    impl_researchelementdefinition_1(inst2)
