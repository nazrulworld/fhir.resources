# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PractitionerRole
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import practitionerrole
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_practitionerrole_1(inst):
    assert inst.active is True
    assert (
        inst.availability[0].availableTime[0].availableEndTime
        == ExternalValidatorModel(valueTime="16:30:00").valueTime
    )
    assert (
        inst.availability[0].availableTime[0].availableStartTime
        == ExternalValidatorModel(valueTime="09:00:00").valueTime
    )
    assert inst.availability[0].availableTime[0].daysOfWeek[0] == "mon"
    assert inst.availability[0].availableTime[0].daysOfWeek[1] == "tue"
    assert inst.availability[0].availableTime[0].daysOfWeek[2] == "wed"
    assert (
        inst.availability[0].availableTime[1].availableEndTime
        == ExternalValidatorModel(valueTime="12:00:00").valueTime
    )
    assert (
        inst.availability[0].availableTime[1].availableStartTime
        == ExternalValidatorModel(valueTime="09:00:00").valueTime
    )
    assert inst.availability[0].availableTime[1].daysOfWeek[0] == "thu"
    assert inst.availability[0].availableTime[1].daysOfWeek[1] == "fri"
    assert (
        inst.availability[0].notAvailableTime[0].description
        == "Adam will be on extended leave during May 2017"
    )
    assert (
        inst.availability[0].notAvailableTime[0].during.end
        == ExternalValidatorModel(valueDateTime="2017-05-20").valueDateTime
    )
    assert (
        inst.availability[0].notAvailableTime[0].during.start
        == ExternalValidatorModel(valueDateTime="2017-05-01").valueDateTime
    )
    assert inst.availability[0].notAvailableTime[1].description == (
        "Adam is generally unavailable on public holidays and during "
        "the Christmas/New Year break"
    )
    assert inst.characteristic[0].coding[0].code == "in-person"
    assert inst.characteristic[0].coding[0].display == "In Person"
    assert (
        inst.characteristic[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://hl7.org/fhir/service-mode").valueUri
    )
    assert inst.characteristic[0].coding[1].code == "videoconference"
    assert inst.characteristic[0].coding[1].display == "Video Conference"
    assert (
        inst.characteristic[0].coding[1].system
        == ExternalValidatorModel(valueUri="http://hl7.org/fhir/service-mode").valueUri
    )
    assert inst.code[0].coding[0].code == "RP"
    assert (
        inst.code[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v2-0286"
        ).valueUri
    )
    assert inst.communication[0].coding[0].code == "en"
    assert (
        inst.communication[0].coding[0].system
        == ExternalValidatorModel(valueUri="urn:ietf:bcp:47").valueUri
    )
    assert inst.contact[0].telecom[0].system == "phone"
    assert inst.contact[0].telecom[0].use == "work"
    assert inst.contact[0].telecom[0].value == "(03) 5555 6473"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].use == "work"
    assert inst.contact[0].telecom[1].value == "adam.southern@example.org"
    assert inst.endpoint[0].reference == "Endpoint/example"
    assert inst.healthcareService[0].reference == "HealthcareService/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="http://www.acme.org/practitioners").valueUri
    )
    assert inst.identifier[0].value == "23"
    assert inst.location[0].display == "South Wing, second floor"
    assert inst.location[0].reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.organization.reference == "Organization/f001"
    assert (
        inst.period.end
        == ExternalValidatorModel(valueDateTime="2012-03-31").valueDateTime
    )
    assert (
        inst.period.start
        == ExternalValidatorModel(valueDateTime="2012-01-01").valueDateTime
    )
    assert inst.practitioner.display == "Dr Adam Careful"
    assert inst.practitioner.reference == "Practitioner/example"
    assert inst.specialty[0].coding[0].code == "408443003"
    assert inst.specialty[0].coding[0].display == "General medical practice"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.text.status == "generated"


def test_practitionerrole_1(base_settings):
    """No. 1 tests collection for PractitionerRole.
    Test File: practitionerrole-example.json
    """
    filename = base_settings["unittest_data_dir"] / "practitionerrole-example.json"
    inst = practitionerrole.PractitionerRole.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "PractitionerRole" == inst.get_resource_type()

    impl_practitionerrole_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "PractitionerRole" == data["resourceType"]

    inst2 = practitionerrole.PractitionerRole(**data)
    impl_practitionerrole_1(inst2)
