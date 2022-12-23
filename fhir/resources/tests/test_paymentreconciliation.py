# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import paymentreconciliation


def impl_paymentreconciliation_1(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.detail[0].amount.currency == "USD"
    assert float(inst.detail[0].amount.value) == float(3500.0)
    assert inst.detail[0].date == fhirtypes.Date.validate("2014-08-16")
    assert (
        inst.detail[0].identifier.system
        == "http://www.BenefitsInc.com/payment/2018/detail"
    )
    assert inst.detail[0].identifier.value == "10-12345-001"
    assert inst.detail[0].payee.reference == "Organization/1"
    assert (
        inst.detail[0].request.identifier.system == "http://happyvalleyclinic.com/claim"
    )
    assert inst.detail[0].request.identifier.value == "AB12345"
    assert (
        inst.detail[0].response.identifier.system
        == "http://www.BenefitsInc.com/fhir/claimresponse"
    )
    assert inst.detail[0].response.identifier.value == "CR20140815-AB12345"
    assert inst.detail[0].submitter.reference == "Organization/1"
    assert inst.detail[0].type.coding[0].code == "payment"
    assert (
        inst.detail[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/payment-type"
    )
    assert inst.detail[1].amount.currency == "USD"
    assert float(inst.detail[1].amount.value) == float(4000.0)
    assert inst.detail[1].date == fhirtypes.Date.validate("2014-08-12")
    assert (
        inst.detail[1].identifier.system
        == "http://www.BenefitsInc.com/payment/2018/detail"
    )
    assert inst.detail[1].identifier.value == "10-12345-002"
    assert (
        inst.detail[1].request.reference
        == "http://www.BenefitsInc.com/fhir/oralhealthclaim/225476332699"
    )
    assert inst.detail[1].type.coding[0].code == "payment"
    assert (
        inst.detail[1].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/payment-type"
    )
    assert inst.detail[2].amount.currency == "USD"
    assert float(inst.detail[2].amount.value) == float(-1500.0)
    assert inst.detail[2].date == fhirtypes.Date.validate("2014-08-16")
    assert (
        inst.detail[2].identifier.system
        == "http://www.BenefitsInc.com/payment/2018/detail"
    )
    assert inst.detail[2].identifier.value == "10-12345-003"
    assert inst.detail[2].type.coding[0].code == "advance"
    assert (
        inst.detail[2].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/payment-type"
    )
    assert inst.disposition == "2014 August mid-month settlement."
    assert inst.formCode.coding[0].code == "PAYREC/2016/01B"
    assert inst.formCode.coding[0].system == "http://ncforms.org/formid"
    assert inst.id == "ER2500"
    assert (
        inst.identifier[0].system
        == "http://www.BenefitsInc.com/fhir/enrollmentresponse"
    )
    assert inst.identifier[0].value == "781234"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.outcome == "complete"
    assert inst.paymentAmount.currency == "USD"
    assert float(inst.paymentAmount.value) == float(7000.0)
    assert inst.paymentDate == fhirtypes.Date.validate("2014-08-01")
    assert inst.paymentIdentifier.system == "http://www.BenefitsInc.com/payment/2018"
    assert inst.paymentIdentifier.value == "10-12345"
    assert inst.paymentIssuer.reference == "Organization/2"
    assert inst.period.end == fhirtypes.DateTime.validate("2014-08-31")
    assert inst.period.start == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.processNote[0].text == (
        "Due to the year end holiday the cutoff for submissions for "
        "December will be the 28th."
    )
    assert inst.processNote[0].type == "display"
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/eligibility/225476332402"
    )
    assert inst.requestor.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the PaymentReconciliation</div>"
    )
    assert inst.text.status == "generated"


def test_paymentreconciliation_1(base_settings):
    """No. 1 tests collection for PaymentReconciliation.
    Test File: paymentreconciliation-example.json
    """
    filename = base_settings["unittest_data_dir"] / "paymentreconciliation-example.json"
    inst = paymentreconciliation.PaymentReconciliation.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PaymentReconciliation" == inst.resource_type

    impl_paymentreconciliation_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PaymentReconciliation" == data["resourceType"]

    inst2 = paymentreconciliation.PaymentReconciliation(**data)
    impl_paymentreconciliation_1(inst2)
