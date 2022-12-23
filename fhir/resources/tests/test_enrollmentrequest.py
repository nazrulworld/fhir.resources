# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import enrollmentrequest


def impl_enrollmentrequest_1(inst):
    assert inst.candidate.reference == "Patient/1"
    assert inst.coverage.reference == "Coverage/9876B1"
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.id == "22345"
    assert inst.identifier[0].system == "http://happyvalley.com/enrollmentrequest"
    assert inst.identifier[0].value == "EN22345"
    assert inst.insurer.reference == "Organization/2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.provider.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the EnrollmentRequest.</div>"
    )
    assert inst.text.status == "generated"


def test_enrollmentrequest_1(base_settings):
    """No. 1 tests collection for EnrollmentRequest.
    Test File: enrollmentrequest-example.json
    """
    filename = base_settings["unittest_data_dir"] / "enrollmentrequest-example.json"
    inst = enrollmentrequest.EnrollmentRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EnrollmentRequest" == inst.resource_type

    impl_enrollmentrequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EnrollmentRequest" == data["resourceType"]

    inst2 = enrollmentrequest.EnrollmentRequest(**data)
    impl_enrollmentrequest_1(inst2)
