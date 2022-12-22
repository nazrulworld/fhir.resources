# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Composition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import composition


def impl_composition_1(inst):
    assert inst.attester[0].mode == "legal"
    assert inst.attester[0].party.display == "Harold Hippocrates, MD"
    assert inst.attester[0].party.reference == "Practitioner/xcda-author"
    assert inst.attester[0].time == fhirtypes.DateTime.validate("2012-01-04T09:10:14Z")
    assert inst.author[0].display == "Harold Hippocrates, MD"
    assert inst.author[0].reference == "Practitioner/xcda-author"
    assert inst.category[0].coding[0].code == "LP173421-1"
    assert inst.category[0].coding[0].display == "Report"
    assert inst.category[0].coding[0].system == "http://loinc.org"
    assert inst.confidentiality == "N"
    assert inst.custodian.display == "Good Health Clinic"
    assert inst.custodian.reference == "Organization/2.16.840.1.113883.19.5"
    assert inst.date == fhirtypes.DateTime.validate("2018-10-30T16:56:04+11:00")
    assert inst.id == "example-mixed"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.section[0].code.coding[0].code == "newborn"
    assert inst.section[0].code.coding[0].display == "New Born Details"
    assert inst.section[0].code.coding[0].system == "http://acme.org/codes/SectionType"
    assert inst.section[0].text.status == "generated"
    assert inst.section[0].title == "Child's Details"
    assert inst.section[1].code.coding[0].code == "mother"
    assert inst.section[1].code.coding[0].display == "Mother's Details"
    assert inst.section[1].code.coding[0].system == "http://acme.org/codes/SectionType"
    assert inst.section[1].text.status == "generated"
    assert inst.section[1].title == "Mpther's Details"
    assert inst.status == "final"
    assert inst.subject.display == "Tahlia Smith"
    assert inst.subject.reference == "Patient/newborn"
    assert inst.text.status == "generated"
    assert inst.title == "Discharge Summary (Neonatal Service)"
    assert inst.type.coding[0].code == "78418-1"
    assert (
        inst.type.coding[0].display == "Neonatal perinatal medicine Discharge summary"
    )
    assert inst.type.coding[0].system == "http://loinc.org"


def test_composition_1(base_settings):
    """No. 1 tests collection for Composition.
    Test File: composition-example-mixed.json
    """
    filename = base_settings["unittest_data_dir"] / "composition-example-mixed.json"
    inst = composition.Composition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Composition" == inst.resource_type

    impl_composition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Composition" == data["resourceType"]

    inst2 = composition.Composition(**data)
    impl_composition_1(inst2)


def impl_composition_2(inst):
    assert inst.attester[0].mode == "legal"
    assert inst.attester[0].party.display == "Harold Hippocrates, MD"
    assert inst.attester[0].party.reference == "Practitioner/xcda-author"
    assert inst.attester[0].time == fhirtypes.DateTime.validate("2012-01-04T09:10:14Z")
    assert inst.author[0].display == "Harold Hippocrates, MD"
    assert inst.author[0].reference == "Practitioner/xcda-author"
    assert inst.category[0].coding[0].code == "LP173421-1"
    assert inst.category[0].coding[0].display == "Report"
    assert inst.category[0].coding[0].system == "http://loinc.org"
    assert inst.confidentiality == "N"
    assert inst.custodian.display == "Good Health Clinic"
    assert inst.custodian.reference == "Organization/2.16.840.1.113883.19.5"
    assert inst.date == fhirtypes.DateTime.validate("2012-01-04T09:10:14Z")
    assert inst.encounter.reference == "Encounter/xcda"
    assert inst.event[0].code[0].coding[0].code == "HEALTHREC"
    assert inst.event[0].code[0].coding[0].display == "health record"
    assert (
        inst.event[0].code[0].coding[0].system
        == "http://terminology.hl7.org/CodeSystem/v3-ActCode"
    )
    assert inst.event[0].detail[0].reference == "Observation/example"
    assert inst.event[0].period.end == fhirtypes.DateTime.validate("2012-11-12")
    assert inst.event[0].period.start == fhirtypes.DateTime.validate("2010-07-18")
    assert inst.id == "example"
    assert inst.identifier.system == "http://healthintersections.com.au/test"
    assert inst.identifier.value == "1"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.relatesTo[0].code == "replaces"
    assert inst.relatesTo[0].targetReference.reference == "Composition/old-example"
    assert inst.relatesTo[1].code == "appends"
    assert (
        inst.relatesTo[1].targetIdentifier.system
        == "http://example.org/fhir/NamingSystem/document-ids"
    )
    assert inst.relatesTo[1].targetIdentifier.value == "ABC123"
    assert inst.section[0].code.coding[0].code == "11348-0"
    assert inst.section[0].code.coding[0].display == "History of past illness Narrative"
    assert inst.section[0].code.coding[0].system == "http://loinc.org"
    assert inst.section[0].entry[0].reference == "Condition/stroke"
    assert inst.section[0].entry[1].reference == "Condition/example"
    assert inst.section[0].entry[2].reference == "Condition/example2"
    assert inst.section[0].mode == "snapshot"
    assert inst.section[0].orderedBy.coding[0].code == "event-date"
    assert inst.section[0].orderedBy.coding[0].display == "Sorted by Event Date"
    assert (
        inst.section[0].orderedBy.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/list-order"
    )
    assert inst.section[0].text.status == "generated"
    assert inst.section[0].title == "History of present illness"
    assert inst.section[1].code.coding[0].code == "10157-6"
    assert (
        inst.section[1].code.coding[0].display
        == "History of family member diseases Narrative"
    )
    assert inst.section[1].code.coding[0].system == "http://loinc.org"
    assert inst.section[1].emptyReason.coding[0].code == "withheld"
    assert inst.section[1].emptyReason.coding[0].display == "Information Withheld"
    assert (
        inst.section[1].emptyReason.coding[0].system
        == "http://terminology.hl7.org/CodeSystem/list-empty-reason"
    )
    assert inst.section[1].mode == "snapshot"
    assert inst.section[1].text.status == "generated"
    assert inst.section[1].title == "History of family member diseases"
    assert inst.status == "final"
    assert inst.subject.display == "Henry Levin the 7th"
    assert inst.subject.reference == "Patient/xcda"
    assert inst.text.status == "generated"
    assert inst.title == "Consultation Note"
    assert inst.type.coding[0].code == "11488-4"
    assert inst.type.coding[0].display == "Consult note"
    assert inst.type.coding[0].system == "http://loinc.org"


def test_composition_2(base_settings):
    """No. 2 tests collection for Composition.
    Test File: composition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "composition-example.json"
    inst = composition.Composition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Composition" == inst.resource_type

    impl_composition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Composition" == data["resourceType"]

    inst2 = composition.Composition(**data)
    impl_composition_2(inst2)
