# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import operationdefinition


def impl_operationdefinition_1(inst):
    assert inst.code == "data-requirements"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == (
        "The data-requirements operation aggregates and returns the "
        "parameters and data requirements for the measure and all its"
        " dependencies as a single module definition"
    )
    assert inst.id == "Measure-data-requirements"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Data Requirements"
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
    assert inst.text.status == "generated"
    assert inst.type is False
    assert inst.url == (
        "http://hl7.org/fhir/OperationDefinition/Measure-data-" "requirements"
    )


def test_operationdefinition_1(base_settings):
    """No. 1 tests collection for OperationDefinition.
    Test File: operation-measure-data-requirements.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-measure-data-requirements.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_1(inst2)


def impl_operationdefinition_2(inst):
    assert inst.code == "translate"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.id == "ConceptMap-translate"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Concept Translation"
    assert inst.parameter[0].documentation == (
        "The code that is to be translated. If a code is provided, a "
        "system must be provided"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "code"
    assert inst.parameter[0].type == "code"
    assert inst.parameter[0].use == "in"
    assert (
        inst.parameter[1].documentation
        == "The system for the code that is to be translated"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "system"
    assert inst.parameter[1].type == "uri"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "The version of the system, if one was provided in the source" " data"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "version"
    assert inst.parameter[2].type == "string"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "source"
    assert inst.parameter[3].type == "uri"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == "A coding to translate"
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "coding"
    assert inst.parameter[4].type == "Coding"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == (
        "A full codeableConcept to validate. The server can translate"
        " any of the coding values (e.g. existing translations) as it"
        " chooses"
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "codeableConcept"
    assert inst.parameter[5].type == "CodeableConcept"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "target"
    assert inst.parameter[6].type == "uri"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "targetsystem"
    assert inst.parameter[7].type == "uri"
    assert inst.parameter[7].use == "in"
    assert (
        inst.parameter[8].documentation
        == "Another element that may help produce the correct mapping"
    )
    assert inst.parameter[8].max == "*"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "dependency"
    assert inst.parameter[8].part[0].documentation == "The element for this dependency"
    assert inst.parameter[8].part[0].max == "1"
    assert inst.parameter[8].part[0].min == 0
    assert inst.parameter[8].part[0].name == "element"
    assert inst.parameter[8].part[0].type == "uri"
    assert inst.parameter[8].part[0].use == "in"
    assert inst.parameter[8].part[1].documentation == "The value for this dependency"
    assert inst.parameter[8].part[1].max == "1"
    assert inst.parameter[8].part[1].min == 0
    assert inst.parameter[8].part[1].name == "concept"
    assert inst.parameter[8].part[1].type == "CodeableConcept"
    assert inst.parameter[8].part[1].use == "in"
    assert inst.parameter[8].use == "in"
    assert inst.parameter[9].documentation == (
        "if this is true, then the operation should return all the "
        "codes that might be mapped to this code. This parameter "
        "reverses the meaning of the source and target parameters"
    )
    assert inst.parameter[9].max == "1"
    assert inst.parameter[9].min == 0
    assert inst.parameter[9].name == "reverse"
    assert inst.parameter[9].type == "boolean"
    assert inst.parameter[9].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "ConceptMap"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/ConceptMap-translate"


def test_operationdefinition_2(base_settings):
    """No. 2 tests collection for OperationDefinition.
    Test File: operation-conceptmap-translate.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-conceptmap-translate.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_2(inst2)


