# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RiskAssessment
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import riskassessment


def impl_riskassessment_1(inst):
    assert inst.id == "population"
    assert inst.status == "final"
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
    assert inst.context.reference == "Encounter/example"
    assert inst.id == "cardiac"
    assert inst.identifier.system == "http://example.org"
    assert inst.identifier.use == "official"
    assert inst.identifier.value == "risk-assessment-cardiac"
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
    assert inst.comment == "High degree of certainty"
    assert inst.id == "genetic"
    assert inst.method.coding[0].code == "BRCAPRO"
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
    assert inst.condition.display == "Ischemic Stroke"
    assert inst.condition.reference == "Condition/stroke"
    assert inst.id == "prognosis"
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
        == "http://hl7.org/fhir/risk-probability"
    )
    assert inst.status == "final"
    assert inst.text.status == "additional"


def test_riskassessment_4(base_settings):
    """No. 4 tests collection for RiskAssessment.
    Test File: riskassessment-example-prognosis.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "riskassessment-example-prognosis.json"
    )
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
