# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import researchstudy


def impl_researchstudy_1(inst):
    assert inst.id == "example"
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_researchstudy_1(base_settings):
    """No. 1 tests collection for ResearchStudy.
    Test File: researchstudy-example.json
    """
    filename = base_settings["unittest_data_dir"] / "researchstudy-example.json"
    inst = researchstudy.ResearchStudy.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ResearchStudy" == inst.resource_type

    impl_researchstudy_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ResearchStudy" == data["resourceType"]

    inst2 = researchstudy.ResearchStudy(**data)
    impl_researchstudy_1(inst2)
