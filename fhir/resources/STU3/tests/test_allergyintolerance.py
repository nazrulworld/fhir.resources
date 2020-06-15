# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AllergyIntolerance
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import allergyintolerance


def impl_allergyintolerance_1(inst):
    assert inst.assertedDate == fhirtypes.DateTime.validate("2014-10-09T14:58:00+11:00")
    assert inst.asserter.reference == "Patient/example"
    assert inst.category[0] == "food"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "227493005"
    assert inst.code.coding[0].display == "Cashew nuts"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.criticality == "high"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://acme.com/ids/patients/risks"
    assert inst.identifier[0].value == "49476534"
    assert inst.lastOccurrence == fhirtypes.DateTime.validate("2012-06")
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
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.text.status == "generated"
    assert inst.type == "allergy"
    assert inst.verificationStatus == "confirmed"


def test_allergyintolerance_1(base_settings):
    """No. 1 tests collection for AllergyIntolerance.
    Test File: allergyintolerance-example.json
    """
    filename = base_settings["unittest_data_dir"] / "allergyintolerance-example.json"
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
    assert inst.assertedDate == fhirtypes.DateTime.validate("2010-03-01")
    assert inst.category[0] == "medication"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "7980"
    assert inst.code.coding[0].display == "Penicillin G"
    assert inst.code.coding[0].system == "http://www.nlm.nih.gov/research/umls/rxnorm"
    assert inst.criticality == "high"
    assert inst.id == "medication"
    assert inst.patient.reference == "Patient/example"
    assert inst.reaction[0].manifestation[0].coding[0].code == "247472004"
    assert inst.reaction[0].manifestation[0].coding[0].display == "Hives"
    assert (
        inst.reaction[0].manifestation[0].coding[0].system == "http://snomed.info/sct"
    )
    assert inst.recorder.reference == "Practitioner/13"
    assert inst.text.status == "generated"
    assert inst.verificationStatus == "unconfirmed"


def test_allergyintolerance_2(base_settings):
    """No. 2 tests collection for AllergyIntolerance.
    Test File: allergyintolerance-medication.json
    """
    filename = base_settings["unittest_data_dir"] / "allergyintolerance-medication.json"
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
    assert inst.assertedDate == fhirtypes.DateTime.validate("2015-08-06T15:37:31-06:00")
    assert inst.category[0] == "food"
    assert inst.clinicalStatus == "active"
    assert inst.code.coding[0].code == "227037002"
    assert inst.code.coding[0].display == "Fish - dietary (substance)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Allergic to fresh fish. Tolerates canned fish"
    assert inst.id == "fishallergy"
    assert inst.identifier[0].system == "http://acme.com/ids/patients/risks"
    assert inst.identifier[0].value == "49476535"
    assert inst.patient.reference == "Patient/example"
    assert inst.recorder.reference == "Practitioner/example"
    assert inst.text.status == "additional"
    assert inst.verificationStatus == "confirmed"


def test_allergyintolerance_3(base_settings):
    """No. 3 tests collection for AllergyIntolerance.
    Test File: allergyintolerance-fishallergy.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "allergyintolerance-fishallergy.json"
    )
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
