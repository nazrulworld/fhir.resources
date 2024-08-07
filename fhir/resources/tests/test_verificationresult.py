# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VerificationResult
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import verificationresult
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_verificationresult_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.status == "attested"
    assert inst.text.status == "generated"


def test_verificationresult_1(base_settings):
    """No. 1 tests collection for VerificationResult.
    Test File: verificationresult-example.json
    """
    filename = base_settings["unittest_data_dir"] / "verificationresult-example.json"
    inst = verificationresult.VerificationResult.model_validate_json(
        filename.read_bytes()
    )
    assert "VerificationResult" == inst.get_resource_type()

    impl_verificationresult_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "VerificationResult" == data["resourceType"]

    inst2 = verificationresult.VerificationResult(**data)
    impl_verificationresult_1(inst2)
