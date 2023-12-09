# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Person
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import person


def impl_person_1(inst):
    assert inst.active is True
    assert inst.address[0].city == "Sandusky"
    assert inst.address[0].country == "USA"
    assert inst.address[0].line[0] == "2086 College St"
    assert inst.address[0].postalCode == "44870"
    assert inst.address[0].state == "OH"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1974-03-07")
    assert inst.gender == "female"
    assert inst.id == "pp"
    assert inst.identifier[0].assigner.display == "Ohio Bureau of Motor Vehicles"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2041-09-23")
    assert inst.identifier[0].system == "urn:oid:2.16.840.1.113883.4.3.39"
    assert inst.identifier[0].type.coding[0].code == "DL"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].type.text == "Ohio driver license"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "TL545786"
    assert inst.link[0].assurance == "level3"
    assert inst.link[0].target.display == "Eve Everywoman"
    assert inst.link[0].target.reference == "http://www.goodhealth.com/Patient/98574"
    assert inst.link[1].assurance == "level2"
    assert inst.link[1].target.display == "Eve Marie Everywoman"
    assert inst.link[1].target.reference == "http://www.acme-medical.com/Patient/ab34d"
    assert inst.managingOrganization.display == "Goodhealth Patient Portal"
    assert (
        inst.managingOrganization.reference
        == "http://www.goodhealth.com/Organization/12"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "Everywoman"
    assert inst.name[0].given[0] == "Eve"
    assert inst.name[0].given[1] == "Marie"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "home"
    assert inst.telecom[0].value == "(621)-479-9743"
    assert inst.text.status == "generated"


def test_person_1(base_settings):
    """No. 1 tests collection for Person.
    Test File: person-patient-portal.json
    """
    filename = base_settings["unittest_data_dir"] / "person-patient-portal.json"
    inst = person.Person.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Person" == inst.resource_type

    impl_person_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Person" == data["resourceType"]

    inst2 = person.Person(**data)
    impl_person_1(inst2)


def impl_person_2(inst):
    assert inst.active is True
    assert inst.birthDate == fhirtypes.Date.validate("1963")
    assert inst.gender == "female"
    assert inst.id == "f002"
    assert inst.link[0].target.display == "Ariadne Bor-Jansma"
    assert inst.link[0].target.reference == "RelatedPerson/f002"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].text == "Ariadne Bor-Jansma"
    assert inst.name[0].use == "usual"
    assert inst.photo.contentType == "image/jpeg"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "home"
    assert inst.telecom[0].value == "+31201234567"
    assert inst.text.status == "generated"


def test_person_2(base_settings):
    """No. 2 tests collection for Person.
    Test File: person-example-f002-ariadne.json
    """
    filename = base_settings["unittest_data_dir"] / "person-example-f002-ariadne.json"
    inst = person.Person.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Person" == inst.resource_type

    impl_person_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Person" == data["resourceType"]

    inst2 = person.Person(**data)
    impl_person_2(inst2)


