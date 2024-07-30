# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import operationdefinition
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_operationdefinition_1(inst):
    assert inst.affectsState is False
    assert inst.code == "translate-id"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[0].valueInteger == 1
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "NamingSystem-translate-id"
    assert inst.instance is False
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unstats.un.org/unsd/methods/m49/m49.htm"}
        ).valueUri
    )
    assert inst.kind == "operation"
    assert inst.name == "TranslateId"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "id"
    assert inst.parameter[0].type == "string"
    assert inst.parameter[0].use == "in"
    assert (
        inst.parameter[1].binding.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName"
            }
        ).valueUri
    )
    assert (
        inst.parameter[1].binding.extension[0].valueString
        == "NamingSystemIdentifierType"
    )
    assert inst.parameter[1].binding.strength == "required"
    assert inst.parameter[1].binding.valueSet == (
        "http://hl7.org/fhir/ValueSet/namingsystem-identifier-" "type|5.0.0"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "sourceType"
    assert inst.parameter[1].type == "code"
    assert inst.parameter[1].use == "in"
    assert (
        inst.parameter[2].binding.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName"
            }
        ).valueUri
    )
    assert (
        inst.parameter[2].binding.extension[0].valueString
        == "NamingSystemIdentifierType"
    )
    assert inst.parameter[2].binding.strength == "required"
    assert inst.parameter[2].binding.valueSet == (
        "http://hl7.org/fhir/ValueSet/namingsystem-identifier-" "type|5.0.0"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "targetType"
    assert inst.parameter[2].type == "code"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
        "If preferredOnly = true then return only the preferred "
        "identifier, or if preferredOnly = false then return all "
        "available ids."
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "preferredOnly"
    assert inst.parameter[3].type == "boolean"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == (
        "If 'date' is supplied return only ids that have a validity "
        "period that includes that date."
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "date"
    assert inst.parameter[4].type == "dateTime"
    assert inst.parameter[4].use == "in"
    assert (
        inst.parameter[5].documentation
        == "True if the identifier could be translated successfully."
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 1
    assert inst.parameter[5].name == "result"
    assert inst.parameter[5].type == "boolean"
    assert inst.parameter[5].use == "out"
    assert (
        inst.parameter[6].documentation
        == "The target identifer(s) of the requested type"
    )
    assert inst.parameter[6].max == "*"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "targetIdentifier"
    assert inst.parameter[6].type == "string"
    assert inst.parameter[6].use == "out"
    assert (
        inst.parameter[7].documentation == "Whether the target identifier is preferred."
    )
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "targetIdentifer.preferred"
    assert inst.parameter[7].type == "boolean"
    assert inst.parameter[7].use == "out"
    assert (
        inst.parameter[8].documentation
        == "The perioid when the target identifier is valid."
    )
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "targetIdentifier.period"
    assert inst.parameter[8].type == "Period"
    assert inst.parameter[8].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "NamingSystem"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Translate id"
    assert inst.type is True
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/OperationDefinition/NamingSystem-translate-id"
            }
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_operationdefinition_1(base_settings):
    """No. 1 tests collection for OperationDefinition.
    Test File: operation-namingsystem-translate-id.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-namingsystem-translate-id.json"
    )
    inst = operationdefinition.OperationDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "OperationDefinition" == inst.get_resource_type()

    impl_operationdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_1(inst2)


def impl_operationdefinition_2(inst):
    assert inst.affectsState is True
    assert inst.code == "docref"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[0].valueInteger == 3
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "DocumentReference-docref"
    assert inst.instance is False
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unstats.un.org/unsd/methods/m49/m49.htm"}
        ).valueUri
    )
    assert inst.kind == "operation"
    assert inst.name == "Docref"
    assert inst.parameter[0].documentation == (
        "The id of the patient resource located on the server on "
        "which this operation is executed.  If there is no match, an "
        "empty Bundle is returned"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "patient"
    assert inst.parameter[0].type == "id"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "start"
    assert inst.parameter[1].type == "dateTime"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "end"
    assert inst.parameter[2].type == "dateTime"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].binding.strength == "required"
    assert (
        inst.parameter[3].binding.valueSet
        == "http://hl7.org/fhir/ValueSet/doc-typecodes|5.0.0"
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "type"
    assert inst.parameter[3].type == "CodeableConcept"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == (
        "This on-demand parameter allows client to dictate whether "
        "they are requesting only 'on-demand' or both 'on-demand' and"
        " 'stable' documents (or delayed/deferred assembly) that meet"
        " the query parameters"
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "on-demand"
    assert inst.parameter[4].type == "boolean"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == (
        'The bundle type is "searchset"containing '
        "[DocumentReference](documentreference.html) resources."
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 1
    assert inst.parameter[5].name == "return"
    assert inst.parameter[5].type == "Bundle"
    assert inst.parameter[5].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "DocumentReference"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Fetch DocumentReference"
    assert inst.type is True
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/OperationDefinition/DocumentReference-docref"
            }
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_operationdefinition_2(base_settings):
    """No. 2 tests collection for OperationDefinition.
    Test File: operation-documentreference-docref.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-documentreference-docref.json"
    )
    inst = operationdefinition.OperationDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "OperationDefinition" == inst.get_resource_type()

    impl_operationdefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_2(inst2)


def impl_operationdefinition_3(inst):
    assert inst.affectsState is False
    assert inst.code == "status"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "This operation is used to return the current status "
        "information about one or more topic-based Subscriptions."
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[0].valueInteger == 2
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Subscription-status"
    assert inst.instance is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unstats.un.org/unsd/methods/m49/m49.htm"}
        ).valueUri
    )
    assert inst.kind == "operation"
    assert inst.name == "Status"
    assert inst.parameter[0].max == "*"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "id"
    assert inst.parameter[0].scope[0] == "type"
    assert inst.parameter[0].type == "id"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].binding.strength == "required"
    assert (
        inst.parameter[1].binding.valueSet
        == "http://hl7.org/fhir/ValueSet/subscription-status|5.0.0"
    )
    assert inst.parameter[1].max == "*"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "status"
    assert inst.parameter[1].scope[0] == "type"
    assert inst.parameter[1].type == "code"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "The operation returns a bundle containing zero or more "
        "SubscriptionStatus resources, one per Subscription in the "
        'request that was found. The Bundle type is "searchset".'
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "return"
    assert inst.parameter[2].type == "Bundle"
    assert inst.parameter[2].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Subscription"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == (
        "Get Current Subscription Status for One or More " "Subscriptions"
    )
    assert inst.type is True
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/OperationDefinition/Subscription-status"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_operationdefinition_3(base_settings):
    """No. 3 tests collection for OperationDefinition.
    Test File: operation-subscription-status.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-subscription-status.json"
    inst = operationdefinition.OperationDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "OperationDefinition" == inst.get_resource_type()

    impl_operationdefinition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_3(inst2)


def impl_operationdefinition_4(inst):
    assert inst.affectsState is False
    assert inst.code == "data-requirements"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "The data-requirements operation aggregates and returns the "
        "parameters and data requirements for the measure and all its"
        " dependencies as a single module definition"
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[0].valueInteger == 3
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Measure-data-requirements"
    assert inst.instance is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unstats.un.org/unsd/methods/m49/m49.htm"}
        ).valueUri
    )
    assert inst.kind == "operation"
    assert inst.name == "DataRequirements"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "periodStart"
    assert inst.parameter[0].type == "date"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The end of the measurement period. The period will end at "
        "the end of the period implied by the supplied timestamp. "
        "E.g. a value of 2014 would set the period end to be "
        "2014-12-31T23:59:59 inclusive"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "periodEnd"
    assert inst.parameter[1].type == "date"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "The result of the requirements gathering is a module-"
        "definition Library that describes the aggregate parameters, "
        "data requirements, and dependencies of the measure"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "return"
    assert inst.parameter[2].type == "Library"
    assert inst.parameter[2].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Measure"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Data Requirements"
    assert inst.type is False
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/OperationDefinition/Measure-data-requirements"
            }
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_operationdefinition_4(base_settings):
    """No. 4 tests collection for OperationDefinition.
    Test File: operation-measure-data-requirements.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-measure-data-requirements.json"
    )
    inst = operationdefinition.OperationDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "OperationDefinition" == inst.get_resource_type()

    impl_operationdefinition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_4(inst2)


