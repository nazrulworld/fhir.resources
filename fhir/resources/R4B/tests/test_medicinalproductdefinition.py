# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicinalproductdefinition


def impl_medicinalproductdefinition_1(inst):
    assert inst.contained[0].id == "ppd1"
    assert inst.contained[1].id == "i1"
    assert inst.id == "product-with-contained-package-and-ingredient"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].productName == "Exampleocillin"
    assert inst.text.status == "generated"


def test_medicinalproductdefinition_1(base_settings):
    """No. 1 tests collection for MedicinalProductDefinition.
    Test File: medicinalproductdefinition-with-contained-package-and-ingredient.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "medicinalproductdefinition-with-contained-package-and-ingredient.json"
    )
    inst = medicinalproductdefinition.MedicinalProductDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductDefinition" == inst.resource_type

    impl_medicinalproductdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductDefinition" == data["resourceType"]

    inst2 = medicinalproductdefinition.MedicinalProductDefinition(**data)
    impl_medicinalproductdefinition_1(inst2)


def impl_medicinalproductdefinition_2(inst):
    assert inst.classification[0].coding[0].code == "B01A"
    assert inst.classification[0].coding[0].system == "http://www.whocc.no/atc/example"
    assert inst.combinedPharmaceuticalDoseForm.coding[0].code == "tablet"
    assert (
        inst.combinedPharmaceuticalDoseForm.coding[0].system
        == "http://example.org.uk/fhir/dosefom"
    )
    assert (
        inst.crossReference[0].product.reference.reference
        == "MedicinalProductDefinition/genericEquilidonium"
    )
    assert inst.id == "equilidem-basics"
    assert inst.identifier[0].system == "http://example.org.uk/fhir/product"
    assert inst.identifier[0].value == "Equilidem25"
    assert inst.ingredient[0].text == "Equilidonium Phosphate"
    assert inst.ingredient[1].text == "Calcium Carbonate"
    assert inst.legalStatusOfSupply.coding[0].code == "POM"
    assert inst.legalStatusOfSupply.coding[0].display == "Prescription only medicine"
    assert (
        inst.legalStatusOfSupply.coding[0].system
        == "http://example.org.uk/fhir/legalstatusofsupply"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].productName == "Equilidem 2.5 mg film-coated tablets"
    assert inst.operation[0].organization[0].display == "EquiliDrugCo Inc."
    assert inst.text.status == "generated"


def test_medicinalproductdefinition_2(base_settings):
    """No. 2 tests collection for MedicinalProductDefinition.
    Test File: medicinalproductdefinition-example-equilidem-basics.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "medicinalproductdefinition-example-equilidem-basics.json"
    )
    inst = medicinalproductdefinition.MedicinalProductDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductDefinition" == inst.resource_type

    impl_medicinalproductdefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductDefinition" == data["resourceType"]

    inst2 = medicinalproductdefinition.MedicinalProductDefinition(**data)
    impl_medicinalproductdefinition_2(inst2)


def impl_medicinalproductdefinition_3(inst):
    assert inst.classification[0].coding[0].code == "B01A"
    assert inst.classification[0].coding[0].system == "http://www.whocc.no/atc/example"
    assert inst.combinedPharmaceuticalDoseForm.coding[0].code == "tablet"
    assert (
        inst.combinedPharmaceuticalDoseForm.coding[0].system
        == "http://example.org.uk/fhir/dosefom"
    )
    assert inst.contained[0].id == "EquilidoniumPhosphate"
    assert inst.contained[1].id == "CalciumCarbonate"
    assert (
        inst.crossReference[0].product.reference.reference
        == "MedicinalProductDefinition/genericEquilidonium"
    )
    assert inst.id == "equilidem-with-ing-and-auth"
    assert inst.identifier[0].system == "http://example.org.uk/fhir/product"
    assert inst.identifier[0].value == "Equilidem25"
    assert inst.legalStatusOfSupply.coding[0].code == "POM"
    assert inst.legalStatusOfSupply.coding[0].display == "Prescription only medicine"
    assert (
        inst.legalStatusOfSupply.coding[0].system
        == "http://example.org.uk/fhir/legalstatusofsupply"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].productName == "Equilidem 2.5 mg film-coated tablets"
    assert inst.operation[0].organization[0].display == "EquiliDrugCo Processing Inc."
    assert inst.text.status == "generated"


