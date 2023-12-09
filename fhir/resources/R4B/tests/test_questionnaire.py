# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic.v1.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import questionnaire


def impl_questionnaire_1(inst):
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].linkId == "Person-display"
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].linkId == "Person-flyover"
    assert inst.item[0].item[1].text == (
        "Demographics and administrative information about a person "
        "independent of a specific health-related context."
    )
    assert inst.item[0].item[1].type == "display"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].linkId == "Person.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "Person.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "choice"
    assert inst.item[0].item[5].linkId == "Person.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].linkId == "Person.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Person.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].linkId == "Person.extension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Person.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Health Level Seven International (Patient Administration)"
    assert inst.status == "draft"
    assert inst.version == "4.3.0"


def test_questionnaire_1(base_settings):
    """No. 1 tests collection for Questionnaire.
    Test File: person-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "person-questionnaire.json"
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_1(inst2)


def impl_questionnaire_2(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.date == fhirtypes.DateTime.validate("2015-10-09T00:00:00+11:00")
    assert inst.experimental is False
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].linkId == "DiagnosticReport-display"
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].linkId == "DiagnosticReport-flyover"
    assert inst.item[0].item[1].type == "display"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[2].item[0].linkId == "DiagnosticReport.id-flyover"
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].item[1].linkId == "DiagnosticReport.id.value"
    assert inst.item[0].item[2].item[1].repeats is False
    assert inst.item[0].item[2].item[1].required is False
    assert inst.item[0].item[2].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[2].item[1].type == "string"
    assert inst.item[0].item[2].linkId == "DiagnosticReport.id"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[3].item[0].linkId == "DiagnosticReport.meta-flyover"
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].linkId == "DiagnosticReport.meta"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].text == "Metadata about the resource"
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[4].item[0].linkId == "DiagnosticReport.implicitRules-flyover"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "DiagnosticReport.implicitRules.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert (
        inst.item[0].item[4].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[4].item[1].type == "string"
    assert inst.item[0].item[4].linkId == "DiagnosticReport.implicitRules"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].linkId == "DiagnosticReport.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "DiagnosticReport.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "choice"
    assert inst.item[0].item[5].linkId == "DiagnosticReport.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].linkId == "DiagnosticReport.text-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "DiagnosticReport.text"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert (
        inst.item[0].item[6].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].linkId == "DiagnosticReport.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "DiagnosticReport.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].linkId == "DiagnosticReport.extension-flyover"
    assert inst.item[0].item[8].item[0].text == "An Extension"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "DiagnosticReport.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extension"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[9].item[0].linkId
        == "DiagnosticReport.modifierExtension-flyover"
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "DiagnosticReport.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "DiagnosticReport"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == (
        "A Diagnostic report - a combination of request information, "
        "atomic results, images, interpretation, as well as formatted"
        " reports"
    )
    assert inst.item[0].type == "group"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Health Level Seven International (Clinical Genomics)"
    assert inst.status == "draft"
    assert inst.version == "4.3.0"


def test_questionnaire_2(base_settings):
    """No. 2 tests collection for Questionnaire.
    Test File: hlaresult-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "hlaresult-questionnaire.json"
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_2(inst2)


def impl_questionnaire_3(inst):
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].linkId == "OperationOutcome-display"
    assert inst.item[0].item[0].text == (
        "Can result from the failure of a REST call or be part of the"
        " response message returned from a request message."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].linkId == "OperationOutcome-flyover"
    assert inst.item[0].item[1].text == (
        "A collection of error, warning, or information messages that"
        " result from a system action."
    )
    assert inst.item[0].item[1].type == "display"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].linkId == "OperationOutcome.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "OperationOutcome.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "choice"
    assert inst.item[0].item[5].linkId == "OperationOutcome.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].linkId == "OperationOutcome.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "OperationOutcome.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].linkId == "OperationOutcome.extension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "OperationOutcome.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.status == "active"
    assert inst.version == "4.3.0"


def test_questionnaire_3(base_settings):
    """No. 3 tests collection for Questionnaire.
    Test File: operationoutcome-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "operationoutcome-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_3(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_3(inst2)


def impl_questionnaire_4(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].linkId == "EventDefinition-flyover"
    assert inst.item[0].item[0].text == (
        "The EventDefinition resource provides a reusable description"
        " of when a particular event can occur."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].linkId == "EventDefinition.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "EventDefinition.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "EventDefinition.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].linkId == "EventDefinition.contained-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "EventDefinition.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].linkId == "EventDefinition.extension-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "EventDefinition.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert inst.item[0].item[9].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[1].valueString == "uri"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.publisher == "Health Level Seven International (Clinical Decision Support)"
    )
    assert inst.status == "draft"
    assert inst.version == "4.3.0"


def test_questionnaire_4(base_settings):
    """No. 4 tests collection for Questionnaire.
    Test File: eventdefinition-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "eventdefinition-questionnaire.json"
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_4(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_4(inst2)


def impl_questionnaire_5(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].linkId == "ActivityDefinition-flyover"
    assert inst.item[0].item[0].text == (
        "This resource allows for the definition of some activity to "
        "be performed, independent of a particular patient, "
        "practitioner, or other performance context."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].linkId == "ActivityDefinition.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "ActivityDefinition.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "ActivityDefinition.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].linkId == "ActivityDefinition.contained-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "ActivityDefinition.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].linkId == "ActivityDefinition.extension-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "ActivityDefinition.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert inst.item[0].item[9].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[1].valueString == "uri"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert (
        inst.publisher == "Health Level Seven International (Clinical Decision Support)"
    )
    assert inst.status == "draft"
    assert inst.version == "4.3.0"


