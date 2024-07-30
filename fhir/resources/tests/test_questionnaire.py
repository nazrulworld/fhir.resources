# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from .. import questionnaire
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_questionnaire_1(inst):
    assert inst.contained[0].id == "vs2"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert inst.id == "qgen-Person1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.item[0].item[0].linkId == "Person-display"
    assert inst.item[0].item[0].type == "display"
    assert (
        inst.item[0].item[1].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[1].linkId == "Person-flyover"
    assert inst.item[0].item[1].text == (
        "Demographics and administrative information about a person "
        "independent of a specific health-related context."
    )
    assert inst.item[0].item[1].type == "display"
    assert (
        inst.item[0].item[2].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[2].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert (
        inst.item[0].item[2].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[2].item[0].linkId == "Person.id-flyover"
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "Person.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "Person.id"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].type == "group"
    assert (
        inst.item[0].item[3].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[3].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[3].item[0].linkId == "Person.meta-flyover"
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "Person.meta"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].text == "Metadata about the resource"
    assert inst.item[0].item[3].type == "group"
    assert (
        inst.item[0].item[4].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[4].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[4].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[4].item[0].linkId == "Person.implicitRules-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Person.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert (
        inst.item[0].item[4].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "Person.implicitRules"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert (
        inst.item[0].item[5].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[5].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert (
        inst.item[0].item[5].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[5].item[0].linkId == "Person.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].answerConstraint == "optionsOrType"
    assert inst.item[0].item[5].item[1].linkId == "Person.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "coding"
    assert inst.item[0].item[5].linkId == "Person.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert (
        inst.item[0].item[6].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[6].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[6].item[0].linkId == "Person.text-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Person.text"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert (
        inst.item[0].item[6].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[6].type == "group"
    assert (
        inst.item[0].item[7].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[7].item[0].linkId == "Person.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Person.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert (
        inst.item[0].item[8].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[8].item[0].linkId == "Person.extension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Person.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert (
        inst.item[0].item[9].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[9].item[0].linkId == "Person.modifierExtension-flyover"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "Person.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Person"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "A generic person record"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Patient Administration)"
    assert inst.status == "draft"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/Questionnaire/qgen-Person1"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_questionnaire_1(base_settings):
    """No. 1 tests collection for Questionnaire.
    Test File: person-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "person-questionnaire.json"
    inst = questionnaire.Questionnaire.model_validate_json(filename.read_bytes())
    assert "Questionnaire" == inst.get_resource_type()

    impl_questionnaire_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_1(inst2)


def impl_questionnaire_2(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.contained[3].id == "vs5"
    assert inst.contained[4].id == "vs6"
    assert inst.contained[5].id == "vs7"
    assert inst.contained[6].id == "vs8"
    assert inst.contained[7].id == "vs9"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert inst.id == "qgen-RequestOrchestration1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[0].linkId == "RequestOrchestration-flyover"
    assert inst.item[0].item[0].text == (
        "A set of related requests that can be used to capture "
        "intended activities that have inter-dependencies such as "
        '"give this medication after that one".'
    )
    assert inst.item[0].item[0].type == "display"
    assert (
        inst.item[0].item[1].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[1].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert (
        inst.item[0].item[1].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[1].item[0].linkId == "RequestOrchestration.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "RequestOrchestration.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "RequestOrchestration.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert (
        inst.item[0].item[2].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[2].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[2].item[0].linkId == "RequestOrchestration.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "RequestOrchestration.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert (
        inst.item[0].item[3].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[3].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[3].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].linkId
        == "RequestOrchestration.implicitRules-flyover"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert (
        inst.item[0].item[3].item[1].linkId
        == "RequestOrchestration.implicitRules.value"
    )
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "RequestOrchestration.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert (
        inst.item[0].item[4].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[4].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert (
        inst.item[0].item[4].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].linkId == "RequestOrchestration.language-flyover"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOrType"
    assert inst.item[0].item[4].item[1].linkId == "RequestOrchestration.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "RequestOrchestration.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert (
        inst.item[0].item[5].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[5].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[5].item[0].linkId == "RequestOrchestration.text-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "RequestOrchestration.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert (
        inst.item[0].item[6].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].linkId == "RequestOrchestration.contained-flyover"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "RequestOrchestration.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert (
        inst.item[0].item[7].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].linkId == "RequestOrchestration.extension-flyover"
    )
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "RequestOrchestration.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert (
        inst.item[0].item[8].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].linkId
        == "RequestOrchestration.modifierExtension-flyover"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "RequestOrchestration.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert (
        inst.item[0].item[9].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].extension[0].valueString == "Identifier"
    assert (
        inst.item[0].item[9].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].linkId == "RequestOrchestration.identifier-flyover"
    )
    assert inst.item[0].item[9].item[0].text == (
        "Allows a service to provide a unique, business identifier " "for the request."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert (
        inst.item[0].item[9].item[1].linkId == "RequestOrchestration.identifier.label"
    )
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert (
        inst.item[0].item[9].item[2].linkId == "RequestOrchestration.identifier.system"
    )
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert (
        inst.item[0].item[9].item[3].linkId == "RequestOrchestration.identifier.value"
    )
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "RequestOrchestration.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Business identifier"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "RequestOrchestration"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "A set of related requests"
    assert inst.item[0].type == "group"
    assert (
        inst.publisher == "Health Level Seven International (Clinical Decision Support)"
    )
    assert inst.status == "draft"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/Questionnaire/qgen-RequestOrchestration1"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_questionnaire_2(base_settings):
    """No. 2 tests collection for Questionnaire.
    Test File: requestorchestration-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "requestorchestration-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.model_validate_json(filename.read_bytes())
    assert "Questionnaire" == inst.get_resource_type()

    impl_questionnaire_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_2(inst2)


def impl_questionnaire_3(inst):
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert inst.id == "qgen-OperationOutcome1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.item[0].item[0].linkId == "OperationOutcome-display"
    assert inst.item[0].item[0].text == (
        "Can result from the failure of a REST call or be part of the"
        " response message returned from a request message."
    )
    assert inst.item[0].item[0].type == "display"
    assert (
        inst.item[0].item[1].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[1].linkId == "OperationOutcome-flyover"
    assert inst.item[0].item[1].text == (
        "A collection of error, warning, or information messages that"
        " result from a system action."
    )
    assert inst.item[0].item[1].type == "display"
    assert (
        inst.item[0].item[2].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[2].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert (
        inst.item[0].item[2].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[2].item[0].linkId == "OperationOutcome.id-flyover"
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "OperationOutcome.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "OperationOutcome.id"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].type == "group"
    assert (
        inst.item[0].item[3].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[3].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[3].item[0].linkId == "OperationOutcome.meta-flyover"
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "OperationOutcome.meta"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].text == "Metadata about the resource"
    assert inst.item[0].item[3].type == "group"
    assert (
        inst.item[0].item[4].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[4].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[4].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].linkId == "OperationOutcome.implicitRules-flyover"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "OperationOutcome.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert (
        inst.item[0].item[4].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "OperationOutcome.implicitRules"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert (
        inst.item[0].item[5].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[5].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert (
        inst.item[0].item[5].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[5].item[0].linkId == "OperationOutcome.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].answerConstraint == "optionsOrType"
    assert inst.item[0].item[5].item[1].linkId == "OperationOutcome.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "coding"
    assert inst.item[0].item[5].linkId == "OperationOutcome.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert (
        inst.item[0].item[6].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[6].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[6].item[0].linkId == "OperationOutcome.text-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "OperationOutcome.text"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert (
        inst.item[0].item[6].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[6].type == "group"
    assert (
        inst.item[0].item[7].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[7].item[0].linkId == "OperationOutcome.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "OperationOutcome.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert (
        inst.item[0].item[8].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[8].item[0].linkId == "OperationOutcome.extension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "OperationOutcome.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert (
        inst.item[0].item[9].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].linkId
        == "OperationOutcome.modifierExtension-flyover"
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "OperationOutcome.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "OperationOutcome"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Information about the success/failure of an action"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.status == "active"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/Questionnaire/qgen-OperationOutcome1"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_questionnaire_3(base_settings):
    """No. 3 tests collection for Questionnaire.
    Test File: operationoutcome-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operationoutcome-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.model_validate_json(filename.read_bytes())
    assert "Questionnaire" == inst.get_resource_type()

    impl_questionnaire_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_3(inst2)


def impl_questionnaire_4(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert inst.id == "qgen-EventDefinition1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[0].linkId == "EventDefinition-flyover"
    assert inst.item[0].item[0].text == (
        "The EventDefinition resource provides a reusable description"
        " of when a particular event can occur."
    )
    assert inst.item[0].item[0].type == "display"
    assert (
        inst.item[0].item[1].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[1].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert (
        inst.item[0].item[1].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[1].item[0].linkId == "EventDefinition.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "EventDefinition.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "EventDefinition.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert (
        inst.item[0].item[2].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[2].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[2].item[0].linkId == "EventDefinition.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "EventDefinition.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert (
        inst.item[0].item[3].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[3].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[3].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].linkId == "EventDefinition.implicitRules-flyover"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "EventDefinition.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "EventDefinition.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert (
        inst.item[0].item[4].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[4].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert (
        inst.item[0].item[4].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[4].item[0].linkId == "EventDefinition.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOrType"
    assert inst.item[0].item[4].item[1].linkId == "EventDefinition.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "EventDefinition.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert (
        inst.item[0].item[5].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[5].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[5].item[0].linkId == "EventDefinition.text-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "EventDefinition.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert (
        inst.item[0].item[6].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[6].item[0].linkId == "EventDefinition.contained-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "EventDefinition.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert (
        inst.item[0].item[7].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[7].item[0].linkId == "EventDefinition.extension-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "EventDefinition.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert (
        inst.item[0].item[8].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].linkId
        == "EventDefinition.modifierExtension-flyover"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "EventDefinition.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert (
        inst.item[0].item[9].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[9].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[9].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[9].item[0].linkId == "EventDefinition.url-flyover"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "EventDefinition.url.value"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == (
        "Canonical identifier for this event definition, represented "
        "as a URI (globally unique)"
    )
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].linkId == "EventDefinition.url"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "EventDefinition"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "A description of when an event can occur"
    assert inst.item[0].type == "group"
    assert (
        inst.publisher == "Health Level Seven International (Clinical Decision Support)"
    )
    assert inst.status == "draft"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/Questionnaire/qgen-EventDefinition1"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_questionnaire_4(base_settings):
    """No. 4 tests collection for Questionnaire.
    Test File: eventdefinition-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "eventdefinition-questionnaire.json"
    inst = questionnaire.Questionnaire.model_validate_json(filename.read_bytes())
    assert "Questionnaire" == inst.get_resource_type()

    impl_questionnaire_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_4(inst2)


def impl_questionnaire_5(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.contained[3].id == "vs5"
    assert inst.contained[4].id == "vs6"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert inst.id == "qgen-ActivityDefinition1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[0].linkId == "ActivityDefinition-flyover"
    assert inst.item[0].item[0].text == (
        "This resource allows for the definition of some activity to "
        "be performed, independent of a particular patient, "
        "practitioner, or other performance context."
    )
    assert inst.item[0].item[0].type == "display"
    assert (
        inst.item[0].item[1].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[1].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert (
        inst.item[0].item[1].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[1].item[0].linkId == "ActivityDefinition.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "ActivityDefinition.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "ActivityDefinition.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert (
        inst.item[0].item[2].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[2].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[2].item[0].linkId == "ActivityDefinition.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "ActivityDefinition.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert (
        inst.item[0].item[3].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[3].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[3].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].linkId
        == "ActivityDefinition.implicitRules-flyover"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert (
        inst.item[0].item[3].item[1].linkId == "ActivityDefinition.implicitRules.value"
    )
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "ActivityDefinition.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert (
        inst.item[0].item[4].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[4].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert (
        inst.item[0].item[4].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[4].item[0].linkId == "ActivityDefinition.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOrType"
    assert inst.item[0].item[4].item[1].linkId == "ActivityDefinition.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "ActivityDefinition.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert (
        inst.item[0].item[5].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[5].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[5].item[0].linkId == "ActivityDefinition.text-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "ActivityDefinition.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert (
        inst.item[0].item[6].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[6].item[0].linkId == "ActivityDefinition.contained-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "ActivityDefinition.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert (
        inst.item[0].item[7].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[7].item[0].linkId == "ActivityDefinition.extension-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "ActivityDefinition.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert (
        inst.item[0].item[8].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].linkId
        == "ActivityDefinition.modifierExtension-flyover"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "ActivityDefinition.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert (
        inst.item[0].item[9].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[9].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[9].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[9].item[0].linkId == "ActivityDefinition.url-flyover"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "ActivityDefinition.url.value"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == (
        "Canonical identifier for this activity definition, "
        "represented as a URI (globally unique)"
    )
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].linkId == "ActivityDefinition.url"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "ActivityDefinition"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == (
        "The definition of a specific activity to be taken, "
        "independent of any particular patient or context"
    )
    assert inst.item[0].type == "group"
    assert (
        inst.publisher == "Health Level Seven International (Clinical Decision Support)"
    )
    assert inst.status == "draft"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/Questionnaire/qgen-ActivityDefinition1"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_questionnaire_5(base_settings):
    """No. 5 tests collection for Questionnaire.
    Test File: activitydefinition-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "activitydefinition-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.model_validate_json(filename.read_bytes())
    assert "Questionnaire" == inst.get_resource_type()

    impl_questionnaire_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_5(inst2)


def impl_questionnaire_6(inst):
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2020-12-28T16:55:11+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert inst.id == "qgen-cdshooksguidanceresponse1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert (
        inst.item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-minOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].extension[0].valueInteger == 1
    assert (
        inst.item[0].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].extension[1].valueInteger == 1
    assert (
        inst.item[0].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[0].linkId == "GuidanceResponse-flyover"
    assert inst.item[0].item[0].text == (
        "A guidance response is the formal response to a guidance "
        "request, including any output parameters returned by the "
        "evaluation, as well as the description of any proposed "
        "actions to be taken."
    )
    assert inst.item[0].item[0].type == "display"
    assert (
        inst.item[0].item[1].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[1].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert (
        inst.item[0].item[1].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[1].item[0].linkId == "GuidanceResponse.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "GuidanceResponse.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "GuidanceResponse.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert (
        inst.item[0].item[2].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[2].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[2].item[0].linkId == "GuidanceResponse.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "GuidanceResponse.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert (
        inst.item[0].item[3].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[3].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[3].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].linkId == "GuidanceResponse.implicitRules-flyover"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "GuidanceResponse.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "GuidanceResponse.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert (
        inst.item[0].item[4].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[4].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert (
        inst.item[0].item[4].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[4].item[0].linkId == "GuidanceResponse.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOrType"
    assert inst.item[0].item[4].item[1].linkId == "GuidanceResponse.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "GuidanceResponse.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert (
        inst.item[0].item[5].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[5].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[5].item[0].linkId == "GuidanceResponse.text-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "GuidanceResponse.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert (
        inst.item[0].item[6].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[6].item[0].linkId == "GuidanceResponse.contained-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "GuidanceResponse.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert (
        inst.item[0].item[7].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[7].item[0].linkId == "GuidanceResponse.extension-flyover"
    assert inst.item[0].item[7].item[0].text == "An Extension"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "GuidanceResponse.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Extension"
    assert inst.item[0].item[7].type == "group"
    assert (
        inst.item[0].item[8].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].linkId
        == "GuidanceResponse.modifierExtension-flyover"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "GuidanceResponse.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert (
        inst.item[0].item[9].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-minOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[9].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].extension[1].valueInteger == 1
    assert (
        inst.item[0].item[9].extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].extension[2].valueString == "Identifier"
    assert (
        inst.item[0].item[9].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].linkId
        == "GuidanceResponse.requestIdentifier-flyover"
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert (
        inst.item[0].item[9].item[1].linkId
        == "GuidanceResponse.requestIdentifier.label"
    )
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert (
        inst.item[0].item[9].item[2].linkId
        == "GuidanceResponse.requestIdentifier.system"
    )
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert (
        inst.item[0].item[9].item[3].linkId
        == "GuidanceResponse.requestIdentifier.value"
    )
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "GuidanceResponse.requestIdentifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is True
    assert inst.item[0].item[9].text == (
        "The identifier of the request associated with this response," " if any"
    )
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "GuidanceResponse"
    assert inst.item[0].repeats is False
    assert inst.item[0].required is True
    assert inst.item[0].text == "The formal response to a guidance request"
    assert inst.item[0].type == "group"
    assert inst.publisher == "HL7"
    assert inst.status == "draft"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/Questionnaire/qgen-cdshooksguidanceresponse1"
            }
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_questionnaire_6(base_settings):
    """No. 6 tests collection for Questionnaire.
    Test File: cdshooksguidanceresponse-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "cdshooksguidanceresponse-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.model_validate_json(filename.read_bytes())
    assert "Questionnaire" == inst.get_resource_type()

    impl_questionnaire_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_6(inst2)


def impl_questionnaire_7(inst):
    assert inst.contained[0].id == "vs2"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert inst.id == "qgen-SearchParameter1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert inst.item[0].item[0].linkId == "SearchParameter-display"
    assert inst.item[0].item[0].text == (
        "In FHIR, search is not performed directly on a resource (by "
        "XML or JSON path), but on a named parameter that maps into "
        "the resource content."
    )
    assert inst.item[0].item[0].type == "display"
    assert (
        inst.item[0].item[1].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[1].linkId == "SearchParameter-flyover"
    assert inst.item[0].item[1].text == (
        "A search parameter that defines a named search item that can"
        " be used to search/filter on a resource."
    )
    assert inst.item[0].item[1].type == "display"
    assert (
        inst.item[0].item[2].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[2].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert (
        inst.item[0].item[2].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[2].item[0].linkId == "SearchParameter.id-flyover"
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "SearchParameter.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "SearchParameter.id"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].type == "group"
    assert (
        inst.item[0].item[3].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[3].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[3].item[0].linkId == "SearchParameter.meta-flyover"
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "SearchParameter.meta"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].text == "Metadata about the resource"
    assert inst.item[0].item[3].type == "group"
    assert (
        inst.item[0].item[4].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[4].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[4].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].linkId == "SearchParameter.implicitRules-flyover"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "SearchParameter.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert (
        inst.item[0].item[4].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "SearchParameter.implicitRules"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert (
        inst.item[0].item[5].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[5].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert (
        inst.item[0].item[5].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[5].item[0].linkId == "SearchParameter.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].answerConstraint == "optionsOrType"
    assert inst.item[0].item[5].item[1].linkId == "SearchParameter.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "coding"
    assert inst.item[0].item[5].linkId == "SearchParameter.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert (
        inst.item[0].item[6].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[6].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[6].item[0].linkId == "SearchParameter.text-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "SearchParameter.text"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert (
        inst.item[0].item[6].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[6].type == "group"
    assert (
        inst.item[0].item[7].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[7].item[0].linkId == "SearchParameter.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "SearchParameter.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert (
        inst.item[0].item[8].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[8].item[0].linkId == "SearchParameter.extension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "SearchParameter.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert (
        inst.item[0].item[9].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].linkId
        == "SearchParameter.modifierExtension-flyover"
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "SearchParameter.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "SearchParameter"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Search parameter for a resource"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.status == "draft"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/Questionnaire/qgen-SearchParameter1"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_questionnaire_7(base_settings):
    """No. 7 tests collection for Questionnaire.
    Test File: searchparameter-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "searchparameter-questionnaire.json"
    inst = questionnaire.Questionnaire.model_validate_json(filename.read_bytes())
    assert "Questionnaire" == inst.get_resource_type()

    impl_questionnaire_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_7(inst2)


def impl_questionnaire_8(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.contained[3].id == "vs5"
    assert inst.contained[4].id == "vs6"
    assert inst.contained[5].id == "vs7"
    assert inst.contained[6].id == "vs8"
    assert inst.contained[7].id == "vs9"
    assert inst.contained[8].id == "vs10"
    assert inst.contained[9].id == "vs11"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert inst.id == "qgen-ExplanationOfBenefit1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[0].linkId == "ExplanationOfBenefit-flyover"
    assert inst.item[0].item[0].text == (
        "This resource provides: the claim details; adjudication "
        "details from the processing of a Claim; and optionally "
        "account balance information, for informing the subscriber of"
        " the benefits provided."
    )
    assert inst.item[0].item[0].type == "display"
    assert (
        inst.item[0].item[1].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[1].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert (
        inst.item[0].item[1].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[1].item[0].linkId == "ExplanationOfBenefit.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "ExplanationOfBenefit.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "ExplanationOfBenefit.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert (
        inst.item[0].item[2].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[2].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[2].item[0].linkId == "ExplanationOfBenefit.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "ExplanationOfBenefit.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert (
        inst.item[0].item[3].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[3].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[3].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].linkId
        == "ExplanationOfBenefit.implicitRules-flyover"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert (
        inst.item[0].item[3].item[1].linkId
        == "ExplanationOfBenefit.implicitRules.value"
    )
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "ExplanationOfBenefit.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert (
        inst.item[0].item[4].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[4].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert (
        inst.item[0].item[4].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].linkId == "ExplanationOfBenefit.language-flyover"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOrType"
    assert inst.item[0].item[4].item[1].linkId == "ExplanationOfBenefit.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "ExplanationOfBenefit.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert (
        inst.item[0].item[5].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[5].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[5].item[0].linkId == "ExplanationOfBenefit.text-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "ExplanationOfBenefit.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert (
        inst.item[0].item[6].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].linkId == "ExplanationOfBenefit.contained-flyover"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "ExplanationOfBenefit.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert (
        inst.item[0].item[7].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].linkId == "ExplanationOfBenefit.extension-flyover"
    )
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "ExplanationOfBenefit.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert (
        inst.item[0].item[8].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].linkId
        == "ExplanationOfBenefit.modifierExtension-flyover"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "ExplanationOfBenefit.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert (
        inst.item[0].item[9].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].extension[0].valueString == "Identifier"
    assert (
        inst.item[0].item[9].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].linkId == "ExplanationOfBenefit.identifier-flyover"
    )
    assert (
        inst.item[0].item[9].item[0].text
        == "A unique identifier assigned to this explanation of benefit."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert (
        inst.item[0].item[9].item[1].linkId == "ExplanationOfBenefit.identifier.label"
    )
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert (
        inst.item[0].item[9].item[2].linkId == "ExplanationOfBenefit.identifier.system"
    )
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert (
        inst.item[0].item[9].item[3].linkId == "ExplanationOfBenefit.identifier.value"
    )
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "ExplanationOfBenefit.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Business Identifier for the resource"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "ExplanationOfBenefit"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Explanation of Benefit resource"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Financial Management)"
    assert inst.status == "draft"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/Questionnaire/qgen-ExplanationOfBenefit1"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_questionnaire_8(base_settings):
    """No. 8 tests collection for Questionnaire.
    Test File: explanationofbenefit-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "explanationofbenefit-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.model_validate_json(filename.read_bytes())
    assert "Questionnaire" == inst.get_resource_type()

    impl_questionnaire_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_8(inst2)


def impl_questionnaire_9(inst):
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert inst.id == "qgen-ImmunizationEvaluation1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[0].linkId == "ImmunizationEvaluation-flyover"
    assert inst.item[0].item[0].text == (
        "Describes a comparison of an immunization event against "
        "published recommendations to determine if the administration"
        ' is "valid" in relation to those  recommendations.'
    )
    assert inst.item[0].item[0].type == "display"
    assert (
        inst.item[0].item[1].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[1].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert (
        inst.item[0].item[1].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[1].item[0].linkId == "ImmunizationEvaluation.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "ImmunizationEvaluation.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "ImmunizationEvaluation.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert (
        inst.item[0].item[2].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[2].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[2].item[0].linkId == "ImmunizationEvaluation.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "ImmunizationEvaluation.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert (
        inst.item[0].item[3].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[3].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[3].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].linkId
        == "ImmunizationEvaluation.implicitRules-flyover"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert (
        inst.item[0].item[3].item[1].linkId
        == "ImmunizationEvaluation.implicitRules.value"
    )
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "ImmunizationEvaluation.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert (
        inst.item[0].item[4].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[4].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert (
        inst.item[0].item[4].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].linkId == "ImmunizationEvaluation.language-flyover"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOrType"
    assert (
        inst.item[0].item[4].item[1].linkId == "ImmunizationEvaluation.language.value"
    )
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "ImmunizationEvaluation.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert (
        inst.item[0].item[5].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[5].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[5].item[0].linkId == "ImmunizationEvaluation.text-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "ImmunizationEvaluation.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert (
        inst.item[0].item[6].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].linkId
        == "ImmunizationEvaluation.contained-flyover"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "ImmunizationEvaluation.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert (
        inst.item[0].item[7].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].linkId
        == "ImmunizationEvaluation.extension-flyover"
    )
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "ImmunizationEvaluation.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert (
        inst.item[0].item[8].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].linkId
        == "ImmunizationEvaluation.modifierExtension-flyover"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "ImmunizationEvaluation.modifierExtension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert (
        inst.item[0].item[9].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].extension[0].valueString == "Identifier"
    assert (
        inst.item[0].item[9].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[0].linkId
        == "ImmunizationEvaluation.identifier-flyover"
    )
    assert inst.item[0].item[9].item[0].text == (
        "A unique identifier assigned to this immunization evaluation" " record."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert (
        inst.item[0].item[9].item[1].linkId == "ImmunizationEvaluation.identifier.label"
    )
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert (
        inst.item[0].item[9].item[2].linkId
        == "ImmunizationEvaluation.identifier.system"
    )
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert (
        inst.item[0].item[9].item[3].linkId == "ImmunizationEvaluation.identifier.value"
    )
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "ImmunizationEvaluation.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Business identifier"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "ImmunizationEvaluation"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Immunization evaluation information"
    assert inst.item[0].type == "group"
    assert inst.publisher == (
        "Health Level Seven International (Public Health and " "Emergency Response)"
    )
    assert inst.status == "draft"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/Questionnaire/qgen-ImmunizationEvaluation1"
            }
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_questionnaire_9(base_settings):
    """No. 9 tests collection for Questionnaire.
    Test File: immunizationevaluation-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "immunizationevaluation-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.model_validate_json(filename.read_bytes())
    assert "Questionnaire" == inst.get_resource_type()

    impl_questionnaire_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_9(inst2)


def impl_questionnaire_10(inst):
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2023-03-26T15:21:02+11:00"}
        ).valueDateTime
    )
    assert inst.experimental is False
    assert inst.id == "qgen-document-bundle1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[0].linkId == "Bundle-flyover"
    assert inst.item[0].item[0].text == "A container the resources of a FHIR document."
    assert inst.item[0].item[0].type == "display"
    assert (
        inst.item[0].item[1].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[1].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert (
        inst.item[0].item[1].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[1].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[1].item[0].linkId == "Bundle.id-flyover"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "Bundle.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "Bundle.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert (
        inst.item[0].item[2].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[2].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[2].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[2].item[0].linkId == "Bundle.meta-flyover"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "Bundle.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert (
        inst.item[0].item[3].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[3].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert (
        inst.item[0].item[3].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[3].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[3].item[0].linkId == "Bundle.implicitRules-flyover"
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "Bundle.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "Bundle.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert (
        inst.item[0].item[4].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[4].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert (
        inst.item[0].item[4].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[4].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[4].item[0].linkId == "Bundle.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].answerConstraint == "optionsOrType"
    assert inst.item[0].item[4].item[1].linkId == "Bundle.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "coding"
    assert inst.item[0].item[4].linkId == "Bundle.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert (
        inst.item[0].item[5].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-minOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[5].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[1].valueInteger == 1
    assert (
        inst.item[0].item[5].extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[5].extension[2].valueString == "Identifier"
    assert (
        inst.item[0].item[5].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[5].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[5].item[0].linkId == "Bundle.identifier-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "Bundle.identifier.label"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "label:"
    assert inst.item[0].item[5].item[1].type == "string"
    assert inst.item[0].item[5].item[2].linkId == "Bundle.identifier.system"
    assert inst.item[0].item[5].item[2].repeats is False
    assert inst.item[0].item[5].item[2].required is False
    assert inst.item[0].item[5].item[2].text == "system:"
    assert inst.item[0].item[5].item[2].type == "string"
    assert inst.item[0].item[5].item[3].linkId == "Bundle.identifier.value"
    assert inst.item[0].item[5].item[3].repeats is False
    assert inst.item[0].item[5].item[3].required is False
    assert inst.item[0].item[5].item[3].text == "value:"
    assert inst.item[0].item[5].item[3].type == "string"
    assert inst.item[0].item[5].linkId == "Bundle.identifier"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is True
    assert inst.item[0].item[5].text == "Persistent identifier for the bundle"
    assert inst.item[0].item[5].type == "group"
    assert (
        inst.item[0].item[6].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-minOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[6].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[6].extension[1].valueInteger == 1
    assert (
        inst.item[0].item[6].extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[6].extension[2].valueString == "code"
    assert (
        inst.item[0].item[6].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[6].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[6].item[0].linkId == "Bundle.type-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].item[1].answerConstraint == "optionsOrType"
    assert inst.item[0].item[6].item[1].linkId == "Bundle.type.value"
    assert inst.item[0].item[6].item[1].repeats is False
    assert inst.item[0].item[6].item[1].required is False
    assert inst.item[0].item[6].item[1].text == "type"
    assert inst.item[0].item[6].item[1].type == "coding"
    assert inst.item[0].item[6].linkId == "Bundle.type"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is True
    assert inst.item[0].item[6].type == "group"
    assert (
        inst.item[0].item[7].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-minOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[7].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[7].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[7].extension[1].valueInteger == 1
    assert (
        inst.item[0].item[7].extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[7].extension[2].valueString == "instant"
    assert (
        inst.item[0].item[7].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[7].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[7].item[0].linkId == "Bundle.timestamp-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].item[1].linkId == "Bundle.timestamp.value"
    assert inst.item[0].item[7].item[1].repeats is False
    assert inst.item[0].item[7].item[1].required is False
    assert inst.item[0].item[7].item[1].text == "When the bundle was assembled"
    assert inst.item[0].item[7].item[1].type == "dateTime"
    assert inst.item[0].item[7].linkId == "Bundle.timestamp"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is True
    assert inst.item[0].item[7].type == "group"
    assert (
        inst.item[0].item[8].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[8].extension[0].valueInteger == 0
    assert (
        inst.item[0].item[8].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[8].extension[1].valueString == "integer"
    assert (
        inst.item[0].item[8].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[0].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[8].item[0].linkId == "Bundle.total-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].item[1].linkId == "Bundle.total.value"
    assert inst.item[0].item[8].item[1].repeats is False
    assert inst.item[0].item[8].item[1].required is False
    assert inst.item[0].item[8].item[1].text == "If search, the total number of matches"
    assert inst.item[0].item[8].item[1].type == "integer"
    assert inst.item[0].item[8].linkId == "Bundle.total"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].item[0].linkId == "Bundle.link-display"
    assert inst.item[0].item[9].item[0].type == "display"
    assert (
        inst.item[0].item[9].item[1].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[1].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[9].item[1].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[9].item[1].extension[0].valueCodeableConcept.coding[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[9].item[1].linkId == "Bundle.link-flyover"
    assert (
        inst.item[0].item[9].item[1].text
        == "A series of links that provide context to this bundle."
    )
    assert inst.item[0].item[9].item[1].type == "display"
    assert (
        inst.item[0].item[9].item[2].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].item[2].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[9].item[2].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].item[2].extension[1].valueString == "string"
    assert (
        inst.item[0].item[9].item[2].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0]
        .item[9]
        .item[2]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[9]
        .item[2]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[9]
        .item[2]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[9].item[2].item[0].linkId == "Bundle.link.id-flyover"
    assert inst.item[0].item[9].item[2].item[0].text == (
        "Unique id for the element within a resource (for internal "
        "references). This may be any string value that does not "
        "contain spaces."
    )
    assert inst.item[0].item[9].item[2].item[0].type == "display"
    assert inst.item[0].item[9].item[2].item[1].linkId == "Bundle.link.id.value"
    assert inst.item[0].item[9].item[2].item[1].repeats is False
    assert inst.item[0].item[9].item[2].item[1].required is False
    assert (
        inst.item[0].item[9].item[2].item[1].text
        == "Unique id for inter-element referencing"
    )
    assert inst.item[0].item[9].item[2].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "Bundle.link.id"
    assert inst.item[0].item[9].item[2].repeats is True
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].type == "group"
    assert (
        inst.item[0].item[9].item[3].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0]
        .item[9]
        .item[3]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[9]
        .item[3]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[9]
        .item[3]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[3].item[0].linkId == "Bundle.link.extension-flyover"
    )
    assert inst.item[0].item[9].item[3].item[0].type == "display"
    assert inst.item[0].item[9].item[3].linkId == "Bundle.link.extension"
    assert inst.item[0].item[9].item[3].repeats is True
    assert inst.item[0].item[9].item[3].required is False
    assert (
        inst.item[0].item[9].item[3].text
        == "Additional content defined by implementations"
    )
    assert inst.item[0].item[9].item[3].type == "group"
    assert (
        inst.item[0].item[9].item[4].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0]
        .item[9]
        .item[4]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[9]
        .item[4]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[9]
        .item[4]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert (
        inst.item[0].item[9].item[4].item[0].linkId
        == "Bundle.link.modifierExtension-flyover"
    )
    assert inst.item[0].item[9].item[4].item[0].type == "display"
    assert inst.item[0].item[9].item[4].linkId == "Bundle.link.modifierExtension"
    assert inst.item[0].item[9].item[4].repeats is True
    assert inst.item[0].item[9].item[4].required is False
    assert (
        inst.item[0].item[9].item[4].text
        == "Extensions that cannot be ignored even if unrecognized"
    )
    assert inst.item[0].item[9].item[4].type == "group"
    assert (
        inst.item[0].item[9].item[5].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-minOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].item[5].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[9].item[5].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].item[5].extension[1].valueInteger == 1
    assert (
        inst.item[0].item[9].item[5].extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].item[5].extension[2].valueString == "code"
    assert (
        inst.item[0].item[9].item[5].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0]
        .item[9]
        .item[5]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[9]
        .item[5]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[9]
        .item[5]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[9].item[5].item[0].linkId == "Bundle.link.relation-flyover"
    assert inst.item[0].item[9].item[5].item[0].type == "display"
    assert inst.item[0].item[9].item[5].item[1].answerConstraint == "optionsOrType"
    assert inst.item[0].item[9].item[5].item[1].linkId == "Bundle.link.relation.value"
    assert inst.item[0].item[9].item[5].item[1].repeats is False
    assert inst.item[0].item[9].item[5].item[1].required is False
    assert inst.item[0].item[9].item[5].item[1].text == "relation"
    assert inst.item[0].item[9].item[5].item[1].type == "coding"
    assert inst.item[0].item[9].item[5].linkId == "Bundle.link.relation"
    assert inst.item[0].item[9].item[5].repeats is True
    assert inst.item[0].item[9].item[5].required is True
    assert inst.item[0].item[9].item[5].type == "group"
    assert (
        inst.item[0].item[9].item[6].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-minOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].item[6].extension[0].valueInteger == 1
    assert (
        inst.item[0].item[9].item[6].extension[1].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].item[6].extension[1].valueInteger == 1
    assert (
        inst.item[0].item[9].item[6].extension[2].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            }
        ).valueUri
    )
    assert inst.item[0].item[9].item[6].extension[2].valueString == "uri"
    assert (
        inst.item[0].item[9].item[6].item[0].extension[0].url
        == ExternalValidatorModel.model_validate(
            {
                "valueUri": "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            }
        ).valueUri
    )
    assert (
        inst.item[0]
        .item[9]
        .item[6]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[9]
        .item[6]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[9]
        .item[6]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/questionnaire-item-control"}
        ).valueUri
    )
    assert inst.item[0].item[9].item[6].item[0].linkId == "Bundle.link.url-flyover"
    assert (
        inst.item[0].item[9].item[6].item[0].text
        == "The reference details for the link."
    )
    assert inst.item[0].item[9].item[6].item[0].type == "display"
    assert inst.item[0].item[9].item[6].item[1].linkId == "Bundle.link.url.value"
    assert inst.item[0].item[9].item[6].item[1].repeats is False
    assert inst.item[0].item[9].item[6].item[1].required is False
    assert inst.item[0].item[9].item[6].item[1].text == "Reference details for the link"
    assert inst.item[0].item[9].item[6].item[1].type == "string"
    assert inst.item[0].item[9].item[6].linkId == "Bundle.link.url"
    assert inst.item[0].item[9].item[6].repeats is True
    assert inst.item[0].item[9].item[6].required is True
    assert inst.item[0].item[9].item[6].type == "group"
    assert inst.item[0].item[9].linkId == "Bundle.link"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Links related to this Bundle"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Bundle"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Represents a FHIR document"
    assert inst.item[0].type == "group"
    assert inst.status == "active"
    assert (
        inst.url
        == ExternalValidatorModel.model_validate(
            {"valueUri": "http://hl7.org/fhir/Questionnaire/qgen-document-bundle1"}
        ).valueUri
    )
    assert inst.version == "5.0.0"


def test_questionnaire_10(base_settings):
    """No. 10 tests collection for Questionnaire.
    Test File: document-bundle-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "document-bundle-questionnaire.json"
    inst = questionnaire.Questionnaire.model_validate_json(filename.read_bytes())
    assert "Questionnaire" == inst.get_resource_type()

    impl_questionnaire_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_10(inst2)
