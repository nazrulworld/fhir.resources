# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AllergyIntolerance
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import allergyintolerance


def impl_allergyintolerance_1(inst):
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].display == "Active"
    assert inst.clinicalStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "clinical"
    )
    assert inst.code.coding[0].code == "716184000"
    assert inst.code.coding[0].display == "No Known Latex Allergy (situation)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "No Known Latex Allergy"
    assert inst.id == "nkla"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.recordedDate == fhirtypes.DateTime.validate("2015-08-06T15:37:31-06:00")
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].display == "Confirmed"
    assert inst.verificationStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "verification"
    )


def test_allergyintolerance_1(base_settings):
    """No. 1 tests collection for AllergyIntolerance.
    Test File: allergyintolerance-nkla.json
    """
    filename = base_settings["unittest_data_dir"] / "allergyintolerance-nkla.json"
    inst = allergyintolerance.AllergyIntolerance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AllergyIntolerance" == inst.resource_type

    impl_allergyintolerance_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AllergyIntolerance" == data["resourceType"]

    inst2 = allergyintolerance.AllergyIntolerance(**data)
    impl_allergyintolerance_1(inst2)


def impl_allergyintolerance_2(inst):
    assert inst.asserter.reference == "Patient/example"
    assert inst.category[0] == "food"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].display == "Active"
    assert inst.clinicalStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "clinical"
    )
    assert inst.code.coding[0].code == "227493005"
    assert inst.code.coding[0].display == "Cashew nuts"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.criticality == "high"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://acme.com/ids/patients/risks"
    assert inst.identifier[0].value == "49476534"
    assert inst.lastOccurrence == fhirtypes.DateTime.validate("2012-06")
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].text == (
        "The criticality is high becasue of the observed anaphylactic"
        " reaction when challenged with cashew extract."
    )
    assert inst.onsetDateTime == fhirtypes.DateTime.validate("2004")
    assert inst.patient.reference == "Patient/example"
    assert inst.reaction[0].description == (
        "Challenge Protocol. Severe reaction to subcutaneous cashew "
        "extract. Epinephrine administered"
    )
    assert inst.reaction[0].exposureRoute.coding[0].code == "34206005"
    assert inst.reaction[0].exposureRoute.coding[0].display == "Subcutaneous route"
    assert inst.reaction[0].exposureRoute.coding[0].system == "http://snomed.info/sct"
    assert inst.reaction[0].manifestation[0].coding[0].code == "39579001"
    assert (
        inst.reaction[0].manifestation[0].coding[0].display == "Anaphylactic reaction"
    )
    assert (
        inst.reaction[0].manifestation[0].coding[0].system == "http://snomed.info/sct"
    )
    assert inst.reaction[0].onset == fhirtypes.DateTime.validate("2012-06-12")
    assert inst.reaction[0].severity == "severe"
    assert inst.reaction[0].substance.coding[0].code == "1160593"
    assert (
        inst.reaction[0].substance.coding[0].display
        == "cashew nut allergenic extract Injectable Product"
    )
    assert (
        inst.reaction[0].substance.coding[0].system
        == "http://www.nlm.nih.gov/research/umls/rxnorm"
    )
    assert inst.reaction[1].manifestation[0].coding[0].code == "64305001"
    assert inst.reaction[1].manifestation[0].coding[0].display == "Urticaria"
    assert (
        inst.reaction[1].manifestation[0].coding[0].system == "http://snomed.info/sct"
    )
    assert inst.reaction[1].note[0].text == (
        "The patient reports that the onset of urticaria was within "
        "15 minutes of eating cashews."
    )
    assert inst.reaction[1].onset == fhirtypes.DateTime.validate("2004")
    assert inst.reaction[1].severity == "moderate"
    assert inst.recordedDate == fhirtypes.DateTime.validate("2014-10-09T14:58:00+11:00")
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.text.status == "generated"
    assert inst.type == "allergy"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].display == "Confirmed"
    assert inst.verificationStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "verification"
    )


def test_allergyintolerance_2(base_settings):
    """No. 2 tests collection for AllergyIntolerance.
    Test File: allergyintolerance-example.json
    """
    filename = base_settings["unittest_data_dir"] / "allergyintolerance-example.json"
    inst = allergyintolerance.AllergyIntolerance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AllergyIntolerance" == inst.resource_type

    impl_allergyintolerance_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AllergyIntolerance" == data["resourceType"]

    inst2 = allergyintolerance.AllergyIntolerance(**data)
    impl_allergyintolerance_2(inst2)


def impl_allergyintolerance_3(inst):
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].display == "Active"
    assert inst.clinicalStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "clinical"
    )
    assert inst.code.coding[0].code == "716186003"
    assert inst.code.coding[0].display == "No Known Allergy (situation)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "NKA"
    assert inst.id == "nka"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/mom"
    assert inst.recordedDate == fhirtypes.DateTime.validate("2015-08-06T15:37:31-06:00")
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].display == "Confirmed"
    assert inst.verificationStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "verification"
    )


