# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentNotice
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import paymentnotice


def impl_paymentnotice_1(inst):
    assert inst.amount.currency == "USD"
    assert float(inst.amount.value) == float(12500.0)
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "77654"
    assert inst.identifier[0].system == "http://benefitsinc.com/paymentnotice"
    assert inst.identifier[0].value == "776543"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.payee.reference == "Organization/1"
    assert inst.payment.reference == "PaymentReconciliation/ER2500"
    assert inst.paymentDate == fhirtypes.Date.validate("2014-08-15")
    assert inst.paymentStatus.coding[0].code == "paid"
    assert (
        inst.paymentStatus.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/paymentstatus"
    )
    assert inst.provider.reference == "Organization/1"
    assert inst.recipient.identifier.system == "http://regulators.gov"
    assert inst.recipient.identifier.value == "AB123"
    assert inst.request.reference == "http://benefitsinc.com/fhir/claim/12345"
    assert (
        inst.response.reference == "http://benefitsinc.com/fhir/claimresponse/CR12345"
    )
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the PaymentNotice</div>"
    )
    assert inst.text.status == "generated"


def test_paymentnotice_1(base_settings):
    """No. 1 tests collection for PaymentNotice.
    Test File: paymentnotice-example.json
    """
    filename = base_settings["unittest_data_dir"] / "paymentnotice-example.json"
    inst = paymentnotice.PaymentNotice.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PaymentNotice" == inst.resource_type

    impl_paymentnotice_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PaymentNotice" == data["resourceType"]

    inst2 = paymentnotice.PaymentNotice(**data)
    impl_paymentnotice_1(inst2)