def test_medicinalproductdefinition_3(base_settings):
    """No. 3 tests collection for MedicinalProductDefinition.
    Test File: medicinalproductdefinition-example-equilidem-using-ingredient-and-auth.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "medicinalproductdefinition-example-equilidem-using-ingredient-and-auth.json"
    )
    inst = medicinalproductdefinition.MedicinalProductDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductDefinition" == inst.resource_type

    impl_medicinalproductdefinition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductDefinition" == data["resourceType"]

    inst2 = medicinalproductdefinition.MedicinalProductDefinition(**data)
    impl_medicinalproductdefinition_3(inst2)


def impl_medicinalproductdefinition_4(inst):
    assert (
        inst.combinedPharmaceuticalDoseForm.coding[0].code == "solution for injection"
    )
    assert (
        inst.combinedPharmaceuticalDoseForm.coding[0].system
        == "http://example.org.uk/fhir/doseform"
    )
    assert inst.contained[0].id == "package"
    assert inst.contained[1].id == "syringeDevice"
    assert inst.contained[2].id == "liquidItem"
    assert inst.id == "drug-and-device"
    assert inst.identifier[0].system == "http://example.org.uk/fhir/product"
    assert inst.identifier[0].value == "Wonderdrug+"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].productName == "Wonderdrug+ liquid 20ml"
    assert inst.text.status == "generated"


def test_medicinalproductdefinition_4(base_settings):
    """No. 4 tests collection for MedicinalProductDefinition.
    Test File: medicinalproductdefinition-example-co-packaged-liquid-and-syringe.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "medicinalproductdefinition-example-co-packaged-liquid-and-syringe.json"
    )
    inst = medicinalproductdefinition.MedicinalProductDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductDefinition" == inst.resource_type

    impl_medicinalproductdefinition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductDefinition" == data["resourceType"]

    inst2 = medicinalproductdefinition.MedicinalProductDefinition(**data)
    impl_medicinalproductdefinition_4(inst2)


def impl_medicinalproductdefinition_5(inst):
    assert (
        inst.combinedPharmaceuticalDoseForm.coding[0].code
        == "Powder and solution for injection with itegral syringe"
    )
    assert (
        inst.combinedPharmaceuticalDoseForm.coding[0].system
        == "http://example.org.uk/fhir/doseform"
    )
    assert inst.contained[0].id == "package"
    assert inst.contained[1].id == "solventItem"
    assert inst.contained[2].id == "powderItem"
    assert inst.contained[3].id == "syringeDevice"
    assert inst.contained[4].id == "administrable-form"
    assert inst.id == "drug-and-device-complete"
    assert inst.identifier[0].system == "http://example.org.uk/fhir/product"
    assert inst.identifier[0].value == "Wonderdrug+"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].productName == "Wonderdrug liquid 20ml (integral syringe)"
    assert inst.text.status == "generated"


def test_medicinalproductdefinition_5(base_settings):
    """No. 5 tests collection for MedicinalProductDefinition.
    Test File: medicinalproductdefinition-example-co-packaged-liquid-and-syringe-complete.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "medicinalproductdefinition-example-co-packaged-liquid-and-syringe-complete.json"
    )
    inst = medicinalproductdefinition.MedicinalProductDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductDefinition" == inst.resource_type

    impl_medicinalproductdefinition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductDefinition" == data["resourceType"]

    inst2 = medicinalproductdefinition.MedicinalProductDefinition(**data)
    impl_medicinalproductdefinition_5(inst2)


def impl_medicinalproductdefinition_6(inst):
    assert (
        inst.combinedPharmaceuticalDoseForm.coding[0].code
        == "Tablet and Cream for topical application"
    )
    assert (
        inst.combinedPharmaceuticalDoseForm.coding[0].system
        == "http://example.org.uk/fhir/doseform"
    )
    assert inst.contained[0].id == "packageCombo"
    assert inst.contained[1].id == "tabletItem"
    assert inst.contained[2].id == "creamItem"
    assert inst.id == "drug-combo-product"
    assert inst.identifier[0].system == "http://example.org.uk/fhir/product"
    assert inst.identifier[0].value == "ThrushTreatCombo"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].productName == "ThrushTreat Combo"
    assert inst.text.status == "generated"


def test_medicinalproductdefinition_6(base_settings):
    """No. 6 tests collection for MedicinalProductDefinition.
    Test File: medicinalproductdefinition-example-combo-product.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "medicinalproductdefinition-example-combo-product.json"
    )
    inst = medicinalproductdefinition.MedicinalProductDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductDefinition" == inst.resource_type

    impl_medicinalproductdefinition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductDefinition" == data["resourceType"]

    inst2 = medicinalproductdefinition.MedicinalProductDefinition(**data)
    impl_medicinalproductdefinition_6(inst2)


