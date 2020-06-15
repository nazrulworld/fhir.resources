# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicinalproductpackaged


def impl_medicinalproductpackaged_1(inst):
    assert inst.batchIdentifier[
        0
    ].outerPackaging.period.end == fhirtypes.DateTime.validate(
        "2016-06-06T11:15:33+10:00"
    )
    assert (
        inst.batchIdentifier[0].outerPackaging.system
        == "http://ema.europa.eu/example/baid1"
    )
    assert inst.batchIdentifier[0].outerPackaging.value == "AAF5699"
    assert (
        inst.description == "ALU-PVC/PVDC BLISTERS. CARTONS OF 10 FILM-COATED TABLETS. "
    )
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://ema.europa.eu/example/pcid"
    assert inst.identifier[0].value == "{PCID}"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.packageItem[0].manufacturer[0].reference == "Organization/example"
    assert inst.packageItem[0].material[0].coding[0].code == "PVC"
    assert (
        inst.packageItem[0].material[0].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert inst.packageItem[0].material[1].coding[0].code == "PVDC"
    assert (
        inst.packageItem[0].material[1].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert inst.packageItem[0].material[2].coding[0].code == "alu"
    assert (
        inst.packageItem[0].material[2].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert (
        inst.packageItem[0].packageItem[0].manufacturedItem[0].reference
        == "MedicinalProductManufactured/example"
    )
    assert (
        inst.packageItem[0].packageItem[0].manufacturer[0].reference
        == "Organization/example"
    )
    assert inst.packageItem[0].packageItem[0].material[0].coding[0].code == "Paperboard"
    assert (
        inst.packageItem[0].packageItem[0].material[0].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert (
        inst.packageItem[0].packageItem[0].physicalCharacteristics.height.unit == "mm"
    )
    assert float(
        inst.packageItem[0].packageItem[0].physicalCharacteristics.height.value
    ) == float(125)
    assert inst.packageItem[0].packageItem[0].physicalCharacteristics.width.unit == "mm"
    assert float(
        inst.packageItem[0].packageItem[0].physicalCharacteristics.width.value
    ) == float(45)
    assert inst.packageItem[0].packageItem[0].quantity.unit == "1"
    assert float(inst.packageItem[0].packageItem[0].quantity.value) == float(1)
    assert inst.packageItem[0].packageItem[0].shelfLifeStorage[0].period.unit == "a"
    assert float(
        inst.packageItem[0].packageItem[0].shelfLifeStorage[0].period.value
    ) == float(3)
    assert inst.packageItem[0].packageItem[0].shelfLifeStorage[
        0
    ].specialPrecautionsForStorage[0].coding[0].code == (
        "Thismedicinalproductdoesnotrequireanyspecialstoragecondition" "."
    )
    assert (
        inst.packageItem[0]
        .packageItem[0]
        .shelfLifeStorage[0]
        .specialPrecautionsForStorage[0]
        .coding[0]
        .system
        == "http://ema.europa.eu/example/specialprecautionsforstorage"
    )
    assert (
        inst.packageItem[0].packageItem[0].shelfLifeStorage[0].type.coding[0].code
        == "ShelfLifeofPackagedMedicinalProduct"
    )
    assert (
        inst.packageItem[0].packageItem[0].shelfLifeStorage[0].type.coding[0].system
        == "http://ema.europa.eu/example/shelfLifeTypePlaceHolder"
    )
    assert inst.packageItem[0].packageItem[0].type.coding[0].code == "Blister"
    assert (
        inst.packageItem[0].packageItem[0].type.coding[0].system
        == "http://ema.europa.eu/example/packageitemcontainertype"
    )
    assert inst.packageItem[0].physicalCharacteristics.depth.unit == "mm"
    assert float(inst.packageItem[0].physicalCharacteristics.depth.value) == float(23.5)
    assert inst.packageItem[0].physicalCharacteristics.height.unit == "mm"
    assert float(inst.packageItem[0].physicalCharacteristics.height.value) == float(50)
    assert inst.packageItem[0].physicalCharacteristics.width.unit == "mm"
    assert float(inst.packageItem[0].physicalCharacteristics.width.value) == float(136)
    assert inst.packageItem[0].quantity.unit == "1"
    assert float(inst.packageItem[0].quantity.value) == float(1)
    assert inst.packageItem[0].type.coding[0].code == "Carton"
    assert (
        inst.packageItem[0].type.coding[0].system
        == "http://ema.europa.eu/example/packageitemcontainertype"
    )
    assert inst.text.status == "generated"


def test_medicinalproductpackaged_1(base_settings):
    """No. 1 tests collection for MedicinalProductPackaged.
    Test File: medicinalproductpackaged-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicinalproductpackaged-example.json"
    )
    inst = medicinalproductpackaged.MedicinalProductPackaged.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductPackaged" == inst.resource_type

    impl_medicinalproductpackaged_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductPackaged" == data["resourceType"]

    inst2 = medicinalproductpackaged.MedicinalProductPackaged(**data)
    impl_medicinalproductpackaged_1(inst2)
