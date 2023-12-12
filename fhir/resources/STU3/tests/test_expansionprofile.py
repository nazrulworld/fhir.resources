# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ExpansionProfile
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import expansionprofile


def impl_expansionprofile_1(inst):
    assert inst.contact[0].name == "FHIR project team"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2016-12-23")
    assert inst.description == "exanple ExpansionProfile for publication"
    assert inst.excludeNested is True
    assert inst.experimental is True
    assert inst.id == "example"
    assert inst.identifier.system == "http://example.org/profiles"
    assert inst.identifier.value == "example"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.name == "Example Expansion Profile"
    assert inst.publisher == "HL7 International"
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[ Provide ' "Rendering ]</div>"
    )
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ExpansionProfile/example"
    assert inst.version == "0.1"


def test_expansionprofile_1(base_settings):
    """No. 1 tests collection for ExpansionProfile.
    Test File: expansionprofile-example.json
    """
    filename = base_settings["unittest_data_dir"] / "expansionprofile-example.json"
    inst = expansionprofile.ExpansionProfile.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ExpansionProfile" == inst.resource_type

    impl_expansionprofile_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ExpansionProfile" == data["resourceType"]

    inst2 = expansionprofile.ExpansionProfile(**data)
    impl_expansionprofile_1(inst2)