def impl_person_3(inst):
    assert inst.active is True
    assert inst.address[0].city == "Northfield"
    assert inst.address[0].line[0] == "1003 Healthcare Drive"
    assert inst.address[0].state == "MN"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1959-04-22")
    assert inst.gender == "male"
    assert inst.id == "pd"
    assert inst.identifier[0].system == "http://hl7.org/fhir/sid/us-ssn"
    assert inst.identifier[0].type.coding[0].code == "SS"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "444444444"
    assert inst.link[0].assurance == "level2"
    assert inst.link[0].target.display == "Dr. Harold Hippocrates"
    assert (
        inst.link[0].target.reference == "http://www.goodhealth.com/Practitioner/98574"
    )
    assert inst.link[1].assurance == "level2"
    assert inst.link[1].target.display == "Harold Hippocrates, MD"
    assert (
        inst.link[1].target.reference
        == "http://www.acme-medical.com/Practitioner/ab34d"
    )
    assert (
        inst.managingOrganization.display == "Northfield Regional Physician Directory"
    )
    assert (
        inst.managingOrganization.reference
        == "http://www.northfield-regional.com/Organization/2"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "Hippocrates"
    assert inst.name[0].given[0] == "Harold"
    assert inst.name[0].use == "official"
    assert inst.telecom[0].system == "phone"
    assert inst.telecom[0].use == "work"
    assert inst.telecom[0].value == "555-555-1003"
    assert inst.text.status == "generated"


def test_person_3(base_settings):
    """No. 3 tests collection for Person.
    Test File: person-provider-directory.json
    """
    filename = base_settings["unittest_data_dir"] / "person-provider-directory.json"
    inst = person.Person.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Person" == inst.resource_type

    impl_person_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Person" == data["resourceType"]

    inst2 = person.Person(**data)
    impl_person_3(inst2)


def impl_person_4(inst):
    assert inst.active is True
    assert inst.address[0].city == "PleasantVille"
    assert inst.address[0].line[0] == "534 Erewhon St"
    assert inst.address[0].postalCode == "3999"
    assert inst.address[0].state == "Vic"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1974-12-25")
    assert inst.gender == "male"
    assert inst.id == "example"
    assert inst.identifier[0].assigner.display == "Acme Healthcare"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2001-05-06")
    assert inst.identifier[0].system == "urn:oid:1.2.36.146.595.217.0.1"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "12345"
    assert inst.link[0].target.display == "Peter Chalmers"
    assert inst.link[0].target.reference == "RelatedPerson/peter"
    assert inst.link[1].target.display == "Peter Chalmers"
    assert inst.link[1].target.reference == "Patient/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "Chalmers"
    assert inst.name[0].given[0] == "Peter"
    assert inst.name[0].given[1] == "James"
    assert inst.name[0].use == "official"
    assert inst.name[1].given[0] == "Jim"
    assert inst.name[1].use == "usual"
    assert inst.telecom[0].use == "home"
    assert inst.telecom[1].system == "phone"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "(03) 5555 6473"
    assert inst.telecom[2].system == "email"
    assert inst.telecom[2].use == "home"
    assert inst.telecom[2].value == "Jim@example.org"
    assert inst.text.status == "generated"


def test_person_4(base_settings):
    """No. 4 tests collection for Person.
    Test File: person-example.json
    """
    filename = base_settings["unittest_data_dir"] / "person-example.json"
    inst = person.Person.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Person" == inst.resource_type

    impl_person_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Person" == data["resourceType"]

    inst2 = person.Person(**data)
    impl_person_4(inst2)


def impl_person_5(inst):
    assert inst.active is True
    assert inst.address[0].city == "PleasantVille"
    assert inst.address[0].line[0] == "534 Erewhon St"
    assert inst.address[0].postalCode == "3999"
    assert inst.address[0].state == "Vic"
    assert inst.address[0].use == "home"
    assert inst.birthDate == fhirtypes.Date.validate("1974-12-25")
    assert inst.gender == "male"
    assert inst.id == "grahame"
    assert inst.identifier[0].assigner.display == "Acme Healthcare"
    assert inst.identifier[0].period.start == fhirtypes.DateTime.validate("2001-05-06")
    assert inst.identifier[0].system == "urn:oid:1.2.36.146.595.217.0.1"
    assert inst.identifier[0].type.coding[0].code == "MR"
    assert (
        inst.identifier[0].type.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v2-0203"
    )
    assert inst.identifier[0].use == "usual"
    assert inst.identifier[0].value == "12345"
    assert inst.managingOrganization.reference == "Organization/1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].family == "Chalmers"
    assert inst.name[0].given[0] == "Peter"
    assert inst.name[0].given[1] == "James"
    assert inst.name[0].use == "official"
    assert inst.name[1].given[0] == "Jim"
    assert inst.name[1].use == "usual"
    assert inst.telecom[0].use == "home"
    assert inst.telecom[1].system == "phone"
    assert inst.telecom[1].use == "work"
    assert inst.telecom[1].value == "(03) 5555 6473"
    assert inst.text.status == "generated"


def test_person_5(base_settings):
    """No. 5 tests collection for Person.
    Test File: person-grahame.json
    """
    filename = base_settings["unittest_data_dir"] / "person-grahame.json"
    inst = person.Person.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Person" == inst.resource_type

    impl_person_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Person" == data["resourceType"]

    inst2 = person.Person(**data)
    impl_person_5(inst2)
