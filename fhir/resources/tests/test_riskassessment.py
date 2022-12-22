# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RiskAssessment
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import riskassessment


def impl_riskassessment_1(inst):
    assert inst.contained[0].id == "group1"
    assert inst.id == "population"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "final"
    assert inst.subject.reference == "#group1"
    assert inst.text.status == "generated"


def test_riskassessment_1(base_settings):
    """No. 1 tests collection for RiskAssessment.
    Test File: riskassessment-example-population.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "riskassessment-example-population.json"
    )
    inst = riskassessment.RiskAssessment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RiskAssessment" == inst.resource_type

    impl_riskassessment_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RiskAssessment" == data["resourceType"]

    inst2 = riskassessment.RiskAssessment(**data)
    impl_riskassessment_1(inst2)


def impl_riskassessment_2(inst):
    assert inst.basis[0].reference == "Patient/pat2"
    assert inst.basis[1].reference == "DiagnosticReport/lipids"
    assert inst.basis[2].reference == "Observation/blood-pressure"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "cardiac"
    assert inst.identifier[0].system == "http://example.org"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "risk-assessment-cardiac"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2014-07-19T16:04:00Z"
    )
    assert inst.performer.display == "http://cvdrisk.nhlbi.nih.gov/#cholesterol"
    assert inst.prediction[0].outcome.text == "Heart Attack"
    assert float(inst.prediction[0].probabilityDecimal) == float(0.02)
    assert inst.prediction[0].whenRange.high.code == "a"
    assert inst.prediction[0].whenRange.high.system == "http://unitsofmeasure.org"
    assert inst.prediction[0].whenRange.high.unit == "years"
    assert float(inst.prediction[0].whenRange.high.value) == float(49)
    assert inst.prediction[0].whenRange.low.code == "a"
    assert inst.prediction[0].whenRange.low.system == "http://unitsofmeasure.org"
    assert inst.prediction[0].whenRange.low.unit == "years"
    assert float(inst.prediction[0].whenRange.low.value) == float(39)
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "additional"


def test_riskassessment_2(base_settings):
    """No. 2 tests collection for RiskAssessment.
    Test File: riskassessment-example-cardiac.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "riskassessment-example-cardiac.json"
    )
    inst = riskassessment.RiskAssessment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RiskAssessment" == inst.resource_type

    impl_riskassessment_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RiskAssessment" == data["resourceType"]

    inst2 = riskassessment.RiskAssessment(**data)
    impl_riskassessment_2(inst2)


