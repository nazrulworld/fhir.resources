# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
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
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
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
    assert inst.identifier[1].system == "urn:ietf:rfc:3986"
    assert inst.identifier[1].use == "old"
    assert inst.identifier[1].value == "urn:oid:2.16.840.1.113883.4.642.1.662"
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
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "StructureMapModelMode"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Structure Map Model Mode"
    assert inst.url == "http://hl7.org/fhir/map-model-mode"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/map-model-mode"
    assert inst.version == "5.0.0"


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
    assert inst.concept[0].code == "medication"
    assert inst.concept[0].display == "Medication"
    assert inst.concept[1].code == "device"
    assert inst.concept[1].display == "Device"
    assert inst.concept[2].code == "intervention"
    assert inst.concept[2].display == "Intervention"
    assert inst.concept[3].code == "factor"
    assert inst.concept[3].display == "Factor"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-15T16:55:11.085+11:00")
    assert inst.description == "Codes for the main intent of the study."
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
    assert inst.extension[2].valueInteger == 0
    assert inst.id == "research-study-focus-type"
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
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "ResearchStudyFocusType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "ResearchStudy Focus Type Code System"
    assert inst.url == "http://hl7.org/fhir/research-study-focus-type"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/research-study-focus-type"
    assert inst.version == "5.0.0"


def test_codesystem_2(base_settings):
    """No. 2 tests collection for CodeSystem.
    Test File: codesystem-research-study-focus-type.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-research-study-focus-type.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
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
    assert inst.identifier[1].system == "urn:ietf:rfc:3986"
    assert inst.identifier[1].use == "old"
    assert inst.identifier[1].value == "urn:oid:2.16.840.1.113883.4.642.1.768"
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
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "CodeSystemHierarchyMeaning"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Code System Hierarchy Meaning"
    assert inst.url == "http://hl7.org/fhir/codesystem-hierarchy-meaning"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning"
    assert inst.version == "5.0.0"


def test_codesystem_3(base_settings):
    """No. 3 tests collection for CodeSystem.
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

    impl_codesystem_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "CodeSystem" == data["resourceType"]

    inst2 = codesystem.CodeSystem(**data)
    impl_codesystem_3(inst2)


def impl_codesystem_4(inst):
    assert inst.caseSensitive is True
    assert inst.concept[0].code == "create"
    assert inst.concept[0].definition == (
        "create(type : string) - type is passed through to the "
        "application on the standard API, and must be known by it."
    )
    assert inst.concept[0].display == "create"
    assert inst.concept[0].property[0].code == "fhirpath"
    assert inst.concept[0].property[0].valueString == "n/a"
    assert inst.concept[1].code == "copy"
    assert inst.concept[1].definition == "copy(source)."
    assert inst.concept[1].display == "copy"
    assert inst.concept[1].property[0].code == "fhirpath"
    assert inst.concept[1].property[0].valueString == "n/a"
    assert inst.concept[2].code == "truncate"
    assert (
        inst.concept[2].definition
        == "truncate(source, length) - source must be stringy type."
    )
    assert inst.concept[2].display == "truncate"
    assert inst.concept[2].property[0].code == "fhirpath"
    assert inst.concept[2].property[0].valueString == "substring"
    assert inst.concept[3].code == "escape"
    assert inst.concept[3].definition == (
        "escape(source, fmt1, fmt2) - change source from one kind of "
        "escaping to another (plain, java, xml, json). note that this"
        " is for when the string itself is escaped."
    )
    assert inst.concept[3].display == "escape"
    assert inst.concept[3].property[0].code == "fhirpath"
    assert inst.concept[3].property[0].valueString == "n/a"
    assert inst.concept[4].code == "cast"
    assert inst.concept[4].display == "cast"
    assert inst.concept[4].property[0].code == "fhirpath"
    assert inst.concept[4].property[0].valueString == "n/a"
    assert inst.concept[5].code == "append"
    assert (
        inst.concept[5].definition == "append(source...) - source is element or string."
    )
    assert inst.concept[5].display == "append"
    assert inst.concept[5].property[0].code == "fhirpath"
    assert inst.concept[5].property[0].valueString == "& (String concatenation)"
    assert inst.concept[6].code == "translate"
    assert (
        inst.concept[6].definition
        == "translate(source, uri_of_map) - use the translate operation."
    )
    assert inst.concept[6].display == "translate"
    assert inst.concept[6].property[0].code == "fhirpath"
    assert inst.concept[6].property[0].valueString == "%terminologies.translate()"
    assert inst.concept[7].code == "reference"
    assert inst.concept[7].definition == (
        "reference(source : object) - return a string that references"
        " the provided tree properly."
    )
    assert inst.concept[7].display == "reference"
    assert inst.concept[7].property[0].code == "fhirpath"
    assert (
        inst.concept[7].property[0].valueString
        == "related to resolve() but returns the string pointer"
    )
    assert inst.concept[8].code == "dateOp"
    assert (
        inst.concept[8].definition
        == "Perform a date operation. *Parameters to be documented*."
    )
    assert inst.concept[8].display == "dateOp"
    assert inst.concept[8].property[0].code == "fhirpath"
    assert inst.concept[8].property[0].valueString == "n/a"
    assert inst.concept[9].code == "uuid"
    assert (
        inst.concept[9].definition
        == "Generate a random UUID (in lowercase). No Parameters."
    )
    assert inst.concept[9].display == "uuid"
    assert inst.concept[9].property[0].code == "fhirpath"
    assert inst.concept[9].property[0].valueString == "n/a"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
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
    assert inst.identifier[1].system == "urn:ietf:rfc:3986"
    assert inst.identifier[1].use == "old"
    assert inst.identifier[1].value == "urn:oid:2.16.840.1.113883.4.642.1.668"
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
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "StructureMapTransform"
    assert inst.property[0].code == "fhirpath"
    assert inst.property[0].description == "FHIRPath equivalent for transform function"
    assert inst.property[0].type == "string"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Structure Map Transform"
    assert inst.url == "http://hl7.org/fhir/map-transform"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/map-transform"
    assert inst.version == "5.0.0"


