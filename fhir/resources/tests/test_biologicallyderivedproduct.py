# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import biologicallyderivedproduct
from .fixtures import ExternalValidatorModel


def impl_biologicallyderivedproduct_1(inst):
    assert (
        inst.biologicalSourceEvent.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.isbt128.org/uri/DonationIdentificationNumber"}
        ).valueUri
    )
    assert inst.biologicalSourceEvent.value == "A999921123456"
    assert inst.division == "A00000"
    assert (
        inst.expirationDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2021-08-02T23:59:00-05:00"}
        ).valueDateTime
    )
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.isbt128.org/uri/MPHOUniqueIdentifier"}
        ).valueUri
    )
    assert inst.identifier[0].value == "A9999E0398A999921123456A00000"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.processingFacility[0].reference == "Organization/A9999"
    assert inst.productCode.coding[0].code == "E0398"
    assert inst.productStatus.code == "available"
    assert inst.property[0].type.coding[0].code == "ABORhD"
    assert inst.property[0].valueCodeableConcept.coding[0].code == "62"
    assert inst.property[0].valueCodeableConcept.coding[0].display == "A RhD Positive"
    assert (
        inst.property[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.isbt128.org/uri/ABORhD"}
        ).valueUri
    )
    assert inst.property[1].type.coding[0].code == "Donor"
    assert inst.property[1].valueCodeableConcept.coding[0].code == "V"
    assert inst.property[1].valueCodeableConcept.coding[0].display == "Volunteer"
    assert (
        inst.property[1].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.isbt128.org/uri/CollectionType"}
        ).valueUri
    )
    assert (
        inst.storageTempRequirements.high.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.storageTempRequirements.high.unit == "degrees C"
    assert float(inst.storageTempRequirements.high.value) == float(6)
    assert (
        inst.storageTempRequirements.low.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.storageTempRequirements.low.unit == "degrees C"
    assert float(inst.storageTempRequirements.low.value) == float(1)
    assert inst.text.status == "generated"


def test_biologicallyderivedproduct_1(base_settings):
    """No. 1 tests collection for BiologicallyDerivedProduct.
    Test File: biologicallyderivedproduct-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "biologicallyderivedproduct-example.json"
    )
    inst = biologicallyderivedproduct.BiologicallyDerivedProduct.model_validate_json(
        filename.read_bytes()
    )
    assert "BiologicallyDerivedProduct" == inst.get_resource_type()

    impl_biologicallyderivedproduct_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "BiologicallyDerivedProduct" == data["resourceType"]

    inst2 = biologicallyderivedproduct.BiologicallyDerivedProduct(**data)
    impl_biologicallyderivedproduct_1(inst2)


def impl_biologicallyderivedproduct_2(inst):
    assert inst.collection.source.display == "HCT Donor"
    assert inst.collection.source.reference == "Patient/example-b"
    assert inst.id == "allogeneicHCT"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.request[0].display == "Service Request for HCT Collection"
    assert (
        inst.request[0].reference
        == "BiologicallyDerivedProduct/HCTcollection-servicerequest"
    )
    assert inst.text.status == "generated"


def test_biologicallyderivedproduct_2(base_settings):
    """No. 2 tests collection for BiologicallyDerivedProduct.
    Test File: biologicallyderivedproduct-example-allogeneicHCT.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "biologicallyderivedproduct-example-allogeneicHCT.json"
    )
    inst = biologicallyderivedproduct.BiologicallyDerivedProduct.model_validate_json(
        filename.read_bytes()
    )
    assert "BiologicallyDerivedProduct" == inst.get_resource_type()

    impl_biologicallyderivedproduct_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "BiologicallyDerivedProduct" == data["resourceType"]

    inst2 = biologicallyderivedproduct.BiologicallyDerivedProduct(**data)
    impl_biologicallyderivedproduct_2(inst2)


def impl_biologicallyderivedproduct_3(inst):
    assert (
        inst.biologicalSourceEvent.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.isbt128.org/uri/DonationIdentificationNumber"}
        ).valueUri
    )
    assert inst.biologicalSourceEvent.value == "W000022000687"
    assert inst.collection.source.display == "HCT Collection"
    assert inst.collection.source.reference == "Patient/example-a"
    assert inst.division == "A00000"
    assert (
        inst.expirationDate
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2028-08-02T23:59:00-05:00"}
        ).valueDateTime
    )
    assert inst.id == "autologousHCT"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.isbt128.org/uri/SingleEuropeanCode"}
        ).valueUri
    )
    assert inst.identifier[0].value == "PL001499Z549917123456 A00T041600320171231"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.processingFacility[0].reference == "Organization/Example"
    assert inst.productCategory.code == "cells"
    assert inst.productCode.coding[0].code == "S1128"
    assert inst.productStatus.code == "available"
    assert inst.property[0].type.coding[0].code == "ABORhD"
    assert inst.property[0].valueCodeableConcept.coding[0].code == "62"
    assert inst.property[0].valueCodeableConcept.coding[0].display == "A RhD Positive"
    assert (
        inst.property[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.isbt128.org/uri/ABORhD"}
        ).valueUri
    )
    assert inst.property[1].type.coding[0].code == "CollectionType"
    assert inst.property[1].valueCodeableConcept.coding[0].code == "1"
    assert (
        inst.property[1].valueCodeableConcept.coding[0].display
        == "For Autologous Use Only"
    )
    assert (
        inst.property[1].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://www.isbt128.org/uri/CollectionType"}
        ).valueUri
    )
    assert inst.property[2].type.coding[0].code == "BagVolume"
    assert (
        inst.property[2].valueQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.property[2].valueQuantity.unit == "mL"
    assert float(inst.property[2].valueQuantity.value) == float(50)
    assert inst.property[3].type.coding[0].code == "74838-4"
    assert (
        inst.property[3].valueQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "https://ucum.org/"}
        ).valueUri
    )
    assert inst.property[3].valueQuantity.unit == "10*6/mL"
    assert float(inst.property[3].valueQuantity.value) == float(2.6)
    assert inst.request[0].display == "Service Request for HCT Collection"
    assert (
        inst.request[0].reference
        == "BiologicallyDerivedProduct/HCTcollection-servicerequest"
    )
    assert (
        inst.storageTempRequirements.high.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.storageTempRequirements.high.unit == "degrees C"
    assert float(inst.storageTempRequirements.high.value) == float(-120)
    assert inst.text.status == "generated"


def test_biologicallyderivedproduct_3(base_settings):
    """No. 3 tests collection for BiologicallyDerivedProduct.
    Test File: biologicallyderivedproduct-example-autologousHCT.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "biologicallyderivedproduct-example-autologousHCT.json"
    )
    inst = biologicallyderivedproduct.BiologicallyDerivedProduct.model_validate_json(
        filename.read_bytes()
    )
    assert "BiologicallyDerivedProduct" == inst.get_resource_type()

    impl_biologicallyderivedproduct_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "BiologicallyDerivedProduct" == data["resourceType"]

    inst2 = biologicallyderivedproduct.BiologicallyDerivedProduct(**data)
    impl_biologicallyderivedproduct_3(inst2)
