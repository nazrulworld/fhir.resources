# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import visionprescription


def impl_visionprescription_1(inst):
    assert inst.dateWritten == fhirtypes.DateTime.validate("2014-06-15")
    assert float(inst.dispense[0].add) == float(1.75)
    assert inst.dispense[0].axis == 160
    assert float(inst.dispense[0].backCurve) == float(8.7)
    assert inst.dispense[0].brand == "OphthaGuard"
    assert inst.dispense[0].color == "green"
    assert float(inst.dispense[0].cylinder) == float(-2.25)
    assert float(inst.dispense[0].diameter) == float(14.0)
    assert inst.dispense[0].duration.code == "month"
    assert inst.dispense[0].duration.system == "http://unitsofmeasure.org"
    assert inst.dispense[0].duration.unit == "month"
    assert float(inst.dispense[0].duration.value) == float(1)
    assert inst.dispense[0].eye == "right"
    assert (
        inst.dispense[0].note[0].text == "Shade treatment for extreme light sensitivity"
    )
    assert float(inst.dispense[0].power) == float(-2.75)
    assert inst.dispense[0].product.coding[0].code == "contact"
    assert (
        inst.dispense[0].product.coding[0].system
        == "http://hl7.org/fhir/ex-visionprescriptionproduct"
    )
    assert float(inst.dispense[1].add) == float(1.75)
    assert inst.dispense[1].axis == 160
    assert float(inst.dispense[1].backCurve) == float(8.7)
    assert inst.dispense[1].brand == "OphthaGuard"
    assert inst.dispense[1].color == "green"
    assert float(inst.dispense[1].cylinder) == float(-3.5)
    assert float(inst.dispense[1].diameter) == float(14.0)
    assert inst.dispense[1].duration.code == "month"
    assert inst.dispense[1].duration.system == "http://unitsofmeasure.org"
    assert inst.dispense[1].duration.unit == "month"
    assert float(inst.dispense[1].duration.value) == float(1)
    assert inst.dispense[1].eye == "left"
    assert (
        inst.dispense[1].note[0].text == "Shade treatment for extreme light sensitivity"
    )
    assert float(inst.dispense[1].power) == float(-2.75)
    assert inst.dispense[1].product.coding[0].code == "contact"
    assert (
        inst.dispense[1].product.coding[0].system
        == "http://hl7.org/fhir/ex-visionprescriptionproduct"
    )
    assert inst.encounter.reference == "Encounter/f001"
    assert inst.id == "33124"
    assert inst.identifier[0].system == "http://www.happysight.com/prescription"
    assert inst.identifier[0].value == "15014"
    assert inst.patient.reference == "Patient/example"
    assert inst.prescriber.reference == "Practitioner/example"
    assert inst.reasonCodeableConcept.coding[0].code == "myopia"
    assert (
        inst.reasonCodeableConcept.coding[0].system
        == "http://samplevisionreasoncodes.com"
    )
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
    assert inst.dateWritten == fhirtypes.DateTime.validate("2014-06-15")
    assert float(inst.dispense[0].add) == float(2.0)
    assert inst.dispense[0].base == "down"
    assert inst.dispense[0].eye == "right"
    assert float(inst.dispense[0].prism) == float(0.5)
    assert inst.dispense[0].product.coding[0].code == "lens"
    assert (
        inst.dispense[0].product.coding[0].system
        == "http://hl7.org/fhir/ex-visionprescriptionproduct"
    )
    assert float(inst.dispense[0].sphere) == float(-2.0)
    assert float(inst.dispense[1].add) == float(2.0)
    assert inst.dispense[1].axis == 180
    assert inst.dispense[1].base == "up"
    assert float(inst.dispense[1].cylinder) == float(-0.5)
    assert inst.dispense[1].eye == "left"
    assert float(inst.dispense[1].prism) == float(0.5)
    assert inst.dispense[1].product.coding[0].code == "lens"
    assert (
        inst.dispense[1].product.coding[0].system
        == "http://hl7.org/fhir/ex-visionprescriptionproduct"
    )
    assert float(inst.dispense[1].sphere) == float(-1.0)
    assert inst.id == "33123"
    assert inst.identifier[0].system == "http://www.happysight.com/prescription"
    assert inst.identifier[0].value == "15013"
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
