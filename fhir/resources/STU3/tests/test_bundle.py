# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Bundle
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import bundle


def impl_bundle_1(inst):
    assert inst.entry[0].fullUrl == "urn:uuid:d9d296d8-5afd-42e1-a0ce-3344e0e003ed"
    assert inst.entry[0].resource.id == "caf609cf-c3a7-4be3-a3aa-356b9bb69d4f"
    assert inst.entry[1].fullUrl == "urn:uuid:03f9aa7d-b395-47b9-84e0-053678b6e4e3"
    assert inst.entry[1].resource.id == "03f9aa7d-b395-47b9-84e0-053678b6e4e3"
    assert inst.entry[2].fullUrl == "http://acme.com/ehr/fhir/Patient/pat1"
    assert inst.entry[2].resource.id == "pat1"
    assert inst.entry[3].fullUrl == "http://acme.com/ehr/fhir/Patient/pat12"
    assert inst.entry[3].resource.id == "pat2"
    assert inst.id == "3a0707d3-549e-4467-b8b8-5a2ab3800efe"
    assert inst.type == "message"


def test_bundle_1(base_settings):
    """No. 1 tests collection for Bundle.
    Test File: message-response-link.json
    """
    filename = base_settings["unittest_data_dir"] / "message-response-link.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_1(inst2)


def impl_bundle_2(inst):
    assert inst.entry[0].fullUrl == "urn:uuid:3fdc72f4-a11d-4a9d-9260-a9f745779e1d"
    assert inst.entry[0].request.method == "POST"
    assert inst.entry[0].request.url == "DocumentReference"
    assert inst.entry[0].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2013-07-01T13:11:33Z"
    )
    assert inst.entry[1].fullUrl == "http://localhost:9556/svc/fhir/Patient/a2"
    assert (
        inst.entry[1].request.ifNoneExist
        == "Patient?identifier=http://acme.org/xds/patients!89765a87b"
    )
    assert inst.entry[1].request.method == "POST"
    assert inst.entry[1].request.url == "Patient"
    assert inst.entry[1].resource.id == "a2"
    assert inst.entry[1].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2013-07-01T13:11:33Z"
    )
    assert inst.entry[2].fullUrl == "http://localhost:9556/svc/fhir/Practitioner/a3"
    assert inst.entry[2].request.method == "POST"
    assert inst.entry[2].request.url == "Practitioner"
    assert inst.entry[2].resource.id == "a3"
    assert inst.entry[2].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2013-07-01T13:11:33Z"
    )
    assert inst.entry[3].fullUrl == "http://localhost:9556/svc/fhir/Practitioner/a4"
    assert inst.entry[3].request.method == "POST"
    assert inst.entry[3].request.url == "Practitioner"
    assert inst.entry[3].resource.id == "a4"
    assert inst.entry[3].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2013-07-01T13:11:33Z"
    )
    assert inst.entry[4].fullUrl == (
        "http://localhost:9556/svc/fhir/Binary/1e404af3-077f-4bee-b7a" "6-a9be97e1ce32"
    )
    assert inst.entry[4].request.method == "POST"
    assert inst.entry[4].request.url == "Binary"
    assert inst.entry[4].resource.id == "1e404af3-077f-4bee-b7a6-a9be97e1ce32"
    assert inst.entry[4].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2013-07-01T13:11:33Z"
    )
    assert inst.id == "xds"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2013-07-01T13:11:33Z")
    assert inst.type == "transaction"


def test_bundle_2(base_settings):
    """No. 2 tests collection for Bundle.
    Test File: xds-example.json
    """
    filename = base_settings["unittest_data_dir"] / "xds-example.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_2(inst2)