def impl_operationdefinition_5(inst):
    assert inst.affectsState is False
    assert inst.code == "translate"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[0].valueInteger == 1
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "ConceptMap-translate"
    assert inst.instance is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unstats.un.org/unsd/methods/m49/m49.htm"}
        ).valueUri
    )
    assert inst.kind == "operation"
    assert inst.name == "Translate"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "url"
    assert inst.parameter[0].scope[0] == "type"
    assert inst.parameter[0].type == "uri"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The concept map is provided directly as part of the request."
        " Servers may choose not to accept concept maps in this "
        "fashion."
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "conceptMap"
    assert inst.parameter[1].scope[0] == "type"
    assert inst.parameter[1].type == "ConceptMap"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "conceptMapVersion"
    assert inst.parameter[2].scope[0] == "type"
    assert inst.parameter[2].type == "string"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
        "The code that is to be translated. If a code is provided, a "
        "system must be provided"
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "sourceCode"
    assert inst.parameter[3].type == "code"
    assert inst.parameter[3].use == "in"
    assert (
        inst.parameter[4].documentation
        == "The system for the code that is to be translated"
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "system"
    assert inst.parameter[4].type == "uri"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == (
        "The version of the system, if one was provided in the source" " data"
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "version"
    assert inst.parameter[5].type == "string"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].documentation == (
        "Limits the scope of the $translate operation to source codes"
        " (ConceptMap.group.element.code) that are members of this "
        "value set."
    )
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "sourceScope"
    assert inst.parameter[6].type == "uri"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].documentation == "A coding to translate"
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "sourceCoding"
    assert inst.parameter[7].type == "Coding"
    assert inst.parameter[7].use == "in"
    assert inst.parameter[8].documentation == (
        "A full codeableConcept to validate. The server can translate"
        " any of the coding values (e.g. existing translations) as it"
        " chooses"
    )
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "sourceCodeableConcept"
    assert inst.parameter[8].type == "CodeableConcept"
    assert inst.parameter[8].use == "in"
    assert inst.parameter[9].documentation == (
        "The target code that is to be translated to. If a code is "
        "provided, a system must be provided"
    )
    assert inst.parameter[9].max == "1"
    assert inst.parameter[9].min == 0
    assert inst.parameter[9].name == "targetCode"
    assert inst.parameter[9].type == "uri"
    assert inst.parameter[9].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "ConceptMap"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Concept Translation"
    assert inst.type is True
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/OperationDefinition/ConceptMap-translate"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_operationdefinition_5(base_settings):
    """No. 5 tests collection for OperationDefinition.
    Test File: operation-conceptmap-translate.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-conceptmap-translate.json"
    )
    inst = operationdefinition.OperationDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "OperationDefinition" == inst.get_resource_type()

    impl_operationdefinition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_5(inst2)


def impl_operationdefinition_6(inst):
    assert inst.affectsState is True
    assert inst.code == "add"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "Add content to an array in a large resource such as List or "
        "Group. See [Operations for Large Resources](operations-for-"
        "large-resources.html)."
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[0].valueInteger == 0
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Resource-add"
    assert inst.instance is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unstats.un.org/unsd/methods/m49/m49.htm"}
        ).valueUri
    )
    assert inst.kind == "operation"
    assert inst.name == "Add"
    assert inst.parameter[0].documentation == (
        "Resource containing content to add. See [Operations for "
        "Large Resources](operations-for-large-resources.html)."
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "additions"
    assert inst.parameter[0].type == "Resource"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "Resource containing content added. See [Operations for Large"
        " Resources](operations-for-large-resources.html)."
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "return"
    assert inst.parameter[1].type == "Resource"
    assert inst.parameter[1].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Resource"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Add to an array in a large resource"
    assert inst.type is False
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/OperationDefinition/Resource-add"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_operationdefinition_6(base_settings):
    """No. 6 tests collection for OperationDefinition.
    Test File: operation-resource-add.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-resource-add.json"
    inst = operationdefinition.OperationDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "OperationDefinition" == inst.get_resource_type()

    impl_operationdefinition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_6(inst2)


