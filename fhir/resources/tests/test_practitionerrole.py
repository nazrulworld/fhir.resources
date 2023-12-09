# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PractitionerRole
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import practitionerrole


def impl_practitionerrole_1(inst):
    assert inst.active is True
    assert inst.availability[0].availableTime[
        0
    ].availableEndTime == fhirtypes.Time.validate("16:30:00")
    assert inst.availability[0].availableTime[
        0
    ].availableStartTime == fhirtypes.Time.validate("09:00:00")
    assert inst.availability[0].availableTime[0].daysOfWeek[0] == "mon"
    assert inst.availability[0].availableTime[0].daysOfWeek[1] == "tue"
    assert inst.availability[0].availableTime[0].daysOfWeek[2] == "wed"
    assert inst.availability[0].availableTime[
        1
    ].availableEndTime == fhirtypes.Time.validate("12:00:00")
    assert inst.availability[0].availableTime[
        1
    ].availableStartTime == fhirtypes.Time.validate("09:00:00")
    assert inst.availability[0].availableTime[1].daysOfWeek[0] == "thu"
    assert inst.availability[0].availableTime[1].daysOfWeek[1] == "fri"
    assert (
        inst.availability[0].notAvailableTime[0].description
        == "Adam will be on extended leave during May 2017"
    )
    assert inst.availability[0].notAvailableTime[
        0
    ].during.end == fhirtypes.DateTime.validate("2017-05-20")
    assert inst.availability[0].notAvailableTime[
        0
    ].during.start == fhirtypes.DateTime.validate("2017-05-01")
    assert inst.availability[0].notAvailableTime[1].description == (
        "Adam is generally unavailable on public holidays and during "
        "the Christmas/New Year break"
    )
    assert inst.characteristic[0].coding[0].code == "in-person"
    assert inst.characteristic[0].coding[0].display == "In Person"
    assert inst.characteristic[0].coding[0].system == "http://hl7.org/fhir/service-mode"
    assert inst.characteristic[0].coding[1].code == "videoconference"
    assert inst.characteristic[0].coding[1].display == "Video Conference"
    assert inst.characteristic[0].coding[1].system == "http://hl7.org/fhir/service-mode"
    assert inst.code[0].coding[0].code == "RP"
    assert (
        inst.code[0].coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0286"
    )
    assert inst.communication[0].coding[0].code == "en"
    assert inst.communication[0].coding[0].system == "urn:ietf:bcp:47"
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "(03) 5555 6473"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].use == "work"
    assert inst.contact[0].telecom[1].value == "adam.southern@example.org"
    assert inst.endpoint[0].reference == "Endpoint/example"
    assert inst.healthcareService[0].reference == "HealthcareService/example"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://www.acme.org/practitioners"
    assert inst.identifier[0].value == "23"
    assert inst.location[0].display == "South Wing, second floor"
    assert inst.location[0].reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.organization.reference == "Organization/f001"
    assert inst.period.end == fhirtypes.DateTime.validate("2012-03-31")
    assert inst.period.start == fhirtypes.DateTime.validate("2012-01-01")
    assert inst.practitioner.display == "Dr Adam Careful"
    assert inst.practitioner.reference == "Practitioner/example"
    assert inst.specialty[0].coding[0].code == "408443003"
    assert inst.specialty[0].coding[0].display == "General medical practice"
    assert inst.specialty[0].coding[0].system == "http://snomed.info/sct"
    assert inst.text.status == "generated"


def test_practitionerrole_1(base_settings):
    """No. 1 tests collection for PractitionerRole.
    Test File: practitionerrole-example.json
    """
    filename = base_settings["unittest_data_dir"] / "practitionerrole-example.json"
    inst = practitionerrole.PractitionerRole.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PractitionerRole" == inst.resource_type

    impl_practitionerrole_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PractitionerRole" == data["resourceType"]

    inst2 = practitionerrole.PractitionerRole(**data)
    impl_practitionerrole_1(inst2)