def impl_bundle_3(inst):
    assert (
        inst.entry[0].fullUrl
        == "http://hl7.org/fhir/SearchParameter/DomainResource-text"
    )
    assert inst.entry[0].resource.id == "DomainResource-text"
    assert (
        inst.entry[1].fullUrl == "http://hl7.org/fhir/SearchParameter/Resource-content"
    )
    assert inst.entry[1].resource.id == "Resource-content"
    assert inst.entry[2].fullUrl == "http://hl7.org/fhir/SearchParameter/Resource-id"
    assert inst.entry[2].resource.id == "Resource-id"
    assert (
        inst.entry[3].fullUrl
        == "http://hl7.org/fhir/SearchParameter/Resource-lastUpdated"
    )
    assert inst.entry[3].resource.id == "Resource-lastUpdated"
    assert (
        inst.entry[4].fullUrl == "http://hl7.org/fhir/SearchParameter/Resource-profile"
    )
    assert inst.entry[4].resource.id == "Resource-profile"
    assert inst.entry[5].fullUrl == "http://hl7.org/fhir/SearchParameter/Resource-query"
    assert inst.entry[5].resource.id == "Resource-query"
    assert (
        inst.entry[6].fullUrl == "http://hl7.org/fhir/SearchParameter/Resource-security"
    )
    assert inst.entry[6].resource.id == "Resource-security"
    assert inst.entry[7].fullUrl == "http://hl7.org/fhir/SearchParameter/Resource-tag"
    assert inst.entry[7].resource.id == "Resource-tag"
    assert (
        inst.entry[8].fullUrl == "http://hl7.org/fhir/SearchParameter/Account-balance"
    )
    assert inst.entry[8].resource.id == "Account-balance"
    assert (
        inst.entry[9].fullUrl
        == "http://hl7.org/fhir/SearchParameter/Account-identifier"
    )
    assert inst.entry[9].resource.id == "Account-identifier"
    assert inst.id == "searchParams"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.type == "collection"


def test_bundle_3(base_settings):
    """No. 3 tests collection for Bundle.
    Test File: search-parameters.json
    """
    filename = base_settings["unittest_data_dir"] / "search-parameters.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_3(inst2)


def impl_bundle_4(inst):
    assert inst.entry[0].fullUrl == "urn:uuid:267b18ce-3d37-4581-9baa-6fada338038b"
    assert inst.entry[0].resource.id == "efdd254b-0e09-4164-883e-35cf3871715f"
    assert inst.entry[1].fullUrl == "http://acme.com/ehr/fhir/Patient/pat1"
    assert inst.entry[1].resource.id == "pat1"
    assert inst.entry[2].fullUrl == "http://acme.com/ehr/fhir/Patient/pat12"
    assert inst.entry[2].resource.id == "pat2"
    assert inst.id == "10bb101f-a121-4264-a920-67be9cb82c74"
    assert inst.type == "message"


def test_bundle_4(base_settings):
    """No. 4 tests collection for Bundle.
    Test File: message-request-link.json
    """
    filename = base_settings["unittest_data_dir"] / "message-request-link.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_4(inst2)


def impl_bundle_5(inst):
    assert inst.entry[0].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-sct"
    assert inst.entry[0].resource.id == "tx-sct"
    assert inst.entry[1].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-rxnorm"
    assert inst.entry[1].resource.id == "tx-rxnorm"
    assert inst.entry[2].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-loinc"
    assert inst.entry[2].resource.id == "tx-loinc"
    assert inst.entry[3].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-ucum"
    assert inst.entry[3].resource.id == "tx-ucum"
    assert inst.entry[4].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-nci"
    assert inst.entry[4].resource.id == "tx-nci"
    assert inst.entry[5].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-cpt"
    assert inst.entry[5].resource.id == "tx-cpt"
    assert inst.entry[6].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-ndf-rt"
    assert inst.entry[6].resource.id == "tx-ndf-rt"
    assert inst.entry[7].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-unii"
    assert inst.entry[7].resource.id == "tx-unii"
    assert inst.entry[8].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-ndc"
    assert inst.entry[8].resource.id == "tx-ndc"
    assert inst.entry[9].fullUrl == "http://hl7.org/fhir/NamingSystem/tx-cvx"
    assert inst.entry[9].resource.id == "tx-cvx"
    assert inst.id == "terminologies"
    assert inst.type == "collection"


def test_bundle_5(base_settings):
    """No. 5 tests collection for Bundle.
    Test File: namingsystem-terminologies.json
    """
    filename = base_settings["unittest_data_dir"] / "namingsystem-terminologies.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_5(inst2)


