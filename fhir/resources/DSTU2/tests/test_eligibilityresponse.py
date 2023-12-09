# -*- coding: utf-8 -*-
from pydantic.v1.datetime_parse import parse_date

from .. import fhirtypes  # noqa: F401
from .. import eligibilityresponse


def test_EligibilityResponse_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"]
        / "eligibilityresponse-example.canonical.json"
    )
    inst = eligibilityresponse.EligibilityResponse.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EligibilityResponse" == inst.resource_type
    impl_EligibilityResponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EligibilityResponse" == data["resourceType"]

    inst2 = eligibilityresponse.EligibilityResponse(**data)
    impl_EligibilityResponse_1(inst2)


def impl_EligibilityResponse_1(inst):
    assert inst.created == parse_date("2014-08-16")
    assert inst.disposition == "Policy is currently in-force."
    assert inst.id == "E2500"
    assert (
        inst.identifier[0].system
        == "http://www.BenefitsInc.com/fhir/eligibilityresponse"
    )
    assert inst.identifier[0].value == "881234"
    assert inst.organization.reference == "Organization/2"
    assert inst.outcome == "complete"
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/eligibility/225476332402"
    )
    assert inst.requestOrganization.reference == "Organization/1"
    assert (
        inst.text.div
        == "<div>A human-readable rendering of the EligibilityResponse.</div>"
    )
    assert inst.text.status == "generated"
