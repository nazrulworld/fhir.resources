# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import codesystem


def impl_codesystem_1(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "source"
    assert inst.concept[0].definition == (
        "This structure describes an instance passed to the mapping "
        "engine that is used a source of data"
    )
    assert inst.concept[0].display == "Source Structure Definition"
    assert inst.concept[1].code == "queried"
    assert inst.concept[1].definition == (
        "This structure describes an instance that the mapping engine"
        " may ask for that is used a source of data"
    )
    assert inst.concept[1].display == "Queried Structure Definition"
    assert inst.concept[2].code == "target"
    assert inst.concept[2].definition == (
        "This structure describes an instance passed to the mapping "
        "engine that is used a target of data"
    )
    assert inst.concept[2].display == "Target Structure Definition"
    assert inst.concept[3].code == "produced"
    assert inst.concept[3].definition == (
        "This structure describes an instance that the mapping engine"
        " may ask to create that is used a target of data"
    )
    assert inst.concept[3].display == "Produced Structure Definition"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "How the referenced structure is used in this mapping"
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
    assert inst.extension[2].valueCode == "fhir"
    assert inst.id == "map-model-mode"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.662"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.name == "StructureMapModelMode"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/map-model-mode"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/map-model-mode"
    assert inst.version == "3.0.1"


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
    assert inst.concept[0].code == "ampoule"
    assert inst.concept[0].definition == "A sealed glass capsule containing a liquid"
    assert inst.concept[0].display == "Ampoule"
    assert inst.concept[1].code == "bottle"
    assert inst.concept[1].definition == (
        "A container, typically made of glass or plastic and with a "
        "narrow neck, used for storing liquids."
    )
    assert inst.concept[1].display == "Bottle"
    assert inst.concept[2].code == "box"
    assert inst.concept[2].definition == (
        "A container with a flat base and sides, typically square or "
        "rectangular and having a lid."
    )
    assert inst.concept[2].display == "Box"
    assert inst.concept[3].code == "cartridge"
    assert inst.concept[3].definition == (
        "A device of various configuration and composition used with "
        "a syringe for the application of anesthetic or other "
        "materials to a patient."
    )
    assert inst.concept[3].display == "Cartridge"
    assert inst.concept[4].code == "container"
    assert inst.concept[4].definition == "A package intended to store pharmaceuticals."
    assert inst.concept[4].display == "Container"
    assert inst.concept[5].code == "tube"
    assert inst.concept[5].definition == (
        "A long, hollow cylinder of metal, plastic, glass, etc., for "
        "holding medications, typically creams or ointments"
    )
    assert inst.concept[5].display == "Tube"
    assert inst.concept[6].code == "unitdose"
    assert inst.concept[6].definition == (
        "A dose of medicine prepared in an individual package for "
        "convenience, safety or monitoring."
    )
    assert inst.concept[6].display == "Unit Dose Blister"
    assert inst.concept[7].code == "vial"
    assert inst.concept[7].definition == (
        "A small container, typically cylindrical and made of glass, "
        "used especially for holding liquid medications."
    )
    assert inst.concept[7].display == "Vial"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == (
        "A coded concept defining the kind of container a medication "
        "package is packaged in"
    )
    assert inst.experimental is False
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
    assert inst.extension[2].valueCode == "phx"
    assert inst.id == "medication-package-form"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.362"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.name == "MedicationContainer"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/medication-package-form"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/medication-package-form"
    assert inst.version == "3.0.1"


def test_codesystem_2(base_settings):
    """No. 2 tests collection for CodeSystem.
    Test File: codesystem-medication-package-form.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-medication-package-form.json"
    )
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
    assert (
        inst.concept[3].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/codesystem-comments"
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
    assert (
        inst.concept[5].extension[0].url
        == "http://hl7.org/fhir/StructureDefinition/codesystem-comments"
    )
    assert (
        inst.concept[5].extension[0].valueString
        == "The existence of this subject to review"
    )
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == (
        "A set of generally useful codes defined so they can be "
        "included in value sets."
    )
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[0].valueString == "Informative"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[1].valueInteger == 0
    assert inst.id == "special-values"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.10"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.name == "SpecialValues"
    assert inst.status == "draft"
    assert inst.text.status == "extensions"
    assert inst.url == "http://hl7.org/fhir/special-values"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/special-values"
    assert inst.version == "3.0.1"


def test_codesystem_3(base_settings):
    """No. 3 tests collection for CodeSystem.
    Test File: codesystem-special-values.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-special-values.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "Codes for the reason why a communication was not done."
    assert inst.experimental is False
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
    assert inst.extension[2].valueCode == "pc"
    assert inst.id == "communication-not-done-reason"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.165"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.name == "CommunicationNotDoneReason"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/communication-not-done-reason"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/communication-not-done-reason"
    assert inst.version == "3.0.1"


def test_codesystem_4(base_settings):
    """No. 4 tests collection for CodeSystem.
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

    impl_codesystem_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_4(inst2)


def impl_codesystem_5(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "grouped-by"
    assert inst.concept[0].display == "Grouped By"
    assert inst.concept[1].code == "is-a"
    assert inst.concept[1].definition == (
        "A hierarchy where the child concepts have an IS-A "
        "relationship with the parents - that is, all the properties "
        "of the parent are also true for its child concepts"
    )
    assert inst.concept[1].display == "Is-A"
    assert inst.concept[2].code == "part-of"
    assert inst.concept[2].definition == (
        "Child elements list the individual parts of a composite "
        "whole (e.g. body site)"
    )
    assert inst.concept[2].display == "Part Of"
    assert inst.concept[3].code == "classified-with"
    assert inst.concept[3].display == "Classified With"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert (
        inst.description == "The meaning of the hierarchy of concepts in a code system"
    )
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
    assert inst.extension[2].valueCode == "vocab"
    assert inst.id == "codesystem-hierarchy-meaning"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.768"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.name == "CodeSystemHierarchyMeaning"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/codesystem-hierarchy-meaning"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning"
    assert inst.version == "3.0.1"


def test_codesystem_5(base_settings):
    """No. 5 tests collection for CodeSystem.
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
        "The action was not successful due to some kind of catered "
        "for error (often equivalent to an HTTP 400 response)."
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
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "Indicates whether the event succeeded or failed"
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "ballot-status"
    )
    assert inst.extension[0].valueString == "Informative"
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[1].valueInteger == 3
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[2].valueCode == "sec"
    assert inst.id == "audit-event-outcome"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.448"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.name == "AuditEventOutcome"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/audit-event-outcome"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/audit-event-outcome"
    assert inst.version == "3.0.1"


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
        inst.concept[0].definition == "Canadian health information displosure policy."
    )
    assert inst.concept[0].display == "Disclosure-CA"
    assert inst.concept[1].code == "disclosure-us"
    assert (
        inst.concept[1].definition
        == "United States health information displosure policy."
    )
    assert inst.concept[1].display == "Disclosure-US"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.content == "complete"
    assert inst.copyright == "This is an example set."
    assert inst.description == "This value set includes sample Contract Subtype codes."
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
    assert inst.id == "contract-subtype"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.720"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "Contract Subtype Codes"
    assert inst.publisher == "Financial Management"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/contractsubtypecodes"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/contract-subtype"
    assert inst.version == "3.0.1"


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
        "application on the standard API, and must be known by it"
    )
    assert inst.concept[0].display == "create"
    assert inst.concept[1].code == "copy"
    assert inst.concept[1].definition == "copy(source)"
    assert inst.concept[1].display == "copy"
    assert inst.concept[2].code == "truncate"
    assert (
        inst.concept[2].definition
        == "truncate(source, length) - source must be stringy type"
    )
    assert inst.concept[2].display == "truncate"
    assert inst.concept[3].code == "escape"
    assert inst.concept[3].definition == (
        "escape(source, fmt1, fmt2) - change source from one kind of "
        "escaping to another (plain, java, xml, json). note that this"
        " is for when the string itself is escaped"
    )
    assert inst.concept[3].display == "escape"
    assert inst.concept[4].code == "cast"
    assert inst.concept[4].definition == (
        "cast(source, type?) - case source from one type to another. "
        "target type can be left as implicit if there is one and only"
        " one target type known"
    )
    assert inst.concept[4].display == "cast"
    assert inst.concept[5].code == "append"
    assert (
        inst.concept[5].definition == "append(source...) - source is element or string"
    )
    assert inst.concept[5].display == "append"
    assert inst.concept[6].code == "translate"
    assert (
        inst.concept[6].definition
        == "translate(source, uri_of_map) - use the translate operation"
    )
    assert inst.concept[6].display == "translate"
    assert inst.concept[7].code == "reference"
    assert inst.concept[7].definition == (
        "reference(source : object) - return a string that references"
        " the provided tree properly"
    )
    assert inst.concept[7].display == "reference"
    assert inst.concept[8].code == "dateOp"
    assert (
        inst.concept[8].definition
        == "Perform a date operation. *Parameters to be documented*"
    )
    assert inst.concept[8].display == "dateOp"
    assert inst.concept[9].code == "uuid"
    assert (
        inst.concept[9].definition
        == "Generate a random UUID (in lowercase). No Parameters"
    )
    assert inst.concept[9].display == "uuid"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == "How data is copied/created"
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
    assert inst.extension[2].valueCode == "fhir"
    assert inst.id == "map-transform"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.668"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.name == "StructureMapTransform"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/map-transform"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/map-transform"
    assert inst.version == "3.0.1"


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
    assert inst.concept[0].code == "benefit"
    assert inst.concept[0].definition == "Maximum benefit allowable."
    assert inst.concept[0].display == "Benefit"
    assert inst.concept[1].code == "deductable"
    assert (
        inst.concept[1].definition == "Cost to be incurred before benefits are applied"
    )
    assert inst.concept[1].display == "Deductable"
    assert inst.concept[2].code == "visit"
    assert inst.concept[2].definition == "Service visit"
    assert inst.concept[2].display == "Visit"
    assert inst.concept[3].code == "room"
    assert inst.concept[3].definition == "Type of room"
    assert inst.concept[3].display == "Room"
    assert inst.concept[4].code == "copay"
    assert inst.concept[4].definition == "Copayment per service"
    assert inst.concept[4].display == "Copayment per service"
    assert inst.concept[5].code == "copay-percent"
    assert inst.concept[5].definition == "Copayment percentage per service"
    assert inst.concept[5].display == "Copayment Percent per service"
    assert inst.concept[6].code == "copay-maximum"
    assert inst.concept[6].definition == "Copayment maximum per service"
    assert inst.concept[6].display == "Copayment maximum per service"
    assert inst.concept[7].code == "vision-exam"
    assert inst.concept[7].definition == "Vision Exam"
    assert inst.concept[7].display == "Vision Exam"
    assert inst.concept[8].code == "vision-glasses"
    assert inst.concept[8].definition == "Frames and lenses"
    assert inst.concept[8].display == "Vision Glasses"
    assert inst.concept[9].code == "vision-contacts"
    assert inst.concept[9].definition == "Contact Lenses"
    assert inst.concept[9].display == "Vision Contacts Coverage"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.content == "complete"
    assert inst.copyright == "This is an example set."
    assert (
        inst.description
        == "This value set includes a smattering of Benefit type codes."
    )
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
    assert inst.id == "benefit-type"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.599"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "Benefit Type Codes"
    assert inst.publisher == "Financial Management"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/benefit-type"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/benefit-type"
    assert inst.version == "3.0.1"


