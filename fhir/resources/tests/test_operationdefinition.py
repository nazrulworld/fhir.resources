# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import operationdefinition


def impl_operationdefinition_1(inst):
    assert inst.affectsState is False
    assert inst.code == "data-requirements"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.description == (
        "The data-requirements operation aggregates and returns the "
        "parameters and data requirements for the measure and all its"
        " dependencies as a single module definition"
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Measure-data-requirements"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "DataRequirements"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "periodStart"
    assert inst.parameter[0].type == "date"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The end of the measurement period. The period will end at "
        "the end of the period implied by the supplied timestamp. "
        "E.g. a value of 2014 would set the period end to be "
        "2014-12-31T23:59:59 inclusive"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "periodEnd"
    assert inst.parameter[1].type == "date"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "The result of the requirements gathering is a module-"
        "definition Library that describes the aggregate parameters, "
        "data requirements, and dependencies of the measure"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "return"
    assert inst.parameter[2].type == "Library"
    assert inst.parameter[2].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Measure"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Data Requirements"
    assert inst.type is False
    assert inst.url == (
        "http://hl7.org/fhir/OperationDefinition/Measure-data-" "requirements"
    )
    assert inst.version == "4.3.0"


def test_operationdefinition_1(base_settings):
    """No. 1 tests collection for OperationDefinition.
    Test File: operation-measure-data-requirements.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-measure-data-requirements.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_1(inst2)


def impl_operationdefinition_2(inst):
    assert inst.affectsState is False
    assert inst.code == "translate"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "ConceptMap-translate"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Translate"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "url"
    assert inst.parameter[0].type == "uri"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The concept map is provided directly as part of the request."
        " Servers may choose not to accept concept maps in this "
        "fashion."
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "conceptMap"
    assert inst.parameter[1].type == "ConceptMap"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "conceptMapVersion"
    assert inst.parameter[2].type == "string"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
        "The code that is to be translated. If a code is provided, a "
        "system must be provided"
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "code"
    assert inst.parameter[3].type == "code"
    assert inst.parameter[3].use == "in"
    assert (
        inst.parameter[4].documentation
        == "The system for the code that is to be translated"
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "system"
    assert inst.parameter[4].type == "uri"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == (
        "The version of the system, if one was provided in the source" " data"
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "version"
    assert inst.parameter[5].type == "string"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "source"
    assert inst.parameter[6].type == "uri"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].documentation == "A coding to translate"
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "coding"
    assert inst.parameter[7].type == "Coding"
    assert inst.parameter[7].use == "in"
    assert inst.parameter[8].documentation == (
        "A full codeableConcept to validate. The server can translate"
        " any of the coding values (e.g. existing translations) as it"
        " chooses"
    )
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "codeableConcept"
    assert inst.parameter[8].type == "CodeableConcept"
    assert inst.parameter[8].use == "in"
    assert inst.parameter[9].max == "1"
    assert inst.parameter[9].min == 0
    assert inst.parameter[9].name == "target"
    assert inst.parameter[9].type == "uri"
    assert inst.parameter[9].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "ConceptMap"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Concept Translation"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/ConceptMap-translate"
    assert inst.version == "4.3.0"


def test_operationdefinition_2(base_settings):
    """No. 2 tests collection for OperationDefinition.
    Test File: operation-conceptmap-translate.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-conceptmap-translate.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_2(inst2)


def impl_operationdefinition_3(inst):
    assert inst.affectsState is False
    assert inst.code == "expand"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 5
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "normative"
    assert inst.id == "ValueSet-expand"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Expand"
    assert inst.parameter[0].documentation == (
        "A canonical reference to a value set. The server must know "
        "the value set (e.g. it is defined explicitly in the server's"
        " value sets, or it is defined implicitly by some code system"
        " known to the server"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "url"
    assert inst.parameter[0].type == "uri"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The value set is provided directly as part of the request. "
        "Servers may choose not to accept value sets in this fashion"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "valueSet"
    assert inst.parameter[1].type == "ValueSet"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "valueSetVersion"
    assert inst.parameter[2].type == "string"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "context"
    assert inst.parameter[3].type == "uri"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "contextDirection"
    assert inst.parameter[4].type == "code"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "filter"
    assert inst.parameter[5].type == "string"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "date"
    assert inst.parameter[6].type == "dateTime"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].documentation == (
        "Paging support - where to start if a subset is desired "
        "(default = 0). Offset is number of records (not number of "
        "pages)"
    )
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "offset"
    assert inst.parameter[7].type == "integer"
    assert inst.parameter[7].use == "in"
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "count"
    assert inst.parameter[8].type == "integer"
    assert inst.parameter[8].use == "in"
    assert inst.parameter[9].documentation == (
        "Controls whether concept designations are to be included or "
        "excluded in value set expansions"
    )
    assert inst.parameter[9].max == "1"
    assert inst.parameter[9].min == 0
    assert inst.parameter[9].name == "includeDesignations"
    assert inst.parameter[9].type == "boolean"
    assert inst.parameter[9].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "ValueSet"
    assert inst.status == "active"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Value Set Expansion"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/ValueSet-expand"
    assert inst.version == "4.3.0"


def test_operationdefinition_3(base_settings):
    """No. 3 tests collection for OperationDefinition.
    Test File: operation-valueset-expand.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-valueset-expand.json"
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_3(inst2)


def impl_operationdefinition_4(inst):
    assert inst.affectsState is True
    assert inst.code == "meta-add"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.description == (
        "This operation takes a meta, and adds the profiles, tags, "
        "and security labels found in it to the nominated resource"
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Resource-meta-add"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "MetaAdd"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "meta"
    assert inst.parameter[0].type == "Meta"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == "Resulting meta for the resource"
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "return"
    assert inst.parameter[1].type == "Meta"
    assert inst.parameter[1].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Resource"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Add profiles, tags, and security labels to a resource"
    assert inst.type is False
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Resource-meta-add"
    assert inst.version == "4.3.0"


def test_operationdefinition_4(base_settings):
    """No. 4 tests collection for OperationDefinition.
    Test File: operation-resource-meta-add.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-resource-meta-add.json"
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_4(inst2)


def impl_operationdefinition_5(inst):
    assert inst.affectsState is False
    assert inst.code == "everything"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 2
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Encounter-everything"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Everything"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "_since"
    assert inst.parameter[0].type == "instant"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "One or more parameters, each containing one or more comma-"
        "delimited FHIR resource types to include in the return "
        "resources. In the absense of any specified types, the server"
        " returns all resource types"
    )
    assert inst.parameter[1].max == "*"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "_type"
    assert inst.parameter[1].type == "code"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "See discussion below on the utility of paging through the "
        "results of the $everything operation"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "_count"
    assert inst.parameter[2].type == "integer"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == 'The bundle type is "searchset"'
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 1
    assert inst.parameter[3].name == "return"
    assert inst.parameter[3].type == "Bundle"
    assert inst.parameter[3].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Encounter"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Fetch Encounter Record"
    assert inst.type is False
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Encounter-everything"
    assert inst.version == "4.3.0"


