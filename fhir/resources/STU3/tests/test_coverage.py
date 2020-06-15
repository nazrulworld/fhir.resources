# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coverage
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import coverage


def impl_coverage_1(inst):
    assert inst.beneficiary.reference == "Patient/5"
    assert inst.contract[0].reference == "Contract/563818"
    assert inst.dependent == "1"
    assert inst.grouping.group == "WESTAIR"
    assert inst.grouping.groupDisplay == "Western Airlines"
    assert inst.grouping.plan == "WESTAIR"
    assert inst.grouping.planDisplay == "Western Airlines"
    assert inst.grouping.subPlan == "D15C9"
    assert inst.grouping.subPlanDisplay == "Platinum"
    assert inst.id == "7546D"
    assert inst.identifier[0].system == "http://xyz.com/codes/identifier"
    assert inst.identifier[0].value == "AB98761"
    assert inst.network == "5"
    assert inst.order == 2
    assert inst.payor[0].reference == "Organization/2"
    assert inst.period.end == fhirtypes.DateTime.validate("2012-03-17")
    assert inst.period.start == fhirtypes.DateTime.validate("2011-03-17")
    assert inst.relationship.coding[0].code == "self"
    assert inst.status == "active"
    assert inst.subscriber.reference == "Patient/5"
    assert inst.subscriberId == "AB9876"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the coverage</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "EHCPOL"
    assert inst.type.coding[0].display == "extended healthcare"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/v3/ActCode"


def test_coverage_1(base_settings):
    """No. 1 tests collection for Coverage.
    Test File: coverage-example-2.json
    """
    filename = base_settings["unittest_data_dir"] / "coverage-example-2.json"
    inst = coverage.Coverage.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Coverage" == inst.resource_type

    impl_coverage_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Coverage" == data["resourceType"]

    inst2 = coverage.Coverage(**data)
    impl_coverage_1(inst2)


def impl_coverage_2(inst):
    assert inst.beneficiary.reference == "Patient/5"
    assert inst.id == "SP1234"
    assert inst.identifier[0].system == "http://hospitalx.com/selfpayagreement"
    assert inst.identifier[0].value == "SP12345678"
    assert inst.payor[0].reference == "Patient/5"
    assert inst.period.end == fhirtypes.DateTime.validate("2012-03-17")
    assert inst.relationship.coding[0].code == "self"
    assert inst.status == "active"
    assert inst.subscriber.reference == "Patient/5"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of a Self Pay Agreement.</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "pay"
    assert inst.type.coding[0].display == "PAY"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/coverage-selfpay"


def test_coverage_2(base_settings):
    """No. 2 tests collection for Coverage.
    Test File: coverage-example-selfpay.json
    """
    filename = base_settings["unittest_data_dir"] / "coverage-example-selfpay.json"
    inst = coverage.Coverage.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Coverage" == inst.resource_type

    impl_coverage_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Coverage" == data["resourceType"]

    inst2 = coverage.Coverage(**data)
    impl_coverage_2(inst2)


def impl_coverage_3(inst):
    assert inst.beneficiary.reference == "Patient/5"
    assert inst.id == "7547E"
    assert inst.identifier[0].system == "http://ehic.com/insurer/123456789/member"
    assert inst.identifier[0].value == "A123456780"
    assert inst.payor[0].identifier.system == "http://ehic.com/insurer"
    assert inst.payor[0].identifier.value == "123456789"
    assert inst.period.end == fhirtypes.DateTime.validate("2012-03-17")
    assert inst.relationship.coding[0].code == "self"
    assert inst.status == "active"
    assert inst.subscriber.reference == "Patient/5"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the European Health Insurance Card</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "EHCPOL"
    assert inst.type.coding[0].display == "extended healthcare"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/v3/ActCode"


def test_coverage_3(base_settings):
    """No. 3 tests collection for Coverage.
    Test File: coverage-example-ehic.json
    """
    filename = base_settings["unittest_data_dir"] / "coverage-example-ehic.json"
    inst = coverage.Coverage.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Coverage" == inst.resource_type

    impl_coverage_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Coverage" == data["resourceType"]

    inst2 = coverage.Coverage(**data)
    impl_coverage_3(inst2)


def impl_coverage_4(inst):
    assert inst.beneficiary.reference == "Patient/4"
    assert inst.dependent == "0"
    assert inst.grouping.classDisplay == "Silver: Family Plan spouse only"
    assert inst.grouping.class_fhir == "SILVER"
    assert inst.grouping.group == "CBI35"
    assert inst.grouping.groupDisplay == "Corporate Baker's Inc. Local #35"
    assert inst.grouping.plan == "B37FC"
    assert (
        inst.grouping.planDisplay
        == "Full Coverage: Medical, Dental, Pharmacy, Vision, EHC"
    )
    assert inst.grouping.subClass == "Tier2"
    assert inst.grouping.subClassDisplay == "Low deductable, max $20 copay"
    assert inst.grouping.subGroup == "123"
    assert inst.grouping.subGroupDisplay == "Trainee Part-time Benefits"
    assert inst.grouping.subPlan == "P7"
    assert inst.grouping.subPlanDisplay == "Includes afterlife benefits"
    assert inst.id == "9876B1"
    assert inst.identifier[0].system == "http://benefitsinc.com/certificate"
    assert inst.identifier[0].value == "12345"
    assert inst.payor[0].reference == "Organization/2"
    assert inst.period.end == fhirtypes.DateTime.validate("2012-05-23")
    assert inst.period.start == fhirtypes.DateTime.validate("2011-05-23")
    assert (
        inst.policyHolder.reference == "http://benefitsinc.com/FHIR/Organization/CBI35"
    )
    assert inst.relationship.coding[0].code == "self"
    assert inst.sequence == "9"
    assert inst.status == "active"
    assert inst.subscriber.reference == "Patient/4"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the coverage</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "EHCPOL"
    assert inst.type.coding[0].display == "extended healthcare"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/v3/ActCode"


def test_coverage_4(base_settings):
    """No. 4 tests collection for Coverage.
    Test File: coverage-example.json
    """
    filename = base_settings["unittest_data_dir"] / "coverage-example.json"
    inst = coverage.Coverage.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Coverage" == inst.resource_type

    impl_coverage_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Coverage" == data["resourceType"]

    inst2 = coverage.Coverage(**data)
    impl_coverage_4(inst2)
