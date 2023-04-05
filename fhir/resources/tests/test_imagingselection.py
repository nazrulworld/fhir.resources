# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingSelection
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import imagingselection


def impl_imagingselection_1(inst):
    assert inst.code.text == "Observation within a DICOM SR"
    assert inst.derivedFrom[0].identifier.system == "urn:dicom:uid"
    assert (
        inst.derivedFrom[0].identifier.value
        == "urn:oid:1.2.840.113747.20080222.95946072916364657859950275"
    )
    assert inst.derivedFrom[0].type == "ImagingStudy"
    assert inst.focus[0].reference == "ImagingSelection/example-basic-image-selection"
    assert (
        inst.frameOfReferenceUid
        == "1.2.840.113747.20080222.95946058736364657859950275.0"
    )
    assert inst.id == "example-dicom-sr-selection"
    assert inst.identifier[0].system == "urn:dicom:uid"
    assert inst.identifier[0].value == (
        "urn:oid:1.2.840.113747.20080222.95946059916364657859950275.2" ".1"
    )
    assert inst.instance[0].sopClass.code == "urn:oid:1.2.840.10008.5.1.4.1.1.88.22"
    assert inst.instance[0].sopClass.system == "urn:ietf:rfc:3986"
    assert inst.instance[0].subset[0] == (
        "1.2.840.113747.20080222.95946058738699434572916359950275.10." "1"
    )
    assert (
        inst.instance[0].uid == "1.2.840.113747.20080222.95946058738699434359950275.1.0"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.seriesUid == "1.2.840.113747.20080222.95946058738664657859950275.1"
    assert inst.status == "available"
    assert inst.studyUid == "1.2.840.113747.20080222.95946058738694657859950275"
    assert inst.subject.identifier.system == "https://fhirhospital.org"
    assert inst.subject.identifier.value == "RNKZPSBNZLNADAZV"
    assert inst.subject.type == "Patient"
    assert inst.text.status == "generated"


def test_imagingselection_1(base_settings):
    """No. 1 tests collection for ImagingSelection.
    Test File: imagingselection-example-dicom-sr-selection.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "imagingselection-example-dicom-sr-selection.json"
    )
    inst = imagingselection.ImagingSelection.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImagingSelection" == inst.resource_type

    impl_imagingselection_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImagingSelection" == data["resourceType"]

    inst2 = imagingselection.ImagingSelection(**data)
    impl_imagingselection_1(inst2)


def impl_imagingselection_2(inst):
    assert inst.code.text == "Key Frames"
    assert inst.derivedFrom[0].identifier.system == "urn:dicom:uid"
    assert inst.derivedFrom[0].identifier.value == (
        "urn:oid:1.2.840.113747.20080222.3077658758893509802450245542" "21747"
    )
    assert inst.derivedFrom[0].type == "ImagingStudy"
    assert (
        inst.frameOfReferenceUid
        == "1.2.840.113747.20080222.307765875869350980245024554221747.0"
    )
    assert inst.id == "example-multiframe-image-selection"
    assert inst.identifier[0].system == "urn:dicom:uid"
    assert inst.identifier[0].value == (
        "urn:oid:1.2.840.113747.20080222.3077658758693009802450245542" "21747.2.1"
    )
    assert inst.instance[0].sopClass.code == "urn:oid:1.2.840.10008.5.1.4.1.1.2.1"
    assert inst.instance[0].sopClass.system == "urn:ietf:rfc:3986"
    assert inst.instance[0].subset[0] == "1"
    assert inst.instance[0].subset[1] == "2"
    assert inst.instance[0].subset[2] == "3"
    assert inst.instance[0].subset[3] == "4"
    assert inst.instance[0].uid == (
        "1.2.840.113747.20080222.307765875869300489355024554221747.1." "0"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.seriesUid == "1.2.840.113747.20080222.307765875869300489245024554221747.1"
    )
    assert inst.status == "available"
    assert inst.studyUid == "1.2.840.113747.20080222.307765875869300489345024554221747"
    assert inst.subject.identifier.system == "https://fhirhospital.org"
    assert inst.subject.identifier.value == "MNSOIISABIDCHRCY"
    assert inst.subject.type == "Patient"
    assert inst.text.status == "generated"


def test_imagingselection_2(base_settings):
    """No. 2 tests collection for ImagingSelection.
    Test File: imagingselection-example-multiframe-image-selection.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "imagingselection-example-multiframe-image-selection.json"
    )
    inst = imagingselection.ImagingSelection.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImagingSelection" == inst.resource_type

    impl_imagingselection_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImagingSelection" == data["resourceType"]

    inst2 = imagingselection.ImagingSelection(**data)
    impl_imagingselection_2(inst2)