def impl_operationdefinition_7(inst):
    assert inst.affectsState is False
    assert inst.code == "apply"
    assert inst.comment == (
        "The result of this operation is a Specimen resource based on"
        " the definition of the specimen as described in the "
        "SpecimenDefinition resource and the supplied parameters."
    )
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "The apply operation applies a SpecimenDefinition in a given "
        "context to create a Specimen resource instance"
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[0].valueInteger == 1
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "SpecimenDefinition-apply"
    assert inst.instance is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unstats.un.org/unsd/methods/m49/m49.htm"}
        ).valueUri
    )
    assert inst.kind == "operation"
    assert inst.name == "Apply"
    assert inst.parameter[0].documentation == (
        "The specimen definition to be applied. If the operation is "
        "invoked at the instance level, this parameter is not "
        "allowed; if the operation is invoked at the type level, this"
        " parameter is required"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "specimenDefinition"
    assert inst.parameter[0].scope[0] == "type"
    assert inst.parameter[0].type == "SpecimenDefinition"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].max == "*"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "subject"
    assert inst.parameter[1].searchType == "reference"
    assert inst.parameter[1].type == "string"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "The practitioner (or practitioner role) that is collecting " "the specimen"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "collector"
    assert inst.parameter[2].searchType == "reference"
    assert inst.parameter[2].type == "string"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
        "The type of user initiating the request, e.g. patient, "
        "healthcare provider, or specific type of healthcare provider"
        " (physician, nurse, etc.)"
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "userType"
    assert inst.parameter[3].type == "CodeableConcept"
    assert inst.parameter[3].use == "in"
    assert (
        inst.parameter[4].documentation
        == "Preferred language of the person using the system"
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "userLanguage"
    assert inst.parameter[4].type == "CodeableConcept"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "userTaskContext"
    assert inst.parameter[5].type == "CodeableConcept"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].documentation == (
        "The current setting of the request (inpatient, outpatient, " "etc.)"
    )
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "setting"
    assert inst.parameter[6].type == "CodeableConcept"
    assert inst.parameter[6].use == "in"
    assert (
        inst.parameter[7].documentation
        == "Additional detail about the setting of the request, if any"
    )
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "settingContext"
    assert inst.parameter[7].type == "CodeableConcept"
    assert inst.parameter[7].use == "in"
    assert inst.parameter[8].documentation == (
        "The Specimen resource that is the result of applying the "
        "specimen definition"
    )
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 1
    assert inst.parameter[8].name == "return"
    assert inst.parameter[8].type == "Specimen"
    assert inst.parameter[8].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "SpecimenDefinition"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Apply"
    assert inst.type is True
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/OperationDefinition/SpecimenDefinition-apply"
            }
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_operationdefinition_7(base_settings):
    """No. 7 tests collection for OperationDefinition.
    Test File: operation-specimendefinition-apply.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-specimendefinition-apply.json"
    )
    inst = operationdefinition.OperationDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "OperationDefinition" == inst.get_resource_type()

    impl_operationdefinition_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_7(inst2)


def impl_operationdefinition_8(inst):
    assert inst.affectsState is False
    assert inst.code == "expand"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[0].valueInteger == 5
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueCode == "normative"
    assert inst.id == "ValueSet-expand"
    assert inst.instance is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unstats.un.org/unsd/methods/m49/m49.htm"}
        ).valueUri
    )
    assert inst.kind == "operation"
    assert inst.name == "Expand"
    assert inst.parameter[0].documentation == (
        "A canonical reference to a value set. The server must know "
        "the value set (e.g. it is defined explicitly in the server's"
        " value sets, or it is defined implicitly by some code system"
        " known to the server"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "url"
    assert inst.parameter[0].scope[0] == "type"
    assert inst.parameter[0].type == "uri"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The value set is provided directly as part of the request. "
        "Servers may choose not to accept value sets in this fashion"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "valueSet"
    assert inst.parameter[1].scope[0] == "type"
    assert inst.parameter[1].type == "ValueSet"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "valueSetVersion"
    assert inst.parameter[2].scope[0] == "type"
    assert inst.parameter[2].type == "string"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "context"
    assert inst.parameter[3].type == "uri"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "contextDirection"
    assert inst.parameter[4].type == "code"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "filter"
    assert inst.parameter[5].type == "string"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "date"
    assert inst.parameter[6].type == "dateTime"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].documentation == (
        "Paging support - where to start if a subset is desired "
        "(default = 0). Offset is number of records (not number of "
        "pages)"
    )
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "offset"
    assert inst.parameter[7].type == "integer"
    assert inst.parameter[7].use == "in"
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "count"
    assert inst.parameter[8].type == "integer"
    assert inst.parameter[8].use == "in"
    assert inst.parameter[9].documentation == (
        "Controls whether concept designations are to be included or "
        "excluded in value set expansions"
    )
    assert inst.parameter[9].max == "1"
    assert inst.parameter[9].min == 0
    assert inst.parameter[9].name == "includeDesignations"
    assert inst.parameter[9].type == "boolean"
    assert inst.parameter[9].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "ValueSet"
    assert inst.status == "active"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Value Set Expansion"
    assert inst.type is True
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/OperationDefinition/ValueSet-expand"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_operationdefinition_8(base_settings):
    """No. 8 tests collection for OperationDefinition.
    Test File: operation-valueset-expand.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-valueset-expand.json"
    inst = operationdefinition.OperationDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "OperationDefinition" == inst.get_resource_type()

    impl_operationdefinition_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_8(inst2)