def impl_operationdefinition_3(inst):
    assert inst.code == "expand"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.id == "ValueSet-expand"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Value Set Expansion"
    assert inst.parameter[0].documentation == (
        "A canonical url for a value set. The server must know the "
        "value set (e.g. it is defined explicitly in the server's "
        "value sets, or it is defined implicitly by some code system "
        "known to the server"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "url"
    assert inst.parameter[0].type == "uri"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The value set is provided directly as part of the request. "
        "Servers may choose not to accept value sets in this fashion"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "valueSet"
    assert inst.parameter[1].type == "ValueSet"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "context"
    assert inst.parameter[2].type == "uri"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "filter"
    assert inst.parameter[3].type == "string"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "profile"
    assert inst.parameter[4].type == "uri"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "date"
    assert inst.parameter[5].type == "dateTime"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].documentation == (
        "Paging support - where to start if a subset is desired "
        "(default = 0). Offset is number of records (not number of "
        "pages)"
    )
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "offset"
    assert inst.parameter[6].type == "integer"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "count"
    assert inst.parameter[7].type == "integer"
    assert inst.parameter[7].use == "in"
    assert inst.parameter[8].documentation == (
        "Controls whether concept designations are to be included or "
        "excluded in value set expansions. Overrides the value in the"
        " expansion profile if there is one"
    )
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "includeDesignations"
    assert inst.parameter[8].type == "boolean"
    assert inst.parameter[8].use == "in"
    assert inst.parameter[9].documentation == (
        "Controls whether the value set definition is included or "
        "excluded in value set expansions. Overrides the value in the"
        " expansion profile if there is one"
    )
    assert inst.parameter[9].max == "1"
    assert inst.parameter[9].min == 0
    assert inst.parameter[9].name == "includeDefinition"
    assert inst.parameter[9].type == "boolean"
    assert inst.parameter[9].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "ValueSet"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/ValueSet-expand"


def test_operationdefinition_3(base_settings):
    """No. 3 tests collection for OperationDefinition.
    Test File: operation-valueset-expand.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-valueset-expand.json"
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_3(inst2)


def impl_operationdefinition_4(inst):
    assert inst.code == "populate"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.id == "Questionnaire-populate"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Populate Questionnaire"
    assert inst.parameter[0].documentation == (
        "A logical questionnaire identifier (i.e. "
        "''Questionnaire.identifier''). The server must know the "
        "questionnaire or be able to retrieve it from other known "
        "repositories."
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "identifier"
    assert inst.parameter[0].type == "uri"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The [Questionnaire](questionnaire.html) is provided directly"
        " as part of the request. Servers may choose not to accept "
        "questionnaires in this fashion"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "questionnaire"
    assert inst.parameter[1].type == "Questionnaire"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "questionnaireRef"
    assert (
        inst.parameter[2].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Questionnaire"
    )
    assert inst.parameter[2].type == "Reference"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 1
    assert inst.parameter[3].name == "subject"
    assert inst.parameter[3].type == "Reference"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].max == "*"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "content"
    assert inst.parameter[4].type == "Reference"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == (
        "If specified and set to 'true' (and the server is capable), "
        "the server should use what resources and other knowledge it "
        "has about the referenced subject when pre-populating answers"
        " to questions."
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "local"
    assert inst.parameter[5].type == "boolean"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].documentation == (
        "The partially (or fully)-populated set of answers for the "
        "specified Questionnaire"
    )
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 1
    assert inst.parameter[6].name == "questionnaire"
    assert inst.parameter[6].type == "QuestionnaireResponse"
    assert inst.parameter[6].use == "out"
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "issues"
    assert inst.parameter[7].type == "OperationOutcome"
    assert inst.parameter[7].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Questionnaire"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is True
    assert inst.url == (
        "http://hl7.org/fhir/OperationDefinition/Questionnaire-" "populate"
    )


def test_operationdefinition_4(base_settings):
    """No. 4 tests collection for OperationDefinition.
    Test File: operation-questionnaire-populate.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-questionnaire-populate.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_4(inst2)


def impl_operationdefinition_5(inst):
    assert inst.code == "meta-add"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.id == "Resource-meta-add"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Add profiles, tags, and security labels to a resource"
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
    assert inst.text.status == "generated"
    assert inst.type is False
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Resource-meta-add"


