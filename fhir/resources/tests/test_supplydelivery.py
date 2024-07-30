# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyDelivery
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import supplydelivery
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_supplydelivery_1(inst):
    assert inst.contained[0].id == "Item1"
    assert inst.contained[1].id == "Item2"
    assert inst.contained[2].id == "Item3"
    assert inst.destination.display == "St Johns Hospital, Anytown, AnyState"
    assert inst.id == "ISBT128"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.isbt128.org/uri/ProductConsignment"}
        ).valueUri
    )
    assert inst.identifier[0].value == "A999922123450101"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.suppliedItem[0].itemReference.reference == "#Item1"
    assert inst.suppliedItem[1].itemReference.reference == "#Item2"
    assert inst.suppliedItem[2].itemReference.reference == "#Item3"
    assert inst.supplier.display == "Community Blood Center"
    assert (
        inst.supplier.identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.isbt128.org/uri/ProcessorFIN"}
        ).valueUri
    )
    assert inst.supplier.identifier.value == "A9999"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "biologicallyderivedproduct"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/supplydelivery-supplyitemtype"}
        ).valueUri
    )
    assert inst.type.text == "Blood Dispatch"


def test_supplydelivery_1(base_settings):
    """No. 1 tests collection for SupplyDelivery.
    Test File: supplydelivery-example-ISBT128.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "supplydelivery-example-ISBT128.json"
    )
    inst = supplydelivery.SupplyDelivery.model_validate_json(filename.read_bytes())
    assert "SupplyDelivery" == inst.get_resource_type()

    impl_supplydelivery_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SupplyDelivery" == data["resourceType"]

    inst2 = supplydelivery.SupplyDelivery(**data)
    impl_supplydelivery_1(inst2)


def impl_supplydelivery_2(inst):
    assert inst.contained[0].id == "Item1"
    assert inst.contained[1].id == "Item2"
    assert inst.contained[2].id == "Item3"
    assert inst.id == "mphodelivery"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.isbt128.org/uri/ProductConsignment"}
        ).valueUri
    )
    assert inst.identifier[0].value == "A999922123450101"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.suppliedItem[0].itemReference.reference == "#Item1"
    assert float(inst.suppliedItem[0].quantity.value) == float(3)
    assert inst.suppliedItem[1].itemReference.reference == "#Item2"
    assert inst.suppliedItem[2].itemReference.reference == "#Item3"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "biologicallyderivedproduct"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/supplydelivery-supplyitemtype"}
        ).valueUri
    )
    assert inst.type.text == "Blood Dispatch"


def test_supplydelivery_2(base_settings):
    """No. 2 tests collection for SupplyDelivery.
    Test File: supplydelivery-example-mphodelivery.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "supplydelivery-example-mphodelivery.json"
    )
    inst = supplydelivery.SupplyDelivery.model_validate_json(filename.read_bytes())
    assert "SupplyDelivery" == inst.get_resource_type()

    impl_supplydelivery_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SupplyDelivery" == data["resourceType"]

    inst2 = supplydelivery.SupplyDelivery(**data)
    impl_supplydelivery_2(inst2)


def impl_supplydelivery_3(inst):
    assert inst.basedOn[0].reference == "SupplyRequest/simpleorder"
    assert inst.destination.display == "Location 1"
    assert inst.id == "simpledelivery"
    assert inst.identifier[0].value == "Order10284"
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
    assert inst.partOf[0].display == "Central Supply Restock"
    assert inst.status == "completed"
    assert inst.suppliedItem[0].itemCodeableConcept.coding[0].code == "BlueTubes"
    assert (
        inst.suppliedItem[0].itemCodeableConcept.coding[0].display
        == "Blood collect tubes blue cap"
    )
    assert float(inst.suppliedItem[0].quantity.value) == float(10)
    assert inst.supplier.display == "Vendor1"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "device"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/supplydelivery-supplyitemtype"}
        ).valueUri
    )
    assert inst.type.text == "Blood collect tubes blue cap"


def test_supplydelivery_3(base_settings):
    """No. 3 tests collection for SupplyDelivery.
    Test File: supplydelivery-example.json
    """
    filename = base_settings["unittest_data_dir"] / "supplydelivery-example.json"
    inst = supplydelivery.SupplyDelivery.model_validate_json(filename.read_bytes())
    assert "SupplyDelivery" == inst.get_resource_type()

    impl_supplydelivery_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SupplyDelivery" == data["resourceType"]

    inst2 = supplydelivery.SupplyDelivery(**data)
    impl_supplydelivery_3(inst2)


def impl_supplydelivery_4(inst):
    assert inst.destination.display == "Home care dept"
    assert inst.id == "pumpdelivery"
    assert inst.identifier[0].assigner.display == "SupplierDeliveryNr"
    assert inst.identifier[0].value == "98398459409"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.patient.display == "Mr. Belpit"
    assert inst.receiver[0].display == "Nurse Smith"
    assert inst.status == "in-progress"
    assert inst.supplier.display == "ACME distribution"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_supplydelivery_4(base_settings):
    """No. 4 tests collection for SupplyDelivery.
    Test File: supplydelivery-example-pumpdelivery.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "supplydelivery-example-pumpdelivery.json"
    )
    inst = supplydelivery.SupplyDelivery.model_validate_json(filename.read_bytes())
    assert "SupplyDelivery" == inst.get_resource_type()

    impl_supplydelivery_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "SupplyDelivery" == data["resourceType"]

    inst2 = supplydelivery.SupplyDelivery(**data)
    impl_supplydelivery_4(inst2)
