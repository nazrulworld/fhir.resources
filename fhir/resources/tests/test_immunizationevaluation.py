# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import immunizationevaluation
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_immunizationevaluation_1(inst):
    assert inst.authority.reference == "Organization/hl7"
    assert inst.date == ExternalValidatorModel(valueDateTime="2013-01-10").valueDateTime
    assert inst.doseNumber == "1"
    assert inst.doseStatus.coding[0].code == "valid"
    assert inst.doseStatus.coding[0].display == "Valid"
    assert (
        inst.doseStatus.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status"
        ).valueUri
    )
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="urn:ietf:rfc:3986").valueUri
    )
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.immunizationEvent.reference == "Immunization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.series == "Vaccination Series 1"
    assert inst.seriesDoses == "3"
    assert inst.status == "completed"
    assert inst.targetDisease.coding[0].code == "1857005"
    assert (
        inst.targetDisease.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
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
        Path(filename).read_bytes()
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
    assert inst.date == ExternalValidatorModel(valueDateTime="2013-01-10").valueDateTime
    assert inst.doseStatus.coding[0].code == "notvalid"
    assert inst.doseStatus.coding[0].display == "Not Valid"
    assert (
        inst.doseStatus.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status"
        ).valueUri
    )
    assert inst.doseStatusReason[0].coding[0].code == "outsideschedule"
    assert inst.doseStatusReason[0].coding[0].display == "Outside Schedule"
    assert (
        inst.doseStatusReason[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status-reason"
        ).valueUri
    )
    assert inst.id == "notValid"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="urn:ietf:rfc:3986").valueUri
    )
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.immunizationEvent.reference == "Immunization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.series == "Vaccination Series 1"
    assert inst.status == "completed"
    assert inst.targetDisease.coding[0].code == "1857005"
    assert (
        inst.targetDisease.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
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
        Path(filename).read_bytes()
    )
    assert "ImmunizationEvaluation" == inst.get_resource_type()

    impl_immunizationevaluation_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ImmunizationEvaluation" == data["resourceType"]

    inst2 = immunizationevaluation.ImmunizationEvaluation(**data)
    impl_immunizationevaluation_2(inst2)