def test_operationdefinition_5(base_settings):
    """No. 5 tests collection for OperationDefinition.
    Test File: operation-resource-meta-add.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-resource-meta-add.json"
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_5(inst2)


def impl_operationdefinition_6(inst):
    assert inst.code == "everything"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.id == "Encounter-everything"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Fetch Encounter Record"
    assert inst.parameter[0].documentation == 'The bundle type is "searchset"'
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "return"
    assert inst.parameter[0].type == "Bundle"
    assert inst.parameter[0].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Encounter"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is False
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Encounter-everything"


def test_operationdefinition_6(base_settings):
    """No. 6 tests collection for OperationDefinition.
    Test File: operation-encounter-everything.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-encounter-everything.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_6(inst2)


def impl_operationdefinition_7(inst):
    assert inst.code == "evaluate"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == (
        "The evaluate operation requests clinical decision support "
        "guidance based on a specific decision support module"
    )
    assert inst.id == "ServiceDefinition-evaluate"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Evaluate"
    assert (
        inst.parameter[0].documentation
        == "An optional client-provided identifier to track the request."
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "requestId"
    assert inst.parameter[0].type == "id"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "evaluateAtDateTime"
    assert inst.parameter[1].type == "dateTime"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "The input parameters for a request, if any. These parameters"
        " are defined by the module that is the target of the "
        "evaluation, and typically supply patient-independent "
        "information to the module."
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "inputParameters"
    assert inst.parameter[2].type == "Parameters"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
        "The input data for the request. These data are defined by "
        "the data requirements of the module and typically provide "
        "patient-dependent information."
    )
    assert inst.parameter[3].max == "*"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "inputData"
    assert inst.parameter[3].type == "Any"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == "The patient in context, if any."
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "patient"
    assert (
        inst.parameter[4].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Patient"
    )
    assert inst.parameter[4].type == "Reference"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == "The encounter in context, if any."
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "encounter"
    assert (
        inst.parameter[5].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Encounter"
    )
    assert inst.parameter[5].type == "Reference"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].documentation == "The organization initiating the request."
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "initiatingOrganization"
    assert (
        inst.parameter[6].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Organization"
    )
    assert inst.parameter[6].type == "Reference"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].documentation == "The person initiating the request."
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "initiatingPerson"
    assert inst.parameter[7].type == "Reference"
    assert inst.parameter[7].use == "in"
    assert inst.parameter[8].documentation == (
        "The type of user initiating the request, e.g. patient, "
        "healthcare provider, or specific type of healthcare provider"
        " (physician, nurse, etc.)."
    )
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "userType"
    assert inst.parameter[8].type == "CodeableConcept"
    assert inst.parameter[8].use == "in"
    assert (
        inst.parameter[9].documentation
        == "Preferred language of the person using the system."
    )
    assert inst.parameter[9].max == "1"
    assert inst.parameter[9].min == 0
    assert inst.parameter[9].name == "userLanguage"
    assert inst.parameter[9].type == "CodeableConcept"
    assert inst.parameter[9].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "ServiceDefinition"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is False
    assert inst.url == (
        "http://hl7.org/fhir/OperationDefinition/ServiceDefinition-" "evaluate"
    )