def impl_bundle_6(inst):
    assert (
        inst.entry[0].fullUrl
        == "http://hl7.org/fhir/StructureDefinition/valueset-history"
    )
    assert inst.entry[0].resource.id == "valueset-history"
    assert inst.entry[1].fullUrl == "http://hl7.org/fhir/StructureDefinition/birthPlace"
    assert inst.entry[1].resource.id == "birthPlace"
    assert (
        inst.entry[2].fullUrl == "http://hl7.org/fhir/StructureDefinition/valueset-map"
    )
    assert inst.entry[2].resource.id == "valueset-map"
    assert inst.entry[3].fullUrl == (
        "http://hl7.org/fhir/StructureDefinition/observation-time-" "offset"
    )
    assert inst.entry[3].resource.id == "observation-time-offset"
    assert inst.entry[4].fullUrl == (
        "http://hl7.org/fhir/StructureDefinition/observation-" "geneticsInterpretation"
    )
    assert inst.entry[4].resource.id == "observation-geneticsInterpretation"
    assert inst.entry[5].fullUrl == (
        "http://hl7.org/fhir/StructureDefinition/11179-de-" "administrative-status"
    )
    assert inst.entry[5].resource.id == "11179-de-administrative-status"
    assert inst.entry[6].fullUrl == (
        "http://hl7.org/fhir/StructureDefinition/patient-" "cadavericDonor"
    )
    assert inst.entry[6].resource.id == "patient-cadavericDonor"
    assert (
        inst.entry[7].fullUrl
        == "http://hl7.org/fhir/StructureDefinition/openEHR-management"
    )
    assert inst.entry[7].resource.id == "openEHR-management"
    assert (
        inst.entry[8].fullUrl
        == "http://hl7.org/fhir/StructureDefinition/valueset-definition"
    )
    assert inst.entry[8].resource.id == "valueset-definition"
    assert inst.entry[9].fullUrl == (
        "http://hl7.org/fhir/StructureDefinition/procedurerequest-" "reasonRejected"
    )
    assert inst.entry[9].resource.id == "procedurerequest-reasonRejected"
    assert inst.id == "extensions"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.type == "collection"


def test_bundle_6(base_settings):
    """No. 6 tests collection for Bundle.
    Test File: extension-definitions.json
    """
    filename = base_settings["unittest_data_dir"] / "extension-definitions.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_6(inst2)


def impl_bundle_7(inst):
    assert inst.entry[0].fullUrl == (
        "http://hl7.org/fhir/ConceptMap/cm-observation-" "relationshiptypes-v3"
    )
    assert inst.entry[0].resource.id == "cm-observation-relationshiptypes-v3"
    assert inst.entry[1].fullUrl == "http://hl7.org/fhir/ConceptMap/cm-address-use-v3"
    assert inst.entry[1].resource.id == "cm-address-use-v3"
    assert (
        inst.entry[2].fullUrl
        == "http://hl7.org/fhir/ConceptMap/cm-contact-point-use-v3"
    )
    assert inst.entry[2].resource.id == "cm-contact-point-use-v3"
    assert (
        inst.entry[3].fullUrl
        == "http://hl7.org/fhir/ConceptMap/cm-contact-point-use-v2"
    )
    assert inst.entry[3].resource.id == "cm-contact-point-use-v2"
    assert (
        inst.entry[4].fullUrl
        == "http://hl7.org/fhir/ConceptMap/cm-administrative-gender-v2"
    )
    assert inst.entry[4].resource.id == "cm-administrative-gender-v2"
    assert inst.entry[5].fullUrl == "http://hl7.org/fhir/ConceptMap/cm-address-type-v3"
    assert inst.entry[5].resource.id == "cm-address-type-v3"
    assert inst.entry[6].fullUrl == (
        "http://hl7.org/fhir/ConceptMap/cm-medication-request-" "status-v3"
    )
    assert inst.entry[6].resource.id == "cm-medication-request-status-v3"
    assert (
        inst.entry[7].fullUrl
        == "http://hl7.org/fhir/ConceptMap/cm-administrative-gender-v3"
    )
    assert inst.entry[7].resource.id == "cm-administrative-gender-v3"
    assert (
        inst.entry[8].fullUrl
        == "http://hl7.org/fhir/ConceptMap/cm-data-absent-reason-v3"
    )
    assert inst.entry[8].resource.id == "cm-data-absent-reason-v3"
    assert inst.entry[9].fullUrl == "http://hl7.org/fhir/ConceptMap/cm-name-use-v2"
    assert inst.entry[9].resource.id == "cm-name-use-v2"
    assert inst.id == "conceptmaps"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.type == "collection"


def test_bundle_7(base_settings):
    """No. 7 tests collection for Bundle.
    Test File: conceptmaps.json
    """
    filename = base_settings["unittest_data_dir"] / "conceptmaps.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_7(inst2)


