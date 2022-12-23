# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import coverageeligibilityrequest


def impl_coverageeligibilityrequest_1(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "52345"
    assert (
        inst.identifier[0].system == "http://happyvalley.com/coverageelegibilityrequest"
    )
    assert inst.identifier[0].value == "52345"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurance[0].focal is True
    assert inst.insurer.reference == "Organization/2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/pat1"
    assert inst.priority.coding[0].code == "normal"
    assert inst.provider.reference == "Organization/1"
    assert inst.purpose[0] == "validation"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the CoverageEligibilityRequest</div>"
    )
    assert inst.text.status == "generated"


def test_coverageeligibilityrequest_1(base_settings):
    """No. 1 tests collection for CoverageEligibilityRequest.
    Test File: coverageeligibilityrequest-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "coverageeligibilityrequest-example.json"
    )
    inst = coverageeligibilityrequest.CoverageEligibilityRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CoverageEligibilityRequest" == inst.resource_type

    impl_coverageeligibilityrequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CoverageEligibilityRequest" == data["resourceType"]

    inst2 = coverageeligibilityrequest.CoverageEligibilityRequest(**data)
    impl_coverageeligibilityrequest_1(inst2)


def impl_coverageeligibilityrequest_2(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.enterer.identifier.system == "http://happyvalleyclinic.com/staff"
    assert inst.enterer.identifier.value == "14"
    assert inst.facility.identifier.system == "http://statecliniclicensor.com/clinicid"
    assert inst.facility.identifier.value == "G35B9"
    assert inst.id == "52346"
    assert (
        inst.identifier[0].system == "http://happyvalley.com/coverageelegibilityrequest"
    )
    assert inst.identifier[0].value == "52346"
    assert inst.insurance[0].businessArrangement == "NB8742"
    assert inst.insurance[0].coverage.reference == "Coverage/9876B1"
    assert inst.insurer.reference == "Organization/2"
    assert inst.item[0].category.coding[0].code == "69"
    assert inst.item[0].category.coding[0].display == "Maternity"
    assert (
        inst.item[0].category.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/ex-benefitcategory"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/pat1"
    assert inst.priority.coding[0].code == "normal"
    assert inst.provider.reference == "Organization/1"
    assert inst.purpose[0] == "validation"
    assert inst.purpose[1] == "benefits"
    assert inst.servicedDate == fhirtypes.Date.validate("2014-09-17")
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the CoverageEligibilityRequest</div>"
    )
    assert inst.text.status == "generated"


def test_coverageeligibilityrequest_2(base_settings):
    """No. 2 tests collection for CoverageEligibilityRequest.
    Test File: coverageeligibilityrequest-example-2.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "coverageeligibilityrequest-example-2.json"
    )
    inst = coverageeligibilityrequest.CoverageEligibilityRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CoverageEligibilityRequest" == inst.resource_type

    impl_coverageeligibilityrequest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CoverageEligibilityRequest" == data["resourceType"]

    inst2 = coverageeligibilityrequest.CoverageEligibilityRequest(**data)
    impl_coverageeligibilityrequest_2(inst2)