def impl_imagingselection_3(inst):
    assert inst.code.text == "Segment within a DICOM Segmentation instance"
    assert inst.derivedFrom[0].identifier.system == "urn:dicom:uid"
    assert inst.derivedFrom[0].identifier.value == (
        "urn:oid:1.2.840.113747.20080222.2340823325925226669316502208" "11572"
    )
    assert inst.derivedFrom[0].type == "ImagingStudy"
    assert (
        inst.frameOfReferenceUid
        == "1.2.840.113747.20080222.234082332589842666931650220811572.0"
    )
    assert inst.id == "example-segmentation-image-selection"
    assert inst.identifier[0].system == "urn:dicom:uid"
    assert inst.identifier[0].value == (
        "urn:oid:1.2.840.113747.20080222.2340823325898426669316502208" "11572.2.1"
    )
    assert inst.instance[0].sopClass.code == "urn:oid:1.2.840.10008.5.1.4.1.1.66.4"
    assert inst.instance[0].sopClass.system == "urn:ietf:rfc:3986"
    assert inst.instance[0].subset[0] == "1"
    assert inst.instance[0].uid == (
        "1.2.840.113747.20080222.234082332589846992522666220811572.1." "0"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.seriesUid == "1.2.840.113747.20080222.234082332589846992931650220811572.1"
    )
    assert inst.status == "available"
    assert inst.studyUid == "1.2.840.113747.20080222.234082332589846966931650220811572"
    assert inst.subject.identifier.system == "https://fhirhospital.org"
    assert inst.subject.identifier.value == "ISRNEJAWJHZOTNBS"
    assert inst.subject.type == "Patient"
    assert inst.text.status == "generated"


def test_imagingselection_3(base_settings):
    """No. 3 tests collection for ImagingSelection.
    Test File: imagingselection-example-segmentation-image-selection.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "imagingselection-example-segmentation-image-selection.json"
    )
    inst = imagingselection.ImagingSelection.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImagingSelection" == inst.resource_type

    impl_imagingselection_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImagingSelection" == data["resourceType"]

    inst2 = imagingselection.ImagingSelection(**data)
    impl_imagingselection_3(inst2)


def impl_imagingselection_4(inst):
    assert inst.code.text == "Key Images"
    assert inst.derivedFrom[0].identifier.system == "urn:dicom:uid"
    assert inst.derivedFrom[0].identifier.value == (
        "urn:oid:1.2.840.113747.20080222.3573835837292430627041253878" "3781"
    )
    assert inst.derivedFrom[0].type == "ImagingStudy"
    assert (
        inst.frameOfReferenceUid
        == "1.2.840.113747.20080222.35738168372924306270412538783781.0"
    )
    assert inst.id == "example-basic-image-selection"
    assert inst.identifier[0].system == "urn:dicom:uid"
    assert inst.identifier[0].value == (
        "urn:oid:1.2.840.113747.20080222.3573816737292430627041253878" "3781.2.1"
    )
    assert inst.instance[0].sopClass.code == "urn:oid:1.2.840.10008.5.1.4.1.1.2"
    assert inst.instance[0].sopClass.system == "urn:ietf:rfc:3986"
    assert (
        inst.instance[0].uid
        == "1.2.840.113747.20080222.35738167368358372924412538783781.1.0"
    )
    assert inst.instance[1].sopClass.code == "urn:oid:1.2.840.10008.5.1.4.1.1.2"
    assert inst.instance[1].sopClass.system == "urn:ietf:rfc:3986"
    assert (
        inst.instance[1].uid
        == "1.2.840.113747.20080222.35738167368358372920412538783781.1.1"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.seriesUid == "1.2.840.113747.20080222.35738167368358376270412538783781.1"
    )
    assert inst.status == "available"
    assert inst.studyUid == "1.2.840.113747.20080222.35738167368354306270412538783781"
    assert inst.subject.identifier.system == "https://fhirhospital.org"
    assert inst.subject.identifier.value == "KUTGIQCVCDRHVBUK"
    assert inst.subject.type == "Patient"
    assert inst.text.status == "generated"


def test_imagingselection_4(base_settings):
    """No. 4 tests collection for ImagingSelection.
    Test File: imagingselection-example-basic-image-selection.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "imagingselection-example-basic-image-selection.json"
    )
    inst = imagingselection.ImagingSelection.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImagingSelection" == inst.resource_type

    impl_imagingselection_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImagingSelection" == data["resourceType"]

    inst2 = imagingselection.ImagingSelection(**data)
    impl_imagingselection_4(inst2)


