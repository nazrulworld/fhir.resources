# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GuidanceResponse
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import guidanceresponse
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_guidanceresponse_1(inst):
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
    assert inst.reasonCode[0].text == "Guideline Appropriate Ordering Assessment"
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


def test_guidanceresponse_1(base_settings):
    """No. 1 tests collection for GuidanceResponse.
    Test File: guidanceresponse-example.json
    """
    filename = base_settings["unittest_data_dir"] / "guidanceresponse-example.json"
    inst = guidanceresponse.GuidanceResponse.model_validate_json(filename.read_bytes())
    assert "GuidanceResponse" == inst.get_resource_type()

    impl_guidanceresponse_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "GuidanceResponse" == data["resourceType"]

    inst2 = guidanceresponse.GuidanceResponse(**data)
    impl_guidanceresponse_1(inst2)