def test_codesystem_4(base_settings):
    """No. 4 tests collection for CodeSystem.
    Test File: codesystem-map-transform.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-map-transform.json"
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
    assert inst.concept[4].code == "indicated-only-after"
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
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.1994"
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
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "TherapyRelationshipType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Therapy Relationship Type"
    assert inst.url == "http://hl7.org/fhir/therapy-relationship-type"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/therapy-relationship-type"
    assert inst.version == "5.0.0"


def test_codesystem_5(base_settings):
    """No. 5 tests collection for CodeSystem.
    Test File: codesystem-therapy-relationship-type.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-therapy-relationship-type.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
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
    assert inst.extension[2].valueInteger == 4
    assert inst.id == "imagingstudy-status"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.991"
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
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "ImagingStudyStatus"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Imaging Study Status"
    assert inst.url == "http://hl7.org/fhir/imagingstudy-status"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/imagingstudy-status"
    assert inst.version == "5.0.0"


def test_codesystem_6(base_settings):
    """No. 6 tests collection for CodeSystem.
    Test File: codesystem-imagingstudy-status.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "codesystem-imagingstudy-status.json"
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
    assert inst.concept[0].code == "medication"
    assert inst.concept[0].definition == "Medication Catalog."
    assert inst.concept[0].display == "Medication Catalog"
    assert inst.concept[1].code == "device"
    assert inst.concept[1].definition == "Device Catalog."
    assert inst.concept[1].display == "Device Catalog"
    assert inst.concept[2].code == "protocol"
    assert inst.concept[2].definition == "Protocol List."
    assert inst.concept[2].display == "Protocol List"
    assert inst.content == "complete"
    assert inst.description == "CatalogType"
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "sd"
    assert inst.id == "catalogType"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.2013"
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
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "CatalogType"
    assert inst.publisher == "HL7 International"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Catalog Type"
    assert inst.url == "http://hl7.org/fhir/catalogType"
    assert inst.version == "5.0.0"


def test_codesystem_7(base_settings):
    """No. 7 tests collection for CodeSystem.
    Test File: codesystem-catalogType.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-catalogType.json"
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
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2023-03-26T15:21:02+11:00")
    assert inst.description == (
        "One of the message events defined as part of this version of" " FHIR."
    )
    assert inst.experimental is True
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/valueset-special-" "status"
    )
    assert inst.extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[1].valueCode == "inm"
    assert inst.extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-"
        "standards-status"
    )
    assert inst.extension[2].valueCode == "draft"
    assert inst.extension[3].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "fmm"
    )
    assert inst.extension[3].valueInteger == 1
    assert inst.id == "message-events"
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == "http://unstats.un.org/unsd/methods/m49/m49.htm"
    )
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2023-03-26T15:21:02.749+11:00"
    )
    assert inst.name == "MessageEvent"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "MessageEvent"
    assert inst.url == "http://hl7.org/fhir/message-events"
    assert inst.version == "5.0.0"


