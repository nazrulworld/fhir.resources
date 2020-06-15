# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import valueset


def impl_valueset_1(inst):
    assert inst.compose.include[0].system == "http://hl7.org/fhir/encounter-status"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "Current state of the encounter"
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[0].valueString == "Informative"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[1].valueInteger == 2
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[2].valueCode == "pa"
    assert inst.id == "encounter-status"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.241"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "EncounterStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/encounter-status"
    assert inst.version == "3.0.1"


def test_valueset_1(base_settings):
    """No. 1 tests collection for ValueSet.
    Test File: valueset-encounter-status.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-encounter-status.json"
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
    assert inst.compose.include[0].system == "http://hl7.org/fhir/report-status-codes"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "The current status of the test report."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[0].valueString == "Informative"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[1].valueInteger == 0
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[2].valueCode == "fhir"
    assert inst.id == "report-status-codes"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.712"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "TestReportStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/report-status-codes"
    assert inst.version == "3.0.1"


def test_valueset_2(base_settings):
    """No. 2 tests collection for ValueSet.
    Test File: valueset-report-status-codes.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-report-status-codes.json"
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
    assert inst.compose.include[0].system == "http://hl7.org/fhir/note-type"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "The presentation types of notes."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[0].valueString == "Informative"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[1].valueInteger == 2
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[2].valueCode == "fm"
    assert inst.id == "note-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.15"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "NoteType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/note-type"
    assert inst.version == "3.0.1"


def test_valueset_3(base_settings):
    """No. 3 tests collection for ValueSet.
    Test File: valueset-note-type.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-note-type.json"
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
    assert inst.compose.include[0].system == "https://precision.fda.gov/apps/"
    assert inst.compose.include[1].system == "https://precision.fda.gov/jobs/"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "This value set includes sequence quality method"
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[0].valueString == "Informative"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[1].valueInteger == 1
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[2].valueCode == "cg"
    assert inst.id == "sequence-quality-method"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.218"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "FDA-Method"
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/sequence-quality-method"
    assert inst.version == "3.0.1"


def test_valueset_4(base_settings):
    """No. 4 tests collection for ValueSet.
    Test File: valueset-sequence-quality-method.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-sequence-quality-method.json"
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
    assert inst.compose.include[0].system == "http://hl7.org/fhir/issue-severity"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "How the issue affects the success of the action."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[0].valueString == "Informative"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[1].valueInteger == 5
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[2].valueCode == "fhir"
    assert inst.id == "issue-severity"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.397"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "IssueSeverity"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/issue-severity"
    assert inst.version == "3.0.1"


def test_valueset_5(base_settings):
    """No. 5 tests collection for ValueSet.
    Test File: valueset-issue-severity.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-issue-severity.json"
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
    assert inst.compose.include[0].system == "http://www.ensembl.org"
    assert inst.compose.include[1].system == "http://www.ncbi.nlm.nih.gov/nuccore"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "This value set includes all Reference codes"
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[0].valueString == "Informative"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[1].valueInteger == 1
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[2].valueCode == "cg"
    assert inst.id == "sequence-referenceSeq"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.216"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "ENSEMBL"
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/sequence-referenceSeq"
    assert inst.version == "3.0.1"


def test_valueset_6(base_settings):
    """No. 6 tests collection for ValueSet.
    Test File: valueset-sequence-referenceSeq.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-sequence-referenceSeq.json"
    )
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
    assert inst.compose.include[0].system == "http://hl7.org/fhir/processoutcomecodes"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.copyright == "This is an example set."
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "This value set includes sample Process Outcome codes."
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[0].valueString == "Informative"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[1].valueInteger == 1
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[2].valueCode == "fm"
    assert inst.id == "process-outcome"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.677"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "Process Outcome Codes"
    assert inst.publisher == "Financial Management"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/process-outcome"
    assert inst.version == "3.0.1"


def test_valueset_7(base_settings):
    """No. 7 tests collection for ValueSet.
    Test File: valueset-process-outcome.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-process-outcome.json"
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
    assert inst.compose.include[0].system == "http://hl7.org/fhir/claim-exception"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.copyright == "This is an example set."
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "This value set includes sample Exception codes."
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[0].valueString == "Informative"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[1].valueInteger == 1
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[2].valueCode == "fm"
    assert inst.id == "claim-exception"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.572"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "Exception Codes"
    assert inst.publisher == "Financial Management"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/claim-exception"
    assert inst.version == "3.0.1"


def test_valueset_8(base_settings):
    """No. 8 tests collection for ValueSet.
    Test File: valueset-claim-exception.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-claim-exception.json"
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
    assert inst.compose.include[0].system == "http://hl7.org/fhir/dicom-audit-lifecycle"
    assert inst.compose.include[1].system == "http://hl7.org/fhir/iso-21089-lifecycle"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-02-19T18:00:00+01:00")
    assert inst.description == (
        "This example FHIR value set is comprised of lifecycle event "
        "codes. The FHIR Actor value set is based on    DICOM Audit "
        "Message, ParticipantObjectDataLifeCycle;   ISO Standard, TS "
        "21089-2017;  "
    )
    assert inst.experimental is False
    assert inst.extensible is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "sec"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[1].valueString == "Trial Use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 3
    assert inst.id == "object-lifecycle-events"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.name == "ObjectLifecycleEvents"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml"> This value set '
        "includes codes from multiple codesets. </div>"
    )
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/object-lifecycle-events"
    assert inst.version == "1.1.0"


def test_valueset_9(base_settings):
    """No. 9 tests collection for ValueSet.
    Test File: valueset-object-lifecycle-events.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-object-lifecycle-events.json"
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
    assert inst.compose.include[0].system == "http://hl7.org/fhir/entformula-additive"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[0].valueString == "Informative"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[1].valueInteger == 1
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[2].valueCode == "oo"
    assert inst.id == "entformula-additive"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.379"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "Enteral Formula Additive Type Code"
    assert inst.publisher == "FHIR NutritionOrder team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ValueSet/entformula-additive"
    assert inst.version == "3.0.1"


def test_valueset_10(base_settings):
    """No. 10 tests collection for ValueSet.
    Test File: valueset-entformula-additive.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-entformula-additive.json"
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
