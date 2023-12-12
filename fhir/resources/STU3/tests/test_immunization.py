# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Immunization
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import immunization


def impl_immunization_1(inst):
    assert inst.date == fhirtypes.DateTime.validate("2013-01-10")
    assert inst.doseQuantity.code == "mg"
    assert inst.doseQuantity.system == "http://unitsofmeasure.org"
    assert float(inst.doseQuantity.value) == float(5)
    assert inst.encounter.reference == "Encounter/example"
    assert inst.expirationDate == fhirtypes.Date.validate("2015-02-15")
    assert inst.explanation.reason[0].coding[0].code == "429060002"
    assert inst.explanation.reason[0].coding[0].system == "http://snomed.info/sct"
    assert inst.id == "example"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.location.reference == "Location/1"
    assert inst.lotNumber == "AAJN11K"
    assert inst.manufacturer.reference == "Organization/hl7"
    assert inst.notGiven is False
    assert inst.note[0].text == "Notes on adminstration of vaccine"
    assert inst.patient.reference == "Patient/example"
    assert inst.practitioner[0].actor.reference == "Practitioner/example"
    assert inst.practitioner[0].role.coding[0].code == "OP"
    assert inst.practitioner[0].role.coding[0].system == "http://hl7.org/fhir/v2/0443"
    assert inst.practitioner[1].actor.reference == "Practitioner/example"
    assert inst.practitioner[1].role.coding[0].code == "AP"
    assert inst.practitioner[1].role.coding[0].system == "http://hl7.org/fhir/v2/0443"
    assert inst.primarySource is True
    assert inst.reaction[0].date == fhirtypes.DateTime.validate("2013-01-10")
    assert inst.reaction[0].detail.reference == "Observation/example"
    assert inst.reaction[0].reported is True
    assert inst.route.coding[0].code == "IM"
    assert inst.route.coding[0].display == "Injection, intramuscular"
    assert inst.route.coding[0].system == "http://hl7.org/fhir/v3/RouteOfAdministration"
    assert inst.site.coding[0].code == "LA"
    assert inst.site.coding[0].display == "left arm"
    assert inst.site.coding[0].system == "http://hl7.org/fhir/v3/ActSite"
    assert inst.status == "completed"
    assert inst.text.status == "generated"
    assert inst.vaccinationProtocol[0].authority.reference == "Organization/hl7"
    assert inst.vaccinationProtocol[0].description == "Vaccination Protocol Sequence 1"
    assert inst.vaccinationProtocol[0].doseSequence == 1
    assert inst.vaccinationProtocol[0].doseStatus.coding[0].code == "count"
    assert inst.vaccinationProtocol[0].doseStatus.coding[0].display == "Counts"
    assert (
        inst.vaccinationProtocol[0].doseStatus.coding[0].system
        == "http://hl7.org/fhir/vaccination-protocol-dose-status"
    )
    assert inst.vaccinationProtocol[0].doseStatusReason.coding[0].code == "coldchbrk"
    assert (
        inst.vaccinationProtocol[0].doseStatusReason.coding[0].display
        == "Cold chain break"
    )
    assert (
        inst.vaccinationProtocol[0].doseStatusReason.coding[0].system
        == "http://hl7.org/fhir/vaccination-protocol-dose-status-reason"
    )
    assert inst.vaccinationProtocol[0].series == "Vaccination Series 1"
    assert inst.vaccinationProtocol[0].seriesDoses == 2
    assert inst.vaccinationProtocol[0].targetDisease[0].coding[0].code == "1857005"
    assert (
        inst.vaccinationProtocol[0].targetDisease[0].coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.vaccineCode.coding[0].code == "FLUVAX"
    assert inst.vaccineCode.coding[0].system == "urn:oid:1.2.36.1.2001.1005.17"
    assert inst.vaccineCode.text == "Fluvax (Influenza)"


def test_immunization_1(base_settings):
    """No. 1 tests collection for Immunization.
    Test File: immunization-example.json
    """
    filename = base_settings["unittest_data_dir"] / "immunization-example.json"
    inst = immunization.Immunization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Immunization" == inst.resource_type

    impl_immunization_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_1(inst2)


def impl_immunization_2(inst):
    assert inst.date == fhirtypes.DateTime.validate("2012-01-15")
    assert inst.id == "historical"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert inst.location.reference == "Location/1"
    assert inst.notGiven is False
    assert inst.note[0].text == "Notes on adminstration of a historical vaccine"
    assert inst.patient.reference == "Patient/example"
    assert inst.primarySource is False
    assert inst.reportOrigin.coding[0].code == "record"
    assert (
        inst.reportOrigin.coding[0].system == "http://hl7.org/fhir/immunization-origin"
    )
    assert inst.reportOrigin.text == "Written Record"
    assert inst.status == "completed"
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "GNFLU"
    assert inst.vaccineCode.coding[0].system == "urn:oid:1.2.36.1.2001.1005.17"
    assert inst.vaccineCode.text == "Influenza"


def test_immunization_2(base_settings):
    """No. 2 tests collection for Immunization.
    Test File: immunization-example-historical.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "immunization-example-historical.json"
    )
    inst = immunization.Immunization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Immunization" == inst.resource_type

    impl_immunization_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_2(inst2)


def impl_immunization_3(inst):
    assert inst.date == fhirtypes.DateTime.validate("2013-01-10")
    assert inst.explanation.reasonNotGiven[0].coding[0].code == "MEDPREC"
    assert inst.explanation.reasonNotGiven[0].coding[0].display == "medical precaution"
    assert (
        inst.explanation.reasonNotGiven[0].coding[0].system
        == "http://hl7.org/fhir/v3/ActReason"
    )
    assert inst.id == "notGiven"
    assert inst.notGiven is True
    assert inst.patient.reference == "Patient/example"
    assert inst.primarySource is True
    assert inst.status == "completed"
    assert inst.text.status == "generated"
    assert inst.vaccineCode.coding[0].code == "01"
    assert inst.vaccineCode.coding[0].display == "DTP"
    assert inst.vaccineCode.coding[0].system == "http://hl7.org/fhir/sid/cvx"


def test_immunization_3(base_settings):
    """No. 3 tests collection for Immunization.
    Test File: immunization-example-refused.json
    """
    filename = base_settings["unittest_data_dir"] / "immunization-example-refused.json"
    inst = immunization.Immunization.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Immunization" == inst.resource_type

    impl_immunization_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Immunization" == data["resourceType"]

    inst2 = immunization.Immunization(**data)
    impl_immunization_3(inst2)
