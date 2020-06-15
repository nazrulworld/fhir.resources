# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProduct
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicinalproduct


def impl_medicinalproduct_1(inst):
    assert inst.attachedDocument[0].reference == "DocumentReference/example"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://ema.europa.eu/example/MPID"
    assert inst.identifier[0].value == "{mpid}"
    assert inst.manufacturingBusinessOperation[
        0
    ].authorisationReferenceNumber.system == (
        "http://ema.europa.eu/example/manufacturingAuthorisationRefer" "enceNumber"
    )
    assert (
        inst.manufacturingBusinessOperation[0].authorisationReferenceNumber.value
        == "1324TZ"
    )
    assert inst.manufacturingBusinessOperation[
        0
    ].effectiveDate == fhirtypes.DateTime.validate("2013-03-15T11:15:33+10:00")
    assert (
        inst.manufacturingBusinessOperation[0].manufacturer[0].reference
        == "Organization/example"
    )
    assert (
        inst.manufacturingBusinessOperation[0].operationType.coding[0].code
        == "Batchrelease"
    )
    assert (
        inst.manufacturingBusinessOperation[0].operationType.coding[0].system
        == "http://ema.europa.eu/example/manufacturingOperationType"
    )
    assert (
        inst.manufacturingBusinessOperation[0].regulator.reference
        == "Organization/example"
    )
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
    assert inst.name[0].namePart[0].type.code == "INV"
    assert inst.name[0].namePart[1].part == "2.5 mg"
    assert inst.name[0].namePart[1].type.code == "STR"
    assert inst.name[0].namePart[2].part == "film-coated tablets"
    assert inst.name[0].namePart[2].type.code == "FRM"
    assert inst.name[0].productName == "Equilidem 2.5 mg film-coated tablets"
    assert inst.productClassification[0].coding[0].code == (
        "WHOAnatomicalTherapeuticChemicalATCClassificationSystem|B01A" "F02"
    )
    assert inst.productClassification[0].coding[0].system == (
        "http://ema.europa.eu/example/WHOAnatomicalTherapeuticChemica"
        "lATCClassificationSystem"
    )
    assert inst.text.status == "generated"


def test_medicinalproduct_1(base_settings):
    """No. 1 tests collection for MedicinalProduct.
    Test File: medicinalproduct-example.json
    """
    filename = base_settings["unittest_data_dir"] / "medicinalproduct-example.json"
    inst = medicinalproduct.MedicinalProduct.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProduct" == inst.resource_type

    impl_medicinalproduct_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProduct" == data["resourceType"]

    inst2 = medicinalproduct.MedicinalProduct(**data)
    impl_medicinalproduct_1(inst2)
