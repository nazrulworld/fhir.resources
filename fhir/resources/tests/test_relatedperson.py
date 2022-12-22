# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RelatedPerson
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import relatedperson


def impl_relatedperson_1(inst):
    assert inst.address[0].city == "PleasantVille"
    assert inst.address[0].line[0] == "534 Erewhon St"
    assert inst.address[0].postalCode == "3999"
    assert inst.address[0].state == "Vic"
    assert inst.address[0].use == "home"
    assert inst.gender == "male"
    assert inst.id == "peter"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "Chalmers"
    assert inst.name[0].given[0] == "Peter"
    assert inst.name[0].given[1] == "James"
    assert inst.name[0].use == "official"
    assert inst.patient.reference == "Patient/animal"
    assert inst.period.start == fhirtypes.DateTime.validate("2012-03-11")
    assert inst.photo[0].contentType == "image/jpeg"
    assert inst.photo[0].url == "Binary/f012"
    assert inst.relationship[0].coding[0].code == "C"
    assert (
        inst.relationship[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0131"
    )
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "(03) 5555 6473"
    assert inst.text.status == "generated"


def test_relatedperson_1(base_settings):
    """No. 1 tests collection for RelatedPerson.
    Test File: relatedperson-example-peter.json
    """
    filename = base_settings["unittest_data_dir"] / "relatedperson-example-peter.json"
    inst = relatedperson.RelatedPerson.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RelatedPerson" == inst.resource_type

    impl_relatedperson_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RelatedPerson" == data["resourceType"]

    inst2 = relatedperson.RelatedPerson(**data)
    impl_relatedperson_1(inst2)


def impl_relatedperson_2(inst):
    assert inst.gender == "female"
    assert inst.id == "f001"
    assert inst.identifier[0].system == "urn:oid:2.16.840.1.113883.2.4.6.3"
    assert inst.identifier[0].type.text == "BSN"
    assert inst.identifier[0].use == "official"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "Abels"
    assert inst.name[0].given[0] == "Sarah"
    assert inst.name[0].use == "usual"
    assert inst.patient.reference == "Patient/f001"
    assert inst.relationship[0].coding[0].code == "SIGOTHR"
    assert (
        inst.relationship[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
    )
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "mobile"
    assert inst.telecom[0].value == "0690383372"
    assert inst.telecom[1].system == "email"
    assert inst.telecom[1].use == "home"
    assert inst.telecom[1].value == "s.abels@kpn.nl"
    assert inst.text.status == "generated"


def test_relatedperson_2(base_settings):
    """No. 2 tests collection for RelatedPerson.
    Test File: relatedperson-example-f001-sarah.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "relatedperson-example-f001-sarah.json"
    )
    inst = relatedperson.RelatedPerson.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RelatedPerson" == inst.resource_type

    impl_relatedperson_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RelatedPerson" == data["resourceType"]

    inst2 = relatedperson.RelatedPerson(**data)
    impl_relatedperson_2(inst2)


def impl_relatedperson_3(inst):
    assert inst.active is True
    assert inst.address[0].line[0] == "2222 Home Street"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1973-05-31")
    assert inst.gender == "female"
    assert inst.id == "newborn-mom"
    assert inst.identifier[0].system == "http://hl7.org/fhir/sid/us-ssn"
    assert inst.identifier[0].type.coding[0].code == "SS"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].value == "444222222"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "Everywoman"
    assert inst.name[0].given[0] == "Eve"
    assert inst.name[0].use == "official"
    assert inst.patient.reference == "Patient/newborn"
    assert inst.relationship[0].coding[0].code == "NMTH"
    assert inst.relationship[0].coding[0].display == "natural mother"
    assert (
        inst.relationship[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
    )
    assert inst.relationship[0].text == "Natural Mother"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "555-555-2003"
    assert inst.text.status == "generated"


def test_relatedperson_3(base_settings):
    """No. 3 tests collection for RelatedPerson.
    Test File: relatedperson-example-newborn-mom.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "relatedperson-example-newborn-mom.json"
    )
    inst = relatedperson.RelatedPerson.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RelatedPerson" == inst.resource_type

    impl_relatedperson_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RelatedPerson" == data["resourceType"]

    inst2 = relatedperson.RelatedPerson(**data)
    impl_relatedperson_3(inst2)


def impl_relatedperson_4(inst):
    assert inst.active is True
    assert inst.address[0].city == "Paris"
    assert inst.address[0].country == "FRA"
    assert inst.address[0].line[0] == "43, Place du Marché Sainte Catherine"
    assert inst.address[0].postalCode == "75004"
    assert inst.gender == "female"
    assert inst.id == "benedicte"
    assert inst.identifier[0].system == "urn:oid:1.2.250.1.61"
    assert inst.identifier[0].type.text == "INSEE"
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "272117510400399"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "du Marché"
    assert inst.name[0].given[0] == "Bénédicte"
    assert inst.patient.reference == "Patient/example"
    assert inst.photo[0].contentType == "image/jpeg"
    assert inst.photo[0].url == "Binary/f016"
    assert inst.relationship[0].coding[0].code == "N"
    assert (
        inst.relationship[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0131"
    )
    assert inst.relationship[0].coding[1].code == "WIFE"
    assert (
        inst.relationship[0].coding[1].system
        == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
    )
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].value == "+33 (237) 998327"
    assert inst.text.status == "generated"


def test_relatedperson_4(base_settings):
    """No. 4 tests collection for RelatedPerson.
    Test File: relatedperson-example.json
    """
    filename = base_settings["unittest_data_dir"] / "relatedperson-example.json"
    inst = relatedperson.RelatedPerson.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RelatedPerson" == inst.resource_type

    impl_relatedperson_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RelatedPerson" == data["resourceType"]

    inst2 = relatedperson.RelatedPerson(**data)
    impl_relatedperson_4(inst2)


def impl_relatedperson_5(inst):
    assert inst.birthDate == fhirtypes.Date.validate("1963")
    assert inst.gender == "female"
    assert inst.id == "f002"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].text == "Ariadne Bor-Jansma"
    assert inst.name[0].use == "usual"
    assert inst.patient.reference == "Patient/f201"
    assert inst.period.start == fhirtypes.DateTime.validate("1975")
    assert inst.photo[0].contentType == "image/jpeg"
    assert inst.relationship[0].coding[0].code == "SIGOTHR"
    assert (
        inst.relationship[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
    )
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "home"
    assert inst.telecom[0].value == "+31201234567"
    assert inst.text.status == "generated"


def test_relatedperson_5(base_settings):
    """No. 5 tests collection for RelatedPerson.
    Test File: relatedperson-example-f002-ariadne.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "relatedperson-example-f002-ariadne.json"
    )
    inst = relatedperson.RelatedPerson.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "RelatedPerson" == inst.resource_type

    impl_relatedperson_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "RelatedPerson" == data["resourceType"]

    inst2 = relatedperson.RelatedPerson(**data)
    impl_relatedperson_5(inst2)
