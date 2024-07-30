# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/HealthcareService
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import healthcareservice
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_healthcareservice_1(inst):
    assert inst.active is True
    assert inst.appointmentRequired is False
    assert (
        inst.availabilityExceptions
        == "Reduced capacity is available during the Christmas period"
    )
    assert inst.availableTime[0].allDay is True
    assert inst.availableTime[0].daysOfWeek[0] == "wed"
    assert (
        inst.availableTime[1].availableEndTime
        == ExternalValidatorModel.model_validate({"valueTime": "05:30:00"}).valueTime
    )
    assert (
        inst.availableTime[1].availableStartTime
        == ExternalValidatorModel.model_validate({"valueTime": "08:30:00"}).valueTime
    )
    assert inst.availableTime[1].daysOfWeek[0] == "mon"
    assert inst.availableTime[1].daysOfWeek[1] == "tue"
    assert inst.availableTime[1].daysOfWeek[2] == "thu"
    assert inst.availableTime[1].daysOfWeek[3] == "fri"
    assert (
        inst.availableTime[2].availableEndTime
        == ExternalValidatorModel.model_validate({"valueTime": "04:30:00"}).valueTime
    )
    assert (
        inst.availableTime[2].availableStartTime
        == ExternalValidatorModel.model_validate({"valueTime": "09:30:00"}).valueTime
    )
    assert inst.availableTime[2].daysOfWeek[0] == "sat"
    assert inst.availableTime[2].daysOfWeek[1] == "fri"
    assert inst.category[0].coding[0].code == "8"
    assert inst.category[0].coding[0].display == "Counselling"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/service-category"}
        ).valueUri
    )
    assert inst.category[0].text == "Counselling"
    assert inst.characteristic[0].coding[0].display == "Wheelchair access"
    assert inst.comment == (
        "Providing Specialist psychology services to the greater Den "
        "Burg area, many years of experience dealing with PTSD issues"
    )
    assert inst.contained[0].id == "DenBurg"
    assert inst.coverageArea[0].display == "Greater Denburg area"
    assert inst.coverageArea[0].reference == "#DenBurg"
    assert inst.eligibility[0].code.coding[0].display == "DVA Required"
    assert inst.eligibility[0].comment == (
        "Evidence of application for DVA status may be sufficient for"
        " commencing assessment"
    )
    assert inst.endpoint[0].reference == "Endpoint/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org/shared-ids"}
        ).valueUri
    )
    assert inst.identifier[0].value == "HS-12"
    assert inst.location[0].reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.name == "Consulting psychologists and/or psychology services"
    assert inst.notAvailable[0].description == "Christmas/Boxing Day"
    assert (
        inst.notAvailable[0].during.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-12-26"}
        ).valueDateTime
    )
    assert (
        inst.notAvailable[0].during.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-12-25"}
        ).valueDateTime
    )
    assert inst.notAvailable[1].description == "New Years Day"
    assert (
        inst.notAvailable[1].during.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-01-01"}
        ).valueDateTime
    )
    assert (
        inst.notAvailable[1].during.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-01-01"}
        ).valueDateTime
    )
    assert inst.program[0].text == "PTSD outreach"
    assert inst.providedBy.display == "Burgers University Medical Center"
    assert inst.providedBy.reference == "Organization/f001"
    assert inst.referralMethod[0].coding[0].code == "phone"
    assert inst.referralMethod[0].coding[0].display == "Phone"
    assert inst.referralMethod[1].coding[0].code == "fax"
    assert inst.referralMethod[1].coding[0].display == "Fax"
    assert inst.referralMethod[2].coding[0].code == "elec"
    assert inst.referralMethod[2].coding[0].display == "Secure Messaging"
    assert inst.referralMethod[3].coding[0].code == "semail"
    assert inst.referralMethod[3].coding[0].display == "Secure Email"
    assert inst.serviceProvisionCode[0].coding[0].code == "cost"
    assert inst.serviceProvisionCode[0].coding[0].display == "Fees apply"
    assert (
        inst.serviceProvisionCode[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://terminology.hl7.org/CodeSystem/service-provision-conditions"
            }
        ).valueUri
    )
    assert inst.specialty[0].coding[0].code == "47505003"
    assert inst.specialty[0].coding[0].display == "Posttraumatic stress disorder"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "(555) silent"
    assert inst.telecom[1].system == "email"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "directaddress@example.com"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "394913002"
    assert inst.type[0].coding[0].display == "Psychotherapy"
    assert (
        inst.type[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.type[1].coding[0].code == "394587001"
    assert inst.type[1].coding[0].display == "Psychiatry"
    assert (
        inst.type[1].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )


def test_healthcareservice_1(base_settings):
    """No. 1 tests collection for HealthcareService.
    Test File: healthcareservice-example.json
    """
    filename = base_settings["unittest_data_dir"] / "healthcareservice-example.json"
    inst = healthcareservice.HealthcareService.model_validate_json(
        filename.read_bytes()
    )
    assert "HealthcareService" == inst.get_resource_type()

    impl_healthcareservice_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "HealthcareService" == data["resourceType"]

    inst2 = healthcareservice.HealthcareService(**data)
    impl_healthcareservice_1(inst2)
