# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingManifest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import imagingmanifest


def impl_imagingmanifest_1(inst):
    assert inst.author.reference == "Practitioner/example"
    assert inst.authoringTime == fhirtypes.DateTime.validate(
        "2014-11-20T11:01:20-08:00"
    )
    assert inst.description == (
        "1 SC image (screen snapshot) and 2 CT images to share a " "chest CT exam"
    )
    assert inst.id == "example"
    assert inst.identifier.value == (
        "urn:oid:2.16.124.113543.6003.189642796.63084.16748.259909290" "1"
    )
    assert inst.patient.reference == "Patient/dicom"
    assert inst.study[0].endpoint[0].reference == "Endpoint/example-iid"
    assert inst.study[0].endpoint[1].reference == "Endpoint/example-wadors"
    assert inst.study[0].imagingStudy.reference == "ImagingStudy/example"
    assert inst.study[0].series[0].endpoint[0].reference == "Endpoint/example-wadors"
    assert (
        inst.study[0].series[0].instance[0].sopClass
        == "urn:oid:1.2.840.10008.5.1.4.1.1.7"
    )
    assert inst.study[0].series[0].instance[0].uid == (
        "urn:oid:2.16.124.113543.6003.189642796.63084.16748.259909290" "2"
    )
    assert inst.study[0].series[0].uid == (
        "urn:oid:2.16.124.113543.6003.189642796.63084.16750.259909290" "1"
    )
    assert (
        inst.study[0].series[1].instance[0].sopClass
        == "urn:oid:1.2.840.10008.5.1.4.1.1.2"
    )
    assert inst.study[0].series[1].instance[0].uid == (
        "urn:oid:2.16.124.113543.6003.189642796.63084.16748.259909290" "3"
    )
    assert (
        inst.study[0].series[1].instance[1].sopClass
        == "urn:oid:1.2.840.10008.5.1.4.1.1.2"
    )
    assert inst.study[0].series[1].instance[1].uid == (
        "urn:oid:2.16.124.113543.6003.189642796.63084.16748.259909290" "4"
    )
    assert inst.study[0].series[1].uid == (
        "urn:oid:2.16.124.113543.6003.189642796.63084.16750.259909290" "2"
    )
    assert inst.study[0].uid == (
        "urn:oid:2.16.124.113543.6003.189642796.63084.16749.259909290" "4"
    )
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A set of images '
        "to share accompanying an report document, including one SC "
        "image and two CT image</div>"
    )
    assert inst.text.status == "generated"


def test_imagingmanifest_1(base_settings):
    """No. 1 tests collection for ImagingManifest.
    Test File: imagingmanifest-example.json
    """
    filename = base_settings["unittest_data_dir"] / "imagingmanifest-example.json"
    inst = imagingmanifest.ImagingManifest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImagingManifest" == inst.resource_type

    impl_imagingmanifest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImagingManifest" == data["resourceType"]

    inst2 = imagingmanifest.ImagingManifest(**data)
    impl_imagingmanifest_1(inst2)
