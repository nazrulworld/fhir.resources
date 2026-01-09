# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentResponse
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import enrollmentresponse
from .conftest import ExternalValidatorModel


def impl_enrollmentresponse_1(inst):
    assert (
        inst.created
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-08-16"}
        ).valueDateTime
    )
    assert inst.disposition == "Dependant added to policy."
    assert inst.id == "ER2500"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.BenefitsInc.com/fhir/enrollmentresponse"}
        ).valueUri
    )
    assert inst.identifier[0].value == "781234"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.organization.reference == "Organization/2"
    assert inst.outcome == "complete"
    assert (
        inst.request.reference
        == "http://www.BenefitsInc.com/fhir/eligibility/225476332402"
    )
    assert inst.requestProvider.reference == "Organization/1"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the EnrollmentResponse</div>"
    )
    assert inst.text.status == "generated"


def test_enrollmentresponse_1(base_settings):
    """No. 1 tests collection for EnrollmentResponse.
    Test File: enrollmentresponse-example.json
    """
    filename = base_settings["unittest_data_dir"] / "enrollmentresponse-example.json"
    inst = enrollmentresponse.EnrollmentResponse.model_validate_json(
        filename.read_bytes()
    )
    assert "EnrollmentResponse" == inst.get_resource_type()

    impl_enrollmentresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "EnrollmentResponse" == data["resourceType"]

    inst2 = enrollmentresponse.EnrollmentResponse(**data)
    impl_enrollmentresponse_1(inst2)
