# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NamingSystem
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import namingsystem


def impl_namingsystem_1(inst):
    assert inst.contact[0].name == "HL7 Australia FHIR Team"
    assert inst.contact[0].telecom[0].system == "url"
    assert (
        inst.contact[0].telecom[0].value
        == "http://hl7-australia.wikispaces.com/FHIR+Australia"
    )
    assert inst.date == fhirtypes.DateTime.validate("2015-08-31")
    assert inst.description == (
        "Australian HI Identifier as established by relevant " "regulations etc."
    )
    assert inst.id == "example-id"
    assert inst.jurisdiction[0].coding[0].code == "AU"
    assert inst.jurisdiction[0].coding[0].system == "urn:iso:std:iso:3166"
    assert inst.kind == "identifier"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "Austalian Healthcare Identifier - Individual"
    assert inst.publisher == "HL7 Australia on behalf of NEHTA"
    assert inst.responsible == "HI Service Operator / NEHTA"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "NI"
    assert inst.type.coding[0].display == "National unique individual identifier"
    assert inst.type.coding[0].system == "http://terminology.hl7.org/CodeSystem/v2-0203"
    assert inst.type.text == "IHI"
    assert inst.uniqueId[0].comment == "This value is used in Australian CDA documents"
    assert inst.uniqueId[0].type == "oid"
    assert inst.uniqueId[0].value == "1.2.36.1.2001.1003.0"
    assert inst.uniqueId[1].period.start == fhirtypes.DateTime.validate("2015-08-21")
    assert inst.uniqueId[1].preferred is True
    assert inst.uniqueId[1].type == "uri"
    assert inst.uniqueId[1].value == "http://ns.electronichealth.net.au/id/hi/ihi/1.0"
    assert inst.usage == "Used in Australia for identifying patients"


def test_namingsystem_1(base_settings):
    """No. 1 tests collection for NamingSystem.
    Test File: namingsystem-example-id.json
    """
    filename = base_settings["unittest_data_dir"] / "namingsystem-example-id.json"
    inst = namingsystem.NamingSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NamingSystem" == inst.resource_type

    impl_namingsystem_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NamingSystem" == data["resourceType"]

    inst2 = namingsystem.NamingSystem(**data)
    impl_namingsystem_1(inst2)


def impl_namingsystem_2(inst):
    assert inst.contact[0].name == "FHIR project team"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2014-12-13")
    assert inst.id == "example"
    assert inst.kind == "codesystem"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name == "SNOMED CT"
    assert inst.publisher == "HL7 International on behalf of IHTSDO"
    assert inst.responsible == "IHTSDO & affiliates"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.uniqueId[0].type == "oid"
    assert inst.uniqueId[0].value == "2.16.840.1.113883.6.96"
    assert inst.uniqueId[1].preferred is True
    assert inst.uniqueId[1].type == "uri"
    assert inst.uniqueId[1].value == "http://snomed.info/sct"


def test_namingsystem_2(base_settings):
    """No. 2 tests collection for NamingSystem.
    Test File: namingsystem-example.json
    """
    filename = base_settings["unittest_data_dir"] / "namingsystem-example.json"
    inst = namingsystem.NamingSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "NamingSystem" == inst.resource_type

    impl_namingsystem_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "NamingSystem" == data["resourceType"]

    inst2 = namingsystem.NamingSystem(**data)
    impl_namingsystem_2(inst2)
