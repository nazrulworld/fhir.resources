# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EligibilityRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import eligibilityrequest


def impl_eligibilityrequest_1(inst):
    assert inst.benefitCategory.coding[0].code == "medical"
    assert (
        inst.benefitCategory.coding[0].system == "http://hl7.org/fhir/benefit-category"
    )
    assert inst.benefitSubCategory.coding[0].code == "69"
    assert inst.benefitSubCategory.coding[0].display == "Maternity"
    assert (
        inst.benefitSubCategory.coding[0].system
        == "http://hl7.org/fhir/benefit-subcategory"
    )
    assert inst.businessArrangement == "NB8742"
    assert inst.coverage.reference == "Coverage/9876B1"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.enterer.identifier.system == "http://happyvalleyclinic.com/staff"
    assert inst.enterer.identifier.value == "14"
    assert inst.facility.identifier.system == "http://statecliniclicensor.com/clinicid"
    assert inst.facility.identifier.value == "G35B9"
    assert inst.id == "52346"
    assert inst.identifier[0].system == "http://happyvalley.com/elegibilityrequest"
    assert inst.identifier[0].value == "52346"
    assert inst.insurer.reference == "Organization/2"
    assert inst.organization.reference == "Organization/1"
    assert inst.patient.reference == "Patient/pat1"
    assert inst.priority.coding[0].code == "normal"
    assert inst.provider.identifier.system == "http://happyvalleyclinic.com/staff"
    assert inst.provider.identifier.value == "18"
    assert inst.servicedDate == fhirtypes.Date.validate("2014-09-17")
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the EligibilityRequest</div>"
    )
    assert inst.text.status == "generated"


def test_eligibilityrequest_1(base_settings):
    """No. 1 tests collection for EligibilityRequest.
    Test File: eligibilityrequest-example-2.json
    """
    filename = base_settings["unittest_data_dir"] / "eligibilityrequest-example-2.json"
    inst = eligibilityrequest.EligibilityRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EligibilityRequest" == inst.resource_type

    impl_eligibilityrequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EligibilityRequest" == data["resourceType"]

    inst2 = eligibilityrequest.EligibilityRequest(**data)
    impl_eligibilityrequest_1(inst2)


def impl_eligibilityrequest_2(inst):
    assert inst.coverage.reference == "Coverage/9876B1"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "52345"
    assert inst.identifier[0].system == "http://happyvalley.com/elegibilityrequest"
    assert inst.identifier[0].value == "52345"
    assert inst.insurer.reference == "Organization/2"
    assert inst.organization.reference == "Organization/1"
    assert inst.patient.reference == "Patient/pat1"
    assert inst.priority.coding[0].code == "normal"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the EligibilityRequest</div>"
    )
    assert inst.text.status == "generated"


def test_eligibilityrequest_2(base_settings):
    """No. 2 tests collection for EligibilityRequest.
    Test File: eligibilityrequest-example.json
    """
    filename = base_settings["unittest_data_dir"] / "eligibilityrequest-example.json"
    inst = eligibilityrequest.EligibilityRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EligibilityRequest" == inst.resource_type

    impl_eligibilityrequest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EligibilityRequest" == data["resourceType"]

    inst2 = eligibilityrequest.EligibilityRequest(**data)
    impl_eligibilityrequest_2(inst2)
