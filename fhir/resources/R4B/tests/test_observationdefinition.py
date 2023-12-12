# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ObservationDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import observationdefinition


def impl_observationdefinition_1(inst):
    assert inst.code.coding[0].code == "15074-8"
    assert inst.code.coding[0].display == "Glucose [Moles/volume] in Blood"
    assert inst.code.coding[0].system == "http://loinc.org"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
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
