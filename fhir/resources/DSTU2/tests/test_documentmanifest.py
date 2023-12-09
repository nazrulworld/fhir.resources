# -*- coding: utf-8 -*-
from pydantic.v1.datetime_parse import parse_date, parse_datetime

from .. import fhirtypes  # noqa: F401
from .. import documentmanifest


def test_DocumentManifest_1(base_settings):
    filename = (
        base_settings["unittest_data_dir"] / "documentmanifest-example.canonical.json"
    )
    inst = documentmanifest.DocumentManifest.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DocumentManifest" == inst.resource_type
    impl_DocumentManifest_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DocumentManifest" == data["resourceType"]

    inst2 = documentmanifest.DocumentManifest(**data)
    impl_DocumentManifest_1(inst2)


def impl_DocumentManifest_1(inst):
    assert inst.author[0].reference == "#a1"
    assert inst.contained[0].id == "a1"
    assert inst.contained[0].name.family[0] == "Dopplemeyer"
    assert inst.contained[0].name.given[0] == "Sherry"
    assert (
        inst.contained[0].practitionerRole[0].managingOrganization.display
        == "Cleveland Clinic"
    )
    assert inst.contained[0].practitionerRole[0].role.text == "Primary Surgon"
    assert inst.contained[0].practitionerRole[0].specialty[0].text == "Orthopedic"
    assert inst.contained[0].telecom[0].system == "email"
    assert inst.contained[0].telecom[0].value == "john.doe@healthcare.example.org"
    assert inst.content[0].pReference.reference == "DocumentReference/example"
    assert inst.created == parse_datetime("2004-12-25T23:50:50-05:00")
    assert inst.description == "Physical"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://example.org/documents"
    assert inst.identifier[0].value == "23425234234-2347"
    assert inst.masterIdentifier.system == "http://example.org/documents"
    assert inst.masterIdentifier.value == "23425234234-2346"
    assert inst.recipient[0].reference == "Practitioner/xcda1"
    assert inst.related[0].identifier.system == "http://example.org/documents"
    assert inst.related[0].identifier.value == "23425234234-9999"
    assert inst.related[0].ref.reference == "DocumentReference/example"
    assert inst.source == "urn:oid:1.3.6.1.4.1.21367.2009.1.2.1"
    assert inst.status == "current"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.div == "<div>Text</div>"
    assert inst.text.status == "generated"
    assert inst.type.text == "History and Physical"
