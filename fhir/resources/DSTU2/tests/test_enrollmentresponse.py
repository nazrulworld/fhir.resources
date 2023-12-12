# -*- coding: utf-8 -*-
from datetime import date

from pydantic.v1.datetime_parse import parse_date

from .. import fhirtypes  # noqa: F401
from .. import enrollmentresponse


def test_EnrollmentResponse_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "enrollmentresponse-example.canonical.json"
    )
    inst = enrollmentresponse.EnrollmentResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EnrollmentResponse" == inst.resource_type
    impl_EnrollmentResponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EnrollmentResponse" == data["resourceType"]

    inst2 = enrollmentresponse.EnrollmentResponse(**data)
    impl_EnrollmentResponse_1(inst2)


def impl_EnrollmentResponse_1(inst):
    assert inst.created == parse_date("2014-08-16")
    assert inst.disposition == "Dependant added to policy."
    assert inst.id == "ER2500"
    assert (
        inst.identifier[0].system
        == "http://www.BenefitsInc.com/fhir/enrollmentresponse"
    )
    assert inst.identifier[0].value == "781234"
    assert inst.organization.reference == "Organization/2"
    assert inst.outcome == "complete"
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/eligibility/225476332402"
    )
    assert inst.requestOrganization.reference == "Organization/1"
    assert (
        inst.text.div
        == "<div>A human-readable rendering of the EnrollmentResponse</div>"
    )
    assert inst.text.status == "generated"
