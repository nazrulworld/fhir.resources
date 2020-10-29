# -*- coding: utf-8 -*-
from pydantic.datetime_parse import parse_date

from .. import fhirtypes  # noqa: F401
from .. import coverage


def test_Coverage_1(base_settings):
    filename = base_settings["unittest_data_dir"] / "coverage-example-2.canonical.json"
    inst = coverage.Coverage.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Coverage" == inst.resource_type
    impl_Coverage_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Coverage" == data["resourceType"]

    inst2 = coverage.Coverage(**data)
    impl_Coverage_1(inst2)


def impl_Coverage_1(inst):
    assert inst.dependent == 1
    assert inst.id == "7546D"
    assert inst.identifier[0].system == "http://xyz.com/codes/identifier"
    assert inst.identifier[0].value == "AB9876"
    assert inst.issuer.reference == "Organization/2"
    assert inst.period.end == parse_date("2012-03-17")
    assert inst.period.start == parse_date("2011-03-17")
    assert inst.plan == "11024"
    assert inst.subPlan == "D15C9"
    assert inst.subscriber.reference == "Patient/5"
    assert inst.text.div == "<div>A human-readable rendering of the coverage</div>"
    assert inst.text.status == "generated"
    assert inst.type.code == "EHCPOL"
    assert inst.type.display == "extended healthcare"
    assert inst.type.system == "http://hl7.org/fhir/v3/ActCode"


def test_Coverage_2(base_settings):
    filename = base_settings["unittest_data_dir"] / "coverage-example.canonical.json"
    inst = coverage.Coverage.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Coverage" == inst.resource_type
    impl_Coverage_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Coverage" == data["resourceType"]

    inst2 = coverage.Coverage(**data)
    impl_Coverage_2(inst2)


def impl_Coverage_2(inst):
    assert inst.dependent == 1
    assert inst.id == "9876B1"
    assert inst.identifier[0].system == "http://benefitsinc.com/certificate"
    assert inst.identifier[0].value == "12345"
    assert inst.issuer.reference == "Organization/2"
    assert inst.period.end == parse_date("2012-05-23")
    assert inst.period.start == parse_date("2011-05-23")
    assert inst.plan == "CBI35"
    assert inst.sequence == 1
    assert inst.subPlan == "123"
    assert inst.subscriber.reference == "Patient/4"
    assert inst.text.div == "<div>A human-readable rendering of the coverage</div>"
    assert inst.text.status == "generated"
    assert inst.type.code == "EHCPOL"
    assert inst.type.display == "extended healthcare"
    assert inst.type.system == "http://hl7.org/fhir/v3/ActCode"
