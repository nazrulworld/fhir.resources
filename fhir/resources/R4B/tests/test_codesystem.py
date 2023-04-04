# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import codesystem


def impl_codesystem_1(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "source"
    assert inst.concept[0].definition == (
        "This structure describes an instance passed to the mapping "
        "engine that is used a source of data."
    )
    assert inst.concept[0].display == "Source Structure Definition"
    assert inst.concept[1].code == "queried"
    assert inst.concept[1].definition == (
        "This structure describes an instance that the mapping engine"
        " may ask for that is used a source of data."
    )
    assert inst.concept[1].display == "Queried Structure Definition"
    assert inst.concept[2].code == "target"
    assert inst.concept[2].definition == (
        "This structure describes an instance passed to the mapping "
        "engine that is used a target of data."
    )
    assert inst.concept[2].display == "Target Structure Definition"
    assert inst.concept[3].code == "produced"
    assert inst.concept[3].definition == (
        "This structure describes an instance that the mapping engine"
        " may ask to create that is used a target of data."
    )
    assert inst.concept[3].display == "Produced Structure Definition"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-17T07:06:13+11:00")
    assert inst.description == "How the referenced structure is used in this mapping."
    assert inst.experimental is False
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
    assert inst.extension[2].valueInteger == 2
    assert inst.id == "map-model-mode"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.676"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T13:47:40.239+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "StructureMapModelMode"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "StructureMapModelMode"
    assert inst.url == "http://hl7.org/fhir/map-model-mode"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/map-model-mode"
    assert inst.version == "4.3.0"


def test_codesystem_1(base_settings):
    """No. 1 tests collection for CodeSystem.
    Test File: codesystem-map-model-mode.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-map-model-mode.json"
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_1(inst2)


def impl_codesystem_2(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "true"
    assert inst.concept[0].definition == "Boolean true."
    assert inst.concept[0].display == "true"
    assert inst.concept[1].code == "false"
    assert inst.concept[1].definition == "Boolean false."
    assert inst.concept[1].display == "false"
    assert inst.concept[2].code == "trace"
    assert inst.concept[2].definition == (
        "The content is greater than zero, but too small to be " "quantified."
    )
    assert inst.concept[2].display == "Trace Amount Detected"
    assert inst.concept[3].code == "sufficient"
    assert inst.concept[3].definition == (
        "The specific quantity is not known, but is known to be non-"
        "zero and is not specified because it makes up the bulk of "
        "the material."
    )
    assert inst.concept[3].display == "Sufficient Quantity"
    assert inst.concept[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/codesystem-concept-" "comments"
    )
    assert inst.concept[3].extension[0].valueString == (
        "used in formulations (e.g. 'Add 10mg of ingredient X, 50mg "
        "of ingredient Y, and sufficient quantity of water to 100mL.'"
        " This code would be used to express the quantity of water. )"
    )
    assert inst.concept[4].code == "withdrawn"
    assert inst.concept[4].definition == "The value is no longer available."
    assert inst.concept[4].display == "Value Withdrawn"
    assert inst.concept[5].code == "nil-known"
    assert (
        inst.concept[5].definition
        == "The are no known applicable values in this context."
    )
    assert inst.concept[5].display == "Nil Known"
    assert inst.concept[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/codesystem-concept-" "comments"
    )
    assert (
        inst.concept[5].extension[0].valueString
        == "The existence of this subject to review"
    )
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.description == (
        "A set of generally useful codes defined so they can be "
        "included in value sets."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.id == "special-values"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.1049"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T12:47:40.239+10:00"
    )
    assert inst.name == "SpecialValues"
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert inst.title == "SpecialValues"
    assert inst.url == "http://terminology.hl7.org/CodeSystem/special-values"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/special-values"
    assert inst.version == "4.3.0"


def test_codesystem_2(base_settings):
    """No. 2 tests collection for CodeSystem.
    Test File: codesystem-special-values.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-special-values.json"
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_2(inst2)


def impl_codesystem_3(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "unknown"
    assert (
        inst.concept[0].definition
        == "The communication was not done due to an unknown reason."
    )
    assert inst.concept[0].display == "Unknown"
    assert inst.concept[1].code == "system-error"
    assert (
        inst.concept[1].definition
        == "The communication was not done due to a system error."
    )
    assert inst.concept[1].display == "System Error"
    assert inst.concept[2].code == "invalid-phone-number"
    assert inst.concept[2].definition == (
        "The communication was not done due to an invalid phone " "number."
    )
    assert inst.concept[2].display == "Invalid Phone Number"
    assert inst.concept[3].code == "recipient-unavailable"
    assert inst.concept[3].definition == (
        "The communication was not done due to the recipient being " "unavailable."
    )
    assert inst.concept[3].display == "Recipient Unavailable"
    assert inst.concept[4].code == "family-objection"
    assert (
        inst.concept[4].definition
        == "The communication was not done due to a family objection."
    )
    assert inst.concept[4].display == "Family Objection"
    assert inst.concept[5].code == "patient-objection"
    assert (
        inst.concept[5].definition
        == "The communication was not done due to a patient objection."
    )
    assert inst.concept[5].display == "Patient Objection"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-17T07:06:13+11:00")
    assert (
        inst.description == "Codes for the reason why a communication did not happen."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "pc"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "draft"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 1
    assert inst.id == "communication-not-done-reason"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.1077"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T13:47:40.239+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "CommunicationNotDoneReason"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "CommunicationNotDoneReason"
    assert inst.url == (
        "http://terminology.hl7.org/CodeSystem/communication-not-" "done-reason"
    )
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/communication-not-done-reason"
    assert inst.version == "4.3.0"


def test_codesystem_3(base_settings):
    """No. 3 tests collection for CodeSystem.
    Test File: codesystem-communication-not-done-reason.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-communication-not-done-reason.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_3(inst2)


def impl_codesystem_4(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "grouped-by"
    assert inst.concept[0].display == "Grouped By"
    assert inst.concept[1].code == "is-a"
    assert inst.concept[1].display == "Is-A"
    assert inst.concept[2].code == "part-of"
    assert inst.concept[2].definition == (
        "Child elements list the individual parts of a composite "
        "whole (e.g. body site)."
    )
    assert inst.concept[2].display == "Part Of"
    assert inst.concept[3].code == "classified-with"
    assert inst.concept[3].display == "Classified With"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-17T07:06:13+11:00")
    assert (
        inst.description == "The meaning of the hierarchy of concepts in a code system."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "vocab"
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
    assert inst.id == "codesystem-hierarchy-meaning"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.785"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T13:47:40.239+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "CodeSystemHierarchyMeaning"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "CodeSystemHierarchyMeaning"
    assert inst.url == "http://hl7.org/fhir/codesystem-hierarchy-meaning"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning"
    assert inst.version == "4.3.0"


def test_codesystem_4(base_settings):
    """No. 4 tests collection for CodeSystem.
    Test File: codesystem-codesystem-hierarchy-meaning.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-codesystem-hierarchy-meaning.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_4(inst2)


def impl_codesystem_5(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "continuous"
    assert inst.concept[0].definition == (
        "A medication which is expected to be continued beyond the "
        "present order and which the patient should be assumed to be "
        "taking unless explicitly stopped."
    )
    assert inst.concept[0].display == "Continuous long term therapy"
    assert inst.concept[1].code == "acute"
    assert inst.concept[1].definition == (
        "A medication which the patient is only expected to consume "
        "for the duration of the current order and which is not "
        "expected to be renewed."
    )
    assert inst.concept[1].display == "Short course (acute) therapy"
    assert inst.concept[2].code == "seasonal"
    assert inst.concept[2].definition == (
        "A medication which is expected to be used on a part time "
        "basis at certain times of the year"
    )
    assert inst.concept[2].display == "Seasonal"
    assert inst.content == "complete"
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "phx"
    assert inst.id == "medicationrequest-course-of-therapy"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.1327"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T12:47:40.239+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "MedicationRequest Course of Therapy Codes"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == (
        "http://terminology.hl7.org/CodeSystem/medicationrequest-" "course-of-therapy"
    )
    assert inst.valueSet == (
        "http://hl7.org/fhir/ValueSet/medicationrequest-course-of-" "therapy"
    )
    assert inst.version == "4.3.0"


def test_codesystem_5(base_settings):
    """No. 5 tests collection for CodeSystem.
    Test File: codesystem-medicationrequest-course-of-therapy.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "codesystem-medicationrequest-course-of-therapy.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_5(inst2)


def impl_codesystem_6(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "0"
    assert inst.concept[0].definition == (
        "The operation completed successfully (whether with warnings " "or not)."
    )
    assert inst.concept[0].display == "Success"
    assert inst.concept[1].code == "4"
    assert inst.concept[1].definition == (
        "The action was not successful due to some kind of minor "
        "failure (often equivalent to an HTTP 400 response)."
    )
    assert inst.concept[1].display == "Minor failure"
    assert inst.concept[2].code == "8"
    assert inst.concept[2].definition == (
        "The action was not successful due to some kind of unexpected"
        " error (often equivalent to an HTTP 500 response)."
    )
    assert inst.concept[2].display == "Serious failure"
    assert inst.concept[3].code == "12"
    assert inst.concept[3].definition == (
        "An error of such magnitude occurred that the system is no "
        "longer available for use (i.e. the system died)."
    )
    assert inst.concept[3].display == "Major failure"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-17T07:06:13+11:00")
    assert inst.description == "Indicates whether the event succeeded or failed."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "sec"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 3
    assert inst.id == "audit-event-outcome"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.455"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T13:47:40.239+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "AuditEventOutcome"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "AuditEventOutcome"
    assert inst.url == "http://hl7.org/fhir/audit-event-outcome"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/audit-event-outcome"
    assert inst.version == "4.3.0"


def test_codesystem_6(base_settings):
    """No. 6 tests collection for CodeSystem.
    Test File: codesystem-audit-event-outcome.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-audit-event-outcome.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_6(inst2)


def impl_codesystem_7(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "disclosure-ca"
    assert (
        inst.concept[0].definition == "Canadian health information disclosure policy."
    )
    assert inst.concept[0].display == "Disclosure-CA"
    assert inst.concept[1].code == "disclosure-us"
    assert (
        inst.concept[1].definition
        == "United States health information disclosure policy."
    )
    assert inst.concept[1].display == "Disclosure-US"
    assert inst.content == "complete"
    assert inst.copyright == "This is an example set."
    assert inst.description == "This value set includes sample Contract Subtype codes."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fm"
    assert inst.id == "contract-subtype"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.0"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T12:47:40.239+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "ContractSubtypeCodes"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Contract Subtype Codes"
    assert inst.url == "http://hl7.org/fhir/contract-subtype"
    assert inst.version == "4.3.0"


def test_codesystem_7(base_settings):
    """No. 7 tests collection for CodeSystem.
    Test File: codesystem-contract-subtype.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-contract-subtype.json"
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_7(inst2)


def impl_codesystem_8(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "create"
    assert inst.concept[0].definition == (
        "create(type : string) - type is passed through to the "
        "application on the standard API, and must be known by it."
    )
    assert inst.concept[0].display == "create"
    assert inst.concept[1].code == "copy"
    assert inst.concept[1].definition == "copy(source)."
    assert inst.concept[1].display == "copy"
    assert inst.concept[2].code == "truncate"
    assert (
        inst.concept[2].definition
        == "truncate(source, length) - source must be stringy type."
    )
    assert inst.concept[2].display == "truncate"
    assert inst.concept[3].code == "escape"
    assert inst.concept[3].definition == (
        "escape(source, fmt1, fmt2) - change source from one kind of "
        "escaping to another (plain, java, xml, json). note that this"
        " is for when the string itself is escaped."
    )
    assert inst.concept[3].display == "escape"
    assert inst.concept[4].code == "cast"
    assert inst.concept[4].definition == (
        "cast(source, type?) - case source from one type to another. "
        "target type can be left as implicit if there is one and only"
        " one target type known."
    )
    assert inst.concept[4].display == "cast"
    assert inst.concept[5].code == "append"
    assert (
        inst.concept[5].definition == "append(source...) - source is element or string."
    )
    assert inst.concept[5].display == "append"
    assert inst.concept[6].code == "translate"
    assert (
        inst.concept[6].definition
        == "translate(source, uri_of_map) - use the translate operation."
    )
    assert inst.concept[6].display == "translate"
    assert inst.concept[7].code == "reference"
    assert inst.concept[7].definition == (
        "reference(source : object) - return a string that references"
        " the provided tree properly."
    )
    assert inst.concept[7].display == "reference"
    assert inst.concept[8].code == "dateOp"
    assert (
        inst.concept[8].definition
        == "Perform a date operation. *Parameters to be documented*."
    )
    assert inst.concept[8].display == "dateOp"
    assert inst.concept[9].code == "uuid"
    assert (
        inst.concept[9].definition
        == "Generate a random UUID (in lowercase). No Parameters."
    )
    assert inst.concept[9].display == "uuid"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-17T07:06:13+11:00")
    assert inst.description == "How data is copied/created."
    assert inst.experimental is False
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
    assert inst.extension[2].valueInteger == 2
    assert inst.id == "map-transform"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.682"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T13:47:40.239+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "StructureMapTransform"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "StructureMapTransform"
    assert inst.url == "http://hl7.org/fhir/map-transform"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/map-transform"
    assert inst.version == "4.3.0"


def test_codesystem_8(base_settings):
    """No. 8 tests collection for CodeSystem.
    Test File: codesystem-map-transform.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-map-transform.json"
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_8(inst2)


def impl_codesystem_9(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "contraindicated-only-with"
    assert (
        inst.concept[0].definition
        == "Only contraindicated if the other therapy is given"
    )
    assert (
        inst.concept[0].display == "Only contraindicated if the other therapy is given"
    )
    assert inst.concept[1].code == "contraindicated-except-with"
    assert (
        inst.concept[1].definition
        == "Contraindicated unless the other therapy is given"
    )
    assert (
        inst.concept[1].display == "Contraindicated unless the other therapy is given"
    )
    assert inst.concept[2].code == "indicated-only-with"
    assert inst.concept[2].definition == (
        "Indicated only when the other therapy is given (co-" "occurrent)"
    )
    assert inst.concept[2].display == (
        "Indicated only when the other therapy is given (co-" "occurrent)"
    )
    assert inst.concept[3].code == "indicated-except-with"
    assert (
        inst.concept[3].definition == "Indicated except when the other therapy is given"
    )
    assert inst.concept[3].display == "Indicated except when the other therapy is given"
    assert inst.concept[4].code == "indicated-only-before"
    assert inst.concept[4].definition == (
        "Indicated only if the other therapy is planned to be given "
        "afterwards (prep)"
    )
    assert inst.concept[4].display == (
        "Indicated only if the other therapy is planned to be given "
        "afterwards (prep)"
    )
    assert inst.concept[5].code == "indicated-only-before"
    assert inst.concept[5].definition == (
        "Indicated only if the other therapy was given before " "(follow-up)"
    )
    assert inst.concept[5].display == (
        "Indicated only if the other therapy was given before " "(follow-up)"
    )
    assert inst.concept[6].code == "replace-other-therapy"
    assert inst.concept[6].definition == "Indicated to replace the other therapy"
    assert inst.concept[6].display == "Indicated to replace the other therapy"
    assert inst.concept[7].code == "replace-other-therapy-contraindicated"
    assert (
        inst.concept[7].definition
        == "Indicated to replace the other contraindicated therapy."
    )
    assert (
        inst.concept[7].display
        == "Indicated to replace the other contraindicated therapy"
    )
    assert inst.concept[8].code == "replace-other-therapy-not-tolerated"
    assert inst.concept[8].definition == (
        "Indicated to replace the other therapy not well tolerated by" " patient"
    )
    assert inst.concept[8].display == (
        "Indicated to replace the other therapy not well tolerated by" " patient"
    )
    assert inst.concept[9].code == "replace-other-therapy-not-effective"
    assert inst.concept[9].definition == (
        "Indicated to replace the other therapy not effective on " "patient"
    )
    assert inst.concept[9].display == (
        "Indicated to replace the other therapy not effective on " "patient"
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-08-15T16:55:11+11:00")
    assert inst.description == (
        "Classification of relationship between a therapy and a "
        "contraindication or an indication."
    )
    assert inst.experimental is False
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
    assert inst.id == "therapy-relationship-type"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.1.1560"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T13:47:40.239+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "TherapyRelationshipType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "TherapyRelationshipType"
    assert inst.url == "http://hl7.org/fhir/therapy-relationship-type"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/therapy-relationship-type"
    assert inst.version == "4.3.0"


def test_codesystem_9(base_settings):
    """No. 9 tests collection for CodeSystem.
    Test File: codesystem-therapy-relationship-type.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-therapy-relationship-type.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_9(inst2)


def impl_codesystem_10(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "registered"
    assert inst.concept[0].definition == (
        "The existence of the imaging study is registered, but there "
        "is nothing yet available."
    )
    assert inst.concept[0].display == "Registered"
    assert inst.concept[1].code == "available"
    assert inst.concept[1].definition == (
        "At least one instance has been associated with this imaging " "study."
    )
    assert inst.concept[1].display == "Available"
    assert inst.concept[2].code == "cancelled"
    assert inst.concept[2].definition == (
        "The imaging study is unavailable because the imaging study "
        "was not started or not completed (also sometimes called "
        '"aborted").'
    )
    assert inst.concept[2].display == "Cancelled"
    assert inst.concept[3].code == "entered-in-error"
    assert inst.concept[3].display == "Entered in Error"
    assert inst.concept[4].code == "unknown"
    assert inst.concept[4].display == "Unknown"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-17T07:06:13+11:00")
    assert inst.description == "The status of the ImagingStudy."
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "ii"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[2].valueInteger == 3
    assert inst.id == "imagingstudy-status"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.991"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2022-05-28T13:47:40.239+11:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "ImagingStudyStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "ImagingStudyStatus"
    assert inst.url == "http://hl7.org/fhir/imagingstudy-status"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/imagingstudy-status"
    assert inst.version == "4.3.0"


def test_codesystem_10(base_settings):
    """No. 10 tests collection for CodeSystem.
    Test File: codesystem-imagingstudy-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-imagingstudy-status.json"
    )
    inst = codesystem.CodeSystem.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "CodeSystem" == inst.resource_type

    impl_codesystem_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_10(inst2)
