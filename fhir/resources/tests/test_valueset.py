# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import valueset


def impl_valueset_1(inst):
    assert inst.compose.include[0].concept[0].code == "ActivityDefinition"
    assert inst.compose.include[0].concept[1].code == "ChargeItemDefinition"
    assert inst.compose.include[0].concept[2].code == "ClinicalUseDefinition"
    assert inst.compose.include[0].concept[3].code == "EventDefinition"
    assert inst.compose.include[0].concept[4].code == "Measure"
    assert inst.compose.include[0].concept[5].code == "MessageDefinition"
    assert inst.compose.include[0].concept[6].code == "ObservationDefinition"
    assert inst.compose.include[0].concept[7].code == "OperationDefinition"
    assert inst.compose.include[0].concept[8].code == "PlanDefinition"
    assert inst.compose.include[0].concept[9].code == "Questionnaire"
    assert inst.compose.include[0].system == "http://hl7.org/fhir/fhir-types"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2023-03-26T15:21:02+11:00")
    assert inst.description == "All Resource Types that represent definition resources"
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "normative"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 5
    assert inst.id == "definition-resource-types"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.1056"
    assert inst.immutable is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2023-03-26T15:21:02.749+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "DefinitionResourceTypes"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "extensions"
    assert inst.title == "Definition Resource Types"
    assert inst.url == "http://hl7.org/fhir/ValueSet/definition-resource-types"
    assert inst.version == "5.0.0"


def test_valueset_1(base_settings):
    """No. 1 tests collection for ValueSet.
    Test File: valueset-definition-resource-types.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-definition-resource-types.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_1(inst2)


def impl_valueset_2(inst):
    assert (
        inst.compose.include[0].system
        == "http://terminology.hl7.org/CodeSystem/location-physical-type"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == (
        "This example value set defines a set of codes that can be "
        "used to indicate the physical form of the Location."
    )
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "pa"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "location-form"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.328"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2023-03-26T15:21:02.749+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "LocationForm"
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Location Form"
    assert inst.url == "http://hl7.org/fhir/ValueSet/location-form"
    assert inst.version == "5.0.0"


def test_valueset_2(base_settings):
    """No. 2 tests collection for ValueSet.
    Test File: valueset-location-form.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-location-form.json"
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_2(inst2)


def impl_valueset_3(inst):
    assert inst.compose.include[0].system == "http://hl7.org/fhir/genomicstudy-status"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == "The status of the GenomicStudy."
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "cg"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "genomicstudy-status"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.3083"
    assert inst.immutable is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2023-03-26T15:21:02.749+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "GenomicStudyStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><ul><li>Include '
        'all codes defined in <a href="codesystem-genomicstudy-'
        'status.html"><code>http://hl7.org/fhir/genomicstudy-'
        "status</code></a></li></ul></div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Genomic Study Status"
    assert inst.url == "http://hl7.org/fhir/ValueSet/genomicstudy-status"
    assert inst.version == "5.0.0"


def test_valueset_3(base_settings):
    """No. 3 tests collection for ValueSet.
    Test File: valueset-genomicstudy-status.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-genomicstudy-status.json"
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_3(inst2)


def impl_valueset_4(inst):
    assert inst.compose.include[0].concept[0].code == "7771000"
    assert inst.compose.include[0].concept[0].display == "Left (qualifier value)"
    assert inst.compose.include[0].concept[1].code == "24028007"
    assert inst.compose.include[0].concept[1].display == "Right (qualifier value)"
    assert inst.compose.include[0].concept[2].code == "51440002"
    assert inst.compose.include[0].concept[2].display == "Bilateral"
    assert inst.compose.include[0].concept[3].code == "46053002"
    assert inst.compose.include[0].concept[3].display == "Distal"
    assert inst.compose.include[0].concept[4].code == "255554000"
    assert inst.compose.include[0].concept[4].display == "Dorsal"
    assert inst.compose.include[0].concept[5].code == "264147007"
    assert inst.compose.include[0].concept[5].display == "Plantar"
    assert inst.compose.include[0].concept[6].code == "261183002"
    assert inst.compose.include[0].concept[6].display == "Upper"
    assert inst.compose.include[0].concept[7].code == "261122009"
    assert inst.compose.include[0].concept[7].display == "Lower"
    assert inst.compose.include[0].concept[8].code == "255561001"
    assert inst.compose.include[0].concept[8].display == "Medial"
    assert inst.compose.include[0].concept[9].code == "49370004"
    assert inst.compose.include[0].concept[9].display == "Lateral"
    assert inst.compose.include[0].system == "http://snomed.info/sct"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == "SNOMED-CT concepts modifying the anatomic location"
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "oo"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "bodystructure-relative-location"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.140"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2023-03-26T15:21:02.749+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "BodystructureLocationQualifier"
    assert inst.publisher == "Order and Observation Workgroup"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Bodystructure Location Qualifier"
    assert inst.url == "http://hl7.org/fhir/ValueSet/bodystructure-relative-location"
    assert inst.version == "5.0.0"


def test_valueset_4(base_settings):
    """No. 4 tests collection for ValueSet.
    Test File: valueset-bodystructure-relative-location.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-bodystructure-relative-location.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_4(inst2)


def impl_valueset_5(inst):
    assert inst.compose.include[0].system == "http://hl7.org/fhir/encounter-status"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == "Current state of the encounter."
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "pa"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 4
    assert inst.id == "encounter-status"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.246"
    assert inst.identifier[1].system == "urn:ietf:rfc:3986"
    assert inst.identifier[1].use == "old"
    assert inst.identifier[1].value == "urn:oid:2.16.840.1.113883.4.642.3.241"
    assert inst.immutable is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2023-03-26T15:21:02.749+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "EncounterStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><ul><li>Include '
        'all codes defined in <a href="codesystem-encounter-'
        'status.html"><code>http://hl7.org/fhir/encounter-'
        "status</code></a></li></ul></div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Encounter Status"
    assert inst.url == "http://hl7.org/fhir/ValueSet/encounter-status"
    assert inst.version == "5.0.0"


