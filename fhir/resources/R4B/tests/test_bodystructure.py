# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BodyStructure
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import bodystructure


def impl_bodystructure_1(inst):
    assert inst.description == "EDD 1/1/2017 confirmation by LMP"
    assert inst.id == "fetus"
    assert (
        inst.identifier[0].system == "http://goodhealth.org/bodystructure/identifiers"
    )
    assert inst.identifier[0].value == "12345"
    assert inst.location.coding[0].code == "83418008"
    assert inst.location.coding[0].display == "Entire fetus (body structure)"
    assert inst.location.coding[0].system == "http://snomed.info/sct"
    assert inst.location.text == "Fetus"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_bodystructure_1(base_settings):
    """No. 1 tests collection for BodyStructure.
    Test File: bodystructure-example-fetus.json
    """
    filename = base_settings["unittest_data_dir"] / "bodystructure-example-fetus.json"
    inst = bodystructure.BodyStructure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "BodyStructure" == inst.resource_type

    impl_bodystructure_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "BodyStructure" == data["resourceType"]

    inst2 = bodystructure.BodyStructure(**data)
    impl_bodystructure_1(inst2)


def impl_bodystructure_2(inst):
    assert inst.description == "7 cm maximum diameter"
    assert inst.id == "tumor"
    assert (
        inst.identifier[0].system == "http://goodhealth.org/bodystructure/identifiers"
    )
    assert inst.identifier[0].value == "12345"
    assert inst.image[0].contentType == "application/dicom"
    assert inst.image[0].url == (
        "http://imaging.acme.com/wado/server?requestType=WADO&amp;wad" "o_details"
    )
    assert inst.location.coding[0].code == "78961009"
    assert inst.location.coding[0].display == "Splenic structure (body structure)"
    assert inst.location.coding[0].system == "http://snomed.info/sct"
    assert inst.location.text == "Spleen"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.morphology.coding[0].code == "4147007"
    assert inst.morphology.coding[0].display == "Mass (morphologic abnormality)"
    assert inst.morphology.coding[0].system == "http://snomed.info/sct"
    assert inst.morphology.text == "Splenic mass"
    assert inst.patient.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_bodystructure_2(base_settings):
    """No. 2 tests collection for BodyStructure.
    Test File: bodystructure-example-tumor.json
    """
    filename = base_settings["unittest_data_dir"] / "bodystructure-example-tumor.json"
    inst = bodystructure.BodyStructure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "BodyStructure" == inst.resource_type

    impl_bodystructure_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "BodyStructure" == data["resourceType"]

    inst2 = bodystructure.BodyStructure(**data)
    impl_bodystructure_2(inst2)


def impl_bodystructure_3(inst):
    assert inst.active is False
    assert inst.description == "inner surface (volar) of the left forearm"
    assert inst.id == "skin-patch"
    assert (
        inst.identifier[0].system == "http://goodhealth.org/bodystructure/identifiers"
    )
    assert inst.identifier[0].value == "12345"
    assert inst.location.coding[0].code == "14975008"
    assert inst.location.coding[0].display == "Forearm"
    assert inst.location.coding[0].system == "http://snomed.info/sct"
    assert inst.location.text == "Forearm"
    assert inst.locationQualifier[0].coding[0].code == "419161000"
    assert inst.locationQualifier[0].coding[0].display == "Unilateral left"
    assert inst.locationQualifier[0].coding[0].system == "http://snomed.info/sct"
    assert inst.locationQualifier[0].text == "Left"
    assert inst.locationQualifier[1].coding[0].code == "263929005"
    assert inst.locationQualifier[1].coding[0].display == "Volar"
    assert inst.locationQualifier[1].coding[0].system == "http://snomed.info/sct"
    assert inst.locationQualifier[1].text == "Volar"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.morphology.text == "Skin patch"
    assert inst.patient.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_bodystructure_3(base_settings):
    """No. 3 tests collection for BodyStructure.
    Test File: bodystructure-example-skin-patch.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "bodystructure-example-skin-patch.json"
    )
    inst = bodystructure.BodyStructure.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "BodyStructure" == inst.resource_type

    impl_bodystructure_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "BodyStructure" == data["resourceType"]

    inst2 = bodystructure.BodyStructure(**data)
    impl_bodystructure_3(inst2)
