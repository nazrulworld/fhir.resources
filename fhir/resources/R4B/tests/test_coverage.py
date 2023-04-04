# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coverage
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import coverage


def impl_coverage_1(inst):
    assert inst.beneficiary.reference == "Patient/5"
    assert inst.class_fhir[0].name == "Western Airlines"
    assert inst.class_fhir[0].type.coding[0].code == "group"
    assert (
        inst.class_fhir[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[0].value == "WESTAIR"
    assert (
        inst.class_fhir[1].name
        == "Full Coverage: Medical, Dental, Pharmacy, Vision, EHC"
    )
    assert inst.class_fhir[1].type.coding[0].code == "plan"
    assert (
        inst.class_fhir[1].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[1].value == "BG4352"
    assert inst.class_fhir[2].name == "Platinum"
    assert inst.class_fhir[2].type.coding[0].code == "subplan"
    assert (
        inst.class_fhir[2].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[2].value == "D15C9"
    assert inst.contract[0].reference == "Contract/INS-101"
    assert inst.costToBeneficiary[0].exception[
        0
    ].period.end == fhirtypes.DateTime.validate("2018-12-31")
    assert inst.costToBeneficiary[0].exception[
        0
    ].period.start == fhirtypes.DateTime.validate("2018-01-01")
    assert inst.costToBeneficiary[0].exception[0].type.coding[0].code == "retired"
    assert inst.costToBeneficiary[0].exception[0].type.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/ex-coverage-financial-" "exception"
    )
    assert inst.costToBeneficiary[0].type.coding[0].code == "gpvisit"
    assert (
        inst.costToBeneficiary[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-copay-type"
    )
    assert inst.costToBeneficiary[0].valueMoney.currency == "USD"
    assert float(inst.costToBeneficiary[0].valueMoney.value) == float(20.0)
    assert inst.dependent == "1"
    assert inst.id == "7546D"
    assert inst.identifier[0].system == "http://xyz.com/codes/identifier"
    assert inst.identifier[0].value == "AB98761"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )


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
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-selfpay"
    )


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
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )


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
    assert inst.class_fhir[0].name == "Corporate Baker's Inc. Local #35"
    assert inst.class_fhir[0].type.coding[0].code == "group"
    assert (
        inst.class_fhir[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[0].value == "CB135"
    assert inst.class_fhir[1].name == "Trainee Part-time Benefits"
    assert inst.class_fhir[1].type.coding[0].code == "subgroup"
    assert (
        inst.class_fhir[1].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[1].value == "123"
    assert (
        inst.class_fhir[2].name
        == "Full Coverage: Medical, Dental, Pharmacy, Vision, EHC"
    )
    assert inst.class_fhir[2].type.coding[0].code == "plan"
    assert (
        inst.class_fhir[2].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[2].value == "B37FC"
    assert inst.class_fhir[3].name == "Includes afterlife benefits"
    assert inst.class_fhir[3].type.coding[0].code == "subplan"
    assert (
        inst.class_fhir[3].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[3].value == "P7"
    assert inst.class_fhir[4].name == "Silver: Family Plan spouse only"
    assert inst.class_fhir[4].type.coding[0].code == "class"
    assert (
        inst.class_fhir[4].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[4].value == "SILVER"
    assert inst.class_fhir[5].name == "Low deductable, max $20 copay"
    assert inst.class_fhir[5].type.coding[0].code == "subclass"
    assert (
        inst.class_fhir[5].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[5].value == "Tier2"
    assert inst.class_fhir[6].type.coding[0].code == "sequence"
    assert (
        inst.class_fhir[6].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[6].value == "9"
    assert inst.class_fhir[7].type.coding[0].code == "rxid"
    assert (
        inst.class_fhir[7].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[7].value == "MDF12345"
    assert inst.class_fhir[8].type.coding[0].code == "rxbin"
    assert (
        inst.class_fhir[8].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[8].value == "987654"
    assert inst.class_fhir[9].type.coding[0].code == "rxgroup"
    assert (
        inst.class_fhir[9].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/coverage-class"
    )
    assert inst.class_fhir[9].value == "M35PT"
    assert inst.dependent == "0"
    assert inst.id == "9876B1"
    assert inst.identifier[0].system == "http://benefitsinc.com/certificate"
    assert inst.identifier[0].value == "12345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.payor[0].reference == "Organization/2"
    assert inst.period.end == fhirtypes.DateTime.validate("2012-05-23")
    assert inst.period.start == fhirtypes.DateTime.validate("2011-05-23")
    assert (
        inst.policyHolder.reference == "http://benefitsinc.com/FHIR/Organization/CBI35"
    )
    assert inst.relationship.coding[0].code == "self"
    assert inst.status == "active"
    assert inst.subscriber.reference == "Patient/4"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the coverage</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "EHCPOL"
    assert inst.type.coding[0].display == "extended healthcare"
    assert (
        inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )


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
