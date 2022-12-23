# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/HealthcareService
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import healthcareservice


def impl_healthcareservice_1(inst):
    assert inst.active is True
    assert inst.appointmentRequired is False
    assert (
        inst.availabilityExceptions
        == "Reduced capacity is available during the Christmas period"
    )
    assert inst.availableTime[0].allDay is True
    assert inst.availableTime[0].daysOfWeek[0] == "wed"
    assert inst.availableTime[1].availableEndTime == fhirtypes.Time.validate("05:30:00")
    assert inst.availableTime[1].availableStartTime == fhirtypes.Time.validate(
        "08:30:00"
    )
    assert inst.availableTime[1].daysOfWeek[0] == "mon"
    assert inst.availableTime[1].daysOfWeek[1] == "tue"
    assert inst.availableTime[1].daysOfWeek[2] == "thu"
    assert inst.availableTime[1].daysOfWeek[3] == "fri"
    assert inst.availableTime[2].availableEndTime == fhirtypes.Time.validate("04:30:00")
    assert inst.availableTime[2].availableStartTime == fhirtypes.Time.validate(
        "09:30:00"
    )
    assert inst.availableTime[2].daysOfWeek[0] == "sat"
    assert inst.availableTime[2].daysOfWeek[1] == "fri"
    assert inst.category[0].coding[0].code == "8"
    assert inst.category[0].coding[0].display == "Counselling"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/service-category"
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
    assert inst.identifier[0].system == "http://example.org/shared-ids"
    assert inst.identifier[0].value == "HS-12"
    assert inst.location[0].reference == "Location/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "Consulting psychologists and/or psychology services"
    assert inst.notAvailable[0].description == "Christmas/Boxing Day"
    assert inst.notAvailable[0].during.end == fhirtypes.DateTime.validate("2015-12-26")
    assert inst.notAvailable[0].during.start == fhirtypes.DateTime.validate(
        "2015-12-25"
    )
    assert inst.notAvailable[1].description == "New Years Day"
    assert inst.notAvailable[1].during.end == fhirtypes.DateTime.validate("2016-01-01")
    assert inst.notAvailable[1].during.start == fhirtypes.DateTime.validate(
        "2016-01-01"
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
    assert inst.serviceProvisionCode[0].coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/service-provision-" "conditions"
    )
    assert inst.specialty[0].coding[0].code == "47505003"
    assert inst.specialty[0].coding[0].display == "Posttraumatic stress disorder"
    assert inst.specialty[0].coding[0].system == "http://snomed.info/sct"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "(555) silent"
    assert inst.telecom[1].system == "email"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "directaddress@example.com"
    assert inst.text.status == "generated"
    assert inst.type[0].coding[0].code == "394913002"
    assert inst.type[0].coding[0].display == "Psychotherapy"
    assert inst.type[0].coding[0].system == "http://snomed.info/sct"
    assert inst.type[1].coding[0].code == "394587001"
    assert inst.type[1].coding[0].display == "Psychiatry"
    assert inst.type[1].coding[0].system == "http://snomed.info/sct"


def test_healthcareservice_1(base_settings):
    """No. 1 tests collection for HealthcareService.
    Test File: healthcareservice-example.json
    """
    filename = base_settings["unittest_data_dir"] / "healthcareservice-example.json"
    inst = healthcareservice.HealthcareService.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "HealthcareService" == inst.resource_type

    impl_healthcareservice_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "HealthcareService" == data["resourceType"]

    inst2 = healthcareservice.HealthcareService(**data)
    impl_healthcareservice_1(inst2)
