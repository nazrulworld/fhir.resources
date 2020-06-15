# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Parameters
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import parameters


def impl_parameters_1(inst):
    assert inst.id == "example"
    assert inst.parameter[0].name == "start"
    assert inst.parameter[0].valueDate == fhirtypes.Date.validate("2010-01-01")
    assert inst.parameter[1].name == "end"


def test_parameters_1(base_settings):
    """No. 1 tests collection for Parameters.
    Test File: parameters-example.json
    """
    filename = base_settings["unittest_data_dir"] / "parameters-example.json"
    inst = parameters.Parameters.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Parameters" == inst.resource_type

    impl_parameters_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Parameters" == data["resourceType"]

    inst2 = parameters.Parameters(**data)
    impl_parameters_1(inst2)
