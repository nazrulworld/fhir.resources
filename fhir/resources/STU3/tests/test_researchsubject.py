# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import researchsubject


def impl_researchsubject_1(inst):
    assert inst.id == "example"
    assert inst.identifier.system == "http://example.org/studysubjectids"
    assert inst.identifier.type.text == "Subject id"
    assert inst.identifier.value == "123"
    assert inst.individual.reference == "Patient/example"
    assert inst.status == "candidate"
    assert inst.study.reference == "ResearchStudy/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_researchsubject_1(base_settings):
    """No. 1 tests collection for ResearchSubject.
    Test File: researchsubject-example.json
    """
    filename = base_settings["unittest_data_dir"] / "researchsubject-example.json"
    inst = researchsubject.ResearchSubject.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ResearchSubject" == inst.resource_type

    impl_researchsubject_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ResearchSubject" == data["resourceType"]

    inst2 = researchsubject.ResearchSubject(**data)
    impl_researchsubject_1(inst2)