def impl_bundle_8(inst):
    assert inst.entry[0].fullUrl == "http://hl7.org/fhir/StructureDefinition/Element"
    assert inst.entry[0].resource.id == "Element"
    assert inst.entry[0].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.entry[1].fullUrl
        == "http://hl7.org/fhir/StructureDefinition/BackboneElement"
    )
    assert inst.entry[1].resource.id == "BackboneElement"
    assert inst.entry[1].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.entry[2].fullUrl == "http://hl7.org/fhir/StructureDefinition/base64Binary"
    )
    assert inst.entry[2].resource.id == "base64Binary"
    assert inst.entry[2].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.entry[3].fullUrl == "http://hl7.org/fhir/StructureDefinition/boolean"
    assert inst.entry[3].resource.id == "boolean"
    assert inst.entry[3].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.entry[4].fullUrl == "http://hl7.org/fhir/StructureDefinition/code"
    assert inst.entry[4].resource.id == "code"
    assert inst.entry[4].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.entry[5].fullUrl == "http://hl7.org/fhir/StructureDefinition/date"
    assert inst.entry[5].resource.id == "date"
    assert inst.entry[5].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.entry[6].fullUrl == "http://hl7.org/fhir/StructureDefinition/dateTime"
    assert inst.entry[6].resource.id == "dateTime"
    assert inst.entry[6].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.entry[7].fullUrl == "http://hl7.org/fhir/StructureDefinition/decimal"
    assert inst.entry[7].resource.id == "decimal"
    assert inst.entry[7].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.entry[8].fullUrl == "http://hl7.org/fhir/StructureDefinition/id"
    assert inst.entry[8].resource.id == "id"
    assert inst.entry[8].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.entry[9].fullUrl == "http://hl7.org/fhir/StructureDefinition/instant"
    assert inst.entry[9].resource.id == "instant"
    assert inst.entry[9].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.id == "types"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.type == "collection"


def test_bundle_8(base_settings):
    """No. 8 tests collection for Bundle.
    Test File: profiles-types.json
    """
    filename = base_settings["unittest_data_dir"] / "profiles-types.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_8(inst2)


