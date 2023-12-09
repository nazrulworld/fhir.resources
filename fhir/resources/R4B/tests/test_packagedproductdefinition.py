# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PackagedProductDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

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
    assert inst.package.manufacturer[0].reference == "Organization/example"
    assert inst.package.material[0].coding[0].code == "Paperboard"
    assert (
        inst.package.material[0].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert float(inst.package.package[0].containedItem[0].amount.value) == float(10)
    assert (
        inst.package.package[0].containedItem[0].item.reference.reference
        == "ManufacturedItemDefinition/tablet"
    )
    assert inst.package.package[0].manufacturer[0].reference == "Organization/example"
    assert inst.package.package[0].material[0].coding[0].code == "PVC"
    assert (
        inst.package.package[0].material[0].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert inst.package.package[0].material[1].coding[0].code == "PVDC"
    assert (
        inst.package.package[0].material[1].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert inst.package.package[0].material[2].coding[0].code == "alu"
    assert (
        inst.package.package[0].material[2].coding[0].system
        == "http://ema.europa.eu/example/packageItemContainerMaterial"
    )
    assert inst.package.package[0].property[0].type.coding[0].code == "height"
    assert inst.package.package[0].property[0].valueQuantity.code == "mm"
    assert (
        inst.package.package[0].property[0].valueQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.package.package[0].property[0].valueQuantity.unit == "mm"
    assert float(inst.package.package[0].property[0].valueQuantity.value) == float(45)
    assert inst.package.package[0].property[1].type.coding[0].code == "width"
    assert inst.package.package[0].property[1].valueQuantity.code == "mm"
    assert (
        inst.package.package[0].property[1].valueQuantity.system
        == "http://unitsofmeasure.org"
    )
    assert inst.package.package[0].property[1].valueQuantity.unit == "mm"
    assert float(inst.package.package[0].property[1].valueQuantity.value) == float(35)
    assert inst.package.package[0].quantity == 1
    assert inst.package.package[0].shelfLifeStorage[0].periodDuration.code == "a"
    assert (
        inst.package.package[0].shelfLifeStorage[0].periodDuration.system
        == "http://unitsofmeasure.org"
    )
    assert inst.package.package[0].shelfLifeStorage[0].periodDuration.unit == "year"
    assert float(
        inst.package.package[0].shelfLifeStorage[0].periodDuration.value
    ) == float(3)
    assert (
        inst.package.package[0]
        .shelfLifeStorage[0]
        .specialPrecautionsForStorage[0]
        .coding[0]
        .code
        == "none"
    )
    assert (
        inst.package.package[0]
        .shelfLifeStorage[0]
        .specialPrecautionsForStorage[0]
        .coding[0]
        .system
        == "http://ema.europa.eu/example/specialprecautionsforstorage"
    )
    assert (
        inst.package.package[0].shelfLifeStorage[0].type.coding[0].code
        == "ShelfLifeofPackagedMedicinalProduct"
    )
    assert (
        inst.package.package[0].shelfLifeStorage[0].type.coding[0].system
        == "http://ema.europa.eu/example/shelfLifeTypePlaceHolder"
    )
    assert inst.package.package[0].type.coding[0].code == "Blister"
    assert (
        inst.package.package[0].type.coding[0].system
        == "http://ema.europa.eu/example/packageitemcontainertype"
    )
    assert inst.package.property[0].type.coding[0].code == "height"
    assert inst.package.property[0].valueQuantity.code == "mm"
    assert inst.package.property[0].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.package.property[0].valueQuantity.unit == "mm"
    assert float(inst.package.property[0].valueQuantity.value) == float(50)
    assert inst.package.property[1].type.coding[0].code == "width"
    assert inst.package.property[1].valueQuantity.code == "mm"
    assert inst.package.property[1].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.package.property[1].valueQuantity.unit == "mm"
    assert float(inst.package.property[1].valueQuantity.value) == float(45)
    assert inst.package.property[2].type.coding[0].code == "depth"
    assert inst.package.property[2].valueQuantity.code == "mm"
    assert inst.package.property[2].valueQuantity.system == "http://unitsofmeasure.org"
    assert inst.package.property[2].valueQuantity.unit == "mm"
    assert float(inst.package.property[2].valueQuantity.value) == float(23.5)
    assert inst.package.quantity == 1
    assert inst.package.type.coding[0].code == "Carton"
    assert (
        inst.package.type.coding[0].system
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
    assert inst.package.containedItem[0].amount.code == "mL"
    assert inst.package.containedItem[0].amount.system == "http://unitsofmeasure.org"
    assert inst.package.containedItem[0].amount.unit == "ml"
    assert float(inst.package.containedItem[0].amount.value) == float(20)
    assert inst.package.containedItem[0].item.reference.reference == "#liquidItem"
    assert inst.package.containedItem[1].item.reference.reference == "#syringeDevice"
    assert (
        inst.packageFor[0].reference
        == "MedicinalProductDefinition/ProductThatHasThisPackType"
    )
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
