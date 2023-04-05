# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ObservationDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import observationdefinition


def impl_observationdefinition_1(inst):
    assert inst.category[0].coding[0].code == "laboratory"
    assert (
        inst.category[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/observation-category"
    )
    assert inst.code.coding[0].code == "13980-8"
    assert (
        inst.code.coding[0].display
        == "Albumin/Protein.total in Serum or Plasma by Electrophoresis"
    )
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.method.coding[0].code == "115341008"
    assert inst.method.coding[0].display == "Total measurement"
    assert inst.method.coding[0].system == "http://snomed.info/sct"
    assert inst.multipleResultsAllowed is False
    assert inst.permittedDataType[0] == "Quantity"
    assert inst.permittedUnit[0].code == "%"
    assert inst.permittedUnit[0].display == "%"
    assert inst.permittedUnit[0].system == "http://unitsofmeasure.org"
    assert inst.qualifiedValue[0].context.coding[0].code == "normal"
    assert inst.qualifiedValue[0].context.coding[0].display == "Normal Range"
    assert (
        inst.qualifiedValue[0].context.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/referencerange-meaning"
    )
    assert float(inst.qualifiedValue[0].range.low.value) == float(50)
    assert inst.qualifiedValue[0].rangeCategory == "reference"
    assert inst.qualifiedValue[1].context.coding[0].code == "normal"
    assert inst.qualifiedValue[1].context.coding[0].display == "Normal Range"
    assert (
        inst.qualifiedValue[1].context.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/referencerange-meaning"
    )
    assert float(inst.qualifiedValue[1].range.high.value) == float(40)
    assert inst.qualifiedValue[1].rangeCategory == "critical"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_observationdefinition_1(base_settings):
    """No. 1 tests collection for ObservationDefinition.
    Test File: observationdefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "observationdefinition-example.json"
    inst = observationdefinition.ObservationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ObservationDefinition" == inst.resource_type

    impl_observationdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ObservationDefinition" == data["resourceType"]

    inst2 = observationdefinition.ObservationDefinition(**data)
    impl_observationdefinition_1(inst2)
