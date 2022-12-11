# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import medicinalproductinteraction


def impl_medicinalproductinteraction_1(inst):
    assert inst.effect.coding[0].code == "Increasedplasmaconcentrations"
    assert (
        inst.effect.coding[0].system
        == "http://ema.europa.eu/example/interactionseffect"
    )
    assert inst.id == "example"
    assert inst.interactant[0].itemCodeableConcept.coding[0].code == "ketoconazole"
    assert (
        inst.interactant[0].itemCodeableConcept.coding[0].system
        == "http://ema.europa.eu/example/interactant"
    )
    assert inst.interactant[1].itemCodeableConcept.coding[0].code == "itraconazole"
    assert (
        inst.interactant[1].itemCodeableConcept.coding[0].system
        == "http://ema.europa.eu/example/interactant"
    )
    assert inst.management.text == (
        "Coadministration not recommended in patients receiving "
        "concomitant systemic treatment strong inhibitors of both "
        "CYP3A4 and P-gp"
    )
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "StrongInhibitorofCYP3A4"
    assert inst.type.coding[0].system == "http://ema.europa.eu/example/interactionsType"


def test_medicinalproductinteraction_1(base_settings):
    """No. 1 tests collection for MedicinalProductInteraction.
    Test File: medicinalproductinteraction-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "medicinalproductinteraction-example.json"
    )
    inst = medicinalproductinteraction.MedicinalProductInteraction.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "MedicinalProductInteraction" == inst.resource_type

    impl_medicinalproductinteraction_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MedicinalProductInteraction" == data["resourceType"]

    inst2 = medicinalproductinteraction.MedicinalProductInteraction(**data)
    impl_medicinalproductinteraction_1(inst2)
