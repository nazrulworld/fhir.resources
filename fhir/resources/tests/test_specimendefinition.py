# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SpecimenDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import specimendefinition


def impl_specimendefinition_1(inst):
    assert inst.id == "2364"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.patientPreparation[0].text == "12 hour fasting"
    assert inst.patientPreparation[1].coding[0].code == "263678003"
    assert inst.patientPreparation[1].coding[0].display == "At rest"
    assert inst.patientPreparation[1].coding[0].system == "http://snomed.info/sct"
    assert inst.text.status == "generated"
    assert inst.timeAspect == "preferrably morning time"
    assert inst.typeCollected.coding[0].code == "122555007"
    assert inst.typeCollected.coding[0].display == "Venous blood specimen"
    assert inst.typeCollected.coding[0].system == "http://snomed.info/sct"
    assert inst.typeTested[0].container.cap.coding[0].code == "yellow"
    assert inst.typeTested[0].container.cap.coding[0].display == "yellow cap"
    assert (
        inst.typeTested[0].container.cap.coding[0].system == "urn:iso:std:iso:6710:2017"
    )
    assert inst.typeTested[0].container.material.coding[0].code == "61088005"
    assert inst.typeTested[0].container.material.coding[0].display == "plastic"
    assert (
        inst.typeTested[0].container.material.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.typeTested[0].container.minimumVolumeQuantity.code == "mL"
    assert (
        inst.typeTested[0].container.minimumVolumeQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[0].container.minimumVolumeQuantity.unit == "ml"
    assert float(inst.typeTested[0].container.minimumVolumeQuantity.value) == float(2)
    assert inst.typeTested[0].container.type.coding[0].code == "702281005"
    assert inst.typeTested[0].container.type.coding[0].display == (
        "Evacuated blood collection tube, thrombin/clot activator/gel" " separator"
    )
    assert (
        inst.typeTested[0].container.type.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.typeTested[0].handling[0].maxDuration.code == "min"
    assert (
        inst.typeTested[0].handling[0].maxDuration.system == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[0].handling[0].maxDuration.unit == "minute"
    assert float(inst.typeTested[0].handling[0].maxDuration.value) == float(60)
    assert (
        inst.typeTested[0].handling[0].temperatureQualifier.text
        == "Ambient temperature"
    )
    assert inst.typeTested[0].handling[0].temperatureRange.high.code == "Cel"
    assert (
        inst.typeTested[0].handling[0].temperatureRange.high.system
        == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[0].handling[0].temperatureRange.high.unit == "°C"
    assert float(inst.typeTested[0].handling[0].temperatureRange.high.value) == float(
        25
    )
    assert inst.typeTested[0].handling[0].temperatureRange.low.code == "Cel"
    assert (
        inst.typeTested[0].handling[0].temperatureRange.low.system
        == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[0].handling[0].temperatureRange.low.unit == "°C"
    assert float(inst.typeTested[0].handling[0].temperatureRange.low.value) == float(15)
    assert inst.typeTested[0].handling[1].maxDuration.code == "h"
    assert (
        inst.typeTested[0].handling[1].maxDuration.system == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[0].handling[1].maxDuration.unit == "hour"
    assert float(inst.typeTested[0].handling[1].maxDuration.value) == float(8)
    assert (
        inst.typeTested[0].handling[1].temperatureQualifier.text
        == "Refrigerated temperature"
    )
    assert inst.typeTested[0].handling[1].temperatureRange.high.code == "Cel"
    assert (
        inst.typeTested[0].handling[1].temperatureRange.high.system
        == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[0].handling[1].temperatureRange.high.unit == "°C"
    assert float(inst.typeTested[0].handling[1].temperatureRange.high.value) == float(8)
    assert inst.typeTested[0].handling[1].temperatureRange.low.code == "Cel"
    assert (
        inst.typeTested[0].handling[1].temperatureRange.low.system
        == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[0].handling[1].temperatureRange.low.unit == "°C"
    assert float(inst.typeTested[0].handling[1].temperatureRange.low.value) == float(2)
    assert inst.typeTested[0].preference == "preferred"
    assert inst.typeTested[0].type.coding[0].code == "119364003"
    assert inst.typeTested[0].type.coding[0].display == "Serum specimen"
    assert inst.typeTested[0].type.coding[0].system == "http://snomed.info/sct"
    assert inst.typeTested[1].container.cap.coding[0].code == "green"
    assert inst.typeTested[1].container.cap.coding[0].display == "green cap"
    assert (
        inst.typeTested[1].container.cap.coding[0].system == "urn:iso:std:iso:6710:2017"
    )
    assert inst.typeTested[1].container.material.coding[0].code == "32039001"
    assert inst.typeTested[1].container.material.coding[0].display == "glass"
    assert (
        inst.typeTested[1].container.material.coding[0].system
        == "http://snomed.info/sct"
    )
    assert inst.typeTested[1].container.minimumVolumeQuantity.code == "mL"
    assert (
        inst.typeTested[1].container.minimumVolumeQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[1].container.minimumVolumeQuantity.unit == "ml"
    assert float(inst.typeTested[1].container.minimumVolumeQuantity.value) == float(2)
    assert inst.typeTested[1].container.type.coding[0].code == "767390000"
    assert inst.typeTested[1].container.type.coding[0].display == (
        "Evacuated blood collection tube with heparin lithium and gel" " separator"
    )
    assert (
        inst.typeTested[1].container.type.coding[0].system == "http://snomed.info/sct"
    )
    assert inst.typeTested[1].handling[0].maxDuration.code == "min"
    assert (
        inst.typeTested[1].handling[0].maxDuration.system == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[1].handling[0].maxDuration.unit == "minute"
    assert float(inst.typeTested[1].handling[0].maxDuration.value) == float(60)
    assert (
        inst.typeTested[1].handling[0].temperatureQualifier.text
        == "Ambient temperature"
    )
    assert inst.typeTested[1].handling[0].temperatureRange.high.code == "Cel"
    assert (
        inst.typeTested[1].handling[0].temperatureRange.high.system
        == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[1].handling[0].temperatureRange.high.unit == "°C"
    assert float(inst.typeTested[1].handling[0].temperatureRange.high.value) == float(
        25
    )
    assert inst.typeTested[1].handling[0].temperatureRange.low.code == "Cel"
    assert (
        inst.typeTested[1].handling[0].temperatureRange.low.system
        == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[1].handling[0].temperatureRange.low.unit == "°C"
    assert float(inst.typeTested[1].handling[0].temperatureRange.low.value) == float(15)
    assert inst.typeTested[1].handling[1].maxDuration.code == "h"
    assert (
        inst.typeTested[1].handling[1].maxDuration.system == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[1].handling[1].maxDuration.unit == "hour"
    assert float(inst.typeTested[1].handling[1].maxDuration.value) == float(8)
    assert (
        inst.typeTested[1].handling[1].temperatureQualifier.text
        == "Refrigerated temperature"
    )
    assert inst.typeTested[1].handling[1].temperatureRange.high.code == "Cel"
    assert (
        inst.typeTested[1].handling[1].temperatureRange.high.system
        == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[1].handling[1].temperatureRange.high.unit == "°C"
    assert float(inst.typeTested[1].handling[1].temperatureRange.high.value) == float(8)
    assert inst.typeTested[1].handling[1].temperatureRange.low.code == "Cel"
    assert (
        inst.typeTested[1].handling[1].temperatureRange.low.system
        == "http://unitsofmeasure.org"
    )
    assert inst.typeTested[1].handling[1].temperatureRange.low.unit == "°C"
    assert float(inst.typeTested[1].handling[1].temperatureRange.low.value) == float(2)
    assert inst.typeTested[1].preference == "alternate"
    assert inst.typeTested[1].rejectionCriterion[0].coding[0].code == "insufficient"
    assert (
        inst.typeTested[1].rejectionCriterion[0].coding[0].display
        == "insufficient specimen volume"
    )
    assert (
        inst.typeTested[1].rejectionCriterion[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/rejection-criteria"
    )
    assert inst.typeTested[1].rejectionCriterion[1].coding[0].code == "hemolized"
    assert (
        inst.typeTested[1].rejectionCriterion[1].coding[0].display
        == "hemolized specimen"
    )
    assert (
        inst.typeTested[1].rejectionCriterion[1].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/rejection-criteria"
    )
    assert inst.typeTested[1].type.coding[0].code == "119361006"
    assert inst.typeTested[1].type.coding[0].display == "Plasma specimen"
    assert inst.typeTested[1].type.coding[0].system == "http://snomed.info/sct"


def test_specimendefinition_1(base_settings):
    """No. 1 tests collection for SpecimenDefinition.
    Test File: specimendefinition-example-serum-plasma.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "specimendefinition-example-serum-plasma.json"
    )
    inst = specimendefinition.SpecimenDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SpecimenDefinition" == inst.resource_type

    impl_specimendefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SpecimenDefinition" == data["resourceType"]

    inst2 = specimendefinition.SpecimenDefinition(**data)
    impl_specimendefinition_1(inst2)
