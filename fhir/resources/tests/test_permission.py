# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Permission
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import permission
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_permission_1(inst):
    assert inst.combining == "deny-overrides"
    assert (
        inst.date[0] == ExternalValidatorModel(valueDateTime="2022-08-04").valueDateTime
    )
    assert inst.id == "example-vhdir"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.rule[0].activity[0].action[0].coding[0].code == "access"
    assert (
        inst.rule[0].activity[0].action[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/consentaction"
        ).valueUri
    )
    assert inst.rule[0].activity[0].actor[0].reference == "CareTeam/example"
    assert inst.rule[0].activity[0].purpose[0].coding[0].code == "HOPERAT"
    assert (
        inst.rule[0].activity[0].purpose[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.rule[0].data[0].security[0].code == "WSHELTER"
    assert (
        inst.rule[0].data[0].security[0].system
        == ExternalValidatorModel(valueUri="https://example.org").valueUri
    )
    assert inst.rule[0].type == "permit"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_permission_1(base_settings):
    """No. 1 tests collection for Permission.
    Test File: permission-example-vhdir.json
    """
    filename = base_settings["unittest_data_dir"] / "permission-example-vhdir.json"
    inst = permission.Permission.model_validate_json(filename.read_bytes())
    assert "Permission" == inst.get_resource_type()

    impl_permission_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Permission" == data["resourceType"]

    inst2 = permission.Permission(**data)
    impl_permission_1(inst2)


def impl_permission_2(inst):
    assert inst.combining == "deny-overrides"
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering ' "here]</div>"
    )
    assert inst.text.status == "generated"


def test_permission_2(base_settings):
    """No. 2 tests collection for Permission.
    Test File: permission-example.json
    """
    filename = base_settings["unittest_data_dir"] / "permission-example.json"
    inst = permission.Permission.model_validate_json(filename.read_bytes())
    assert "Permission" == inst.get_resource_type()

    impl_permission_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Permission" == data["resourceType"]

    inst2 = permission.Permission(**data)
    impl_permission_2(inst2)


def impl_permission_3(inst):
    assert inst.asserter.reference == "Organization/f203"
    assert inst.combining == "deny-overrides"
    assert (
        inst.date[0] == ExternalValidatorModel(valueDateTime="2018-12-24").valueDateTime
    )
    assert inst.id == "example-saner"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.rule[0].activity[0].action[0].coding[0].code == "access"
    assert (
        inst.rule[0].activity[0].action[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/consentaction"
        ).valueUri
    )
    assert inst.rule[0].activity[0].actor[0].reference == "Organization/f203"
    assert inst.rule[0].activity[0].purpose[0].coding[0].code == "HCOMPL"
    assert (
        inst.rule[0].activity[0].purpose[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.rule[0].data[0].expression.expression == (
        "http://hl7.org/fhir/uv/saner/Measure/CDCHealthcareSupplyPath" "way"
    )
    assert inst.rule[0].data[0].expression.language == "text/fhirpath"
    assert inst.rule[0].limit[0].coding[0].code == "AUDIT"
    assert (
        inst.rule[0].limit[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActCode"
        ).valueUri
    )
    assert inst.rule[0].type == "permit"
    assert inst.status == "active"
    assert inst.text.status == "generated"


def test_permission_3(base_settings):
    """No. 3 tests collection for Permission.
    Test File: permission-example-saner.json
    """
    filename = base_settings["unittest_data_dir"] / "permission-example-saner.json"
    inst = permission.Permission.model_validate_json(filename.read_bytes())
    assert "Permission" == inst.get_resource_type()

    impl_permission_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Permission" == data["resourceType"]

    inst2 = permission.Permission(**data)
    impl_permission_3(inst2)
