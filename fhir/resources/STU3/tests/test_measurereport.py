# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MeasureReport
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import measurereport


def impl_measurereport_1(inst):
    assert inst.contained[0].id == "reporter"
    assert inst.evaluatedResources.reference == "Bundle/456"
    assert inst.group[0].identifier.value == "CMS146-group-1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].count == 1
    assert inst.group[0].population[1].code.coding[0].code == "numerator"
    assert inst.group[0].population[1].count == 1
    assert inst.group[0].population[2].code.coding[0].code == "denominator"
    assert inst.group[0].population[2].count == 1
    assert inst.group[0].population[3].code.coding[0].code == "denominator-exclusion"
    assert inst.group[0].population[3].count == 0
    assert inst.group[0].stratifier[0].identifier.value == "stratifier-ages-up-to-9"
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
    assert inst.group[0].stratifier[0].stratum[0].value == "true"
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
    assert inst.group[0].stratifier[0].stratum[1].value == "false"
    assert inst.group[0].stratifier[1].identifier.value == "stratifier-ages-10-plus"
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
    assert inst.group[0].stratifier[1].stratum[0].value == "true"
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
    assert inst.group[0].stratifier[1].stratum[1].value == "false"
    assert inst.group[0].stratifier[2].identifier.value == "stratifier-gender"
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
    assert inst.group[0].stratifier[2].stratum[0].value == "male"
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
    assert inst.group[0].stratifier[2].stratum[1].value == "female"
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
    assert inst.group[0].stratifier[2].stratum[2].value == "other"
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
    assert inst.group[0].stratifier[2].stratum[3].value == "unknown"
    assert inst.id == "measurereport-cms146-cat1-example"
    assert inst.identifier.value == "measurereport-cms146-cat1-example-2017-03-13"
    assert inst.measure.reference == "Measure/CMS146"
    assert inst.patient.reference == "Patient/123"
    assert inst.period.end == fhirtypes.DateTime.validate("2014-03-31")
    assert inst.period.start == fhirtypes.DateTime.validate("2014-01-01")
    assert inst.reportingOrganization.reference == "#reporter"
    assert inst.status == "complete"
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
    assert inst.group[0].identifier.value == "CMS146-group-1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].count == 500
    assert (
        inst.group[0].population[0].patients.reference
        == "List/CMS146-initial-population"
    )
    assert inst.group[0].population[1].code.coding[0].code == "numerator"
    assert inst.group[0].population[1].count == 200
    assert inst.group[0].population[1].patients.reference == "List/CMS146-numerator"
    assert inst.group[0].population[2].code.coding[0].code == "denominator"
    assert inst.group[0].population[2].count == 500
    assert inst.group[0].population[2].patients.reference == "List/CMS146-denominator"
    assert inst.group[0].population[3].code.coding[0].code == "denominator-exclusion"
    assert inst.group[0].population[3].count == 100
    assert (
        inst.group[0].population[3].patients.reference
        == "List/CMS146-denominator-exclusions"
    )
    assert inst.group[0].stratifier[0].identifier.value == "stratifier-ages-up-to-9"
    assert (
        inst.group[0].stratifier[0].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[0].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[0].population[0].patients.reference
        == "List/CMS146-stratifier-ages-up-to-9-true-initial-population"
    )
    assert (
        inst.group[0].stratifier[0].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[1].count == 100
    assert (
        inst.group[0].stratifier[0].stratum[0].population[1].patients.reference
        == "List/CMS146-stratifier-ages-up-to-9-true-numerator"
    )
    assert (
        inst.group[0].stratifier[0].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[2].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[0].population[2].patients.reference
        == "List/CMS146-stratifier-ages-up-to-9-true-denominator"
    )
    assert (
        inst.group[0].stratifier[0].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[0].stratum[0].population[3].count == 50
    assert inst.group[0].stratifier[0].stratum[0].population[3].patients.reference == (
        "List/CMS146-stratifier-ages-up-to-9-true-denominator-" "exclusions"
    )
    assert inst.group[0].stratifier[0].stratum[0].value == "true"
    assert (
        inst.group[0].stratifier[0].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[0].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[1].population[0].patients.reference
        == "List/CMS146-stratifier-ages-up-to-9-false-initial-population"
    )
    assert (
        inst.group[0].stratifier[0].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[1].count == 100
    assert (
        inst.group[0].stratifier[0].stratum[1].population[1].patients.reference
        == "List/CMS146-stratifier-ages-up-to-9-false-numerator"
    )
    assert (
        inst.group[0].stratifier[0].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[2].count == 250
    assert (
        inst.group[0].stratifier[0].stratum[1].population[2].patients.reference
        == "List/CMS146-stratifier-ages-up-to-9-false-denominator"
    )
    assert (
        inst.group[0].stratifier[0].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[0].stratum[1].population[3].count == 50
    assert inst.group[0].stratifier[0].stratum[1].population[3].patients.reference == (
        "List/CMS146-stratifier-ages-up-to-9-false-denominator-" "exclusions"
    )
    assert inst.group[0].stratifier[0].stratum[1].value == "false"
    assert inst.group[0].stratifier[1].identifier.value == "stratifier-ages-10-plus"
    assert (
        inst.group[0].stratifier[1].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[0].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[0].population[0].patients.reference
        == "List/CMS146-stratifier-ages-10-plus-true-initial-population"
    )
    assert (
        inst.group[0].stratifier[1].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[1].count == 100
    assert (
        inst.group[0].stratifier[1].stratum[0].population[1].patients.reference
        == "List/CMS146-stratifier-ages-10-plus-true-numerator"
    )
    assert (
        inst.group[0].stratifier[1].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[2].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[0].population[2].patients.reference
        == "List/CMS146-stratifier-ages-10-plus-true-denominator"
    )
    assert (
        inst.group[0].stratifier[1].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[1].stratum[0].population[3].count == 50
    assert inst.group[0].stratifier[1].stratum[0].population[3].patients.reference == (
        "List/CMS146-stratifier-ages-10-plus-true-denominator-" "exclusions"
    )
    assert inst.group[0].stratifier[1].stratum[0].value == "true"
    assert (
        inst.group[0].stratifier[1].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[0].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[1].population[0].patients.reference
        == "List/CMS146-stratifier-ages-10-plus-false-initial-population"
    )
    assert (
        inst.group[0].stratifier[1].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[1].count == 100
    assert (
        inst.group[0].stratifier[1].stratum[1].population[1].patients.reference
        == "List/CMS146-stratifier-ages-10-plus-false-numerator"
    )
    assert (
        inst.group[0].stratifier[1].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[2].count == 250
    assert (
        inst.group[0].stratifier[1].stratum[1].population[2].patients.reference
        == "List/CMS146-stratifier-ages-10-plus-false-denominator"
    )
    assert (
        inst.group[0].stratifier[1].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[1].stratum[1].population[3].count == 50
    assert inst.group[0].stratifier[1].stratum[1].population[3].patients.reference == (
        "List/CMS146-stratifier-ages-10-plus-false-denominator-" "exclusions"
    )
    assert inst.group[0].stratifier[1].stratum[1].value == "false"
    assert inst.group[0].stratifier[2].identifier.value == "stratifier-gender"
    assert (
        inst.group[0].stratifier[2].stratum[0].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[0].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[0].population[0].patients.reference
        == "List/CMS146-stratifier-gender-male-initial-population"
    )
    assert (
        inst.group[0].stratifier[2].stratum[0].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[1].count == 100
    assert (
        inst.group[0].stratifier[2].stratum[0].population[1].patients.reference
        == "List/CMS146-stratifier-gender-male-numerator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[0].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[2].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[0].population[2].patients.reference
        == "List/CMS146-stratifier-gender-male-denominator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[0].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[0].population[3].count == 50
    assert (
        inst.group[0].stratifier[2].stratum[0].population[3].patients.reference
        == "List/CMS146-stratifier-gender-male-denominator-exclusions"
    )
    assert inst.group[0].stratifier[2].stratum[0].value == "male"
    assert (
        inst.group[0].stratifier[2].stratum[1].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[0].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[1].population[0].patients.reference
        == "List/CMS146-stratifier-gender-female-initial-population"
    )
    assert (
        inst.group[0].stratifier[2].stratum[1].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[1].count == 100
    assert (
        inst.group[0].stratifier[2].stratum[1].population[1].patients.reference
        == "List/CMS146-stratifier-gender-female-numerator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[1].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[2].count == 250
    assert (
        inst.group[0].stratifier[2].stratum[1].population[2].patients.reference
        == "List/CMS146-stratifier-gender-female-denominator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[1].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[1].population[3].count == 50
    assert (
        inst.group[0].stratifier[2].stratum[1].population[3].patients.reference
        == "List/CMS146-stratifier-gender-female-denominator-exclusions"
    )
    assert inst.group[0].stratifier[2].stratum[1].value == "female"
    assert (
        inst.group[0].stratifier[2].stratum[2].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[0].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[0].patients.reference
        == "List/CMS146-stratifier-gender-other-initial-population"
    )
    assert (
        inst.group[0].stratifier[2].stratum[2].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[1].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[1].patients.reference
        == "List/CMS146-stratifier-gender-other-numerator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[2].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[2].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[2].patients.reference
        == "List/CMS146-stratifier-gender-other-denominator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[2].population[3].code.coding[0].code
        == "denominator-exclusion"
    )
    assert inst.group[0].stratifier[2].stratum[2].population[3].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[2].population[3].patients.reference
        == "List/CMS146-stratifier-gender-other-denominator-exclusions"
    )
    assert inst.group[0].stratifier[2].stratum[2].value == "other"
    assert (
        inst.group[0].stratifier[2].stratum[3].population[0].code.coding[0].code
        == "initial-population"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[0].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[0].patients.reference
        == "List/CMS146-stratifier-gender-unknown-initial-population"
    )
    assert (
        inst.group[0].stratifier[2].stratum[3].population[1].code.coding[0].code
        == "numerator"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[1].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[1].patients.reference
        == "List/CMS146-stratifier-gender-unknown-numerator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[3].population[2].code.coding[0].code
        == "denominator"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[2].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[2].patients.reference
        == "List/CMS146-stratifier-gender-unknown-denominator"
    )
    assert (
        inst.group[0].stratifier[2].stratum[3].population[3].code.coding[0].code
        == "denominator-exclusions"
    )
    assert inst.group[0].stratifier[2].stratum[3].population[3].count == 0
    assert (
        inst.group[0].stratifier[2].stratum[3].population[3].patients.reference
        == "List/CMS146-stratifier-gender-unknown-denominator-exclusions"
    )
    assert inst.group[0].stratifier[2].stratum[3].value == "unknown"
    assert inst.id == "measurereport-cms146-cat2-example"
    assert inst.identifier.value == "measurereport-cms146-cat2-example-2017-03-13"
    assert inst.measure.reference == "Measure/CMS146"
    assert inst.period.end == fhirtypes.DateTime.validate("2014-03-31")
    assert inst.period.start == fhirtypes.DateTime.validate("2014-01-01")
    assert inst.reportingOrganization.reference == "#reporter"
    assert inst.status == "complete"
    assert inst.text.status == "generated"
    assert inst.type == "patient-list"


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
    assert inst.contained[0].id == "reporter"
    assert inst.group[0].identifier.value == "CMS146-group-1"
    assert inst.group[0].population[0].code.coding[0].code == "initial-population"
    assert inst.group[0].population[0].count == 500
    assert inst.group[0].population[1].code.coding[0].code == "numerator"
    assert inst.group[0].population[1].count == 200
    assert inst.group[0].population[2].code.coding[0].code == "denominator"
    assert inst.group[0].population[2].count == 500
    assert inst.group[0].population[3].code.coding[0].code == "denominator-exclusion"
    assert inst.group[0].population[3].count == 100
    assert inst.group[0].stratifier[0].identifier.value == "stratifier-ages-up-to-9"
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
    assert inst.group[0].stratifier[0].stratum[0].value == "true"
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
    assert inst.group[0].stratifier[0].stratum[1].value == "false"
    assert inst.group[0].stratifier[1].identifier.value == "stratifier-ages-10-plus"
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
    assert inst.group[0].stratifier[1].stratum[0].value == "true"
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
    assert inst.group[0].stratifier[1].stratum[1].value == "false"
    assert inst.group[0].stratifier[2].identifier.value == "stratifier-gender"
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
    assert inst.group[0].stratifier[2].stratum[0].value == "male"
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
    assert inst.group[0].stratifier[2].stratum[1].value == "female"
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
    assert inst.group[0].stratifier[2].stratum[2].value == "other"
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
    assert inst.group[0].stratifier[2].stratum[3].value == "unknown"
    assert inst.id == "measurereport-cms146-cat3-example"
    assert inst.identifier.value == "measurereport-cms146-cat3-example-2017-03-13"
    assert inst.measure.reference == "Measure/CMS146"
    assert inst.period.end == fhirtypes.DateTime.validate("2014-03-31")
    assert inst.period.start == fhirtypes.DateTime.validate("2014-01-01")
    assert inst.reportingOrganization.reference == "#reporter"
    assert inst.status == "complete"
    assert inst.text.status == "generated"
    assert inst.type == "summary"


def test_measurereport_3(base_settings):
    """No. 3 tests collection for MeasureReport.
    Test File: measurereport-cms146-cat3-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "measurereport-cms146-cat3-example.json"
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
