# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NamingSystem
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import namingsystem
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_namingsystem_1(inst):
    assert inst.contact[0].name == "HL7 Australia FHIR Team"
    assert inst.contact[0].telecom[0].system == "url"
    assert (
        inst.contact[0].telecom[0].value
        == "http://hl7-australia.wikispaces.com/FHIR+Australia"
    )
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-08-31"}
        ).valueDateTime
    )
    assert inst.description == (
        "Australian HI Identifier as established by relevant " "regulations etc."
    )
    assert inst.id == "example-id"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.22.3"
    assert inst.jurisdiction[0].coding[0].code == "AU"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:iso:std:iso:3166"}
        ).valueUri
    )
    assert inst.kind == "identifier"
    assert inst.name == "AustalianHealthcareIdentifierIndividual"
    assert inst.publisher == "HL7 Australia on behalf of NEHTA"
    assert inst.responsible == "HI Service Operator / NEHTA"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "Austalian Healthcare Identifier - Individual"
    assert inst.type.coding[0].code == "NI"
    assert inst.type.coding[0].display == "National unique individual identifier"
    assert (
        inst.type.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/v2-0203"}
        ).valueUri
    )
    assert inst.type.text == "IHI"
    assert inst.uniqueId[0].comment == "This value is used in Australian CDA documents"
    assert inst.uniqueId[0].type == "oid"
    assert inst.uniqueId[0].value == "1.2.36.1.2001.1003.0"
    assert (
        inst.uniqueId[1].period.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2015-08-21"}
        ).valueDateTime
    )
    assert inst.uniqueId[1].preferred is True
    assert inst.uniqueId[1].type == "uri"
    assert inst.uniqueId[1].value == "http://ns.electronichealth.net.au/id/hi/ihi/1.0"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/example-id"}
        ).valueUri
    )
    assert inst.usage == "Used in Australia for identifying patients"


def test_namingsystem_1(base_settings):
    """No. 1 tests collection for NamingSystem.
    Test File: namingsystem-example-id.json
    """
    filename = base_settings["unittest_data_dir"] / "namingsystem-example-id.json"
    inst = namingsystem.NamingSystem.model_validate_json(filename.read_bytes())
    assert "NamingSystem" == inst.get_resource_type()

    impl_namingsystem_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "NamingSystem" == data["resourceType"]

    inst2 = namingsystem.NamingSystem(**data)
    impl_namingsystem_1(inst2)


def impl_namingsystem_2(inst):
    assert (
        inst.approvalDate
        == ExternalValidatorModel.model_validate({"valueDate": "2021-07-21"}).valueDate
    )
    assert inst.author[0].name == "ACME NamingSystem Development"
    assert inst.author[0].telecom[0].system == "url"
    assert inst.author[0].telecom[0].value == "http://acme.org/development"
    assert inst.contact[0].name == "FHIR project team"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2021-07-21"}
        ).valueDateTime
    )
    assert inst.description == (
        "This is an example naming system that illustrates usage of "
        "the metadata resource elements introduced in R5"
    )
    assert inst.editor[0].name == "ACME NamingSystem Management"
    assert inst.editor[0].telecom[0].system == "url"
    assert inst.editor[0].telecom[0].value == "http://acme.org/management"
    assert (
        inst.effectivePeriod.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-07-31"}
        ).valueDateTime
    )
    assert (
        inst.effectivePeriod.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2021-08-01"}
        ).valueDateTime
    )
    assert inst.endorser[0].name == "National Foundation for NamingSystem Quality"
    assert inst.endorser[0].telecom[0].system == "url"
    assert inst.endorser[0].telecom[0].value == "http://example.org/nfnq"
    assert inst.experimental is True
    assert inst.id == "example-metadata"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.22.5"
    assert inst.kind == "identifier"
    assert (
        inst.lastReviewDate
        == ExternalValidatorModel.model_validate({"valueDate": "2022-07-21"}).valueDate
    )
    assert inst.meta.profile[0] == (
        "http://hl7.org/fhir/StructureDefinition/shareablenamingsyste" "m"
    )
    assert inst.name == "ExampleMetadata"
    assert inst.publisher == "FHIR (Example)"
    assert (
        inst.relatedArtifact[0].resource == "http://hl7.org/fhir/NamingSystem/example"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert inst.reviewer[0].name == "Society for Creative NamingSystem Review"
    assert inst.reviewer[0].telecom[0].system == "url"
    assert inst.reviewer[0].telecom[0].value == "http://example.org/scnr"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Metadata Example"
    assert inst.topic[0].coding[0].code == "treatment"
    assert inst.topic[0].coding[0].display == "Treatment"
    assert (
        inst.topic[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/definition-topic"}
        ).valueUri
    )
    assert inst.uniqueId[0].type == "oid"
    assert inst.uniqueId[0].value == "1.2.3.4.5.6.7"
    assert inst.uniqueId[1].preferred is True
    assert inst.uniqueId[1].type == "uri"
    assert inst.uniqueId[1].value == "http://example.com/identifiers"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/example-metadata"}
        ).valueUri
    )
    assert inst.version == "20210721"