def test_codesystem_8(base_settings):
    """No. 8 tests collection for CodeSystem.
    Test File: codesystem-message-events.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-message-events.json"
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
    assert inst.concept[0].code == "100000072072"
    assert inst.concept[0].display == "Active"
    assert inst.concept[1].code == "100000072073"
    assert inst.concept[1].display == "Adjuvant"
    assert inst.concept[2].code == "100000072082"
    assert inst.concept[2].display == "Excipient"
    assert inst.concept[3].code == "100000136065"
    assert inst.concept[3].display == "Starting material for excipient"
    assert inst.concept[4].code == "100000136066"
    assert inst.concept[4].display == "Solvent / Diluent"
    assert inst.concept[5].code == "100000136178"
    assert (
        inst.concept[5].display
        == "Raw materials used in the manufacture of the product"
    )
    assert inst.concept[6].code == "100000136179"
    assert inst.concept[6].display == "Starting material for active substance"
    assert inst.concept[7].code == "100000136561"
    assert inst.concept[7].display == "Overage"
    assert inst.concept[8].code == "200000003427"
    assert inst.concept[8].display == "bioenhancer"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.content == "complete"
    assert inst.date == fhirtypes.DateTime.validate("2021-01-05T10:01:24+11:00")
    assert inst.description == (
        "A classification of the ingredient identifying its purpose "
        "within the product, e.g. active, inactive."
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
    assert inst.id == "ingredient-role"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.2080"
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
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "IngredientRole"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Ingredient Role"
    assert inst.url == "http://hl7.org/fhir/ingredient-role"
    assert inst.valueSet == "http://hl7.org/fhir/ValueSet/ingredient-role"
    assert inst.version == "5.0.0"


def test_codesystem_9(base_settings):
    """No. 9 tests collection for CodeSystem.
    Test File: codesystem-ingredient-role.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-ingredient-role.json"
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
    assert inst.caseSensitive is False
    assert inst.concept[0].code == "aliceblue"
    assert inst.concept[0].display == "aliceblue"
    assert inst.concept[0].property[0].code == "rgb"
    assert inst.concept[0].property[0].valueString == "#F0F8FF"
    assert inst.concept[1].code == "antiquewhite"
    assert inst.concept[1].display == "antiquewhite"
    assert inst.concept[1].property[0].code == "rgb"
    assert inst.concept[1].property[0].valueString == "#FAEBD7"
    assert inst.concept[2].code == "aqua"
    assert inst.concept[2].display == "aqua"
    assert inst.concept[2].property[0].code == "rgb"
    assert inst.concept[2].property[0].valueString == "#00FFFF"
    assert inst.concept[3].code == "aquamarine"
    assert inst.concept[3].display == "aquamarine"
    assert inst.concept[3].property[0].code == "rgb"
    assert inst.concept[3].property[0].valueString == "#7FFFD4"
    assert inst.concept[4].code == "azure"
    assert inst.concept[4].display == "azure"
    assert inst.concept[4].property[0].code == "rgb"
    assert inst.concept[4].property[0].valueString == "#F0FFFF"
    assert inst.concept[5].code == "beige"
    assert inst.concept[5].display == "beige"
    assert inst.concept[5].property[0].code == "rgb"
    assert inst.concept[5].property[0].valueString == "#F5F5DC"
    assert inst.concept[6].code == "bisque"
    assert inst.concept[6].display == "bisque"
    assert inst.concept[6].property[0].code == "rgb"
    assert inst.concept[6].property[0].valueString == "#FFE4C4"
    assert inst.concept[7].code == "black"
    assert inst.concept[7].display == "black"
    assert inst.concept[7].property[0].code == "rgb"
    assert inst.concept[7].property[0].valueString == "#000000"
    assert inst.concept[8].code == "blanchedalmond"
    assert inst.concept[8].display == "blanchedalmond"
    assert inst.concept[8].property[0].code == "rgb"
    assert inst.concept[8].property[0].valueString == "#FFEBCD"
    assert inst.concept[9].code == "blue"
    assert inst.concept[9].display == "blue"
    assert inst.concept[9].property[0].code == "rgb"
    assert inst.concept[9].property[0].valueString == "#0000FF"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.content == "complete"
    assert inst.experimental is False
    assert inst.extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/structuredefinition-" "wg"
    )
    assert inst.extension[0].valueCode == "fhir"
    assert inst.id == "color-names"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.4.2120"
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
        == "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
    )
    assert inst.name == "ColorCodes"
    assert inst.property[0].code == "rgb"
    assert inst.property[0].description == (
        "The RGB color that matches the named color (as defined in "
        "CSS4 specification)"
    )
    assert inst.property[0].type == "string"
    assert inst.publisher == "FHIR Infrastructure"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Codes for Colors"
    assert inst.url == "http://hl7.org/fhir/color-names"
    assert inst.version == "5.0.0"


def test_codesystem_10(base_settings):
    """No. 10 tests collection for CodeSystem.
    Test File: codesystem-color-names.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-color-names.json"
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
