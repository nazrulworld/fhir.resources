# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from .. import capabilitystatement
from .conftest import ExternalValidatorModel


def impl_capabilitystatement_1(inst):
    assert inst.acceptUnknown == "no"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is True
    assert inst.fhirVersion == "3.0.2"
    assert inst.format[0] == "xml"
    assert inst.format[1] == "json"
    assert inst.id == "base2"
    assert inst.kind == "capability"
    assert inst.name == "Base FHIR Capability Statement (Empty)"
    assert inst.publisher == "FHIR Project Team"
    assert inst.rest[0].documentation == "An empty Capability Statement"
    assert inst.rest[0].mode == "server"
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert (
        inst.rest[0].resource[0].interaction[0].documentation
        == "Read CapabilityStatement Resource"
    )
    assert inst.rest[0].resource[0].type == "CapabilityStatement"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.description == (
        "This is the Capability Statement to declare that the server "
        "supports SMART-on-FHIR. See the SMART-on-FHIR docs for the "
        "extension that would go with such a server"
    )
    assert inst.rest[0].security.service[0].coding[0].code == "SMART-on-FHIR"
    assert inst.rest[0].security.service[0].coding[0].display == "SMART-on-FHIR"
    assert (
        inst.rest[0].security.service[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/restful-security-service"}
        ).valueUri
    )
    assert inst.rest[0].security.service[0].text == "See http://docs.smarthealthit.org/"
    assert inst.software.name == "Insert your softwware name here..."
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CapabilityStatement/base2"}
        ).valueUri
    )
    assert inst.version == "3.0.2-11200"


