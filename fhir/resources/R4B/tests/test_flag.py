# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Flag
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import flag


def impl_flag_1(inst):
    assert inst.author.display == "Nancy Nurse"
    assert inst.author.reference == "Practitioner/example"
    assert inst.category[0].coding[0].code == "safety"
    assert inst.category[0].coding[0].display == "Safety"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/flag-category"
    )
    assert inst.category[0].text == "Safety"
    assert inst.code.coding[0].code == "bigdog"
    assert inst.code.coding[0].display == "Big dog"
    assert inst.code.coding[0].system == "http://example.org/local"
    assert inst.code.text == (
        "Patient has a big dog at his home. Always always wear a suit"
        " of armor or take other active counter-measures"
    )
    assert inst.id == "example"
    assert inst.identifier[0].value == "12345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.period.end == fhirtypes.DateTime.validate("2016-12-01")
    assert inst.period.start == fhirtypes.DateTime.validate("2015-01-17")
    assert inst.status == "inactive"
    assert inst.subject.display == "Peter Patient"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Large Dog '
        "warning for Peter Patient</div>"
    )
    assert inst.text.status == "generated"


def test_flag_1(base_settings):
    """No. 1 tests collection for Flag.
    Test File: flag-example.json
    """
    filename = base_settings["unittest_data_dir"] / "flag-example.json"
    inst = flag.Flag.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Flag" == inst.resource_type

    impl_flag_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Flag" == data["resourceType"]

    inst2 = flag.Flag(**data)
    impl_flag_1(inst2)


def impl_flag_2(inst):
    assert inst.category[0].coding[0].code == "infection"
    assert inst.category[0].coding[0].display == "Infection Control Level"
    assert inst.category[0].coding[0].system == "http://example.org/local"
    assert inst.code.coding[0].code == "l3"
    assert inst.code.coding[0].display == "Follow Level 3 Protocol"
    assert inst.code.coding[0].system == "http://example.org/local/if1"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "example-encounter"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "active"
    assert inst.subject.display == "Peter Patient"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Follow Infection'
        " Control Level 3 Protocol</div>"
    )
    assert inst.text.status == "generated"


def test_flag_2(base_settings):
    """No. 2 tests collection for Flag.
    Test File: flag-example-encounter.json
    """
    filename = base_settings["unittest_data_dir"] / "flag-example-encounter.json"
    inst = flag.Flag.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Flag" == inst.resource_type

    impl_flag_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Flag" == data["resourceType"]

    inst2 = flag.Flag(**data)
    impl_flag_2(inst2)
