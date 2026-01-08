# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from .. import operationdefinition
from .fixtures import ExternalValidatorModel


def impl_operationdefinition_1(inst):
    assert inst.code == "everything"
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
    assert inst.id == "Patient-everything"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Fetch Patient Record"
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "start"
    assert inst.parameter[0].type == "date"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "end"
    assert inst.parameter[1].type == "date"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == 'The bundle type is "searchset"'
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 1
    assert inst.parameter[2].name == "return"
    assert inst.parameter[2].type == "Bundle"
    assert inst.parameter[2].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Patient"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is True
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/OperationDefinition/Patient-everything"}
        ).valueUri
    )


def test_operationdefinition_1(base_settings):
    """No. 1 tests collection for OperationDefinition.
    Test File: operationdefinition-operation-patient-everything(Patient-everything).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationdefinition-operation-patient-everything(Patient-everything).json"
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
    assert inst.code == "find"
    assert inst.comment == (
        "Note that servers may support searching by a functional "
        "list, and not support this operation that allows clients to "
        "find the list directly"
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
    assert inst.id == "List-find"
    assert inst.instance is False
    assert inst.kind == "operation"
    assert inst.name == "Find a functional list"
    assert inst.parameter[0].documentation == (
        "The id of a patient resource located on the server on which "
        "this operation is executed"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "patient"
    assert inst.parameter[0].type == "id"
    assert inst.parameter[0].use == "in"
    assert (
        inst.parameter[1].documentation
        == "The code for the functional list that is being found"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 1
    assert inst.parameter[1].name == "name"
    assert inst.parameter[1].type == "code"
    assert inst.parameter[1].use == "in"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "List"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is True
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/OperationDefinition/List-find"}
        ).valueUri
    )


def test_operationdefinition_2(base_settings):
    """No. 2 tests collection for OperationDefinition.
    Test File: operationdefinition-operation-list-find(List-find).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationdefinition-operation-list-find(List-find).json"
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
    assert inst.code == "questionnaire"
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
    assert inst.id == "StructureDefinition-questionnaire"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Build Questionnaire"
    assert inst.parameter[0].documentation == (
        "A logical profile identifier (i.e. "
        "'StructureDefinition.identifier''). The server must know the"
        " profile or be able to retrieve it from other known "
        "repositories."
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "identifier"
    assert inst.parameter[0].type == "uri"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The [StructureDefinition](structuredefinition.html) is "
        "provided directly as part of the request. Servers may choose"
        " not to accept profiles in this fashion"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "profile"
    assert inst.parameter[1].searchType == "token"
    assert inst.parameter[1].type == "string"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "The profile's official URL (i.e. 'StructureDefinition.url')."
        " The server must know the profile or be able to retrieve it "
        "from other known repositories."
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "url"
    assert inst.parameter[2].type == "uri"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == (
        "If true, the questionnaire will only include those elements "
        "marked as \"mustSupport='true'\" in the StructureDefinition."
    )
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "supportedOnly"
    assert inst.parameter[3].type == "boolean"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == (
        "The questionnaire form generated based on the " "StructureDefinition."
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 1
    assert inst.parameter[4].name == "return"
    assert inst.parameter[4].type == "Questionnaire"
    assert inst.parameter[4].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "StructureDefinition"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is True
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/OperationDefinition/StructureDefinition-questionnaire"
            }
        ).valueUri
    )


