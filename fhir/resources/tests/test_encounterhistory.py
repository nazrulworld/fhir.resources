# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EncounterHistory
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import encounterhistory
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_encounterhistory_1(inst):
    assert inst.class_fhir.coding[0].code == "IMP"
    assert inst.class_fhir.coding[0].display == "inpatient encounter"
    assert (
        inst.class_fhir.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://www.amc.nl/zorgportal/identifiers/visits"
        ).valueUri
    )
    assert inst.identifier[0].use == "official"
    assert inst.identifier[0].value == "v2452"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "in-progress"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Encounter with '
        "patient @example</div>"
    )
    assert inst.text.status == "generated"


def test_encounterhistory_1(base_settings):
    """No. 1 tests collection for EncounterHistory.
    Test File: encounterhistory-example.json
    """
    filename = base_settings["unittest_data_dir"] / "encounterhistory-example.json"
    inst = encounterhistory.EncounterHistory.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "EncounterHistory" == inst.get_resource_type()

    impl_encounterhistory_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EncounterHistory" == data["resourceType"]

    inst2 = encounterhistory.EncounterHistory(**data)
    impl_encounterhistory_1(inst2)
