# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyRequest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import supplyrequest


def impl_supplyrequest_1(inst):
    assert inst.authoredOn == fhirtypes.DateTime.validate("2016-12-31")
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
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2016-12-31")
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
    inst = supplyrequest.SupplyRequest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SupplyRequest" == inst.resource_type

    impl_supplyrequest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SupplyRequest" == data["resourceType"]

    inst2 = supplyrequest.SupplyRequest(**data)
    impl_supplyrequest_1(inst2)
