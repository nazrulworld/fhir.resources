# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Basic
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import basic
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_basic_1(inst):
    assert inst.code.coding[0].code == "UMLCLASSMODEL"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/do-not-use/fhir-codes#resourceTypes"}
        ).valueUri
    )
    assert (
        inst.extension[0].extension[0].url
        == ExternalValidatorModel.model_validate({"valueUri": "name"}).valueUri
    )
    assert inst.extension[0].extension[0].valueString == "Class1"
    assert (
        inst.extension[0].extension[1].extension[0].url
        == ExternalValidatorModel.model_validate({"valueUri": "name"}).valueUri
    )
    assert inst.extension[0].extension[1].extension[0].valueString == "attribute1"
    assert (
        inst.extension[0].extension[1].extension[1].url
        == ExternalValidatorModel.model_validate({"valueUri": "minOccurs"}).valueUri
    )
    assert inst.extension[0].extension[1].extension[1].valueInteger == 1
    assert (
        inst.extension[0].extension[1].extension[2].url
        == ExternalValidatorModel.model_validate({"valueUri": "maxOccurs"}).valueUri
    )
    assert inst.extension[0].extension[1].extension[2].valueCode == "*"
    assert (
        inst.extension[0].extension[1].url
        == ExternalValidatorModel.model_validate({"valueUri": "attribute"}).valueUri
    )
    assert (
        inst.extension[0].extension[2].extension[0].url
        == ExternalValidatorModel.model_validate({"valueUri": "name"}).valueUri
    )
    assert inst.extension[0].extension[2].extension[0].valueString == "attribute2"
    assert (
        inst.extension[0].extension[2].extension[1].url
        == ExternalValidatorModel.model_validate({"valueUri": "minOccurs"}).valueUri
    )
    assert inst.extension[0].extension[2].extension[1].valueInteger == 0
    assert (
        inst.extension[0].extension[2].extension[2].url
        == ExternalValidatorModel.model_validate({"valueUri": "maxOccurs"}).valueUri
    )
    assert inst.extension[0].extension[2].extension[2].valueInteger == 1
    assert (
        inst.extension[0].extension[2].url
        == ExternalValidatorModel.model_validate({"valueUri": "attribute"}).valueUri
    )
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/do-not-use/fhir-extensions/UMLclass"}
        ).valueUri
    )
    assert inst.id == "classModel"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_basic_1(base_settings):
    """No. 1 tests collection for Basic.
    Test File: basic-example2.json
    """
    filename = base_settings["unittest_data_dir"] / "basic-example2.json"
    inst = basic.Basic.model_validate_json(filename.read_bytes())
    assert "Basic" == inst.get_resource_type()

    impl_basic_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Basic" == data["resourceType"]

    inst2 = basic.Basic(**data)
    impl_basic_1(inst2)


def impl_basic_2(inst):
    assert inst.code.text == "Example Narrative Tester"
    assert inst.id == "basic-example-narrative"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.text.status == "additional"


def test_basic_2(base_settings):
    """No. 2 tests collection for Basic.
    Test File: basic-example-narrative.json
    """
    filename = base_settings["unittest_data_dir"] / "basic-example-narrative.json"
    inst = basic.Basic.model_validate_json(filename.read_bytes())
    assert "Basic" == inst.get_resource_type()

    impl_basic_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Basic" == data["resourceType"]

    inst2 = basic.Basic(**data)
    impl_basic_2(inst2)


def impl_basic_3(inst):
    assert inst.author.reference == "Practitioner/example"
    assert inst.code.coding[0].code == "referral"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/basic-resource-type"}
        ).valueUri
    )
    assert (
        inst.created
        == ExternalValidatorModel.model_validate({"valueDate": "2013-05-14"}).valueDate
    )
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://example.org/do-not-use/fhir-extensions/referral#requestingPractitioner"
            }
        ).valueUri
    )
    assert inst.extension[0].valueReference.display == "Dokter Bronsig"
    assert inst.extension[0].valueReference.reference == "Practitioner/f201"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/do-not-use/fhir-extensions/referral#notes"}
        ).valueUri
    )
    assert inst.extension[1].valueString == (
        "The patient had fever peaks over the last couple of days. He"
        " is worried about these peaks."
    )
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://example.org/do-not-use/fhir-extensions/referral#fulfillingEncounter"
            }
        ).valueUri
    )
    assert inst.extension[2].valueReference.reference == "Encounter/f201"
    assert inst.id == "referral"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://goodhealth.org/basic/identifiers"}
        ).valueUri
    )
    assert inst.identifier[0].value == "19283746"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.modifierExtension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://example.org/do-not-use/fhir-extensions/referral#referredForService"
            }
        ).valueUri
    )
    assert inst.modifierExtension[0].valueCodeableConcept.coding[0].code == "11429006"
    assert (
        inst.modifierExtension[0].valueCodeableConcept.coding[0].display
        == "Consultation"
    )
    assert (
        inst.modifierExtension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert (
        inst.modifierExtension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://example.org/do-not-use/fhir-extensions/referral#targetDate"
            }
        ).valueUri
    )
    assert (
        inst.modifierExtension[1].valuePeriod.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-04-15"}
        ).valueDateTime
    )
    assert (
        inst.modifierExtension[1].valuePeriod.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-04-01"}
        ).valueDateTime
    )
    assert (
        inst.modifierExtension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://example.org/do-not-use/fhir-extensions/referral#status"
            }
        ).valueUri
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
    inst = basic.Basic.model_validate_json(filename.read_bytes())
    assert "Basic" == inst.get_resource_type()

    impl_basic_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Basic" == data["resourceType"]

    inst2 = basic.Basic(**data)
    impl_basic_3(inst2)