def test_namingsystem_2(base_settings):
    """No. 2 tests collection for NamingSystem.
    Test File: namingsystem-example-metadata.json
    """
    filename = base_settings["unittest_data_dir"] / "namingsystem-example-metadata.json"
    inst = namingsystem.NamingSystem.model_validate_json(filename.read_bytes())
    assert "NamingSystem" == inst.get_resource_type()

    impl_namingsystem_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "NamingSystem" == data["resourceType"]

    inst2 = namingsystem.NamingSystem(**data)
    impl_namingsystem_2(inst2)


def impl_namingsystem_3(inst):
    assert (
        inst.approvalDate
        == ExternalValidatorModel.model_validate({"valueDate": "2021-07-21"}).valueDate
    )
    assert inst.author[0].name == "ACME NamingSystem Development"
    assert inst.author[0].telecom[0].system == "url"
    assert inst.author[0].telecom[0].value == "http://acme.org/development"
    assert inst.contact[0].name == "FHIR project team"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-07-21"}
        ).valueDateTime
    )
    assert inst.description == (
        "This is an example naming system that illustrates usage of "
        "the metadata resource elements introduced in R5"
    )
    assert inst.editor[0].name == "ACME NamingSystem Management"
    assert inst.editor[0].telecom[0].system == "url"
    assert inst.editor[0].telecom[0].value == "http://acme.org/management"
    assert (
        inst.effectivePeriod.end
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-07-31"}
        ).valueDateTime
    )
    assert (
        inst.effectivePeriod.start
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2022-08-01"}
        ).valueDateTime
    )
    assert inst.endorser[0].name == "National Foundation for NamingSystem Quality"
    assert inst.endorser[0].telecom[0].system == "url"
    assert inst.endorser[0].telecom[0].value == "http://example.org/nfnq"
    assert inst.experimental is True
    assert inst.id == "example-metadata-2"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.22.4"
    assert inst.kind == "identifier"
    assert (
        inst.lastReviewDate
        == ExternalValidatorModel.model_validate({"valueDate": "2022-07-21"}).valueDate
    )
    assert inst.meta.profile[0] == (
        "http://hl7.org/fhir/StructureDefinition/shareablenamingsyste" "m"
    )
    assert inst.name == "ExampleMetadata"
    assert inst.publisher == "FHIR (Example)"
    assert (
        inst.relatedArtifact[0].resource == "http://hl7.org/fhir/NamingSystem/example"
    )
    assert inst.relatedArtifact[0].type == "derived-from"
    assert (
        inst.relatedArtifact[1].resource
        == "http://hl7.org/fhir/NamingSystem/example-metadata|20210701"
    )
    assert inst.relatedArtifact[1].type == "predecessor"
    assert inst.reviewer[0].name == "Society for Creative NamingSystem Review"
    assert inst.reviewer[0].telecom[0].system == "url"
    assert inst.reviewer[0].telecom[0].value == "http://example.org/scnr"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.title == "Metadata Example"
    assert inst.topic[0].coding[0].code == "treatment"
    assert inst.topic[0].coding[0].display == "Treatment"
    assert (
        inst.topic[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://terminology.hl7.org/CodeSystem/definition-topic"}
        ).valueUri
    )
    assert inst.uniqueId[0].type == "oid"
    assert inst.uniqueId[0].value == "1.2.3.4.5.6.7"
    assert inst.uniqueId[1].preferred is True
    assert inst.uniqueId[1].type == "uri"
    assert inst.uniqueId[1].value == "http://example.com/identifiers"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/example-metadata-2"}
        ).valueUri
    )
    assert inst.version == "20220721"


def test_namingsystem_3(base_settings):
    """No. 3 tests collection for NamingSystem.
    Test File: namingsystem-example-metadata-2.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "namingsystem-example-metadata-2.json"
    )
    inst = namingsystem.NamingSystem.model_validate_json(filename.read_bytes())
    assert "NamingSystem" == inst.get_resource_type()

    impl_namingsystem_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "NamingSystem" == data["resourceType"]

    inst2 = namingsystem.NamingSystem(**data)
    impl_namingsystem_3(inst2)


def impl_namingsystem_4(inst):
    assert inst.contact[0].name == "FHIR project team"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2014-12-13"}
        ).valueDateTime
    )
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.22.1"
    assert inst.kind == "codesystem"
    assert inst.name == "SNOMEDCT"
    assert inst.publisher == "HL7 International on behalf of IHTSDO"
    assert inst.responsible == "IHTSDO & affiliates"
    assert inst.status == "active"
    assert inst.text.status == "generated"
    assert inst.title == "SNOMED CT"
    assert inst.uniqueId[0].type == "oid"
    assert inst.uniqueId[0].value == "2.16.840.1.113883.6.96"
    assert inst.uniqueId[1].preferred is True
    assert inst.uniqueId[1].type == "uri"
    assert inst.uniqueId[1].value == "http://snomed.info/sct"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/NamingSystem/example"}
        ).valueUri
    )


def test_namingsystem_4(base_settings):
    """No. 4 tests collection for NamingSystem.
    Test File: namingsystem-example.json
    """
    filename = base_settings["unittest_data_dir"] / "namingsystem-example.json"
    inst = namingsystem.NamingSystem.model_validate_json(filename.read_bytes())
    assert "NamingSystem" == inst.get_resource_type()

    impl_namingsystem_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "NamingSystem" == data["resourceType"]

    inst2 = namingsystem.NamingSystem(**data)
    impl_namingsystem_4(inst2)
