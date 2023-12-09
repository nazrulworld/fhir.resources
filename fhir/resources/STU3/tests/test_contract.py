# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Contract
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import contract


def impl_contract_1(inst):
    assert inst.authority[0].display == "Canada Infoway"
    assert inst.authority[0].reference == "Organization/Infoway"
    assert inst.domain[0].display == "Canada Infoway"
    assert inst.domain[0].reference == "Location/Infoway"
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
    assert inst.subType[0].coding[0].code == "Opt-In"
    assert inst.subType[0].coding[0].display == "Default Authorization with exceptions."
    assert (
        inst.subType[0].coding[0].system
        == "http://www.infoway-inforoute.ca.org/Consent-subtype-codes"
    )
    assert inst.subject[0].display == "P. van de Heuvel"
    assert inst.subject[0].reference == "Patient/f001"
    assert inst.term[0].text == (
        "Withhold this order and any results or related objects from " "any provider."
    )
    assert inst.term[0].topic[0].display == "Good Health Clinic"
    assert inst.term[0].topic[0].reference == "Organization/2.16.840.1.113883.19.5"
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
    assert inst.agent[0].actor.display == "VA Ann Arbor Healthcare System"
    assert inst.agent[0].actor.reference == "Organization/f001"
    assert inst.agent[0].role[0].coding[0].code == "IR"
    assert inst.agent[0].role[0].coding[0].display == "Recipient"
    assert (
        inst.agent[0].role[0].coding[0].system
        == "http://org.mdhhs.fhir.consent-actor-type"
    )
    assert inst.agent[0].role[0].text == "Recipient of restricted health information"
    assert inst.agent[1].actor.display == "Community Mental Health Clinic"
    assert inst.agent[1].actor.reference == "Organization/2"
    assert inst.agent[1].role[0].coding[0].code == "IS"
    assert inst.agent[1].role[0].coding[0].display == "Sender"
    assert (
        inst.agent[1].role[0].coding[0].system
        == "http://org.mdhhs.fhir.consent-actor-type"
    )
    assert inst.agent[1].role[0].text == "Sender of restricted health information"
    assert inst.id == "C-2121"
    assert inst.issued == fhirtypes.DateTime.validate("2031-11-01T21:18:27-04:00")
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
    assert inst.meta.versionId == "1"
    assert inst.securityLabel[0].code == "R"
    assert inst.securityLabel[0].display == "Restricted"
    assert inst.securityLabel[0].system == "http://hl7.org/fhir/v3/Confidentiality"
    assert inst.securityLabel[1].code == "ETH"
    assert inst.securityLabel[1].display == "substance abuse information sensitivity"
    assert inst.securityLabel[1].system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.securityLabel[2].code == "42CFRPart2"
    assert inst.securityLabel[2].system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.securityLabel[3].code == "TREAT"
    assert inst.securityLabel[3].display == "treatment"
    assert inst.securityLabel[3].system == "http://hl7.org/fhir/v3/ActReason"
    assert inst.securityLabel[4].code == "HPAYMT"
    assert inst.securityLabel[4].display == "healthcare payment"
    assert inst.securityLabel[4].system == "http://hl7.org/fhir/v3/ActReason"
    assert inst.securityLabel[5].code == "HOPERAT"
    assert inst.securityLabel[5].display == "healthcare operations"
    assert inst.securityLabel[5].system == "http://hl7.org/fhir/v3/ActReason"
    assert inst.securityLabel[6].code == "PERSISTLABEL"
    assert inst.securityLabel[6].display == "persist security label"
    assert inst.securityLabel[6].system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.securityLabel[7].code == "PRIVMARK"
    assert inst.securityLabel[7].display == "privacy mark"
    assert inst.securityLabel[7].system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.securityLabel[8].code == "NORDSCLCD"
    assert inst.securityLabel[8].display == "no redisclosure without consent directive"
    assert inst.securityLabel[8].system == "http://hl7.org/fhir/v3/ActCode"
    assert inst.signer[0].party.display == "Alice Recruit"
    assert inst.signer[0].party.reference == "Patient/f201"
    assert inst.signer[0].signature[0].type[0].code == "1.2.840.10065.1.12.1.1"
    assert inst.signer[0].signature[0].type[0].system == "urn:iso-astm:E1762-95:2013"
    assert inst.signer[0].signature[0].when == fhirtypes.Instant.validate(
        "2017-02-08T10:57:34+01:00"
    )
    assert inst.signer[0].signature[0].whoReference.reference == "Patient/f201"
    assert inst.signer[0].type.code == "SELF"
    assert inst.signer[0].type.system == "http://org.mdhhs.fhir.consent-signer-type"
    assert inst.subType[0].coding[0].code == "MDHHS-5515"
    assert inst.subType[0].coding[0].display == (
        "Michigan MDHHS-5515 Consent to Share Behavioral Health "
        "Information for Care Coordination Purposes"
    )
    assert (
        inst.subType[0].coding[0].system == "http://hl7.org/fhir/consentcategorycodes"
    )
    assert inst.subject[0].reference == "Patient/f201"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "OPTIN"
    assert inst.type.coding[0].system == "http://org.mdhhs.fhir.consentdirective-type"
    assert inst.type.text == "Opt-in consent directive"


