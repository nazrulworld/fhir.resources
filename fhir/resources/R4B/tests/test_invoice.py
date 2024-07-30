# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Invoice
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import invoice
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_invoice_1(inst):
    assert inst.account.reference == "Account/example"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2017-01-25T08:00:00+01:00"}
        ).valueDateTime
    )
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://myHospital.org/Invoices"}
        ).valueUri
    )
    assert inst.identifier[0].value == "654321"
    assert (
        inst.issuer.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://myhospital/NamingSystem/departments"}
        ).valueUri
    )
    assert inst.issuer.identifier.value == "CARD_INTERMEDIATE_CARE"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.participant[0].actor.reference == "Practitioner/example"
    assert inst.participant[0].role.coding[0].code == "17561000"
    assert inst.participant[0].role.coding[0].display == "Cardiologist"
    assert (
        inst.participant[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
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
    inst = invoice.Invoice.model_validate_json(filename.read_bytes())
    assert "Invoice" == inst.get_resource_type()

    impl_invoice_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Invoice" == data["resourceType"]

    inst2 = invoice.Invoice(**data)
    impl_invoice_1(inst2)
