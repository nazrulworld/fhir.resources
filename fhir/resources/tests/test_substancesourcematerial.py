# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceSourceMaterial
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import substancesourcematerial
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_substancesourcematerial_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_substancesourcematerial_1(base_settings):
    """No. 1 tests collection for SubstanceSourceMaterial.
    Test File: substancesourcematerial-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "substancesourcematerial-example.json"
    )
    inst = substancesourcematerial.SubstanceSourceMaterial.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "SubstanceSourceMaterial" == inst.get_resource_type()

    impl_substancesourcematerial_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SubstanceSourceMaterial" == data["resourceType"]

    inst2 = substancesourcematerial.SubstanceSourceMaterial(**data)
    impl_substancesourcematerial_1(inst2)
