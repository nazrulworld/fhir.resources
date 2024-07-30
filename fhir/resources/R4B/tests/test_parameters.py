# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Parameters
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import parameters
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_parameters_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.parameter[0].name == "exact"
    assert inst.parameter[0].valueBoolean is True
    assert inst.parameter[1].name == "property"
    assert inst.parameter[1].part[0].name == "code"
    assert inst.parameter[1].part[0].valueCode == "focus"
    assert inst.parameter[1].part[1].name == "value"
    assert inst.parameter[1].part[1].valueCode == "top"
    assert inst.parameter[2].name == "patient"
    assert inst.parameter[2].resource.id == "example"


def test_parameters_1(base_settings):
    """No. 1 tests collection for Parameters.
    Test File: parameters-example.json
    """
    filename = base_settings["unittest_data_dir"] / "parameters-example.json"
    inst = parameters.Parameters.model_validate_json(filename.read_bytes())
    assert "Parameters" == inst.get_resource_type()

    impl_parameters_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Parameters" == data["resourceType"]

    inst2 = parameters.Parameters(**data)
    impl_parameters_1(inst2)