def test_operationdefinition_5(base_settings):
    """No. 5 tests collection for OperationDefinition.
    Test File: operation-encounter-everything.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-encounter-everything.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_5(inst2)


def impl_operationdefinition_6(inst):
    assert inst.affectsState is False
    assert inst.code == "graph"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 1
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Resource-graph"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Graph"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "graph"
    assert inst.parameter[0].type == "uri"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The set of resources that were in the graph based on the "
        "provided definition"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "result"
    assert inst.parameter[1].type == "Bundle"
    assert inst.parameter[1].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Resource"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Return a graph of resources"
    assert inst.type is False
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Resource-graph"
    assert inst.version == "4.3.0"


def test_operationdefinition_6(base_settings):
    """No. 6 tests collection for OperationDefinition.
    Test File: operation-resource-graph.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-resource-graph.json"
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_6(inst2)


def impl_operationdefinition_7(inst):
    assert inst.affectsState is False
    assert inst.code == "meta"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Resource-meta"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Meta"
    assert inst.parameter[0].documentation == "The meta returned by the operation"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "return"
    assert inst.parameter[0].type == "Meta"
    assert inst.parameter[0].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Resource"
    assert inst.status == "draft"
    assert inst.system is True
    assert inst.text.status == "extensions"
    assert inst.title == "Access a list of profiles, tags, and security labels"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Resource-meta"
    assert inst.version == "4.3.0"