def impl_imagingselection_5(inst):
    assert inst.code.text == "Referenced DICOM Grayscale Softcopy Presentation State"
    assert inst.derivedFrom[0].identifier.system == "urn:dicom:uid"
    assert inst.derivedFrom[0].identifier.value == (
        "urn:oid:1.2.840.113747.20080222.1041207392912890031639036314" "39818"
    )
    assert inst.derivedFrom[0].type == "ImagingStudy"
    assert inst.focus[0].reference == "ImagingSelection/example-basic-image-selection"
    assert (
        inst.frameOfReferenceUid
        == "1.2.840.113747.20080222.104120739293289003163903631439818.0"
    )
    assert inst.id == "example-presentation-state-selection"
    assert inst.identifier[0].system == "urn:dicom:uid"
    assert inst.identifier[0].value == (
        "urn:oid:1.2.840.113747.20080222.1041207392938361511639036314" "39818.2.1"
    )
    assert inst.instance[0].sopClass.code == "urn:oid:1.2.840.10008.5.1.4.1.1.11.1"
    assert inst.instance[0].sopClass.system == "urn:ietf:rfc:3986"
    assert inst.instance[0].uid == (
        "1.2.840.113747.20080222.104120739293836151289903631439818.1." "0"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.seriesUid == "1.2.840.113747.20080222.104120739293836151283903631439818.1"
    )
    assert inst.status == "available"
    assert inst.studyUid == "1.2.840.113747.20080222.104120739293836153163903631439818"
    assert inst.subject.identifier.system == "https://fhirhospital.org"
    assert inst.subject.identifier.value == "WMQVWGBPNPQHAWCO"
    assert inst.subject.type == "Patient"
    assert inst.text.status == "generated"


def test_imagingselection_5(base_settings):
    """No. 5 tests collection for ImagingSelection.
    Test File: imagingselection-example-presentation-state-selection.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "imagingselection-example-presentation-state-selection.json"
    )
    inst = imagingselection.ImagingSelection.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImagingSelection" == inst.resource_type

    impl_imagingselection_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImagingSelection" == data["resourceType"]

    inst2 = imagingselection.ImagingSelection(**data)
    impl_imagingselection_5(inst2)


def impl_imagingselection_6(inst):
    assert inst.code.text == "Region selected from multiframe CT volume"
    assert inst.derivedFrom[0].identifier.system == "urn:dicom:uid"
    assert inst.derivedFrom[0].identifier.value == (
        "urn:oid:1.2.840.113747.20080222.1899142719569233292660249885" "86343"
    )
    assert inst.derivedFrom[0].type == "ImagingStudy"
    assert (
        inst.frameOfReferenceUid
        == "1.2.840.113747.20080222.189914270656923329266024988586343.0"
    )
    assert inst.id == "example-3d-image-region-selection"
    assert inst.identifier[0].system == "urn:dicom:uid"
    assert inst.identifier[0].value == (
        "urn:oid:1.2.840.113747.20080222.1899142719348233292660249885" "86343.2.1"
    )
    assert float(inst.instance[0].imageRegion3D[0].coordinate[0]) == float(-50.0)
    assert float(inst.instance[0].imageRegion3D[0].coordinate[1]) == float(-50.0)
    assert float(inst.instance[0].imageRegion3D[0].coordinate[2]) == float(-50.0)
    assert float(inst.instance[0].imageRegion3D[0].coordinate[3]) == float(50.0)
    assert float(inst.instance[0].imageRegion3D[0].coordinate[4]) == float(50.0)
    assert float(inst.instance[0].imageRegion3D[0].coordinate[5]) == float(50.0)
    assert float(inst.instance[0].imageRegion3D[0].coordinate[6]) == float(25.0)
    assert float(inst.instance[0].imageRegion3D[0].coordinate[7]) == float(-25.0)
    assert float(inst.instance[0].imageRegion3D[0].coordinate[8]) == float(0.0)
    assert float(inst.instance[0].imageRegion3D[0].coordinate[9]) == float(-25.0)
    assert inst.instance[0].imageRegion3D[0].regionType == "ellipse"
    assert inst.instance[0].sopClass.code == "urn:oid:1.2.840.10008.5.1.4.1.1.2.1"
    assert inst.instance[0].sopClass.system == "urn:ietf:rfc:3986"
    assert inst.instance[0].uid == (
        "1.2.840.113747.20080222.189914271934870656923024988586343.1." "0"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.seriesUid == "1.2.840.113747.20080222.189914271934870659266024988586343.1"
    )
    assert inst.status == "available"
    assert inst.studyUid == "1.2.840.113747.20080222.189914271934870656966024988586343"
    assert inst.subject.identifier.system == "https://fhirhospital.org"
    assert inst.subject.identifier.value == "PNWYPXNBXMPGMTWX"
    assert inst.subject.type == "Patient"
    assert inst.text.status == "generated"


def test_imagingselection_6(base_settings):
    """No. 6 tests collection for ImagingSelection.
    Test File: imagingselection-example-3d-image-region-selection.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "imagingselection-example-3d-image-region-selection.json"
    )
    inst = imagingselection.ImagingSelection.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImagingSelection" == inst.resource_type

    impl_imagingselection_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImagingSelection" == data["resourceType"]

    inst2 = imagingselection.ImagingSelection(**data)
    impl_imagingselection_6(inst2)


