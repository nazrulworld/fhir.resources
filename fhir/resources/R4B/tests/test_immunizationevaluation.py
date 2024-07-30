# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import immunizationevaluation
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_immunizationevaluation_1(inst):
    assert inst.authority.reference == "Organization/hl7"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-01-10"}
        ).valueDateTime
    )
    assert inst.doseNumberPositiveInt == 1
    assert inst.doseStatus.coding[0].code == "valid"
    assert inst.doseStatus.coding[0].display == "Valid"
    assert (
        inst.doseStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status"
            }
        ).valueUri
    )
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.immunizationEvent.reference == "Immunization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.series == "Vaccination Series 1"
    assert inst.seriesDosesPositiveInt == 3
    assert inst.status == "completed"
    assert inst.targetDisease.coding[0].code == "1857005"
    assert (
        inst.targetDisease.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_immunizationevaluation_1(base_settings):
    """No. 1 tests collection for ImmunizationEvaluation.
    Test File: immunizationevaluation-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "immunizationevaluation-example.json"
    )
    inst = immunizationevaluation.ImmunizationEvaluation.model_validate_json(
        filename.read_bytes()
    )
    assert "ImmunizationEvaluation" == inst.get_resource_type()

    impl_immunizationevaluation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ImmunizationEvaluation" == data["resourceType"]

    inst2 = immunizationevaluation.ImmunizationEvaluation(**data)
    impl_immunizationevaluation_1(inst2)


def impl_immunizationevaluation_2(inst):
    assert inst.authority.reference == "Organization/hl7"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2013-01-10"}
        ).valueDateTime
    )
    assert inst.doseNumberPositiveInt == 2
    assert inst.doseStatus.coding[0].code == "notvalid"
    assert inst.doseStatus.coding[0].display == "Not Valid"
    assert (
        inst.doseStatus.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status"
            }
        ).valueUri
    )
    assert inst.doseStatusReason[0].coding[0].code == "outsidesched"
    assert (
        inst.doseStatusReason[0].coding[0].display
        == "Administered outside recommended schedule"
    )
    assert (
        inst.doseStatusReason[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status-reason"
            }
        ).valueUri
    )
    assert inst.id == "notValid"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.immunizationEvent.reference == "Immunization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.series == "Vaccination Series 1"
    assert inst.seriesDosesPositiveInt == 3
    assert inst.status == "completed"
    assert inst.targetDisease.coding[0].code == "1857005"
    assert (
        inst.targetDisease.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_immunizationevaluation_2(base_settings):
    """No. 2 tests collection for ImmunizationEvaluation.
    Test File: immunizationevaluation-example-notvalid.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "immunizationevaluation-example-notvalid.json"
    )
    inst = immunizationevaluation.ImmunizationEvaluation.model_validate_json(
        filename.read_bytes()
    )
    assert "ImmunizationEvaluation" == inst.get_resource_type()

    impl_immunizationevaluation_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ImmunizationEvaluation" == data["resourceType"]

    inst2 = immunizationevaluation.ImmunizationEvaluation(**data)
    impl_immunizationevaluation_2(inst2)
