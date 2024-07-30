# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from .. import questionnaire
from .fixtures import ExternalValidatorModel  # noqa: F401


def impl_questionnaire_1(inst):
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
            {"valueDateTime": "2012-05-12T00:00:00+10:00"}
        ).valueDateTime
    )
    assert inst.id == "qs1"
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
    assert inst.item[0].item[1].text == "Group of elements for HDL Cholesterol result."
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
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "Observation.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "Observation.id"
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
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "Observation.meta"
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
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Observation.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert (
        inst.item[0].item[4].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "Observation.implicitRules"
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
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "Observation.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "choice"
    assert inst.item[0].item[5].linkId == "Observation.language"
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
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Observation.text"
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
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Observation.contained"
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
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Observation.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "Observation.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Observation"
    assert inst.item[0].repeats is False
    assert inst.item[0].required is True
    assert inst.item[0].text == "HDL Cholesterol Result"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Grahame Grieve"
    assert inst.status == "draft"


def test_questionnaire_1(base_settings):
    """No. 1 tests collection for Questionnaire.
    Test File: questionnaire-hdlcholesterol-questionnaire(qs1).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaire-hdlcholesterol-questionnaire(qs1).json"
    )
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
            {"valueDateTime": "2012-05-12T00:00:00+10:00"}
        ).valueDateTime
    )
    assert inst.id == "qs1"
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
    assert inst.item[0].item[1].text == "Group of elements for Triglyceride result."
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
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "Observation.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "Observation.id"
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
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "Observation.meta"
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
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Observation.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert (
        inst.item[0].item[4].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "Observation.implicitRules"
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
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "Observation.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "choice"
    assert inst.item[0].item[5].linkId == "Observation.language"
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
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Observation.text"
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
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Observation.contained"
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
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Observation.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "Observation.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Observation"
    assert inst.item[0].repeats is False
    assert inst.item[0].required is True
    assert inst.item[0].text == "Triglyceride Result"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Grahame Grieve"
    assert inst.status == "draft"


def test_questionnaire_2(base_settings):
    """No. 2 tests collection for Questionnaire.
    Test File: questionnaire-triglyceride-questionnaire(qs1).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaire-triglyceride-questionnaire(qs1).json"
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
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.id == "qs1"
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
    assert inst.item[0].item[0].text == (
        "A booking of a healthcare event among patient(s), "
        "practitioner(s), related person(s) and/or device(s) for a "
        "specific date/time. This may result in one or more "
        "Encounter(s)."
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
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "Appointment.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "Appointment.id"
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
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "Appointment.meta"
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
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "Appointment.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "Appointment.implicitRules"
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
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Appointment.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "Appointment.language"
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
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "Appointment.text"
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
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Appointment.contained"
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
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Appointment.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Appointment.modifierExtension"
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
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "Appointment.identifier.label"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "Appointment.identifier.system"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].item[3].linkId == "Appointment.identifier.value"
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "Appointment.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "External Ids for this item"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Appointment"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == (
        "A booking of a healthcare event among patient(s), "
        "practitioner(s), related person(s) and/or device(s) for a "
        "specific date/time. This may result in one or more "
        "Encounter(s)"
    )
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Patient Administration)"
    assert inst.status == "draft"


