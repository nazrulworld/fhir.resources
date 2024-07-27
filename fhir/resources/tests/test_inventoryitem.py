# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/InventoryItem
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import inventoryitem
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_inventoryitem_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_inventoryitem_1(base_settings):
    """No. 1 tests collection for InventoryItem.
    Test File: inventoryitem-example.json
    """
    filename = base_settings["unittest_data_dir"] / "inventoryitem-example.json"
    inst = inventoryitem.InventoryItem.model_validate_json(Path(filename).read_bytes())
    assert "InventoryItem" == inst.get_resource_type()

    impl_inventoryitem_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "InventoryItem" == data["resourceType"]

    inst2 = inventoryitem.InventoryItem(**data)
    impl_inventoryitem_1(inst2)
