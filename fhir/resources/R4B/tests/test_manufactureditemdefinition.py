# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ManufacturedItemDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import manufactureditemdefinition


def impl_manufactureditemdefinition_1(inst):
    assert inst.id == "example"
    assert inst.manufacturedDoseForm.coding[0].code == "Film-coatedtablet"
    assert (
        inst.manufacturedDoseForm.coding[0].system
        == "http://ema.europa.eu/example/manufactureddoseform"
    )
    assert inst.manufacturer[0].reference == "Organization/example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
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
        == "http://ema.europa.eu/example/unitofpresentation"
    )


def test_manufactureditemdefinition_1(base_settings):
    """No. 1 tests collection for ManufacturedItemDefinition.
    Test File: manufactureditemdefinition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "manufactureditemdefinition-example.json"
    )
    inst = manufactureditemdefinition.ManufacturedItemDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ManufacturedItemDefinition" == inst.resource_type

    impl_manufactureditemdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ManufacturedItemDefinition" == data["resourceType"]

    inst2 = manufactureditemdefinition.ManufacturedItemDefinition(**data)
    impl_manufactureditemdefinition_1(inst2)
