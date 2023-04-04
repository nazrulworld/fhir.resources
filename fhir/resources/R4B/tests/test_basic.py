# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Basic
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import basic


def impl_basic_1(inst):
    assert inst.code.coding[0].code == "UMLCLASSMODEL"
    assert (
        inst.code.coding[0].system
        == "http://example.org/do-not-use/fhir-codes#resourceTypes"
    )
    assert inst.extension[0].extension[0].url == "name"
    assert inst.extension[0].extension[0].valueString == "Class1"
    assert inst.extension[0].extension[1].extension[0].url == "name"
    assert inst.extension[0].extension[1].extension[0].valueString == "attribute1"
    assert inst.extension[0].extension[1].extension[1].url == "minOccurs"
    assert inst.extension[0].extension[1].extension[1].valueInteger == 1
    assert inst.extension[0].extension[1].extension[2].url == "maxOccurs"
    assert inst.extension[0].extension[1].extension[2].valueCode == "*"
    assert inst.extension[0].extension[1].url == "attribute"
    assert inst.extension[0].extension[2].extension[0].url == "name"
    assert inst.extension[0].extension[2].extension[0].valueString == "attribute2"
    assert inst.extension[0].extension[2].extension[1].url == "minOccurs"
    assert inst.extension[0].extension[2].extension[1].valueInteger == 0
    assert inst.extension[0].extension[2].extension[2].url == "maxOccurs"
    assert inst.extension[0].extension[2].extension[2].valueInteger == 1
    assert inst.extension[0].extension[2].url == "attribute"
    assert (
        inst.extension[0].url
        == "http://example.org/do-not-use/fhir-extensions/UMLclass"
    )
    assert inst.id == "classModel"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"


def test_basic_1(base_settings):
    """No. 1 tests collection for Basic.
    Test File: basic-example2.json
    """
    filename = base_settings["unittest_data_dir"] / "basic-example2.json"
    inst = basic.Basic.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Basic" == inst.resource_type

    impl_basic_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Basic" == data["resourceType"]

    inst2 = basic.Basic(**data)
    impl_basic_1(inst2)


def impl_basic_2(inst):
    assert inst.code.text == "Example Narrative Tester"
    assert inst.id == "basic-example-narrative"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "additional"


def test_basic_2(base_settings):
    """No. 2 tests collection for Basic.
    Test File: basic-example-narrative.json
    """
    filename = base_settings["unittest_data_dir"] / "basic-example-narrative.json"
    inst = basic.Basic.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Basic" == inst.resource_type

    impl_basic_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Basic" == data["resourceType"]

    inst2 = basic.Basic(**data)
    impl_basic_2(inst2)


def impl_basic_3(inst):
    assert inst.author.reference == "Practitioner/example"
    assert inst.code.coding[0].code == "referral"
    assert (
        inst.code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/basic-resource-type"
    )
    assert inst.created == fhirtypes.Date.validate("2013-05-14")
    assert inst.extension[0].url == (
        "http://example.org/do-not-use/fhir-"
        "extensions/referral#requestingPractitioner"
    )
    assert inst.extension[0].valueReference.display == "Dokter Bronsig"
    assert inst.extension[0].valueReference.reference == "Practitioner/f201"
    assert (
        inst.extension[1].url
        == "http://example.org/do-not-use/fhir-extensions/referral#notes"
    )
    assert inst.extension[1].valueString == (
        "The patient had fever peaks over the last couple of days. He"
        " is worried about these peaks."
    )
    assert inst.extension[2].url == (
        "http://example.org/do-not-use/fhir-" "extensions/referral#fulfillingEncounter"
    )
    assert inst.extension[2].valueReference.reference == "Encounter/f201"
    assert inst.id == "referral"
    assert inst.identifier[0].system == "http://goodhealth.org/basic/identifiers"
    assert inst.identifier[0].value == "19283746"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.modifierExtension[0].url == (
        "http://example.org/do-not-use/fhir-" "extensions/referral#referredForService"
    )
    assert inst.modifierExtension[0].valueCodeableConcept.coding[0].code == "11429006"
    assert (
        inst.modifierExtension[0].valueCodeableConcept.coding[0].display
        == "Consultation"
    )
    assert (
        inst.modifierExtension[0].valueCodeableConcept.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.modifierExtension[1].url == (
        "http://example.org/do-not-use/fhir-" "extensions/referral#targetDate"
    )
    assert inst.modifierExtension[1].valuePeriod.end == fhirtypes.DateTime.validate(
        "2013-04-15"
    )
    assert inst.modifierExtension[1].valuePeriod.start == fhirtypes.DateTime.validate(
        "2013-04-01"
    )
    assert inst.modifierExtension[2].url == (
        "http://example.org/do-not-use/fhir-" "extensions/referral#status"
    )
    assert inst.modifierExtension[2].valueCode == "complete"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"


def test_basic_3(base_settings):
    """No. 3 tests collection for Basic.
    Test File: basic-example.json
    """
    filename = base_settings["unittest_data_dir"] / "basic-example.json"
    inst = basic.Basic.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Basic" == inst.resource_type

    impl_basic_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Basic" == data["resourceType"]

    inst2 = basic.Basic(**data)
    impl_basic_3(inst2)