def impl_medicinalproductdefinition_7(inst):
    assert inst.contained[0].id == "Acetamin-pack-20"
    assert inst.contained[1].id == "Acetamin-tab-500"
    assert inst.id == "Acetamin-500-20-generic"
    assert inst.identifier[0].system == "http://example.nation.org/drugs"
    assert inst.identifier[0].value == "12345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].productName == "Acetaminophen 500 mg tablets [generic]"
    assert inst.text.status == "generated"


def test_medicinalproductdefinition_7(base_settings):
    """No. 7 tests collection for MedicinalProductDefinition.
    Test File: medicinalproductdefinition-acetaminophen-500mg-tablets-box-of-20.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "medicinalproductdefinition-acetaminophen-500mg-tablets-box-of-20.json"
    )
    inst = medicinalproductdefinition.MedicinalProductDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductDefinition" == inst.resource_type

    impl_medicinalproductdefinition_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductDefinition" == data["resourceType"]

    inst2 = medicinalproductdefinition.MedicinalProductDefinition(**data)
    impl_medicinalproductdefinition_7(inst2)


def impl_medicinalproductdefinition_8(inst):
    assert inst.attachedDocument[0].reference == "DocumentReference/example"
    assert inst.classification[0].coding[0].code == "B01AF02"
    assert inst.classification[0].coding[0].system == (
        "http://ema.europa.eu/example/WHOAnatomicalTherapeuticChemica"
        "lATCClassificationSystem"
    )
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://ema.europa.eu/example/MPID"
    assert inst.identifier[0].value == "{mpid}"
    assert inst.masterFile[0].reference == "DocumentReference/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.name[0].countryLanguage[0].country.coding[0].code == "EU"
    assert (
        inst.name[0].countryLanguage[0].country.coding[0].system
        == "http://ema.europa.eu/example/countryCode"
    )
    assert inst.name[0].countryLanguage[0].jurisdiction.coding[0].code == "EU"
    assert (
        inst.name[0].countryLanguage[0].jurisdiction.coding[0].system
        == "http://ema.europa.eu/example/jurisdictionCode"
    )
    assert inst.name[0].countryLanguage[0].language.coding[0].code == "EN"
    assert (
        inst.name[0].countryLanguage[0].language.coding[0].system
        == "http://ema.europa.eu/example/languageCode"
    )
    assert inst.name[0].namePart[0].part == "Equilidem"
    assert inst.name[0].namePart[0].type.coding[0].code == "INV"
    assert inst.name[0].namePart[1].part == "2.5 mg"
    assert inst.name[0].namePart[1].type.coding[0].code == "STR"
    assert inst.name[0].namePart[2].part == "film-coated tablets"
    assert inst.name[0].namePart[2].type.coding[0].code == "FRM"
    assert inst.name[0].productName == "Equilidem 2.5 mg film-coated tablets"
    assert inst.operation[0].effectiveDate.start == fhirtypes.DateTime.validate(
        "2013-03-15"
    )
    assert inst.operation[0].type.concept.coding[0].code == "Batchrelease"
    assert (
        inst.operation[0].type.concept.coding[0].system
        == "http://ema.europa.eu/example/manufacturingOperationType"
    )
    assert inst.text.status == "generated"


def test_medicinalproductdefinition_8(base_settings):
    """No. 8 tests collection for MedicinalProductDefinition.
    Test File: medicinalproductdefinition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicinalproductdefinition-example.json"
    )
    inst = medicinalproductdefinition.MedicinalProductDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductDefinition" == inst.resource_type

    impl_medicinalproductdefinition_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductDefinition" == data["resourceType"]

    inst2 = medicinalproductdefinition.MedicinalProductDefinition(**data)
    impl_medicinalproductdefinition_8(inst2)
