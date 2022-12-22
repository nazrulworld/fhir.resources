# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/InsurancePlan
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import insuranceplan


def impl_insuranceplan_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "foo"
    assert inst.text.status == "generated"


def test_insuranceplan_1(base_settings):
    """No. 1 tests collection for InsurancePlan.
    Test File: insuranceplan-example.json
    """
    filename = base_settings["unittest_data_dir"] / "insuranceplan-example.json"
    inst = insuranceplan.InsurancePlan.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "InsurancePlan" == inst.resource_type

    impl_insuranceplan_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "InsurancePlan" == data["resourceType"]

    inst2 = insuranceplan.InsurancePlan(**data)
    impl_insuranceplan_1(inst2)
