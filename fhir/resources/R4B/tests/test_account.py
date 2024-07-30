# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Account
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import account
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_account_1(inst):
    assert inst.coverage[0].coverage.reference == "Coverage/7546D"
    assert inst.coverage[0].priority == 1
    assert inst.description == "Hospital charges"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:0.1.2.3.4.5.6.7"}
        ).valueUri
    )
    assert inst.identifier[0].value == "654321"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "HACC Funded Billing for Peter James Chalmers"
    assert inst.owner.reference == "Organization/hl7"
    assert (
        inst.servicePeriod.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-06-30"}
        ).valueDateTime
    )
    assert (
        inst.servicePeriod.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-01-01"}
        ).valueDateTime
    )
    assert inst.status == "active"
    assert inst.subject[0].display == "Peter James Chalmers"
    assert inst.subject[0].reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">HACC Funded '
        "Billing for Peter James Chalmers</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "PBILLACCT"
    assert inst.type.coding[0].display == "patient billing account"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.type.text == "patient"


def test_account_1(base_settings):
    """No. 1 tests collection for Account.
    Test File: account-example.json
    """
    filename = base_settings["unittest_data_dir"] / "account-example.json"
    inst = account.Account.model_validate_json(filename.read_bytes())
    assert "Account" == inst.get_resource_type()

    impl_account_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Account" == data["resourceType"]

    inst2 = account.Account(**data)
    impl_account_1(inst2)


def impl_account_2(inst):
    assert inst.coverage[0].coverage.reference == "Coverage/9876B1"
    assert inst.coverage[0].priority == 1
    assert inst.coverage[1].coverage.reference == "Coverage/7546D"
    assert inst.coverage[1].priority == 2
    assert inst.description == "Hospital charges"
    assert inst.guarantor[0].onHold is False
    assert inst.guarantor[0].party.display == "Bénédicte du Marché"
    assert inst.guarantor[0].party.reference == "RelatedPerson/benedicte"
    assert (
        inst.guarantor[0].period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-01-01"}
        ).valueDateTime
    )
    assert inst.id == "ewg"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:0.1.2.3.4.5.6.7"}
        ).valueUri
    )
    assert inst.identifier[0].value == "654321"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Inpatient: Peter James Chalmers"
    assert inst.owner.display == "Burgers University Medical Center"
    assert inst.owner.reference == "Organization/f001"
    assert (
        inst.servicePeriod.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-06-30"}
        ).valueDateTime
    )
    assert (
        inst.servicePeriod.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-01-01"}
        ).valueDateTime
    )
    assert inst.status == "active"
    assert inst.subject[0].display == "Peter James Chalmers"
    assert inst.subject[0].reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Inpatient '
        "Admission for Peter James Chalmers Account</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "PBILLACCT"
    assert inst.type.coding[0].display == "patient billing account"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.type.text == "patient"


def test_account_2(base_settings):
    """No. 2 tests collection for Account.
    Test File: account-example-with-guarantor.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "account-example-with-guarantor.json"
    )
    inst = account.Account.model_validate_json(filename.read_bytes())
    assert "Account" == inst.get_resource_type()

    impl_account_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Account" == data["resourceType"]

    inst2 = account.Account(**data)
    impl_account_2(inst2)
