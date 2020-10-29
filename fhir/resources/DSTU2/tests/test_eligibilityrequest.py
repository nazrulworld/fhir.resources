# -*- coding: utf-8 -*-
from pydantic.datetime_parse import parse_date

from .. import fhirtypes  # noqa: F401
from .. import eligibilityrequest


def test_EligibilityRequest_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "eligibilityrequest-example.canonical.json"
    )
    inst = eligibilityrequest.EligibilityRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EligibilityRequest" == inst.resource_type
    impl_EligibilityRequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EligibilityRequest" == data["resourceType"]

    inst2 = eligibilityrequest.EligibilityRequest(**data)
    impl_EligibilityRequest_1(inst2)


def impl_EligibilityRequest_1(inst):
    assert inst.created == parse_date("2014-08-16")
    assert inst.id == "52345"
    assert inst.identifier[0].system == "http://happyvalley.com/elegibilityrequest"
    assert inst.identifier[0].value == "52345"
    assert inst.organization.reference == "Organization/2"
    assert (
        inst.text.div
        == "<div>A human-readable rendering of the EligibilityRequest</div>"
    )
    assert inst.text.status == "generated"