def test_allergyintolerance_3(base_settings):
    """No. 3 tests collection for AllergyIntolerance.
    Test File: allergyintolerance-nka.json
    """
    filename = base_settings["unittest_data_dir"] / "allergyintolerance-nka.json"
    inst = allergyintolerance.AllergyIntolerance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AllergyIntolerance" == inst.resource_type

    impl_allergyintolerance_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AllergyIntolerance" == data["resourceType"]

    inst2 = allergyintolerance.AllergyIntolerance(**data)
    impl_allergyintolerance_3(inst2)


def impl_allergyintolerance_4(inst):
    assert inst.category[0] == "medication"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].display == "Active"
    assert inst.clinicalStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "clinical"
    )
    assert inst.code.coding[0].code == "7980"
    assert inst.code.coding[0].display == "Penicillin G"
    assert inst.code.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.criticality == "high"
    assert inst.id == "medication"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.reaction[0].manifestation[0].coding[0].code == "247472004"
    assert inst.reaction[0].manifestation[0].coding[0].display == "Hives"
    assert (
        inst.reaction[0].manifestation[0].coding[0].system == "http://snomed.info/sct"
    )
    assert inst.recordedDate == fhirtypes.DateTime.validate("2010-03-01")
    assert inst.recorder.reference == "Practitioner/13"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "unconfirmed"
    assert inst.verificationStatus.coding[0].display == "Unconfirmed"
    assert inst.verificationStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "verification"
    )


def test_allergyintolerance_4(base_settings):
    """No. 4 tests collection for AllergyIntolerance.
    Test File: allergyintolerance-medication.json
    """
    filename = base_settings["unittest_data_dir"] / "allergyintolerance-medication.json"
    inst = allergyintolerance.AllergyIntolerance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AllergyIntolerance" == inst.resource_type

    impl_allergyintolerance_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AllergyIntolerance" == data["resourceType"]

    inst2 = allergyintolerance.AllergyIntolerance(**data)
    impl_allergyintolerance_4(inst2)


def impl_allergyintolerance_5(inst):
    assert inst.category[0] == "food"
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].display == "Active"
    assert inst.clinicalStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "clinical"
    )
    assert inst.code.coding[0].code == "227037002"
    assert inst.code.coding[0].display == "Fish - dietary (substance)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Allergic to fresh fish. Tolerates canned fish"
    assert inst.id == "fishallergy"
    assert inst.identifier[0].system == "http://acme.com/ids/patients/risks"
    assert inst.identifier[0].value == "49476535"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.recordedDate == fhirtypes.DateTime.validate("2015-08-06T15:37:31-06:00")
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.text.status == "additional"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].display == "Confirmed"
    assert inst.verificationStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "verification"
    )


def test_allergyintolerance_5(base_settings):
    """No. 5 tests collection for AllergyIntolerance.
    Test File: allergyintolerance-fishallergy.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "allergyintolerance-fishallergy.json"
    )
    inst = allergyintolerance.AllergyIntolerance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AllergyIntolerance" == inst.resource_type

    impl_allergyintolerance_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AllergyIntolerance" == data["resourceType"]

    inst2 = allergyintolerance.AllergyIntolerance(**data)
    impl_allergyintolerance_5(inst2)


def impl_allergyintolerance_6(inst):
    assert inst.clinicalStatus.coding[0].code == "active"
    assert inst.clinicalStatus.coding[0].display == "Active"
    assert inst.clinicalStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "clinical"
    )
    assert inst.code.coding[0].code == "409137002"
    assert inst.code.coding[0].display == "No Known Drug Allergy (situation)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "NKDA"
    assert inst.id == "nkda"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/mom"
    assert inst.recordedDate == fhirtypes.DateTime.validate("2015-08-06T15:37:31-06:00")
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.text.status == "generated"
    assert inst.verificationStatus.coding[0].code == "confirmed"
    assert inst.verificationStatus.coding[0].display == "Confirmed"
    assert inst.verificationStatus.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/allergyintolerance-" "verification"
    )


def test_allergyintolerance_6(base_settings):
    """No. 6 tests collection for AllergyIntolerance.
    Test File: allergyintolerance-nkda.json
    """
    filename = base_settings["unittest_data_dir"] / "allergyintolerance-nkda.json"
    inst = allergyintolerance.AllergyIntolerance.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AllergyIntolerance" == inst.resource_type

    impl_allergyintolerance_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AllergyIntolerance" == data["resourceType"]

    inst2 = allergyintolerance.AllergyIntolerance(**data)
    impl_allergyintolerance_6(inst2)
