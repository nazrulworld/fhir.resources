# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import questionnaire


def impl_questionnaire_1(inst):
    assert inst.contained[0].id == "vs2"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[1].linkId == "display.ID"
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
    assert inst.item[0].item[2].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[3].item[0].linkId == "display.ID"
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
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
    assert inst.item[0].item[4].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[5].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[6].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[7].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[8].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Person.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[9].item[0].linkId == "display.ID"
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
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.contained[3].id == "vs5"
    assert inst.contained[4].id == "vs6"
    assert inst.contained[5].id == "vs7"
    assert inst.date == fhirtypes.DateTime.validate("2015-10-09T00:00:00+11:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[1].linkId == "display.ID"
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
    assert inst.item[0].item[2].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[3].item[0].linkId == "display.ID"
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
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
    assert inst.item[0].item[4].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[5].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[6].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[7].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[8].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[9].item[0].linkId == "display.ID"
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
    assert inst.publisher == "Health Level Seven International (Clinical Genomics)"
    assert inst.status == "draft"


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
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
    assert inst.id == "qs1"
    assert inst.identifier[0].system == "urn:ietf:rfc:3986"
    assert inst.item[0].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[1].linkId == "display.ID"
    assert inst.item[0].item[1].text == (
        "A collection of error, warning or information messages that "
        "result from a system action."
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
    assert inst.item[0].item[2].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[3].item[0].linkId == "display.ID"
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
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
    assert inst.item[0].item[4].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[5].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[6].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[7].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[8].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "OperationOutcome.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[9].item[0].linkId == "display.ID"
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
    assert inst.status == "draft"


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
    assert inst.contained[1].id == "vs3"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
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
    assert inst.item[0].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[1].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[2].item[0].linkId == "display.ID"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
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
    assert inst.item[0].item[3].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[4].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[5].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[6].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[7].item[0].linkId == "display.ID"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "ActivityDefinition.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[8].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[9].item[0].linkId == "display.ID"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "ActivityDefinition.url.value"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == (
        "Logical URI to reference this activity definition (globally " "unique)"
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


def test_questionnaire_4(base_settings):
    """No. 4 tests collection for Questionnaire.
    Test File: activitydefinition-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "activitydefinition-questionnaire.json"
    )
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
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
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
    assert inst.item[0].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[1].linkId == "display.ID"
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
    assert inst.item[0].item[2].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[3].item[0].linkId == "display.ID"
    assert inst.item[0].item[3].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
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
    assert inst.item[0].item[4].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[5].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[6].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[7].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[8].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "SearchParameter.extension"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[9].item[0].linkId == "display.ID"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].linkId == "SearchParameter.modifierExtension"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "Extensions that cannot be ignored"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "SearchParameter"
    assert inst.item[0].repeats is False
    assert inst.item[0].required is True
    assert inst.item[0].text == "Search Parameter for a resource"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (FHIR Infrastructure)"
    assert inst.status == "draft"


def test_questionnaire_5(base_settings):
    """No. 5 tests collection for Questionnaire.
    Test File: searchparameter-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "searchparameter-questionnaire.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
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
    assert inst.item[0].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[1].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[2].item[0].linkId == "display.ID"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
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
    assert inst.item[0].item[3].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[4].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[5].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[6].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[7].item[0].linkId == "display.ID"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "ExplanationOfBenefit.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[8].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[9].item[0].linkId == "display.ID"
    assert inst.item[0].item[9].item[0].text == "The EOB Business Identifier."
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
    assert inst.item[0].item[9].text == "Business Identifier"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "ExplanationOfBenefit"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Explanation of Benefit resource"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Financial Management)"
    assert inst.status == "draft"


def test_questionnaire_6(base_settings):
    """No. 6 tests collection for Questionnaire.
    Test File: explanationofbenefit-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "explanationofbenefit-questionnaire.json"
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
    assert inst.contained[0].id == "vs2"
    assert inst.contained[1].id == "vs3"
    assert inst.contained[2].id == "vs4"
    assert inst.contained[3].id == "vs5"
    assert inst.contained[4].id == "vs6"
    assert inst.contained[5].id == "vs7"
    assert inst.contained[6].id == "vs8"
    assert inst.contained[7].id == "vs9"
    assert inst.contained[8].id == "vs10"
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
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
    assert inst.item[0].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[1].item[0].linkId == "display.ID"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "CarePlan.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "CarePlan.id"
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
    assert inst.item[0].item[2].item[0].linkId == "display.ID"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "CarePlan.meta"
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
    assert inst.item[0].item[3].item[0].linkId == "display.ID"
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "CarePlan.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "CarePlan.implicitRules"
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
    assert inst.item[0].item[4].item[0].linkId == "display.ID"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "CarePlan.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "CarePlan.language"
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
    assert inst.item[0].item[5].item[0].linkId == "display.ID"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "CarePlan.text"
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
    assert inst.item[0].item[6].item[0].linkId == "display.ID"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "CarePlan.contained"
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
    assert inst.item[0].item[7].item[0].linkId == "display.ID"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "CarePlan.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[8].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "CarePlan.modifierExtension"
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
    assert inst.item[0].item[9].item[0].linkId == "display.ID"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "CarePlan.identifier.label"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == "label:"
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].item[2].linkId == "CarePlan.identifier.system"
    assert inst.item[0].item[9].item[2].repeats is False
    assert inst.item[0].item[9].item[2].required is False
    assert inst.item[0].item[9].item[2].text == "system:"
    assert inst.item[0].item[9].item[2].type == "string"
    assert inst.item[0].item[9].item[3].linkId == "CarePlan.identifier.value"
    assert inst.item[0].item[9].item[3].repeats is False
    assert inst.item[0].item[9].item[3].required is False
    assert inst.item[0].item[9].item[3].text == "value:"
    assert inst.item[0].item[9].item[3].type == "string"
    assert inst.item[0].item[9].linkId == "CarePlan.identifier"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].text == "External Ids for this plan"
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "CarePlan"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Healthcare plan for patient or group"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Patient Care)"
    assert inst.status == "draft"


def test_questionnaire_7(base_settings):
    """No. 7 tests collection for Questionnaire.
    Test File: careplan-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "careplan-questionnaire.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
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
    assert inst.item[0].item[0].linkId == "display.ID"
    assert inst.item[0].item[0].text == (
        "A code system resource specifies a set of codes drawn from "
        "one or more code systems."
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
    assert inst.item[0].item[1].item[0].linkId == "display.ID"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "CodeSystem.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "CodeSystem.id"
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
    assert inst.item[0].item[2].item[0].linkId == "display.ID"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "CodeSystem.meta"
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
    assert inst.item[0].item[3].item[0].linkId == "display.ID"
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "CodeSystem.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "CodeSystem.implicitRules"
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
    assert inst.item[0].item[4].item[0].linkId == "display.ID"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "CodeSystem.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "CodeSystem.language"
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
    assert inst.item[0].item[5].item[0].linkId == "display.ID"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "CodeSystem.text"
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
    assert inst.item[0].item[6].item[0].linkId == "display.ID"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "CodeSystem.contained"
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
    assert inst.item[0].item[7].item[0].linkId == "display.ID"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "CodeSystem.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[8].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "CodeSystem.modifierExtension"
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
    assert inst.item[0].item[9].item[0].linkId == "display.ID"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "CodeSystem.url.value"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert inst.item[0].item[9].item[1].text == (
        "Logical URI to reference this code system (globally unique) " "(Coding.system)"
    )
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].linkId == "CodeSystem.url"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "CodeSystem"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "A set of codes drawn from one or more code systems"
    assert inst.item[0].type == "group"
    assert inst.publisher == "Health Level Seven International (Vocabulary)"
    assert inst.status == "draft"


def test_questionnaire_8(base_settings):
    """No. 8 tests collection for Questionnaire.
    Test File: codesystem-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "codesystem-questionnaire.json"
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
    assert inst.date == fhirtypes.DateTime.validate("2017-04-19T07:44:43+10:00")
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
    assert inst.item[0].item[0].linkId == "display.ID"
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
    assert inst.item[0].item[1].item[0].linkId == "display.ID"
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "Library.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "Logical id of this artifact"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "Library.id"
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
    assert inst.item[0].item[2].item[0].linkId == "display.ID"
    assert inst.item[0].item[2].item[0].text == (
        "The metadata about the resource. This is content that is "
        "maintained by the infrastructure. Changes to the content may"
        " not always be associated with version changes to the "
        "resource."
    )
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "Library.meta"
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
    assert inst.item[0].item[3].item[0].linkId == "display.ID"
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "Library.implicitRules.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "A set of rules under which this content was created"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "Library.implicitRules"
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
    assert inst.item[0].item[4].item[0].linkId == "display.ID"
    assert inst.item[0].item[4].item[0].type == "display"
    assert inst.item[0].item[4].item[1].linkId == "Library.language.value"
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "language"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "Library.language"
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
    assert inst.item[0].item[5].item[0].linkId == "display.ID"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].linkId == "Library.text"
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
    assert inst.item[0].item[6].item[0].linkId == "display.ID"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].linkId == "Library.contained"
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
    assert inst.item[0].item[7].item[0].linkId == "display.ID"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].linkId == "Library.extension"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].text == "Additional Content defined by implementations"
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
    assert inst.item[0].item[8].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].linkId == "Library.modifierExtension"
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
    assert inst.item[0].item[9].item[0].linkId == "display.ID"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "Library.url.value"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert (
        inst.item[0].item[9].item[1].text
        == "Logical URI to reference this library (globally unique)"
    )
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].linkId == "Library.url"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "Library"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Represents a library of quality improvement components"
    assert inst.item[0].type == "group"
    assert (
        inst.publisher == "Health Level Seven International (Clinical Decision Support)"
    )
    assert inst.status == "draft"


def test_questionnaire_9(base_settings):
    """No. 9 tests collection for Questionnaire.
    Test File: library-questionnaire.json
    """
    filename = base_settings["unittest_data_dir"] / "library-questionnaire.json"
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
    assert inst.contained[3].id == "vs5"
    assert inst.contained[4].id == "vs6"
    assert inst.contained[5].id == "vs7"
    assert inst.contained[6].id == "vs8"
    assert inst.date == fhirtypes.DateTime.validate("2015-02-28T00:00:00+11:00")
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
    assert inst.item[0].item[0].linkId == "display.ID"
    assert inst.item[0].item[0].text == (
        "Captures constraints on each element within the resource, "
        "profile, or extension."
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
    assert inst.item[0].item[1].item[0].linkId == "display.ID"
    assert inst.item[0].item[1].item[0].text == (
        "unique id for the element within a resource (for internal "
        "references). This may be any string value that does not "
        "contain spaces."
    )
    assert inst.item[0].item[1].item[0].type == "display"
    assert inst.item[0].item[1].item[1].linkId == "ElementDefinition.id.value"
    assert inst.item[0].item[1].item[1].repeats is False
    assert inst.item[0].item[1].item[1].required is False
    assert inst.item[0].item[1].item[1].text == "xml:id (or equivalent in JSON)"
    assert inst.item[0].item[1].item[1].type == "string"
    assert inst.item[0].item[1].linkId == "ElementDefinition.id"
    assert inst.item[0].item[1].repeats is True
    assert inst.item[0].item[1].required is False
    assert inst.item[0].item[1].type == "group"
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
    assert inst.item[0].item[2].item[0].linkId == "display.ID"
    assert inst.item[0].item[2].item[0].type == "display"
    assert inst.item[0].item[2].linkId == "ElementDefinition.extension"
    assert inst.item[0].item[2].repeats is True
    assert inst.item[0].item[2].required is False
    assert inst.item[0].item[2].text == "Additional Content defined by implementations"
    assert inst.item[0].item[2].type == "group"
    assert inst.item[0].item[3].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "minOccurs"
    )
    assert inst.item[0].item[3].extension[0].valueInteger == 1
    assert inst.item[0].item[3].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[3].extension[1].valueInteger == 1
    assert inst.item[0].item[3].extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[3].extension[2].valueString == "string"
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
    assert inst.item[0].item[3].item[0].linkId == "display.ID"
    assert inst.item[0].item[3].item[0].text == (
        "The path identifies the element and is expressed as a "
        '"."-separated list of ancestor elements, beginning with '
        "the name of the resource or extension."
    )
    assert inst.item[0].item[3].item[0].type == "display"
    assert inst.item[0].item[3].item[1].linkId == "ElementDefinition.path.value"
    assert inst.item[0].item[3].item[1].repeats is False
    assert inst.item[0].item[3].item[1].required is False
    assert (
        inst.item[0].item[3].item[1].text
        == "Path of the element in the hierarchy of elements"
    )
    assert inst.item[0].item[3].item[1].type == "string"
    assert inst.item[0].item[3].linkId == "ElementDefinition.path"
    assert inst.item[0].item[3].repeats is True
    assert inst.item[0].item[3].required is True
    assert inst.item[0].item[3].type == "group"
    assert inst.item[0].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[4].extension[0].valueInteger == 0
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
    assert inst.item[0].item[4].item[0].linkId == "display.ID"
    assert inst.item[0].item[4].item[0].type == "display"
    assert (
        inst.item[0].item[4].item[1].linkId == "ElementDefinition.representation.value"
    )
    assert inst.item[0].item[4].item[1].repeats is False
    assert inst.item[0].item[4].item[1].required is False
    assert inst.item[0].item[4].item[1].text == "representation"
    assert inst.item[0].item[4].item[1].type == "choice"
    assert inst.item[0].item[4].linkId == "ElementDefinition.representation"
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
    assert inst.item[0].item[5].extension[1].valueString == "string"
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
    assert inst.item[0].item[5].item[0].linkId == "display.ID"
    assert inst.item[0].item[5].item[0].type == "display"
    assert inst.item[0].item[5].item[1].linkId == "ElementDefinition.sliceName.value"
    assert inst.item[0].item[5].item[1].repeats is False
    assert inst.item[0].item[5].item[1].required is False
    assert (
        inst.item[0].item[5].item[1].text
        == "Name for this particular element (in a set of slices)"
    )
    assert inst.item[0].item[5].item[1].type == "string"
    assert inst.item[0].item[5].linkId == "ElementDefinition.sliceName"
    assert inst.item[0].item[5].repeats is True
    assert inst.item[0].item[5].required is False
    assert inst.item[0].item[5].type == "group"
    assert inst.item[0].item[6].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[6].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[6].extension[1].valueString == "string"
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
    assert inst.item[0].item[6].item[0].linkId == "display.ID"
    assert inst.item[0].item[6].item[0].type == "display"
    assert inst.item[0].item[6].item[1].linkId == "ElementDefinition.label.value"
    assert inst.item[0].item[6].item[1].repeats is False
    assert inst.item[0].item[6].item[1].required is False
    assert (
        inst.item[0].item[6].item[1].text
        == "Name for element to display with or prompt for element"
    )
    assert inst.item[0].item[6].item[1].type == "string"
    assert inst.item[0].item[6].linkId == "ElementDefinition.label"
    assert inst.item[0].item[6].repeats is True
    assert inst.item[0].item[6].required is False
    assert inst.item[0].item[6].type == "group"
    assert inst.item[0].item[7].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[7].extension[0].valueString == "Coding"
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
    assert inst.item[0].item[7].item[0].linkId == "display.ID"
    assert inst.item[0].item[7].item[0].type == "display"
    assert inst.item[0].item[7].item[1].linkId == "ElementDefinition.code.value"
    assert inst.item[0].item[7].item[1].repeats is False
    assert inst.item[0].item[7].item[1].required is False
    assert inst.item[0].item[7].item[1].text == "Corresponding codes in terminologies"
    assert inst.item[0].item[7].item[1].type == "open-choice"
    assert inst.item[0].item[7].linkId == "ElementDefinition.code"
    assert inst.item[0].item[7].repeats is True
    assert inst.item[0].item[7].required is False
    assert inst.item[0].item[7].type == "group"
    assert inst.item[0].item[8].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[8].extension[0].valueInteger == 0
    assert inst.item[0].item[8].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[0].type == "display"
    assert inst.item[0].item[8].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0].item[8].item[1].extension[0].valueCodeableConcept.coding[0].code
        == "flyover"
    )
    assert (
        inst.item[0].item[8].item[1].extension[0].valueCodeableConcept.coding[0].display
        == "Fly-over"
    )
    assert (
        inst.item[0].item[8].item[1].extension[0].valueCodeableConcept.coding[0].system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[1].linkId == "display.ID"
    assert inst.item[0].item[8].item[1].type == "display"
    assert inst.item[0].item[8].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[8].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[8].item[2].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[8].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[8].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[2]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[2]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[2]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[2].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[2].item[0].text == (
        "unique id for the element within a resource (for internal "
        "references). This may be any string value that does not "
        "contain spaces."
    )
    assert inst.item[0].item[8].item[2].item[0].type == "display"
    assert (
        inst.item[0].item[8].item[2].item[1].linkId
        == "ElementDefinition.slicing.id.value"
    )
    assert inst.item[0].item[8].item[2].item[1].repeats is False
    assert inst.item[0].item[8].item[2].item[1].required is False
    assert inst.item[0].item[8].item[2].item[1].text == "xml:id (or equivalent in JSON)"
    assert inst.item[0].item[8].item[2].item[1].type == "string"
    assert inst.item[0].item[8].item[2].linkId == "ElementDefinition.slicing.id"
    assert inst.item[0].item[8].item[2].repeats is True
    assert inst.item[0].item[8].item[2].required is False
    assert inst.item[0].item[8].item[2].type == "group"
    assert inst.item[0].item[8].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[3]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[3]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[3]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[3].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[3].item[0].type == "display"
    assert inst.item[0].item[8].item[3].linkId == "ElementDefinition.slicing.extension"
    assert inst.item[0].item[8].item[3].repeats is True
    assert inst.item[0].item[8].item[3].required is False
    assert (
        inst.item[0].item[8].item[3].text
        == "Additional Content defined by implementations"
    )
    assert inst.item[0].item[8].item[3].type == "group"
    assert inst.item[0].item[8].item[4].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[4].item[0].type == "display"
    assert inst.item[0].item[8].item[4].item[1].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[1]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[1]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[1]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[4].item[1].linkId == "display.ID"
    assert inst.item[0].item[8].item[4].item[1].type == "display"
    assert inst.item[0].item[8].item[4].item[2].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[8].item[4].item[2].extension[0].valueInteger == 1
    assert inst.item[0].item[8].item[4].item[2].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[8].item[4].item[2].extension[1].valueString == "string"
    assert inst.item[0].item[8].item[4].item[2].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[2]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[2]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[2]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[4].item[2].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[4].item[2].item[0].text == (
        "unique id for the element within a resource (for internal "
        "references). This may be any string value that does not "
        "contain spaces."
    )
    assert inst.item[0].item[8].item[4].item[2].item[0].type == "display"
    assert (
        inst.item[0].item[8].item[4].item[2].item[1].linkId
        == "ElementDefinition.slicing.discriminator.id.value"
    )
    assert inst.item[0].item[8].item[4].item[2].item[1].repeats is False
    assert inst.item[0].item[8].item[4].item[2].item[1].required is False
    assert (
        inst.item[0].item[8].item[4].item[2].item[1].text
        == "xml:id (or equivalent in JSON)"
    )
    assert inst.item[0].item[8].item[4].item[2].item[1].type == "string"
    assert (
        inst.item[0].item[8].item[4].item[2].linkId
        == "ElementDefinition.slicing.discriminator.id"
    )
    assert inst.item[0].item[8].item[4].item[2].repeats is True
    assert inst.item[0].item[8].item[4].item[2].required is False
    assert inst.item[0].item[8].item[4].item[2].type == "group"
    assert inst.item[0].item[8].item[4].item[3].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[3]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[3]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[3]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[4].item[3].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[4].item[3].item[0].type == "display"
    assert (
        inst.item[0].item[8].item[4].item[3].linkId
        == "ElementDefinition.slicing.discriminator.extension"
    )
    assert inst.item[0].item[8].item[4].item[3].repeats is True
    assert inst.item[0].item[8].item[4].item[3].required is False
    assert (
        inst.item[0].item[8].item[4].item[3].text
        == "Additional Content defined by implementations"
    )
    assert inst.item[0].item[8].item[4].item[3].type == "group"
    assert inst.item[0].item[8].item[4].item[4].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "minOccurs"
    )
    assert inst.item[0].item[8].item[4].item[4].extension[0].valueInteger == 1
    assert inst.item[0].item[8].item[4].item[4].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[8].item[4].item[4].extension[1].valueInteger == 1
    assert inst.item[0].item[8].item[4].item[4].extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[8].item[4].item[4].extension[2].valueString == "code"
    assert inst.item[0].item[8].item[4].item[4].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[4]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[4]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[4]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[4].item[4].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[4].item[4].item[0].text == (
        "How the element value is interpreted when discrimination is " "evaluated."
    )
    assert inst.item[0].item[8].item[4].item[4].item[0].type == "display"
    assert (
        inst.item[0].item[8].item[4].item[4].item[1].linkId
        == "ElementDefinition.slicing.discriminator.type.value"
    )
    assert inst.item[0].item[8].item[4].item[4].item[1].repeats is False
    assert inst.item[0].item[8].item[4].item[4].item[1].required is False
    assert inst.item[0].item[8].item[4].item[4].item[1].text == "type"
    assert inst.item[0].item[8].item[4].item[4].item[1].type == "choice"
    assert (
        inst.item[0].item[8].item[4].item[4].linkId
        == "ElementDefinition.slicing.discriminator.type"
    )
    assert inst.item[0].item[8].item[4].item[4].repeats is True
    assert inst.item[0].item[8].item[4].item[4].required is True
    assert inst.item[0].item[8].item[4].item[4].type == "group"
    assert inst.item[0].item[8].item[4].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "minOccurs"
    )
    assert inst.item[0].item[8].item[4].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[8].item[4].item[5].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[8].item[4].item[5].extension[1].valueInteger == 1
    assert inst.item[0].item[8].item[4].item[5].extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[8].item[4].item[5].extension[2].valueString == "string"
    assert inst.item[0].item[8].item[4].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[5]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[5]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[4]
        .item[5]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[4].item[5].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[4].item[5].item[0].type == "display"
    assert (
        inst.item[0].item[8].item[4].item[5].item[1].linkId
        == "ElementDefinition.slicing.discriminator.path.value"
    )
    assert inst.item[0].item[8].item[4].item[5].item[1].repeats is False
    assert inst.item[0].item[8].item[4].item[5].item[1].required is False
    assert inst.item[0].item[8].item[4].item[5].item[1].text == "Path to element value"
    assert inst.item[0].item[8].item[4].item[5].item[1].type == "string"
    assert (
        inst.item[0].item[8].item[4].item[5].linkId
        == "ElementDefinition.slicing.discriminator.path"
    )
    assert inst.item[0].item[8].item[4].item[5].repeats is True
    assert inst.item[0].item[8].item[4].item[5].required is True
    assert inst.item[0].item[8].item[4].item[5].type == "group"
    assert (
        inst.item[0].item[8].item[4].linkId == "ElementDefinition.slicing.discriminator"
    )
    assert inst.item[0].item[8].item[4].repeats is True
    assert inst.item[0].item[8].item[4].required is False
    assert (
        inst.item[0].item[8].item[4].text
        == "Element values that are used to distinguish the slices"
    )
    assert inst.item[0].item[8].item[4].type == "group"
    assert inst.item[0].item[8].item[5].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[8].item[5].extension[0].valueInteger == 1
    assert inst.item[0].item[8].item[5].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[8].item[5].extension[1].valueString == "string"
    assert inst.item[0].item[8].item[5].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[5]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[5]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[5]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[5].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[5].item[0].type == "display"
    assert (
        inst.item[0].item[8].item[5].item[1].linkId
        == "ElementDefinition.slicing.description.value"
    )
    assert inst.item[0].item[8].item[5].item[1].repeats is False
    assert inst.item[0].item[8].item[5].item[1].required is False
    assert (
        inst.item[0].item[8].item[5].item[1].text
        == "Text description of how slicing works (or not)"
    )
    assert inst.item[0].item[8].item[5].item[1].type == "string"
    assert (
        inst.item[0].item[8].item[5].linkId == "ElementDefinition.slicing.description"
    )
    assert inst.item[0].item[8].item[5].repeats is True
    assert inst.item[0].item[8].item[5].required is False
    assert inst.item[0].item[8].item[5].type == "group"
    assert inst.item[0].item[8].item[6].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[8].item[6].extension[0].valueInteger == 1
    assert inst.item[0].item[8].item[6].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[8].item[6].extension[1].valueString == "boolean"
    assert inst.item[0].item[8].item[6].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[6]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[6]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[6]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[6].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[6].item[0].type == "display"
    assert (
        inst.item[0].item[8].item[6].item[1].linkId
        == "ElementDefinition.slicing.ordered.value"
    )
    assert inst.item[0].item[8].item[6].item[1].repeats is False
    assert inst.item[0].item[8].item[6].item[1].required is False
    assert (
        inst.item[0].item[8].item[6].item[1].text
        == "If elements must be in same order as slices"
    )
    assert inst.item[0].item[8].item[6].item[1].type == "boolean"
    assert inst.item[0].item[8].item[6].linkId == "ElementDefinition.slicing.ordered"
    assert inst.item[0].item[8].item[6].repeats is True
    assert inst.item[0].item[8].item[6].required is False
    assert inst.item[0].item[8].item[6].type == "group"
    assert inst.item[0].item[8].item[7].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "minOccurs"
    )
    assert inst.item[0].item[8].item[7].extension[0].valueInteger == 1
    assert inst.item[0].item[8].item[7].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[8].item[7].extension[1].valueInteger == 1
    assert inst.item[0].item[8].item[7].extension[2].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[8].item[7].extension[2].valueString == "code"
    assert inst.item[0].item[8].item[7].item[0].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "itemControl"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[7]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .code
        == "flyover"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[7]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .display
        == "Fly-over"
    )
    assert (
        inst.item[0]
        .item[8]
        .item[7]
        .item[0]
        .extension[0]
        .valueCodeableConcept.coding[0]
        .system
        == "http://hl7.org/fhir/questionnaire-item-control"
    )
    assert inst.item[0].item[8].item[7].item[0].linkId == "display.ID"
    assert inst.item[0].item[8].item[7].item[0].type == "display"
    assert (
        inst.item[0].item[8].item[7].item[1].linkId
        == "ElementDefinition.slicing.rules.value"
    )
    assert inst.item[0].item[8].item[7].item[1].repeats is False
    assert inst.item[0].item[8].item[7].item[1].required is False
    assert inst.item[0].item[8].item[7].item[1].text == "rules"
    assert inst.item[0].item[8].item[7].item[1].type == "choice"
    assert inst.item[0].item[8].item[7].linkId == "ElementDefinition.slicing.rules"
    assert inst.item[0].item[8].item[7].repeats is True
    assert inst.item[0].item[8].item[7].required is True
    assert inst.item[0].item[8].item[7].type == "group"
    assert inst.item[0].item[8].linkId == "ElementDefinition.slicing"
    assert inst.item[0].item[8].repeats is True
    assert inst.item[0].item[8].required is False
    assert inst.item[0].item[8].text == "This element is sliced - slices follow"
    assert inst.item[0].item[8].type == "group"
    assert inst.item[0].item[9].extension[0].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "maxOccurs"
    )
    assert inst.item[0].item[9].extension[0].valueInteger == 0
    assert inst.item[0].item[9].extension[1].url == (
        "http://hl7.org/fhir/StructureDefinition/questionnaire-" "fhirType"
    )
    assert inst.item[0].item[9].extension[1].valueString == "string"
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
    assert inst.item[0].item[9].item[0].linkId == "display.ID"
    assert inst.item[0].item[9].item[0].type == "display"
    assert inst.item[0].item[9].item[1].linkId == "ElementDefinition.short.value"
    assert inst.item[0].item[9].item[1].repeats is False
    assert inst.item[0].item[9].item[1].required is False
    assert (
        inst.item[0].item[9].item[1].text
        == "Concise definition for space-constrained presentation"
    )
    assert inst.item[0].item[9].item[1].type == "string"
    assert inst.item[0].item[9].linkId == "ElementDefinition.short"
    assert inst.item[0].item[9].repeats is True
    assert inst.item[0].item[9].required is False
    assert inst.item[0].item[9].type == "group"
    assert inst.item[0].linkId == "ElementDefinition"
    assert inst.item[0].repeats is True
    assert inst.item[0].required is False
    assert inst.item[0].text == "Definition of an element in a resource or extension"
    assert inst.item[0].type == "group"
    assert (
        inst.publisher == "Health Level Seven International (Orders and Observations)"
    )
    assert inst.status == "draft"


def test_questionnaire_10(base_settings):
    """No. 10 tests collection for Questionnaire.
    Test File: elementdefinition-de-questionnaire.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "elementdefinition-de-questionnaire.json"
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