def test_questionnaire_3(base_settings):
    """No. 3 tests collection for Questionnaire.
    Test File: questionnaire-appointment-questionnaire(qs1).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaire-appointment-questionnaire(qs1).json"
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
    assert inst.contained[2].id == "vs4"
    assert inst.contained[3].id == "vs5"
    assert inst.contained[4].id == "vs6"
    assert inst.contained[5].id == "vs7"
    assert inst.contained[6].id == "vs8"
    assert inst.contained[7].id == "vs9"
    assert inst.contained[8].id == "vs10"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.id == "qs1"
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
    assert inst.item[0].item[0].text == (
        "A formal agreement between parties regarding the conduct of "
        "business, exchange of information or other matters."
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
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "Contract.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "Contract.id"
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
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "Contract.meta"
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
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "Contract.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "Contract.implicitRules"
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
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Contract.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "Contract.language"
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
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "Contract.text"
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
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Contract.contained"
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
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Contract.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Contract.modifierExtension"
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
    assert inst.item[0].item[9].extension[1].valueString == "Identifier"
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
    assert inst.item[0].item[9].item[0].text == "Unique identifier for this Contract."
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "Contract.identifier.label"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "Contract.identifier.system"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].item[3].linkId == "Contract.identifier.value"
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "Contract.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Contract number"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Contract"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Legal Agreement"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Financial Management)"
    assert inst.status == "draft"


def test_questionnaire_4(base_settings):
    """No. 4 tests collection for Questionnaire.
    Test File: questionnaire-contract-questionnaire(qs1).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaire-contract-questionnaire(qs1).json"
    )
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
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.id == "qs1"
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
    assert inst.item[0].item[0].text == (
        "A text description of the DICOM SOP instances selected in "
        "the ImagingManifest; or the reason for, or significance of, "
        "the selection."
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
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "ImagingManifest.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "ImagingManifest.id"
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
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "ImagingManifest.meta"
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
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "ImagingManifest.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "ImagingManifest.implicitRules"
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
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "ImagingManifest.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "ImagingManifest.language"
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
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "ImagingManifest.text"
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
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "ImagingManifest.contained"
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
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "ImagingManifest.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "ImagingManifest.modifierExtension"
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
    assert inst.item[0].item[9].extension[1].valueString == "Identifier"
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
    assert inst.item[0].item[9].item[0].text == (
        "Unique identifier of the DICOM Key Object Selection (KOS) "
        "that this resource represents."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "ImagingManifest.identifier.label"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "ImagingManifest.identifier.system"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].item[3].linkId == "ImagingManifest.identifier.value"
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "ImagingManifest.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "SOP Instance UID"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "ImagingManifest"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Key Object Selection"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Imaging Integration)"
    assert inst.status == "draft"


def test_questionnaire_5(base_settings):
    """No. 5 tests collection for Questionnaire.
    Test File: questionnaire-imagingmanifest-questionnaire(qs1).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaire-imagingmanifest-questionnaire(qs1).json"
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
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.id == "qs1"
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
    assert inst.item[0].item[0].text == (
        "A summary of information based on the results of executing a" " TestScript."
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
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "TestReport.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "TestReport.id"
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
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "TestReport.meta"
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
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "TestReport.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "TestReport.implicitRules"
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
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "TestReport.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "TestReport.language"
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
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "TestReport.text"
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
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "TestReport.contained"
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
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "TestReport.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "TestReport.modifierExtension"
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
    assert inst.item[0].item[9].extension[1].valueString == "Identifier"
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
    assert inst.item[0].item[9].item[0].text == (
        "Identifier for the TestScript assigned for external purposes"
        " outside the context of FHIR."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "TestReport.identifier.label"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "TestReport.identifier.system"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].item[3].linkId == "TestReport.identifier.value"
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "TestReport.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "External identifier"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "TestReport"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Describes the results of a TestScript execution"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.status == "draft"


def test_questionnaire_6(base_settings):
    """No. 6 tests collection for Questionnaire.
    Test File: questionnaire-testreport-questionnaire(qs1).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaire-testreport-questionnaire(qs1).json"
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
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.id == "qs1"
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
    assert inst.item[0].item[0].text == (
        "A record of a device being used by a patient where the "
        "record is the result of a report from the patient or another"
        " clinician."
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
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "DeviceUseStatement.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "DeviceUseStatement.id"
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
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "DeviceUseStatement.meta"
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
    assert inst.item[0].item[3].item[0].type == "display"
    assert (
        inst.item[0].item[3].item[1].linkId == "DeviceUseStatement.implicitRules.value"
    )
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "DeviceUseStatement.implicitRules"
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
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "DeviceUseStatement.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "DeviceUseStatement.language"
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
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "DeviceUseStatement.text"
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
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "DeviceUseStatement.contained"
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
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "DeviceUseStatement.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "DeviceUseStatement.modifierExtension"
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
        inst.item[0].item[9].item[0].text
        == "An external identifier for this statement such as an IRI."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "DeviceUseStatement.identifier.label"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "DeviceUseStatement.identifier.system"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].item[3].linkId == "DeviceUseStatement.identifier.value"
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "DeviceUseStatement.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "External identifier for this record"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "DeviceUseStatement"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Record of use of a device"
    assert inst.item[0].type == "group"
    assert (
        inst.publisher == "Health Level Seven International (Orders and Observations)"
    )
    assert inst.status == "draft"