def test_contract_2(base_settings):
    """No. 2 tests collection for Contract.
    Test File: contract-example-42cfr-part2.json
    """
    filename = base_settings["unittest_data_dir"] / "contract-example-42cfr-part2.json"
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
    assert inst.authority[0].display == "Canada Infoway"
    assert inst.authority[0].reference == "Organization/Infoway"
    assert inst.domain[0].display == "Canada Infoway"
    assert inst.domain[0].reference == "Location/Infoway"
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
    assert inst.subType[0].coding[0].code == "Opt-In"
    assert inst.subType[0].coding[0].display == "Default Authorization with exceptions."
    assert (
        inst.subType[0].coding[0].system
        == "http://www.infoway-inforoute.ca.org/Consent-subtype-codes"
    )
    assert inst.subject[0].display == "P. van de Heuvel"
    assert inst.subject[0].reference == "Patient/f001"
    assert inst.term[0].subType.coding[0].code == "ProcedureRequest"
    assert inst.term[0].subType.coding[0].system == "http://hl7.org/fhir/resource-types"
    assert inst.term[0].text == "Withhold orders from any provider."
    assert inst.term[0].type.coding[0].code == "withhold-object-type"
    assert (
        inst.term[0].type.coding[0].system
        == "http://example.org/fhir/consent-term-type-codes"
    )
    assert inst.term[1].subType.coding[0].code == "DiagnosticReport"
    assert inst.term[1].subType.coding[0].system == "http://hl7.org/fhir/resource-types"
    assert inst.term[1].text == "Withhold order results from any provider."
    assert inst.term[1].type.coding[0].code == "withhold-object-type"
    assert (
        inst.term[1].type.coding[0].system
        == "http://example.org/fhir/consent-term-type-codes"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "57016-8"
    assert inst.type.coding[0].system == "http://loinc.org"


def test_contract_3(base_settings):
    """No. 3 tests collection for Contract.
    Test File: pcd-example-notLabs.json
    """
    filename = base_settings["unittest_data_dir"] / "pcd-example-notLabs.json"
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
    assert inst.agent[0].actor.reference == "Patient/f001"
    assert inst.authority[0].display == "Canada Infoway"
    assert inst.authority[0].reference == "Organization/2"
    assert inst.domain[0].display == "Canada Infoway"
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
    assert inst.signer[0].party.reference == "Patient/f001"
    assert inst.signer[0].signature[0].type[0].code == "1.2.840.10065.1.12.1.1"
    assert inst.signer[0].signature[0].type[0].system == "urn:iso-astm:E1762-95:2013"
    assert inst.signer[0].signature[0].when == fhirtypes.Instant.validate(
        "2013-06-08T10:57:34-07:00"
    )
    assert inst.signer[0].signature[0].whoReference.reference == "Patient/f001"
    assert inst.signer[0].type.code == "COVPTY"
    assert (
        inst.signer[0].type.system == "http://www.hl7.org/fhir/contractsignertypecodes"
    )
    assert inst.subType[0].coding[0].code == "Opt-In"
    assert inst.subType[0].coding[0].display == "Default Authorization with exceptions."
    assert (
        inst.subType[0].coding[0].system
        == "http://www.infoway-inforoute.ca.org/Consent-subtype-codes"
    )
    assert inst.subject[0].display == "P. van de Heuvel"
    assert inst.subject[0].reference == "Patient/f001"
    assert inst.term[0].text == (
        "Withhold this order and any results or related objects from "
        "specified nurse provider."
    )
    assert inst.term[0].topic[0].display == "Fictive Nurse"
    assert inst.term[0].topic[0].reference == "Practitioner/f204"
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


def test_contract_4(base_settings):
    """No. 4 tests collection for Contract.
    Test File: pcd-example-notThem.json
    """
    filename = base_settings["unittest_data_dir"] / "pcd-example-notThem.json"
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
    assert inst.authority[0].display == "Canada Infoway"
    assert inst.authority[0].reference == "Organization/Infoway"
    assert inst.domain[0].display == "Canada Infoway"
    assert inst.domain[0].reference == "Location/Infoway"
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
    assert inst.subType[0].coding[0].code == "Opt-In"
    assert inst.subType[0].coding[0].display == "Default Authorization with exceptions."
    assert (
        inst.subType[0].coding[0].system
        == "http://www.infoway-inforoute.ca.org/Consent-subtype-codes"
    )
    assert inst.subject[0].display == "P. van de Heuvel"
    assert inst.subject[0].reference == "Patient/f001"
    assert inst.term[0].text == "Withhold all data authored by Good Health provider."
    assert inst.term[0].topic[0].display == "Good Health Clinic"
    assert inst.term[0].topic[0].reference == "Organization/2.16.840.1.113883.19.5"
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


def test_contract_5(base_settings):
    """No. 5 tests collection for Contract.
    Test File: pcd-example-notAuthor.json
    """
    filename = base_settings["unittest_data_dir"] / "pcd-example-notAuthor.json"
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
    assert inst.id == "C-123"
    assert inst.identifier.system == "http://happyvalley.com/contract"
    assert inst.identifier.value == "12347"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the contract</div>"
    )
    assert inst.text.status == "generated"


def test_contract_6(base_settings):
    """No. 6 tests collection for Contract.
    Test File: contract-example.json
    """
    filename = base_settings["unittest_data_dir"] / "contract-example.json"
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
    assert inst.authority[0].display == "Canada Infoway"
    assert inst.authority[0].reference == "Organization/Infoway"
    assert inst.domain[0].display == "Canada Infoway"
    assert inst.domain[0].reference == "Location/Infoway"
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
    assert inst.subType[0].coding[0].code == "Opt-In"
    assert inst.subType[0].coding[0].display == "Default Authorization with exceptions."
    assert (
        inst.subType[0].coding[0].system
        == "http://www.infoway-inforoute.ca.org/Consent-subtype-codes"
    )
    assert inst.subject[0].display == "P. van de Heuvel"
    assert inst.subject[0].reference == "Patient/f001"
    assert inst.term[0].text == (
        "Withhold this order and any results or related objects from " "any provider."
    )
    assert inst.term[0].topic[0].reference == "ProcedureRequest/example-lipid"
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


def test_contract_7(base_settings):
    """No. 7 tests collection for Contract.
    Test File: pcd-example-notThis.json
    """
    filename = base_settings["unittest_data_dir"] / "pcd-example-notThis.json"
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
