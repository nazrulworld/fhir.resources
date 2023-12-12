# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import chargeitemdefinition


def impl_chargeitemdefinition_1(inst):
    assert (
        inst.applicability[0].description
        == "Verify ChargeItem pertains to Device 12345"
    )
    assert (
        inst.applicability[0].expression
        == "%context.service.suppliedItem='Device/12345'"
    )
    assert inst.applicability[0].language == "text/fhirpath"
    assert inst.description == "Financial details for  custom made device"
    assert inst.experimental is True
    assert inst.id == "device"
    assert inst.instance[0].reference == "Device/12345"
    assert inst.propertyGroup[0].priceComponent[0].amount.currency == "EUR"
    assert float(inst.propertyGroup[0].priceComponent[0].amount.value) == float(67.44)
    assert inst.propertyGroup[0].priceComponent[0].code.coding[0].code == "VK"
    assert (
        inst.propertyGroup[0].priceComponent[0].code.coding[0].display
        == "Verkaufspreis (netto)"
    )
    assert (
        inst.propertyGroup[0].priceComponent[0].code.coding[0].system
        == "http://fhir.de/CodeSystem/billing-attributes"
    )
    assert inst.propertyGroup[0].priceComponent[0].type == "base"
    assert inst.propertyGroup[1].applicability[0].description == "Gültigkeit Steuersatz"
    assert (
        inst.propertyGroup[1].applicability[0].expression
        == "%context.occurenceDateTime > '2018-04-01'"
    )
    assert inst.propertyGroup[1].applicability[0].language == "text/fhirpath"
    assert inst.propertyGroup[1].priceComponent[0].code.coding[0].code == "MWST"
    assert (
        inst.propertyGroup[1].priceComponent[0].code.coding[0].display
        == "Mehrwersteuersatz"
    )
    assert (
        inst.propertyGroup[1].priceComponent[0].code.coding[0].system
        == "http://fhir.de/CodeSystem/billing-attributes"
    )
    assert float(inst.propertyGroup[1].priceComponent[0].factor) == float(1.19)
    assert inst.propertyGroup[1].priceComponent[0].type == "tax"
    assert inst.propertyGroup[2].applicability[0].description == "Gültigkeit Steuersatz"
    assert (
        inst.propertyGroup[2].applicability[0].expression
        == "%context.occurenceDateTime <= '2018-04-01'"
    )
    assert inst.propertyGroup[2].applicability[0].language == "text/fhirpath"
    assert inst.propertyGroup[2].priceComponent[0].code.coding[0].code == "MWST"
    assert (
        inst.propertyGroup[2].priceComponent[0].code.coding[0].display
        == "Mehrwersteuersatz"
    )
    assert (
        inst.propertyGroup[2].priceComponent[0].code.coding[0].system
        == "http://fhir.de/CodeSystem/billing-attributes"
    )
    assert float(inst.propertyGroup[2].priceComponent[0].factor) == float(1.07)
    assert inst.propertyGroup[2].priceComponent[0].type == "tax"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.url == "http://sap.org/ChargeItemDefinition/device-123"


def test_chargeitemdefinition_1(base_settings):
    """No. 1 tests collection for ChargeItemDefinition.
    Test File: chargeitemdefinition-device-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "chargeitemdefinition-device-example.json"
    )
    inst = chargeitemdefinition.ChargeItemDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ChargeItemDefinition" == inst.resource_type

    impl_chargeitemdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ChargeItemDefinition" == data["resourceType"]

    inst2 = chargeitemdefinition.ChargeItemDefinition(**data)
    impl_chargeitemdefinition_1(inst2)


def impl_chargeitemdefinition_2(inst):
    assert (
        inst.applicability[0].description
        == "Excludes billing code 13250 for same Encounter"
    )
    assert inst.applicability[0].expression == "[some CQL expression]"
    assert inst.applicability[0].language == "text/cql"
    assert inst.applicability[1].description == "Applies only once per Encounter"
    assert inst.applicability[1].expression == "[some CQL expression]"
    assert inst.applicability[1].language == "text/CQL"
    assert inst.code.coding[0].code == "30110"
    assert inst.code.coding[0].display == "Allergologiediagnostik I"
    assert inst.code.coding[0].system == "http://fhir.de/CodingSystem/kbv/ebm"
    assert inst.description == (
        "Allergologisch-diagnostischer Komplex zur Diagnostik "
        "und/oder zum Ausschluss einer (Kontakt-)Allergie vom Spättyp"
        " (Typ IV), einschl. Kosten"
    )
    assert inst.effectivePeriod.end == fhirtypes.DateTime.validate("2018-06-30")
    assert inst.effectivePeriod.start == fhirtypes.DateTime.validate("2018-04-01")
    assert inst.experimental is True
    assert inst.id == "ebm"
    assert inst.propertyGroup[0].priceComponent[0].amount.currency == "EUR"
    assert float(inst.propertyGroup[0].priceComponent[0].amount.value) == float(67.44)
    assert inst.propertyGroup[0].priceComponent[0].code.coding[0].code == "gesamt-euro"
    assert (
        inst.propertyGroup[0].priceComponent[0].code.coding[0].display
        == "Gesamt (Euro)"
    )
    assert (
        inst.propertyGroup[0].priceComponent[0].code.coding[0].system
        == "http://fhir.de/CodeSystem/kbv/ebm-attribute"
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
        == "http://fhir.de/CodeSystem/kbv/ebm-attribute"
    )
    assert float(inst.propertyGroup[0].priceComponent[1].factor) == float(633)
    assert inst.propertyGroup[0].priceComponent[1].type == "informational"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.url == "http://fhir.de/ChargeItemDefinition/kbv/ebm-30110"
    assert inst.version == "2-2018"


def test_chargeitemdefinition_2(base_settings):
    """No. 2 tests collection for ChargeItemDefinition.
    Test File: chargeitemdefinition-ebm-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "chargeitemdefinition-ebm-example.json"
    )
    inst = chargeitemdefinition.ChargeItemDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ChargeItemDefinition" == inst.resource_type

    impl_chargeitemdefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ChargeItemDefinition" == data["resourceType"]

    inst2 = chargeitemdefinition.ChargeItemDefinition(**data)
    impl_chargeitemdefinition_2(inst2)
