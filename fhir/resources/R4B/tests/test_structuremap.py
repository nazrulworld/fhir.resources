# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureMap
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import structuremap


def impl_structuremap_1(inst):
    assert inst.experimental is True
    assert inst.group[0].input[0].mode == "source"
    assert inst.group[0].input[0].name == "source"
    assert inst.group[0].input[0].type == "ActivityDefinition"
    assert inst.group[0].input[1].mode == "target"
    assert inst.group[0].input[1].name == "target"
    assert inst.group[0].input[1].type == "SupplyRequest"
    assert inst.group[0].name == "main"
    assert inst.group[0].rule[0].name == "status"
    assert inst.group[0].rule[0].source[0].context == "source"
    assert inst.group[0].rule[0].source[0].element == "id"
    assert inst.group[0].rule[0].source[0].variable == "a"
    assert inst.group[0].rule[0].target[0].context == "target"
    assert inst.group[0].rule[0].target[0].contextType == "variable"
    assert inst.group[0].rule[0].target[0].element == "status"
    assert inst.group[0].rule[0].target[0].parameter[0].valueString == "'draft'"
    assert inst.group[0].rule[0].target[0].transform == "evaluate"
    assert inst.group[0].rule[1].name == "category"
    assert inst.group[0].rule[1].source[0].context == "source"
    assert inst.group[0].rule[1].source[0].element == "id"
    assert inst.group[0].rule[1].source[0].variable == "a"
    assert inst.group[0].rule[1].target[0].context == "target"
    assert inst.group[0].rule[1].target[0].contextType == "variable"
    assert inst.group[0].rule[1].target[0].element == "category"
    assert inst.group[0].rule[1].target[0].parameter[0].valueString == "'non-stock'"
    assert inst.group[0].rule[1].target[0].transform == "evaluate"
    assert inst.group[0].rule[2].name == "priority"
    assert inst.group[0].rule[2].source[0].context == "source"
    assert inst.group[0].rule[2].source[0].element == "id"
    assert inst.group[0].rule[2].source[0].variable == "a"
    assert inst.group[0].rule[2].target[0].context == "target"
    assert inst.group[0].rule[2].target[0].contextType == "variable"
    assert inst.group[0].rule[2].target[0].element == "priority"
    assert inst.group[0].rule[2].target[0].parameter[0].valueString == "'routine'"
    assert inst.group[0].rule[2].target[0].transform == "evaluate"
    assert inst.group[0].rule[3].name == "quantity"
    assert inst.group[0].rule[3].source[0].context == "source"
    assert inst.group[0].rule[3].source[0].element == "quantity"
    assert inst.group[0].rule[3].source[0].variable == "a"
    assert inst.group[0].rule[3].target[0].context == "target"
    assert inst.group[0].rule[3].target[0].contextType == "variable"
    assert inst.group[0].rule[3].target[0].element == "category"
    assert inst.group[0].rule[3].target[0].transform == "copy"
    assert inst.group[0].rule[4].name == "item"
    assert inst.group[0].rule[4].source[0].context == "source"
    assert inst.group[0].rule[4].source[0].element == "code"
    assert inst.group[0].rule[4].source[0].variable == "a"
    assert inst.group[0].rule[4].target[0].context == "target"
    assert inst.group[0].rule[4].target[0].contextType == "variable"
    assert inst.group[0].rule[4].target[0].element == "orderedItem.itemCodeableConcept"
    assert inst.group[0].rule[4].target[0].transform == "copy"
    assert inst.group[0].rule[5].name == "when"
    assert inst.group[0].rule[5].source[0].context == "source"
    assert inst.group[0].rule[5].source[0].element == "id"
    assert inst.group[0].rule[5].source[0].variable == "a"
    assert inst.group[0].rule[5].target[0].context == "target"
    assert inst.group[0].rule[5].target[0].contextType == "variable"
    assert inst.group[0].rule[5].target[0].element == "occurrenceDateTime"
    assert inst.group[0].rule[5].target[0].parameter[0].valueString == "now()"
    assert inst.group[0].rule[5].target[0].transform == "evaluate"
    assert inst.group[0].rule[6].name == "authoredOn"
    assert inst.group[0].rule[6].source[0].context == "source"
    assert inst.group[0].rule[6].source[0].element == "id"
    assert inst.group[0].rule[6].source[0].variable == "a"
    assert inst.group[0].rule[6].target[0].context == "target"
    assert inst.group[0].rule[6].target[0].contextType == "variable"
    assert inst.group[0].rule[6].target[0].element == "authoredOn"
    assert inst.group[0].rule[6].target[0].parameter[0].valueString == "now()"
    assert inst.group[0].rule[6].target[0].transform == "evaluate"
    assert inst.group[0].typeMode == "none"
    assert inst.id == "supplyrequest-transform"
    assert inst.name == "Transform from an ActivityDefinition to a SupplyRequest"
    assert inst.status == "draft"
    assert inst.structure[0].mode == "source"
    assert (
        inst.structure[0].url
        == "http://hl7.org/fhir/StructureDefinition/activitydefinition"
    )
    assert inst.structure[1].mode == "target"
    assert (
        inst.structure[1].url == "http://hl7.org/fhir/StructureDefinition/supplyrequest"
    )
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/StructureMap/supplyrequest-transform"


def test_structuremap_1(base_settings):
    """No. 1 tests collection for StructureMap.
    Test File: structuremap-supplyrequest-transform.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "structuremap-supplyrequest-transform.json"
    )
    inst = structuremap.StructureMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "StructureMap" == inst.resource_type

    impl_structuremap_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "StructureMap" == data["resourceType"]

    inst2 = structuremap.StructureMap(**data)
    impl_structuremap_1(inst2)


def impl_structuremap_2(inst):
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2017-03-09")
    assert inst.description == "Example Structure Map"
    assert inst.experimental is True
    assert inst.group[0].documentation == "test -> testValue"
    assert inst.group[0].input[0].mode == "source"
    assert inst.group[0].input[0].name == "test"
    assert inst.group[0].name == "Examples"
    assert inst.group[0].rule[0].name == "rule1"
    assert inst.group[0].rule[0].source[0].context == "Source"
    assert inst.group[0].rule[0].source[0].element == "test"
    assert inst.group[0].rule[0].source[0].type == "SourceClassA"
    assert inst.group[0].rule[0].source[0].variable == "t"
    assert inst.group[0].rule[0].target[0].context == "Destination"
    assert inst.group[0].rule[0].target[0].contextType == "variable"
    assert inst.group[0].rule[0].target[0].element == "testValue"
    assert inst.group[0].rule[0].target[0].transform == "copy"
    assert inst.group[0].typeMode == "none"
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:37843577-95fb-4adb-84c0-8837188a7bf3"
    assert inst.jurisdiction[0].coding[0].code == "009"
    assert inst.jurisdiction[0].coding[0].display == "Oceania"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.name == "ExampleMap"
    assert inst.publisher == "HL7 FHIR Standard"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Example Map"
    assert inst.url == "http://hl7.org/fhir/StructureMap/example"
    assert inst.version == "0.1"


def test_structuremap_2(base_settings):
    """No. 2 tests collection for StructureMap.
    Test File: structuremap-example.json
    """
    filename = base_settings["unittest_data_dir"] / "structuremap-example.json"
    inst = structuremap.StructureMap.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "StructureMap" == inst.resource_type

    impl_structuremap_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "StructureMap" == data["resourceType"]

    inst2 = structuremap.StructureMap(**data)
    impl_structuremap_2(inst2)