def test_questionnaire_7(base_settings):
    """No. 7 tests collection for Questionnaire.
    Test File: questionnaire-deviceusestatement-questionnaire(qs1).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaire-deviceusestatement-questionnaire(qs1).json"
    )
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
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-03-25T00:00:00+11:00"}
        ).valueDateTime
    )
    assert inst.id == "qs1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
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
    assert inst.item[0].item[1].text == (
        "This profile defines how to represent heart rate "
        "observations in FHIR using a standard LOINC code and UCUM "
        "units of measure."
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
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "Observation.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "Observation.id"
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
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "Observation.meta"
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
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Observation.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert (
        inst.item[0].item[4].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "Observation.implicitRules"
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
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "Observation.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "choice"
    assert inst.item[0].item[5].linkId == "Observation.language"
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
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Observation.text"
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
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Observation.contained"
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
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Observation.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "Observation.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Observation"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "FHIR Heart Rate Profile"
    assert inst.item[0].type == "group"
    assert inst.publisher == (
        "Health Level Seven International (Orders and Observations " "Workgroup)"
    )
    assert inst.status == "draft"


def test_questionnaire_8(base_settings):
    """No. 8 tests collection for Questionnaire.
    Test File: questionnaire-heartrate-questionnaire(qs1).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaire-heartrate-questionnaire(qs1).json"
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
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2019-10-24T11:53:00+11:00"}
        ).valueDateTime
    )
    assert inst.id == "qs1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
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
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "Composition.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "Composition.id"
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
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "Composition.meta"
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
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Composition.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert (
        inst.item[0].item[4].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "Composition.implicitRules"
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
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "Composition.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "choice"
    assert inst.item[0].item[5].linkId == "Composition.language"
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
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Composition.text"
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
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Composition.contained"
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
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Composition.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "Composition.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Composition"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == (
        "A set of resources composed into a single coherent clinical "
        "statement with clinical attestation"
    )
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Structured Documents)"
    assert inst.status == "draft"


def test_questionnaire_9(base_settings):
    """No. 9 tests collection for Questionnaire.
    Test File: questionnaire-composition-questionnaire(qs1).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaire-composition-questionnaire(qs1).json"
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
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.contained[3].id == "vs5"
    assert inst.contained[4].id == "vs6"
    assert (
        inst.date
        == ExternalValidatorModel.model_validate(
            {"valueDateTime": "2016-03-25T00:00:00+11:00"}
        ).valueDateTime
    )
    assert inst.id == "qs1"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel.model_validate(
            {"valueUri": "urn:ietf:rfc:3986"}
        ).valueUri
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
    assert inst.item[0].item[1].text == (
        "The FHIR Vitals Signs profile sets a minimum expectations "
        "for the Observation Resource to record, search and fetch the"
        " vital signs associated with a patient."
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
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "Observation.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "Observation.id"
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
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "Observation.meta"
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
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Observation.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert (
        inst.item[0].item[4].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "Observation.implicitRules"
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
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "Observation.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "choice"
    assert inst.item[0].item[5].linkId == "Observation.language"
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
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Observation.text"
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
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Observation.contained"
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
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Observation.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "Observation.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Observation"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "FHIR Vital Signs Profile"
    assert inst.item[0].type == "group"
    assert inst.publisher == (
        "Health Level Seven International (Orders and Observations " "Workgroup)"
    )
    assert inst.status == "draft"


def test_questionnaire_10(base_settings):
    """No. 10 tests collection for Questionnaire.
    Test File: questionnaire-vitalsigns-questionnaire(qs1).json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "questionnaire-vitalsigns-questionnaire(qs1).json"
    )
    inst = questionnaire.Questionnaire.model_validate_json(filename.read_bytes())
    assert "Questionnaire" == inst.get_resource_type()

    impl_questionnaire_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_10(inst2)
