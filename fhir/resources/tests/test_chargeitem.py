# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItem
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import chargeitem


def impl_chargeitem_1(inst):
    assert inst.account[0].reference == "Account/example"
    assert inst.code.coding[0].code == "01510"
    assert inst.code.coding[0].display == (
        "Zusatzpauschale für Beobachtung nach diagnostischer " "Koronarangiografie"
    )
    assert inst.context.reference == "Encounter/example"
    assert inst.definitionUri[0] == (
        "http://www.kbv.de/tools/ebm/html/01520_290436086082622081363" "2.html"
    )
    assert inst.enteredDate == fhirtypes.DateTime.validate("2017-01-25T23:55:04+01:00")
    assert inst.enterer.reference == "Practitioner/example"
    assert float(inst.factorOverride) == float(0.8)
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://myHospital.org/ChargeItems"
    assert inst.identifier[0].value == "654321"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.note[0].authorReference.reference == "Practitioner/example"
    assert inst.note[0].text == "The code is only applicable for periods longer than 4h"
    assert inst.note[0].time == fhirtypes.DateTime.validate("2017-01-25T23:55:04+01:00")
    assert inst.occurrencePeriod.end == fhirtypes.DateTime.validate(
        "2017-01-25T12:35:00+01:00"
    )
    assert inst.occurrencePeriod.start == fhirtypes.DateTime.validate(
        "2017-01-25T08:00:00+01:00"
    )
    assert inst.overrideReason == (
        "Patient is Cardiologist's golf buddy, so he gets a 20% " "discount!"
    )
    assert inst.performer[0].actor.reference == "Practitioner/example"
    assert inst.performer[0].function.coding[0].code == "17561000"
    assert inst.performer[0].function.coding[0].display == "Cardiologist"
    assert inst.performer[0].function.coding[0].system == "http://snomed.info/sct"
    assert inst.performer[1].actor.reference == "Practitioner/example"
    assert inst.performer[1].function.coding[0].code == "224542009"
    assert inst.performer[1].function.coding[0].display == "Coronary Care Nurse"
    assert inst.performer[1].function.coding[0].system == "http://snomed.info/sct"
    assert (
        inst.performingOrganization.identifier.system
        == "http://myhospital/NamingSystem/departments"
    )
    assert inst.performingOrganization.identifier.value == "CARD_INTERMEDIATE_CARE"
    assert inst.priceOverride.currency == "EUR"
    assert float(inst.priceOverride.value) == float(40)
    assert float(inst.quantity.value) == float(1)
    assert inst.reason[0].coding[0].code == "I51.6"
    assert inst.reason[0].coding[0].display == "Cardiovascular disease, unspecified"
    assert inst.reason[0].coding[0].system == "http://hl7.org/fhir/sid/icd-10"
    assert (
        inst.requestingOrganization.identifier.system
        == "http://myhospital/NamingSystem/departments"
    )
    assert inst.requestingOrganization.identifier.value == "CARD_U1"
    assert inst.service[0].reference == "Procedure/example"
    assert inst.status == "billable"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">Example of '
        "ChargeItem Usage in Context of the German EBM Billing code "
        "system</div>"
    )
    assert inst.text.status == "generated"


def test_chargeitem_1(base_settings):
    """No. 1 tests collection for ChargeItem.
    Test File: chargeitem-example.json
    """
    filename = base_settings["unittest_data_dir"] / "chargeitem-example.json"
    inst = chargeitem.ChargeItem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ChargeItem" == inst.resource_type

    impl_chargeitem_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ChargeItem" == data["resourceType"]

    inst2 = chargeitem.ChargeItem(**data)
    impl_chargeitem_1(inst2)
