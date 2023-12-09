# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DataElement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import dataelement


def impl_dataelement_1(inst):
    assert inst.contained[0].id == "2179414"
    assert inst.contained[1].id == "2179414-permitted"
    assert inst.contained[2].id == "2179414-cm"
    assert inst.date == fhirtypes.DateTime.validate("2016-01-01")
    assert inst.element[0].binding.strength == "required"
    assert inst.element[0].binding.valueSetReference.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/11179-permitted-" "value-valueset"
    )
    assert (
        inst.element[0].binding.valueSetReference.extension[0].valueReference.reference
        == "#2179414-permitted"
    )
    assert inst.element[0].binding.valueSetReference.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/11179-permitted-" "value-conceptmap"
    )
    assert (
        inst.element[0].binding.valueSetReference.extension[1].valueReference.reference
        == "#2179414-cm"
    )
    assert inst.element[0].binding.valueSetReference.reference == "#2179414"
    assert inst.element[0].code[0].code == "46098-0"
    assert inst.element[0].code[0].display == "Sex"
    assert inst.element[0].code[0].system == "http://loinc.org"
    assert inst.element[0].definition == "The code representing the gender of a person."
    assert (
        inst.element[0].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/minLength"
    )
    assert inst.element[0].extension[0].valueInteger == 1
    assert inst.element[0].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/elementdefinition-" "question"
    )
    assert inst.element[0].extension[1].valueString == "Gender"
    assert inst.element[0].mapping[0].identity == "fhir"
    assert inst.element[0].mapping[0].language == "application/xquery"
    assert inst.element[0].mapping[0].map == "return f:/Patient/f:gender"
    assert inst.element[0].maxLength == 13
    assert inst.element[0].path == "Gender"
    assert inst.element[0].type[0].code == "CodeableConcept"
    assert inst.id == "gender"
    assert inst.identifier[0].value == "2179650"
    assert inst.jurisdiction[0].coding[0].code == "US"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.mapping[0].identity == "fhir"
    assert inst.mapping[0].name == "Fast Healthcare Interoperable Resources (FHIR)"
    assert inst.mapping[0].uri == "http://hl7.org/fhir/api"
    assert inst.name == "Gender Code"
    assert inst.publisher == "DCP"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Administrative gender"
    assert inst.version == "1.0"


def test_dataelement_1(base_settings):
    """No. 1 tests collection for DataElement.
    Test File: dataelement-example.json
    """
    filename = base_settings["unittest_data_dir"] / "dataelement-example.json"
    inst = dataelement.DataElement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DataElement" == inst.resource_type

    impl_dataelement_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DataElement" == data["resourceType"]

    inst2 = dataelement.DataElement(**data)
    impl_dataelement_1(inst2)


def impl_dataelement_2(inst):
    assert inst.element[0].alias[0] == "Protime, PT"
    assert inst.element[0].comment == (
        "Used to screen the integrity of the extrinsic and common "
        "pathways of coagulation and to monitor warfarin "
        "anticoagulation. "
    )
    assert inst.element[0].definition == (
        "The PT test evaluates the extrinsic and common pathways of "
        "the coagulation cascade."
    )
    assert inst.element[0].example[0].label == "Simple"
    assert float(inst.element[0].example[0].valueDecimal) == float(10.0)
    assert inst.element[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/elementdefinition-" "allowedUnits"
    )
    assert inst.element[0].extension[0].valueCodeableConcept.coding[0].code == "s"
    assert (
        inst.element[0].extension[0].valueCodeableConcept.coding[0].display == "second"
    )
    assert (
        inst.element[0].extension[0].valueCodeableConcept.coding[0].system
        == "http://unitsofmeasure.org"
    )
    assert (
        inst.element[0].extension[0].valueCodeableConcept.coding[0].userSelected is True
    )
    assert inst.element[0].extension[0].valueCodeableConcept.coding[0].version == "1.9"
    assert inst.element[0].extension[0].valueCodeableConcept.text == "second"
    assert inst.element[0].mapping[0].identity == "loinc"
    assert inst.element[0].mapping[0].map == "5964-2"
    assert inst.element[0].path == "prothrombin"
    assert inst.element[0].requirements == (
        "This test is orderable. A plasma specimen in a 3.2% sodium "
        "citrate blue top tube is required."
    )
    assert inst.element[0].type[0].code == "decimal"
    assert inst.id == "prothrombin"
    assert inst.identifier[0].assigner.display == "Century Hospital Laboratory"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2011-05-19")
    assert (
        inst.identifier[0].system
        == "http://www.CenturyHospital/Laboratory/DirectoryofServices"
    )
    assert inst.identifier[0].type.text == "Prothrombin Time, PT"
    assert inst.identifier[0].value == "11"
    assert inst.mapping[0].comment == "Version 2.48 or later"
    assert inst.mapping[0].identity == "loinc"
    assert inst.mapping[0].name == "LOINC"
    assert inst.mapping[0].uri == "http://loinc.org/"
    assert inst.name == "Prothrombin Time"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_dataelement_2(base_settings):
    """No. 2 tests collection for DataElement.
    Test File: dataelement-labtestmaster-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "dataelement-labtestmaster-example.json"
    )
    inst = dataelement.DataElement.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DataElement" == inst.resource_type

    impl_dataelement_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DataElement" == data["resourceType"]

    inst2 = dataelement.DataElement(**data)
    impl_dataelement_2(inst2)