def test_capabilitystatement_1(base_settings):
    """No. 1 tests collection for CapabilityStatement.
    Test File: capabilitystatement-capabilitystatement-base2(base2).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "capabilitystatement-capabilitystatement-base2(base2).json"
    )
    inst = capabilitystatement.CapabilityStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "CapabilityStatement" == inst.get_resource_type()

    impl_capabilitystatement_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_1(inst2)


def impl_capabilitystatement_2(inst):
    assert inst.acceptUnknown == "both"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is True
    assert inst.fhirVersion == "3.0.2"
    assert inst.format[0] == "xml"
    assert inst.format[1] == "json"
    assert inst.id == "base"
    assert inst.kind == "capability"
    assert inst.name == "Base FHIR Capability Statement (Full)"
    assert inst.publisher == "FHIR Project Team"
    assert inst.rest[0].documentation == "All the functionality defined in FHIR"
    assert inst.rest[0].interaction[0].code == "transaction"
    assert inst.rest[0].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].interaction[1].code == "batch"
    assert inst.rest[0].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].interaction[2].code == "history-system"
    assert inst.rest[0].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].interaction[3].code == "search-system"
    assert inst.rest[0].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].mode == "server"
    assert (
        inst.rest[0].operation[0].definition.reference
        == "http://hl7.org/fhir/OperationDefinition/resource-validate"
    )
    assert inst.rest[0].operation[0].name == "validate"
    assert (
        inst.rest[0].operation[1].definition.reference
        == "http://hl7.org/fhir/OperationDefinition/resource-meta"
    )
    assert inst.rest[0].operation[1].name == "meta"
    assert (
        inst.rest[0].operation[2].definition.reference
        == "http://hl7.org/fhir/OperationDefinition/resource-meta-add"
    )
    assert inst.rest[0].operation[2].name == "meta-add"
    assert (
        inst.rest[0].operation[3].definition.reference
        == "http://hl7.org/fhir/OperationDefinition/resource-meta-delete"
    )
    assert inst.rest[0].operation[3].name == "meta-delete"
    assert inst.rest[0].operation[4].definition.reference == (
        "http://hl7.org/fhir/OperationDefinition/activitydefinition-" "apply"
    )
    assert inst.rest[0].operation[4].name == "apply"
    assert inst.rest[0].operation[5].definition.reference == (
        "http://hl7.org/fhir/OperationDefinition/activitydefinition-"
        "data-requirements"
    )
    assert inst.rest[0].operation[5].name == "data-requirements"
    assert inst.rest[0].operation[6].definition.reference == (
        "http://hl7.org/fhir/OperationDefinition/capabilitystatement-" "subset"
    )
    assert inst.rest[0].operation[6].name == "subset"
    assert inst.rest[0].operation[7].definition.reference == (
        "http://hl7.org/fhir/OperationDefinition/capabilitystatement-" "implements"
    )
    assert inst.rest[0].operation[7].name == "implements"
    assert inst.rest[0].operation[8].definition.reference == (
        "http://hl7.org/fhir/OperationDefinition/capabilitystatement-" "conforms"
    )
    assert inst.rest[0].operation[8].name == "conforms"
    assert (
        inst.rest[0].operation[9].definition.reference
        == "http://hl7.org/fhir/OperationDefinition/codesystem-lookup"
    )
    assert inst.rest[0].operation[9].name == "lookup"
    assert inst.rest[0].resource[0].conditionalCreate is True
    assert inst.rest[0].resource[0].conditionalDelete == "multiple"
    assert inst.rest[0].resource[0].conditionalUpdate is True
    assert inst.rest[0].resource[0].interaction[0].code == "read"
    assert inst.rest[0].resource[0].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[1].code == "vread"
    assert inst.rest[0].resource[0].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[2].code == "update"
    assert inst.rest[0].resource[0].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[3].code == "delete"
    assert inst.rest[0].resource[0].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[0].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[5].code == "history-type"
    assert inst.rest[0].resource[0].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[6].code == "create"
    assert inst.rest[0].resource[0].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[0].interaction[7].code == "search-type"
    assert inst.rest[0].resource[0].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[0].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Account"
    )
    assert inst.rest[0].resource[0].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[0].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[0].searchInclude[0] == "Account.owner"
    assert inst.rest[0].resource[0].searchInclude[1] == "Account.subject"
    assert inst.rest[0].resource[0].searchInclude[2] == "Account.patient"
    assert (
        inst.rest[0].resource[0].searchParam[0].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Account-owner"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[0].searchParam[0].documentation == "Who is responsible?"
    )
    assert inst.rest[0].resource[0].searchParam[0].name == "owner"
    assert inst.rest[0].resource[0].searchParam[0].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[1].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Account-identifier"}
        ).valueUri
    )
    assert inst.rest[0].resource[0].searchParam[1].documentation == "Account number"
    assert inst.rest[0].resource[0].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[0].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[2].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Account-period"}
        ).valueUri
    )
    assert inst.rest[0].resource[0].searchParam[2].documentation == "Transaction window"
    assert inst.rest[0].resource[0].searchParam[2].name == "period"
    assert inst.rest[0].resource[0].searchParam[2].type == "date"
    assert (
        inst.rest[0].resource[0].searchParam[3].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Account-balance"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[0].searchParam[3].documentation
        == "How much is in account?"
    )
    assert inst.rest[0].resource[0].searchParam[3].name == "balance"
    assert inst.rest[0].resource[0].searchParam[3].type == "quantity"
    assert (
        inst.rest[0].resource[0].searchParam[4].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Account-subject"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[0].searchParam[4].documentation
        == "What is account tied to?"
    )
    assert inst.rest[0].resource[0].searchParam[4].name == "subject"
    assert inst.rest[0].resource[0].searchParam[4].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[5].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Account-patient"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[0].searchParam[5].documentation
        == "What is account tied to?"
    )
    assert inst.rest[0].resource[0].searchParam[5].name == "patient"
    assert inst.rest[0].resource[0].searchParam[5].type == "reference"
    assert (
        inst.rest[0].resource[0].searchParam[6].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Account-name"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[0].searchParam[6].documentation == "Human-readable label"
    )
    assert inst.rest[0].resource[0].searchParam[6].name == "name"
    assert inst.rest[0].resource[0].searchParam[6].type == "string"
    assert (
        inst.rest[0].resource[0].searchParam[7].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Account-type"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[0].searchParam[7].documentation
        == "E.g. patient, expense, depreciation"
    )
    assert inst.rest[0].resource[0].searchParam[7].name == "type"
    assert inst.rest[0].resource[0].searchParam[7].type == "token"
    assert (
        inst.rest[0].resource[0].searchParam[8].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Account-status"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[0].searchParam[8].documentation
        == "active | inactive | entered-in-error"
    )
    assert inst.rest[0].resource[0].searchParam[8].name == "status"
    assert inst.rest[0].resource[0].searchParam[8].type == "token"
    assert inst.rest[0].resource[0].searchRevInclude[0] == "ChargeItem.account"
    assert inst.rest[0].resource[0].type == "Account"
    assert inst.rest[0].resource[1].conditionalCreate is True
    assert inst.rest[0].resource[1].conditionalDelete == "multiple"
    assert inst.rest[0].resource[1].conditionalUpdate is True
    assert inst.rest[0].resource[1].interaction[0].code == "read"
    assert inst.rest[0].resource[1].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[1].code == "vread"
    assert inst.rest[0].resource[1].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[2].code == "update"
    assert inst.rest[0].resource[1].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[3].code == "delete"
    assert inst.rest[0].resource[1].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[1].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[5].code == "history-type"
    assert inst.rest[0].resource[1].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[6].code == "create"
    assert inst.rest[0].resource[1].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[1].interaction[7].code == "search-type"
    assert inst.rest[0].resource[1].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[1].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/ActivityDefinition"
    )
    assert inst.rest[0].resource[1].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[1].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[1].searchInclude[0] == "ActivityDefinition.successor"
    assert (
        inst.rest[0].resource[1].searchInclude[1] == "ActivityDefinition.derived-from"
    )
    assert inst.rest[0].resource[1].searchInclude[2] == "ActivityDefinition.predecessor"
    assert inst.rest[0].resource[1].searchInclude[3] == "ActivityDefinition.composed-of"
    assert inst.rest[0].resource[1].searchInclude[4] == "ActivityDefinition.depends-on"
    assert (
        inst.rest[0].resource[1].searchParam[0].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/ActivityDefinition-date"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[1].searchParam[0].documentation
        == "The activity definition publication date"
    )
    assert inst.rest[0].resource[1].searchParam[0].name == "date"
    assert inst.rest[0].resource[1].searchParam[0].type == "date"
    assert (
        inst.rest[0].resource[1].searchParam[1].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/ActivityDefinition-identifier"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[1].searchParam[1].documentation
        == "External identifier for the activity definition"
    )
    assert inst.rest[0].resource[1].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[1].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[1].searchParam[2].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/ActivityDefinition-successor"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[1].searchParam[2].documentation
        == "What resource is being referenced"
    )
    assert inst.rest[0].resource[1].searchParam[2].name == "successor"
    assert inst.rest[0].resource[1].searchParam[2].type == "reference"
    assert (
        inst.rest[0].resource[1].searchParam[3].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/ActivityDefinition-jurisdiction"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[1].searchParam[3].documentation
        == "Intended jurisdiction for the activity definition"
    )
    assert inst.rest[0].resource[1].searchParam[3].name == "jurisdiction"
    assert inst.rest[0].resource[1].searchParam[3].type == "token"
    assert (
        inst.rest[0].resource[1].searchParam[4].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/ActivityDefinition-description"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[1].searchParam[4].documentation
        == "The description of the activity definition"
    )
    assert inst.rest[0].resource[1].searchParam[4].name == "description"
    assert inst.rest[0].resource[1].searchParam[4].type == "string"
    assert (
        inst.rest[0].resource[1].searchParam[5].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/ActivityDefinition-derived-from"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[1].searchParam[5].documentation
        == "What resource is being referenced"
    )
    assert inst.rest[0].resource[1].searchParam[5].name == "derived-from"
    assert inst.rest[0].resource[1].searchParam[5].type == "reference"
    assert (
        inst.rest[0].resource[1].searchParam[6].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/ActivityDefinition-predecessor"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[1].searchParam[6].documentation
        == "What resource is being referenced"
    )
    assert inst.rest[0].resource[1].searchParam[6].name == "predecessor"
    assert inst.rest[0].resource[1].searchParam[6].type == "reference"
    assert (
        inst.rest[0].resource[1].searchParam[7].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/ActivityDefinition-title"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[1].searchParam[7].documentation
        == "The human-friendly name of the activity definition"
    )
    assert inst.rest[0].resource[1].searchParam[7].name == "title"
    assert inst.rest[0].resource[1].searchParam[7].type == "string"
    assert (
        inst.rest[0].resource[1].searchParam[8].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/ActivityDefinition-composed-of"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[1].searchParam[8].documentation
        == "What resource is being referenced"
    )
    assert inst.rest[0].resource[1].searchParam[8].name == "composed-of"
    assert inst.rest[0].resource[1].searchParam[8].type == "reference"
    assert (
        inst.rest[0].resource[1].searchParam[9].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/ActivityDefinition-version"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[1].searchParam[9].documentation
        == "The business version of the activity definition"
    )
    assert inst.rest[0].resource[1].searchParam[9].name == "version"
    assert inst.rest[0].resource[1].searchParam[9].type == "token"
    assert inst.rest[0].resource[1].searchRevInclude[0] == "Communication.definition"
    assert inst.rest[0].resource[1].searchRevInclude[1] == "DeviceRequest.definition"
    assert inst.rest[0].resource[1].searchRevInclude[2] == "Procedure.definition"
    assert inst.rest[0].resource[1].searchRevInclude[3] == "ProcedureRequest.definition"
    assert inst.rest[0].resource[1].searchRevInclude[4] == "ReferralRequest.definition"
    assert inst.rest[0].resource[1].type == "ActivityDefinition"
    assert inst.rest[0].resource[2].conditionalCreate is True
    assert inst.rest[0].resource[2].conditionalDelete == "multiple"
    assert inst.rest[0].resource[2].conditionalUpdate is True
    assert inst.rest[0].resource[2].interaction[0].code == "read"
    assert inst.rest[0].resource[2].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[1].code == "vread"
    assert inst.rest[0].resource[2].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[2].code == "update"
    assert inst.rest[0].resource[2].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[3].code == "delete"
    assert inst.rest[0].resource[2].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[2].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[5].code == "history-type"
    assert inst.rest[0].resource[2].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[6].code == "create"
    assert inst.rest[0].resource[2].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[2].interaction[7].code == "search-type"
    assert inst.rest[0].resource[2].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[2].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/AdverseEvent"
    )
    assert inst.rest[0].resource[2].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[2].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[2].searchInclude[0] == "AdverseEvent.recorder"
    assert inst.rest[0].resource[2].searchInclude[1] == "AdverseEvent.study"
    assert inst.rest[0].resource[2].searchInclude[2] == "AdverseEvent.reaction"
    assert inst.rest[0].resource[2].searchInclude[3] == "AdverseEvent.subject"
    assert inst.rest[0].resource[2].searchInclude[4] == "AdverseEvent.substance"
    assert inst.rest[0].resource[2].searchInclude[5] == "AdverseEvent.location"
    assert (
        inst.rest[0].resource[2].searchParam[0].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AdverseEvent-date"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[2].searchParam[0].documentation
        == "When the event occurred"
    )
    assert inst.rest[0].resource[2].searchParam[0].name == "date"
    assert inst.rest[0].resource[2].searchParam[0].type == "date"
    assert (
        inst.rest[0].resource[2].searchParam[1].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AdverseEvent-recorder"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[2].searchParam[1].documentation
        == "Who recorded the adverse event"
    )
    assert inst.rest[0].resource[2].searchParam[1].name == "recorder"
    assert inst.rest[0].resource[2].searchParam[1].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[2].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AdverseEvent-study"}
        ).valueUri
    )
    assert inst.rest[0].resource[2].searchParam[2].documentation == "AdverseEvent.study"
    assert inst.rest[0].resource[2].searchParam[2].name == "study"
    assert inst.rest[0].resource[2].searchParam[2].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[3].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AdverseEvent-reaction"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[2].searchParam[3].documentation
        == "Adverse Reaction Events linked to exposure to substance"
    )
    assert inst.rest[0].resource[2].searchParam[3].name == "reaction"
    assert inst.rest[0].resource[2].searchParam[3].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[4].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AdverseEvent-seriousness"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[2].searchParam[4].documentation
        == "Mild | Moderate | Severe"
    )
    assert inst.rest[0].resource[2].searchParam[4].name == "seriousness"
    assert inst.rest[0].resource[2].searchParam[4].type == "token"
    assert (
        inst.rest[0].resource[2].searchParam[5].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AdverseEvent-subject"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[2].searchParam[5].documentation
        == "Subject or group impacted by event"
    )
    assert inst.rest[0].resource[2].searchParam[5].name == "subject"
    assert inst.rest[0].resource[2].searchParam[5].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[6].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AdverseEvent-substance"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[2].searchParam[6].documentation
        == "Refers to the specific entity that caused the adverse event"
    )
    assert inst.rest[0].resource[2].searchParam[6].name == "substance"
    assert inst.rest[0].resource[2].searchParam[6].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[7].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AdverseEvent-location"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[2].searchParam[7].documentation
        == "Location where adverse event occurred"
    )
    assert inst.rest[0].resource[2].searchParam[7].name == "location"
    assert inst.rest[0].resource[2].searchParam[7].type == "reference"
    assert (
        inst.rest[0].resource[2].searchParam[8].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AdverseEvent-category"}
        ).valueUri
    )
    assert inst.rest[0].resource[2].searchParam[8].name == "category"
    assert inst.rest[0].resource[2].searchParam[8].type == "token"
    assert (
        inst.rest[0].resource[2].searchParam[9].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AdverseEvent-type"}
        ).valueUri
    )
    assert inst.rest[0].resource[2].searchParam[9].documentation == "actual | potential"
    assert inst.rest[0].resource[2].searchParam[9].name == "type"
    assert inst.rest[0].resource[2].searchParam[9].type == "token"
    assert inst.rest[0].resource[2].type == "AdverseEvent"
    assert inst.rest[0].resource[3].conditionalCreate is True
    assert inst.rest[0].resource[3].conditionalDelete == "multiple"
    assert inst.rest[0].resource[3].conditionalUpdate is True
    assert inst.rest[0].resource[3].interaction[0].code == "read"
    assert inst.rest[0].resource[3].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[1].code == "vread"
    assert inst.rest[0].resource[3].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[2].code == "update"
    assert inst.rest[0].resource[3].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[3].code == "delete"
    assert inst.rest[0].resource[3].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[3].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[5].code == "history-type"
    assert inst.rest[0].resource[3].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[6].code == "create"
    assert inst.rest[0].resource[3].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[3].interaction[7].code == "search-type"
    assert inst.rest[0].resource[3].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[3].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/AllergyIntolerance"
    )
    assert inst.rest[0].resource[3].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[3].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[3].searchInclude[0] == "AllergyIntolerance.recorder"
    assert inst.rest[0].resource[3].searchInclude[1] == "AllergyIntolerance.asserter"
    assert inst.rest[0].resource[3].searchInclude[2] == "AllergyIntolerance.patient"
    assert (
        inst.rest[0].resource[3].searchParam[0].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-severity"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[3].searchParam[0].documentation
        == "mild | moderate | severe (of event as a whole)"
    )
    assert inst.rest[0].resource[3].searchParam[0].name == "severity"
    assert inst.rest[0].resource[3].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[1].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/clinical-date"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[3].searchParam[1].documentation
        == "Date record was believed accurate"
    )
    assert inst.rest[0].resource[3].searchParam[1].name == "date"
    assert inst.rest[0].resource[3].searchParam[1].type == "date"
    assert (
        inst.rest[0].resource[3].searchParam[2].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/clinical-identifier"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[3].searchParam[2].documentation
        == "External ids for this item"
    )
    assert inst.rest[0].resource[3].searchParam[2].name == "identifier"
    assert inst.rest[0].resource[3].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[3].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-manifestation"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[3].searchParam[3].documentation
        == "Clinical symptoms/signs associated with the Event"
    )
    assert inst.rest[0].resource[3].searchParam[3].name == "manifestation"
    assert inst.rest[0].resource[3].searchParam[3].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[4].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-recorder"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[3].searchParam[4].documentation
        == "Who recorded the sensitivity"
    )
    assert inst.rest[0].resource[3].searchParam[4].name == "recorder"
    assert inst.rest[0].resource[3].searchParam[4].type == "reference"
    assert (
        inst.rest[0].resource[3].searchParam[5].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/clinical-code"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[3].searchParam[5].documentation
        == "Code that identifies the allergy or intolerance"
    )
    assert inst.rest[0].resource[3].searchParam[5].name == "code"
    assert inst.rest[0].resource[3].searchParam[5].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[6].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-verification-status"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[3].searchParam[6].documentation
        == "unconfirmed | confirmed | refuted | entered-in-error"
    )
    assert inst.rest[0].resource[3].searchParam[6].name == "verification-status"
    assert inst.rest[0].resource[3].searchParam[6].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[7].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-criticality"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[3].searchParam[7].documentation
        == "low | high | unable-to-assess"
    )
    assert inst.rest[0].resource[3].searchParam[7].name == "criticality"
    assert inst.rest[0].resource[3].searchParam[7].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[8].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AllergyIntolerance-clinical-status"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[3].searchParam[8].documentation
        == "active | inactive | resolved"
    )
    assert inst.rest[0].resource[3].searchParam[8].name == "clinical-status"
    assert inst.rest[0].resource[3].searchParam[8].type == "token"
    assert (
        inst.rest[0].resource[3].searchParam[9].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/clinical-type"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[3].searchParam[9].documentation
        == "allergy | intolerance - Underlying mechanism (if known)"
    )
    assert inst.rest[0].resource[3].searchParam[9].name == "type"
    assert inst.rest[0].resource[3].searchParam[9].type == "token"
    assert inst.rest[0].resource[3].searchRevInclude[0] == "ClinicalImpression.problem"
    assert (
        inst.rest[0].resource[3].searchRevInclude[1]
        == "ImmunizationRecommendation.information"
    )
    assert inst.rest[0].resource[3].type == "AllergyIntolerance"
    assert inst.rest[0].resource[4].conditionalCreate is True
    assert inst.rest[0].resource[4].conditionalDelete == "multiple"
    assert inst.rest[0].resource[4].conditionalUpdate is True
    assert inst.rest[0].resource[4].interaction[0].code == "read"
    assert inst.rest[0].resource[4].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[1].code == "vread"
    assert inst.rest[0].resource[4].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[2].code == "update"
    assert inst.rest[0].resource[4].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[3].code == "delete"
    assert inst.rest[0].resource[4].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[4].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[5].code == "history-type"
    assert inst.rest[0].resource[4].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[6].code == "create"
    assert inst.rest[0].resource[4].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[4].interaction[7].code == "search-type"
    assert inst.rest[0].resource[4].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[4].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Appointment"
    )
    assert inst.rest[0].resource[4].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[4].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[4].searchInclude[0] == "Appointment.actor"
    assert inst.rest[0].resource[4].searchInclude[1] == "Appointment.practitioner"
    assert inst.rest[0].resource[4].searchInclude[2] == "Appointment.incomingreferral"
    assert inst.rest[0].resource[4].searchInclude[3] == "Appointment.patient"
    assert inst.rest[0].resource[4].searchInclude[4] == "Appointment.location"
    assert (
        inst.rest[0].resource[4].searchParam[0].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Appointment-date"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[4].searchParam[0].documentation
        == "Appointment date/time."
    )
    assert inst.rest[0].resource[4].searchParam[0].name == "date"
    assert inst.rest[0].resource[4].searchParam[0].type == "date"
    assert (
        inst.rest[0].resource[4].searchParam[1].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Appointment-actor"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[4].searchParam[1].documentation
        == "Any one of the individuals participating in the appointment"
    )
    assert inst.rest[0].resource[4].searchParam[1].name == "actor"
    assert inst.rest[0].resource[4].searchParam[1].type == "reference"
    assert (
        inst.rest[0].resource[4].searchParam[2].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Appointment-identifier"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[4].searchParam[2].documentation
        == "An Identifier of the Appointment"
    )
    assert inst.rest[0].resource[4].searchParam[2].name == "identifier"
    assert inst.rest[0].resource[4].searchParam[2].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[3].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Appointment-practitioner"}
        ).valueUri
    )
    assert inst.rest[0].resource[4].searchParam[3].documentation == (
        "One of the individuals of the appointment is this " "practitioner"
    )
    assert inst.rest[0].resource[4].searchParam[3].name == "practitioner"
    assert inst.rest[0].resource[4].searchParam[3].type == "reference"
    assert (
        inst.rest[0].resource[4].searchParam[4].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/Appointment-incomingreferral"
            }
        ).valueUri
    )
    assert inst.rest[0].resource[4].searchParam[4].documentation == (
        "The ReferralRequest provided as information to allocate to " "the Encounter"
    )
    assert inst.rest[0].resource[4].searchParam[4].name == "incomingreferral"
    assert inst.rest[0].resource[4].searchParam[4].type == "reference"
    assert (
        inst.rest[0].resource[4].searchParam[5].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Appointment-part-status"}
        ).valueUri
    )
    assert inst.rest[0].resource[4].searchParam[5].documentation == (
        "The Participation status of the subject, or other "
        "participant on the appointment. Can be used to locate "
        "participants that have not responded to meeting requests."
    )
    assert inst.rest[0].resource[4].searchParam[5].name == "part-status"
    assert inst.rest[0].resource[4].searchParam[5].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[6].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Appointment-patient"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[4].searchParam[6].documentation
        == "One of the individuals of the appointment is this patient"
    )
    assert inst.rest[0].resource[4].searchParam[6].name == "patient"
    assert inst.rest[0].resource[4].searchParam[6].type == "reference"
    assert (
        inst.rest[0].resource[4].searchParam[7].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/Appointment-appointment-type"
            }
        ).valueUri
    )
    assert inst.rest[0].resource[4].searchParam[7].documentation == (
        "The style of appointment or patient that has been booked in "
        "the slot (not service type)"
    )
    assert inst.rest[0].resource[4].searchParam[7].name == "appointment-type"
    assert inst.rest[0].resource[4].searchParam[7].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[8].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Appointment-service-type"}
        ).valueUri
    )
    assert inst.rest[0].resource[4].searchParam[8].documentation == (
        "The specific service that is to be performed during this " "appointment"
    )
    assert inst.rest[0].resource[4].searchParam[8].name == "service-type"
    assert inst.rest[0].resource[4].searchParam[8].type == "token"
    assert (
        inst.rest[0].resource[4].searchParam[9].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Appointment-location"}
        ).valueUri
    )
    assert inst.rest[0].resource[4].searchParam[9].documentation == (
        "This location is listed in the participants of the " "appointment"
    )
    assert inst.rest[0].resource[4].searchParam[9].name == "location"
    assert inst.rest[0].resource[4].searchParam[9].type == "reference"
    assert (
        inst.rest[0].resource[4].searchRevInclude[0]
        == "AppointmentResponse.appointment"
    )
    assert inst.rest[0].resource[4].searchRevInclude[1] == "CarePlan.activity-reference"
    assert inst.rest[0].resource[4].searchRevInclude[2] == "ClinicalImpression.action"
    assert inst.rest[0].resource[4].searchRevInclude[3] == "Encounter.appointment"
    assert inst.rest[0].resource[4].type == "Appointment"
    assert inst.rest[0].resource[5].conditionalCreate is True
    assert inst.rest[0].resource[5].conditionalDelete == "multiple"
    assert inst.rest[0].resource[5].conditionalUpdate is True
    assert inst.rest[0].resource[5].interaction[0].code == "read"
    assert inst.rest[0].resource[5].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[1].code == "vread"
    assert inst.rest[0].resource[5].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[2].code == "update"
    assert inst.rest[0].resource[5].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[3].code == "delete"
    assert inst.rest[0].resource[5].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[5].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[5].code == "history-type"
    assert inst.rest[0].resource[5].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[6].code == "create"
    assert inst.rest[0].resource[5].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[5].interaction[7].code == "search-type"
    assert inst.rest[0].resource[5].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[5].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/AppointmentResponse"
    )
    assert inst.rest[0].resource[5].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[5].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[5].searchInclude[0] == "AppointmentResponse.actor"
    assert (
        inst.rest[0].resource[5].searchInclude[1] == "AppointmentResponse.practitioner"
    )
    assert inst.rest[0].resource[5].searchInclude[2] == "AppointmentResponse.patient"
    assert (
        inst.rest[0].resource[5].searchInclude[3] == "AppointmentResponse.appointment"
    )
    assert inst.rest[0].resource[5].searchInclude[4] == "AppointmentResponse.location"
    assert (
        inst.rest[0].resource[5].searchParam[0].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AppointmentResponse-actor"
            }
        ).valueUri
    )
    assert inst.rest[0].resource[5].searchParam[0].documentation == (
        "The Person, Location/HealthcareService or Device that this "
        "appointment response replies for"
    )
    assert inst.rest[0].resource[5].searchParam[0].name == "actor"
    assert inst.rest[0].resource[5].searchParam[0].type == "reference"
    assert (
        inst.rest[0].resource[5].searchParam[1].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AppointmentResponse-identifier"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[5].searchParam[1].documentation
        == "An Identifier in this appointment response"
    )
    assert inst.rest[0].resource[5].searchParam[1].name == "identifier"
    assert inst.rest[0].resource[5].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[5].searchParam[2].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AppointmentResponse-practitioner"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[5].searchParam[2].documentation
        == "This Response is for this Practitioner"
    )
    assert inst.rest[0].resource[5].searchParam[2].name == "practitioner"
    assert inst.rest[0].resource[5].searchParam[2].type == "reference"
    assert (
        inst.rest[0].resource[5].searchParam[3].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AppointmentResponse-part-status"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[5].searchParam[3].documentation
        == "The participants acceptance status for this appointment"
    )
    assert inst.rest[0].resource[5].searchParam[3].name == "part-status"
    assert inst.rest[0].resource[5].searchParam[3].type == "token"
    assert (
        inst.rest[0].resource[5].searchParam[4].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AppointmentResponse-patient"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[5].searchParam[4].documentation
        == "This Response is for this Patient"
    )
    assert inst.rest[0].resource[5].searchParam[4].name == "patient"
    assert inst.rest[0].resource[5].searchParam[4].type == "reference"
    assert (
        inst.rest[0].resource[5].searchParam[5].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AppointmentResponse-appointment"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[5].searchParam[5].documentation
        == "The appointment that the response is attached to"
    )
    assert inst.rest[0].resource[5].searchParam[5].name == "appointment"
    assert inst.rest[0].resource[5].searchParam[5].type == "reference"
    assert (
        inst.rest[0].resource[5].searchParam[6].definition
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/SearchParameter/AppointmentResponse-location"
            }
        ).valueUri
    )
    assert (
        inst.rest[0].resource[5].searchParam[6].documentation
        == "This Response is for this Location"
    )
    assert inst.rest[0].resource[5].searchParam[6].name == "location"
    assert inst.rest[0].resource[5].searchParam[6].type == "reference"
    assert inst.rest[0].resource[5].type == "AppointmentResponse"
    assert inst.rest[0].resource[6].conditionalCreate is True
    assert inst.rest[0].resource[6].conditionalDelete == "multiple"
    assert inst.rest[0].resource[6].conditionalUpdate is True
    assert inst.rest[0].resource[6].interaction[0].code == "read"
    assert inst.rest[0].resource[6].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[1].code == "vread"
    assert inst.rest[0].resource[6].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[2].code == "update"
    assert inst.rest[0].resource[6].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[3].code == "delete"
    assert inst.rest[0].resource[6].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[6].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[5].code == "history-type"
    assert inst.rest[0].resource[6].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[6].code == "create"
    assert inst.rest[0].resource[6].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[6].interaction[7].code == "search-type"
    assert inst.rest[0].resource[6].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[6].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/AuditEvent"
    )
    assert inst.rest[0].resource[6].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[6].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[6].searchInclude[0] == "AuditEvent.agent"
    assert inst.rest[0].resource[6].searchInclude[1] == "AuditEvent.patient"
    assert inst.rest[0].resource[6].searchInclude[2] == "AuditEvent.entity"
    assert (
        inst.rest[0].resource[6].searchParam[0].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AuditEvent-date"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[6].searchParam[0].documentation
        == "Time when the event occurred on source"
    )
    assert inst.rest[0].resource[6].searchParam[0].name == "date"
    assert inst.rest[0].resource[6].searchParam[0].type == "date"
    assert (
        inst.rest[0].resource[6].searchParam[1].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AuditEvent-entity-type"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[6].searchParam[1].documentation
        == "Type of entity involved"
    )
    assert inst.rest[0].resource[6].searchParam[1].name == "entity-type"
    assert inst.rest[0].resource[6].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[2].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AuditEvent-agent"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[6].searchParam[2].documentation
        == "Direct reference to resource"
    )
    assert inst.rest[0].resource[6].searchParam[2].name == "agent"
    assert inst.rest[0].resource[6].searchParam[2].type == "reference"
    assert (
        inst.rest[0].resource[6].searchParam[3].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AuditEvent-address"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[6].searchParam[3].documentation
        == "Identifier for the network access point of the user device"
    )
    assert inst.rest[0].resource[6].searchParam[3].name == "address"
    assert inst.rest[0].resource[6].searchParam[3].type == "string"
    assert (
        inst.rest[0].resource[6].searchParam[4].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AuditEvent-entity-role"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[6].searchParam[4].documentation
        == "What role the entity played"
    )
    assert inst.rest[0].resource[6].searchParam[4].name == "entity-role"
    assert inst.rest[0].resource[6].searchParam[4].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[5].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AuditEvent-source"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[6].searchParam[5].documentation
        == "The identity of source detecting the event"
    )
    assert inst.rest[0].resource[6].searchParam[5].name == "source"
    assert inst.rest[0].resource[6].searchParam[5].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[6].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AuditEvent-type"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[6].searchParam[6].documentation
        == "Type/identifier of event"
    )
    assert inst.rest[0].resource[6].searchParam[6].name == "type"
    assert inst.rest[0].resource[6].searchParam[6].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[7].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AuditEvent-altid"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[6].searchParam[7].documentation
        == "Alternative User id e.g. authentication"
    )
    assert inst.rest[0].resource[6].searchParam[7].name == "altid"
    assert inst.rest[0].resource[6].searchParam[7].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[8].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AuditEvent-site"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[6].searchParam[8].documentation
        == "Logical source location within the enterprise"
    )
    assert inst.rest[0].resource[6].searchParam[8].name == "site"
    assert inst.rest[0].resource[6].searchParam[8].type == "token"
    assert (
        inst.rest[0].resource[6].searchParam[9].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/AuditEvent-agent-name"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[6].searchParam[9].documentation
        == "Human-meaningful name for the agent"
    )
    assert inst.rest[0].resource[6].searchParam[9].name == "agent-name"
    assert inst.rest[0].resource[6].searchParam[9].type == "string"
    assert inst.rest[0].resource[6].type == "AuditEvent"
    assert inst.rest[0].resource[7].conditionalCreate is True
    assert inst.rest[0].resource[7].conditionalDelete == "multiple"
    assert inst.rest[0].resource[7].conditionalUpdate is True
    assert inst.rest[0].resource[7].interaction[0].code == "read"
    assert inst.rest[0].resource[7].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[1].code == "vread"
    assert inst.rest[0].resource[7].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[2].code == "update"
    assert inst.rest[0].resource[7].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[3].code == "delete"
    assert inst.rest[0].resource[7].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[7].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[5].code == "history-type"
    assert inst.rest[0].resource[7].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[6].code == "create"
    assert inst.rest[0].resource[7].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[7].interaction[7].code == "search-type"
    assert inst.rest[0].resource[7].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[7].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Basic"
    )
    assert inst.rest[0].resource[7].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[7].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[7].searchInclude[0] == "Basic.subject"
    assert inst.rest[0].resource[7].searchInclude[1] == "Basic.patient"
    assert inst.rest[0].resource[7].searchInclude[2] == "Basic.author"
    assert (
        inst.rest[0].resource[7].searchParam[0].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Basic-identifier"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[7].searchParam[0].documentation == "Business identifier"
    )
    assert inst.rest[0].resource[7].searchParam[0].name == "identifier"
    assert inst.rest[0].resource[7].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[7].searchParam[1].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Basic-code"}
        ).valueUri
    )
    assert inst.rest[0].resource[7].searchParam[1].documentation == "Kind of Resource"
    assert inst.rest[0].resource[7].searchParam[1].name == "code"
    assert inst.rest[0].resource[7].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[7].searchParam[2].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Basic-subject"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[7].searchParam[2].documentation
        == "Identifies the focus of this resource"
    )
    assert inst.rest[0].resource[7].searchParam[2].name == "subject"
    assert inst.rest[0].resource[7].searchParam[2].type == "reference"
    assert (
        inst.rest[0].resource[7].searchParam[3].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Basic-created"}
        ).valueUri
    )
    assert inst.rest[0].resource[7].searchParam[3].documentation == "When created"
    assert inst.rest[0].resource[7].searchParam[3].name == "created"
    assert inst.rest[0].resource[7].searchParam[3].type == "date"
    assert (
        inst.rest[0].resource[7].searchParam[4].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Basic-patient"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[7].searchParam[4].documentation
        == "Identifies the focus of this resource"
    )
    assert inst.rest[0].resource[7].searchParam[4].name == "patient"
    assert inst.rest[0].resource[7].searchParam[4].type == "reference"
    assert (
        inst.rest[0].resource[7].searchParam[5].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Basic-author"}
        ).valueUri
    )
    assert inst.rest[0].resource[7].searchParam[5].documentation == "Who created"
    assert inst.rest[0].resource[7].searchParam[5].name == "author"
    assert inst.rest[0].resource[7].searchParam[5].type == "reference"
    assert inst.rest[0].resource[7].type == "Basic"
    assert inst.rest[0].resource[8].conditionalCreate is True
    assert inst.rest[0].resource[8].conditionalDelete == "multiple"
    assert inst.rest[0].resource[8].conditionalUpdate is True
    assert inst.rest[0].resource[8].interaction[0].code == "read"
    assert inst.rest[0].resource[8].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[1].code == "vread"
    assert inst.rest[0].resource[8].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[2].code == "update"
    assert inst.rest[0].resource[8].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[3].code == "delete"
    assert inst.rest[0].resource[8].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[8].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[5].code == "history-type"
    assert inst.rest[0].resource[8].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[6].code == "create"
    assert inst.rest[0].resource[8].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[8].interaction[7].code == "search-type"
    assert inst.rest[0].resource[8].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[8].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Binary"
    )
    assert inst.rest[0].resource[8].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[8].referencePolicy[1] == "logical"
    assert (
        inst.rest[0].resource[8].searchParam[0].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Binary-contenttype"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[8].searchParam[0].documentation
        == "MimeType of the binary content"
    )
    assert inst.rest[0].resource[8].searchParam[0].name == "contenttype"
    assert inst.rest[0].resource[8].searchParam[0].type == "token"
    assert inst.rest[0].resource[8].type == "Binary"
    assert inst.rest[0].resource[9].conditionalCreate is True
    assert inst.rest[0].resource[9].conditionalDelete == "multiple"
    assert inst.rest[0].resource[9].conditionalUpdate is True
    assert inst.rest[0].resource[9].interaction[0].code == "read"
    assert inst.rest[0].resource[9].interaction[0].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[1].code == "vread"
    assert inst.rest[0].resource[9].interaction[1].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[2].code == "update"
    assert inst.rest[0].resource[9].interaction[2].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[3].code == "delete"
    assert inst.rest[0].resource[9].interaction[3].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[4].code == "history-instance"
    assert inst.rest[0].resource[9].interaction[4].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[5].code == "history-type"
    assert inst.rest[0].resource[9].interaction[5].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[6].code == "create"
    assert inst.rest[0].resource[9].interaction[6].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert inst.rest[0].resource[9].interaction[7].code == "search-type"
    assert inst.rest[0].resource[9].interaction[7].documentation == (
        "Implemented per the specification (or Insert other doco " "here)"
    )
    assert (
        inst.rest[0].resource[9].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/BodySite"
    )
    assert inst.rest[0].resource[9].referencePolicy[0] == "literal"
    assert inst.rest[0].resource[9].referencePolicy[1] == "logical"
    assert inst.rest[0].resource[9].searchInclude[0] == "BodySite.patient"
    assert (
        inst.rest[0].resource[9].searchParam[0].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/BodySite-identifier"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[9].searchParam[0].documentation
        == "Identifier for this instance of the anatomical location"
    )
    assert inst.rest[0].resource[9].searchParam[0].name == "identifier"
    assert inst.rest[0].resource[9].searchParam[0].type == "token"
    assert (
        inst.rest[0].resource[9].searchParam[1].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/BodySite-code"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[9].searchParam[1].documentation
        == "Named anatomical location"
    )
    assert inst.rest[0].resource[9].searchParam[1].name == "code"
    assert inst.rest[0].resource[9].searchParam[1].type == "token"
    assert (
        inst.rest[0].resource[9].searchParam[2].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/BodySite-patient"}
        ).valueUri
    )
    assert (
        inst.rest[0].resource[9].searchParam[2].documentation
        == "Patient to whom bodysite belongs"
    )
    assert inst.rest[0].resource[9].searchParam[2].name == "patient"
    assert inst.rest[0].resource[9].searchParam[2].type == "reference"
    assert inst.rest[0].resource[9].type == "BodySite"
    assert (
        inst.rest[0].searchParam[0].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/DomainResource-text"}
        ).valueUri
    )
    assert (
        inst.rest[0].searchParam[0].documentation
        == "Search on the narrative of the resource"
    )
    assert inst.rest[0].searchParam[0].name == "_text"
    assert inst.rest[0].searchParam[0].type == "string"
    assert (
        inst.rest[0].searchParam[1].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-query"}
        ).valueUri
    )
    assert inst.rest[0].searchParam[1].documentation == (
        "A custom search profile that describes a specific defined " "query operation"
    )
    assert inst.rest[0].searchParam[1].name == "_query"
    assert inst.rest[0].searchParam[1].type == "token"
    assert (
        inst.rest[0].searchParam[2].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-profile"}
        ).valueUri
    )
    assert (
        inst.rest[0].searchParam[2].documentation
        == "Profiles this resource claims to conform to"
    )
    assert inst.rest[0].searchParam[2].name == "_profile"
    assert inst.rest[0].searchParam[2].type == "uri"
    assert (
        inst.rest[0].searchParam[3].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-lastUpdated"}
        ).valueUri
    )
    assert (
        inst.rest[0].searchParam[3].documentation
        == "When the resource version last changed"
    )
    assert inst.rest[0].searchParam[3].name == "_lastUpdated"
    assert inst.rest[0].searchParam[3].type == "date"
    assert (
        inst.rest[0].searchParam[4].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-tag"}
        ).valueUri
    )
    assert inst.rest[0].searchParam[4].documentation == "Tags applied to this resource"
    assert inst.rest[0].searchParam[4].name == "_tag"
    assert inst.rest[0].searchParam[4].type == "token"
    assert (
        inst.rest[0].searchParam[5].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-security"}
        ).valueUri
    )
    assert (
        inst.rest[0].searchParam[5].documentation
        == "Security Labels applied to this resource"
    )
    assert inst.rest[0].searchParam[5].name == "_security"
    assert inst.rest[0].searchParam[5].type == "token"
    assert (
        inst.rest[0].searchParam[6].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-id"}
        ).valueUri
    )
    assert inst.rest[0].searchParam[6].documentation == "Logical id of this artifact"
    assert inst.rest[0].searchParam[6].name == "_id"
    assert inst.rest[0].searchParam[6].type == "token"
    assert (
        inst.rest[0].searchParam[7].definition
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/SearchParameter/Resource-content"}
        ).valueUri
    )
    assert (
        inst.rest[0].searchParam[7].documentation
        == "Search on the entire content of the resource"
    )
    assert inst.rest[0].searchParam[7].name == "_content"
    assert inst.rest[0].searchParam[7].type == "string"
    assert inst.rest[0].security.cors is True
    assert inst.rest[0].security.description == (
        "This is the Capability Statement to declare that the server "
        "supports SMART-on-FHIR. See the SMART-on-FHIR docs for the "
        "extension that would go with such a server"
    )
    assert inst.rest[0].security.service[0].coding[0].code == "SMART-on-FHIR"
    assert inst.rest[0].security.service[0].coding[0].display == "SMART-on-FHIR"
    assert (
        inst.rest[0].security.service[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/restful-security-service"}
        ).valueUri
    )
    assert inst.rest[0].security.service[0].text == "See http://docs.smarthealthit.org/"
    assert inst.software.name == "Insert your softwware name here..."
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/CapabilityStatement/base"}
        ).valueUri
    )
    assert inst.version == "3.0.2-11200"


def test_capabilitystatement_2(base_settings):
    """No. 2 tests collection for CapabilityStatement.
    Test File: capabilitystatement-capabilitystatement-base(base).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "capabilitystatement-capabilitystatement-base(base).json"
    )
    inst = capabilitystatement.CapabilityStatement.model_validate_json(
        filename.read_bytes()
    )
    assert "CapabilityStatement" == inst.get_resource_type()

    impl_capabilitystatement_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "CapabilityStatement" == data["resourceType"]

    inst2 = capabilitystatement.CapabilityStatement(**data)
    impl_capabilitystatement_2(inst2)
