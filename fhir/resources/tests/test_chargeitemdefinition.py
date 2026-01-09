# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import chargeitemdefinition
from .conftest import ExternalValidatorModel


def impl_chargeitemdefinition_1(inst):
    assert (
        inst.applicability[0].condition.description
        == "Verify ChargeItem pertains to Device 12345"
    )
    assert (
        inst.applicability[0].condition.expression
        == "%context.service.suppliedItem.reference='Device/12345'"
    )
    assert inst.applicability[0].condition.language == "text/fhirpath"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-02"}
        ).valueDateTime
    )
    assert inst.description == "Financial details for custom made device"
    assert inst.id == "device"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.29.2"
    assert inst.instance[0].reference == "Device/example"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unstats.un.org/unsd/methods/m49/m49.htm"}
        ).valueUri
    )
    assert inst.name == "CustomDevice345675"
    assert inst.propertyGroup[0].priceComponent[0].amount.currency == "EUR"
    assert float(inst.propertyGroup[0].priceComponent[0].amount.value) == float(67.44)
    assert inst.propertyGroup[0].priceComponent[0].code.coding[0].code == "VK"
    assert (
        inst.propertyGroup[0].priceComponent[0].code.coding[0].display
        == "Verkaufspreis (netto)"
    )
    assert (
        inst.propertyGroup[0].priceComponent[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://fhir.de/CodeSystem/billing-attributes"}
        ).valueUri
    )
    assert inst.propertyGroup[0].priceComponent[0].type == "base"
    assert (
        inst.propertyGroup[1].applicability[0].condition.description
        == "Gültigkeit Steuersatz"
    )
    assert (
        inst.propertyGroup[1].applicability[0].condition.expression
        == "%context.occurenceDateTime > '2018-04-01'"
    )
    assert inst.propertyGroup[1].applicability[0].condition.language == "text/fhirpath"
    assert inst.propertyGroup[1].priceComponent[0].code.coding[0].code == "MWST"
    assert (
        inst.propertyGroup[1].priceComponent[0].code.coding[0].display
        == "Mehrwersteuersatz"
    )
    assert (
        inst.propertyGroup[1].priceComponent[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://fhir.de/CodeSystem/billing-attributes"}
        ).valueUri
    )
    assert float(inst.propertyGroup[1].priceComponent[0].factor) == float(1.19)
    assert inst.propertyGroup[1].priceComponent[0].type == "tax"
    assert (
        inst.propertyGroup[2].applicability[0].condition.description
        == "Gültigkeit Steuersatz"
    )
    assert (
        inst.propertyGroup[2].applicability[0].condition.expression
        == "%context.occurenceDateTime <= '2018-04-01'"
    )
    assert inst.propertyGroup[2].applicability[0].condition.language == "text/fhirpath"
    assert inst.propertyGroup[2].priceComponent[0].code.coding[0].code == "MWST"
    assert (
        inst.propertyGroup[2].priceComponent[0].code.coding[0].display
        == "Mehrwersteuersatz"
    )
    assert (
        inst.propertyGroup[2].priceComponent[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://fhir.de/CodeSystem/billing-attributes"}
        ).valueUri
    )
    assert float(inst.propertyGroup[2].priceComponent[0].factor) == float(1.07)
    assert inst.propertyGroup[2].priceComponent[0].type == "tax"
    assert inst.publisher == "Example Publisher"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Financial details for custom made device (345675)"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://sap.org/ChargeItemDefinition/device-123"}
        ).valueUri
    )
    assert inst.useContext[0].code.code == "venue"
    assert (
        inst.useContext[0].code.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/usage-context-type"}
        ).valueUri
    )
    assert inst.useContext[0].valueCodeableConcept.coding[0].code == "440655000"
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].display
        == "Outpatient environment"
    )
    assert (
        inst.useContext[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://snomed.info/sct"}
        ).valueUri
    )
    assert inst.useContext[1].code.code == "age"
    assert (
        inst.useContext[1].code.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/usage-context-type"}
        ).valueUri
    )
    assert inst.useContext[1].valueQuantity.code == "a"
    assert inst.useContext[1].valueQuantity.comparator == ">"
    assert (
        inst.useContext[1].valueQuantity.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unitsofmeasure.org"}
        ).valueUri
    )
    assert inst.useContext[1].valueQuantity.unit == "yrs"
    assert float(inst.useContext[1].valueQuantity.value) == float(18)