def test_operationdefinition_7(base_settings):
    """No. 7 tests collection for OperationDefinition.
    Test File: operation-resource-meta.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-resource-meta.json"
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_7(inst2)


def impl_operationdefinition_8(inst):
    assert inst.affectsState is False
    assert inst.code == "care-gaps"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.description == (
        "The care-gaps operation is used to determine gaps-in-care "
        "based on the results of quality measures"
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Measure-care-gaps"
    assert inst.instance is False
    assert inst.kind == "operation"
    assert inst.name == "CareGaps"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "periodStart"
    assert inst.parameter[0].type == "date"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The end of the measurement period. The period will end at "
        "the end of the period implied by the supplied timestamp. "
        "E.g. a value of 2014 would set the period end to be "
        "2014-12-31T23:59:59 inclusive"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "periodEnd"
    assert inst.parameter[1].type == "date"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "The topic to be used to determine which measures are "
        "considered for the care gaps report. Any measure with the "
        "given topic will be included in the report"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "topic"
    assert inst.parameter[2].type == "string"
    assert inst.parameter[2].use == "in"
    assert (
        inst.parameter[3].documentation
        == "Subject for which the care gaps report will be produced"
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 1
    assert inst.parameter[3].name == "subject"
    assert inst.parameter[3].searchType == "reference"
    assert inst.parameter[3].type == "string"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == (
        "The result of the care gaps report will be returned as a "
        "document bundle with a MeasureReport entry for each included"
        " measure"
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 1
    assert inst.parameter[4].name == "return"
    assert inst.parameter[4].type == "Bundle"
    assert inst.parameter[4].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Measure"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Care Gaps"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Measure-care-gaps"
    assert inst.version == "4.3.0"


def test_operationdefinition_8(base_settings):
    """No. 8 tests collection for OperationDefinition.
    Test File: operation-measure-care-gaps.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-measure-care-gaps.json"
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_8(inst2)


def impl_operationdefinition_9(inst):
    assert inst.affectsState is False
    assert inst.code == "submit-data"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Measure-submit-data"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "SubmitData"
    assert inst.parameter[0].documentation == "The measure report being submitted"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "measureReport"
    assert inst.parameter[0].type == "MeasureReport"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The individual resources that make up the data-of-interest " "being submitted"
    )
    assert inst.parameter[1].max == "*"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "resource"
    assert inst.parameter[1].type == "Resource"
    assert inst.parameter[1].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Measure"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Submit Data"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Measure-submit-data"
    assert inst.version == "4.3.0"


def test_operationdefinition_9(base_settings):
    """No. 9 tests collection for OperationDefinition.
    Test File: operation-measure-submit-data.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-measure-submit-data.json"
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_9(inst2)


def impl_operationdefinition_10(inst):
    assert inst.affectsState is False
    assert inst.code == "evaluate-measure"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.description == (
        "The evaluate-measure operation is used to calculate an "
        "eMeasure and obtain the results"
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[0].valueInteger == 3
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Measure-evaluate-measure"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "EvaluateMeasure"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "periodStart"
    assert inst.parameter[0].type == "date"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The end of the measurement period. The period will end at "
        "the end of the period implied by the supplied timestamp. "
        "E.g. a value of 2014 would set the period end to be "
        "2014-12-31T23:59:59 inclusive"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "periodEnd"
    assert inst.parameter[1].type == "date"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "The measure to evaluate. This parameter is only required "
        "when the operation is invoked on the resource type, it is "
        "not used when invoking the operation on a Measure instance"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "measure"
    assert inst.parameter[2].searchType == "reference"
    assert inst.parameter[2].type == "string"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
        "The type of measure report: subject, subject-list, or "
        "population. If not specified, a default value of subject "
        "will be used if the subject parameter is supplied, "
        "otherwise, population will be used"
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "reportType"
    assert inst.parameter[3].type == "code"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "subject"
    assert inst.parameter[4].searchType == "reference"
    assert inst.parameter[4].type == "string"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == (
        "Practitioner for which the measure will be calculated. If "
        "specified, the measure will be calculated only for subjects "
        "that have a primary relationship to the identified "
        "practitioner"
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "practitioner"
    assert inst.parameter[5].searchType == "reference"
    assert inst.parameter[5].type == "string"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "lastReceivedOn"
    assert inst.parameter[6].type == "dateTime"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 1
    assert inst.parameter[7].name == "return"
    assert inst.parameter[7].type == "MeasureReport"
    assert inst.parameter[7].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Measure"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Evaluate Measure"
    assert inst.type is True
    assert inst.url == (
        "http://hl7.org/fhir/OperationDefinition/Measure-evaluate-" "measure"
    )
    assert inst.version == "4.3.0"


def test_operationdefinition_10(base_settings):
    """No. 10 tests collection for OperationDefinition.
    Test File: operation-measure-evaluate-measure.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-measure-evaluate-measure.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_10(inst2)
