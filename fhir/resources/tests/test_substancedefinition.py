# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import substancedefinition
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_substancedefinition_1(inst):
    assert inst.classification[0].coding[0].code == "100000075670"
    assert inst.classification[0].coding[0].display == "Chemical"
    assert (
        inst.classification[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://example.europa.eu/fhir/SubstanceType"
        ).valueUri
    )
    assert inst.code[0].code.coding[0].code == "SUB99611MIG"
    assert (
        inst.code[0].code.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://example.europa.eu/fhir/Substance"
        ).valueUri
    )
    assert inst.domain.coding[0].code == "100000000012"
    assert inst.domain.coding[0].display == "Human use"
    assert (
        inst.domain.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://example.europa.eu/fhir/Domain"
        ).valueUri
    )
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://example.europa.eu/fhir/SMSId"
        ).valueUri
    )
    assert inst.identifier[0].value == "100000099270"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name[0].language[0].coding[0].code == "en"
    assert inst.name[0].language[0].coding[0].display == "English"
    assert (
        inst.name[0].language[0].coding[0].system
        == ExternalValidatorModel(valueUri="urn:ietf:bcp:47").valueUri
    )
    assert inst.name[0].name == "PARACETAMOL"
    assert inst.name[0].preferred is True
    assert inst.name[0].status.coding[0].code == "200000005004"
    assert inst.name[0].status.coding[0].display == "Current"
    assert (
        inst.name[0].status.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://example.europa.eu/fhir/Status"
        ).valueUri
    )
    assert inst.name[1].language[0].coding[0].code == "el"
    assert inst.name[1].language[0].coding[0].display == "Greek"
    assert (
        inst.name[1].language[0].coding[0].system
        == ExternalValidatorModel(valueUri="urn:ietf:bcp:47").valueUri
    )
    assert inst.name[1].name == "ΠΑΡΑΚΕΤΑΜΌΛΗ"
    assert inst.name[1].preferred is False
    assert inst.name[1].status.coding[0].code == "200000005004"
    assert inst.name[1].status.coding[0].display == "Current"
    assert (
        inst.name[1].status.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://example.europa.eu/fhir/Status"
        ).valueUri
    )
    assert inst.name[2].language[0].coding[0].code == "bg"
    assert inst.name[2].language[0].coding[0].display == "Bulgarian"
    assert (
        inst.name[2].language[0].coding[0].system
        == ExternalValidatorModel(valueUri="urn:ietf:bcp:47").valueUri
    )
    assert inst.name[2].name == "ПАРАЦЕТАМОЛ"
    assert inst.name[2].preferred is False
    assert inst.name[2].status.coding[0].code == "200000005004"
    assert inst.name[2].status.coding[0].display == "Current"
    assert (
        inst.name[2].status.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://example.europa.eu/fhir/Status"
        ).valueUri
    )
    assert inst.name[3].language[0].coding[0].code == "en"
    assert inst.name[3].language[0].coding[0].display == "English"
    assert (
        inst.name[3].language[0].coding[0].system
        == ExternalValidatorModel(valueUri="urn:ietf:bcp:47").valueUri
    )
    assert inst.name[3].name == "ACETAMINOPHEN"
    assert inst.name[3].preferred is False
    assert inst.name[3].status.coding[0].code == "200000005004"
    assert inst.name[3].status.coding[0].display == "Current"
    assert (
        inst.name[3].status.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://example.europa.eu/fhir/Status"
        ).valueUri
    )
    assert inst.status.coding[0].code == "200000005004"
    assert inst.status.coding[0].display == "Current"
    assert (
        inst.status.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://example.europa.eu/fhir/Status"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_substancedefinition_1(base_settings):
    """No. 1 tests collection for SubstanceDefinition.
    Test File: substancedefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "substancedefinition-example.json"
    inst = substancedefinition.SubstanceDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "SubstanceDefinition" == inst.get_resource_type()

    impl_substancedefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SubstanceDefinition" == data["resourceType"]

    inst2 = substancedefinition.SubstanceDefinition(**data)
    impl_substancedefinition_1(inst2)
