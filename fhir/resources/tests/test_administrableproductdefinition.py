# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdministrableProductDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import administrableproductdefinition


def impl_administrableproductdefinition_1(inst):
    assert inst.administrableDoseForm.coding[0].code == "Film-coatedtablet"
    assert (
        inst.administrableDoseForm.coding[0].system
        == "http://ema.europa.eu/example/administrabledoseform"
    )
    assert inst.id == "example"
    assert (
        inst.identifier[0].system == "http://ema.europa.eu/example/phpididentifiersets"
    )
    assert inst.identifier[0].value == "{PhPID}"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.routeOfAdministration[0].code.coding[0].code == "OralUse"
    assert (
        inst.routeOfAdministration[0].code.coding[0].system
        == "http://ema.europa.eu/example/routeofadministration"
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.unitOfPresentation.coding[0].code == "Tablet"
    assert (
        inst.unitOfPresentation.coding[0].system
        == "http://ema.europa.eu/example/unitofpresentation"
    )


def test_administrableproductdefinition_1(base_settings):
    """No. 1 tests collection for AdministrableProductDefinition.
    Test File: administrableproductdefinition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "administrableproductdefinition-example.json"
    )
    inst = administrableproductdefinition.AdministrableProductDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "AdministrableProductDefinition" == inst.resource_type

    impl_administrableproductdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "AdministrableProductDefinition" == data["resourceType"]

    inst2 = administrableproductdefinition.AdministrableProductDefinition(**data)
    impl_administrableproductdefinition_1(inst2)