def test_operationdefinition_7(base_settings):
    """No. 7 tests collection for OperationDefinition.
    Test File: operation-servicedefinition-evaluate.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-servicedefinition-evaluate.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_7(inst2)


def impl_operationdefinition_8(inst):
    assert inst.code == "meta"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.id == "Resource-meta"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Access a list of profiles, tags, and security labels"
    assert inst.parameter[0].documentation == "The meta returned by the operation"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "return"
    assert inst.parameter[0].type == "Meta"
    assert inst.parameter[0].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Resource"
    assert inst.status == "draft"
    assert inst.system is True
    assert inst.text.status == "generated"
    assert inst.type is True
    assert inst.url == "http://hl7.org/fhir/OperationDefinition/Resource-meta"


def test_operationdefinition_8(base_settings):
    """No. 8 tests collection for OperationDefinition.
    Test File: operation-resource-meta.json
    """
    filename = base_settings["unittest_data_dir"] / "operation-resource-meta.json"
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_8(inst2)


def impl_operationdefinition_9(inst):
    assert inst.code == "data-requirements"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == (
        "The data-requirements operation aggregates and returns the "
        "parameters and data requirements for the service module and "
        "all its dependencies as a single module definition library."
    )
    assert inst.id == "ServiceDefinition-data-requirements"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Data Requirements"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "evaluateAtDateTime"
    assert inst.parameter[0].type == "dateTime"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The result of the requirements gathering is a module-"
        "definition Library that describes the aggregate parameters, "
        "data requirements, and dependencies of the service."
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "return"
    assert inst.parameter[1].type == "Library"
    assert inst.parameter[1].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "ServiceDefinition"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is False
    assert inst.url == (
        "http://hl7.org/fhir/OperationDefinition/ServiceDefinition-" "data-requirements"
    )


def test_operationdefinition_9(base_settings):
    """No. 9 tests collection for OperationDefinition.
    Test File: operation-servicedefinition-data-requirements.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operation-servicedefinition-data-requirements.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_9(inst2)


def impl_operationdefinition_10(inst):
    assert inst.code == "evaluate-measure"
    assert inst.contact[0].telecom[0].system == "url"
    assert inst.contact[0].telecom[0].value == "http://hl7.org/fhir"
    assert inst.contact[0].telecom[1].system == "email"
    assert inst.contact[0].telecom[1].value == "fhir@lists.hl7.org"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.description == (
        "The evaluate-measure operation is used to invoke an eMeasure"
        " and obtain the results"
    )
    assert inst.id == "Measure-evaluate-measure"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Evaluate Measure"
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
        "The measure to evaluate. This parameter is only required "
        "when the operation is invoked on the resource type, it is "
        "not used when invoking the operation on a Measure instance"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "measure"
    assert (
        inst.parameter[2].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Measure"
    )
    assert inst.parameter[2].type == "Reference"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
        "The type of measure report, patient, patient-list, or "
        "population. If not specified, a default value of patient "
        "will be used if the patient parameter is supplied, "
        "otherwise, population will be used"
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "reportType"
    assert inst.parameter[3].type == "code"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == (
        "Patient to evaluate against. If not specified, the measure "
        "will be evaluated for all patients that meet the "
        "requirements of the measure. If specified, only the "
        "referenced patient will be evaluated"
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "patient"
    assert (
        inst.parameter[4].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Patient"
    )
    assert inst.parameter[4].type == "Reference"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == (
        "Practitioner to evaluate. If specified, the measure will be "
        "evaluated only for patients whose primary practitioner is "
        "the identified practitioner"
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "practitioner"
    assert (
        inst.parameter[5].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Practitioner"
    )
    assert inst.parameter[5].type == "Reference"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "lastReceivedOn"
    assert inst.parameter[6].type == "dateTime"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].documentation == (
        "The results of the measure calculation. See the "
        "MeasureReport resource for a complete description of the "
        "output of this operation"
    )
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 1
    assert inst.parameter[7].name == "return"
    assert inst.parameter[7].type == "MeasureReport"
    assert inst.parameter[7].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Measure"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is True
    assert inst.url == (
        "http://hl7.org/fhir/OperationDefinition/Measure-evaluate-" "measure"
    )


def test_operationdefinition_10(base_settings):
    """No. 10 tests collection for OperationDefinition.
    Test File: operation-measure-evaluate-measure.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operation-measure-evaluate-measure.json"
    )
    inst = operationdefinition.OperationDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "OperationDefinition" == inst.resource_type

    impl_operationdefinition_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "OperationDefinition" == data["resourceType"]

    inst2 = operationdefinition.OperationDefinition(**data)
    impl_operationdefinition_10(inst2)
