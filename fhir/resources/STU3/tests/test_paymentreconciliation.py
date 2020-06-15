# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import paymentreconciliation


def impl_paymentreconciliation_1(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.detail[0].amount.code == "USD"
    assert inst.detail[0].amount.system == "urn:iso:std:iso:4217"
    assert float(inst.detail[0].amount.value) == float(1000.0)
    assert inst.detail[0].date == fhirtypes.Date.validate("2014-08-16")
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
    assert inst.detail[0].type.coding[0].system == "http://hl7.org/fhir/payment-type"
    assert inst.detail[1].amount.code == "USD"
    assert inst.detail[1].amount.system == "urn:iso:std:iso:4217"
    assert float(inst.detail[1].amount.value) == float(4000.0)
    assert inst.detail[1].date == fhirtypes.Date.validate("2014-08-12")
    assert (
        inst.detail[1].request.reference
        == "http://www.BenefitsInc.com/fhir/oralhealthclaim/225476332699"
    )
    assert inst.detail[1].type.coding[0].code == "payment"
    assert inst.detail[1].type.coding[0].system == "http://hl7.org/fhir/payment-type"
    assert inst.detail[2].amount.code == "USD"
    assert inst.detail[2].amount.system == "urn:iso:std:iso:4217"
    assert float(inst.detail[2].amount.value) == float(-1500.0)
    assert inst.detail[2].date == fhirtypes.Date.validate("2014-08-16")
    assert inst.detail[2].type.coding[0].code == "advance"
    assert inst.detail[2].type.coding[0].system == "http://hl7.org/fhir/payment-type"
    assert inst.disposition == "2014 August mid-month settlement."
    assert inst.form.coding[0].code == "PAYREC/2016/01B"
    assert inst.form.coding[0].system == "http://ncforms.org/formid"
    assert inst.id == "ER2500"
    assert (
        inst.identifier[0].system
        == "http://www.BenefitsInc.com/fhir/enrollmentresponse"
    )
    assert inst.identifier[0].value == "781234"
    assert inst.organization.reference == "Organization/2"
    assert inst.outcome.coding[0].code == "complete"
    assert inst.outcome.coding[0].system == "http://hl7.org/fhir/remittance-outcome"
    assert inst.period.end == fhirtypes.DateTime.validate("2014-08-31")
    assert inst.period.start == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.processNote[0].text == (
        "Due to the year end holiday the cutoff for submissions for "
        "December will be the 28th."
    )
    assert inst.processNote[0].type.coding[0].code == "display"
    assert inst.processNote[0].type.coding[0].system == "http://hl7.org/fhir/note-type"
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/eligibility/225476332402"
    )
    assert inst.requestOrganization.reference == "Organization/1"
    assert inst.requestProvider.reference == "Practitioner/example"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the PaymentReconciliation</div>"
    )
    assert inst.text.status == "generated"
    assert inst.total.code == "USD"
    assert inst.total.system == "urn:iso:std:iso:4217"
    assert float(inst.total.value) == float(3500.0)


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
