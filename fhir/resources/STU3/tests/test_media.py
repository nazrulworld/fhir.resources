# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Media
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import media


def impl_media_1(inst):
    assert inst.content.contentType == "image/gif"
    assert inst.content.creation == fhirtypes.DateTime.validate("2009-09-03")
    assert inst.content.id == "a1"
    assert inst.device.display == "Acme Camera"
    assert inst.frames == 1
    assert inst.height == 145
    assert inst.id == "example"
    assert inst.operator.reference == "Practitioner/xcda-author"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.subtype.coding[0].code == "diagram"
    assert inst.subtype.coding[0].system == "http://hl7.org/fhir/media-subtype"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Diagram for '
        'Patient Henry Levin (MRN 12345):<br/><img src="#11" '
        'alt="diagram"/></div>'
    )
    assert inst.text.status == "generated"
    assert inst.type == "photo"
    assert inst.width == 126


def test_media_1(base_settings):
    """No. 1 tests collection for Media.
    Test File: media-example.json
    """
    filename = base_settings["unittest_data_dir"] / "media-example.json"
    inst = media.Media.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Media" == inst.resource_type

    impl_media_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Media" == data["resourceType"]

    inst2 = media.Media(**data)
    impl_media_1(inst2)


def impl_media_2(inst):
    assert inst.content.contentType == "application/dicom"
    assert inst.device.display == "G.E. Medical Systems"
    assert inst.extension[0].url == "http://nema.org/fhir/extensions#0002-0010"
    assert inst.extension[0].valueUri == "urn:oid:1.2.840.10008.1.2.1"
    assert inst.height == 480
    assert inst.id == "1.2.840.11361907579238403408700.3.0.14.19970327150033"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].type.text == "InstanceUID"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == (
        "urn:oid:1.2.840.11361907579238403408700.3.0.14.1997032715003" "3"
    )
    assert inst.identifier[1].system == "http://acme-imaging.com/accession/2012"
    assert inst.identifier[1].type.text == "accessionNo"
    assert inst.identifier[1].value == "1234567"
    assert inst.identifier[2].system == "urn:ietf:rfc:3986"
    assert inst.identifier[2].type.text == "studyId"
    assert (
        inst.identifier[2].value
        == "urn:oid:1.2.840.113619.2.21.848.34082.0.538976288.3"
    )
    assert inst.identifier[3].system == "urn:ietf:rfc:3986"
    assert inst.identifier[3].type.text == "seriesId"
    assert (
        inst.identifier[3].value
        == "urn:oid:1.2.840.113619.2.21.3408.700.0.757923840.3.0"
    )
    assert inst.subject.reference == "Patient/example"
    assert inst.subtype.coding[0].code == "US"
    assert (
        inst.subtype.coding[0].system == "http://dicom.nema.org/resources/ontology/DCM"
    )
    assert inst.text.status == "generated"
    assert inst.type == "photo"
    assert inst.view.coding[0].code == "399067008"
    assert inst.view.coding[0].display == "Lateral projection"
    assert inst.view.coding[0].system == "http://snomed.info/sct"
    assert inst.width == 640


def test_media_2(base_settings):
    """No. 2 tests collection for Media.
    Test File: media-example-dicom.json
    """
    filename = base_settings["unittest_data_dir"] / "media-example-dicom.json"
    inst = media.Media.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Media" == inst.resource_type

    impl_media_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Media" == data["resourceType"]

    inst2 = media.Media(**data)
    impl_media_2(inst2)


def impl_media_3(inst):
    assert inst.basedOn[0].identifier.assigner.display == "XYZ Medical Clinic"
    assert (
        inst.basedOn[0].identifier.system
        == "http://someclinic.org/fhir/NamingSystem/imaging-orders"
    )
    assert inst.basedOn[0].identifier.value == "111222"
    assert inst.bodySite.coding[0].code == "85151006"
    assert inst.bodySite.coding[0].display == "Structure of left hand (body structure)"
    assert inst.bodySite.coding[0].system == "http://snomed.info.sct"
    assert inst.content.contentType == "image/jpeg"
    assert inst.content.creation == fhirtypes.DateTime.validate("2016-03-15")
    assert inst.content.id == "a1"
    assert inst.content.url == "http://someimagingcenter.org/fhir/Binary/A12345"
    assert inst.context.reference == "Encounter/example"
    assert inst.height == 432
    assert inst.id == "xray"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2016-03-15")
    assert inst.subject.reference == "Patient/example"
    assert inst.subtype.coding[0].code == "39714003"
    assert inst.subtype.coding[0].display == "Skeletal X-ray of wrist and hand"
    assert inst.subtype.coding[0].system == "http://snomed.info/sct"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Xray of left '
        "hand for Patient Henry Levin (MRN 12345) 2016-03-15</div>"
    )
    assert inst.text.status == "generated"
    assert inst.type == "photo"
    assert inst.width == 640


def test_media_3(base_settings):
    """No. 3 tests collection for Media.
    Test File: media-example-xray.json
    """
    filename = base_settings["unittest_data_dir"] / "media-example-xray.json"
    inst = media.Media.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Media" == inst.resource_type

    impl_media_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Media" == data["resourceType"]

    inst2 = media.Media(**data)
    impl_media_3(inst2)


def impl_media_4(inst):
    assert inst.content.contentType == "audio/mpeg"
    assert inst.content.data == bytes_validator(
        "dG9vIGJpZyB0b28gaW5jbHVkZSB0aGUgd2hvbGU="
    )
    assert inst.content.id == "a1"
    assert inst.duration == 65
    assert inst.id == "sound"
    assert inst.operator.reference == "Practitioner/xcda-author"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Sound recording '
        "of speech example for Patient Henry Levin (MRN "
        '12345):<br/><img src="#11" alt="diagram"/></div>'
    )
    assert inst.text.status == "generated"
    assert inst.type == "video"


def test_media_4(base_settings):
    """No. 4 tests collection for Media.
    Test File: media-example-sound.json
    """
    filename = base_settings["unittest_data_dir"] / "media-example-sound.json"
    inst = media.Media.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Media" == inst.resource_type

    impl_media_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Media" == data["resourceType"]

    inst2 = media.Media(**data)
    impl_media_4(inst2)