def impl_riskassessment_3(inst):
    assert inst.basis[0].reference == "List/prognosis"
    assert inst.id == "genetic"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.method.coding[0].code == "BRCAPRO"
    assert inst.note[0].text == "High degree of certainty"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate(
        "2006-01-13T23:01:00Z"
    )
    assert inst.prediction[0].outcome.text == "Breast Cancer"
    assert float(inst.prediction[0].probabilityDecimal) == float(0.000168)
    assert inst.prediction[0].whenRange.high.code == "a"
    assert inst.prediction[0].whenRange.high.system == "http://unitsofmeasure.org"
    assert inst.prediction[0].whenRange.high.unit == "years"
    assert float(inst.prediction[0].whenRange.high.value) == float(53)
    assert inst.prediction[1].outcome.text == "Breast Cancer"
    assert float(inst.prediction[1].probabilityDecimal) == float(0.000368)
    assert inst.prediction[1].whenRange.high.code == "a"
    assert inst.prediction[1].whenRange.high.system == "http://unitsofmeasure.org"
    assert inst.prediction[1].whenRange.high.unit == "years"
    assert float(inst.prediction[1].whenRange.high.value) == float(57)
    assert inst.prediction[1].whenRange.low.code == "a"
    assert inst.prediction[1].whenRange.low.system == "http://unitsofmeasure.org"
    assert inst.prediction[1].whenRange.low.unit == "years"
    assert float(inst.prediction[1].whenRange.low.value) == float(54)
    assert inst.prediction[2].outcome.text == "Breast Cancer"
    assert float(inst.prediction[2].probabilityDecimal) == float(0.000594)
    assert inst.prediction[2].whenRange.high.code == "a"
    assert inst.prediction[2].whenRange.high.system == "http://unitsofmeasure.org"
    assert inst.prediction[2].whenRange.high.unit == "years"
    assert float(inst.prediction[2].whenRange.high.value) == float(62)
    assert inst.prediction[2].whenRange.low.code == "a"
    assert inst.prediction[2].whenRange.low.system == "http://unitsofmeasure.org"
    assert inst.prediction[2].whenRange.low.unit == "years"
    assert float(inst.prediction[2].whenRange.low.value) == float(58)
    assert inst.prediction[3].outcome.text == "Breast Cancer"
    assert float(inst.prediction[3].probabilityDecimal) == float(0.000838)
    assert inst.prediction[3].whenRange.high.code == "a"
    assert inst.prediction[3].whenRange.high.system == "http://unitsofmeasure.org"
    assert inst.prediction[3].whenRange.high.unit == "years"
    assert float(inst.prediction[3].whenRange.high.value) == float(67)
    assert inst.prediction[3].whenRange.low.code == "a"
    assert inst.prediction[3].whenRange.low.system == "http://unitsofmeasure.org"
    assert inst.prediction[3].whenRange.low.unit == "years"
    assert float(inst.prediction[3].whenRange.low.value) == float(63)
    assert inst.prediction[4].outcome.text == "Breast Cancer"
    assert float(inst.prediction[4].probabilityDecimal) == float(0.001089)
    assert inst.prediction[4].whenRange.high.code == "a"
    assert inst.prediction[4].whenRange.high.system == "http://unitsofmeasure.org"
    assert inst.prediction[4].whenRange.high.unit == "years"
    assert float(inst.prediction[4].whenRange.high.value) == float(72)
    assert inst.prediction[4].whenRange.low.code == "a"
    assert inst.prediction[4].whenRange.low.system == "http://unitsofmeasure.org"
    assert inst.prediction[4].whenRange.low.unit == "years"
    assert float(inst.prediction[4].whenRange.low.value) == float(68)
    assert inst.prediction[5].outcome.text == "Breast Cancer"
    assert float(inst.prediction[5].probabilityDecimal) == float(0.001327)
    assert inst.prediction[5].whenRange.high.code == "a"
    assert inst.prediction[5].whenRange.high.system == "http://unitsofmeasure.org"
    assert inst.prediction[5].whenRange.high.unit == "years"
    assert float(inst.prediction[5].whenRange.high.value) == float(77)
    assert inst.prediction[5].whenRange.low.code == "a"
    assert inst.prediction[5].whenRange.low.system == "http://unitsofmeasure.org"
    assert inst.prediction[5].whenRange.low.unit == "years"
    assert float(inst.prediction[5].whenRange.low.value) == float(73)
    assert inst.prediction[6].outcome.text == "Breast Cancer"
    assert float(inst.prediction[6].probabilityDecimal) == float(0.00153)
    assert inst.prediction[6].whenRange.high.code == "a"
    assert inst.prediction[6].whenRange.high.system == "http://unitsofmeasure.org"
    assert inst.prediction[6].whenRange.high.unit == "years"
    assert float(inst.prediction[6].whenRange.high.value) == float(82)
    assert inst.prediction[6].whenRange.low.code == "a"
    assert inst.prediction[6].whenRange.low.system == "http://unitsofmeasure.org"
    assert inst.prediction[6].whenRange.low.unit == "years"
    assert float(inst.prediction[6].whenRange.low.value) == float(78)
    assert inst.prediction[7].outcome.text == "Breast Cancer"
    assert float(inst.prediction[7].probabilityDecimal) == float(0.001663)
    assert inst.prediction[7].whenRange.high.code == "a"
    assert inst.prediction[7].whenRange.high.system == "http://unitsofmeasure.org"
    assert inst.prediction[7].whenRange.high.unit == "years"
    assert float(inst.prediction[7].whenRange.high.value) == float(88)
    assert inst.prediction[7].whenRange.low.code == "a"
    assert inst.prediction[7].whenRange.low.system == "http://unitsofmeasure.org"
    assert inst.prediction[7].whenRange.low.unit == "years"
    assert float(inst.prediction[7].whenRange.low.value) == float(83)
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/b248b1b2-1686-4b94-9936-37d7a5f94b51"
    assert inst.text.status == "generated"


def test_riskassessment_3(base_settings):
    """No. 3 tests collection for RiskAssessment.
    Test File: riskassessment-example.json
    """
    filename = base_settings["unittest_data_dir"] / "riskassessment-example.json"
    inst = riskassessment.RiskAssessment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RiskAssessment" == inst.resource_type

    impl_riskassessment_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RiskAssessment" == data["resourceType"]

    inst2 = riskassessment.RiskAssessment(**data)
    impl_riskassessment_3(inst2)


