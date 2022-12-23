# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Schedule
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import schedule


def impl_schedule_1(inst):
    assert inst.active is True
    assert inst.actor[0].display == "Dr. Beverly Crusher"
    assert inst.actor[0].reference == "Practitioner/1"
    assert inst.actor[1].display == "USS Enterprise-D Sickbay"
    assert inst.actor[1].reference == "Location/3"
    assert inst.comment == (
        "The slots attached to this schedule are for genetic "
        "counselling in the USS Enterprise-D Sickbay."
    )
    assert inst.id == "exampleloc1"
    assert inst.identifier[0].system == "http://example.org/scheduleid"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "46"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.planningHorizon.end == fhirtypes.DateTime.validate(
        "2017-12-25T09:30:00Z"
    )
    assert inst.planningHorizon.start == fhirtypes.DateTime.validate(
        "2017-12-25T09:15:00Z"
    )
    assert inst.serviceCategory[0].coding[0].code == "17"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert inst.serviceType[0].coding[0].code == "75"
    assert inst.serviceType[0].coding[0].display == "Genetic Counselling"
    assert inst.specialty[0].coding[0].code == "394580004"
    assert inst.specialty[0].coding[0].display == "Clinical genetics"
    assert inst.text.status == "generated"


def test_schedule_1(base_settings):
    """No. 1 tests collection for Schedule.
    Test File: schedule-provider-location1-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "schedule-provider-location1-example.json"
    )
    inst = schedule.Schedule.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Schedule" == inst.resource_type

    impl_schedule_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Schedule" == data["resourceType"]

    inst2 = schedule.Schedule(**data)
    impl_schedule_1(inst2)


def impl_schedule_2(inst):
    assert inst.active is True
    assert inst.actor[0].display == "Burgers UMC, South Wing, second floor"
    assert inst.actor[0].reference == "Location/1"
    assert inst.comment == (
        "The slots attached to this schedule should be specialized to"
        " cover immunizations within the clinic"
    )
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://example.org/scheduleid"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "45"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.planningHorizon.end == fhirtypes.DateTime.validate(
        "2013-12-25T09:30:00Z"
    )
    assert inst.planningHorizon.start == fhirtypes.DateTime.validate(
        "2013-12-25T09:15:00Z"
    )
    assert inst.serviceCategory[0].coding[0].code == "17"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert inst.serviceType[0].coding[0].code == "57"
    assert inst.serviceType[0].coding[0].display == "Immunization"
    assert inst.specialty[0].coding[0].code == "408480009"
    assert inst.specialty[0].coding[0].display == "Clinical immunology"
    assert inst.text.status == "generated"


def test_schedule_2(base_settings):
    """No. 2 tests collection for Schedule.
    Test File: schedule-example.json
    """
    filename = base_settings["unittest_data_dir"] / "schedule-example.json"
    inst = schedule.Schedule.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Schedule" == inst.resource_type

    impl_schedule_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Schedule" == data["resourceType"]

    inst2 = schedule.Schedule(**data)
    impl_schedule_2(inst2)


def impl_schedule_3(inst):
    assert inst.active is True
    assert inst.actor[0].display == "Dr. Beverly Crusher"
    assert inst.actor[0].reference == "Practitioner/1"
    assert inst.actor[1].display == "Starfleet HQ Sickbay"
    assert inst.actor[1].reference == "Location/2"
    assert inst.comment == (
        "The slots attached to this schedule are for neurosurgery "
        "operations at Starfleet HQ only."
    )
    assert inst.id == "exampleloc2"
    assert inst.identifier[0].system == "http://example.org/scheduleid"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "47"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.planningHorizon.end == fhirtypes.DateTime.validate(
        "2017-12-25T09:30:00Z"
    )
    assert inst.planningHorizon.start == fhirtypes.DateTime.validate(
        "2017-12-25T09:15:00Z"
    )
    assert inst.serviceCategory[0].coding[0].code == "31"
    assert inst.serviceCategory[0].coding[0].display == "Specialist Surgical"
    assert inst.serviceType[0].coding[0].code == "221"
    assert inst.serviceType[0].coding[0].display == "Surgery - General"
    assert inst.specialty[0].coding[0].code == "394610002"
    assert inst.specialty[0].coding[0].display == "Surgery-Neurosurgery"
    assert inst.text.status == "generated"


def test_schedule_3(base_settings):
    """No. 3 tests collection for Schedule.
    Test File: schedule-provider-location2-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "schedule-provider-location2-example.json"
    )
    inst = schedule.Schedule.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Schedule" == inst.resource_type

    impl_schedule_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Schedule" == data["resourceType"]

    inst2 = schedule.Schedule(**data)
    impl_schedule_3(inst2)
