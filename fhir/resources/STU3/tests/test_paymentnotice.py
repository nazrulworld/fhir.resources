# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentNotice
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import paymentnotice


def impl_paymentnotice_1(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "77654"
    assert inst.identifier[0].system == "http://benefitsinc.com/paymentnotice"
    assert inst.identifier[0].value == "776543"
    assert inst.organization.reference == "Organization/1"
    assert inst.paymentStatus.coding[0].code == "paid"
    assert inst.paymentStatus.coding[0].system == "http://hl7.org/fhir/paymentstatus"
    assert inst.provider.identifier.system == "http://npid.org/provider"
    assert inst.provider.identifier.value == "PR957857"
    assert inst.request.reference == "http://benefitsinc.com/fhir/claim/12345"
    assert (
        inst.response.reference == "http://benefitsinc.com/fhir/claimresponse/CR12345"
    )
    assert inst.status == "active"
    assert inst.statusDate == fhirtypes.Date.validate("2014-08-15")
    assert inst.target.identifier.system == "http://regulators.gov"
    assert inst.target.identifier.value == "AB123"
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
