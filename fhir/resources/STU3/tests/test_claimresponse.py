# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import claimresponse


def impl_claimresponse_1(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.disposition == "Claim settled as per contract."
    assert inst.id == "R3500"
    assert inst.identifier[0].system == "http://www.BenefitsInc.com/fhir/remittance"
    assert inst.identifier[0].value == "R3500"
    assert inst.insurer.identifier.system == "http://www.jurisdiction.org/insurers"
    assert inst.insurer.identifier.value == "555123"
    assert inst.item[0].adjudication[0].amount.code == "USD"
    assert inst.item[0].adjudication[0].amount.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].adjudication[0].amount.value) == float(135.57)
    assert inst.item[0].adjudication[0].category.coding[0].code == "eligible"
    assert inst.item[0].adjudication[1].amount.code == "USD"
    assert inst.item[0].adjudication[1].amount.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].adjudication[1].amount.value) == float(10.0)
    assert inst.item[0].adjudication[1].category.coding[0].code == "copay"
    assert inst.item[0].adjudication[2].category.coding[0].code == "eligpercent"
    assert float(inst.item[0].adjudication[2].value) == float(80.0)
    assert inst.item[0].adjudication[3].amount.code == "USD"
    assert inst.item[0].adjudication[3].amount.system == "urn:iso:std:iso:4217"
    assert float(inst.item[0].adjudication[3].amount.value) == float(100.47)
    assert inst.item[0].adjudication[3].category.coding[0].code == "benefit"
    assert inst.item[0].sequenceLinkId == 1
    assert inst.outcome.coding[0].code == "complete"
    assert inst.outcome.coding[0].system == "http://hl7.org/fhir/remittance-outcome"
    assert inst.patient.reference == "Patient/1"
    assert inst.payeeType.coding[0].code == "provider"
    assert inst.payeeType.coding[0].system == "http://hl7.org/fhir/payeetype"
    assert inst.payment.amount.code == "USD"
    assert inst.payment.amount.system == "urn:iso:std:iso:4217"
    assert float(inst.payment.amount.value) == float(100.47)
    assert inst.payment.date == fhirtypes.Date.validate("2014-08-31")
    assert (
        inst.payment.identifier.system
        == "http://www.BenefitsInc.com/fhir/paymentidentifier"
    )
    assert inst.payment.identifier.value == "201408-2-1569478"
    assert inst.payment.type.coding[0].code == "complete"
    assert inst.payment.type.coding[0].system == "http://hl7.org/fhir/ex-paymenttype"
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/oralhealthclaim/15476332402"
    )
    assert inst.requestOrganization.reference == "Organization/1"
    assert inst.requestProvider.reference == "Practitioner/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the ClaimResponse</div>"
    )
    assert inst.text.status == "generated"
    assert inst.totalBenefit.code == "USD"
    assert inst.totalBenefit.system == "urn:iso:std:iso:4217"
    assert float(inst.totalBenefit.value) == float(100.47)
    assert inst.totalCost.code == "USD"
    assert inst.totalCost.system == "urn:iso:std:iso:4217"
    assert float(inst.totalCost.value) == float(135.57)


def test_claimresponse_1(base_settings):
    """No. 1 tests collection for ClaimResponse.
    Test File: claimresponse-example.json
    """
    filename = base_settings["unittest_data_dir"] / "claimresponse-example.json"
    inst = claimresponse.ClaimResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ClaimResponse" == inst.resource_type

    impl_claimresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ClaimResponse" == data["resourceType"]

    inst2 = claimresponse.ClaimResponse(**data)
    impl_claimresponse_1(inst2)