def test_chargeitemdefinition_1(base_settings):
    """No. 1 tests collection for ChargeItemDefinition.
    Test File: chargeitemdefinition-device-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "chargeitemdefinition-device-example.json"
    )
    inst = chargeitemdefinition.ChargeItemDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "ChargeItemDefinition" == inst.get_resource_type()

    impl_chargeitemdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ChargeItemDefinition" == data["resourceType"]

    inst2 = chargeitemdefinition.ChargeItemDefinition(**data)
    impl_chargeitemdefinition_1(inst2)


def impl_chargeitemdefinition_2(inst):
    assert (
        inst.applicability[0].condition.description
        == "Excludes billing code 13250 for same Encounter"
    )
    assert inst.applicability[0].condition.expression == "[some CQL expression]"
    assert inst.applicability[0].condition.language == "text/cql"
    assert (
        inst.applicability[0].effectivePeriod.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2018-06-30"}
        ).valueDateTime
    )
    assert (
        inst.applicability[0].effectivePeriod.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2018-04-01"}
        ).valueDateTime
    )
    assert (
        inst.applicability[1].condition.description == "Applies only once per Encounter"
    )
    assert inst.applicability[1].condition.expression == "[some CQL expression]"
    assert inst.applicability[1].condition.language == "text/CQL"
    assert (
        inst.applicability[1].effectivePeriod.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2018-06-30"}
        ).valueDateTime
    )
    assert (
        inst.applicability[1].effectivePeriod.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2018-04-01"}
        ).valueDateTime
    )
    assert inst.code.coding[0].code == "30110"
    assert inst.code.coding[0].display == "Allergologiediagnostik I"
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://fhir.de/CodingSystem/kbv/ebm"}
        ).valueUri
    )
    assert inst.description == (
        "Allergologisch-diagnostischer Komplex zur Diagnostik "
        "und/oder zum Ausschluss einer (Kontakt-)Allergie vom Spättyp"
        " (Typ IV), einschl. Kosten"
    )
    assert inst.id == "ebm"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.29.1"
    assert inst.propertyGroup[0].priceComponent[0].amount.currency == "EUR"
    assert float(inst.propertyGroup[0].priceComponent[0].amount.value) == float(67.44)
    assert inst.propertyGroup[0].priceComponent[0].code.coding[0].code == "gesamt-euro"
    assert (
        inst.propertyGroup[0].priceComponent[0].code.coding[0].display
        == "Gesamt (Euro)"
    )
    assert (
        inst.propertyGroup[0].priceComponent[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://fhir.de/CodeSystem/kbv/ebm-attribute"}
        ).valueUri
    )
    assert inst.propertyGroup[0].priceComponent[0].type == "base"
    assert (
        inst.propertyGroup[0].priceComponent[1].code.coding[0].code == "gesamt-punkte"
    )
    assert (
        inst.propertyGroup[0].priceComponent[1].code.coding[0].display
        == "Gesamt (Punkte)"
    )
    assert (
        inst.propertyGroup[0].priceComponent[1].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://fhir.de/CodeSystem/kbv/ebm-attribute"}
        ).valueUri
    )
    assert float(inst.propertyGroup[0].priceComponent[1].factor) == float(633)
    assert inst.propertyGroup[0].priceComponent[1].type == "informational"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://fhir.de/ChargeItemDefinition/kbv/ebm-30110"}
        ).valueUri
    )
    assert inst.version == "2-2018"


def test_chargeitemdefinition_2(base_settings):
    """No. 2 tests collection for ChargeItemDefinition.
    Test File: chargeitemdefinition-ebm-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "chargeitemdefinition-ebm-example.json"
    )
    inst = chargeitemdefinition.ChargeItemDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "ChargeItemDefinition" == inst.get_resource_type()

    impl_chargeitemdefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ChargeItemDefinition" == data["resourceType"]

    inst2 = chargeitemdefinition.ChargeItemDefinition(**data)
    impl_chargeitemdefinition_2(inst2)
