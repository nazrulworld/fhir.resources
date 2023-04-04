# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GraphDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import graphdefinition


def impl_graphdefinition_1(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2015-08-04")
    assert inst.description == (
        "Specify to include list references when generating a "
        "document using the $document operation"
    )
    assert inst.experimental is True
    assert inst.id == "example"
    assert inst.link[0].description == "Link to List"
    assert inst.link[0].path == "Composition.section.entry"
    assert inst.link[0].target[0].compartment[0].code == "Patient"
    assert inst.link[0].target[0].compartment[0].rule == "identical"
    assert inst.link[0].target[0].compartment[0].use == "requirement"
    assert inst.link[0].target[0].link[0].description == "Include any list entries"
    assert inst.link[0].target[0].link[0].path == "List.entry.item"
    assert inst.link[0].target[0].link[0].target[0].compartment[0].code == "Patient"
    assert inst.link[0].target[0].link[0].target[0].compartment[0].rule == "identical"
    assert inst.link[0].target[0].link[0].target[0].compartment[0].use == "requirement"
    assert inst.link[0].target[0].link[0].target[0].type == "Resource"
    assert inst.link[0].target[0].type == "List"
    assert inst.name == "Document Generation Template"
    assert inst.publisher == "FHIR Project"
    assert inst.start == "Composition"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://h7.org/fhir/GraphDefinition/example"


def test_graphdefinition_1(base_settings):
    """No. 1 tests collection for GraphDefinition.
    Test File: graphdefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "graphdefinition-example.json"
    inst = graphdefinition.GraphDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "GraphDefinition" == inst.resource_type

    impl_graphdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "GraphDefinition" == data["resourceType"]

    inst2 = graphdefinition.GraphDefinition(**data)
    impl_graphdefinition_1(inst2)
