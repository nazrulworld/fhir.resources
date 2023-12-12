# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Citation
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import citation


def impl_citation_1(inst):
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


def test_citation_1(base_settings):
    """No. 1 tests collection for Citation.
    Test File: citation-example.json
    """
    filename = base_settings["unittest_data_dir"] / "citation-example.json"
    inst = citation.Citation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Citation" == inst.resource_type

    impl_citation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Citation" == data["resourceType"]

    inst2 = citation.Citation(**data)
    impl_citation_1(inst2)
