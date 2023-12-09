# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Group
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import group


def impl_group_1(inst):
    assert inst.actual is True
    assert inst.characteristic[0].code.text == "gender"
    assert inst.characteristic[0].exclude is False
    assert inst.characteristic[0].valueCodeableConcept.text == "mixed"
    assert inst.characteristic[1].code.text == "owner"
    assert inst.characteristic[1].exclude is False
    assert inst.characteristic[1].valueCodeableConcept.text == "John Smith"
    assert inst.code.text == "Horse"
    assert inst.id == "101"
    assert (
        inst.identifier[0].system
        == "http://someveterinarianclinic.org/fhir/NamingSystem/herds"
    )
    assert inst.identifier[0].value == "12345"
    assert inst.name == "John's herd"
    assert inst.quantity == 25
    assert inst.text.status == "additional"
    assert inst.type == "animal"


def test_group_1(base_settings):
    """No. 1 tests collection for Group.
    Test File: group-example.json
    """
    filename = base_settings["unittest_data_dir"] / "group-example.json"
    inst = group.Group.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Group" == inst.resource_type

    impl_group_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Group" == data["resourceType"]

    inst2 = group.Group(**data)
    impl_group_1(inst2)


def impl_group_2(inst):
    assert inst.actual is True
    assert inst.id == "102"
    assert inst.member[0].entity.reference == "Patient/pat1"
    assert inst.member[0].period.start == fhirtypes.DateTime.validate("2014-10-08")
    assert inst.member[1].entity.reference == "Patient/pat2"
    assert inst.member[1].inactive is True
    assert inst.member[1].period.start == fhirtypes.DateTime.validate("2015-04-02")
    assert inst.member[2].entity.reference == "Patient/pat3"
    assert inst.member[2].period.start == fhirtypes.DateTime.validate("2015-08-06")
    assert inst.member[3].entity.reference == "Patient/pat4"
    assert inst.member[3].period.start == fhirtypes.DateTime.validate("2015-08-06")
    assert inst.text.status == "additional"
    assert inst.type == "person"


def test_group_2(base_settings):
    """No. 2 tests collection for Group.
    Test File: group-example-member.json
    """
    filename = base_settings["unittest_data_dir"] / "group-example-member.json"
    inst = group.Group.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Group" == inst.resource_type

    impl_group_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Group" == data["resourceType"]

    inst2 = group.Group(**data)
    impl_group_2(inst2)