def test_operationdefinition_3(base_settings):
    """No. 3 tests collection for OperationDefinition.
    Test File: operationdefinition-operation-structuredefinition-questionnaire(StructureDefinition-questionnaire).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationdefinition-operation-structuredefinition-questionnaire(StructureDefinition-questionnaire).json"
    )
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
    assert inst.code == "populatelink"
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
    assert inst.id == "Questionnaire-populatelink"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Generate a link to a Questionnaire completion webpage"
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
    assert inst.parameter[3].max == "*"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "content"
    assert inst.parameter[3].type == "Reference"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == (
        "If specified and set to 'true' (and the server is capable), "
        "the server should use what resources and other knowledge it "
        "has about the referenced subject when pre-populating answers"
        " to questions."
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "local"
    assert inst.parameter[4].type == "boolean"
    assert inst.parameter[4].use == "in"
    assert inst.parameter[5].documentation == (
        "The URL for the web form  that supports capturing the "
        "information defined by questionnaire, possibly partially (or"
        " fully)-populated with a set of answers for the specified "
        "Questionnaire"
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 1
    assert inst.parameter[5].name == "link"
    assert inst.parameter[5].type == "uri"
    assert inst.parameter[5].use == "out"
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "issues"
    assert inst.parameter[6].type == "OperationOutcome"
    assert inst.parameter[6].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "Questionnaire"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is True
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/OperationDefinition/Questionnaire-populatelink"
            }
        ).valueUri
    )


def test_operationdefinition_4(base_settings):
    """No. 4 tests collection for OperationDefinition.
    Test File: operationdefinition-operation-questionnaire-populatelink(Questionnaire-populatelink).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationdefinition-operation-questionnaire-populatelink(Questionnaire-populatelink).json"
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
    assert inst.code == "apply"
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
        "The apply operation realizes a definition in a specific " "context"
    )
    assert inst.id == "ActivityDefinition-apply"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Apply"
    assert (
        inst.parameter[0].documentation
        == "The patient that is the target of the activity to be applied"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "patient"
    assert (
        inst.parameter[0].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Patient"
    )
    assert inst.parameter[0].type == "Reference"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == "The encounter in context, if any"
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "encounter"
    assert (
        inst.parameter[1].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Encounter"
    )
    assert inst.parameter[1].type == "Reference"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == "The practitioner in context"
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "practitioner"
    assert (
        inst.parameter[2].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Practitioner"
    )
    assert inst.parameter[2].type == "Reference"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == "The organization in context"
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 0
    assert inst.parameter[3].name == "organization"
    assert (
        inst.parameter[3].profile.reference
        == "http://hl7.org/fhir/StructureDefinition/Organization"
    )
    assert inst.parameter[3].type == "Reference"
    assert inst.parameter[3].use == "in"
    assert inst.parameter[4].documentation == (
        "The type of user initiating the request, e.g. patient, "
        "healthcare provider, or specific type of healthcare provider"
        " (physician, nurse, etc.)"
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "userType"
    assert inst.parameter[4].type == "CodeableConcept"
    assert inst.parameter[4].use == "in"
    assert (
        inst.parameter[5].documentation
        == "Preferred language of the person using the system"
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "userLanguage"
    assert inst.parameter[5].type == "CodeableConcept"
    assert inst.parameter[5].use == "in"
    assert inst.parameter[6].max == "1"
    assert inst.parameter[6].min == 0
    assert inst.parameter[6].name == "userTaskContext"
    assert inst.parameter[6].type == "CodeableConcept"
    assert inst.parameter[6].use == "in"
    assert inst.parameter[7].documentation == (
        "The current setting of the request (inpatient, outpatient, " "etc)"
    )
    assert inst.parameter[7].max == "1"
    assert inst.parameter[7].min == 0
    assert inst.parameter[7].name == "setting"
    assert inst.parameter[7].type == "CodeableConcept"
    assert inst.parameter[7].use == "in"
    assert (
        inst.parameter[8].documentation
        == "Additional detail about the setting of the request, if any"
    )
    assert inst.parameter[8].max == "1"
    assert inst.parameter[8].min == 0
    assert inst.parameter[8].name == "settingContext"
    assert inst.parameter[8].type == "CodeableConcept"
    assert inst.parameter[8].use == "in"
    assert (
        inst.parameter[9].documentation
        == "The resource that is the result of applying the definition"
    )
    assert inst.parameter[9].max == "1"
    assert inst.parameter[9].min == 1
    assert inst.parameter[9].name == "return"
    assert inst.parameter[9].type == "Any"
    assert inst.parameter[9].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "ActivityDefinition"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is False
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/OperationDefinition/ActivityDefinition-apply"
            }
        ).valueUri
    )


def test_operationdefinition_5(base_settings):
    """No. 5 tests collection for OperationDefinition.
    Test File: operationdefinition-operation-activitydefinition-apply(ActivityDefinition-apply).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationdefinition-operation-activitydefinition-apply(ActivityDefinition-apply).json"
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
    assert inst.code == "expand"
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
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/OperationDefinition/ValueSet-expand"}
        ).valueUri
    )


def test_operationdefinition_6(base_settings):
    """No. 6 tests collection for OperationDefinition.
    Test File: operationdefinition-operation-valueset-expand(ValueSet-expand).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationdefinition-operation-valueset-expand(ValueSet-expand).json"
    )
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
    assert inst.code == "meta-delete"
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
        "This operation takes a meta, and deletes the profiles, tags,"
        " and security labels found in it from the nominated "
        "resource.   This operation can also be used on historical "
        "entries"
    )
    assert inst.id == "Resource-meta-delete"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Delete profiles, tags, and security labels for a resource"
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
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/OperationDefinition/Resource-meta-delete"}
        ).valueUri
    )


