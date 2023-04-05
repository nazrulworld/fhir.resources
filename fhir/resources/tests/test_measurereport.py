# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MeasureReport
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import measurereport


def impl_measurereport_1(inst):
    assert inst.contained[0].id == "reporter"
    assert inst.date == fhirtypes.DateTime.validate("2014-04-01")
    assert inst.evaluatedResource[0].reference == "Condition/example"
    assert inst.group[0].id == "CMS146-group-1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].count == 1
    assert inst.group[0].population[1].code.coding[0].code == "numerator"
    assert inst.group[0].population[1].count == 1
    assert inst.group[0].population[2].code.coding[0].code == "denominator"
    assert inst.group[0].population[2].count == 1
    assert inst.group[0].population[3].code.coding[0].code == "denominator-exclusion"
    assert inst.group[0].population[3].count == 0
    assert inst.group[0].stratifier[0].code.text == "stratifier-ages-up-to-9"
    assert (
        inst.group[0].stratifier[0].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[0].count == 1
    assert (
        inst.group[0].stratifier[0].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[1].count == 1
    assert (
        inst.group[0].stratifier[0].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[2].count == 1
    assert (
        inst.group[0].stratifier[0].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[3].count == 0
    assert inst.group[0].stratifier[0].stratum[0].valueBoolean is True
    assert (
        inst.group[0].stratifier[0].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[0].count == 0
    assert (
        inst.group[0].stratifier[0].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[1].count == 0
    assert (
        inst.group[0].stratifier[0].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[2].count == 0
    assert (
        inst.group[0].stratifier[0].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[3].count == 0
    assert inst.group[0].stratifier[0].stratum[1].valueBoolean is False
    assert inst.group[0].stratifier[1].code.text == "stratifier-ages-10-plus"
    assert (
        inst.group[0].stratifier[1].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[0].count == 0
    assert (
        inst.group[0].stratifier[1].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[1].count == 0
    assert (
        inst.group[0].stratifier[1].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[2].count == 0
    assert (
        inst.group[0].stratifier[1].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[3].count == 0
    assert inst.group[0].stratifier[1].stratum[0].valueBoolean is True
    assert (
        inst.group[0].stratifier[1].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[0].count == 1
    assert (
        inst.group[0].stratifier[1].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[1].count == 1
    assert (
        inst.group[0].stratifier[1].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[2].count == 1
    assert (
        inst.group[0].stratifier[1].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[3].count == 0
    assert inst.group[0].stratifier[1].stratum[1].valueBoolean is True
    assert inst.group[0].stratifier[2].code.text == "stratifier-gender"
    assert (
        inst.group[0].stratifier[2].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[0].count == 1
    assert (
        inst.group[0].stratifier[2].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[1].count == 1
    assert (
        inst.group[0].stratifier[2].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[2].count == 1
    assert (
        inst.group[0].stratifier[2].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[3].count == 0
    assert inst.group[0].stratifier[2].stratum[0].valueCodeableConcept.text == "male"
    assert (
        inst.group[0].stratifier[2].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[0].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[1].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[2].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[3].count == 0
    assert inst.group[0].stratifier[2].stratum[1].valueCodeableConcept.text == "female"
    assert (
        inst.group[0].stratifier[2].stratum[2].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[0].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[1].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[2].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[3].count == 0
    assert inst.group[0].stratifier[2].stratum[2].valueCodeableConcept.text == "other"
    assert (
        inst.group[0].stratifier[2].stratum[3].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[0].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[1].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[2].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[3].count == 0
    assert inst.group[0].stratifier[2].stratum[3].valueCodeableConcept.text == "unknown"
    assert inst.id == "measurereport-cms146-cat1-example"
    assert inst.identifier[0].value == "measurereport-cms146-cat1-example-2017-03-13"
    assert inst.measure == "http://example.org/fhir/Measure/CMS146"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2014-03-31")
    assert inst.period.start == fhirtypes.DateTime.validate("2014-01-01")
    assert inst.reporter.reference == "#reporter"
    assert inst.status == "complete"
    assert inst.subject.reference == "Patient/123"
    assert inst.text.status == "generated"
    assert inst.type == "individual"


def test_measurereport_1(base_settings):
    """No. 1 tests collection for MeasureReport.
    Test File: measurereport-cms146-cat1-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "measurereport-cms146-cat1-example.json"
    )
    inst = measurereport.MeasureReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MeasureReport" == inst.resource_type

    impl_measurereport_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MeasureReport" == data["resourceType"]

    inst2 = measurereport.MeasureReport(**data)
    impl_measurereport_1(inst2)


def impl_measurereport_2(inst):
    assert inst.contained[0].id == "patient-new"
    assert inst.group[0].code.coding[0].code == "QRPH_ADX_ART5_N"
    assert float(inst.group[0].measureScoreQuantity.value) == float(1)
    assert inst.group[0].stratifier[0].code.coding[0].code == "AGE_GROUP:SEX"
    assert float(
        inst.group[0].stratifier[0].stratum[0].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[0].stratifier[0].stratum[0].valueCodeableConcept.coding[0].code
        == "P0Y--P20Y:F"
    )
    assert float(
        inst.group[0].stratifier[0].stratum[1].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[0].stratifier[0].stratum[1].valueCodeableConcept.coding[0].code
        == "P0Y--P20Y:M"
    )
    assert float(
        inst.group[0].stratifier[0].stratum[2].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[0].stratifier[0].stratum[2].valueCodeableConcept.coding[0].code
        == "P20Y--P40Y:F"
    )
    assert float(
        inst.group[0].stratifier[0].stratum[3].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[0].stratifier[0].stratum[3].valueCodeableConcept.coding[0].code
        == "P20Y--P40Y:M"
    )
    assert float(
        inst.group[0].stratifier[0].stratum[4].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[0].stratifier[0].stratum[4].valueCodeableConcept.coding[0].code
        == "P40Y--P65Y:F"
    )
    assert float(
        inst.group[0].stratifier[0].stratum[5].measureScoreQuantity.value
    ) == float(1)
    assert (
        inst.group[0].stratifier[0].stratum[5].valueCodeableConcept.coding[0].code
        == "P40Y--P65Y:M"
    )
    assert inst.id == "general-example-of-report"
    assert inst.measure == "http://ohie.org/Measure/hiv-indicators"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2018-12-31")
    assert inst.period.start == fhirtypes.DateTime.validate("2018-01-01")
    assert inst.status == "complete"
    assert inst.subject.reference == "#patient-new"
    assert inst.text.status == "generated"
    assert inst.type == "individual"


def test_measurereport_2(base_settings):
    """No. 2 tests collection for MeasureReport.
    Test File: measurereport-general-example.json
    """
    filename = base_settings["unittest_data_dir"] / "measurereport-general-example.json"
    inst = measurereport.MeasureReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MeasureReport" == inst.resource_type

    impl_measurereport_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MeasureReport" == data["resourceType"]

    inst2 = measurereport.MeasureReport(**data)
    impl_measurereport_2(inst2)


def impl_measurereport_3(inst):
    assert inst.contained[0].id == "1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].code.coding[0].display == "Initial Population"
    assert (
        inst.group[0].population[0].code.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/measure-population"
    )
    assert inst.group[0].population[0].count == 2
    assert inst.group[0].population[0].subjectResults.reference == "#1"
    assert inst.id == "788ca455-e11b1a59"
    assert inst.measure == (
        "http://lantanagroup.com/fhir/nhsn-measures/Measure/NHSNGlyce"
        "micControlHypoglycemicInitialPopulation"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2022-08-31T23:59:59+00:00")
    assert inst.period.start == fhirtypes.DateTime.validate("2022-08-01T00:00:00+00:00")
    assert (
        inst.reporter.reference == "Organization/aa389ad5-e6fe-4030-88ce-010ab96e4ac4"
    )
    assert inst.status == "complete"
    assert inst.text.status == "generated"
    assert inst.type == "subject-list"


def test_measurereport_3(base_settings):
    """No. 3 tests collection for MeasureReport.
    Test File: measurereport-788ca455-e11b1a59.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "measurereport-788ca455-e11b1a59.json"
    )
    inst = measurereport.MeasureReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MeasureReport" == inst.resource_type

    impl_measurereport_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MeasureReport" == data["resourceType"]

    inst2 = measurereport.MeasureReport(**data)
    impl_measurereport_3(inst2)


def impl_measurereport_4(inst):
    assert inst.group[0].code.coding[0].code == "QRPH_ADX_ART1_N"
    assert float(inst.group[0].measureScoreQuantity.value) == float(0)
    assert inst.group[0].stratifier[0].code.coding[0].code == "AGE_GROUP:SEX"
    assert float(
        inst.group[0].stratifier[0].stratum[0].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[0].stratifier[0].stratum[0].valueCodeableConcept.coding[0].code
        == "P0Y--P1Y:F"
    )
    assert float(
        inst.group[0].stratifier[0].stratum[1].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[0].stratifier[0].stratum[1].valueCodeableConcept.coding[0].code
        == "P0Y--P1Y:M"
    )
    assert float(
        inst.group[0].stratifier[0].stratum[2].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[0].stratifier[0].stratum[2].valueCodeableConcept.coding[0].code
        == "P1Y--P5Y:F"
    )
    assert float(
        inst.group[0].stratifier[0].stratum[3].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[0].stratifier[0].stratum[3].valueCodeableConcept.coding[0].code
        == "P1Y--P5Y:M"
    )
    assert float(
        inst.group[0].stratifier[0].stratum[4].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[0].stratifier[0].stratum[4].valueCodeableConcept.coding[0].code
        == "P10Y--P15Y:F"
    )
    assert float(
        inst.group[0].stratifier[0].stratum[5].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[0].stratifier[0].stratum[5].valueCodeableConcept.coding[0].code
        == "P10Y--P15Y:M"
    )
    assert inst.group[1].code.coding[0].code == "QRPH_ADX_ART1_N"
    assert float(inst.group[1].measureScoreQuantity.value) == float(0)
    assert inst.group[1].stratifier[0].code.coding[0].code == "AGE_GROUP:SEX"
    assert float(
        inst.group[1].stratifier[0].stratum[0].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[1].stratifier[0].stratum[0].valueCodeableConcept.coding[0].code
        == "P0Y--P1Y:F"
    )
    assert float(
        inst.group[1].stratifier[0].stratum[1].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[1].stratifier[0].stratum[1].valueCodeableConcept.coding[0].code
        == "P0Y--P1Y:M"
    )
    assert float(
        inst.group[1].stratifier[0].stratum[2].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[1].stratifier[0].stratum[2].valueCodeableConcept.coding[0].code
        == "P1Y--P5Y:F"
    )
    assert float(
        inst.group[1].stratifier[0].stratum[3].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[1].stratifier[0].stratum[3].valueCodeableConcept.coding[0].code
        == "P1Y--P5Y:M"
    )
    assert float(
        inst.group[1].stratifier[0].stratum[4].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[1].stratifier[0].stratum[4].valueCodeableConcept.coding[0].code
        == "P10Y--P15Y:F"
    )
    assert float(
        inst.group[1].stratifier[0].stratum[5].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[1].stratifier[0].stratum[5].valueCodeableConcept.coding[0].code
        == "P10Y--P15Y:M"
    )
    assert inst.group[2].code.coding[0].code == "QRPH_ADX_ART1_N"
    assert float(inst.group[2].measureScoreQuantity.value) == float(0)
    assert (
        inst.group[2].stratifier[0].stratum[0].component[0].code.coding[0].code
        == "AGE_GROUP"
    )
    assert (
        inst.group[2]
        .stratifier[0]
        .stratum[0]
        .component[0]
        .valueCodeableConcept.coding[0]
        .code
        == "P0Y--P1Y"
    )
    assert (
        inst.group[2].stratifier[0].stratum[0].component[1].code.coding[0].code == "SEX"
    )
    assert (
        inst.group[2]
        .stratifier[0]
        .stratum[0]
        .component[1]
        .valueCodeableConcept.coding[0]
        .code
        == "F"
    )
    assert float(
        inst.group[2].stratifier[0].stratum[0].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[2].stratifier[0].stratum[1].component[0].code.coding[0].code
        == "AGE_GROUP"
    )
    assert (
        inst.group[2]
        .stratifier[0]
        .stratum[1]
        .component[0]
        .valueCodeableConcept.coding[0]
        .code
        == "P0Y--P1Y"
    )
    assert (
        inst.group[2].stratifier[0].stratum[1].component[1].code.coding[0].code == "SEX"
    )
    assert (
        inst.group[2]
        .stratifier[0]
        .stratum[1]
        .component[1]
        .valueCodeableConcept.coding[0]
        .code
        == "M"
    )
    assert float(
        inst.group[2].stratifier[0].stratum[1].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[2].stratifier[0].stratum[2].component[0].code.coding[0].code
        == "AGE_GROUP"
    )
    assert (
        inst.group[2]
        .stratifier[0]
        .stratum[2]
        .component[0]
        .valueCodeableConcept.coding[0]
        .code
        == "P1Y--P5Y"
    )
    assert (
        inst.group[2].stratifier[0].stratum[2].component[1].code.coding[0].code == "SEX"
    )
    assert (
        inst.group[2]
        .stratifier[0]
        .stratum[2]
        .component[1]
        .valueCodeableConcept.coding[0]
        .code
        == "F"
    )
    assert float(
        inst.group[2].stratifier[0].stratum[2].measureScoreQuantity.value
    ) == float(0)
    assert (
        inst.group[2].stratifier[0].stratum[3].component[0].code.coding[0].code
        == "AGE_GROUP"
    )
    assert (
        inst.group[2]
        .stratifier[0]
        .stratum[3]
        .component[0]
        .valueCodeableConcept.coding[0]
        .code
        == "P1Y--P5Y"
    )
    assert (
        inst.group[2].stratifier[0].stratum[3].component[1].code.coding[0].code == "SEX"
    )
    assert (
        inst.group[2]
        .stratifier[0]
        .stratum[3]
        .component[1]
        .valueCodeableConcept.coding[0]
        .code
        == "F"
    )
    assert float(
        inst.group[2].stratifier[0].stratum[3].measureScoreQuantity.value
    ) == float(0)
    assert inst.id == "hiv-indicators"
    assert inst.measure == "http://ohie.org/Measure/hiv-indicators"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2018-01-31")
    assert inst.period.start == fhirtypes.DateTime.validate("2018-01-01")
    assert inst.reporter.reference == "Organization/hl7"
    assert inst.status == "complete"
    assert inst.text.status == "generated"
    assert inst.type == "summary"


def test_measurereport_4(base_settings):
    """No. 4 tests collection for MeasureReport.
    Test File: measurereport-hiv-indicators.json
    """
    filename = base_settings["unittest_data_dir"] / "measurereport-hiv-indicators.json"
    inst = measurereport.MeasureReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MeasureReport" == inst.resource_type

    impl_measurereport_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MeasureReport" == data["resourceType"]

    inst2 = measurereport.MeasureReport(**data)
    impl_measurereport_4(inst2)


def impl_measurereport_5(inst):
    assert inst.contained[0].id == "reporter"
    assert inst.date == fhirtypes.DateTime.validate("2014-04-01")
    assert inst.group[0].id == "CMS146-group-1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].count == 500
    assert inst.group[0].population[1].code.coding[0].code == "numerator"
    assert inst.group[0].population[1].count == 200
    assert inst.group[0].population[2].code.coding[0].code == "denominator"
    assert inst.group[0].population[2].count == 500
    assert inst.group[0].population[3].code.coding[0].code == "denominator-exclusion"
    assert inst.group[0].population[3].count == 100
    assert inst.group[0].stratifier[0].code.text == "stratifier-ages-up-to-9"
    assert (
        inst.group[0].stratifier[0].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[0].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[1].count == 100
    assert (
        inst.group[0].stratifier[0].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[2].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[3].count == 50
    assert inst.group[0].stratifier[0].stratum[0].valueBoolean is True
    assert (
        inst.group[0].stratifier[0].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[0].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[1].count == 100
    assert (
        inst.group[0].stratifier[0].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[2].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[3].count == 50
    assert inst.group[0].stratifier[0].stratum[1].valueBoolean is False
    assert inst.group[0].stratifier[1].code.text == "stratifier-ages-10-plus"
    assert (
        inst.group[0].stratifier[1].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[0].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[1].count == 100
    assert (
        inst.group[0].stratifier[1].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[2].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[3].count == 50
    assert inst.group[0].stratifier[1].stratum[0].valueBoolean is True
    assert (
        inst.group[0].stratifier[1].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[0].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[1].count == 100
    assert (
        inst.group[0].stratifier[1].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[2].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[3].count == 50
    assert inst.group[0].stratifier[1].stratum[1].valueBoolean is False
    assert inst.group[0].stratifier[2].code.text == "stratifier-gender"
    assert (
        inst.group[0].stratifier[2].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[0].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[1].count == 100
    assert (
        inst.group[0].stratifier[2].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[2].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[3].count == 50
    assert inst.group[0].stratifier[2].stratum[0].valueCodeableConcept.text == "male"
    assert (
        inst.group[0].stratifier[2].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[0].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[1].count == 100
    assert (
        inst.group[0].stratifier[2].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[2].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[3].count == 50
    assert inst.group[0].stratifier[2].stratum[1].valueCodeableConcept.text == "female"
    assert (
        inst.group[0].stratifier[2].stratum[2].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[0].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[1].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[2].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[3].count == 0
    assert inst.group[0].stratifier[2].stratum[2].valueCodeableConcept.text == "other"
    assert (
        inst.group[0].stratifier[2].stratum[3].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[0].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[1].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[2].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[3].count == 0
    assert inst.group[0].stratifier[2].stratum[3].valueCodeableConcept.text == "unknown"
    assert inst.id == "measurereport-cms146-cat3-example"
    assert inst.identifier[0].value == "measurereport-cms146-cat3-example-2017-03-13"
    assert inst.measure == "http://example.org/fhir/Measure/CMS146"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2014-03-31")
    assert inst.period.start == fhirtypes.DateTime.validate("2014-01-01")
    assert inst.reporter.reference == "#reporter"
    assert inst.status == "complete"
    assert inst.text.status == "generated"
    assert inst.type == "summary"


def test_measurereport_5(base_settings):
    """No. 5 tests collection for MeasureReport.
    Test File: measurereport-cms146-cat3-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "measurereport-cms146-cat3-example.json"
    )
    inst = measurereport.MeasureReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MeasureReport" == inst.resource_type

    impl_measurereport_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MeasureReport" == data["resourceType"]

    inst2 = measurereport.MeasureReport(**data)
    impl_measurereport_5(inst2)
