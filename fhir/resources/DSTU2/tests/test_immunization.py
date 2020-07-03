# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Immunization
Release: DSTU2
Version: 1.0.2
Revision: 7202
"""
from .. import fhirtypes  # noqa: F401
from .. import immunization


def testImmunization1(base_settings):
    filename = base_settings["unittest_data_dir"] / "immunization-example-refused.json"
    inst = immunization.Immunization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Immunization" == inst.resource_type
    impl_Immunization_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_Immunization_1(inst2)


def impl_Immunization_1(inst):

    assert inst.date == fhirtypes.Date.validate("2013-01-10")
    assert inst.explanation.reasonNotGiven[0].coding[0].code == "MEDPREC"
    assert inst.explanation.reasonNotGiven[0].coding[0].display == (
        "medical precaution"
    )
    assert inst.explanation.reasonNotGiven[0].coding[0].system == (
        "http://hl7.org/fhir/v3/ActReason"
    )
    assert inst.id == "notGiven"
    assert inst.reported is False
    assert inst.status == "completed"
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "01"
    assert inst.vaccineCode.coding[0].display == "DTP"
    assert inst.vaccineCode.coding[0].system == "http://hl7.org/fhir/sid/cvx"
    assert inst.wasNotGiven is True


def test_Immunization_2(base_settings):
    filename = base_settings["unittest_data_dir"] / "immunization-example.json"
    inst = immunization.Immunization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Immunization" == inst.resource_type
    impl_Immunization_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_Immunization_2(inst2)


def impl_Immunization_2(inst):
    assert inst.date == fhirtypes.Date.validate("2013-01-10")

    assert inst.doseQuantity.code == "mg"
    assert inst.doseQuantity.system == "http://unitsofmeasure.org"
    assert inst.doseQuantity.value == 5
    assert inst.expirationDate == fhirtypes.Date.validate("2015-02-15")

    assert inst.explanation.reason[0].coding[0].code == "429060002"
    assert inst.explanation.reason[0].coding[0].system == "http://snomed.info/sct"
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.lotNumber == "AAJN11K"
    assert inst.note[0].text == "Notes on adminstration of vaccine"
    assert inst.reaction[0].date == fhirtypes.Date.validate("2013-01-10")

    assert inst.reaction[0].reported is True
    assert inst.reported is False
    assert inst.route.coding[0].code == "IM"
    assert inst.route.coding[0].display == "Injection, intramuscular"
    assert inst.route.coding[0].system == (
        "http://hl7.org/fhir/v3/RouteOfAdministration"
    )
    assert inst.site.coding[0].code == "LA"
    assert inst.site.coding[0].display == "left arm"
    assert inst.site.coding[0].system == "http://hl7.org/fhir/v3/ActSite"
    assert inst.status == "completed"
    assert inst.text.status == "generated"
    assert inst.vaccinationProtocol[0].description == (
        "Vaccination Protocol Sequence 1"
    )
    assert inst.vaccinationProtocol[0].doseSequence == 1
    assert inst.vaccinationProtocol[0].doseStatus.coding[0].code == "count"
    assert inst.vaccinationProtocol[0].doseStatus.coding[0].display == "Counts"

    assert inst.vaccinationProtocol[0].doseStatus.coding[0].system == (
        "http://hl7.org/fhir/vaccination-protocol-dose-status"
    )
    assert inst.vaccinationProtocol[0].doseStatusReason.coding[0].code == "coldchbrk"

    assert inst.vaccinationProtocol[0].doseStatusReason.coding[0].display == (
        "Cold chain break"
    )
    assert inst.vaccinationProtocol[0].doseStatusReason.coding[0].system == (
        "http://hl7.org/fhir/vaccination-protocol-dose-status-reason"
    )
    assert inst.vaccinationProtocol[0].series == "Vaccination Series 1"
    assert inst.vaccinationProtocol[0].seriesDoses == 2
    assert inst.vaccinationProtocol[0].targetDisease[0].coding[0].code == ("1857005")
    assert inst.vaccinationProtocol[0].targetDisease[0].coding[0].system == (
        "http://snomed.info/sct"
    )
    assert inst.vaccineCode.coding[0].code == "FLUVAX"
    assert inst.vaccineCode.coding[0].system == "urn:oid:1.2.36.1.2001.1005.17"
    assert inst.vaccineCode.text == "Fluvax (Influenza)"
    assert inst.wasNotGiven is False