def test_operationdefinition_7(base_settings):
    """No. 7 tests collection for OperationDefinition.
    Test File: operationdefinition-operation-resource-meta-delete(Resource-meta-delete).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationdefinition-operation-resource-meta-delete(Resource-meta-delete).json"
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
    assert inst.code == "data-requirements"
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
        "The data-requirements operation aggregates and returns the "
        "parameters and data requirements for the activity definition"
        " and all its dependencies as a single module definition "
        "library"
    )
    assert inst.id == "ActivityDefinition-data-requirements"
    assert inst.instance is True
    assert inst.kind == "operation"
    assert inst.name == "Data Requirements"
    assert inst.parameter[0].documentation == (
        "The result of the requirements gathering represented as a "
        "module-definition Library that describes the aggregate "
        "parameters, data requirements, and dependencies of the "
        "activity definition"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "return"
    assert inst.parameter[0].type == "Library"
    assert inst.parameter[0].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "ActivityDefinition"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is False
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/OperationDefinition/ActivityDefinition-data-requirements"
            }
        ).valueUri
    )


def test_operationdefinition_8(base_settings):
    """No. 8 tests collection for OperationDefinition.
    Test File: operationdefinition-operation-activitydefinition-data-requirements(ActivityDefinition-data-requirements).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationdefinition-operation-activitydefinition-data-requirements(ActivityDefinition-data-requirements).json"
    )
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
    assert inst.code == "closure"
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
    assert inst.id == "ConceptMap-closure"
    assert inst.instance is False
    assert inst.kind == "operation"
    assert inst.name == "Closure Table Maintenance"
    assert inst.parameter[0].documentation == (
        "The name that defines the particular context for the "
        "subsumption based closure table"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 1
    assert inst.parameter[0].name == "name"
    assert inst.parameter[0].type == "string"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == "Concepts to add to the closure table"
    assert inst.parameter[1].max == "*"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "concept"
    assert inst.parameter[1].type == "Coding"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "A request to resynchronise - request to send all new entries"
        " since the nominated version was sent by the server"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "version"
    assert inst.parameter[2].type == "id"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 1
    assert inst.parameter[3].name == "return"
    assert inst.parameter[3].type == "ConceptMap"
    assert inst.parameter[3].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "ConceptMap"
    assert inst.status == "draft"
    assert inst.system is True
    assert inst.text.status == "generated"
    assert inst.type is False
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/OperationDefinition/ConceptMap-closure"}
        ).valueUri
    )


def test_operationdefinition_9(base_settings):
    """No. 9 tests collection for OperationDefinition.
    Test File: operationdefinition-operation-conceptmap-closure(ConceptMap-closure).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationdefinition-operation-conceptmap-closure(ConceptMap-closure).json"
    )
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
    assert inst.code == "conforms"
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
    assert inst.id == "CapabilityStatement-conforms"
    assert inst.instance is False
    assert inst.kind == "operation"
    assert inst.name == "Test if a server implements a client's required operations"
    assert inst.parameter[0].documentation == (
        "The canonical URL for the left-hand system's capability " "statement"
    )
    assert inst.parameter[0].max == "1"
    assert inst.parameter[0].min == 0
    assert inst.parameter[0].name == "left"
    assert inst.parameter[0].type == "uri"
    assert inst.parameter[0].use == "in"
    assert inst.parameter[1].documentation == (
        "The canonical URL for the right-hand system's capability " "statement"
    )
    assert inst.parameter[1].max == "1"
    assert inst.parameter[1].min == 0
    assert inst.parameter[1].name == "right"
    assert inst.parameter[1].type == "uri"
    assert inst.parameter[1].use == "in"
    assert inst.parameter[2].documentation == (
        "What kind of comparison to perform - server to server, or "
        "client to server (use the codes 'server/server' or "
        "'client/server')"
    )
    assert inst.parameter[2].max == "1"
    assert inst.parameter[2].min == 0
    assert inst.parameter[2].name == "mode"
    assert inst.parameter[2].type == "code"
    assert inst.parameter[2].use == "in"
    assert inst.parameter[3].documentation == "Outcome of the CapabilityStatement test"
    assert inst.parameter[3].max == "1"
    assert inst.parameter[3].min == 1
    assert inst.parameter[3].name == "issues"
    assert inst.parameter[3].type == "OperationOutcome"
    assert inst.parameter[3].use == "out"
    assert inst.parameter[4].documentation == (
        "The intersection of the functionality described by the "
        "CapabilityStatement resources"
    )
    assert inst.parameter[4].max == "1"
    assert inst.parameter[4].min == 0
    assert inst.parameter[4].name == "union"
    assert inst.parameter[4].type == "CapabilityStatement"
    assert inst.parameter[4].use == "out"
    assert inst.parameter[5].documentation == (
        "The union of the functionality described by the "
        "CapabilityStatement resources"
    )
    assert inst.parameter[5].max == "1"
    assert inst.parameter[5].min == 0
    assert inst.parameter[5].name == "intersection"
    assert inst.parameter[5].type == "CapabilityStatement"
    assert inst.parameter[5].use == "out"
    assert inst.publisher == "HL7 (FHIR Project)"
    assert inst.resource[0] == "CapabilityStatement"
    assert inst.status == "draft"
    assert inst.system is False
    assert inst.text.status == "generated"
    assert inst.type is True
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/OperationDefinition/CapabilityStatement-conforms"
            }
        ).valueUri
    )


def test_operationdefinition_10(base_settings):
    """No. 10 tests collection for OperationDefinition.
    Test File: operationdefinition-operation-capabilitystatement-conforms(CapabilityStatement-conforms).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "operationdefinition-operation-capabilitystatement-conforms(CapabilityStatement-conforms).json"
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
