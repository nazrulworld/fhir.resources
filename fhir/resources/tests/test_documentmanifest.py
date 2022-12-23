# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentManifest
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import documentmanifest


def impl_documentmanifest_1(inst):
    assert inst.author[0].reference == "#a1"
    assert inst.contained[0].id == "a1"
    assert inst.content[0].reference == "DocumentReference/example"
    assert inst.created == fhirtypes.DateTime.validate("2004-12-25T23:50:50-05:00")
    assert inst.description == "Physical"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://example.org/documents"
    assert inst.identifier[0].value == "23425234234-2347"
    assert inst.masterIdentifier.system == "http://example.org/documents"
    assert inst.masterIdentifier.value == "23425234234-2346"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.recipient[0].reference == "Practitioner/xcda1"
    assert inst.related[0].identifier.system == "http://example.org/documents"
    assert inst.related[0].identifier.value == "23425234234-9999"
    assert inst.related[0].ref.reference == "DocumentReference/example"
    assert inst.source == "urn:oid:1.3.6.1.4.1.21367.2009.1.2.1"
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.div == '<div xmlns="http://www.w3.org/1999/xhtml">Text</div>'
    assert inst.text.status == "generated"
    assert inst.type.text == "History and Physical"


def test_documentmanifest_1(base_settings):
    """No. 1 tests collection for DocumentManifest.
    Test File: documentmanifest-example.json
    """
    filename = base_settings["unittest_data_dir"] / "documentmanifest-example.json"
    inst = documentmanifest.DocumentManifest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentManifest" == inst.resource_type

    impl_documentmanifest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentManifest" == data["resourceType"]

    inst2 = documentmanifest.DocumentManifest(**data)
    impl_documentmanifest_1(inst2)


def impl_documentmanifest_2(inst):
    assert inst.contained[0].id == "org-1"
    assert inst.contained[1].id == "a1"
    assert inst.contained[2].id == "a2"
    assert inst.content[0].reference == "#a1"
    assert inst.content[1].reference == "#a2"
    assert inst.content[2].reference == "DocumentReference/example"
    assert inst.content[3].reference == "DiagnosticReport/f001"
    assert inst.created == fhirtypes.DateTime.validate("2014-09-21T11:50:23-05:00")
    assert inst.id == "654789"
    assert inst.identifier[0].system == "http://happyvalley.com/supportingdocumentation"
    assert inst.identifier[0].value == "52345"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.recipient[0].reference == "#org-1"
    assert inst.related[0].identifier.system == "http://happyvalley.com/claim"
    assert inst.related[0].identifier.value == "12345"
    assert (
        inst.related[1].identifier.system
        == "http://www.BenefitsInc.com/fhir/remittance"
    )
    assert inst.related[1].identifier.value == "R3500"
    assert inst.status == "current"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A Financial '
        "Management Attachment example</div>"
    )
    assert inst.text.status == "generated"


def test_documentmanifest_2(base_settings):
    """No. 2 tests collection for DocumentManifest.
    Test File: documentmanifest-fm-attachment.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "documentmanifest-fm-attachment.json"
    )
    inst = documentmanifest.DocumentManifest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentManifest" == inst.resource_type

    impl_documentmanifest_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentManifest" == data["resourceType"]

    inst2 = documentmanifest.DocumentManifest(**data)
    impl_documentmanifest_2(inst2)
