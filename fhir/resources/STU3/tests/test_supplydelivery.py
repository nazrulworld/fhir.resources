# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyDelivery
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import supplydelivery


def impl_supplydelivery_1(inst):
    assert inst.basedOn[0].reference == "SupplyRequest/simpleorder"
    assert inst.destination.display == "Location 1"
    assert inst.id == "simpledelivery"
    assert inst.identifier.value == "Order10284"
    assert inst.occurrenceDateTime == fhirtypes.DateTime.validate("2016-12-31")
    assert inst.partOf[0].display == "Central Supply Restock"
    assert inst.status == "completed"
    assert inst.suppliedItem.itemCodeableConcept.coding[0].code == "BlueTubes"
    assert (
        inst.suppliedItem.itemCodeableConcept.coding[0].display
        == "Blood collect tubes blue cap"
    )
    assert float(inst.suppliedItem.quantity.value) == float(10)
    assert inst.supplier.display == "Vendor1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "device"
    assert inst.type.coding[0].system == "http://hl7.org/fhir/supply-item-type"
    assert inst.type.text == "Blood collect tubes blue cap"


def test_supplydelivery_1(base_settings):
    """No. 1 tests collection for SupplyDelivery.
    Test File: supplydelivery-example.json
    """
    filename = base_settings["unittest_data_dir"] / "supplydelivery-example.json"
    inst = supplydelivery.SupplyDelivery.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SupplyDelivery" == inst.resource_type

    impl_supplydelivery_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SupplyDelivery" == data["resourceType"]

    inst2 = supplydelivery.SupplyDelivery(**data)
    impl_supplydelivery_1(inst2)


def impl_supplydelivery_2(inst):
    assert inst.destination.display == "Home care dept"
    assert inst.id == "pumpdelivery"
    assert inst.identifier.assigner.display == "SupplierDeliveryNr"
    assert inst.identifier.value == "98398459409"
    assert inst.patient.display == "Mr. Belpit"
    assert inst.receiver[0].display == "Nurse Smith"
    assert inst.status == "in-progress"
    assert inst.supplier.display == "ACME distribution"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_supplydelivery_2(base_settings):
    """No. 2 tests collection for SupplyDelivery.
    Test File: supplydelivery-example-pumpdelivery.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "supplydelivery-example-pumpdelivery.json"
    )
    inst = supplydelivery.SupplyDelivery.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "SupplyDelivery" == inst.resource_type

    impl_supplydelivery_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "SupplyDelivery" == data["resourceType"]

    inst2 = supplydelivery.SupplyDelivery(**data)
    impl_supplydelivery_2(inst2)
