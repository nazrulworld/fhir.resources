# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from .. import valueset
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_valueset_1(inst):
    assert (
        inst.compose.include[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/message-reasons-encounter"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "Example Message Reasons. These are the set of codes that "
        "might be used an updating an encounter using admin-update."
    )
    assert inst.experimental is True
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 1
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "inm"
    assert inst.id == "message-reason-encounter"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.365"
    assert inst.immutable is True
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablevalueset"}
        ).valueUri
    )
    assert inst.name == "Example Message Reason Codes"
    assert inst.publisher == "FHIR Project"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/message-reason-encounter"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_valueset_1(base_settings):
    """No. 1 tests collection for ValueSet.
    Test File: valueset-valueset-message-reason-encounter(message-reason-encounter).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-valueset-message-reason-encounter(message-reason-encounter).json"
    )
    inst = valueset.ValueSet.model_validate_json(filename.read_bytes())
    assert "ValueSet" == inst.get_resource_type()

    impl_valueset_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_1(inst2)


def impl_valueset_2(inst):
    assert (
        inst.compose.include[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/implant-status"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "A set codes that define the functional status of an " "implanted device."
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 0
    assert inst.id == "implant-status"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.865"
    assert inst.immutable is True
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablevalueset"}
        ).valueUri
    )
    assert inst.name == "Implant Status"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/implant-status"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_valueset_2(base_settings):
    """No. 2 tests collection for ValueSet.
    Test File: valueset-valueset-implant-status(implant-status).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-valueset-implant-status(implant-status).json"
    )
    inst = valueset.ValueSet.model_validate_json(filename.read_bytes())
    assert "ValueSet" == inst.get_resource_type()

    impl_valueset_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_2(inst2)


def impl_valueset_3(inst):
    assert (
        inst.compose.include[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/action-selection-behavior"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == "Defines selection behavior of a group"
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 2
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "cds"
    assert inst.id == "action-selection-behavior"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.784"
    assert inst.immutable is True
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablevalueset"}
        ).valueUri
    )
    assert inst.name == "ActionSelectionBehavior"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/action-selection-behavior"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_valueset_3(base_settings):
    """No. 3 tests collection for ValueSet.
    Test File: valueset-valueset-action-selection-behavior(action-selection-behavior).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-valueset-action-selection-behavior(action-selection-behavior).json"
    )
    inst = valueset.ValueSet.model_validate_json(filename.read_bytes())
    assert "ValueSet" == inst.get_resource_type()

    impl_valueset_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_3(inst2)


def impl_valueset_4(inst):
    assert (
        inst.compose.include[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/search-param-type"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == "Data types allowed to be used for search parameters."
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 4
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "fhir"
    assert inst.id == "search-param-type"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.11"
    assert inst.immutable is True
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablevalueset"}
        ).valueUri
    )
    assert inst.name == "SearchParamType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/search-param-type"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_valueset_4(base_settings):
    """No. 4 tests collection for ValueSet.
    Test File: valueset-valueset-search-param-type(search-param-type).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-valueset-search-param-type(search-param-type).json"
    )
    inst = valueset.ValueSet.model_validate_json(filename.read_bytes())
    assert "ValueSet" == inst.get_resource_type()

    impl_valueset_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_4(inst2)


def impl_valueset_5(inst):
    assert (
        inst.compose.include[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://loinc.org"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.copyright == (
        "This content from LOINC® is copyright © 1995 Regenstrief "
        "Institute, Inc. and the LOINC Committee, and available at no"
        " cost under the license at http://loinc.org/terms-of-use."
    )
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "This value set includes all the LOINC codes which relate to "
        "Diagnostic Observations."
    )
    assert inst.experimental is True
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 3
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "oo"
    assert inst.id == "report-codes"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.228"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablevalueset"}
        ).valueUri
    )
    assert inst.name == "LOINC Diagnostic Report Codes"
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/report-codes"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_valueset_5(base_settings):
    """No. 5 tests collection for ValueSet.
    Test File: valueset-valueset-report-codes(report-codes).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-valueset-report-codes(report-codes).json"
    )
    inst = valueset.ValueSet.model_validate_json(filename.read_bytes())
    assert "ValueSet" == inst.get_resource_type()

    impl_valueset_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_5(inst2)


def impl_valueset_6(inst):
    assert (
        inst.compose.include[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/observation-relationshiptypes"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == "Codes specifying how two observations are related."
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 5
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "oo"
    assert inst.id == "observation-relationshiptypes"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.389"
    assert inst.immutable is True
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablevalueset"}
        ).valueUri
    )
    assert inst.name == "ObservationRelationshipType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/observation-relationshiptypes"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_valueset_6(base_settings):
    """No. 6 tests collection for ValueSet.
    Test File: valueset-valueset-observation-relationshiptypes(observation-relationshiptypes).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-valueset-observation-relationshiptypes(observation-relationshiptypes).json"
    )
    inst = valueset.ValueSet.model_validate_json(filename.read_bytes())
    assert "ValueSet" == inst.get_resource_type()

    impl_valueset_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_6(inst2)