def test_questionnaire_5(base_settings):
    """No. 5 tests collection for Questionnaire.
    Test File: activitydefinition-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "activitydefinition-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_5(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_5(inst2)


def impl_questionnaire_6(inst):
    assert inst.date == fhirtypes.DateTime.validate("2021-01-17T07:06:13+11:00")
    assert inst.experimental is False
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "minOccurs"
    )
    assert inst.item[0].extension[0].valueInteger == 1
    assert inst.item[0].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].extension[1].valueInteger == 1
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].linkId == "GuidanceResponse-flyover"
    assert inst.item[0].item[0].text == (
        "A guidance response is the formal response to a guidance "
        "request, including any output parameters returned by the "
        "evaluation, as well as the description of any proposed "
        "actions to be taken."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[4].item[0].linkId == "GuidanceResponse.language-flyover"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "GuidanceResponse.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "GuidanceResponse.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[6].item[0].linkId == "GuidanceResponse.contained-flyover"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "GuidanceResponse.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].linkId == "GuidanceResponse.extension-flyover"
    assert inst.item[0].item[7].item[0].text == "An Extension"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "GuidanceResponse.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Extension"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "minOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 1
    assert inst.item[0].item[9].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[9].extension[1].valueInteger == 1
    assert inst.item[0].item[9].extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[2].valueString == "Identifier"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "HL7"
    assert inst.status == "draft"
    assert inst.version == "4.3.0"


def test_questionnaire_6(base_settings):
    """No. 6 tests collection for Questionnaire.
    Test File: cdshooksguidanceresponse-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "cdshooksguidanceresponse-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_6(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_6(inst2)


