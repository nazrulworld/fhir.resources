# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GuidanceResponse
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import guidanceresponse
from .conftest import ExternalValidatorModel


def impl_guidanceresponse_1(inst):
    assert inst.dataRequirement[0].codeFilter[0].code[0].code == "4548-4"
    assert (
        inst.dataRequirement[0].codeFilter[0].code[0].display
        == "Hemoglobin A1c/Hemoglobin.total in Blood"
    )
    assert (
        inst.dataRequirement[0].codeFilter[0].code[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.dataRequirement[0].codeFilter[0].path == "code"
    assert inst.dataRequirement[0].mustSupport[0] == "value"
    assert inst.dataRequirement[0].type == "Observation"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "additional-data-example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org"}
        ).valueUri
    )
    assert inst.identifier[0].value == "guidanceResponse2"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.moduleUri
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://someguidelineprovider.org/diabetes-guidelines.html"}
        ).valueUri
    )
    assert (
        inst.occurrenceDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2017-03-10T16:02:00Z"}
        ).valueDateTime
    )
    assert inst.performer.reference == "Device/software"
    assert inst.reason[0].concept.text == "Diabetes Guideline"
    assert (
        inst.requestIdentifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org"}
        ).valueUri
    )
    assert inst.requestIdentifier.value == "guidanceRequest2"
    assert inst.status == "data-required"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_guidanceresponse_1(base_settings):
    """No. 1 tests collection for GuidanceResponse.
    Test File: guidanceresponse-additional-data-example.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "guidanceresponse-additional-data-example.json"
    )
    inst = guidanceresponse.GuidanceResponse.model_validate_json(filename.read_bytes())
    assert "GuidanceResponse" == inst.get_resource_type()

    impl_guidanceresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "GuidanceResponse" == data["resourceType"]

    inst2 = guidanceresponse.GuidanceResponse(**data)
    impl_guidanceresponse_1(inst2)


def impl_guidanceresponse_2(inst):
    assert inst.contained[0].id == "outputParameters1"
    assert inst.encounter.reference == "Encounter/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org"}
        ).valueUri
    )
    assert inst.identifier[0].value == "guidanceResponse1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert (
        inst.moduleUri
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://someguidelineprovider.org/radiology-appropriateness-guidelines.html"
            }
        ).valueUri
    )
    assert (
        inst.occurrenceDateTime
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2017-03-10T16:02:00Z"}
        ).valueDateTime
    )
    assert inst.outputParameters.reference == "#outputParameters1"
    assert inst.performer.reference == "Device/software"
    assert inst.reason[0].concept.text == "Guideline Appropriate Ordering Assessment"
    assert (
        inst.requestIdentifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://example.org"}
        ).valueUri
    )
    assert inst.requestIdentifier.value == "guidanceRequest1"
    assert inst.status == "success"
    assert inst.subject.reference == "Patient/example"
    assert inst.text.status == "generated"


def test_guidanceresponse_2(base_settings):
    """No. 2 tests collection for GuidanceResponse.
    Test File: guidanceresponse-example.json
    """
    filename = base_settings["unittest_data_dir"] / "guidanceresponse-example.json"
    inst = guidanceresponse.GuidanceResponse.model_validate_json(filename.read_bytes())
    assert "GuidanceResponse" == inst.get_resource_type()

    impl_guidanceresponse_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "GuidanceResponse" == data["resourceType"]

    inst2 = guidanceresponse.GuidanceResponse(**data)
    impl_guidanceresponse_2(inst2)
