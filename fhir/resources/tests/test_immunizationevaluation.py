# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import immunizationevaluation


def impl_immunizationevaluation_1(inst):
    assert inst.authority.reference == "Organization/hl7"
    assert inst.date == fhirtypes.DateTime.validate("2013-01-10")
    assert inst.doseNumberPositiveInt == 1
    assert inst.doseStatus.coding[0].code == "valid"
    assert inst.doseStatus.coding[0].display == "Valid"
    assert inst.doseStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/immunization-" "evaluation-dose-status"
    )
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.immunizationEvent.reference == "Immunization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.series == "Vaccination Series 1"
    assert inst.seriesDosesPositiveInt == 3
    assert inst.status == "completed"
    assert inst.targetDisease.coding[0].code == "1857005"
    assert inst.targetDisease.coding[0].system == "http://snomed.info/sct"
    assert inst.text.status == "generated"


def test_immunizationevaluation_1(base_settings):
    """No. 1 tests collection for ImmunizationEvaluation.
    Test File: immunizationevaluation-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "immunizationevaluation-example.json"
    )
    inst = immunizationevaluation.ImmunizationEvaluation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImmunizationEvaluation" == inst.resource_type

    impl_immunizationevaluation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImmunizationEvaluation" == data["resourceType"]

    inst2 = immunizationevaluation.ImmunizationEvaluation(**data)
    impl_immunizationevaluation_1(inst2)


def impl_immunizationevaluation_2(inst):
    assert inst.authority.reference == "Organization/hl7"
    assert inst.date == fhirtypes.DateTime.validate("2013-01-10")
    assert inst.doseNumberPositiveInt == 2
    assert inst.doseStatus.coding[0].code == "notvalid"
    assert inst.doseStatus.coding[0].display == "Not Valid"
    assert inst.doseStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/immunization-" "evaluation-dose-status"
    )
    assert inst.doseStatusReason[0].coding[0].code == "outsidesched"
    assert (
        inst.doseStatusReason[0].coding[0].display
        == "Administered outside recommended schedule"
    )
    assert inst.doseStatusReason[0].coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/immunization-"
        "evaluation-dose-status-reason"
    )
    assert inst.id == "notValid"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.immunizationEvent.reference == "Immunization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.series == "Vaccination Series 1"
    assert inst.seriesDosesPositiveInt == 3
    assert inst.status == "completed"
    assert inst.targetDisease.coding[0].code == "1857005"
    assert inst.targetDisease.coding[0].system == "http://snomed.info/sct"
    assert inst.text.status == "generated"


def test_immunizationevaluation_2(base_settings):
    """No. 2 tests collection for ImmunizationEvaluation.
    Test File: immunizationevaluation-example-notvalid.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "immunizationevaluation-example-notvalid.json"
    )
    inst = immunizationevaluation.ImmunizationEvaluation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImmunizationEvaluation" == inst.resource_type

    impl_immunizationevaluation_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImmunizationEvaluation" == data["resourceType"]

    inst2 = immunizationevaluation.ImmunizationEvaluation(**data)
    impl_immunizationevaluation_2(inst2)
