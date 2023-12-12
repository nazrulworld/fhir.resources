# -*- coding: utf-8 -*-
from datetime import date

from pydantic.v1.datetime_parse import parse_date

from .. import fhirtypes  # noqa: F401
from .. import enrollmentrequest


def test_EnrollmentRequest_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "enrollmentrequest-example.canonical.json"
    )
    inst = enrollmentrequest.EnrollmentRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EnrollmentRequest" == inst.resource_type
    impl_EnrollmentRequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EnrollmentRequest" == data["resourceType"]

    inst2 = enrollmentrequest.EnrollmentRequest(**data)
    impl_EnrollmentRequest_1(inst2)


def impl_EnrollmentRequest_1(inst):
    assert inst.coverage.reference == "Coverage/9876B1"
    assert inst.created == parse_date("2014-08-16")
    assert inst.id == "22345"
    assert inst.identifier[0].system == "http://happyvalley.com/enrollmentrequest"
    assert inst.identifier[0].value == "EN22345"
    assert inst.organization.reference == "Organization/1"
    assert inst.relationship.code == "spouse"
    assert inst.subject.reference == "Patient/1"
    assert (
        inst.text.div
        == "<div>A human-readable rendering of the EnrollmentRequest.</div>"
    )
    assert inst.text.status == "generated"