def test_codesystem_9(base_settings):
    """No. 9 tests collection for CodeSystem.
    Test File: codesystem-benefit-type.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-benefit-type.json"
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
    assert inst.concept[0].code == "institutional"
    assert (
        inst.concept[0].definition == "Hospital, clinic and typically inpatient claims."
    )
    assert inst.concept[0].display == "Institutional"
    assert inst.concept[1].code == "oral"
    assert inst.concept[1].definition == "Dental, Denture and Hygiene claims."
    assert inst.concept[1].display == "Oral"
    assert inst.concept[2].code == "pharmacy"
    assert inst.concept[2].definition == "Pharmacy claims for goods and services."
    assert inst.concept[2].display == "Pharmacy"
    assert inst.concept[3].code == "professional"
    assert inst.concept[3].definition == (
        "Typically outpatient claims from Physician, Psychological, "
        "Chiropractor, Physiotherapy, Speach Pathology, "
        "rehabilitative, consulting."
    )
    assert inst.concept[3].display == "Professional"
    assert inst.concept[4].code == "vision"
    assert inst.concept[4].definition == (
        "Vision claims for professional services and products such as"
        " glasses and contact lenses."
    )
    assert inst.concept[4].display == "Vision"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.content == "complete"
    assert inst.copyright == "This is an example set."
    assert inst.description == "This value set includes sample Claim Type codes."
    assert inst.experimental is True
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
    assert inst.id == "claim-type"
    assert inst.identifier.system == "urn:ietf:rfc:3986"
    assert inst.identifier.value == "urn:oid:2.16.840.1.113883.4.642.1.551"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "Example Claim Type Codes"
    assert inst.publisher == "Financial Management"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.url == "http://hl7.org/fhir/ex-claimtype"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/claim-type"
    assert inst.version == "3.0.1"


def test_codesystem_10(base_settings):
    """No. 10 tests collection for CodeSystem.
    Test File: codesystem-claim-type.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-claim-type.json"
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