def impl_imagingselection_7(inst):
    assert inst.code.text == "Region selected from image"
    assert inst.derivedFrom[0].identifier.system == "urn:dicom:uid"
    assert (
        inst.derivedFrom[0].identifier.value
        == "1.2.840.113747.20080222.324856729726954657132726086516575"
    )
    assert inst.derivedFrom[0].type == "ImagingStudy"
    assert (
        inst.frameOfReferenceUid
        == "1.2.840.113747.20080222.324856823100954657132726086516575.0"
    )
    assert inst.id == "example-2d-image-region-selection"
    assert inst.identifier[0].system == "urn:dicom:uid"
    assert inst.identifier[0].value == (
        "urn:oid:1.2.840.113747.20080222.3248567223100954657132726086" "516575.2.1"
    )
    assert float(inst.instance[0].imageRegion2D[0].coordinate[0]) == float(0.25)
    assert float(inst.instance[0].imageRegion2D[0].coordinate[1]) == float(0.25)
    assert float(inst.instance[0].imageRegion2D[0].coordinate[2]) == float(0.75)
    assert float(inst.instance[0].imageRegion2D[0].coordinate[3]) == float(0.25)
    assert float(inst.instance[0].imageRegion2D[0].coordinate[4]) == float(0.75)
    assert float(inst.instance[0].imageRegion2D[0].coordinate[5]) == float(0.75)
    assert float(inst.instance[0].imageRegion2D[0].coordinate[6]) == float(0.25)
    assert float(inst.instance[0].imageRegion2D[0].coordinate[7]) == float(0.75)
    assert inst.instance[0].imageRegion2D[0].regionType == "polyline"
    assert inst.instance[0].sopClass.code == "urn:oid:1.2.840.10008.5.1.4.1.1.2"
    assert inst.instance[0].sopClass.system == "urn:ietf:rfc:3986"
    assert inst.instance[0].uid == (
        "1.2.840.113747.20080222.324856729726823100132726086516575.1." "0"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.seriesUid == "1.2.840.113747.20080222.324856729726954657132726086516575.1"
    )
    assert inst.status == "available"
    assert inst.studyUid == "1.2.840.113747.20080222.324856729726854657132726086516575"
    assert inst.subject.identifier.system == "https://fhirhospital.org"
    assert inst.subject.identifier.value == "NTCGFHHKYUYKDPQX"
    assert inst.subject.type == "Patient"
    assert inst.text.status == "generated"


def test_imagingselection_7(base_settings):
    """No. 7 tests collection for ImagingSelection.
    Test File: imagingselection-example-2d-image-region-selection.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "imagingselection-example-2d-image-region-selection.json"
    )
    inst = imagingselection.ImagingSelection.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ImagingSelection" == inst.resource_type

    impl_imagingselection_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ImagingSelection" == data["resourceType"]

    inst2 = imagingselection.ImagingSelection(**data)
    impl_imagingselection_7(inst2)
