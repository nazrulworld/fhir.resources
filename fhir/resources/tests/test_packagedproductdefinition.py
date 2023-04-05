# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PackagedProductDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import packagedproductdefinition


def impl_packagedproductdefinition_1(inst):
    assert (
        inst.description == "ALU-PVC/PVDC BLISTERS. CARTONS OF 10 FILM-COATED TABLETS."
    )
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://ema.europa.eu/example/pcid"
    assert inst.identifier[0].value == "{PCID}"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.packaging.manufacturer[0].reference == "Organization/example"
    assert inst.packaging.material[0].coding[0].code == "Paperboard"
    assert (
        inst.packaging.material[0].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert float(inst.packaging.packaging[0].containedItem[0].amount.value) == float(10)
    assert (
        inst.packaging.packaging[0].containedItem[0].item.reference.reference
        == "ManufacturedItemDefinition/tablet"
    )
    assert (
        inst.packaging.packaging[0].manufacturer[0].reference == "Organization/example"
    )
    assert inst.packaging.packaging[0].material[0].coding[0].code == "PVC"
    assert (
        inst.packaging.packaging[0].material[0].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert inst.packaging.packaging[0].material[1].coding[0].code == "PVDC"
    assert (
        inst.packaging.packaging[0].material[1].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert inst.packaging.packaging[0].material[2].coding[0].code == "alu"
    assert (
        inst.packaging.packaging[0].material[2].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert inst.packaging.packaging[0].property[0].type.coding[0].code == "height"
    assert inst.packaging.packaging[0].property[0].valueQuantity.code == "mm"
    assert (
        inst.packaging.packaging[0].property[0].valueQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.packaging.packaging[0].property[0].valueQuantity.unit == "mm"
    assert float(inst.packaging.packaging[0].property[0].valueQuantity.value) == float(
        45
    )
    assert inst.packaging.packaging[0].property[1].type.coding[0].code == "width"
    assert inst.packaging.packaging[0].property[1].valueQuantity.code == "mm"
    assert (
        inst.packaging.packaging[0].property[1].valueQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.packaging.packaging[0].property[1].valueQuantity.unit == "mm"
    assert float(inst.packaging.packaging[0].property[1].valueQuantity.value) == float(
        35
    )
    assert inst.packaging.packaging[0].quantity == 1
    assert inst.packaging.packaging[0].shelfLifeStorage[0].periodDuration.code == "a"
    assert (
        inst.packaging.packaging[0].shelfLifeStorage[0].periodDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.packaging.packaging[0].shelfLifeStorage[0].periodDuration.unit == "year"
    assert float(
        inst.packaging.packaging[0].shelfLifeStorage[0].periodDuration.value
    ) == float(3)
    assert (
        inst.packaging.packaging[0]
        .shelfLifeStorage[0]
        .specialPrecautionsForStorage[0]
        .coding[0]
        .code
        == "none"
    )
    assert (
        inst.packaging.packaging[0]
        .shelfLifeStorage[0]
        .specialPrecautionsForStorage[0]
        .coding[0]
        .system
        == "http://ema.europa.eu/example/specialprecautionsforstorage"
    )
    assert (
        inst.packaging.packaging[0].shelfLifeStorage[0].type.coding[0].code
        == "ShelfLifeofPackagedMedicinalProduct"
    )
    assert (
        inst.packaging.packaging[0].shelfLifeStorage[0].type.coding[0].system
        == "http://ema.europa.eu/example/shelfLifeTypePlaceHolder"
    )
    assert inst.packaging.packaging[0].type.coding[0].code == "Blister"
    assert (
        inst.packaging.packaging[0].type.coding[0].system
        == "http://ema.europa.eu/example/packageitemcontainertype"
    )
    assert inst.packaging.property[0].type.coding[0].code == "height"
    assert inst.packaging.property[0].valueQuantity.code == "mm"
    assert (
        inst.packaging.property[0].valueQuantity.system == "http://unitsofmeasure.org"
    )
    assert inst.packaging.property[0].valueQuantity.unit == "mm"
    assert float(inst.packaging.property[0].valueQuantity.value) == float(50)
    assert inst.packaging.property[1].type.coding[0].code == "width"
    assert inst.packaging.property[1].valueQuantity.code == "mm"
    assert (
        inst.packaging.property[1].valueQuantity.system == "http://unitsofmeasure.org"
    )
    assert inst.packaging.property[1].valueQuantity.unit == "mm"
    assert float(inst.packaging.property[1].valueQuantity.value) == float(45)
    assert inst.packaging.property[2].type.coding[0].code == "depth"
    assert inst.packaging.property[2].valueQuantity.code == "mm"
    assert (
        inst.packaging.property[2].valueQuantity.system == "http://unitsofmeasure.org"
    )
    assert inst.packaging.property[2].valueQuantity.unit == "mm"
    assert float(inst.packaging.property[2].valueQuantity.value) == float(23.5)
    assert inst.packaging.quantity == 1
    assert inst.packaging.type.coding[0].code == "Carton"
    assert (
        inst.packaging.type.coding[0].system
        == "http://ema.europa.eu/example/packageitemcontainertype"
    )
    assert inst.text.status == "generated"


def test_packagedproductdefinition_1(base_settings):
    """No. 1 tests collection for PackagedProductDefinition.
    Test File: packagedproductdefinition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "packagedproductdefinition-example.json"
    )
    inst = packagedproductdefinition.PackagedProductDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PackagedProductDefinition" == inst.resource_type

    impl_packagedproductdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PackagedProductDefinition" == data["resourceType"]

    inst2 = packagedproductdefinition.PackagedProductDefinition(**data)
    impl_packagedproductdefinition_1(inst2)


def impl_packagedproductdefinition_2(inst):
    assert inst.contained[0].id == "syringeDevice"
    assert inst.contained[1].id == "liquidItem"
    assert inst.id == "package-with-liquid-and-syringe"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.packageFor[0].reference
        == "MedicinalProductDefinition/ProductThatHasThisPackType"
    )
    assert inst.packaging.containedItem[0].amount.code == "mL"
    assert inst.packaging.containedItem[0].amount.system == "http://unitsofmeasure.org"
    assert inst.packaging.containedItem[0].amount.unit == "ml"
    assert float(inst.packaging.containedItem[0].amount.value) == float(20)
    assert inst.packaging.containedItem[0].item.reference.reference == "#liquidItem"
    assert inst.packaging.containedItem[1].item.reference.reference == "#syringeDevice"
    assert inst.text.status == "generated"


def test_packagedproductdefinition_2(base_settings):
    """No. 2 tests collection for PackagedProductDefinition.
    Test File: packagedproductdefinition-example-co-packaged-liquid-and-syringe.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "packagedproductdefinition-example-co-packaged-liquid-and-syringe.json"
    )
    inst = packagedproductdefinition.PackagedProductDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "PackagedProductDefinition" == inst.resource_type

    impl_packagedproductdefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "PackagedProductDefinition" == data["resourceType"]

    inst2 = packagedproductdefinition.PackagedProductDefinition(**data)
    impl_packagedproductdefinition_2(inst2)
