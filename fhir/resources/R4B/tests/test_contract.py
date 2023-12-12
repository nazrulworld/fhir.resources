# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Contract
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import contract


def impl_contract_1(inst):
    assert inst.authority[0].display == "Michigan Health"
    assert inst.authority[0].reference == "Organization/3"
    assert inst.domain[0].display == "UK Pharmacies"
    assert inst.domain[0].reference == "Location/ukp"
    assert (
        inst.friendly[0].contentAttachment.title
        == "The terms of the consent in friendly consumer speak."
    )
    assert inst.id == "pcd-example-notOrg"
    assert inst.issued == fhirtypes.DateTime.validate("2015-11-18")
    assert (
        inst.legal[0].contentAttachment.title
        == "The terms of the consent in lawyer speak."
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.subType[0].coding[0].code == "Opt-In"
    assert inst.subType[0].coding[0].display == "Default Authorization with exceptions."
    assert (
        inst.subType[0].coding[0].system
        == "http://www.infoway-inforoute.ca.org/Consent-subtype-codes"
    )
    assert inst.subject[0].display == "P. van de Heuvel"
    assert inst.subject[0].reference == "Patient/f001"
    assert inst.term[0].offer.text == (
        "Withhold this order and any results or related objects from " "any provider."
    )
    assert inst.term[0].offer.topic.display == "Good Health Clinic"
    assert inst.term[0].offer.topic.reference == "Organization/2.16.840.1.113883.19.5"
    assert inst.term[0].type.coding[0].code == "withhold-from"
    assert (
        inst.term[0].type.coding[0].display
        == "Withhold all data from specified actor entity."
    )
    assert (
        inst.term[0].type.coding[0].system
        == "http://example.org/fhir/consent-term-type-codes"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "57016-8"
    assert inst.type.coding[0].system == "http://loinc.org"


def test_contract_1(base_settings):
    """No. 1 tests collection for Contract.
    Test File: pcd-example-notOrg.json
    """
    filename = base_settings["unittest_data_dir"] / "pcd-example-notOrg.json"
    inst = contract.Contract.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Contract" == inst.resource_type

    impl_contract_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Contract" == data["resourceType"]

    inst2 = contract.Contract(**data)
    impl_contract_1(inst2)


def impl_contract_2(inst):
    assert inst.applies.start == fhirtypes.DateTime.validate("2017-01-01")
    assert inst.id == "INS-101"
    assert inst.identifier[0].system == "http://xyz-insurance.com/forms"
    assert inst.identifier[0].value == "YCSCWLN(01-2017)"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.subject[0].reference == "Patient/1"
    assert inst.term[0].asset[0].period[0].start == fhirtypes.DateTime.validate(
        "2017-06-01"
    )
    assert inst.term[0].asset[0].subtype[0].text == "sample"
    assert inst.term[0].asset[0].type[0].coding[0].code == "RicardianContract"
    assert (
        inst.term[0].asset[0].type[0].coding[0].system == "http://something/something"
    )
    assert inst.term[0].asset[0].valuedItem[
        0
    ].effectiveTime == fhirtypes.DateTime.validate("1995")
    assert (
        inst.term[0].asset[0].valuedItem[0].entityCodeableConcept.text == "Ford Bobcat"
    )
    assert float(inst.term[0].asset[0].valuedItem[0].factor) == float(1.0)
    assert (
        inst.term[0].asset[0].valuedItem[0].identifier.system
        == "http://somewhere.motor-vehicle.com/vin"
    )
    assert inst.term[0].asset[0].valuedItem[0].identifier.value == "XXSVT34-7665t952236"
    assert inst.term[0].asset[0].valuedItem[0].net.currency == "CAD"
    assert float(inst.term[0].asset[0].valuedItem[0].net.value) == float(200.0)
    assert float(inst.term[0].asset[0].valuedItem[0].points) == float(1.0)
    assert float(inst.term[0].asset[0].valuedItem[0].quantity.value) == float(1)
    assert inst.term[0].asset[0].valuedItem[0].unitPrice.currency == "CAD"
    assert float(inst.term[0].asset[0].valuedItem[0].unitPrice.value) == float(200.0)
    assert inst.term[0].group[0].offer.text == "Eligible Providers"
    assert inst.term[0].group[1].offer.text == "Responsibility for Payment"
    assert inst.term[0].group[2].group[0].group[0].offer.text == "Emergency Room Copay"
    assert (
        inst.term[0].group[2].group[0].group[1].offer.text == "Professional Visit Copay"
    )
    assert inst.term[0].group[2].group[0].offer.text == "Copays"
    assert inst.term[0].group[2].group[1].offer.text == "Calendar Year Deductible"
    assert inst.term[0].group[2].group[2].offer.text == "Out-Of-Pocket Maximum"
    assert inst.term[0].group[2].group[3].group[0].offer.text == "Ambulance Services"
    assert inst.term[0].group[2].group[3].group[1].offer.text == "Dental Services"
    assert inst.term[0].group[2].group[3].group[2].offer.text == "Diagnostic Services"
    assert (
        inst.term[0].group[2].group[3].group[3].offer.text == "Emergency Room Services"
    )
    assert (
        inst.term[0].group[2].group[3].group[4].offer.text == "Hospital Inpatient Care"
    )
    assert inst.term[0].group[2].group[3].offer.text == "Medical Services"
    assert inst.term[0].group[2].offer.text == "List of Benefits"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "healthinsurance"
    assert inst.type.coding[0].display == "Health Insurance"
    assert (
        inst.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/contract-type"
    )


def test_contract_2(base_settings):
    """No. 2 tests collection for Contract.
    Test File: contract-example-ins-policy.json
    """
    filename = base_settings["unittest_data_dir"] / "contract-example-ins-policy.json"
    inst = contract.Contract.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Contract" == inst.resource_type

    impl_contract_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Contract" == data["resourceType"]

    inst2 = contract.Contract(**data)
    impl_contract_2(inst2)


def impl_contract_3(inst):
    assert inst.applies.start == fhirtypes.DateTime.validate(
        "2013-11-01T21:18:27-04:00"
    )
    assert inst.contentDerivative.coding[0].code == "registration"
    assert inst.contentDerivative.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/contract-content-" "derivative"
    )
    assert inst.id == "C-2121"
    assert inst.issued == fhirtypes.DateTime.validate("2013-11-01T21:18:27-04:00")
    assert inst.legal[0].contentAttachment.contentType == "application/pdf"
    assert inst.legal[0].contentAttachment.language == "en-US"
    assert (
        inst.legal[0].contentAttachment.title
        == "MDHHS-5515 Consent To Share Your Health Information"
    )
    assert (
        inst.legal[0].contentAttachment.url
        == "http://org.mihin.ecms/ConsentDirective-2121"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2016-07-19T18:18:42.108-04:00"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.meta.versionId == "1"
    assert inst.signer[0].party.display == "Alice Recruit"
    assert inst.signer[0].party.reference == "Patient/f201"
    assert inst.signer[0].signature[0].type[0].code == "1.2.840.10065.1.12.1.1"
    assert inst.signer[0].signature[0].type[0].system == "urn:iso-astm:E1762-95:2013"
    assert inst.signer[0].signature[0].when == fhirtypes.Instant.validate(
        "2017-02-08T10:57:34+01:00"
    )
    assert inst.signer[0].signature[0].who.reference == "Patient/f201"
    assert inst.signer[0].type.code == "SELF"
    assert inst.signer[0].type.system == "http://mdhhs.org/fhir/consent-signer-type"
    assert inst.status == "executed"
    assert inst.subType[0].coding[0].code == "hcd"
    assert (
        inst.subType[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/consentcategorycodes"
    )
    assert inst.subject[0].reference == "Patient/f201"
    assert inst.term[0].action[0].intent.coding[0].code == "HPRGRP"
    assert (
        inst.term[0].action[0].intent.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.term[0].action[0].status.text == "Sample"
    assert (
        inst.term[0].action[0].subject[0].reference[0].display
        == "VA Ann Arbor Healthcare System"
    )
    assert (
        inst.term[0].action[0].subject[0].reference[0].reference == "Organization/f001"
    )
    assert inst.term[0].action[0].subject[0].role.coding[0].code == "IR"
    assert inst.term[0].action[0].subject[0].role.coding[0].display == "Recipient"
    assert (
        inst.term[0].action[0].subject[0].role.coding[0].system
        == "http://mdhhs.org/fhir/consent-actor-type"
    )
    assert (
        inst.term[0].action[0].subject[0].role.text
        == "Recipient of restricted health information"
    )
    assert (
        inst.term[0].action[0].subject[1].reference[0].display
        == "Community Mental Health Clinic"
    )
    assert inst.term[0].action[0].subject[1].reference[0].reference == "Organization/2"
    assert inst.term[0].action[0].subject[1].role.coding[0].code == "IS"
    assert inst.term[0].action[0].subject[1].role.coding[0].display == "Sender"
    assert (
        inst.term[0].action[0].subject[1].role.coding[0].system
        == "http://mdhhs.org/fhir/consent-actor-type"
    )
    assert (
        inst.term[0].action[0].subject[1].role.text
        == "Sender of restricted health information"
    )
    assert inst.term[0].action[0].type.coding[0].code == "action-a"
    assert (
        inst.term[0].action[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/contractaction"
    )
    assert inst.term[0].asset[0].period[0].end == fhirtypes.DateTime.validate(
        "2019-11-01T21:18:27-04:00"
    )
    assert inst.term[0].asset[0].period[0].start == fhirtypes.DateTime.validate(
        "2013-11-01T21:18:27-04:00"
    )
    assert inst.term[0].offer.decision.coding[0].code == "OPTIN"
    assert (
        inst.term[0].offer.decision.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.term[0].offer.text == "Can't refuse"
    assert inst.term[0].offer.type.coding[0].code == "statutory"
    assert (
        inst.term[0].offer.type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/contracttermtypecodes"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "OPTIN"
    assert inst.type.coding[0].system == "http://mdhhs.org/fhir/consentdirective-type"
    assert inst.type.text == "Opt-in consent directive"


def test_contract_3(base_settings):
    """No. 3 tests collection for Contract.
    Test File: contract-example-42cfr-part2.json
    """
    filename = base_settings["unittest_data_dir"] / "contract-example-42cfr-part2.json"
    inst = contract.Contract.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Contract" == inst.resource_type

    impl_contract_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Contract" == data["resourceType"]

    inst2 = contract.Contract(**data)
    impl_contract_3(inst2)


def impl_contract_4(inst):
    assert inst.authority[0].display == "Michigan Health"
    assert inst.authority[0].reference == "Organization/3"
    assert inst.domain[0].display == "UK Pharmacies"
    assert inst.domain[0].reference == "Location/ukp"
    assert (
        inst.friendly[0].contentAttachment.title
        == "The terms of the consent in friendly consumer speak."
    )
    assert inst.id == "pcd-example-notLabs"
    assert inst.issued == fhirtypes.DateTime.validate("2014-08-17")
    assert (
        inst.legal[0].contentAttachment.title
        == "The terms of the consent in lawyer speak."
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.subType[0].coding[0].code == "Opt-In"
    assert inst.subType[0].coding[0].display == "Default Authorization with exceptions."
    assert (
        inst.subType[0].coding[0].system
        == "http://www.infoway-inforoute.ca.org/Consent-subtype-codes"
    )
    assert inst.subject[0].display == "P. van de Heuvel"
    assert inst.subject[0].reference == "Patient/f001"
    assert inst.term[0].group[0].offer.text == "Withhold orders from any provider."
    assert inst.term[0].group[0].subType.coding[0].code == "ServiceRequest"
    assert (
        inst.term[0].group[0].subType.coding[0].system
        == "http://hl7.org/fhir/resource-types"
    )
    assert inst.term[0].group[0].type.coding[0].code == "withhold-object-type"
    assert (
        inst.term[0].group[0].type.coding[0].system
        == "http://example.org/fhir/consent-term-type-codes"
    )
    assert (
        inst.term[0].group[1].offer.text == "Withhold order results from any provider."
    )
    assert inst.term[0].group[1].subType.coding[0].code == "DiagnosticReport"
    assert (
        inst.term[0].group[1].subType.coding[0].system
        == "http://hl7.org/fhir/resource-types"
    )
    assert inst.term[0].group[1].type.coding[0].code == "withhold-object-type"
    assert (
        inst.term[0].group[1].type.coding[0].system
        == "http://example.org/fhir/consent-term-type-codes"
    )
    assert inst.term[0].offer.text == "sample"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "57016-8"
    assert inst.type.coding[0].system == "http://loinc.org"


def test_contract_4(base_settings):
    """No. 4 tests collection for Contract.
    Test File: pcd-example-notLabs.json
    """
    filename = base_settings["unittest_data_dir"] / "pcd-example-notLabs.json"
    inst = contract.Contract.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Contract" == inst.resource_type

    impl_contract_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Contract" == data["resourceType"]

    inst2 = contract.Contract(**data)
    impl_contract_4(inst2)


def impl_contract_5(inst):
    assert inst.authority[0].display == "Michigan Health"
    assert inst.authority[0].reference == "Organization/3"
    assert inst.domain[0].display == "UK Pharmacies"
    assert inst.domain[0].reference == "Location/ukp"
    assert (
        inst.friendly[0].contentAttachment.title
        == "The terms of the consent in friendly consumer speak."
    )
    assert inst.id == "pcd-example-notThem"
    assert inst.issued == fhirtypes.DateTime.validate("2015-11-18")
    assert (
        inst.legal[0].contentAttachment.title
        == "The terms of the consent in lawyer speak."
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.signer[0].party.reference == "Patient/f001"
    assert inst.signer[0].signature[0].type[0].code == "1.2.840.10065.1.12.1.1"
    assert inst.signer[0].signature[0].type[0].system == "urn:iso-astm:E1762-95:2013"
    assert inst.signer[0].signature[0].when == fhirtypes.Instant.validate(
        "2013-06-08T10:57:34-07:00"
    )
    assert inst.signer[0].signature[0].who.reference == "Patient/f001"
    assert inst.signer[0].type.code == "COVPTY"
    assert inst.signer[0].type.system == (
        "http://terminology.hl7.org/CodeSystem/contractsignertypecode" "s"
    )
    assert inst.subType[0].coding[0].code == "Opt-In"
    assert inst.subType[0].coding[0].display == "Default Authorization with exceptions."
    assert (
        inst.subType[0].coding[0].system
        == "http://www.infoway-inforoute.ca.org/Consent-subtype-codes"
    )
    assert inst.subject[0].display == "P. van de Heuvel"
    assert inst.subject[0].reference == "Patient/f001"
    assert inst.term[0].offer.text == (
        "Withhold this order and any results or related objects from "
        "specified nurse provider."
    )
    assert inst.term[0].offer.topic.display == "Fictive Nurse"
    assert inst.term[0].offer.topic.reference == "Practitioner/f204"
    assert inst.term[0].type.coding[0].code == "withhold-from"
    assert (
        inst.term[0].type.coding[0].display
        == "Withhold all data from specified actor entity."
    )
    assert (
        inst.term[0].type.coding[0].system
        == "http://example.org/fhir/consent-term-type-codes"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "57016-8"
    assert inst.type.coding[0].system == "http://loinc.org"


def test_contract_5(base_settings):
    """No. 5 tests collection for Contract.
    Test File: pcd-example-notThem.json
    """
    filename = base_settings["unittest_data_dir"] / "pcd-example-notThem.json"
    inst = contract.Contract.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Contract" == inst.resource_type

    impl_contract_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Contract" == data["resourceType"]

    inst2 = contract.Contract(**data)
    impl_contract_5(inst2)


def impl_contract_6(inst):
    assert inst.authority[0].display == "Michigan Health"
    assert inst.authority[0].reference == "Organization/3"
    assert inst.domain[0].display == "UK Pharmacies"
    assert inst.domain[0].reference == "Location/ukp"
    assert (
        inst.friendly[0].contentAttachment.title
        == "The terms of the consent in friendly consumer speak."
    )
    assert inst.id == "pcd-example-notAuthor"
    assert inst.issued == fhirtypes.DateTime.validate("2015-11-18")
    assert (
        inst.legal[0].contentAttachment.title
        == "The terms of the consent in lawyer speak."
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.subType[0].coding[0].code == "Opt-In"
    assert inst.subType[0].coding[0].display == "Default Authorization with exceptions."
    assert (
        inst.subType[0].coding[0].system
        == "http://www.infoway-inforoute.ca.org/Consent-subtype-codes"
    )
    assert inst.subject[0].display == "P. van de Heuvel"
    assert inst.subject[0].reference == "Patient/f001"
    assert (
        inst.term[0].offer.text == "Withhold all data authored by Good Health provider."
    )
    assert inst.term[0].offer.topic.display == "Good Health Clinic"
    assert inst.term[0].offer.topic.reference == "Organization/2.16.840.1.113883.19.5"
    assert inst.term[0].type.coding[0].code == "withhold-authored-by"
    assert (
        inst.term[0].type.coding[0].display
        == "Withhold all data authored by specified actor entity."
    )
    assert (
        inst.term[0].type.coding[0].system
        == "http://example.org/fhir/consent-term-type-codes"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "57016-8"
    assert inst.type.coding[0].system == "http://loinc.org"


def test_contract_6(base_settings):
    """No. 6 tests collection for Contract.
    Test File: pcd-example-notAuthor.json
    """
    filename = base_settings["unittest_data_dir"] / "pcd-example-notAuthor.json"
    inst = contract.Contract.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Contract" == inst.resource_type

    impl_contract_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Contract" == data["resourceType"]

    inst2 = contract.Contract(**data)
    impl_contract_6(inst2)


def impl_contract_7(inst):
    assert inst.id == "C-123"
    assert inst.identifier[0].system == "http://happyvalley.com/contract"
    assert inst.identifier[0].value == "12347"
    assert inst.legallyBindingAttachment.contentType == "application/pdf"
    assert inst.legallyBindingAttachment.url == "http://www.aws3.com/storage/doc.pdf"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.rule[0].contentAttachment.contentType == "application/txt"
    assert (
        inst.rule[0].contentAttachment.url == "http://www.rfc-editor.org/bcp/bcp13.txt"
    )
    assert inst.term[0].asset[0].period[0].start == fhirtypes.DateTime.validate(
        "2017-06-01"
    )
    assert inst.term[0].asset[0].subtype[0].text == "sample"
    assert inst.term[0].asset[0].type[0].coding[0].code == "RicardianContract"
    assert (
        inst.term[0].asset[0].type[0].coding[0].system == "http://something/something"
    )
    assert inst.term[0].asset[0].valuedItem[
        0
    ].effectiveTime == fhirtypes.DateTime.validate("1995")
    assert (
        inst.term[0].asset[0].valuedItem[0].entityCodeableConcept.text == "Ford Bobcat"
    )
    assert float(inst.term[0].asset[0].valuedItem[0].factor) == float(1.0)
    assert (
        inst.term[0].asset[0].valuedItem[0].identifier.system
        == "http://somewhere.motor-vehicle.com/vin"
    )
    assert inst.term[0].asset[0].valuedItem[0].identifier.value == "XXSVT34-7665t952236"
    assert inst.term[0].asset[0].valuedItem[0].net.currency == "CAD"
    assert float(inst.term[0].asset[0].valuedItem[0].net.value) == float(200.0)
    assert float(inst.term[0].asset[0].valuedItem[0].points) == float(1.0)
    assert float(inst.term[0].asset[0].valuedItem[0].quantity.value) == float(1)
    assert inst.term[0].asset[0].valuedItem[0].unitPrice.currency == "CAD"
    assert float(inst.term[0].asset[0].valuedItem[0].unitPrice.value) == float(200.0)
    assert inst.term[0].offer.text == "Can't refuse"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the contract</div>"
    )
    assert inst.text.status == "generated"


def test_contract_7(base_settings):
    """No. 7 tests collection for Contract.
    Test File: contract-example.json
    """
    filename = base_settings["unittest_data_dir"] / "contract-example.json"
    inst = contract.Contract.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Contract" == inst.resource_type

    impl_contract_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Contract" == data["resourceType"]

    inst2 = contract.Contract(**data)
    impl_contract_7(inst2)


def impl_contract_8(inst):
    assert inst.authority[0].display == "Michigan Health"
    assert inst.authority[0].reference == "Organization/3"
    assert inst.domain[0].display == "UK Pharmacies"
    assert inst.domain[0].reference == "Location/ukp"
    assert (
        inst.friendly[0].contentAttachment.title
        == "The terms of the consent in friendly consumer speak."
    )
    assert inst.id == "pcd-example-notThis"
    assert inst.issued == fhirtypes.DateTime.validate("2015-11-18")
    assert (
        inst.legal[0].contentAttachment.title
        == "The terms of the consent in lawyer speak."
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.subType[0].coding[0].code == "Opt-In"
    assert inst.subType[0].coding[0].display == "Default Authorization with exceptions."
    assert (
        inst.subType[0].coding[0].system
        == "http://www.infoway-inforoute.ca.org/Consent-subtype-codes"
    )
    assert inst.subject[0].display == "P. van de Heuvel"
    assert inst.subject[0].reference == "Patient/f001"
    assert inst.term[0].applies.start == fhirtypes.DateTime.validate("2015-11-18")
    assert inst.term[0].identifier.system == "http://example.org/fhir/term-items"
    assert inst.term[0].identifier.value == "3347689"
    assert inst.term[0].issued == fhirtypes.DateTime.validate("2015-11-01")
    assert inst.term[0].offer.text == (
        "Withhold this order and any results or related objects from " "any provider."
    )
    assert inst.term[0].offer.topic.reference == "ServiceRequest/lipid"
    assert inst.term[0].type.coding[0].code == "withhold-identified-object-and-related"
    assert inst.term[0].type.coding[0].display == (
        "Withhold the identified object and any other resources that "
        "are related to this object."
    )
    assert (
        inst.term[0].type.coding[0].system
        == "http://example.org/fhir/consent-term-type-codes"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "57016-8"
    assert inst.type.coding[0].system == "http://loinc.org"


def test_contract_8(base_settings):
    """No. 8 tests collection for Contract.
    Test File: pcd-example-notThis.json
    """
    filename = base_settings["unittest_data_dir"] / "pcd-example-notThis.json"
    inst = contract.Contract.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Contract" == inst.resource_type

    impl_contract_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Contract" == data["resourceType"]

    inst2 = contract.Contract(**data)
    impl_contract_8(inst2)
