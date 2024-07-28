# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/FormularyItem
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import formularyitem
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_formularyitem_1(inst):
    assert inst.code.coding[0].code == "323418000"
    assert (
        inst.code.coding[0].display
        == "Phenoxymethylpenicillin 125mg/5mL oral solution (product)"
    )
    assert (
        inst.code.coding[0].system
        == ExternalValidatorModel(valueUri="http://snomed.info/sct").valueUri
    )
    assert inst.code.coding[1].code == "22571011000036102"
    assert inst.code.coding[1].display == (
        "phenoxymethylpenicillin 125 mg / 5 mL oral liquid, 5 mL " "measure"
    )
    assert (
        inst.code.coding[1].system
        == ExternalValidatorModel(valueUri="http://nehta.gov.au/amt/v2").valueUri
    )
    assert inst.id == "formularyitemexample01"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.text.status == "generated"


def test_formularyitem_1(base_settings):
    """No. 1 tests collection for FormularyItem.
    Test File: formularyitemexample01.json
    """
    filename = base_settings["unittest_data_dir"] / "formularyitemexample01.json"
    inst = formularyitem.FormularyItem.model_validate_json(filename.read_bytes())
    assert "FormularyItem" == inst.get_resource_type()

    impl_formularyitem_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "FormularyItem" == data["resourceType"]

    inst2 = formularyitem.FormularyItem(**data)
    impl_formularyitem_1(inst2)
