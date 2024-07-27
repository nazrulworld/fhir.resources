# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SpecimenDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import specimendefinition
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_specimendefinition_1(inst):
    assert inst.experimental is False
    assert inst.id == "2364"
    assert inst.identifier.value == "12345"
    assert inst.patientPreparation[0].text == "12 hour fasting"
    assert inst.patientPreparation[1].coding[0].code == "263678003"
    assert inst.patientPreparation[1].coding[0].display == "At rest"
    assert (
        inst.patientPreparation[1].coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.timeAspect == "preferrably morning time"
    assert inst.title == "Example Specimen Definition for Testing"
    assert inst.typeCollected.coding[0].code == "122555007"
    assert inst.typeCollected.coding[0].display == "Venous blood specimen"
    assert (
        inst.typeCollected.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.typeTested[0].container.cap.coding[0].code == "yellow"
    assert inst.typeTested[0].container.cap.coding[0].display == "yellow cap"
    assert (
        inst.typeTested[0].container.cap.coding[0].system
        == ExternalValidatorModel(valueUri="urn:iso:std:iso:6710:2017").valueUri
    )
    assert inst.typeTested[0].container.material.coding[0].code == "61088005"
    assert inst.typeTested[0].container.material.coding[0].display == "plastic"
    assert (
        inst.typeTested[0].container.material.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.typeTested[0].container.minimumVolumeQuantity.code == "mL"
    assert (
        inst.typeTested[0].container.minimumVolumeQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[0].container.minimumVolumeQuantity.unit == "ml"
    assert float(inst.typeTested[0].container.minimumVolumeQuantity.value) == float(2)
    assert inst.typeTested[0].container.type.coding[0].code == "702281005"
    assert inst.typeTested[0].container.type.coding[0].display == (
        "Evacuated blood collection tube, thrombin/clot activator/gel" " separator"
    )
    assert (
        inst.typeTested[0].container.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.typeTested[0].handling[0].maxDuration.code == "min"
    assert (
        inst.typeTested[0].handling[0].maxDuration.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
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
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[0].handling[0].temperatureRange.high.unit == "°C"
    assert float(inst.typeTested[0].handling[0].temperatureRange.high.value) == float(
        25
    )
    assert inst.typeTested[0].handling[0].temperatureRange.low.code == "Cel"
    assert (
        inst.typeTested[0].handling[0].temperatureRange.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[0].handling[0].temperatureRange.low.unit == "°C"
    assert float(inst.typeTested[0].handling[0].temperatureRange.low.value) == float(15)
    assert inst.typeTested[0].handling[1].maxDuration.code == "h"
    assert (
        inst.typeTested[0].handling[1].maxDuration.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
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
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[0].handling[1].temperatureRange.high.unit == "°C"
    assert float(inst.typeTested[0].handling[1].temperatureRange.high.value) == float(8)
    assert inst.typeTested[0].handling[1].temperatureRange.low.code == "Cel"
    assert (
        inst.typeTested[0].handling[1].temperatureRange.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[0].handling[1].temperatureRange.low.unit == "°C"
    assert float(inst.typeTested[0].handling[1].temperatureRange.low.value) == float(2)
    assert inst.typeTested[0].isDerived is False
    assert inst.typeTested[0].preference == "preferred"
    assert inst.typeTested[0].type.coding[0].code == "119364003"
    assert inst.typeTested[0].type.coding[0].display == "Serum specimen"
    assert (
        inst.typeTested[0].type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.typeTested[1].container.cap.coding[0].code == "green"
    assert inst.typeTested[1].container.cap.coding[0].display == "green cap"
    assert (
        inst.typeTested[1].container.cap.coding[0].system
        == ExternalValidatorModel(valueUri="urn:iso:std:iso:6710:2017").valueUri
    )
    assert inst.typeTested[1].container.material.coding[0].code == "32039001"
    assert inst.typeTested[1].container.material.coding[0].display == "glass"
    assert (
        inst.typeTested[1].container.material.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.typeTested[1].container.minimumVolumeQuantity.code == "mL"
    assert (
        inst.typeTested[1].container.minimumVolumeQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[1].container.minimumVolumeQuantity.unit == "ml"
    assert float(inst.typeTested[1].container.minimumVolumeQuantity.value) == float(2)
    assert inst.typeTested[1].container.type.coding[0].code == "702281005"
    assert inst.typeTested[1].container.type.coding[0].display == (
        "Evacuated blood collection tube, thrombin/clot activator/gel" " separator"
    )
    assert (
        inst.typeTested[1].container.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.typeTested[1].handling[0].maxDuration.code == "min"
    assert (
        inst.typeTested[1].handling[0].maxDuration.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
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
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[1].handling[0].temperatureRange.high.unit == "°C"
    assert float(inst.typeTested[1].handling[0].temperatureRange.high.value) == float(
        25
    )
    assert inst.typeTested[1].handling[0].temperatureRange.low.code == "Cel"
    assert (
        inst.typeTested[1].handling[0].temperatureRange.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[1].handling[0].temperatureRange.low.unit == "°C"
    assert float(inst.typeTested[1].handling[0].temperatureRange.low.value) == float(15)
    assert inst.typeTested[1].handling[1].maxDuration.code == "h"
    assert (
        inst.typeTested[1].handling[1].maxDuration.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
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
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[1].handling[1].temperatureRange.high.unit == "°C"
    assert float(inst.typeTested[1].handling[1].temperatureRange.high.value) == float(8)
    assert inst.typeTested[1].handling[1].temperatureRange.low.code == "Cel"
    assert (
        inst.typeTested[1].handling[1].temperatureRange.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
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
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/rejection-criteria"
        ).valueUri
    )
    assert inst.typeTested[1].rejectionCriterion[1].coding[0].code == "hemolized"
    assert (
        inst.typeTested[1].rejectionCriterion[1].coding[0].display
        == "hemolized specimen"
    )
    assert (
        inst.typeTested[1].rejectionCriterion[1].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/rejection-criteria"
        ).valueUri
    )
    assert inst.typeTested[1].type.coding[0].code == "119361006"
    assert inst.typeTested[1].type.coding[0].display == "Plasma specimen"
    assert (
        inst.typeTested[1].type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert (
        inst.url
        == ExternalValidatorModel(
            valueUri="http://example.com/specdef/v1/12345"
        ).valueUri
    )


def test_specimendefinition_1(base_settings):
    """No. 1 tests collection for SpecimenDefinition.
    Test File: specimendefinition-example-serum-plasma.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "specimendefinition-example-serum-plasma.json"
    )
    inst = specimendefinition.SpecimenDefinition.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "SpecimenDefinition" == inst.get_resource_type()

    impl_specimendefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SpecimenDefinition" == data["resourceType"]

    inst2 = specimendefinition.SpecimenDefinition(**data)
    impl_specimendefinition_1(inst2)


def impl_specimendefinition_2(inst):
    assert inst.experimental is True
    assert inst.id == "7"
    assert inst.identifier.value == "123455"
    assert inst.patientPreparation[0].text == "no strict fasting"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Venous blood specimen"
    assert inst.typeCollected.coding[0].code == "122555007"
    assert (
        inst.typeCollected.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.typeCollected.text == "Venous blood specimen (specimen)"
    assert inst.typeTested[0].container.cap.coding[0].code == "yellow"
    assert inst.typeTested[0].container.cap.coding[0].display == "yellow cap"
    assert (
        inst.typeTested[0].container.cap.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/5.1.0/CodeSystem-container-cap.html"
        ).valueUri
    )
    assert inst.typeTested[0].container.material.text == "glass"
    assert inst.typeTested[0].container.minimumVolumeQuantity.code == "mL"
    assert (
        inst.typeTested[0].container.minimumVolumeQuantity.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[0].container.minimumVolumeQuantity.unit == "ml"
    assert float(inst.typeTested[0].container.minimumVolumeQuantity.value) == float(2)
    assert inst.typeTested[0].container.type.coding[0].code == "702281005"
    assert inst.typeTested[0].container.type.coding[0].display == (
        "Evacuated blood collection tube with thrombin and clot "
        "activator and gel separator"
    )
    assert (
        inst.typeTested[0].container.type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.typeTested[0].handling[0].maxDuration.code == "h"
    assert (
        inst.typeTested[0].handling[0].maxDuration.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert float(inst.typeTested[0].handling[0].maxDuration.value) == float(12)
    assert inst.typeTested[0].handling[0].temperatureQualifier.coding[0].code == "room"
    assert (
        inst.typeTested[0].handling[0].temperatureQualifier.coding[0].display
        == "room temperature"
    )
    assert inst.typeTested[0].handling[0].temperatureRange.high.code == "Cel"
    assert (
        inst.typeTested[0].handling[0].temperatureRange.high.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[0].handling[0].temperatureRange.high.unit == "°C"
    assert float(inst.typeTested[0].handling[0].temperatureRange.high.value) == float(
        25
    )
    assert inst.typeTested[0].handling[0].temperatureRange.low.code == "Cel"
    assert (
        inst.typeTested[0].handling[0].temperatureRange.low.system
        == ExternalValidatorModel(valueUri="http://unitsofmeasure.org").valueUri
    )
    assert inst.typeTested[0].handling[0].temperatureRange.low.unit == "°C"
    assert float(inst.typeTested[0].handling[0].temperatureRange.low.value) == float(15)
    assert inst.typeTested[0].isDerived is True
    assert inst.typeTested[0].preference == "preferred"
    assert inst.typeTested[0].type.coding[0].code == "119364003"
    assert (
        inst.typeTested[0].type.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.typeTested[0].type.text == "Serum specimen (specimen)"
    assert (
        inst.url
        == ExternalValidatorModel(
            valueUri="http://example-lab.com/specdef/123455"
        ).valueUri
    )


def test_specimendefinition_2(base_settings):
    """No. 2 tests collection for SpecimenDefinition.
    Test File: specimendefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "specimendefinition-example.json"
    inst = specimendefinition.SpecimenDefinition.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "SpecimenDefinition" == inst.get_resource_type()

    impl_specimendefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SpecimenDefinition" == data["resourceType"]

    inst2 = specimendefinition.SpecimenDefinition(**data)
    impl_specimendefinition_2(inst2)
