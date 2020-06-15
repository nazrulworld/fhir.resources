# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Consent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import consent


def impl_consent_1(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2015-11-18")
    assert inst.except_fhir[0].data[0].meaning == "related"
    assert inst.except_fhir[0].data[0].reference.reference == "Task/f201"
    assert inst.except_fhir[0].type == "deny"
    assert inst.id == "consent-example-notThis"
    assert inst.organization[0].display == "Canada Infoway"
    assert inst.organization[0].reference == "Organization/Infoway"
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.policyRule == "http://hl7.org/fhir/ConsentPolicy/opt-in"
    assert inst.sourceAttachment.title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_consent_1(base_settings):
    """No. 1 tests collection for Consent.
    Test File: consent-example-notThis.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-notThis.json"
    inst = consent.Consent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Consent" == inst.resource_type

    impl_consent_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_1(inst2)


def impl_consent_2(inst):
    assert inst.consentingParty[0].reference == "RelatedPerson/peter"
    assert inst.dateTime == fhirtypes.DateTime.validate("2016-06-23T17:02:33+10:00")
    assert inst.except_fhir[0].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[0].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert inst.except_fhir[0].class_fhir[0].code == "MedicationRequest"
    assert (
        inst.except_fhir[0].class_fhir[0].system == "http://hl7.org/fhir/resource-types"
    )
    assert inst.except_fhir[0].type == "permit"
    assert inst.id == "consent-example-smartonfhir"
    assert inst.organization[0].reference == "Organization/example"
    assert inst.patient.reference == "Patient/xcda"
    assert inst.period.end == fhirtypes.DateTime.validate("2016-06-23T17:32:33+10:00")
    assert inst.period.start == fhirtypes.DateTime.validate("2016-06-23T17:02:33+10:00")
    assert inst.policyRule == "http://hl7.org/fhir/ConsentPolicy/opt-in"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_consent_2(base_settings):
    """No. 2 tests collection for Consent.
    Test File: consent-example-smartonfhir.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-smartonfhir.json"
    inst = consent.Consent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Consent" == inst.resource_type

    impl_consent_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_2(inst2)


def impl_consent_3(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2015-11-18")
    assert inst.except_fhir[0].actor[0].reference.display == "Good Health Clinic"
    assert (
        inst.except_fhir[0].actor[0].reference.reference
        == "Organization/2.16.840.1.113883.19.5"
    )
    assert inst.except_fhir[0].actor[0].role.coding[0].code == "CST"
    assert (
        inst.except_fhir[0].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[0].type == "deny"
    assert inst.id == "consent-example-notAuthor"
    assert inst.organization[0].display == "Canada Infoway"
    assert inst.organization[0].reference == "Organization/Infoway"
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.policyRule == "http://hl7.org/fhir/ConsentPolicy/opt-in"
    assert inst.sourceAttachment.title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_consent_3(base_settings):
    """No. 3 tests collection for Consent.
    Test File: consent-example-notAuthor.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-notAuthor.json"
    inst = consent.Consent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Consent" == inst.resource_type

    impl_consent_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_3(inst2)


def impl_consent_4(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2015-11-18")
    assert inst.except_fhir[0].period.end == fhirtypes.DateTime.validate("2015-02-01")
    assert inst.except_fhir[0].period.start == fhirtypes.DateTime.validate("2015-01-01")
    assert inst.except_fhir[0].type == "deny"
    assert inst.id == "consent-example-notTime"
    assert inst.organization[0].display == "Canada Infoway"
    assert inst.organization[0].reference == "Organization/Infoway"
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.policyRule == "http://hl7.org/fhir/ConsentPolicy/opt-in"
    assert inst.sourceAttachment.title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_consent_4(base_settings):
    """No. 4 tests collection for Consent.
    Test File: consent-example-notTime.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-notTime.json"
    inst = consent.Consent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Consent" == inst.resource_type

    impl_consent_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_4(inst2)


def impl_consent_5(inst):
    assert inst.actor[0].reference.reference == "Practitioner/13"
    assert inst.actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.category[0].coding[0].code == "HIPAA-Auth"
    assert (
        inst.category[0].coding[0].system == "http://hl7.org/fhir/consentcategorycodes"
    )
    assert inst.consentingParty[0].reference == "Patient/72"
    assert inst.dateTime == fhirtypes.DateTime.validate("2016-05-26T00:41:10-04:00")
    assert (
        inst.except_fhir[0].actor[0].reference.reference == "Practitioner/xcda-author"
    )
    assert inst.except_fhir[0].actor[0].role.coding[0].code == "AUT"
    assert (
        inst.except_fhir[0].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[0].class_fhir[0].code == "application/hl7-cda+xml"
    assert inst.except_fhir[0].class_fhir[0].system == "urn:ietf:bcp:13"
    assert inst.except_fhir[0].code[0].code == "34133-9"
    assert inst.except_fhir[0].code[0].system == "http://loinc.org"
    assert inst.except_fhir[0].code[1].code == "18842-5"
    assert inst.except_fhir[0].code[1].system == "http://loinc.org"
    assert inst.except_fhir[0].type == "permit"
    assert inst.id == "consent-example-signature"
    assert inst.identifier.system == "urn:oid:2.16.840.1.113883.3.72.5.9.1"
    assert inst.identifier.value == "494e0c7a-a69e-4fb4-9d02-6aae747790d7"
    assert inst.organization[0].reference == "Organization/example"
    assert inst.patient.reference == "Patient/72"
    assert inst.period.end == fhirtypes.DateTime.validate("2016-10-10")
    assert inst.period.start == fhirtypes.DateTime.validate("2015-10-10")
    assert inst.policyRule == "http://hl7.org/fhir/ConsentPolicy/opt-in"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_consent_5(base_settings):
    """No. 5 tests collection for Consent.
    Test File: consent-example-signature.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-signature.json"
    inst = consent.Consent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Consent" == inst.resource_type

    impl_consent_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_5(inst2)


def impl_consent_6(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2015-11-18")
    assert inst.except_fhir[0].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[0].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert inst.except_fhir[0].action[1].coding[0].code == "correct"
    assert (
        inst.except_fhir[0].action[1].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert inst.except_fhir[0].actor[0].reference.display == "Fictive Nurse"
    assert inst.except_fhir[0].actor[0].reference.reference == "Practitioner/f204"
    assert inst.except_fhir[0].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[0].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[0].type == "deny"
    assert inst.id == "consent-example-notThem"
    assert inst.organization[0].display == "Canada Infoway"
    assert inst.organization[0].reference == "Organization/Infoway"
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.policyRule == "http://hl7.org/fhir/ConsentPolicy/opt-in"
    assert inst.sourceAttachment.title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_consent_6(base_settings):
    """No. 6 tests collection for Consent.
    Test File: consent-example-notThem.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-notThem.json"
    inst = consent.Consent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Consent" == inst.resource_type

    impl_consent_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_6(inst2)


def impl_consent_7(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2015-11-18")
    assert inst.except_fhir[0].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[0].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert (
        inst.except_fhir[0].actor[0].reference.display
        == "Good Health Psychiatric Hospital"
    )
    assert (
        inst.except_fhir[0].actor[0].reference.reference
        == "Organization/2.16.840.1.113883.19.6"
    )
    assert inst.except_fhir[0].actor[0].role.coding[0].code == "CST"
    assert (
        inst.except_fhir[0].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[0].actor[1].reference.display == "Good Health Clinic"
    assert inst.except_fhir[0].actor[1].reference.reference == "Patient/example"
    assert inst.except_fhir[0].actor[1].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[0].actor[1].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[0].type == "permit"
    assert inst.id == "consent-example-grantor"
    assert inst.organization[0].display == "Canada Infoway"
    assert inst.organization[0].reference == "Organization/Infoway"
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.policyRule == "http://hl7.org/fhir/ConsentPolicy/opt-out"
    assert inst.sourceAttachment.title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_consent_7(base_settings):
    """No. 7 tests collection for Consent.
    Test File: consent-example-grantor.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-grantor.json"
    inst = consent.Consent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Consent" == inst.resource_type

    impl_consent_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_7(inst2)


def impl_consent_8(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2015-11-18")
    assert inst.except_fhir[0].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[0].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert inst.except_fhir[0].action[1].coding[0].code == "correct"
    assert (
        inst.except_fhir[0].action[1].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert inst.except_fhir[0].actor[0].reference.display == "Good Health Clinic"
    assert (
        inst.except_fhir[0].actor[0].reference.reference
        == "Organization/2.16.840.1.113883.19.5"
    )
    assert inst.except_fhir[0].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[0].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[0].type == "deny"
    assert inst.id == "consent-example-notOrg"
    assert inst.organization[0].display == "Canada Infoway"
    assert inst.organization[0].reference == "Organization/Infoway"
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.policyRule == "http://hl7.org/fhir/ConsentPolicy/opt-in"
    assert inst.sourceAttachment.title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_consent_8(base_settings):
    """No. 8 tests collection for Consent.
    Test File: consent-example-notOrg.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-notOrg.json"
    inst = consent.Consent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Consent" == inst.resource_type

    impl_consent_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_8(inst2)


def impl_consent_9(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2016-06-16")
    assert inst.except_fhir[0].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[0].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert (
        inst.except_fhir[0].actor[0].reference.display
        == "Non-migrated Team - Imperial College Healthcare"
    )
    assert inst.except_fhir[0].actor[0].reference.reference == "Organization/ich-nmt"
    assert inst.except_fhir[0].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[0].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[0].securityLabel[0].code == "N"
    assert (
        inst.except_fhir[0].securityLabel[0].system
        == "http://hl7.org/fhir/v3/Confidentiality"
    )
    assert inst.except_fhir[0].type == "permit"
    assert inst.except_fhir[1].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[1].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert (
        inst.except_fhir[1].actor[0].reference.display
        == "Non-migrated Team - Imperial College Healthcare"
    )
    assert inst.except_fhir[1].actor[0].reference.reference == "Organization/ich-nmt"
    assert inst.except_fhir[1].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[1].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[1].securityLabel[0].code == "PSY"
    assert (
        inst.except_fhir[1].securityLabel[0].system == "http://hl7.org/fhir/v3/ActCode"
    )
    assert inst.except_fhir[1].type == "permit"
    assert inst.except_fhir[2].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[2].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert (
        inst.except_fhir[2].actor[0].reference.display
        == "Non-migrated Team - Imperial College Healthcare"
    )
    assert inst.except_fhir[2].actor[0].reference.reference == "Organization/ich-nmt"
    assert inst.except_fhir[2].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[2].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[2].securityLabel[0].code == "SOC"
    assert (
        inst.except_fhir[2].securityLabel[0].system == "http://hl7.org/fhir/v3/ActCode"
    )
    assert inst.except_fhir[2].type == "permit"
    assert inst.except_fhir[3].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[3].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert (
        inst.except_fhir[3].actor[0].reference.display
        == "Core Information Exchange team - Imperial College Healthcare"
    )
    assert inst.except_fhir[3].actor[0].reference.reference == "Organization/ich-core"
    assert inst.except_fhir[3].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[3].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[3].securityLabel[0].code == "N"
    assert (
        inst.except_fhir[3].securityLabel[0].system
        == "http://hl7.org/fhir/v3/Confidentiality"
    )
    assert inst.except_fhir[3].type == "permit"
    assert inst.except_fhir[4].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[4].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert (
        inst.except_fhir[4].actor[0].reference.display
        == "Core Information Exchange team - Imperial College Healthcare"
    )
    assert inst.except_fhir[4].actor[0].reference.reference == "Organization/ich-core"
    assert inst.except_fhir[4].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[4].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[4].securityLabel[0].code == "PSY"
    assert (
        inst.except_fhir[4].securityLabel[0].system == "http://hl7.org/fhir/v3/ActCode"
    )
    assert inst.except_fhir[4].type == "permit"
    assert inst.except_fhir[5].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[5].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert (
        inst.except_fhir[5].actor[0].reference.display
        == "Core Information Exchange team - Imperial College Healthcare"
    )
    assert inst.except_fhir[5].actor[0].reference.reference == "Organization/ich-core"
    assert inst.except_fhir[5].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[5].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[5].securityLabel[0].code == "SOC"
    assert (
        inst.except_fhir[5].securityLabel[0].system == "http://hl7.org/fhir/v3/ActCode"
    )
    assert inst.except_fhir[5].type == "permit"
    assert inst.except_fhir[6].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[6].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert (
        inst.except_fhir[6].actor[0].reference.display
        == "Core Information Exchange team - Imperial College Healthcare"
    )
    assert inst.except_fhir[6].actor[0].reference.reference == "Organization/ich-core"
    assert inst.except_fhir[6].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[6].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[6].securityLabel[0].code == "SEX"
    assert (
        inst.except_fhir[6].securityLabel[0].system == "http://hl7.org/fhir/v3/ActCode"
    )
    assert inst.except_fhir[6].type == "permit"
    assert inst.except_fhir[7].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[7].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert (
        inst.except_fhir[7].actor[0].reference.display
        == "Torbay and Source Devon Trust - Parkinson's Team"
    )
    assert inst.except_fhir[7].actor[0].reference.reference == "Organization/tsd-park"
    assert inst.except_fhir[7].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[7].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[7].securityLabel[0].code == "N"
    assert (
        inst.except_fhir[7].securityLabel[0].system
        == "http://hl7.org/fhir/v3/Confidentiality"
    )
    assert inst.except_fhir[7].type == "permit"
    assert inst.except_fhir[8].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[8].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert (
        inst.except_fhir[8].actor[0].reference.display
        == "Torbay and Source Devon Trust - Parkinson's Team"
    )
    assert inst.except_fhir[8].actor[0].reference.reference == "Organization/tsd-park"
    assert inst.except_fhir[8].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[8].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[8].securityLabel[0].code == "PSY"
    assert (
        inst.except_fhir[8].securityLabel[0].system == "http://hl7.org/fhir/v3/ActCode"
    )
    assert inst.except_fhir[8].type == "permit"
    assert inst.except_fhir[9].action[0].coding[0].code == "access"
    assert (
        inst.except_fhir[9].action[0].coding[0].system
        == "http://hl7.org/fhir/consentaction"
    )
    assert (
        inst.except_fhir[9].actor[0].reference.display
        == "Torbay and Source Devon Trust - Parkinson's Team"
    )
    assert inst.except_fhir[9].actor[0].reference.reference == "Organization/tsd-park"
    assert inst.except_fhir[9].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.except_fhir[9].actor[0].role.coding[0].system
        == "http://hl7.org/fhir/v3/ParticipationType"
    )
    assert inst.except_fhir[9].securityLabel[0].code == "SOC"
    assert (
        inst.except_fhir[9].securityLabel[0].system == "http://hl7.org/fhir/v3/ActCode"
    )
    assert inst.except_fhir[9].type == "permit"
    assert inst.id == "consent-example-pkb"
    assert inst.organization[0].display == "Patients Know Best"
    assert inst.organization[0].reference == "Organization/pkb"
    assert inst.patient.display == "...example patient..."
    assert inst.patient.reference == "Patient/example"
    assert inst.policyRule == "http://hl7.org/fhir/ConsentPolicy/opt-out"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_consent_9(base_settings):
    """No. 9 tests collection for Consent.
    Test File: consent-example-pkb.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-pkb.json"
    inst = consent.Consent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Consent" == inst.resource_type

    impl_consent_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_9(inst2)


def impl_consent_10(inst):
    assert inst.dateTime == fhirtypes.DateTime.validate("2016-05-11")
    assert inst.id == "consent-example-basic"
    assert inst.organization[0].display == "Canada Infoway"
    assert inst.organization[0].reference == "Organization/Infoway"
    assert inst.patient.display == "P. van de Heuvel"
    assert inst.patient.reference == "Patient/f001"
    assert inst.period.end == fhirtypes.DateTime.validate("2016-01-01")
    assert inst.period.start == fhirtypes.DateTime.validate("1964-01-01")
    assert inst.policyRule == "http://goodhealth.org/consent/policy/opt-in"
    assert inst.sourceAttachment.title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_consent_10(base_settings):
    """No. 10 tests collection for Consent.
    Test File: consent-example.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example.json"
    inst = consent.Consent.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Consent" == inst.resource_type

    impl_consent_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_10(inst2)
