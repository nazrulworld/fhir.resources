# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Consent
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import consent
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_consent_1(inst):
    assert inst.category[0].coding[0].code == "59284-0"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.controller[0].reference == "Organization/f001"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate({"valueDate": "2018-12-28"}).valueDate
    )
    assert inst.decision == "permit"
    assert inst.id == "consent-example-notThis"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.provision[0].data[0].meaning == "related"
    assert (
        inst.provision[0].data[0].reference.reference == "MedicationRequest/medrx0305"
    )
    assert inst.regulatoryBasis[0].coding[0].code == "INFA"
    assert (
        inst.regulatoryBasis[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.sourceAttachment[0].title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_consent_1(base_settings):
    """No. 1 tests collection for Consent.
    Test File: consent-example-notThis.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-notThis.json"
    inst = consent.Consent.model_validate_json(filename.read_bytes())
    assert "Consent" == inst.get_resource_type()

    impl_consent_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_1(inst2)


def impl_consent_2(inst):
    assert inst.category[0].coding[0].code == "59284-0"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.controller[0].reference == "Organization/f001"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate({"valueDate": "2016-06-23"}).valueDate
    )
    assert inst.decision == "permit"
    assert inst.grantor[0].reference == "RelatedPerson/peter"
    assert inst.id == "consent-example-smartonfhir"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.provision[0].period.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-06-23T17:32:33+10:00"}
        ).valueDateTime
    )
    assert (
        inst.provision[0].period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-06-23T17:02:33+10:00"}
        ).valueDateTime
    )
    assert inst.provision[0].provision[0].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].provision[0].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert inst.provision[0].provision[0].action[1].coding[0].code == "correct"
    assert (
        inst.provision[0].provision[0].action[1].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert inst.regulatoryBasis[0].coding[0].code == "INFA"
    assert (
        inst.regulatoryBasis[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.status == "generated"


def test_consent_2(base_settings):
    """No. 2 tests collection for Consent.
    Test File: consent-example-smartonfhir.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-smartonfhir.json"
    inst = consent.Consent.model_validate_json(filename.read_bytes())
    assert "Consent" == inst.get_resource_type()

    impl_consent_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_2(inst2)


def impl_consent_3(inst):
    assert inst.category[0].coding[0].code == "npp"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentcategorycodes"}
        ).valueUri
    )
    assert inst.controller[0].reference == "Organization/f001"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate({"valueDate": "2018-12-28"}).valueDate
    )
    assert inst.decision == "permit"
    assert inst.grantee[0].reference == "Patient/pat2"
    assert inst.id == "consent-example-CDA"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:2.16.840.1.113883.3.72.5.9.1"}
        ).valueUri
    )
    assert inst.identifier[0].value == "494e0c7a-a69e-4fb4-9d02-6aae747790d7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.provision[0].actor[0].reference.reference == "Practitioner/f001"
    assert inst.provision[0].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert (
        inst.provision[0].period.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-10"}
        ).valueDateTime
    )
    assert (
        inst.provision[0].period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2018-10-10"}
        ).valueDateTime
    )
    assert (
        inst.provision[0].provision[0].actor[0].reference.reference
        == "Practitioner/xcda-author"
    )
    assert inst.provision[0].provision[0].actor[0].role.coding[0].code == "AUT"
    assert (
        inst.provision[0].provision[0].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[0].code[0].coding[0].code == "34133-9"
    assert (
        inst.provision[0].provision[0].code[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.provision[0].provision[0].code[1].coding[0].code == "18842-5"
    assert (
        inst.provision[0].provision[0].code[1].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert (
        inst.provision[0].provision[0].documentType[0].code == "application/hl7-cda+xml"
    )
    assert (
        inst.provision[0].provision[0].documentType[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:bcp:13"}
        ).valueUri
    )
    assert inst.regulatoryBasis[0].coding[0].code == "INFA"
    assert (
        inst.regulatoryBasis[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.sourceReference[0].reference == "Contract/pcd-example-notAuthor"
    assert inst.status == "active"
    assert inst.subject.reference == "Patient/pat2"
    assert inst.text.status == "generated"


def test_consent_3(base_settings):
    """No. 3 tests collection for Consent.
    Test File: consent-example-CDA.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-CDA.json"
    inst = consent.Consent.model_validate_json(filename.read_bytes())
    assert "Consent" == inst.get_resource_type()

    impl_consent_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_3(inst2)


def impl_consent_4(inst):
    assert inst.category[0].coding[0].code == "59284-0"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.controller[0].reference == "Organization/f001"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate({"valueDate": "2015-11-18"}).valueDate
    )
    assert inst.decision == "permit"
    assert inst.id == "consent-example-notAuthor"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.provision[0].actor[0].reference.reference == "Organization/f001"
    assert inst.provision[0].actor[0].role.coding[0].code == "CST"
    assert (
        inst.provision[0].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.regulatoryBasis[0].coding[0].code == "INFA"
    assert (
        inst.regulatoryBasis[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.sourceAttachment[0].title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_consent_4(base_settings):
    """No. 4 tests collection for Consent.
    Test File: consent-example-notAuthor.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-notAuthor.json"
    inst = consent.Consent.model_validate_json(filename.read_bytes())
    assert "Consent" == inst.get_resource_type()

    impl_consent_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_4(inst2)


def impl_consent_5(inst):
    assert inst.category[0].coding[0].code == "59284-0"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.controller[0].reference == "Organization/f001"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate({"valueDate": "2018-12-28"}).valueDate
    )
    assert inst.decision == "permit"
    assert inst.id == "consent-example-notTime"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.provision[0].period.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-02-01"}
        ).valueDateTime
    )
    assert (
        inst.provision[0].period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-01-01"}
        ).valueDateTime
    )
    assert inst.regulatoryBasis[0].coding[0].code == "INFA"
    assert (
        inst.regulatoryBasis[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.sourceAttachment[0].title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_consent_5(base_settings):
    """No. 5 tests collection for Consent.
    Test File: consent-example-notTime.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-notTime.json"
    inst = consent.Consent.model_validate_json(filename.read_bytes())
    assert "Consent" == inst.get_resource_type()

    impl_consent_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_5(inst2)


def impl_consent_6(inst):
    assert inst.category[0].coding[0].code == "59284-0"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.controller[0].reference == "Organization/f001"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate({"valueDate": "2018-12-24"}).valueDate
    )
    assert inst.decision == "permit"
    assert inst.id == "consent-example-notThem"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.provision[0].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert inst.provision[0].action[1].coding[0].code == "correct"
    assert (
        inst.provision[0].action[1].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert inst.provision[0].actor[0].reference.display == "Carla Espinosa"
    assert inst.provision[0].actor[0].reference.reference == "Practitioner/f204"
    assert inst.provision[0].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.regulatoryBasis[0].coding[0].code == "INFA"
    assert (
        inst.regulatoryBasis[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.sourceAttachment[0].title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.subject.display == "Eve Everywoman"
    assert inst.subject.reference == "Patient/mom"
    assert inst.text.status == "generated"
    assert (
        inst.verification[0].verificationDate[0]
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2021-11-11"}
        ).valueDateTime
    )
    assert inst.verification[0].verified is True
    assert inst.verification[0].verifiedBy.reference == "Organization/f001"
    assert inst.verification[0].verifiedWith.reference == "RelatedPerson/benedicte"


def test_consent_6(base_settings):
    """No. 6 tests collection for Consent.
    Test File: consent-example-notThem.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-notThem.json"
    inst = consent.Consent.model_validate_json(filename.read_bytes())
    assert "Consent" == inst.get_resource_type()

    impl_consent_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_6(inst2)


def impl_consent_7(inst):
    assert inst.category[0].coding[0].code == "INFAO"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.controller[0].reference == "Organization/f203"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate({"valueDate": "2018-12-24"}).valueDate
    )
    assert inst.decision == "deny"
    assert inst.grantee[0].display == "Simone Heps"
    assert inst.grantee[0].reference == "Practitioner/f007"
    assert inst.grantor[0].reference == "Patient/pat1"
    assert inst.id == "consent-example-grantor"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.provision[0].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert inst.provision[0].actor[0].reference.reference == "Organization/f203"
    assert inst.provision[0].actor[0].role.coding[0].code == "CST"
    assert (
        inst.provision[0].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].actor[1].reference.display == "Simone Heps"
    assert inst.provision[0].actor[1].reference.reference == "Practitioner/f007"
    assert inst.provision[0].actor[1].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].actor[1].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.regulatoryBasis[0].coding[0].code == "INFAO"
    assert (
        inst.regulatoryBasis[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.sourceAttachment[0].title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.subject.display == "Roel"
    assert inst.subject.reference == "Patient/f201"
    assert inst.text.status == "generated"


def test_consent_7(base_settings):
    """No. 7 tests collection for Consent.
    Test File: consent-example-grantor.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-grantor.json"
    inst = consent.Consent.model_validate_json(filename.read_bytes())
    assert "Consent" == inst.get_resource_type()

    impl_consent_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_7(inst2)


def impl_consent_8(inst):
    assert inst.category[0].coding[0].code == "59284-0"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.controller[0].reference == "Organization/2.16.840.1.113883.19.5"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate({"valueDate": "2018-12-24"}).valueDate
    )
    assert inst.decision == "permit"
    assert inst.id == "consent-example-notOrg"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.provision[0].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert inst.provision[0].action[1].coding[0].code == "correct"
    assert (
        inst.provision[0].action[1].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert inst.provision[0].actor[0].reference.reference == "Organization/f001"
    assert inst.provision[0].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.regulatoryBasis[0].coding[0].code == "INFA"
    assert (
        inst.regulatoryBasis[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.sourceAttachment[0].title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.subject.display == "P. van de Heuvel"
    assert inst.subject.reference == "Patient/f001"
    assert inst.text.status == "generated"


def test_consent_8(base_settings):
    """No. 8 tests collection for Consent.
    Test File: consent-example-notOrg.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-notOrg.json"
    inst = consent.Consent.model_validate_json(filename.read_bytes())
    assert "Consent" == inst.get_resource_type()

    impl_consent_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_8(inst2)


def impl_consent_9(inst):
    assert inst.category[0].coding[0].code == "59284-0"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.controller[0].reference == "Organization/f001"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate({"valueDate": "2018-12-28"}).valueDate
    )
    assert inst.decision == "deny"
    assert inst.id == "consent-example-pkb"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.provision[0].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert inst.provision[0].actor[0].reference.reference == "Organization/f001"
    assert inst.provision[0].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[0].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].provision[0].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert (
        inst.provision[0].provision[0].actor[0].reference.reference
        == "Organization/f001"
    )
    assert inst.provision[0].provision[0].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].provision[0].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[0].securityLabel[0].code == "PSY"
    assert (
        inst.provision[0].provision[0].securityLabel[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.provision[0].provision[1].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].provision[1].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert (
        inst.provision[0].provision[1].actor[0].reference.reference
        == "Organization/f001"
    )
    assert inst.provision[0].provision[1].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].provision[1].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[1].securityLabel[0].code == "SPI"
    assert (
        inst.provision[0].provision[1].securityLabel[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.provision[0].provision[2].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].provision[2].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert (
        inst.provision[0].provision[2].actor[0].reference.reference
        == "Organization/f001"
    )
    assert inst.provision[0].provision[2].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].provision[2].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[2].securityLabel[0].code == "N"
    assert (
        inst.provision[0].provision[2].securityLabel[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"}
        ).valueUri
    )
    assert inst.provision[0].provision[3].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].provision[3].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert (
        inst.provision[0].provision[3].actor[0].reference.reference
        == "Organization/f001"
    )
    assert inst.provision[0].provision[3].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].provision[3].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[3].securityLabel[0].code == "PSY"
    assert (
        inst.provision[0].provision[3].securityLabel[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.provision[0].provision[4].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].provision[4].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert (
        inst.provision[0].provision[4].actor[0].reference.reference
        == "Organization/f001"
    )
    assert inst.provision[0].provision[4].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].provision[4].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[4].securityLabel[0].code == "SPI"
    assert (
        inst.provision[0].provision[4].securityLabel[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.provision[0].provision[5].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].provision[5].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert (
        inst.provision[0].provision[5].actor[0].reference.reference
        == "Organization/f001"
    )
    assert inst.provision[0].provision[5].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].provision[5].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[5].securityLabel[0].code == "SEX"
    assert (
        inst.provision[0].provision[5].securityLabel[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.provision[0].provision[6].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].provision[6].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert (
        inst.provision[0].provision[6].actor[0].reference.reference
        == "Organization/f001"
    )
    assert inst.provision[0].provision[6].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].provision[6].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[6].securityLabel[0].code == "N"
    assert (
        inst.provision[0].provision[6].securityLabel[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"}
        ).valueUri
    )
    assert inst.provision[0].provision[7].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].provision[7].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert (
        inst.provision[0].provision[7].actor[0].reference.reference
        == "Organization/f001"
    )
    assert inst.provision[0].provision[7].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].provision[7].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[7].securityLabel[0].code == "PSY"
    assert (
        inst.provision[0].provision[7].securityLabel[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.provision[0].provision[8].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].provision[8].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert (
        inst.provision[0].provision[8].actor[0].reference.reference
        == "Organization/f001"
    )
    assert inst.provision[0].provision[8].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].provision[8].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[8].securityLabel[0].code == "SPI"
    assert (
        inst.provision[0].provision[8].securityLabel[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.provision[0].provision[9].action[0].coding[0].code == "access"
    assert (
        inst.provision[0].provision[9].action[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/consentaction"}
        ).valueUri
    )
    assert (
        inst.provision[0].provision[9].actor[0].reference.reference
        == "Organization/f001"
    )
    assert inst.provision[0].provision[9].actor[0].role.coding[0].code == "PRCP"
    assert (
        inst.provision[0].provision[9].actor[0].role.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"}
        ).valueUri
    )
    assert inst.provision[0].provision[9].securityLabel[0].code == "SEX"
    assert (
        inst.provision[0].provision[9].securityLabel[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.provision[0].securityLabel[0].code == "N"
    assert (
        inst.provision[0].securityLabel[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"}
        ).valueUri
    )
    assert inst.regulatoryBasis[0].coding[0].code == "INFA"
    assert (
        inst.regulatoryBasis[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_consent_9(base_settings):
    """No. 9 tests collection for Consent.
    Test File: consent-example-pkb.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example-pkb.json"
    inst = consent.Consent.model_validate_json(filename.read_bytes())
    assert "Consent" == inst.get_resource_type()

    impl_consent_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_9(inst2)


def impl_consent_10(inst):
    assert inst.category[0].coding[0].code == "59284-0"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.controller[0].reference == "Organization/f001"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate({"valueDate": "2018-12-28"}).valueDate
    )
    assert inst.decision == "deny"
    assert inst.id == "consent-example-basic"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.provision[0].period.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-01-01"}
        ).valueDateTime
    )
    assert (
        inst.provision[0].period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "1964-01-01"}
        ).valueDateTime
    )
    assert inst.regulatoryBasis[0].coding[0].code == "INFA"
    assert (
        inst.regulatoryBasis[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActCode"}
        ).valueUri
    )
    assert inst.sourceAttachment[0].title == "The terms of the consent in lawyer speak."
    assert inst.status == "active"
    assert inst.subject.display == "Peter James Chalmers"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_consent_10(base_settings):
    """No. 10 tests collection for Consent.
    Test File: consent-example.json
    """
    filename = base_settings["unittest_data_dir"] / "consent-example.json"
    inst = consent.Consent.model_validate_json(filename.read_bytes())
    assert "Consent" == inst.get_resource_type()

    impl_consent_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Consent" == data["resourceType"]

    inst2 = consent.Consent(**data)
    impl_consent_10(inst2)
