# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/AdministrableProductDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import administrableproductdefinition
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_administrableproductdefinition_1(inst):
    assert inst.administrableDoseForm.coding[0].code == "Film-coatedtablet"
    assert (
        inst.administrableDoseForm.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ema.europa.eu/example/administrabledoseform"}
        ).valueUri
    )
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ema.europa.eu/example/phpididentifiersets"}
        ).valueUri
    )
    assert inst.identifier[0].value == "{PhPID}"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.routeOfAdministration[0].code.coding[0].code == "OralUse"
    assert (
        inst.routeOfAdministration[0].code.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ema.europa.eu/example/routeofadministration"}
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.unitOfPresentation.coding[0].code == "Tablet"
    assert (
        inst.unitOfPresentation.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ema.europa.eu/example/unitofpresentation"}
        ).valueUri
    )


def test_administrableproductdefinition_1(base_settings):
    """No. 1 tests collection for AdministrableProductDefinition.
    Test File: administrableproductdefinition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "administrableproductdefinition-example.json"
    )
    inst = administrableproductdefinition.AdministrableProductDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "AdministrableProductDefinition" == inst.get_resource_type()

    impl_administrableproductdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "AdministrableProductDefinition" == data["resourceType"]

    inst2 = administrableproductdefinition.AdministrableProductDefinition(**data)
    impl_administrableproductdefinition_1(inst2)
