# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BodySite
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import bodysite


def impl_bodysite_1(inst):
    assert inst.code.coding[0].code == "83418008"
    assert inst.code.coding[0].display == "Entire fetus (body structure)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Fetus"
    assert inst.description == "EDD 1/1/2017 confirmation by LMP"
    assert inst.id == "fetus"
    assert inst.identifier[0].system == "http://goodhealth.org/bodysite/identifiers"
    assert inst.identifier[0].value == "12345"
    assert inst.patient.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_bodysite_1(base_settings):
    """No. 1 tests collection for BodySite.
    Test File: bodysite-example-fetus.json
    """
    filename = base_settings["unittest_data_dir"] / "bodysite-example-fetus.json"
    inst = bodysite.BodySite.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "BodySite" == inst.resource_type

    impl_bodysite_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "BodySite" == data["resourceType"]

    inst2 = bodysite.BodySite(**data)
    impl_bodysite_1(inst2)


def impl_bodysite_2(inst):
    assert inst.code.coding[0].code == "4147007"
    assert inst.code.coding[0].display == "Mass (morphologic abnormality)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Splenic mass"
    assert inst.description == "7 cm maximum diameter"
    assert inst.id == "tumor"
    assert inst.identifier[0].system == "http://goodhealth.org/bodysite/identifiers"
    assert inst.identifier[0].value == "12345"
    assert inst.image[0].contentType == "application/dicom"
    assert inst.image[0].url == (
        "http://imaging.acme.com/wado/server?requestType=WADO&amp;wad" "o_details"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.qualifier[0].coding[0].code == "78961009"
    assert inst.qualifier[0].coding[0].display == "Splenic structure (body structure)"
    assert inst.qualifier[0].coding[0].system == "http://snomed.info/sct"
    assert inst.qualifier[0].text == "Splenic mass"
    assert inst.text.status == "generated"


def test_bodysite_2(base_settings):
    """No. 2 tests collection for BodySite.
    Test File: bodysite-example-tumor.json
    """
    filename = base_settings["unittest_data_dir"] / "bodysite-example-tumor.json"
    inst = bodysite.BodySite.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "BodySite" == inst.resource_type

    impl_bodysite_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "BodySite" == data["resourceType"]

    inst2 = bodysite.BodySite(**data)
    impl_bodysite_2(inst2)


def impl_bodysite_3(inst):
    assert inst.active is False
    assert inst.code.coding[0].code == "39937001"
    assert inst.code.coding[0].display == "Skin structure (body structure)"
    assert inst.code.coding[0].system == "http://snomed.info/sct"
    assert inst.code.text == "Skin patch"
    assert inst.description == "inner surface (volar) of the left forearm"
    assert inst.id == "skin-patch"
    assert inst.identifier[0].system == "http://goodhealth.org/bodysite/identifiers"
    assert inst.identifier[0].value == "12345"
    assert inst.patient.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_bodysite_3(base_settings):
    """No. 3 tests collection for BodySite.
    Test File: bodysite-example-skin-patch.json
    """
    filename = base_settings["unittest_data_dir"] / "bodysite-example-skin-patch.json"
    inst = bodysite.BodySite.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "BodySite" == inst.resource_type

    impl_bodysite_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "BodySite" == data["resourceType"]

    inst2 = bodysite.BodySite(**data)
    impl_bodysite_3(inst2)
