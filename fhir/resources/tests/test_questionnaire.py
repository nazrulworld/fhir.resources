# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Questionnaire
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""

import copy
import io
import json
import os
import unittest

import pytest

from .. import questionnaire
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class QuestionnaireTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Questionnaire", js["resourceType"])

        def _do_clean(container):
            for item in copy.copy(container):
                if "linkId" not in item:
                    index = container.index(item)
                    item["linkId"] = "Fake.id"
                    container[index] = item
                if "item" in item:
                    _do_clean(item["item"])

        # do some extra!
        _do_clean(js["item"])

        return questionnaire.Questionnaire(js)

    def testQuestionnaire1(self):
        inst = self.instantiate_from("person-questionnaire.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire1(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire1(inst2)

    def implQuestionnaire1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("qs1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].text),
            force_bytes(
                "Demographics and administrative information about a person independent of a specific health-related context."
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].item[1].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[2].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[1].valueString),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].linkId),
            force_bytes("Person.id.value"),
        )
        self.assertFalse(inst.item[0].item[2].item[1].repeats)
        self.assertFalse(inst.item[0].item[2].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].text),
            force_bytes("Logical id of this artifact"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].linkId), force_bytes("Person.id")
        )
        self.assertTrue(inst.item[0].item[2].repeats)
        self.assertFalse(inst.item[0].item[2].required)
        self.assertEqual(force_bytes(inst.item[0].item[2].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[3].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].text),
            force_bytes(
                "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].linkId), force_bytes("Person.meta")
        )
        self.assertTrue(inst.item[0].item[3].repeats)
        self.assertFalse(inst.item[0].item[3].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].text),
            force_bytes("Metadata about the resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[3].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[4].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].linkId),
            force_bytes("Person.implicitRules.value"),
        )
        self.assertFalse(inst.item[0].item[4].item[1].repeats)
        self.assertFalse(inst.item[0].item[4].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].text),
            force_bytes("A set of rules under which this content was created"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].linkId),
            force_bytes("Person.implicitRules"),
        )
        self.assertTrue(inst.item[0].item[4].repeats)
        self.assertFalse(inst.item[0].item[4].required)
        self.assertEqual(force_bytes(inst.item[0].item[4].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[5].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[1].valueString),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].linkId),
            force_bytes("Person.language.value"),
        )
        self.assertFalse(inst.item[0].item[5].item[1].repeats)
        self.assertFalse(inst.item[0].item[5].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].text), force_bytes("language")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].type), force_bytes("choice")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].linkId), force_bytes("Person.language")
        )
        self.assertTrue(inst.item[0].item[5].repeats)
        self.assertFalse(inst.item[0].item[5].required)
        self.assertEqual(force_bytes(inst.item[0].item[5].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[6].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[6].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].linkId), force_bytes("Person.text")
        )
        self.assertTrue(inst.item[0].item[6].repeats)
        self.assertFalse(inst.item[0].item[6].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].text),
            force_bytes("Text summary of the resource, for human interpretation"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[6].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].linkId), force_bytes("Person.contained")
        )
        self.assertTrue(inst.item[0].item[7].repeats)
        self.assertFalse(inst.item[0].item[7].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[7].text),
            force_bytes("Contained, inline Resources"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[7].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].linkId), force_bytes("Person.extension")
        )
        self.assertTrue(inst.item[0].item[8].repeats)
        self.assertFalse(inst.item[0].item[8].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[8].text),
            force_bytes("Additional content defined by implementations"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[8].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].linkId),
            force_bytes("Person.modifierExtension"),
        )
        self.assertTrue(inst.item[0].item[9].repeats)
        self.assertFalse(inst.item[0].item[9].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].text),
            force_bytes("Extensions that cannot be ignored"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[9].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.item[0].linkId), force_bytes("Person"))
        self.assertTrue(inst.item[0].repeats)
        self.assertFalse(inst.item[0].required)
        self.assertEqual(
            force_bytes(inst.item[0].text), force_bytes("A generic person record")
        )
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes("Health Level Seven International (Patient Administration)"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testQuestionnaire2(self):
        inst = self.instantiate_from("hlaresult-questionnaire.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire2(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire2(inst2)

    def implQuestionnaire2(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("vs2"))
        self.assertEqual(inst.date.date, FHIRDate("2015-10-09T00:00:00+11:00").date)
        self.assertEqual(inst.date.as_json(), "2015-10-09T00:00:00+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("qs1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[1].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[2].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[1].valueString),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].linkId),
            force_bytes("DiagnosticReport.id.value"),
        )
        self.assertFalse(inst.item[0].item[2].item[1].repeats)
        self.assertFalse(inst.item[0].item[2].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].text),
            force_bytes("Logical id of this artifact"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].linkId), force_bytes("DiagnosticReport.id")
        )
        self.assertTrue(inst.item[0].item[2].repeats)
        self.assertFalse(inst.item[0].item[2].required)
        self.assertEqual(force_bytes(inst.item[0].item[2].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[3].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].text),
            force_bytes(
                "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].linkId),
            force_bytes("DiagnosticReport.meta"),
        )
        self.assertTrue(inst.item[0].item[3].repeats)
        self.assertFalse(inst.item[0].item[3].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].text),
            force_bytes("Metadata about the resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[3].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[4].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].linkId),
            force_bytes("DiagnosticReport.implicitRules.value"),
        )
        self.assertFalse(inst.item[0].item[4].item[1].repeats)
        self.assertFalse(inst.item[0].item[4].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].text),
            force_bytes("A set of rules under which this content was created"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].linkId),
            force_bytes("DiagnosticReport.implicitRules"),
        )
        self.assertTrue(inst.item[0].item[4].repeats)
        self.assertFalse(inst.item[0].item[4].required)
        self.assertEqual(force_bytes(inst.item[0].item[4].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[5].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[1].valueString),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].linkId),
            force_bytes("DiagnosticReport.language.value"),
        )
        self.assertFalse(inst.item[0].item[5].item[1].repeats)
        self.assertFalse(inst.item[0].item[5].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].text), force_bytes("language")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].type), force_bytes("choice")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].linkId),
            force_bytes("DiagnosticReport.language"),
        )
        self.assertTrue(inst.item[0].item[5].repeats)
        self.assertFalse(inst.item[0].item[5].required)
        self.assertEqual(force_bytes(inst.item[0].item[5].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[6].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[6].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].linkId),
            force_bytes("DiagnosticReport.text"),
        )
        self.assertTrue(inst.item[0].item[6].repeats)
        self.assertFalse(inst.item[0].item[6].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].text),
            force_bytes("Text summary of the resource, for human interpretation"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[6].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].linkId),
            force_bytes("DiagnosticReport.contained"),
        )
        self.assertTrue(inst.item[0].item[7].repeats)
        self.assertFalse(inst.item[0].item[7].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[7].text),
            force_bytes("Contained, inline Resources"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[7].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].text), force_bytes("An Extension")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].linkId),
            force_bytes("DiagnosticReport.extension"),
        )
        self.assertTrue(inst.item[0].item[8].repeats)
        self.assertFalse(inst.item[0].item[8].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[8].text), force_bytes("Extension")
        )
        self.assertEqual(force_bytes(inst.item[0].item[8].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].linkId),
            force_bytes("DiagnosticReport.modifierExtension"),
        )
        self.assertTrue(inst.item[0].item[9].repeats)
        self.assertFalse(inst.item[0].item[9].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].text),
            force_bytes("Extensions that cannot be ignored"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[9].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].linkId), force_bytes("DiagnosticReport")
        )
        self.assertTrue(inst.item[0].repeats)
        self.assertFalse(inst.item[0].required)
        self.assertEqual(
            force_bytes(inst.item[0].text),
            force_bytes(
                "A Diagnostic report - a combination of request information, atomic results, images, interpretation, as well as formatted reports"
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes("Health Level Seven International (Clinical Genomics)"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testQuestionnaire3(self):
        inst = self.instantiate_from("operationoutcome-questionnaire.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire3(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire3(inst2)

    def implQuestionnaire3(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("qs1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].text),
            force_bytes(
                "Can result from the failure of a REST call or be part of the response message returned from a request message."
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].text),
            force_bytes(
                "A collection of error, warning, or information messages that result from a system action."
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].item[1].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[2].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[1].valueString),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].linkId),
            force_bytes("OperationOutcome.id.value"),
        )
        self.assertFalse(inst.item[0].item[2].item[1].repeats)
        self.assertFalse(inst.item[0].item[2].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].text),
            force_bytes("Logical id of this artifact"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].linkId), force_bytes("OperationOutcome.id")
        )
        self.assertTrue(inst.item[0].item[2].repeats)
        self.assertFalse(inst.item[0].item[2].required)
        self.assertEqual(force_bytes(inst.item[0].item[2].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[3].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].text),
            force_bytes(
                "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].linkId),
            force_bytes("OperationOutcome.meta"),
        )
        self.assertTrue(inst.item[0].item[3].repeats)
        self.assertFalse(inst.item[0].item[3].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].text),
            force_bytes("Metadata about the resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[3].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[4].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].linkId),
            force_bytes("OperationOutcome.implicitRules.value"),
        )
        self.assertFalse(inst.item[0].item[4].item[1].repeats)
        self.assertFalse(inst.item[0].item[4].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].text),
            force_bytes("A set of rules under which this content was created"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].linkId),
            force_bytes("OperationOutcome.implicitRules"),
        )
        self.assertTrue(inst.item[0].item[4].repeats)
        self.assertFalse(inst.item[0].item[4].required)
        self.assertEqual(force_bytes(inst.item[0].item[4].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[5].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[1].valueString),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].linkId),
            force_bytes("OperationOutcome.language.value"),
        )
        self.assertFalse(inst.item[0].item[5].item[1].repeats)
        self.assertFalse(inst.item[0].item[5].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].text), force_bytes("language")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].type), force_bytes("choice")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].linkId),
            force_bytes("OperationOutcome.language"),
        )
        self.assertTrue(inst.item[0].item[5].repeats)
        self.assertFalse(inst.item[0].item[5].required)
        self.assertEqual(force_bytes(inst.item[0].item[5].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[6].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[6].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].linkId),
            force_bytes("OperationOutcome.text"),
        )
        self.assertTrue(inst.item[0].item[6].repeats)
        self.assertFalse(inst.item[0].item[6].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].text),
            force_bytes("Text summary of the resource, for human interpretation"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[6].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].linkId),
            force_bytes("OperationOutcome.contained"),
        )
        self.assertTrue(inst.item[0].item[7].repeats)
        self.assertFalse(inst.item[0].item[7].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[7].text),
            force_bytes("Contained, inline Resources"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[7].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].linkId),
            force_bytes("OperationOutcome.extension"),
        )
        self.assertTrue(inst.item[0].item[8].repeats)
        self.assertFalse(inst.item[0].item[8].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[8].text),
            force_bytes("Additional content defined by implementations"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[8].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].linkId),
            force_bytes("OperationOutcome.modifierExtension"),
        )
        self.assertTrue(inst.item[0].item[9].repeats)
        self.assertFalse(inst.item[0].item[9].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].text),
            force_bytes("Extensions that cannot be ignored"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[9].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].linkId), force_bytes("OperationOutcome")
        )
        self.assertTrue(inst.item[0].repeats)
        self.assertFalse(inst.item[0].required)
        self.assertEqual(
            force_bytes(inst.item[0].text),
            force_bytes("Information about the success/failure of an action"),
        )
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes("Health Level Seven International (FHIR Infrastructure)"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testQuestionnaire4(self):
        inst = self.instantiate_from("eventdefinition-questionnaire.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire4(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire4(inst2)

    def implQuestionnaire4(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("vs2"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("qs1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].text),
            force_bytes(
                "The EventDefinition resource provides a reusable description of when a particular event can occur."
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[1].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].valueString),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].linkId),
            force_bytes("EventDefinition.id.value"),
        )
        self.assertFalse(inst.item[0].item[1].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].text),
            force_bytes("Logical id of this artifact"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].linkId), force_bytes("EventDefinition.id")
        )
        self.assertTrue(inst.item[0].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].required)
        self.assertEqual(force_bytes(inst.item[0].item[1].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[2].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].text),
            force_bytes(
                "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].linkId),
            force_bytes("EventDefinition.meta"),
        )
        self.assertTrue(inst.item[0].item[2].repeats)
        self.assertFalse(inst.item[0].item[2].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].text),
            force_bytes("Metadata about the resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[2].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[3].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].linkId),
            force_bytes("EventDefinition.implicitRules.value"),
        )
        self.assertFalse(inst.item[0].item[3].item[1].repeats)
        self.assertFalse(inst.item[0].item[3].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].text),
            force_bytes("A set of rules under which this content was created"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].linkId),
            force_bytes("EventDefinition.implicitRules"),
        )
        self.assertTrue(inst.item[0].item[3].repeats)
        self.assertFalse(inst.item[0].item[3].required)
        self.assertEqual(force_bytes(inst.item[0].item[3].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[4].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].valueString),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].linkId),
            force_bytes("EventDefinition.language.value"),
        )
        self.assertFalse(inst.item[0].item[4].item[1].repeats)
        self.assertFalse(inst.item[0].item[4].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].text), force_bytes("language")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].type), force_bytes("choice")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].linkId),
            force_bytes("EventDefinition.language"),
        )
        self.assertTrue(inst.item[0].item[4].repeats)
        self.assertFalse(inst.item[0].item[4].required)
        self.assertEqual(force_bytes(inst.item[0].item[4].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[5].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].linkId),
            force_bytes("EventDefinition.text"),
        )
        self.assertTrue(inst.item[0].item[5].repeats)
        self.assertFalse(inst.item[0].item[5].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].text),
            force_bytes("Text summary of the resource, for human interpretation"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[5].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].linkId),
            force_bytes("EventDefinition.contained"),
        )
        self.assertTrue(inst.item[0].item[6].repeats)
        self.assertFalse(inst.item[0].item[6].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].text),
            force_bytes("Contained, inline Resources"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[6].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].linkId),
            force_bytes("EventDefinition.extension"),
        )
        self.assertTrue(inst.item[0].item[7].repeats)
        self.assertFalse(inst.item[0].item[7].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[7].text),
            force_bytes("Additional content defined by implementations"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[7].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].linkId),
            force_bytes("EventDefinition.modifierExtension"),
        )
        self.assertTrue(inst.item[0].item[8].repeats)
        self.assertFalse(inst.item[0].item[8].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[8].text),
            force_bytes("Extensions that cannot be ignored"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[8].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[9].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].linkId),
            force_bytes("EventDefinition.url.value"),
        )
        self.assertFalse(inst.item[0].item[9].item[1].repeats)
        self.assertFalse(inst.item[0].item[9].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].text),
            force_bytes(
                "Canonical identifier for this event definition, represented as a URI (globally unique)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].linkId), force_bytes("EventDefinition.url")
        )
        self.assertTrue(inst.item[0].item[9].repeats)
        self.assertFalse(inst.item[0].item[9].required)
        self.assertEqual(force_bytes(inst.item[0].item[9].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].linkId), force_bytes("EventDefinition")
        )
        self.assertTrue(inst.item[0].repeats)
        self.assertFalse(inst.item[0].required)
        self.assertEqual(
            force_bytes(inst.item[0].text),
            force_bytes("A description of when an event can occur"),
        )
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes("Health Level Seven International (Clinical Decision Support)"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testQuestionnaire5(self):
        inst = self.instantiate_from("activitydefinition-questionnaire.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire5(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire5(inst2)

    def implQuestionnaire5(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("vs2"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("vs3"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("vs4"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("qs1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].text),
            force_bytes(
                "This resource allows for the definition of some activity to be performed, independent of a particular patient, practitioner, or other performance context."
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[1].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].valueString),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].linkId),
            force_bytes("ActivityDefinition.id.value"),
        )
        self.assertFalse(inst.item[0].item[1].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].text),
            force_bytes("Logical id of this artifact"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].linkId),
            force_bytes("ActivityDefinition.id"),
        )
        self.assertTrue(inst.item[0].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].required)
        self.assertEqual(force_bytes(inst.item[0].item[1].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[2].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].text),
            force_bytes(
                "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].linkId),
            force_bytes("ActivityDefinition.meta"),
        )
        self.assertTrue(inst.item[0].item[2].repeats)
        self.assertFalse(inst.item[0].item[2].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].text),
            force_bytes("Metadata about the resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[2].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[3].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].linkId),
            force_bytes("ActivityDefinition.implicitRules.value"),
        )
        self.assertFalse(inst.item[0].item[3].item[1].repeats)
        self.assertFalse(inst.item[0].item[3].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].text),
            force_bytes("A set of rules under which this content was created"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].linkId),
            force_bytes("ActivityDefinition.implicitRules"),
        )
        self.assertTrue(inst.item[0].item[3].repeats)
        self.assertFalse(inst.item[0].item[3].required)
        self.assertEqual(force_bytes(inst.item[0].item[3].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[4].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].valueString),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].linkId),
            force_bytes("ActivityDefinition.language.value"),
        )
        self.assertFalse(inst.item[0].item[4].item[1].repeats)
        self.assertFalse(inst.item[0].item[4].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].text), force_bytes("language")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].type), force_bytes("choice")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].linkId),
            force_bytes("ActivityDefinition.language"),
        )
        self.assertTrue(inst.item[0].item[4].repeats)
        self.assertFalse(inst.item[0].item[4].required)
        self.assertEqual(force_bytes(inst.item[0].item[4].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[5].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].linkId),
            force_bytes("ActivityDefinition.text"),
        )
        self.assertTrue(inst.item[0].item[5].repeats)
        self.assertFalse(inst.item[0].item[5].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].text),
            force_bytes("Text summary of the resource, for human interpretation"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[5].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].linkId),
            force_bytes("ActivityDefinition.contained"),
        )
        self.assertTrue(inst.item[0].item[6].repeats)
        self.assertFalse(inst.item[0].item[6].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].text),
            force_bytes("Contained, inline Resources"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[6].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].linkId),
            force_bytes("ActivityDefinition.extension"),
        )
        self.assertTrue(inst.item[0].item[7].repeats)
        self.assertFalse(inst.item[0].item[7].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[7].text),
            force_bytes("Additional content defined by implementations"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[7].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].linkId),
            force_bytes("ActivityDefinition.modifierExtension"),
        )
        self.assertTrue(inst.item[0].item[8].repeats)
        self.assertFalse(inst.item[0].item[8].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[8].text),
            force_bytes("Extensions that cannot be ignored"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[8].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[9].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].linkId),
            force_bytes("ActivityDefinition.url.value"),
        )
        self.assertFalse(inst.item[0].item[9].item[1].repeats)
        self.assertFalse(inst.item[0].item[9].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].text),
            force_bytes(
                "Canonical identifier for this activity definition, represented as a URI (globally unique)"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].linkId),
            force_bytes("ActivityDefinition.url"),
        )
        self.assertTrue(inst.item[0].item[9].repeats)
        self.assertFalse(inst.item[0].item[9].required)
        self.assertEqual(force_bytes(inst.item[0].item[9].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].linkId), force_bytes("ActivityDefinition")
        )
        self.assertTrue(inst.item[0].repeats)
        self.assertFalse(inst.item[0].required)
        self.assertEqual(
            force_bytes(inst.item[0].text),
            force_bytes(
                "The definition of a specific activity to be taken, independent of any particular patient or context"
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes("Health Level Seven International (Clinical Decision Support)"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testQuestionnaire6(self):
        inst = self.instantiate_from("cdshooksguidanceresponse-questionnaire.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire6(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire6(inst2)

    def implQuestionnaire6(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("qs1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-minOccurs"
            ),
        )
        self.assertEqual(inst.item[0].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].extension[1].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].text),
            force_bytes(
                "A guidance response is the formal response to a guidance request, including any output parameters returned by the evaluation, as well as the description of any proposed actions to be taken."
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[1].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].valueString),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].linkId),
            force_bytes("GuidanceResponse.id.value"),
        )
        self.assertFalse(inst.item[0].item[1].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].text),
            force_bytes("Logical id of this artifact"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].linkId), force_bytes("GuidanceResponse.id")
        )
        self.assertTrue(inst.item[0].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].required)
        self.assertEqual(force_bytes(inst.item[0].item[1].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[2].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].text),
            force_bytes(
                "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].linkId),
            force_bytes("GuidanceResponse.meta"),
        )
        self.assertTrue(inst.item[0].item[2].repeats)
        self.assertFalse(inst.item[0].item[2].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].text),
            force_bytes("Metadata about the resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[2].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[3].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].linkId),
            force_bytes("GuidanceResponse.implicitRules.value"),
        )
        self.assertFalse(inst.item[0].item[3].item[1].repeats)
        self.assertFalse(inst.item[0].item[3].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].text),
            force_bytes("A set of rules under which this content was created"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].linkId),
            force_bytes("GuidanceResponse.implicitRules"),
        )
        self.assertTrue(inst.item[0].item[3].repeats)
        self.assertFalse(inst.item[0].item[3].required)
        self.assertEqual(force_bytes(inst.item[0].item[3].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[4].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].valueString),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].linkId),
            force_bytes("GuidanceResponse.language.value"),
        )
        self.assertFalse(inst.item[0].item[4].item[1].repeats)
        self.assertFalse(inst.item[0].item[4].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].text), force_bytes("language")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].type), force_bytes("choice")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].linkId),
            force_bytes("GuidanceResponse.language"),
        )
        self.assertTrue(inst.item[0].item[4].repeats)
        self.assertFalse(inst.item[0].item[4].required)
        self.assertEqual(force_bytes(inst.item[0].item[4].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[5].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].linkId),
            force_bytes("GuidanceResponse.text"),
        )
        self.assertTrue(inst.item[0].item[5].repeats)
        self.assertFalse(inst.item[0].item[5].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].text),
            force_bytes("Text summary of the resource, for human interpretation"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[5].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].linkId),
            force_bytes("GuidanceResponse.contained"),
        )
        self.assertTrue(inst.item[0].item[6].repeats)
        self.assertFalse(inst.item[0].item[6].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].text),
            force_bytes("Contained, inline Resources"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[6].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].text), force_bytes("An Extension")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].linkId),
            force_bytes("GuidanceResponse.extension"),
        )
        self.assertTrue(inst.item[0].item[7].repeats)
        self.assertFalse(inst.item[0].item[7].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[7].text), force_bytes("Extension")
        )
        self.assertEqual(force_bytes(inst.item[0].item[7].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].linkId),
            force_bytes("GuidanceResponse.modifierExtension"),
        )
        self.assertTrue(inst.item[0].item[8].repeats)
        self.assertFalse(inst.item[0].item[8].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[8].text),
            force_bytes("Extensions that cannot be ignored"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[8].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-minOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[9].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[9].extension[1].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[2].valueString),
            force_bytes("Identifier"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].linkId),
            force_bytes("GuidanceResponse.requestIdentifier.label"),
        )
        self.assertFalse(inst.item[0].item[9].item[1].repeats)
        self.assertFalse(inst.item[0].item[9].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].text), force_bytes("label:")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[2].linkId),
            force_bytes("GuidanceResponse.requestIdentifier.system"),
        )
        self.assertFalse(inst.item[0].item[9].item[2].repeats)
        self.assertFalse(inst.item[0].item[9].item[2].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[2].text), force_bytes("system:")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[2].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[3].linkId),
            force_bytes("GuidanceResponse.requestIdentifier.value"),
        )
        self.assertFalse(inst.item[0].item[9].item[3].repeats)
        self.assertFalse(inst.item[0].item[9].item[3].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[3].text), force_bytes("value:")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[3].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].linkId),
            force_bytes("GuidanceResponse.requestIdentifier"),
        )
        self.assertTrue(inst.item[0].item[9].repeats)
        self.assertTrue(inst.item[0].item[9].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].text),
            force_bytes(
                "The identifier of the request associated with this response, if any"
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].item[9].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].linkId), force_bytes("GuidanceResponse")
        )
        self.assertFalse(inst.item[0].repeats)
        self.assertTrue(inst.item[0].required)
        self.assertEqual(
            force_bytes(inst.item[0].text),
            force_bytes("The formal response to a guidance request"),
        )
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testQuestionnaire7(self):
        inst = self.instantiate_from("searchparameter-questionnaire.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire7(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire7(inst2)

    def implQuestionnaire7(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("qs1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].text),
            force_bytes(
                "In FHIR, search is not performed directly on a resource (by XML or JSON path), but on a named parameter that maps into the resource content."
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[1].extension[0].valueCodeableConcept.coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].text),
            force_bytes(
                "A search parameter that defines a named search item that can be used to search/filter on a resource."
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].item[1].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[2].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[1].valueString),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].linkId),
            force_bytes("SearchParameter.id.value"),
        )
        self.assertFalse(inst.item[0].item[2].item[1].repeats)
        self.assertFalse(inst.item[0].item[2].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].text),
            force_bytes("Logical id of this artifact"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].linkId), force_bytes("SearchParameter.id")
        )
        self.assertTrue(inst.item[0].item[2].repeats)
        self.assertFalse(inst.item[0].item[2].required)
        self.assertEqual(force_bytes(inst.item[0].item[2].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[3].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].text),
            force_bytes(
                "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].linkId),
            force_bytes("SearchParameter.meta"),
        )
        self.assertTrue(inst.item[0].item[3].repeats)
        self.assertFalse(inst.item[0].item[3].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].text),
            force_bytes("Metadata about the resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[3].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[4].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].linkId),
            force_bytes("SearchParameter.implicitRules.value"),
        )
        self.assertFalse(inst.item[0].item[4].item[1].repeats)
        self.assertFalse(inst.item[0].item[4].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].text),
            force_bytes("A set of rules under which this content was created"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].linkId),
            force_bytes("SearchParameter.implicitRules"),
        )
        self.assertTrue(inst.item[0].item[4].repeats)
        self.assertFalse(inst.item[0].item[4].required)
        self.assertEqual(force_bytes(inst.item[0].item[4].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[5].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[1].valueString),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].linkId),
            force_bytes("SearchParameter.language.value"),
        )
        self.assertFalse(inst.item[0].item[5].item[1].repeats)
        self.assertFalse(inst.item[0].item[5].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].text), force_bytes("language")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[1].type), force_bytes("choice")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].linkId),
            force_bytes("SearchParameter.language"),
        )
        self.assertTrue(inst.item[0].item[5].repeats)
        self.assertFalse(inst.item[0].item[5].required)
        self.assertEqual(force_bytes(inst.item[0].item[5].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[6].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[6].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].linkId),
            force_bytes("SearchParameter.text"),
        )
        self.assertTrue(inst.item[0].item[6].repeats)
        self.assertFalse(inst.item[0].item[6].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].text),
            force_bytes("Text summary of the resource, for human interpretation"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[6].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].linkId),
            force_bytes("SearchParameter.contained"),
        )
        self.assertTrue(inst.item[0].item[7].repeats)
        self.assertFalse(inst.item[0].item[7].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[7].text),
            force_bytes("Contained, inline Resources"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[7].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].linkId),
            force_bytes("SearchParameter.extension"),
        )
        self.assertTrue(inst.item[0].item[8].repeats)
        self.assertFalse(inst.item[0].item[8].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[8].text),
            force_bytes("Additional content defined by implementations"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[8].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].linkId),
            force_bytes("SearchParameter.modifierExtension"),
        )
        self.assertTrue(inst.item[0].item[9].repeats)
        self.assertFalse(inst.item[0].item[9].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].text),
            force_bytes("Extensions that cannot be ignored"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[9].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].linkId), force_bytes("SearchParameter")
        )
        self.assertTrue(inst.item[0].repeats)
        self.assertFalse(inst.item[0].required)
        self.assertEqual(
            force_bytes(inst.item[0].text),
            force_bytes("Search parameter for a resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes("Health Level Seven International (FHIR Infrastructure)"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testQuestionnaire8(self):
        inst = self.instantiate_from("explanationofbenefit-questionnaire.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire8(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire8(inst2)

    def implQuestionnaire8(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("vs2"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("vs3"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("vs4"))
        self.assertEqual(force_bytes(inst.contained[3].id), force_bytes("vs5"))
        self.assertEqual(force_bytes(inst.contained[4].id), force_bytes("vs6"))
        self.assertEqual(force_bytes(inst.contained[5].id), force_bytes("vs7"))
        self.assertEqual(force_bytes(inst.contained[6].id), force_bytes("vs8"))
        self.assertEqual(force_bytes(inst.contained[7].id), force_bytes("vs9"))
        self.assertEqual(force_bytes(inst.contained[8].id), force_bytes("vs10"))
        self.assertEqual(force_bytes(inst.contained[9].id), force_bytes("vs11"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("qs1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].text),
            force_bytes(
                "This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally account balance information, for informing the subscriber of the benefits provided."
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[1].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].valueString),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].linkId),
            force_bytes("ExplanationOfBenefit.id.value"),
        )
        self.assertFalse(inst.item[0].item[1].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].text),
            force_bytes("Logical id of this artifact"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].linkId),
            force_bytes("ExplanationOfBenefit.id"),
        )
        self.assertTrue(inst.item[0].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].required)
        self.assertEqual(force_bytes(inst.item[0].item[1].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[2].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].text),
            force_bytes(
                "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].linkId),
            force_bytes("ExplanationOfBenefit.meta"),
        )
        self.assertTrue(inst.item[0].item[2].repeats)
        self.assertFalse(inst.item[0].item[2].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].text),
            force_bytes("Metadata about the resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[2].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[3].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].linkId),
            force_bytes("ExplanationOfBenefit.implicitRules.value"),
        )
        self.assertFalse(inst.item[0].item[3].item[1].repeats)
        self.assertFalse(inst.item[0].item[3].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].text),
            force_bytes("A set of rules under which this content was created"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].linkId),
            force_bytes("ExplanationOfBenefit.implicitRules"),
        )
        self.assertTrue(inst.item[0].item[3].repeats)
        self.assertFalse(inst.item[0].item[3].required)
        self.assertEqual(force_bytes(inst.item[0].item[3].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[4].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].valueString),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].linkId),
            force_bytes("ExplanationOfBenefit.language.value"),
        )
        self.assertFalse(inst.item[0].item[4].item[1].repeats)
        self.assertFalse(inst.item[0].item[4].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].text), force_bytes("language")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].type), force_bytes("choice")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].linkId),
            force_bytes("ExplanationOfBenefit.language"),
        )
        self.assertTrue(inst.item[0].item[4].repeats)
        self.assertFalse(inst.item[0].item[4].required)
        self.assertEqual(force_bytes(inst.item[0].item[4].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[5].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].linkId),
            force_bytes("ExplanationOfBenefit.text"),
        )
        self.assertTrue(inst.item[0].item[5].repeats)
        self.assertFalse(inst.item[0].item[5].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].text),
            force_bytes("Text summary of the resource, for human interpretation"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[5].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].linkId),
            force_bytes("ExplanationOfBenefit.contained"),
        )
        self.assertTrue(inst.item[0].item[6].repeats)
        self.assertFalse(inst.item[0].item[6].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].text),
            force_bytes("Contained, inline Resources"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[6].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].linkId),
            force_bytes("ExplanationOfBenefit.extension"),
        )
        self.assertTrue(inst.item[0].item[7].repeats)
        self.assertFalse(inst.item[0].item[7].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[7].text),
            force_bytes("Additional content defined by implementations"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[7].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].linkId),
            force_bytes("ExplanationOfBenefit.modifierExtension"),
        )
        self.assertTrue(inst.item[0].item[8].repeats)
        self.assertFalse(inst.item[0].item[8].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[8].text),
            force_bytes("Extensions that cannot be ignored"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[8].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[0].valueString),
            force_bytes("Identifier"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].text),
            force_bytes("A unique identifier assigned to this explanation of benefit."),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].linkId),
            force_bytes("ExplanationOfBenefit.identifier.label"),
        )
        self.assertFalse(inst.item[0].item[9].item[1].repeats)
        self.assertFalse(inst.item[0].item[9].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].text), force_bytes("label:")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[2].linkId),
            force_bytes("ExplanationOfBenefit.identifier.system"),
        )
        self.assertFalse(inst.item[0].item[9].item[2].repeats)
        self.assertFalse(inst.item[0].item[9].item[2].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[2].text), force_bytes("system:")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[2].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[3].linkId),
            force_bytes("ExplanationOfBenefit.identifier.value"),
        )
        self.assertFalse(inst.item[0].item[9].item[3].repeats)
        self.assertFalse(inst.item[0].item[9].item[3].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[3].text), force_bytes("value:")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[3].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].linkId),
            force_bytes("ExplanationOfBenefit.identifier"),
        )
        self.assertTrue(inst.item[0].item[9].repeats)
        self.assertFalse(inst.item[0].item[9].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].text),
            force_bytes("Business Identifier for the resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[9].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].linkId), force_bytes("ExplanationOfBenefit")
        )
        self.assertTrue(inst.item[0].repeats)
        self.assertFalse(inst.item[0].required)
        self.assertEqual(
            force_bytes(inst.item[0].text),
            force_bytes("Explanation of Benefit resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes("Health Level Seven International (Financial Management)"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testQuestionnaire9(self):
        inst = self.instantiate_from("immunizationevaluation-questionnaire.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire9(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire9(inst2)

    def implQuestionnaire9(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("vs2"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("vs3"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("qs1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].text),
            force_bytes(
                'Describes a comparison of an immunization event against published recommendations to determine if the administration is "valid" in relation to those  recommendations.'
            ),
        )
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[1].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].valueString),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].linkId),
            force_bytes("ImmunizationEvaluation.id.value"),
        )
        self.assertFalse(inst.item[0].item[1].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].text),
            force_bytes("Logical id of this artifact"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].linkId),
            force_bytes("ImmunizationEvaluation.id"),
        )
        self.assertTrue(inst.item[0].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].required)
        self.assertEqual(force_bytes(inst.item[0].item[1].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[2].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].text),
            force_bytes(
                "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].linkId),
            force_bytes("ImmunizationEvaluation.meta"),
        )
        self.assertTrue(inst.item[0].item[2].repeats)
        self.assertFalse(inst.item[0].item[2].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].text),
            force_bytes("Metadata about the resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[2].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[3].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].linkId),
            force_bytes("ImmunizationEvaluation.implicitRules.value"),
        )
        self.assertFalse(inst.item[0].item[3].item[1].repeats)
        self.assertFalse(inst.item[0].item[3].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].text),
            force_bytes("A set of rules under which this content was created"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].linkId),
            force_bytes("ImmunizationEvaluation.implicitRules"),
        )
        self.assertTrue(inst.item[0].item[3].repeats)
        self.assertFalse(inst.item[0].item[3].required)
        self.assertEqual(force_bytes(inst.item[0].item[3].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[4].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].valueString),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].linkId),
            force_bytes("ImmunizationEvaluation.language.value"),
        )
        self.assertFalse(inst.item[0].item[4].item[1].repeats)
        self.assertFalse(inst.item[0].item[4].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].text), force_bytes("language")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].type), force_bytes("choice")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].linkId),
            force_bytes("ImmunizationEvaluation.language"),
        )
        self.assertTrue(inst.item[0].item[4].repeats)
        self.assertFalse(inst.item[0].item[4].required)
        self.assertEqual(force_bytes(inst.item[0].item[4].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[5].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].linkId),
            force_bytes("ImmunizationEvaluation.text"),
        )
        self.assertTrue(inst.item[0].item[5].repeats)
        self.assertFalse(inst.item[0].item[5].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].text),
            force_bytes("Text summary of the resource, for human interpretation"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[5].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].linkId),
            force_bytes("ImmunizationEvaluation.contained"),
        )
        self.assertTrue(inst.item[0].item[6].repeats)
        self.assertFalse(inst.item[0].item[6].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].text),
            force_bytes("Contained, inline Resources"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[6].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].linkId),
            force_bytes("ImmunizationEvaluation.extension"),
        )
        self.assertTrue(inst.item[0].item[7].repeats)
        self.assertFalse(inst.item[0].item[7].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[7].text),
            force_bytes("Additional content defined by implementations"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[7].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].linkId),
            force_bytes("ImmunizationEvaluation.modifierExtension"),
        )
        self.assertTrue(inst.item[0].item[8].repeats)
        self.assertFalse(inst.item[0].item[8].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[8].text),
            force_bytes("Extensions that cannot be ignored"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[8].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[0].valueString),
            force_bytes("Identifier"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].text),
            force_bytes(
                "A unique identifier assigned to this immunization evaluation record."
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].linkId),
            force_bytes("ImmunizationEvaluation.identifier.label"),
        )
        self.assertFalse(inst.item[0].item[9].item[1].repeats)
        self.assertFalse(inst.item[0].item[9].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].text), force_bytes("label:")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[2].linkId),
            force_bytes("ImmunizationEvaluation.identifier.system"),
        )
        self.assertFalse(inst.item[0].item[9].item[2].repeats)
        self.assertFalse(inst.item[0].item[9].item[2].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[2].text), force_bytes("system:")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[2].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[3].linkId),
            force_bytes("ImmunizationEvaluation.identifier.value"),
        )
        self.assertFalse(inst.item[0].item[9].item[3].repeats)
        self.assertFalse(inst.item[0].item[9].item[3].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[3].text), force_bytes("value:")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[3].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].linkId),
            force_bytes("ImmunizationEvaluation.identifier"),
        )
        self.assertTrue(inst.item[0].item[9].repeats)
        self.assertFalse(inst.item[0].item[9].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].text), force_bytes("Business identifier")
        )
        self.assertEqual(force_bytes(inst.item[0].item[9].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].linkId), force_bytes("ImmunizationEvaluation")
        )
        self.assertTrue(inst.item[0].repeats)
        self.assertFalse(inst.item[0].required)
        self.assertEqual(
            force_bytes(inst.item[0].text),
            force_bytes("Immunization evaluation information"),
        )
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes(
                "Health Level Seven International (Public Health and Emergency Response)"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testQuestionnaire10(self):
        inst = self.instantiate_from("medicinalproductindication-questionnaire.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire10(inst)

        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire10(inst2)

    def implQuestionnaire10(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("vs2"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("qs1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0].item[0].extension[0].valueCodeableConcept.coding[0].system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[0].text),
            force_bytes("Indication for the Medicinal Product."),
        )
        self.assertEqual(force_bytes(inst.item[0].item[0].type), force_bytes("display"))
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[1].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].extension[1].valueString),
            force_bytes("string"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[1]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].linkId),
            force_bytes("MedicinalProductIndication.id.value"),
        )
        self.assertFalse(inst.item[0].item[1].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].text),
            force_bytes("Logical id of this artifact"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[1].linkId),
            force_bytes("MedicinalProductIndication.id"),
        )
        self.assertTrue(inst.item[0].item[1].repeats)
        self.assertFalse(inst.item[0].item[1].required)
        self.assertEqual(force_bytes(inst.item[0].item[1].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[2].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[2].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[2]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].text),
            force_bytes(
                "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[2].linkId),
            force_bytes("MedicinalProductIndication.meta"),
        )
        self.assertTrue(inst.item[0].item[2].repeats)
        self.assertFalse(inst.item[0].item[2].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[2].text),
            force_bytes("Metadata about the resource"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[2].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[3].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].extension[1].valueString),
            force_bytes("uri"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[3]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].linkId),
            force_bytes("MedicinalProductIndication.implicitRules.value"),
        )
        self.assertFalse(inst.item[0].item[3].item[1].repeats)
        self.assertFalse(inst.item[0].item[3].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].text),
            force_bytes("A set of rules under which this content was created"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].item[1].type), force_bytes("string")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[3].linkId),
            force_bytes("MedicinalProductIndication.implicitRules"),
        )
        self.assertTrue(inst.item[0].item[3].repeats)
        self.assertFalse(inst.item[0].item[3].required)
        self.assertEqual(force_bytes(inst.item[0].item[3].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[4].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].extension[1].valueString),
            force_bytes("code"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[4]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].linkId),
            force_bytes("MedicinalProductIndication.language.value"),
        )
        self.assertFalse(inst.item[0].item[4].item[1].repeats)
        self.assertFalse(inst.item[0].item[4].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].text), force_bytes("language")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].item[1].type), force_bytes("choice")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[4].linkId),
            force_bytes("MedicinalProductIndication.language"),
        )
        self.assertTrue(inst.item[0].item[4].repeats)
        self.assertFalse(inst.item[0].item[4].required)
        self.assertEqual(force_bytes(inst.item[0].item[4].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[5].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-maxOccurs"
            ),
        )
        self.assertEqual(inst.item[0].item[5].extension[0].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[5]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[5].linkId),
            force_bytes("MedicinalProductIndication.text"),
        )
        self.assertTrue(inst.item[0].item[5].repeats)
        self.assertFalse(inst.item[0].item[5].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[5].text),
            force_bytes("Text summary of the resource, for human interpretation"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[5].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[6]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[6].linkId),
            force_bytes("MedicinalProductIndication.contained"),
        )
        self.assertTrue(inst.item[0].item[6].repeats)
        self.assertFalse(inst.item[0].item[6].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[6].text),
            force_bytes("Contained, inline Resources"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[6].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[7]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[7].linkId),
            force_bytes("MedicinalProductIndication.extension"),
        )
        self.assertTrue(inst.item[0].item[7].repeats)
        self.assertFalse(inst.item[0].item[7].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[7].text),
            force_bytes("Additional content defined by implementations"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[7].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[8]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[8].linkId),
            force_bytes("MedicinalProductIndication.modifierExtension"),
        )
        self.assertTrue(inst.item[0].item[8].repeats)
        self.assertFalse(inst.item[0].item[8].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[8].text),
            force_bytes("Extensions that cannot be ignored"),
        )
        self.assertEqual(force_bytes(inst.item[0].item[8].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-fhirType"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].extension[0].valueString),
            force_bytes("Reference"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-itemControl"
            ),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .code
            ),
            force_bytes("flyover"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .display
            ),
            force_bytes("Fly-over"),
        )
        self.assertEqual(
            force_bytes(
                inst.item[0]
                .item[9]
                .item[0]
                .extension[0]
                .valueCodeableConcept.coding[0]
                .system
            ),
            force_bytes("http://hl7.org/fhir/questionnaire-item-control"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].text),
            force_bytes("The medication for which this is an indication."),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[0].type), force_bytes("display")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-allowedResource"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].extension[0].valueCode),
            force_bytes("MedicinalProduct, Medication"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/questionnaire-referenceFilter"
            ),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].extension[1].valueString),
            force_bytes("subject=$subj&patient=$subj&encounter=$encounter"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].linkId),
            force_bytes("MedicinalProductIndication.subject.value"),
        )
        self.assertFalse(inst.item[0].item[9].item[1].repeats)
        self.assertFalse(inst.item[0].item[9].item[1].required)
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].text),
            force_bytes("The medication for which this is an indication"),
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].item[1].type), force_bytes("reference")
        )
        self.assertEqual(
            force_bytes(inst.item[0].item[9].linkId),
            force_bytes("MedicinalProductIndication.subject"),
        )
        self.assertTrue(inst.item[0].item[9].repeats)
        self.assertFalse(inst.item[0].item[9].required)
        self.assertEqual(force_bytes(inst.item[0].item[9].type), force_bytes("group"))
        self.assertEqual(
            force_bytes(inst.item[0].linkId), force_bytes("MedicinalProductIndication")
        )
        self.assertTrue(inst.item[0].repeats)
        self.assertFalse(inst.item[0].required)
        self.assertEqual(
            force_bytes(inst.item[0].text), force_bytes("MedicinalProductIndication")
        )
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("group"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes(
                "Health Level Seven International (Biomedical Research and Regulation)"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))