def test_valueset_5(base_settings):
    """No. 5 tests collection for ValueSet.
    Test File: valueset-encounter-status.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-encounter-status.json"
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_5(inst2)


def impl_valueset_6(inst):
    assert inst.compose.include[0].system == "http://hl7.org/fhir/report-status-codes"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == "The current status of the test report."
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "report-status-codes"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.724"
    assert inst.identifier[1].system == "urn:ietf:rfc:3986"
    assert inst.identifier[1].use == "old"
    assert inst.identifier[1].value == "urn:oid:2.16.840.1.113883.4.642.3.712"
    assert inst.immutable is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2023-03-26T15:21:02.749+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "TestReportStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><ul><li>Include '
        'all codes defined in <a href="codesystem-report-status-'
        'codes.html"><code>http://hl7.org/fhir/report-status-'
        "codes</code></a></li></ul></div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Test Report Status"
    assert inst.url == "http://hl7.org/fhir/ValueSet/report-status-codes"
    assert inst.version == "5.0.0"


def test_valueset_6(base_settings):
    """No. 6 tests collection for ValueSet.
    Test File: valueset-report-status-codes.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-report-status-codes.json"
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_6(inst2)


def impl_valueset_7(inst):
    assert inst.compose.include[0].system == "http://hl7.org/fhir/note-type"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2023-03-26T15:21:02+11:00")
    assert inst.description == "The presentation types of notes."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fm"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 4
    assert inst.id == "note-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.15"
    assert inst.immutable is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2023-03-26T15:21:02.749+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "NoteType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><ul><li>Include '
        'all codes defined in <a href="codesystem-note-'
        'type.html"><code>http://hl7.org/fhir/note-'
        "type</code></a></li></ul></div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "NoteType"
    assert inst.url == "http://hl7.org/fhir/ValueSet/note-type"
    assert inst.version == "5.0.0"


def test_valueset_7(base_settings):
    """No. 7 tests collection for ValueSet.
    Test File: valueset-note-type.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-note-type.json"
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_7(inst2)


def impl_valueset_8(inst):
    assert inst.compose.include[0].system == "http://hl7.org/fhir/issue-severity"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == "How the issue affects the success of the action."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "normative"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "normative-version"
    )
    assert inst.extension[2].valueCode == "4.0.0"
    assert inst.extension[3].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[3].valueInteger == 5
    assert inst.id == "issue-severity"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.408"
    assert inst.identifier[1].system == "urn:ietf:rfc:3986"
    assert inst.identifier[1].use == "old"
    assert inst.identifier[1].value == "urn:oid:2.16.840.1.113883.4.642.3.397"
    assert inst.identifier[2].system == "urn:ietf:rfc:3986"
    assert inst.identifier[2].use == "old"
    assert inst.identifier[2].value == "urn:oid:2.16.840.1.113883.4.642.2.223"
    assert inst.immutable is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2023-03-26T15:21:02.749+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "IssueSeverity"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"><ul><li>Include '
        'all codes defined in <a href="codesystem-issue-'
        'severity.html"><code>http://hl7.org/fhir/issue-'
        "severity</code></a></li></ul></div>"
    )
    assert inst.text.status == "generated"
    assert inst.title == "Issue Severity"
    assert inst.url == "http://hl7.org/fhir/ValueSet/issue-severity"
    assert inst.version == "5.0.0"


def test_valueset_8(base_settings):
    """No. 8 tests collection for ValueSet.
    Test File: valueset-issue-severity.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-issue-severity.json"
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_8(inst2)


def impl_valueset_9(inst):
    assert (
        inst.compose.include[0].system
        == "http://hl7.org/fhir/substance-source-material-genus"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == (
        "The genus of an organism, typically referring to the Latin "
        "epithet of the genus element of the plant/animal scientific "
        "name."
    )
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "brr"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "substance-source-material-genus"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.3253"
    assert inst.immutable is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2023-03-26T15:21:02.749+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "SourceMaterialGenus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Source Material Genus"
    assert inst.url == "http://hl7.org/fhir/ValueSet/substance-source-material-genus"
    assert inst.version == "5.0.0"


def test_valueset_9(base_settings):
    """No. 9 tests collection for ValueSet.
    Test File: valueset-substance-source-material-genus.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-substance-source-material-genus.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_9(inst2)


def impl_valueset_10(inst):
    assert (
        inst.compose.include[0].system == "http://hl7.org/fhir/cited-artifact-part-type"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2020-12-28T16:55:11+11:00")
    assert inst.description == (
        "To describe the reason for the variant citation, such as "
        "version number or subpart specification."
    )
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "cds"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "cited-artifact-part-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.2964"
    assert inst.immutable is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2023-03-26T15:21:02.749+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "CitedArtifactPartType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Cited Artifact Part Type"
    assert inst.url == "http://hl7.org/fhir/ValueSet/cited-artifact-part-type"
    assert inst.version == "5.0.0"


def test_valueset_10(base_settings):
    """No. 10 tests collection for ValueSet.
    Test File: valueset-cited-artifact-part-type.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-cited-artifact-part-type.json"
    )
    inst = valueset.ValueSet.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "ValueSet" == inst.resource_type

    impl_valueset_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_10(inst2)
