# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import immunizationrecommendation


def impl_immunizationrecommendation_1(inst):
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1235"
    assert inst.patient.reference == "Patient/example"
    assert inst.recommendation[0].date == fhirtypes.DateTime.validate(
        "2015-02-09T11:04:15.817-05:00"
    )
    assert inst.recommendation[0].dateCriterion[0].code.coding[0].code == "earliest"
    assert (
        inst.recommendation[0].dateCriterion[0].code.coding[0].display
        == "Earliest Date"
    )
    assert inst.recommendation[0].dateCriterion[0].code.coding[0].system == (
        "http://hl7.org/fhir/immunization-recommendation-date-" "criterion"
    )
    assert inst.recommendation[0].dateCriterion[0].value == fhirtypes.DateTime.validate(
        "2015-12-01T00:00:00-05:00"
    )
    assert inst.recommendation[0].dateCriterion[1].code.coding[0].code == "recommended"
    assert (
        inst.recommendation[0].dateCriterion[1].code.coding[0].display == "Recommended"
    )
    assert inst.recommendation[0].dateCriterion[1].code.coding[0].system == (
        "http://hl7.org/fhir/immunization-recommendation-date-" "criterion"
    )
    assert inst.recommendation[0].dateCriterion[1].value == fhirtypes.DateTime.validate(
        "2015-12-01T00:00:00-05:00"
    )
    assert inst.recommendation[0].dateCriterion[2].code.coding[0].code == "overdue"
    assert (
        inst.recommendation[0].dateCriterion[2].code.coding[0].display
        == "Past Due Date"
    )
    assert inst.recommendation[0].dateCriterion[2].code.coding[0].system == (
        "http://hl7.org/fhir/immunization-recommendation-date-" "criterion"
    )
    assert inst.recommendation[0].dateCriterion[2].value == fhirtypes.DateTime.validate(
        "2016-12-28T00:00:00-05:00"
    )
    assert inst.recommendation[0].doseNumber == 1
    assert inst.recommendation[0].forecastStatus.text == "Not Complete"
    assert inst.recommendation[0].protocol.authority.reference == "Organization/hl7"
    assert inst.recommendation[0].protocol.description == "First sequence in protocol"
    assert inst.recommendation[0].protocol.doseSequence == 1
    assert inst.recommendation[0].protocol.series == "Vaccination Series 1"
    assert (
        inst.recommendation[0].supportingImmunization[0].reference
        == "Immunization/example"
    )
    assert (
        inst.recommendation[0].supportingPatientInformation[0].reference
        == "Observation/example"
    )
    assert inst.recommendation[0].vaccineCode.coding[0].code == "14745005"
    assert inst.recommendation[0].vaccineCode.coding[0].display == "Hepatitis A vaccine"
    assert (
        inst.recommendation[0].vaccineCode.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Authored by ' "Joginder Madra</div>"
    )
    assert inst.text.status == "generated"


def test_immunizationrecommendation_1(base_settings):
    """No. 1 tests collection for ImmunizationRecommendation.
    Test File: immunizationrecommendation-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "immunizationrecommendation-example.json"
    )
    inst = immunizationrecommendation.ImmunizationRecommendation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImmunizationRecommendation" == inst.resource_type

    impl_immunizationrecommendation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImmunizationRecommendation" == data["resourceType"]

    inst2 = immunizationrecommendation.ImmunizationRecommendation(**data)
    impl_immunizationrecommendation_1(inst2)


def impl_immunizationrecommendation_2(inst):
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1235"
    assert inst.patient.reference == "Patient/example"
    assert inst.recommendation[0].date == fhirtypes.DateTime.validate(
        "2015-02-09T11:04:15.817-05:00"
    )
    assert inst.recommendation[0].dateCriterion[0].code.coding[0].code == "earliest"
    assert (
        inst.recommendation[0].dateCriterion[0].code.coding[0].display
        == "Earliest Date"
    )
    assert inst.recommendation[0].dateCriterion[0].code.coding[0].system == (
        "http://hl7.org/fhir/immunization-recommendation-date-" "criterion"
    )
    assert inst.recommendation[0].dateCriterion[0].value == fhirtypes.DateTime.validate(
        "2015-12-01T00:00:00-05:00"
    )
    assert inst.recommendation[0].dateCriterion[1].code.coding[0].code == "recommended"
    assert (
        inst.recommendation[0].dateCriterion[1].code.coding[0].display == "Recommended"
    )
    assert inst.recommendation[0].dateCriterion[1].code.coding[0].system == (
        "http://hl7.org/fhir/immunization-recommendation-date-" "criterion"
    )
    assert inst.recommendation[0].dateCriterion[1].value == fhirtypes.DateTime.validate(
        "2015-12-01T00:00:00-05:00"
    )
    assert inst.recommendation[0].dateCriterion[2].code.coding[0].code == "overdue"
    assert (
        inst.recommendation[0].dateCriterion[2].code.coding[0].display
        == "Past Due Date"
    )
    assert inst.recommendation[0].dateCriterion[2].code.coding[0].system == (
        "http://hl7.org/fhir/immunization-recommendation-date-" "criterion"
    )
    assert inst.recommendation[0].dateCriterion[2].value == fhirtypes.DateTime.validate(
        "2016-12-28T00:00:00-05:00"
    )
    assert inst.recommendation[0].doseNumber == 1
    assert inst.recommendation[0].forecastStatus.text == "Not Complete"
    assert inst.recommendation[0].protocol.authority.reference == "Organization/hl7"
    assert inst.recommendation[0].protocol.description == "First sequence in protocol"
    assert inst.recommendation[0].protocol.doseSequence == 1
    assert inst.recommendation[0].protocol.series == "Vaccination Series 1"
    assert (
        inst.recommendation[0].supportingImmunization[0].reference
        == "Immunization/example"
    )
    assert (
        inst.recommendation[0].supportingPatientInformation[0].reference
        == "Observation/example"
    )
    assert inst.recommendation[0].targetDisease.coding[0].code == "40468003"
    assert (
        inst.recommendation[0].targetDisease.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Authored by ' "Joginder Madra</div>"
    )
    assert inst.text.status == "generated"


def test_immunizationrecommendation_2(base_settings):
    """No. 2 tests collection for ImmunizationRecommendation.
    Test File: immunizationrecommendation-target-disease-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "immunizationrecommendation-target-disease-example.json"
    )
    inst = immunizationrecommendation.ImmunizationRecommendation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImmunizationRecommendation" == inst.resource_type

    impl_immunizationrecommendation_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImmunizationRecommendation" == data["resourceType"]

    inst2 = immunizationrecommendation.ImmunizationRecommendation(**data)
    impl_immunizationrecommendation_2(inst2)
