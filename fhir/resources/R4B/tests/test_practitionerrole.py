# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PractitionerRole
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import practitionerrole
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_practitionerrole_1(inst):
    assert inst.active is True
    assert inst.availabilityExceptions == (
        "Adam is generally unavailable on public holidays and during "
        "the Christmas/New Year break"
    )
    assert (
        inst.availableTime[0].availableEndTime
        == ExternalValidatorModel.model_validate({"valueTime": "16:30:00"}).valueTime
    )
    assert (
        inst.availableTime[0].availableStartTime
        == ExternalValidatorModel.model_validate({"valueTime": "09:00:00"}).valueTime
    )
    assert inst.availableTime[0].daysOfWeek[0] == "mon"
    assert inst.availableTime[0].daysOfWeek[1] == "tue"
    assert inst.availableTime[0].daysOfWeek[2] == "wed"
    assert (
        inst.availableTime[1].availableEndTime
        == ExternalValidatorModel.model_validate({"valueTime": "12:00:00"}).valueTime
    )
    assert (
        inst.availableTime[1].availableStartTime
        == ExternalValidatorModel.model_validate({"valueTime": "09:00:00"}).valueTime
    )
    assert inst.availableTime[1].daysOfWeek[0] == "thu"
    assert inst.availableTime[1].daysOfWeek[1] == "fri"
    assert inst.code[0].coding[0].code == "RP"
    assert (
        inst.code[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0286"}
        ).valueUri
    )
    assert inst.endpoint[0].reference == "Endpoint/example"
    assert inst.healthcareService[0].reference == "HealthcareService/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.acme.org/practitioners"}
        ).valueUri
    )
    assert inst.identifier[0].value == "23"
    assert inst.location[0].display == "South Wing, second floor"
    assert inst.location[0].reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.notAvailable[0].description
        == "Adam will be on extended leave during May 2017"
    )
    assert (
        inst.notAvailable[0].during.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2017-05-20"}
        ).valueDateTime
    )
    assert (
        inst.notAvailable[0].during.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2017-05-01"}
        ).valueDateTime
    )
    assert inst.organization.reference == "Organization/f001"
    assert (
        inst.period.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2012-03-31"}
        ).valueDateTime
    )
    assert (
        inst.period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2012-01-01"}
        ).valueDateTime
    )
    assert inst.practitioner.display == "Dr Adam Careful"
    assert inst.practitioner.reference == "Practitioner/example"
    assert inst.specialty[0].coding[0].code == "408443003"
    assert inst.specialty[0].coding[0].display == "General medical practice"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "(03) 5555 6473"
    assert inst.telecom[1].system == "email"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "adam.southern@example.org"
    assert inst.text.status == "generated"


def test_practitionerrole_1(base_settings):
    """No. 1 tests collection for PractitionerRole.
    Test File: practitionerrole-example.json
    """
    filename = base_settings["unittest_data_dir"] / "practitionerrole-example.json"
    inst = practitionerrole.PractitionerRole.model_validate_json(filename.read_bytes())
    assert "PractitionerRole" == inst.get_resource_type()

    impl_practitionerrole_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "PractitionerRole" == data["resourceType"]

    inst2 = practitionerrole.PractitionerRole(**data)
    impl_practitionerrole_1(inst2)
