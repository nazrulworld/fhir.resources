# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Schedule
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import schedule
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


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
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="http://example.org/scheduleid").valueUri
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "46"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert (
        inst.planningHorizon.end
        == ExternalValidatorModel(valueDateTime="2017-12-25T09:30:00Z").valueDateTime
    )
    assert (
        inst.planningHorizon.start
        == ExternalValidatorModel(valueDateTime="2017-12-25T09:15:00Z").valueDateTime
    )
    assert inst.serviceCategory[0].coding[0].code == "17"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert (
        inst.serviceCategory[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/service-category"
        ).valueUri
    )
    assert inst.serviceType[0].concept.coding[0].code == "75"
    assert inst.serviceType[0].concept.coding[0].display == "Genetic Counselling"
    assert (
        inst.serviceType[0].concept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/service-type"
        ).valueUri
    )
    assert inst.specialty[0].coding[0].code == "394580004"
    assert inst.specialty[0].coding[0].display == "Clinical genetics"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.text.status == "generated"


def test_schedule_1(base_settings):
    """No. 1 tests collection for Schedule.
    Test File: schedule-provider-location1-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "schedule-provider-location1-example.json"
    )
    inst = schedule.Schedule.model_validate_json(Path(filename).read_bytes())
    assert "Schedule" == inst.get_resource_type()

    impl_schedule_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
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
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="http://example.org/scheduleid").valueUri
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "45"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "Burgers UMC, South Wing - Immunizations"
    assert (
        inst.planningHorizon.end
        == ExternalValidatorModel(valueDateTime="2013-12-25T09:30:00Z").valueDateTime
    )
    assert (
        inst.planningHorizon.start
        == ExternalValidatorModel(valueDateTime="2013-12-25T09:15:00Z").valueDateTime
    )
    assert inst.serviceCategory[0].coding[0].code == "17"
    assert inst.serviceCategory[0].coding[0].display == "General Practice"
    assert (
        inst.serviceCategory[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/service-category"
        ).valueUri
    )
    assert inst.serviceType[0].concept.coding[0].code == "57"
    assert inst.serviceType[0].concept.coding[0].display == "Immunization"
    assert (
        inst.serviceType[0].concept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/service-type"
        ).valueUri
    )
    assert inst.specialty[0].coding[0].code == "408480009"
    assert inst.specialty[0].coding[0].display == "Clinical immunology"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.text.status == "generated"


def test_schedule_2(base_settings):
    """No. 2 tests collection for Schedule.
    Test File: schedule-example.json
    """
    filename = base_settings["unittest_data_dir"] / "schedule-example.json"
    inst = schedule.Schedule.model_validate_json(Path(filename).read_bytes())
    assert "Schedule" == inst.get_resource_type()

    impl_schedule_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Schedule" == data["resourceType"]

    inst2 = schedule.Schedule(**data)
    impl_schedule_2(inst2)


def impl_schedule_3(inst):
    assert inst.active is True
    assert inst.actor[0].display == "Burgers UMC, South Wing, second floor"
    assert inst.actor[0].reference == "Location/1"
    assert inst.id == "example-hcs"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.name == "Burgers UMC, Posttraumatic Stress Disorder counselling"
    assert (
        inst.planningHorizon.end
        == ExternalValidatorModel(valueDateTime="2023-12-25T09:30:00Z").valueDateTime
    )
    assert (
        inst.planningHorizon.start
        == ExternalValidatorModel(valueDateTime="2023-12-25T09:15:00Z").valueDateTime
    )
    assert inst.serviceCategory[0].coding[0].code == "8"
    assert inst.serviceCategory[0].coding[0].display == "Counselling"
    assert (
        inst.serviceCategory[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/service-category"
        ).valueUri
    )
    assert (
        inst.serviceType[0].reference.display
        == "Burgers UMC, Posttraumatic Stress Disorder Clinic"
    )
    assert inst.serviceType[0].reference.reference == "HealthcareService/example"
    assert inst.specialty[0].coding[0].code == "47505003"
    assert inst.specialty[0].coding[0].display == "Posttraumatic stress disorder"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.text.status == "generated"


def test_schedule_3(base_settings):
    """No. 3 tests collection for Schedule.
    Test File: schedule-example-hcs.json
    """
    filename = base_settings["unittest_data_dir"] / "schedule-example-hcs.json"
    inst = schedule.Schedule.model_validate_json(Path(filename).read_bytes())
    assert "Schedule" == inst.get_resource_type()

    impl_schedule_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Schedule" == data["resourceType"]

    inst2 = schedule.Schedule(**data)
    impl_schedule_3(inst2)


def impl_schedule_4(inst):
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
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(valueUri="http://example.org/scheduleid").valueUri
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "47"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert (
        inst.planningHorizon.end
        == ExternalValidatorModel(valueDateTime="2017-12-25T09:30:00Z").valueDateTime
    )
    assert (
        inst.planningHorizon.start
        == ExternalValidatorModel(valueDateTime="2017-12-25T09:15:00Z").valueDateTime
    )
    assert inst.serviceCategory[0].coding[0].code == "31"
    assert inst.serviceCategory[0].coding[0].display == "Specialist Surgical"
    assert (
        inst.serviceCategory[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/service-category"
        ).valueUri
    )
    assert inst.serviceType[0].concept.coding[0].code == "221"
    assert inst.serviceType[0].concept.coding[0].display == "Surgery - General"
    assert (
        inst.serviceType[0].concept.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/service-type"
        ).valueUri
    )
    assert inst.specialty[0].coding[0].code == "394610002"
    assert inst.specialty[0].coding[0].display == "Surgery-Neurosurgery"
    assert (
        inst.specialty[0].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.text.status == "generated"


def test_schedule_4(base_settings):
    """No. 4 tests collection for Schedule.
    Test File: schedule-provider-location2-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "schedule-provider-location2-example.json"
    )
    inst = schedule.Schedule.model_validate_json(Path(filename).read_bytes())
    assert "Schedule" == inst.get_resource_type()

    impl_schedule_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Schedule" == data["resourceType"]

    inst2 = schedule.Schedule(**data)
    impl_schedule_4(inst2)
