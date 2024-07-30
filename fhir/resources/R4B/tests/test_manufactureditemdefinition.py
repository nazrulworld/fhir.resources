# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ManufacturedItemDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import manufactureditemdefinition
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_manufactureditemdefinition_1(inst):
    assert inst.id == "example"
    assert inst.manufacturedDoseForm.coding[0].code == "Film-coatedtablet"
    assert (
        inst.manufacturedDoseForm.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ema.europa.eu/example/manufactureddoseform"}
        ).valueUri
    )
    assert inst.manufacturer[0].reference == "Organization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.property[0].type.coding[0].code == "shape"
    assert inst.property[0].valueCodeableConcept.text == "Oval"
    assert inst.property[1].type.coding[0].code == "color"
    assert inst.property[1].valueCodeableConcept.text == "pink"
    assert inst.property[2].type.coding[0].code == "imprint"
    assert inst.property[2].valueCodeableConcept.text == "894"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.unitOfPresentation.coding[0].code == "Tablet"
    assert (
        inst.unitOfPresentation.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ema.europa.eu/example/unitofpresentation"}
        ).valueUri
    )


def test_manufactureditemdefinition_1(base_settings):
    """No. 1 tests collection for ManufacturedItemDefinition.
    Test File: manufactureditemdefinition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "manufactureditemdefinition-example.json"
    )
    inst = manufactureditemdefinition.ManufacturedItemDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "ManufacturedItemDefinition" == inst.get_resource_type()

    impl_manufactureditemdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ManufacturedItemDefinition" == data["resourceType"]

    inst2 = manufactureditemdefinition.ManufacturedItemDefinition(**data)
    impl_manufactureditemdefinition_1(inst2)
