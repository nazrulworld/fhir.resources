# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentReference
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from .. import documentreference
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_documentreference_1(inst):
    assert inst.authenticator.reference == "Organization/f001"
    assert inst.author[0].reference == "Practitioner/xcda1"
    assert inst.author[1].reference == "#a2"
    assert inst.category[0].coding[0].code == "History and Physical"
    assert inst.category[0].coding[0].display == "History and Physical"
    assert (
        inst.category[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ihe.net/xds/connectathon/classCodes"}
        ).valueUri
    )
    assert inst.contained[0].id == "a2"
    assert inst.content[0].attachment.contentType == "application/hl7-v3+xml"
    assert (
        inst.content[0].attachment.creation
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2005-12-24T09:35:00+11:00"}
        ).valueDateTime
    )
    assert (
        inst.content[0].attachment.hash
        == ExternalValidatorModel.model_validate(
            {"valueBase64Binary": "2jmj7l5rSw0yVb/vlWAYkK/YBwk="}
        ).valueBase64Binary
    )
    assert inst.content[0].attachment.language == "en-US"
    assert inst.content[0].attachment.size == 3654
    assert inst.content[0].attachment.title == "Physical"
    assert (
        inst.content[0].attachment.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUrl": "http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510"
            }
        ).valueUrl
    )
    assert inst.content[0].format.code == "urn:ihe:pcc:handp:2008"
    assert inst.content[0].format.display == "History and Physical Specification"
    assert (
        inst.content[0].format.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:oid:1.3.6.1.4.1.19376.1.2.3"}
        ).valueUri
    )
    assert inst.context.encounter[0].reference == "Encounter/xcda"
    assert inst.context.event[0].coding[0].code == "T-D8200"
    assert inst.context.event[0].coding[0].display == "Arm"
    assert (
        inst.context.event[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://ihe.net/xds/connectathon/eventCodes"}
        ).valueUri
    )
    assert inst.context.facilityType.coding[0].code == "Outpatient"
    assert inst.context.facilityType.coding[0].display == "Outpatient"
    assert (
        inst.context.facilityType.coding[0].system
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes"
            }
        ).valueUri
    )
    assert (
        inst.context.period.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2004-12-23T08:01:00+11:00"}
        ).valueDateTime
    )
    assert (
        inst.context.period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2004-12-23T08:00:00+11:00"}
        ).valueDateTime
    )
    assert inst.context.practiceSetting.coding[0].code == "General Medicine"
    assert inst.context.practiceSetting.coding[0].display == "General Medicine"
    assert (
        inst.context.practiceSetting.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.ihe.net/xds/connectathon/practiceSettingCodes"}
        ).valueUri
    )
    assert (
        inst.context.related[0].identifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert (
        inst.context.related[0].identifier.value
        == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.2345"
    )
    assert inst.context.related[0].reference == "Patient/xcda"
    assert inst.context.sourcePatientInfo.reference == "Patient/xcda"
    assert inst.custodian.reference == "Organization/f001"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2005-12-24T09:43:41+11:00"}
        ).valueInstant
    )
    assert inst.description == "Physical"
    assert inst.docStatus == "preliminary"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
    assert (
        inst.masterIdentifier.system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.masterIdentifier.value == "urn:oid:1.3.6.1.4.1.21367.2005.3.7"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-ActReason"}
        ).valueUri
    )
    assert inst.relatesTo[0].code == "appends"
    assert inst.relatesTo[0].target.reference == "DocumentReference/example"
    assert inst.securityLabel[0].coding[0].code == "V"
    assert inst.securityLabel[0].coding[0].display == "very restricted"
    assert (
        inst.securityLabel[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"}
        ).valueUri
    )
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "34108-1"
    assert inst.type.coding[0].display == "Outpatient Note"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )


def test_documentreference_1(base_settings):
    """No. 1 tests collection for DocumentReference.
    Test File: documentreference-example.json
    """
    filename = base_settings["unittest_data_dir"] / "documentreference-example.json"
    inst = documentreference.DocumentReference.model_validate_json(
        filename.read_bytes()
    )
    assert "DocumentReference" == inst.get_resource_type()

    impl_documentreference_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "DocumentReference" == data["resourceType"]

    inst2 = documentreference.DocumentReference(**data)
    impl_documentreference_1(inst2)
