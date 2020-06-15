# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EvidenceVariable
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import evidencevariable


def impl_evidencevariable_1(inst):
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


def test_evidencevariable_1(base_settings):
    """No. 1 tests collection for EvidenceVariable.
    Test File: evidencevariable-example.json
    """
    filename = base_settings["unittest_data_dir"] / "evidencevariable-example.json"
    inst = evidencevariable.EvidenceVariable.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EvidenceVariable" == inst.resource_type

    impl_evidencevariable_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EvidenceVariable" == data["resourceType"]

    inst2 = evidencevariable.EvidenceVariable(**data)
    impl_evidencevariable_1(inst2)
