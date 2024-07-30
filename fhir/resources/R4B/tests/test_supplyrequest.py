# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import supplyrequest
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_supplyrequest_1(inst):
    assert (
        inst.authoredOn
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-12-31"}
        ).valueDateTime
    )
    assert inst.category.coding[0].code == "central"
    assert inst.category.coding[0].display == "Central Stock Resupply"
    assert inst.deliverFrom.display == "Location 1"
    assert inst.deliverTo.display == "GoodHealth Clinic Receiving"
    assert inst.id == "simpleorder"
    assert inst.identifier[0].value == "Order10284"
    assert inst.itemCodeableConcept.coding[0].code == "BlueTubes"
    assert inst.itemCodeableConcept.coding[0].display == "Blood collect tubes blue cap"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.occurrenceDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-12-31"}
        ).valueDateTime
    )
    assert inst.priority == "asap"
    assert float(inst.quantity.value) == float(10)
    assert inst.reasonCode[0].coding[0].code == "stock_low"
    assert inst.reasonCode[0].coding[0].display == "Refill due to low stock"
    assert inst.requester.display == "Henry Seven"
    assert inst.status == "active"
    assert inst.supplier[0].display == "Vendor1"
    assert inst.text.status == "generated"


def test_supplyrequest_1(base_settings):
    """No. 1 tests collection for SupplyRequest.
    Test File: supplyrequest-example-simpleorder.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "supplyrequest-example-simpleorder.json"
    )
    inst = supplyrequest.SupplyRequest.model_validate_json(filename.read_bytes())
    assert "SupplyRequest" == inst.get_resource_type()

    impl_supplyrequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SupplyRequest" == data["resourceType"]

    inst2 = supplyrequest.SupplyRequest(**data)
    impl_supplyrequest_1(inst2)
