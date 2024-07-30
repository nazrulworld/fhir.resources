# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import researchdefinition
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_researchdefinition_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.population.reference == "ResearchElementDefinition/example"
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_researchdefinition_1(base_settings):
    """No. 1 tests collection for ResearchDefinition.
    Test File: researchdefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "researchdefinition-example.json"
    inst = researchdefinition.ResearchDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "ResearchDefinition" == inst.get_resource_type()

    impl_researchdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ResearchDefinition" == data["resourceType"]

    inst2 = researchdefinition.ResearchDefinition(**data)
    impl_researchdefinition_1(inst2)