def impl_valueset_7(inst):
    assert (
        inst.compose.include[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/bundle-type"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "Indicates the purpose of a bundle - how it was intended to " "be used."
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 5
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "fhir"
    assert inst.id == "bundle-type"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.612"
    assert inst.immutable is True
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablevalueset"}
        ).valueUri
    )
    assert inst.name == "BundleType"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/bundle-type"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_valueset_7(base_settings):
    """No. 7 tests collection for ValueSet.
    Test File: valueset-valueset-bundle-type(bundle-type).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-valueset-bundle-type(bundle-type).json"
    )
    inst = valueset.ValueSet.model_validate_json(filename.read_bytes())
    assert "ValueSet" == inst.get_resource_type()

    impl_valueset_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_7(inst2)


def impl_valueset_8(inst):
    assert inst.compose.include[0].filter[0].op == "is-a"
    assert inst.compose.include[0].filter[0].property == "concept"
    assert inst.compose.include[0].filter[0].value == "_ActAccountCode"
    assert (
        inst.compose.include[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/v3/ActCode"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "This examples value set defines the set of codes that can be"
        " used to represent the type of an account."
    )
    assert inst.experimental is True
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 1
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "pa"
    assert inst.id == "account-type"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.716"
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablevalueset"}
        ).valueUri
    )
    assert inst.name == "Account Types"
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/account-type"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_valueset_8(base_settings):
    """No. 8 tests collection for ValueSet.
    Test File: valueset-valueset-account-type(account-type).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-valueset-account-type(account-type).json"
    )
    inst = valueset.ValueSet.model_validate_json(filename.read_bytes())
    assert "ValueSet" == inst.get_resource_type()

    impl_valueset_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_8(inst2)


def impl_valueset_9(inst):
    assert (
        inst.compose.include[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/testscript-operation-codes"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "This value set defines a set of codes that are used to "
        "indicate the supported operations of a testing engine or "
        "tool."
    )
    assert inst.experimental is True
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 2
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "fhir"
    assert inst.id == "testscript-operation-codes"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.690"
    assert inst.immutable is True
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablevalueset"}
        ).valueUri
    )
    assert inst.name == "TestScriptOperationCode"
    assert inst.publisher == "FHIR Project team"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/testscript-operation-codes"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_valueset_9(base_settings):
    """No. 9 tests collection for ValueSet.
    Test File: valueset-valueset-testscript-operation-codes(testscript-operation-codes).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-valueset-testscript-operation-codes(testscript-operation-codes).json"
    )
    inst = valueset.ValueSet.model_validate_json(filename.read_bytes())
    assert "ValueSet" == inst.get_resource_type()

    impl_valueset_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_9(inst2)


def impl_valueset_10(inst):
    assert (
        inst.compose.include[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://www.hl7.org/fhir/contractsignertypecodes"}
        ).valueUri
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert (
        inst.description == "This value set includes sample Contract Signer Type codes."
    )
    assert inst.experimental is True
    assert inst.extensible is True
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            }
        ).valueUri
    )
    assert inst.extension[0].valueString == "Informative"
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[1].valueInteger == 1
    assert (
        inst.extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            }
        ).valueUri
    )
    assert inst.extension[2].valueCode == "fm"
    assert inst.id == "contract-signer-type"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.identifier[0].value == "urn:oid:2.16.840.1.113883.4.642.3.725"
    assert inst.immutable is True
    assert (
        inst.meta.lastUpdated
        == ExternalValidatorModel.model_validate(
            {"valueInstant": "2019-10-24T11:53:00+11:00"}
        ).valueInstant
    )
    assert (
        inst.meta.profile[0]
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/StructureDefinition/shareablevalueset"}
        ).valueUri
    )
    assert inst.name == "Contract Signer Type Codes"
    assert inst.publisher == "Financial Management"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/ValueSet/contract-signer-type"}
        ).valueUri
    )
    assert inst.version == "3.0.2"


def test_valueset_10(base_settings):
    """No. 10 tests collection for ValueSet.
    Test File: valueset-valueset-contract-signer-type(contract-signer-type).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "valueset-valueset-contract-signer-type(contract-signer-type).json"
    )
    inst = valueset.ValueSet.model_validate_json(filename.read_bytes())
    assert "ValueSet" == inst.get_resource_type()

    impl_valueset_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "ValueSet" == data["resourceType"]

    inst2 = valueset.ValueSet(**data)
    impl_valueset_10(inst2)
