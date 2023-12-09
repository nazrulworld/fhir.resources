# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentResponse
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import enrollmentresponse


def impl_enrollmentresponse_1(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-08-16")
    assert inst.disposition == "Dependant added to policy."
    assert inst.id == "ER2500"
    assert (
        inst.identifier[0].system
        == "http://www.BenefitsInc.com/fhir/enrollmentresponse"
    )
    assert inst.identifier[0].value == "781234"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.organization.reference == "Organization/2"
    assert inst.outcome == "complete"
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/eligibility/225476332402"
    )
    assert inst.requestProvider.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the EnrollmentResponse</div>"
    )
    assert inst.text.status == "generated"


def test_enrollmentresponse_1(base_settings):
    """No. 1 tests collection for EnrollmentResponse.
    Test File: enrollmentresponse-example.json
    """
    filename = base_settings["unittest_data_dir"] / "enrollmentresponse-example.json"
    inst = enrollmentresponse.EnrollmentResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EnrollmentResponse" == inst.resource_type

    impl_enrollmentresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EnrollmentResponse" == data["resourceType"]

    inst2 = enrollmentresponse.EnrollmentResponse(**data)
    impl_enrollmentresponse_1(inst2)