def impl_riskassessment_4(inst):
    assert inst.basedOn.reference == "ImmunizationRecommendation/example"
    assert inst.basis[0].reference == "DiagnosticReport/example"
    assert inst.basis[1].reference == "Observation/example"
    assert inst.code.coding[0].code == "709510001"
    assert inst.code.coding[0].display == "Assessment of risk for disease (procedure)"
    assert inst.code.coding[0].system == "http://browser.ihtsdotools.org/"
    assert inst.condition.reference == "Condition/example"
    assert inst.encounter.display == "Encounter with patient @example"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "riskexample"
    assert inst.identifier[0].system == "http://example.org"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "risk-assessment-breastcancer1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == "This risk assessment is for reference only"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2017-10-10")
    assert inst.parent.reference == "DiagnosticReport/example"
    assert inst.performer.reference == "Practitioner/example"
    assert inst.prediction[0].outcome.text == "Breast Cancer"
    assert float(inst.prediction[0].probabilityDecimal) == float(0.000368)
    assert inst.prediction[0].whenRange.high.code == "a"
    assert inst.prediction[0].whenRange.high.system == "http://unitsofmeasure.org"
    assert inst.prediction[0].whenRange.high.unit == "years"
    assert float(inst.prediction[0].whenRange.high.value) == float(57)
    assert inst.prediction[0].whenRange.low.code == "a"
    assert inst.prediction[0].whenRange.low.system == "http://unitsofmeasure.org"
    assert inst.prediction[0].whenRange.low.unit == "years"
    assert float(inst.prediction[0].whenRange.low.value) == float(54)
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Risk assessment '
        "for reference only</div>"
    )
    assert inst.text.status == "generated"


def test_riskassessment_4(base_settings):
    """No. 4 tests collection for RiskAssessment.
    Test File: riskassessment-riskexample.json
    """
    filename = base_settings["unittest_data_dir"] / "riskassessment-riskexample.json"
    inst = riskassessment.RiskAssessment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RiskAssessment" == inst.resource_type

    impl_riskassessment_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RiskAssessment" == data["resourceType"]

    inst2 = riskassessment.RiskAssessment(**data)
    impl_riskassessment_4(inst2)


def impl_riskassessment_5(inst):
    assert inst.basis[0].reference == "Observation/example-genetics-brcapat"
    assert inst.code.coding[0].code == "709510001"
    assert inst.code.coding[0].display == "Assessment of risk for disease (procedure)"
    assert inst.code.coding[0].system == "http://browser.ihtsdotools.org/"
    assert inst.id == "breastcancer-risk"
    assert inst.identifier[0].system == "http://example.org"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "risk-assessment-breastcancer1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == (
        "This risk assessment is based on BRCA1 and BRCA2 genetic " "mutation test"
    )
    assert inst.performer.reference == "Practitioner/example"
    assert inst.prediction[0].outcome.text == "Unknown risk of developing breast cancer"
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "additional"


def test_riskassessment_5(base_settings):
    """No. 5 tests collection for RiskAssessment.
    Test File: riskassessment-example-breastcancer.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "riskassessment-example-breastcancer.json"
    )
    inst = riskassessment.RiskAssessment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RiskAssessment" == inst.resource_type

    impl_riskassessment_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RiskAssessment" == data["resourceType"]

    inst2 = riskassessment.RiskAssessment(**data)
    impl_riskassessment_5(inst2)


def impl_riskassessment_6(inst):
    assert inst.condition.display == "Ischemic Stroke"
    assert inst.condition.reference == "Condition/stroke"
    assert inst.id == "prognosis"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2010-11-22")
    assert (
        inst.prediction[0].outcome.coding[0].code
        == "249943000:363698007=72098002,260868000=6934004"
    )
    assert inst.prediction[0].outcome.coding[0].system == "http://snomed.info/sct"
    assert inst.prediction[0].outcome.text == "permanent weakness of the left arm"
    assert inst.prediction[0].qualitativeRisk.coding[0].code == "moderate"
    assert inst.prediction[0].qualitativeRisk.coding[0].display == "moderate likelihood"
    assert (
        inst.prediction[0].qualitativeRisk.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/risk-probability"
    )
    assert inst.status == "final"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "additional"


def test_riskassessment_6(base_settings):
    """No. 6 tests collection for RiskAssessment.
    Test File: riskassessment-example-prognosis.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "riskassessment-example-prognosis.json"
    )
    inst = riskassessment.RiskAssessment.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RiskAssessment" == inst.resource_type

    impl_riskassessment_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RiskAssessment" == data["resourceType"]

    inst2 = riskassessment.RiskAssessment(**data)
    impl_riskassessment_6(inst2)
