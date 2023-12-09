# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import valueset


def impl_valueset_1(inst):
    assert (
        inst.compose.include[0].system
        == "http://terminology.hl7.org/CodeSystem/device-status-reason"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-17T07:06:13+11:00")
    assert inst.description == "The availability status reason of the device."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "oo"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 2
    assert inst.id == "device-status-reason"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.1081"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T13:47:40.239+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "FHIRDeviceStatusReason"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "FHIRDeviceStatusReason"
    assert inst.url == "http://hl7.org/fhir/ValueSet/device-status-reason"
    assert inst.version == "4.3.0"


def test_valueset_1(base_settings):
    """No. 1 tests collection for ValueSet.
    Test File: valueset-device-status-reason.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-device-status-reason.json"
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
        == "http://hl7.org/fhir/definition-resource-types"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.description == (
        "A list of all the definition resource types defined in this "
        "version of the FHIR specification."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "vocab"
    assert inst.id == "definition-resource-types"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.1056"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T12:47:40.239+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "DefinitionResourceType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "DefinitionResourceType"
    assert inst.url == "http://hl7.org/fhir/ValueSet/definition-resource-types"
    assert inst.version == "4.3.0"


def test_valueset_2(base_settings):
    """No. 2 tests collection for ValueSet.
    Test File: valueset-definition-resource-types.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-definition-resource-types.json"
    )
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
    assert inst.compose.include[0].concept[0].code == "419161000"
    assert inst.compose.include[0].concept[0].display == "Unilateral left"
    assert inst.compose.include[0].concept[1].code == "419465000"
    assert inst.compose.include[0].concept[1].display == "Unilateral right"
    assert inst.compose.include[0].concept[2].code == "51440002"
    assert inst.compose.include[0].concept[2].display == "Bilateral"
    assert inst.compose.include[0].concept[3].code == "261183002"
    assert inst.compose.include[0].concept[3].display == "Upper"
    assert inst.compose.include[0].concept[4].code == "261122009"
    assert inst.compose.include[0].concept[4].display == "Lower"
    assert inst.compose.include[0].concept[5].code == "255561001"
    assert inst.compose.include[0].concept[5].display == "Medial"
    assert inst.compose.include[0].concept[6].code == "49370004"
    assert inst.compose.include[0].concept[6].display == "Lateral"
    assert inst.compose.include[0].concept[7].code == "264217000"
    assert inst.compose.include[0].concept[7].display == "Superior"
    assert inst.compose.include[0].concept[8].code == "261089000"
    assert inst.compose.include[0].concept[8].display == "Inferior"
    assert inst.compose.include[0].concept[9].code == "255551008"
    assert inst.compose.include[0].concept[9].display == "Posterior"
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
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T12:47:40.239+10:00"
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
    assert inst.version == "4.3.0"


def test_valueset_3(base_settings):
    """No. 3 tests collection for ValueSet.
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

    impl_valueset_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_3(inst2)


def impl_valueset_4(inst):
    assert inst.compose.include[0].system == "http://hl7.org/fhir/encounter-status"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-17T07:06:13+11:00")
    assert inst.description == "Current state of the encounter."
    assert inst.experimental is False
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
    assert inst.extension[2].valueInteger == 2
    assert inst.id == "encounter-status"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.246"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T13:47:40.239+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "EncounterStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "EncounterStatus"
    assert inst.url == "http://hl7.org/fhir/ValueSet/encounter-status"
    assert inst.version == "4.3.0"


def test_valueset_4(base_settings):
    """No. 4 tests collection for ValueSet.
    Test File: valueset-encounter-status.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-encounter-status.json"
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
    assert (
        inst.compose.include[0].system
        == "http://terminology.hl7.org/CodeSystem/consentscope"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.copyright == "This is an example set."
    assert inst.description == "This value set includes the four Consent scope codes."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "cbcc"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 2
    assert inst.id == "consent-scope"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.761"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T12:47:40.239+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "ConsentScopeCodes"
    assert inst.publisher == "CBCC"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Consent Scope Codes"
    assert inst.url == "http://hl7.org/fhir/ValueSet/consent-scope"
    assert inst.version == "4.3.0"


def test_valueset_5(base_settings):
    """No. 5 tests collection for ValueSet.
    Test File: valueset-consent-scope.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-consent-scope.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2021-01-17T07:06:13+11:00")
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
    assert inst.extension[2].valueInteger == 0
    assert inst.id == "report-status-codes"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.724"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T13:47:40.239+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "TestReportStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "TestReportStatus"
    assert inst.url == "http://hl7.org/fhir/ValueSet/report-status-codes"
    assert inst.version == "4.3.0"


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
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
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
    assert inst.extension[2].valueInteger == 2
    assert inst.id == "note-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.15"
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T12:47:40.239+10:00"
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
    assert inst.version == "4.3.0"


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
    assert inst.compose.include[0].system == "https://precision.fda.gov/apps/"
    assert inst.compose.include[1].system == "https://precision.fda.gov/jobs/"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == "This value set includes sequence quality method"
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "cg"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "sequence-quality-method"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.223"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T12:47:40.239+10:00"
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
    assert inst.version == "4.3.0"


def test_valueset_8(base_settings):
    """No. 8 tests collection for ValueSet.
    Test File: valueset-sequence-quality-method.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-sequence-quality-method.json"
    )
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
    assert inst.compose.include[0].system == "http://hl7.org/fhir/issue-severity"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-17T07:06:13+11:00")
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
    assert inst.immutable is True
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T13:47:40.239+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.name == "IssueSeverity"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "IssueSeverity"
    assert inst.url == "http://hl7.org/fhir/ValueSet/issue-severity"
    assert inst.version == "4.3.0"


def test_valueset_9(base_settings):
    """No. 9 tests collection for ValueSet.
    Test File: valueset-issue-severity.json
    """
    filename = base_settings["unittest_data_dir"] / "valueset-issue-severity.json"
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
    assert inst.compose.include[0].system == "http://www.ensembl.org"
    assert inst.compose.include[1].system == "http://www.ncbi.nlm.nih.gov/nuccore"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.description == "This value set includes all Reference codes"
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "cg"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "sequence-referenceSeq"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.221"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T12:47:40.239+10:00"
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
    assert inst.version == "4.3.0"


def test_valueset_10(base_settings):
    """No. 10 tests collection for ValueSet.
    Test File: valueset-sequence-referenceSeq.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "valueset-sequence-referenceSeq.json"
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
