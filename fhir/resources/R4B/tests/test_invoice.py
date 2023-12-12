# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Invoice
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import invoice


def impl_invoice_1(inst):
    assert inst.account.reference == "Account/example"
    assert inst.date == fhirtypes.DateTime.validate("2017-01-25T08:00:00+01:00")
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://myHospital.org/Invoices"
    assert inst.identifier[0].value == "654321"
    assert inst.issuer.identifier.system == "http://myhospital/NamingSystem/departments"
    assert inst.issuer.identifier.value == "CARD_INTERMEDIATE_CARE"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.participant[0].actor.reference == "Practitioner/example"
    assert inst.participant[0].role.coding[0].code == "17561000"
    assert inst.participant[0].role.coding[0].display == "Cardiologist"
    assert inst.participant[0].role.coding[0].system == "http://snomed.info/sct"
    assert inst.status == "issued"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Example of ' "Invoice</div>"
    )
    assert inst.text.status == "generated"
    assert inst.totalGross.currency == "EUR"
    assert float(inst.totalGross.value) == float(48)
    assert inst.totalNet.currency == "EUR"
    assert float(inst.totalNet.value) == float(40)


def test_invoice_1(base_settings):
    """No. 1 tests collection for Invoice.
    Test File: invoice-example.json
    """
    filename = base_settings["unittest_data_dir"] / "invoice-example.json"
    inst = invoice.Invoice.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Invoice" == inst.resource_type

    impl_invoice_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Invoice" == data["resourceType"]

    inst2 = invoice.Invoice(**data)
    impl_invoice_1(inst2)