def impl_bundle_9(inst):
    assert inst.entry[0].fullUrl == "http://hl7.org/fhir/ValueSet/v3-CalendarType"
    assert inst.entry[0].resource.id == "v3-CalendarType"
    assert inst.entry[0].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2016-11-11T00:00:00.000+11:00"
    )
    assert (
        inst.entry[0].resource.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert (
        inst.entry[1].fullUrl
        == "http://hl7.org/fhir/ValueSet/v3-ManagedParticipationStatus"
    )
    assert inst.entry[1].resource.id == "v3-ManagedParticipationStatus"
    assert inst.entry[1].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2016-11-11T00:00:00.000+11:00"
    )
    assert (
        inst.entry[1].resource.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert (
        inst.entry[2].fullUrl == "http://hl7.org/fhir/ValueSet/v3-ActConsentDirective"
    )
    assert inst.entry[2].resource.id == "v3-ActConsentDirective"
    assert inst.entry[2].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.entry[2].resource.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert (
        inst.entry[3].fullUrl
        == "http://hl7.org/fhir/ValueSet/v3-InformationSensitivityPolicy"
    )
    assert inst.entry[3].resource.id == "v3-InformationSensitivityPolicy"
    assert inst.entry[3].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.entry[3].resource.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.entry[4].fullUrl == "http://hl7.org/fhir/ValueSet/v3-RoleClass"
    assert inst.entry[4].resource.id == "v3-RoleClass"
    assert inst.entry[4].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2016-11-11T00:00:00.000+11:00"
    )
    assert (
        inst.entry[4].resource.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.entry[5].fullUrl == (
        "http://hl7.org/fhir/ValueSet/v3-ConfidentialityClassificatio" "n"
    )
    assert inst.entry[5].resource.id == "v3-ConfidentialityClassification"
    assert inst.entry[5].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.entry[5].resource.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.entry[6].fullUrl == (
        "http://hl7.org/fhir/ValueSet/v3-ServiceDeliveryLocationRoleT" "ype"
    )
    assert inst.entry[6].resource.id == "v3-ServiceDeliveryLocationRoleType"
    assert inst.entry[6].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.entry[6].resource.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.entry[7].fullUrl == "http://hl7.org/fhir/ValueSet/v3-QueryResponse"
    assert inst.entry[7].resource.id == "v3-QueryResponse"
    assert inst.entry[7].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2016-11-11T00:00:00.000+11:00"
    )
    assert (
        inst.entry[7].resource.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.entry[8].fullUrl == "http://hl7.org/fhir/ValueSet/v3-SecurityPolicy"
    assert inst.entry[8].resource.id == "v3-SecurityPolicy"
    assert inst.entry[8].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert (
        inst.entry[8].resource.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert (
        inst.entry[9].fullUrl
        == "http://hl7.org/fhir/ValueSet/v3-TableCellHorizontalAlign"
    )
    assert inst.entry[9].resource.id == "v3-TableCellHorizontalAlign"
    assert inst.entry[9].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2016-11-11T00:00:00.000+11:00"
    )
    assert (
        inst.entry[9].resource.meta.profile[0]
        == "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
    )
    assert inst.id == "v3-valuesets"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate(
        "2017-04-19T07:44:43.294+10:00"
    )
    assert inst.type == "collection"


def test_bundle_9(base_settings):
    """No. 9 tests collection for Bundle.
    Test File: v3-codesystems.json
    """
    filename = base_settings["unittest_data_dir"] / "v3-codesystems.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_9(inst2)


def impl_bundle_10(inst):
    assert inst.entry[0].fullUrl == "http://hl7.org/fhir/Practitioner/1"
    assert inst.entry[0].resource.id == "1"
    assert inst.entry[1].fullUrl == "http://hl7.org/fhir/Practitioner/13"
    assert inst.entry[1].resource.id == "13"
    assert inst.entry[1].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2012-05-29T23:45:32Z"
    )
    assert inst.entry[2].fullUrl == "http://hl7.org/fhir/Practitioner/14"
    assert inst.entry[2].resource.id == "14"
    assert inst.entry[2].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2012-05-29T23:45:32Z"
    )
    assert inst.entry[3].fullUrl == "http://hl7.org/fhir/Practitioner/15"
    assert inst.entry[3].resource.id == "15"
    assert inst.entry[3].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2012-05-29T23:45:32Z"
    )
    assert inst.entry[4].fullUrl == "http://hl7.org/fhir/Practitioner/16"
    assert inst.entry[4].resource.id == "16"
    assert inst.entry[4].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2012-05-29T23:45:32Z"
    )
    assert inst.entry[5].fullUrl == "http://hl7.org/fhir/Practitioner/17"
    assert inst.entry[5].resource.id == "17"
    assert inst.entry[5].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2012-05-29T23:45:32Z"
    )
    assert inst.entry[6].fullUrl == "http://hl7.org/fhir/Practitioner/18"
    assert inst.entry[6].resource.id == "18"
    assert inst.entry[6].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2012-05-29T23:45:32Z"
    )
    assert inst.entry[7].fullUrl == "http://hl7.org/fhir/Practitioner/19"
    assert inst.entry[7].resource.id == "19"
    assert inst.entry[7].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2012-05-29T23:45:32Z"
    )
    assert inst.entry[8].fullUrl == "http://hl7.org/fhir/Practitioner/20"
    assert inst.entry[8].resource.id == "20"
    assert inst.entry[8].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2012-05-29T23:45:32Z"
    )
    assert inst.entry[9].fullUrl == "http://hl7.org/fhir/Practitioner/21"
    assert inst.entry[9].resource.id == "21"
    assert inst.entry[9].resource.meta.lastUpdated == fhirtypes.Instant.validate(
        "2012-05-29T23:45:32Z"
    )
    assert inst.id == "3ad0687e-f477-468c-afd5-fcc2bf897809"
    assert inst.meta.lastUpdated == fhirtypes.Instant.validate("2012-05-29T23:45:32Z")
    assert inst.type == "collection"


def test_bundle_10(base_settings):
    """No. 10 tests collection for Bundle.
    Test File: practitioner-examples-general.json
    """
    filename = base_settings["unittest_data_dir"] / "practitioner-examples-general.json"
    inst = bundle.Bundle.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Bundle" == inst.resource_type

    impl_bundle_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Bundle" == data["resourceType"]

    inst2 = bundle.Bundle(**data)
    impl_bundle_10(inst2)
