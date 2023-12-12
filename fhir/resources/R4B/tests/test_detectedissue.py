# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DetectedIssue
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import detectedissue


def impl_detectedissue_1(inst):
    assert inst.id == "allergy"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "final"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_detectedissue_1(base_settings):
    """No. 1 tests collection for DetectedIssue.
    Test File: detectedissue-example-allergy.json
    """
    filename = base_settings["unittest_data_dir"] / "detectedissue-example-allergy.json"
    inst = detectedissue.DetectedIssue.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DetectedIssue" == inst.resource_type

    impl_detectedissue_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DetectedIssue" == data["resourceType"]

    inst2 = detectedissue.DetectedIssue(**data)
    impl_detectedissue_1(inst2)


def impl_detectedissue_2(inst):
    assert inst.author.reference == "Device/software"
    assert inst.code.coding[0].code == "DUPTHPY"
    assert inst.code.coding[0].display == "Duplicate Therapy Alert"
    assert (
        inst.code.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.detail == "Similar test was performed within the past 14 days"
    assert inst.id == "duplicate"
    assert inst.identifiedDateTime == fhirtypes.DateTime.validate("2013-05-08")
    assert inst.identifier[0].system == "http://example.org"
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "12345"
    assert (
        inst.implicated[0].display
        == "Chest CT - ordered May 8, 2013 by Dr. Adam Careful"
    )
    assert inst.implicated[0].reference == "ServiceRequest/di"
    assert inst.implicated[1].display == (
        "Image 1 from Series 3: CT Images on Patient MINT (MINT1234) "
        "taken at 1-Jan 2011 01:20 AM"
    )
    assert inst.implicated[1].reference == "ImagingStudy/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/dicom"
    assert inst.reference == (
        "http://www.tmhp.com/RadiologyClinicalDecisionSupport/2011/CH"
        "EST%20IMAGING%20GUIDELINES%202011.pdf"
    )
    assert inst.status == "final"
    assert inst.text.status == "generated"


def test_detectedissue_2(base_settings):
    """No. 2 tests collection for DetectedIssue.
    Test File: detectedissue-example-dup.json
    """
    filename = base_settings["unittest_data_dir"] / "detectedissue-example-dup.json"
    inst = detectedissue.DetectedIssue.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DetectedIssue" == inst.resource_type

    impl_detectedissue_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DetectedIssue" == data["resourceType"]

    inst2 = detectedissue.DetectedIssue(**data)
    impl_detectedissue_2(inst2)


def impl_detectedissue_3(inst):
    assert inst.author.reference == "Device/software"
    assert inst.code.coding[0].code == "DRG"
    assert inst.code.coding[0].display == "Drug Interaction Alert"
    assert (
        inst.code.coding[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.id == "ddi"
    assert inst.identifiedDateTime == fhirtypes.DateTime.validate("2014-01-05")
    assert (
        inst.implicated[0].display
        == "500 mg Acetaminophen tablet 1/day, PRN since 2010"
    )
    assert inst.implicated[0].reference == "MedicationStatement/example001"
    assert inst.implicated[1].display == "Warfarin 1 MG TAB prescribed Jan. 15, 2015"
    assert inst.implicated[1].reference == "MedicationRequest/medrx0331"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.mitigation[0].action.coding[0].code == "13"
    assert inst.mitigation[0].action.coding[0].display == "Stopped Concurrent Therapy"
    assert (
        inst.mitigation[0].action.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.mitigation[0].action.text == (
        "Asked patient to discontinue regular use of Tylenol and to "
        "consult with clinician if they need to resume to allow "
        "appropriate INR monitoring"
    )
    assert inst.mitigation[0].author.display == "Dr. Adam Careful"
    assert inst.mitigation[0].author.reference == "Practitioner/example"
    assert inst.mitigation[0].date == fhirtypes.DateTime.validate("2014-01-05")
    assert inst.severity == "high"
    assert inst.status == "final"
    assert inst.text.status == "generated"


def test_detectedissue_3(base_settings):
    """No. 3 tests collection for DetectedIssue.
    Test File: detectedissue-example.json
    """
    filename = base_settings["unittest_data_dir"] / "detectedissue-example.json"
    inst = detectedissue.DetectedIssue.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DetectedIssue" == inst.resource_type

    impl_detectedissue_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DetectedIssue" == data["resourceType"]

    inst2 = detectedissue.DetectedIssue(**data)
    impl_detectedissue_3(inst2)


def impl_detectedissue_4(inst):
    assert inst.id == "lab"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.status == "final"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_detectedissue_4(base_settings):
    """No. 4 tests collection for DetectedIssue.
    Test File: detectedissue-example-lab.json
    """
    filename = base_settings["unittest_data_dir"] / "detectedissue-example-lab.json"
    inst = detectedissue.DetectedIssue.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DetectedIssue" == inst.resource_type

    impl_detectedissue_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DetectedIssue" == data["resourceType"]

    inst2 = detectedissue.DetectedIssue(**data)
    impl_detectedissue_4(inst2)
