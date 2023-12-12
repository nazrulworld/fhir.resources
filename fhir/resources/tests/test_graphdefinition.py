# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GraphDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

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
    assert inst.id == "example"
    assert inst.link[0].compartment[0].code == "Patient"
    assert inst.link[0].compartment[0].rule == "identical"
    assert inst.link[0].compartment[0].use == "requires"
    assert inst.link[0].description == "Link from Composition.section to list"
    assert inst.link[0].path == "Composition.section.entry"
    assert inst.link[0].sourceId == "comp1"
    assert inst.link[0].targetId == "list1"
    assert inst.link[1].compartment[0].code == "Patient"
    assert inst.link[1].compartment[0].rule == "identical"
    assert inst.link[1].compartment[0].use == "requires"
    assert inst.link[1].description == "Include any list entries"
    assert inst.link[1].path == "List.entry.item"
    assert inst.link[1].sourceId == "list1"
    assert inst.link[1].targetId == "resN"
    assert inst.name == "DocumentGenerationTemplate"
    assert inst.node[0].description == "The base composition"
    assert inst.node[0].nodeId == "comp1"
    assert (
        inst.node[0].profile
        == "http://hl7.org/fhir/StructureDefinition/clinicaldocument"
    )
    assert inst.node[0].type == "Composition"
    assert (
        inst.node[1].description
        == "A list resource that a section entry reference points to"
    )
    assert inst.node[1].nodeId == "list1"
    assert inst.node[1].type == "List"
    assert (
        inst.node[2].description
        == "Generic resource that's the target of a list reference"
    )
    assert inst.node[2].nodeId == "resN"
    assert inst.node[2].type == "Resource"
    assert inst.publisher == "FHIR Project"
    assert inst.start == "comp1"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Document Generation Template"
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
