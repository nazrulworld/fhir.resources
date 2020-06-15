# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MeasureReport
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import measurereport


def impl_measurereport_1(inst):
    assert inst.contained[0].id == "reporter"
    assert inst.date == fhirtypes.DateTime.validate("2014-04-01T11:15:33+10:00")
    assert inst.evaluatedResource[0].reference == "Condition/123"
    assert inst.group[0].id == "CMS146-group-1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].count == 1
    assert inst.group[0].population[1].code.coding[0].code == "numerator"
    assert inst.group[0].population[1].count == 1
    assert inst.group[0].population[2].code.coding[0].code == "denominator"
    assert inst.group[0].population[2].count == 1
    assert inst.group[0].population[3].code.coding[0].code == "denominator-exclusion"
    assert inst.group[0].population[3].count == 0
    assert inst.group[0].stratifier[0].code[0].text == "stratifier-ages-up-to-9"
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
    assert inst.group[0].stratifier[0].stratum[0].value.text == "true"
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
    assert inst.group[0].stratifier[0].stratum[1].value.text == "false"
    assert inst.group[0].stratifier[1].code[0].text == "stratifier-ages-10-plus"
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
    assert inst.group[0].stratifier[1].stratum[0].value.text == "true"
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
    assert inst.group[0].stratifier[1].stratum[1].value.text == "false"
    assert inst.group[0].stratifier[2].code[0].text == "stratifier-gender"
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
    assert inst.group[0].stratifier[2].stratum[0].value.text == "male"
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
    assert inst.group[0].stratifier[2].stratum[1].value.text == "female"
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
    assert inst.group[0].stratifier[2].stratum[2].value.text == "other"
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
    assert inst.group[0].stratifier[2].stratum[3].value.text == "unknown"
    assert inst.id == "measurereport-cms146-cat1-example"
    assert inst.identifier[0].value == "measurereport-cms146-cat1-example-2017-03-13"
    assert inst.measure == "Measure/CMS146"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2014-03-31T11:15:33+10:00")
    assert inst.period.start == fhirtypes.DateTime.validate("2014-01-01T11:15:33+10:00")
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
    assert inst.contained[0].id == "reporter"
    assert inst.date == fhirtypes.DateTime.validate("2014-04-01T11:15:33+10:00")
    assert inst.group[0].id == "CMS146-group-1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].count == 500
    assert (
        inst.group[0].population[0].subjectResults.reference
        == "List/CMS146-initial-population"
    )
    assert inst.group[0].population[1].code.coding[0].code == "numerator"
    assert inst.group[0].population[1].count == 200
    assert (
        inst.group[0].population[1].subjectResults.reference == "List/CMS146-numerator"
    )
    assert inst.group[0].population[2].code.coding[0].code == "denominator"
    assert inst.group[0].population[2].count == 500
    assert (
        inst.group[0].population[2].subjectResults.reference
        == "List/CMS146-denominator"
    )
    assert inst.group[0].population[3].code.coding[0].code == "denominator-exclusion"
    assert inst.group[0].population[3].count == 100
    assert (
        inst.group[0].population[3].subjectResults.reference
        == "List/CMS146-denominator-exclusions"
    )
    assert inst.group[0].stratifier[0].code[0].text == "stratifier-ages-up-to-9"
    assert (
        inst.group[0].stratifier[0].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[0].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[0].population[0].subjectResults.reference
        == "List/CMS146-stratifier-ages-up-to-9-true-initial-population"
    )
    assert (
        inst.group[0].stratifier[0].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[1].count == 100
    assert (
        inst.group[0].stratifier[0].stratum[0].population[1].subjectResults.reference
        == "List/CMS146-stratifier-ages-up-to-9-true-numerator"
    )
    assert (
        inst.group[0].stratifier[0].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[2].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[0].population[2].subjectResults.reference
        == "List/CMS146-stratifier-ages-up-to-9-true-denominator"
    )
    assert (
        inst.group[0].stratifier[0].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[3].count == 50
    assert inst.group[0].stratifier[0].stratum[0].population[
        3
    ].subjectResults.reference == (
        "List/CMS146-stratifier-ages-up-to-9-true-denominator-" "exclusions"
    )
    assert inst.group[0].stratifier[0].stratum[0].value.text == "true"
    assert (
        inst.group[0].stratifier[0].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[0].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[1].population[0].subjectResults.reference
        == "List/CMS146-stratifier-ages-up-to-9-false-initial-population"
    )
    assert (
        inst.group[0].stratifier[0].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[1].count == 100
    assert (
        inst.group[0].stratifier[0].stratum[1].population[1].subjectResults.reference
        == "List/CMS146-stratifier-ages-up-to-9-false-numerator"
    )
    assert (
        inst.group[0].stratifier[0].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[2].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[1].population[2].subjectResults.reference
        == "List/CMS146-stratifier-ages-up-to-9-false-denominator"
    )
    assert (
        inst.group[0].stratifier[0].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[3].count == 50
    assert inst.group[0].stratifier[0].stratum[1].population[
        3
    ].subjectResults.reference == (
        "List/CMS146-stratifier-ages-up-to-9-false-denominator-" "exclusions"
    )
    assert inst.group[0].stratifier[0].stratum[1].value.text == "false"
    assert inst.group[0].stratifier[1].code[0].text == "stratifier-ages-10-plus"
    assert (
        inst.group[0].stratifier[1].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[0].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[0].population[0].subjectResults.reference
        == "List/CMS146-stratifier-ages-10-plus-true-initial-population"
    )
    assert (
        inst.group[0].stratifier[1].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[1].count == 100
    assert (
        inst.group[0].stratifier[1].stratum[0].population[1].subjectResults.reference
        == "List/CMS146-stratifier-ages-10-plus-true-numerator"
    )
    assert (
        inst.group[0].stratifier[1].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[2].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[0].population[2].subjectResults.reference
        == "List/CMS146-stratifier-ages-10-plus-true-denominator"
    )
    assert (
        inst.group[0].stratifier[1].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[3].count == 50
    assert inst.group[0].stratifier[1].stratum[0].population[
        3
    ].subjectResults.reference == (
        "List/CMS146-stratifier-ages-10-plus-true-denominator-" "exclusions"
    )
    assert inst.group[0].stratifier[1].stratum[0].value.text == "true"
    assert (
        inst.group[0].stratifier[1].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[0].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[1].population[0].subjectResults.reference
        == "List/CMS146-stratifier-ages-10-plus-false-initial-population"
    )
    assert (
        inst.group[0].stratifier[1].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[1].count == 100
    assert (
        inst.group[0].stratifier[1].stratum[1].population[1].subjectResults.reference
        == "List/CMS146-stratifier-ages-10-plus-false-numerator"
    )
    assert (
        inst.group[0].stratifier[1].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[2].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[1].population[2].subjectResults.reference
        == "List/CMS146-stratifier-ages-10-plus-false-denominator"
    )
    assert (
        inst.group[0].stratifier[1].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[3].count == 50
    assert inst.group[0].stratifier[1].stratum[1].population[
        3
    ].subjectResults.reference == (
        "List/CMS146-stratifier-ages-10-plus-false-denominator-" "exclusions"
    )
    assert inst.group[0].stratifier[1].stratum[1].value.text == "false"
    assert inst.group[0].stratifier[2].code[0].text == "stratifier-gender"
    assert (
        inst.group[0].stratifier[2].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[0].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[0].population[0].subjectResults.reference
        == "List/CMS146-stratifier-gender-male-initial-population"
    )
    assert (
        inst.group[0].stratifier[2].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[1].count == 100
    assert (
        inst.group[0].stratifier[2].stratum[0].population[1].subjectResults.reference
        == "List/CMS146-stratifier-gender-male-numerator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[2].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[0].population[2].subjectResults.reference
        == "List/CMS146-stratifier-gender-male-denominator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[3].count == 50
    assert (
        inst.group[0].stratifier[2].stratum[0].population[3].subjectResults.reference
        == "List/CMS146-stratifier-gender-male-denominator-exclusions"
    )
    assert inst.group[0].stratifier[2].stratum[0].value.text == "male"
    assert (
        inst.group[0].stratifier[2].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[0].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[1].population[0].subjectResults.reference
        == "List/CMS146-stratifier-gender-female-initial-population"
    )
    assert (
        inst.group[0].stratifier[2].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[1].count == 100
    assert (
        inst.group[0].stratifier[2].stratum[1].population[1].subjectResults.reference
        == "List/CMS146-stratifier-gender-female-numerator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[2].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[1].population[2].subjectResults.reference
        == "List/CMS146-stratifier-gender-female-denominator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[3].count == 50
    assert (
        inst.group[0].stratifier[2].stratum[1].population[3].subjectResults.reference
        == "List/CMS146-stratifier-gender-female-denominator-exclusions"
    )
    assert inst.group[0].stratifier[2].stratum[1].value.text == "female"
    assert (
        inst.group[0].stratifier[2].stratum[2].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[0].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[0].subjectResults.reference
        == "List/CMS146-stratifier-gender-other-initial-population"
    )
    assert (
        inst.group[0].stratifier[2].stratum[2].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[1].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[1].subjectResults.reference
        == "List/CMS146-stratifier-gender-other-numerator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[2].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[2].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[2].subjectResults.reference
        == "List/CMS146-stratifier-gender-other-denominator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[2].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[3].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[3].subjectResults.reference
        == "List/CMS146-stratifier-gender-other-denominator-exclusions"
    )
    assert inst.group[0].stratifier[2].stratum[2].value.text == "other"
    assert (
        inst.group[0].stratifier[2].stratum[3].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[0].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[0].subjectResults.reference
        == "List/CMS146-stratifier-gender-unknown-initial-population"
    )
    assert (
        inst.group[0].stratifier[2].stratum[3].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[1].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[1].subjectResults.reference
        == "List/CMS146-stratifier-gender-unknown-numerator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[3].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[2].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[2].subjectResults.reference
        == "List/CMS146-stratifier-gender-unknown-denominator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[3].population[3].code.coding[0].code
        == "denominator-exclusions"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[3].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[3].subjectResults.reference
        == "List/CMS146-stratifier-gender-unknown-denominator-exclusions"
    )
    assert inst.group[0].stratifier[2].stratum[3].value.text == "unknown"
    assert inst.id == "measurereport-cms146-cat2-example"
    assert inst.identifier[0].value == "measurereport-cms146-cat2-example-2017-03-13"
    assert inst.measure == "Measure/CMS146"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2014-03-31T11:15:33+10:00")
    assert inst.period.start == fhirtypes.DateTime.validate("2014-01-01T11:15:33+10:00")
    assert inst.reporter.reference == "#reporter"
    assert inst.status == "complete"
    assert inst.text.status == "generated"
    assert inst.type == "subject-list"


def test_measurereport_2(base_settings):
    """No. 2 tests collection for MeasureReport.
    Test File: measurereport-cms146-cat2-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "measurereport-cms146-cat2-example.json"
    )
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
    assert inst.group[0].code.coding[0].code == "QRPH_ADX_ART1_N"
    assert float(inst.group[0].measureScore.value) == float(0)
    assert inst.group[0].stratifier[0].code[0].coding[0].code == "AGE_GROUP:SEX"
    assert float(inst.group[0].stratifier[0].stratum[0].measureScore.value) == float(0)
    assert inst.group[0].stratifier[0].stratum[0].value.coding[0].code == "P0Y--P1Y:F"
    assert float(inst.group[0].stratifier[0].stratum[1].measureScore.value) == float(0)
    assert inst.group[0].stratifier[0].stratum[1].value.coding[0].code == "P0Y--P1Y:M"
    assert float(inst.group[0].stratifier[0].stratum[2].measureScore.value) == float(0)
    assert inst.group[0].stratifier[0].stratum[2].value.coding[0].code == "P1Y--P5Y:F"
    assert float(inst.group[0].stratifier[0].stratum[3].measureScore.value) == float(0)
    assert inst.group[0].stratifier[0].stratum[3].value.coding[0].code == "P1Y--P5Y:M"
    assert float(inst.group[0].stratifier[0].stratum[4].measureScore.value) == float(0)
    assert inst.group[0].stratifier[0].stratum[4].value.coding[0].code == "P10Y--P15Y:F"
    assert float(inst.group[0].stratifier[0].stratum[5].measureScore.value) == float(0)
    assert inst.group[0].stratifier[0].stratum[5].value.coding[0].code == "P10Y--P15Y:M"
    assert inst.group[1].code.coding[0].code == "QRPH_ADX_ART1_N"
    assert float(inst.group[1].measureScore.value) == float(0)
    assert inst.group[1].stratifier[0].code[0].coding[0].code == "AGE_GROUP:SEX"
    assert float(inst.group[1].stratifier[0].stratum[0].measureScore.value) == float(0)
    assert inst.group[1].stratifier[0].stratum[0].value.coding[0].code == "P0Y--P1Y:F"
    assert float(inst.group[1].stratifier[0].stratum[1].measureScore.value) == float(0)
    assert inst.group[1].stratifier[0].stratum[1].value.coding[0].code == "P0Y--P1Y:M"
    assert float(inst.group[1].stratifier[0].stratum[2].measureScore.value) == float(0)
    assert inst.group[1].stratifier[0].stratum[2].value.coding[0].code == "P1Y--P5Y:F"
    assert float(inst.group[1].stratifier[0].stratum[3].measureScore.value) == float(0)
    assert inst.group[1].stratifier[0].stratum[3].value.coding[0].code == "P1Y--P5Y:M"
    assert float(inst.group[1].stratifier[0].stratum[4].measureScore.value) == float(0)
    assert inst.group[1].stratifier[0].stratum[4].value.coding[0].code == "P10Y--P15Y:F"
    assert float(inst.group[1].stratifier[0].stratum[5].measureScore.value) == float(0)
    assert inst.group[1].stratifier[0].stratum[5].value.coding[0].code == "P10Y--P15Y:M"
    assert inst.group[2].code.coding[0].code == "QRPH_ADX_ART1_N"
    assert float(inst.group[2].measureScore.value) == float(0)
    assert inst.group[2].stratifier[0].code[0].coding[0].code == "AGE_GROUP"
    assert inst.group[2].stratifier[0].code[1].coding[0].code == "SEX"
    assert (
        inst.group[2].stratifier[0].stratum[0].component[0].code.coding[0].code
        == "AGE_GROUP"
    )
    assert (
        inst.group[2].stratifier[0].stratum[0].component[0].value.coding[0].code
        == "P0Y--P1Y"
    )
    assert (
        inst.group[2].stratifier[0].stratum[0].component[1].code.coding[0].code == "SEX"
    )
    assert (
        inst.group[2].stratifier[0].stratum[0].component[1].value.coding[0].code == "F"
    )
    assert float(inst.group[2].stratifier[0].stratum[0].measureScore.value) == float(0)
    assert (
        inst.group[2].stratifier[0].stratum[1].component[0].code.coding[0].code
        == "AGE_GROUP"
    )
    assert (
        inst.group[2].stratifier[0].stratum[1].component[0].value.coding[0].code
        == "P0Y--P1Y"
    )
    assert (
        inst.group[2].stratifier[0].stratum[1].component[1].code.coding[0].code == "SEX"
    )
    assert (
        inst.group[2].stratifier[0].stratum[1].component[1].value.coding[0].code == "M"
    )
    assert float(inst.group[2].stratifier[0].stratum[1].measureScore.value) == float(0)
    assert (
        inst.group[2].stratifier[0].stratum[2].component[0].code.coding[0].code
        == "AGE_GROUP"
    )
    assert (
        inst.group[2].stratifier[0].stratum[2].component[0].value.coding[0].code
        == "P1Y--P5Y"
    )
    assert (
        inst.group[2].stratifier[0].stratum[2].component[1].code.coding[0].code == "SEX"
    )
    assert (
        inst.group[2].stratifier[0].stratum[2].component[1].value.coding[0].code == "F"
    )
    assert float(inst.group[2].stratifier[0].stratum[2].measureScore.value) == float(0)
    assert (
        inst.group[2].stratifier[0].stratum[3].component[0].code.coding[0].code
        == "AGE_GROUP"
    )
    assert (
        inst.group[2].stratifier[0].stratum[3].component[0].value.coding[0].code
        == "P1Y--P5Y"
    )
    assert (
        inst.group[2].stratifier[0].stratum[3].component[1].code.coding[0].code == "SEX"
    )
    assert (
        inst.group[2].stratifier[0].stratum[3].component[1].value.coding[0].code == "F"
    )
    assert float(inst.group[2].stratifier[0].stratum[3].measureScore.value) == float(0)
    assert inst.id == "hiv-indicators"
    assert inst.measure == "http://ohie.org/Measure/hiv-indicators"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2018-01-31T11:15:33+10:00")
    assert inst.period.start == fhirtypes.DateTime.validate("2018-01-01T11:15:33+10:00")
    assert inst.reporter.reference == "Organization/ZW01"
    assert inst.status == "complete"
    assert inst.text.status == "generated"
    assert inst.type == "summary"


def test_measurereport_3(base_settings):
    """No. 3 tests collection for MeasureReport.
    Test File: measurereport-hiv-indicators.json
    """
    filename = base_settings["unittest_data_dir"] / "measurereport-hiv-indicators.json"
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
    assert inst.contained[0].id == "reporter"
    assert inst.date == fhirtypes.DateTime.validate("2014-04-01T11:15:33+10:00")
    assert inst.group[0].id == "CMS146-group-1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].count == 500
    assert inst.group[0].population[1].code.coding[0].code == "numerator"
    assert inst.group[0].population[1].count == 200
    assert inst.group[0].population[2].code.coding[0].code == "denominator"
    assert inst.group[0].population[2].count == 500
    assert inst.group[0].population[3].code.coding[0].code == "denominator-exclusion"
    assert inst.group[0].population[3].count == 100
    assert inst.group[0].stratifier[0].code[0].text == "stratifier-ages-up-to-9"
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
    assert inst.group[0].stratifier[0].stratum[0].value.text == "true"
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
    assert inst.group[0].stratifier[0].stratum[1].value.text == "false"
    assert inst.group[0].stratifier[1].code[0].text == "stratifier-ages-10-plus"
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
    assert inst.group[0].stratifier[1].stratum[0].value.text == "true"
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
    assert inst.group[0].stratifier[1].stratum[1].value.text == "false"
    assert inst.group[0].stratifier[2].code[0].text == "stratifier-gender"
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
    assert inst.group[0].stratifier[2].stratum[0].value.text == "male"
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
    assert inst.group[0].stratifier[2].stratum[1].value.text == "female"
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
    assert inst.group[0].stratifier[2].stratum[2].value.text == "other"
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
    assert inst.group[0].stratifier[2].stratum[3].value.text == "unknown"
    assert inst.id == "measurereport-cms146-cat3-example"
    assert inst.identifier[0].value == "measurereport-cms146-cat3-example-2017-03-13"
    assert inst.measure == "Measure/CMS146"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2014-03-31T11:15:33+10:00")
    assert inst.period.start == fhirtypes.DateTime.validate("2014-01-01T11:15:33+10:00")
    assert inst.reporter.reference == "#reporter"
    assert inst.status == "complete"
    assert inst.text.status == "generated"
    assert inst.type == "summary"


def test_measurereport_4(base_settings):
    """No. 4 tests collection for MeasureReport.
    Test File: measurereport-cms146-cat3-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "measurereport-cms146-cat3-example.json"
    )
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
