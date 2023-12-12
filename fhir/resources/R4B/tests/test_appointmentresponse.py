# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AppointmentResponse
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import appointmentresponse


def impl_appointmentresponse_1(inst):
    assert inst.actor.display == "Dr Adam Careful"
    assert inst.actor.reference == "Practitioner/example"
    assert inst.appointment.display == "Brian MRI results discussion"
    assert inst.appointment.reference == "Appointment/examplereq"
    assert inst.comment == "can't we try for this time, can't do mornings"
    assert inst.end == fhirtypes.Instant.validate("2013-12-25T13:30:00Z")
    assert inst.id == "exampleresp"
    assert (
        inst.identifier[0].system
        == "http://example.org/sampleappointmentresponse-identifier"
    )
    assert inst.identifier[0].value == "response123"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.participantStatus == "tentative"
    assert inst.participantType[0].coding[0].code == "ATND"
    assert (
        inst.participantType[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ParticipationType"
    )
    assert inst.start == fhirtypes.Instant.validate("2013-12-25T13:15:00Z")
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Accept Brian MRI'
        " results discussion</div>"
    )
    assert inst.text.status == "generated"


def test_appointmentresponse_1(base_settings):
    """No. 1 tests collection for AppointmentResponse.
    Test File: appointmentresponse-example-req.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "appointmentresponse-example-req.json"
    )
    inst = appointmentresponse.AppointmentResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AppointmentResponse" == inst.resource_type

    impl_appointmentresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AppointmentResponse" == data["resourceType"]

    inst2 = appointmentresponse.AppointmentResponse(**data)
    impl_appointmentresponse_1(inst2)


def impl_appointmentresponse_2(inst):
    assert inst.actor.display == "Peter James Chalmers"
    assert inst.actor.reference == "Patient/example"
    assert inst.appointment.display == "Brian MRI results discussion"
    assert inst.appointment.reference == "Appointment/example"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.participantStatus == "accepted"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Accept Brian MRI'
        " results discussion</div>"
    )
    assert inst.text.status == "generated"


def test_appointmentresponse_2(base_settings):
    """No. 2 tests collection for AppointmentResponse.
    Test File: appointmentresponse-example.json
    """
    filename = base_settings["unittest_data_dir"] / "appointmentresponse-example.json"
    inst = appointmentresponse.AppointmentResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AppointmentResponse" == inst.resource_type

    impl_appointmentresponse_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AppointmentResponse" == data["resourceType"]

    inst2 = appointmentresponse.AppointmentResponse(**data)
    impl_appointmentresponse_2(inst2)