def impl_operationdefinition_9(inst):
    assert inst.affectsState is True
    assert inst.code == "meta-add"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.description == (
        "This operation takes a meta, and adds the profiles, tags, "
        "and security labels found in it to the nominated resource"
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[0].valueInteger == 3
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Resource-meta-add"
    assert inst.instance is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unstats.un.org/unsd/methods/m49/m49.htm"}
        ).valueUri
    )
    assert inst.kind == "operation"
    assert inst.name == "MetaAdd"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "meta"
    assert inst.parameter[0].type == "Meta"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == "Resulting meta for the resource"
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "return"
    assert inst.parameter[1].type == "Meta"
    assert inst.parameter[1].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Resource"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Add profiles, tags, and security labels to a resource"
    assert inst.type is False
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/OperationDefinition/Resource-meta-add"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_operationdefinition_9(base_settings):
    """No. 9 tests collection for OperationDefinition.
    Test File: operation-resource-meta-add.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-resource-meta-add.json"
    inst = operationdefinition.OperationDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "OperationDefinition" == inst.get_resource_type()

    impl_operationdefinition_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_9(inst2)


def impl_operationdefinition_10(inst):
    assert inst.affectsState is False
    assert inst.code == "everything"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert (
        inst.extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            }
        ).valueUri
    )
    assert inst.extension[0].valueInteger == 2
    assert (
        inst.extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            }
        ).valueUri
    )
    assert inst.extension[1].valueCode == "trial-use"
    assert inst.id == "Encounter-everything"
    assert inst.instance is True
    assert inst.jurisdiction[0].coding[0].code == "001"
    assert inst.jurisdiction[0].coding[0].display == "World"
    assert (
        inst.jurisdiction[0].coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://unstats.un.org/unsd/methods/m49/m49.htm"}
        ).valueUri
    )
    assert inst.kind == "operation"
    assert inst.name == "Everything"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "_since"
    assert inst.parameter[0].type == "instant"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "One or more parameters, each containing one or more comma-"
        "delimited FHIR resource types to include in the return "
        "resources. In the absense of any specified types, the server"
        " returns all resource types"
    )
    assert inst.parameter[1].max == "*"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "_type"
    assert inst.parameter[1].type == "code"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "See discussion below on the utility of paging through the "
        "results of the $everything operation"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "_count"
    assert inst.parameter[2].type == "integer"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == 'The bundle type is "searchset"'
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 1
    assert inst.parameter[3].name == "return"
    assert inst.parameter[3].type == "Bundle"
    assert inst.parameter[3].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Encounter"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "extensions"
    assert inst.title == "Fetch Encounter Record"
    assert inst.type is False
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/OperationDefinition/Encounter-everything"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_operationdefinition_10(base_settings):
    """No. 10 tests collection for OperationDefinition.
    Test File: operation-encounter-everything.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-encounter-everything.json"
    )
    inst = operationdefinition.OperationDefinition.model_validate_json(
        filename.read_bytes()
    )
    assert "OperationDefinition" == inst.get_resource_type()

    impl_operationdefinition_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_10(inst2)