def impl_questionnaire_7(inst):
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].linkId == "SearchParameter-display"
    assert inst.item[0].item[0].text == (
        "In FHIR, search is not performed directly on a resource (by "
        "XML or JSON path), but on a named parameter that maps into "
        "the resource content."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[1].linkId == "SearchParameter-flyover"
    assert inst.item[0].item[1].text == (
        "A search parameter that defines a named search item that can"
        " be used to search/filter on a resource."
    )
    assert inst.item[0].item[1].type == "display"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "uri"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[5].extension[1].valueString == "code"
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[5].item[0].linkId == "SearchParameter.language-flyover"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "SearchParameter.language.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert inst.item[0].item[5].item[1].text == "language"
    assert inst.item[0].item[5].item[1].type == "choice"
    assert inst.item[0].item[5].linkId == "SearchParameter.language"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[7].item[0].linkId == "SearchParameter.contained-flyover"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "SearchParameter.contained"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Contained, inline Resources"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[0].linkId == "SearchParameter.extension-flyover"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "SearchParameter.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional content defined by implementations"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.status == "draft"
    assert inst.version == "4.3.0"


def test_questionnaire_7(base_settings):
    """No. 7 tests collection for Questionnaire.
    Test File: searchparameter-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "searchparameter-questionnaire.json"
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_7(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
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
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].linkId == "ExplanationOfBenefit-flyover"
    assert inst.item[0].item[0].text == (
        "This resource provides: the claim details; adjudication "
        "details from the processing of a Claim; and optionally "
        "account balance information, for informing the subscriber of"
        " the benefits provided."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[4].item[0].linkId == "ExplanationOfBenefit.language-flyover"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "ExplanationOfBenefit.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "ExplanationOfBenefit.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[0].valueString == "Identifier"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Health Level Seven International (Financial Management)"
    assert inst.status == "draft"
    assert inst.version == "4.3.0"


def test_questionnaire_8(base_settings):
    """No. 8 tests collection for Questionnaire.
    Test File: explanationofbenefit-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "explanationofbenefit-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_8(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_8(inst2)


def impl_questionnaire_9(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].linkId == "ImmunizationEvaluation-flyover"
    assert inst.item[0].item[0].text == (
        "Describes a comparison of an immunization event against "
        "published recommendations to determine if the administration"
        ' is "valid" in relation to those  recommendations.'
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[4].item[0].linkId == "ImmunizationEvaluation.language-flyover"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert (
        inst.item[0].item[4].item[1].linkId == "ImmunizationEvaluation.language.value"
    )
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "ImmunizationEvaluation.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[0].valueString == "Identifier"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
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
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == (
        "Health Level Seven International (Public Health and " "Emergency Response)"
    )
    assert inst.status == "draft"
    assert inst.version == "4.3.0"


def test_questionnaire_9(base_settings):
    """No. 9 tests collection for Questionnaire.
    Test File: immunizationevaluation-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "immunizationevaluation-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_9(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_9(inst2)


def impl_questionnaire_10(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.date == fhirtypes.DateTime.validate("2022-05-28T12:47:40+10:00")
    assert inst.experimental is False
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[0].linkId == "CoverageEligibilityResponse-flyover"
    assert inst.item[0].item[0].text == (
        "This resource provides eligibility and plan details from the"
        " processing of an CoverageEligibilityRequest resource."
    )
    assert inst.item[0].item[0].type == "display"
    assert inst.item[0].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[1].extension[0].valueInteger == 1
    assert inst.item[0].item[1].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[1].extension[1].valueString == "string"
    assert inst.item[0].item[1].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[1].item[0].linkId == "CoverageEligibilityResponse.id-flyover"
    )
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "CoverageEligibilityResponse.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "CoverageEligibilityResponse.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
    assert inst.item[0].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[2].item[0].linkId
        == "CoverageEligibilityResponse.meta-flyover"
    )
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content "
        "might not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "CoverageEligibilityResponse.meta"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Metadata about the resource"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[1].valueString == "uri"
    assert inst.item[0].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[3].item[0].linkId
        == "CoverageEligibilityResponse.implicitRules-flyover"
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert (
        inst.item[0].item[3].item[1].linkId
        == "CoverageEligibilityResponse.implicitRules.value"
    )
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "CoverageEligibilityResponse.implicitRules"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is False
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[4].extension[1].valueString == "code"
    assert inst.item[0].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[4].item[0].linkId
        == "CoverageEligibilityResponse.language-flyover"
    )
    assert inst.item[0].item[4].item[0].type == "display"
    assert (
        inst.item[0].item[4].item[1].linkId
        == "CoverageEligibilityResponse.language.value"
    )
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "CoverageEligibilityResponse.language"
    assert inst.item[0].item[4].repeats is True
    assert inst.item[0].item[4].required is False
    assert inst.item[0].item[4].type == "group"
    assert inst.item[0].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[5].item[0].linkId
        == "CoverageEligibilityResponse.text-flyover"
    )
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "CoverageEligibilityResponse.text"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert (
        inst.item[0].item[5].text
        == "Text summary of the resource, for human interpretation"
    )
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[6].item[0].linkId
        == "CoverageEligibilityResponse.contained-flyover"
    )
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "CoverageEligibilityResponse.contained"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].text == "Contained, inline Resources"
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[7].item[0].linkId
        == "CoverageEligibilityResponse.extension-flyover"
    )
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "CoverageEligibilityResponse.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional content defined by implementations"
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[8].item[0].linkId
        == "CoverageEligibilityResponse.modifierExtension-flyover"
    )
    assert inst.item[0].item[8].item[0].type == "display"
    assert (
        inst.item[0].item[8].linkId == "CoverageEligibilityResponse.modifierExtension"
    )
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[0].valueString == "Identifier"
    assert inst.item[0].item[9].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
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
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert (
        inst.item[0].item[9].item[0].linkId
        == "CoverageEligibilityResponse.identifier-flyover"
    )
    assert inst.item[0].item[9].item[0].text == (
        "A unique identifier assigned to this coverage eligiblity " "request."
    )
    assert inst.item[0].item[9].item[0].type == "display"
    assert (
        inst.item[0].item[9].item[1].linkId
        == "CoverageEligibilityResponse.identifier.label"
    )
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert (
        inst.item[0].item[9].item[2].linkId
        == "CoverageEligibilityResponse.identifier.system"
    )
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert (
        inst.item[0].item[9].item[3].linkId
        == "CoverageEligibilityResponse.identifier.value"
    )
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "CoverageEligibilityResponse.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert (
        inst.item[0].item[9].text
        == "Business Identifier for coverage eligiblity request"
    )
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "CoverageEligibilityResponse"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "CoverageEligibilityResponse resource"
    assert inst.item[0].type == "group"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.publisher == "Health Level Seven International (Financial Management)"
    assert inst.status == "draft"
    assert inst.version == "4.3.0"


def test_questionnaire_10(base_settings):
    """No. 10 tests collection for Questionnaire.
    Test File: coverageeligibilityresponse-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "coverageeligibilityresponse-questionnaire.json"
    )
    inst = questionnaire.Questionnaire.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "Questionnaire" == inst.resource_type

    impl_questionnaire_10(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "Questionnaire" == data["resourceType"]

    inst2 = questionnaire.Questionnaire(**data)
    impl_questionnaire_10(inst2)
