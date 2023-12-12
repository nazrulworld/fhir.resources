# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import visionprescription


def impl_visionprescription_1(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-06-15")
    assert inst.dateWritten == fhirtypes.DateTime.validate("2014-06-15")
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "33124"
    assert inst.identifier[0].system == "http://www.happysight.com/prescription"
    assert inst.identifier[0].value == "15014"
    assert float(inst.lensSpecification[0].add) == float(1.75)
    assert inst.lensSpecification[0].axis == 160
    assert float(inst.lensSpecification[0].backCurve) == float(8.7)
    assert inst.lensSpecification[0].brand == "OphthaGuard"
    assert inst.lensSpecification[0].color == "green"
    assert float(inst.lensSpecification[0].cylinder) == float(-2.25)
    assert float(inst.lensSpecification[0].diameter) == float(14.0)
    assert inst.lensSpecification[0].duration.code == "mo"
    assert inst.lensSpecification[0].duration.system == "http://unitsofmeasure.org"
    assert inst.lensSpecification[0].duration.unit == "mo"
    assert float(inst.lensSpecification[0].duration.value) == float(1)
    assert inst.lensSpecification[0].eye == "right"
    assert (
        inst.lensSpecification[0].note[0].text
        == "Shade treatment for extreme light sensitivity"
    )
    assert float(inst.lensSpecification[0].power) == float(-2.75)
    assert inst.lensSpecification[0].product.coding[0].code == "contact"
    assert inst.lensSpecification[0].product.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/ex-" "visionprescriptionproduct"
    )
    assert float(inst.lensSpecification[1].add) == float(1.75)
    assert inst.lensSpecification[1].axis == 160
    assert float(inst.lensSpecification[1].backCurve) == float(8.7)
    assert inst.lensSpecification[1].brand == "OphthaGuard"
    assert inst.lensSpecification[1].color == "green"
    assert float(inst.lensSpecification[1].cylinder) == float(-3.5)
    assert float(inst.lensSpecification[1].diameter) == float(14.0)
    assert inst.lensSpecification[1].duration.code == "mo"
    assert inst.lensSpecification[1].duration.system == "http://unitsofmeasure.org"
    assert inst.lensSpecification[1].duration.unit == "month"
    assert float(inst.lensSpecification[1].duration.value) == float(1)
    assert inst.lensSpecification[1].eye == "left"
    assert (
        inst.lensSpecification[1].note[0].text
        == "Shade treatment for extreme light sensitivity"
    )
    assert float(inst.lensSpecification[1].power) == float(-2.75)
    assert inst.lensSpecification[1].product.coding[0].code == "contact"
    assert inst.lensSpecification[1].product.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/ex-" "visionprescriptionproduct"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.prescriber.reference == "Practitioner/example"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Sample Contract '
        "Lens prescription</div>"
    )
    assert inst.text.status == "generated"


def test_visionprescription_1(base_settings):
    """No. 1 tests collection for VisionPrescription.
    Test File: visionprescription-example-1.json
    """
    filename = base_settings["unittest_data_dir"] / "visionprescription-example-1.json"
    inst = visionprescription.VisionPrescription.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "VisionPrescription" == inst.resource_type

    impl_visionprescription_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "VisionPrescription" == data["resourceType"]

    inst2 = visionprescription.VisionPrescription(**data)
    impl_visionprescription_1(inst2)


def impl_visionprescription_2(inst):
    assert inst.created == fhirtypes.DateTime.validate("2014-06-15")
    assert inst.dateWritten == fhirtypes.DateTime.validate("2014-06-15")
    assert inst.id == "33123"
    assert inst.identifier[0].system == "http://www.happysight.com/prescription"
    assert inst.identifier[0].value == "15013"
    assert float(inst.lensSpecification[0].add) == float(2.0)
    assert inst.lensSpecification[0].eye == "right"
    assert float(inst.lensSpecification[0].prism[0].amount) == float(0.5)
    assert inst.lensSpecification[0].prism[0].base == "down"
    assert inst.lensSpecification[0].product.coding[0].code == "lens"
    assert inst.lensSpecification[0].product.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/ex-" "visionprescriptionproduct"
    )
    assert float(inst.lensSpecification[0].sphere) == float(-2.0)
    assert float(inst.lensSpecification[1].add) == float(2.0)
    assert inst.lensSpecification[1].axis == 180
    assert float(inst.lensSpecification[1].cylinder) == float(-0.5)
    assert inst.lensSpecification[1].eye == "left"
    assert float(inst.lensSpecification[1].prism[0].amount) == float(0.5)
    assert inst.lensSpecification[1].prism[0].base == "up"
    assert inst.lensSpecification[1].product.coding[0].code == "lens"
    assert inst.lensSpecification[1].product.coding[0].system == (
        "http://terminology.hl7.org/CodeSystem/ex-" "visionprescriptionproduct"
    )
    assert float(inst.lensSpecification[1].sphere) == float(-1.0)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patient.reference == "Patient/example"
    assert inst.prescriber.reference == "Practitioner/example"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_visionprescription_2(base_settings):
    """No. 2 tests collection for VisionPrescription.
    Test File: visionprescription-example.json
    """
    filename = base_settings["unittest_data_dir"] / "visionprescription-example.json"
    inst = visionprescription.VisionPrescription.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "VisionPrescription" == inst.resource_type

    impl_visionprescription_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "VisionPrescription" == data["resourceType"]

    inst2 = visionprescription.VisionPrescription(**data)
    impl_visionprescription_2(inst2)
