# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/InventoryReport
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import inventoryreport


def impl_inventoryreport_1(inst):
    assert inst.countType == "snapshot"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.reportedDateTime == fhirtypes.DateTime.validate("2020-09-22")
    assert inst.status == "draft"
    assert inst.text.status == "generated"


def test_inventoryreport_1(base_settings):
    """No. 1 tests collection for InventoryReport.
    Test File: inventoryreport-example.json
    """
    filename = base_settings["unittest_data_dir"] / "inventoryreport-example.json"
    inst = inventoryreport.InventoryReport.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "InventoryReport" == inst.resource_type

    impl_inventoryreport_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "InventoryReport" == data["resourceType"]

    inst2 = inventoryreport.InventoryReport(**data)
    impl_inventoryreport_1(inst2)
