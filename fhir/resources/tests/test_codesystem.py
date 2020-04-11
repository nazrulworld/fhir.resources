# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import codesystem
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class CodeSystemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("CodeSystem", js["resourceType"])
        return codesystem.CodeSystem(js)

    def testCodeSystem1(self):
        inst = self.instantiate_from("codesystem-map-model-mode.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem1(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem1(inst2)

    def implCodeSystem1(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("source"))
        self.assertEqual(
            force_bytes(inst.concept[0].definition),
            force_bytes(
                "This structure describes an instance passed to the mapping engine that is used a source of data."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[0].display),
            force_bytes("Source Structure Definition"),
        )
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("queried"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes(
                "This structure describes an instance that the mapping engine may ask for that is used a source of data."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[1].display),
            force_bytes("Queried Structure Definition"),
        )
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("target"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes(
                "This structure describes an instance passed to the mapping engine that is used a target of data."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[2].display),
            force_bytes("Target Structure Definition"),
        )
        self.assertEqual(force_bytes(inst.concept[3].code), force_bytes("produced"))
        self.assertEqual(
            force_bytes(inst.concept[3].definition),
            force_bytes(
                "This structure describes an instance that the mapping engine may ask to create that is used a target of data."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[3].display),
            force_bytes("Produced Structure Definition"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("How the referenced structure is used in this mapping."),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("fhir"))
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[1].valueCode), force_bytes("trial-use")
        )
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[2].valueInteger, 2)
        self.assertEqual(force_bytes(inst.id), force_bytes("map-model-mode"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.4.676"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("StructureMapModelMode"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("StructureMapModelMode"))
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/map-model-mode")
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/map-model-mode"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testCodeSystem2(self):
        inst = self.instantiate_from("codesystem-special-values.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem2(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem2(inst2)

    def implCodeSystem2(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("true"))
        self.assertEqual(
            force_bytes(inst.concept[0].definition), force_bytes("Boolean true.")
        )
        self.assertEqual(force_bytes(inst.concept[0].display), force_bytes("true"))
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("false"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition), force_bytes("Boolean false.")
        )
        self.assertEqual(force_bytes(inst.concept[1].display), force_bytes("false"))
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("trace"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes(
                "The content is greater than zero, but too small to be quantified."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[2].display), force_bytes("Trace Amount Detected")
        )
        self.assertEqual(force_bytes(inst.concept[3].code), force_bytes("sufficient"))
        self.assertEqual(
            force_bytes(inst.concept[3].definition),
            force_bytes(
                "The specific quantity is not known, but is known to be non-zero and is not specified because it makes up the bulk of the material."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[3].display), force_bytes("Sufficient Quantity")
        )
        self.assertEqual(
            force_bytes(inst.concept[3].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments"
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[3].extension[0].valueString),
            force_bytes(
                "used in formulations (e.g. 'Add 10mg of ingredient X, 50mg of ingredient Y, and sufficient quantity of water to 100mL.' This code would be used to express the quantity of water. )"
            ),
        )
        self.assertEqual(force_bytes(inst.concept[4].code), force_bytes("withdrawn"))
        self.assertEqual(
            force_bytes(inst.concept[4].definition),
            force_bytes("The value is no longer available."),
        )
        self.assertEqual(
            force_bytes(inst.concept[4].display), force_bytes("Value Withdrawn")
        )
        self.assertEqual(force_bytes(inst.concept[5].code), force_bytes("nil-known"))
        self.assertEqual(
            force_bytes(inst.concept[5].definition),
            force_bytes("The are no known applicable values in this context."),
        )
        self.assertEqual(force_bytes(inst.concept[5].display), force_bytes("Nil Known"))
        self.assertEqual(
            force_bytes(inst.concept[5].extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments"
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[5].extension[0].valueString),
            force_bytes("The existence of this subject to review"),
        )
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "A set of generally useful codes defined so they can be included in value sets."
            ),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("fhir"))
        self.assertEqual(force_bytes(inst.id), force_bytes("special-values"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.4.1049"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("SpecialValues"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("extensions"))
        self.assertEqual(force_bytes(inst.title), force_bytes("SpecialValues"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://terminology.hl7.org/CodeSystem/special-values"),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/special-values"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testCodeSystem3(self):
        inst = self.instantiate_from("codesystem-communication-not-done-reason.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem3(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem3(inst2)

    def implCodeSystem3(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("unknown"))
        self.assertEqual(
            force_bytes(inst.concept[0].definition),
            force_bytes("The communication was not done due to an unknown reason."),
        )
        self.assertEqual(force_bytes(inst.concept[0].display), force_bytes("Unknown"))
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("system-error"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes("The communication was not done due to a system error."),
        )
        self.assertEqual(
            force_bytes(inst.concept[1].display), force_bytes("System Error")
        )
        self.assertEqual(
            force_bytes(inst.concept[2].code), force_bytes("invalid-phone-number")
        )
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes(
                "The communication was not done due to an invalid phone number."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[2].display), force_bytes("Invalid Phone Number")
        )
        self.assertEqual(
            force_bytes(inst.concept[3].code), force_bytes("recipient-unavailable")
        )
        self.assertEqual(
            force_bytes(inst.concept[3].definition),
            force_bytes(
                "The communication was not done due to the recipient being unavailable."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[3].display), force_bytes("Recipient Unavailable")
        )
        self.assertEqual(
            force_bytes(inst.concept[4].code), force_bytes("family-objection")
        )
        self.assertEqual(
            force_bytes(inst.concept[4].definition),
            force_bytes("The communication was not done due to a family objection."),
        )
        self.assertEqual(
            force_bytes(inst.concept[4].display), force_bytes("Family Objection")
        )
        self.assertEqual(
            force_bytes(inst.concept[5].code), force_bytes("patient-objection")
        )
        self.assertEqual(
            force_bytes(inst.concept[5].definition),
            force_bytes("The communication was not done due to a patient objection."),
        )
        self.assertEqual(
            force_bytes(inst.concept[5].display), force_bytes("Patient Objection")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Codes for the reason why a communication did not happen."),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("pc"))
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[1].valueCode), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[2].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("communication-not-done-reason")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.4.1077"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("CommunicationNotDoneReason")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("CommunicationNotDoneReason")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/communication-not-done-reason"
            ),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/communication-not-done-reason"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testCodeSystem4(self):
        inst = self.instantiate_from("codesystem-codesystem-hierarchy-meaning.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem4(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem4(inst2)

    def implCodeSystem4(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("grouped-by"))
        self.assertEqual(
            force_bytes(inst.concept[0].display), force_bytes("Grouped By")
        )
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("is-a"))
        self.assertEqual(force_bytes(inst.concept[1].display), force_bytes("Is-A"))
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("part-of"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes(
                "Child elements list the individual parts of a composite whole (e.g. body site)."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[2].display), force_bytes("Part Of"))
        self.assertEqual(
            force_bytes(inst.concept[3].code), force_bytes("classified-with")
        )
        self.assertEqual(
            force_bytes(inst.concept[3].display), force_bytes("Classified With")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("The meaning of the hierarchy of concepts in a code system."),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("vocab"))
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[1].valueCode), force_bytes("normative")
        )
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-normative-version"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("4.0.0"))
        self.assertEqual(
            force_bytes(inst.extension[3].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[3].valueInteger, 5)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("codesystem-hierarchy-meaning")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.4.785"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("CodeSystemHierarchyMeaning")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("CodeSystemHierarchyMeaning")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/codesystem-hierarchy-meaning"),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testCodeSystem5(self):
        inst = self.instantiate_from(
            "codesystem-medicationrequest-course-of-therapy.json"
        )
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem5(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem5(inst2)

    def implCodeSystem5(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("continuous"))
        self.assertEqual(
            force_bytes(inst.concept[0].definition),
            force_bytes(
                "A medication which is expected to be continued beyond the present order and which the patient should be assumed to be taking unless explicitly stopped."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[0].display),
            force_bytes("Continuous long term therapy"),
        )
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("acute"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes(
                "A medication which the patient is only expected to consume for the duration of the current order and which is not expected to be renewed."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[1].display),
            force_bytes("Short course (acute) therapy"),
        )
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("seasonal"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes(
                "A medication which is expected to be used on a part time basis at certain times of the year"
            ),
        )
        self.assertEqual(force_bytes(inst.concept[2].display), force_bytes("Seasonal"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("MedicationRequest Course of Therapy Codes"),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("phx"))
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[1].valueCode), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[2].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("medicationrequest-course-of-therapy")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.4.1327"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablecodesystem"),
        )
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("medicationRequest Course of Therapy Codes"),
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project team"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title),
            force_bytes("Medication request  course of  therapy  codes"),
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://terminology.hl7.org/CodeSystem/medicationrequest-course-of-therapy"
            ),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes(
                "http://hl7.org/fhir/ValueSet/medicationrequest-course-of-therapy"
            ),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testCodeSystem6(self):
        inst = self.instantiate_from("codesystem-audit-event-outcome.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem6(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem6(inst2)

    def implCodeSystem6(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("0"))
        self.assertEqual(
            force_bytes(inst.concept[0].definition),
            force_bytes(
                "The operation completed successfully (whether with warnings or not)."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[0].display), force_bytes("Success"))
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("4"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes(
                "The action was not successful due to some kind of minor failure (often equivalent to an HTTP 400 response)."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[1].display), force_bytes("Minor failure")
        )
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("8"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes(
                "The action was not successful due to some kind of unexpected error (often equivalent to an HTTP 500 response)."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[2].display), force_bytes("Serious failure")
        )
        self.assertEqual(force_bytes(inst.concept[3].code), force_bytes("12"))
        self.assertEqual(
            force_bytes(inst.concept[3].definition),
            force_bytes(
                "An error of such magnitude occurred that the system is no longer available for use (i.e. the system died)."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[3].display), force_bytes("Major failure")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Indicates whether the event succeeded or failed."),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("sec"))
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[1].valueCode), force_bytes("trial-use")
        )
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[2].valueInteger, 3)
        self.assertEqual(force_bytes(inst.id), force_bytes("audit-event-outcome"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.4.455"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("AuditEventOutcome"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("AuditEventOutcome"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/audit-event-outcome"),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/audit-event-outcome"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testCodeSystem7(self):
        inst = self.instantiate_from("codesystem-contract-subtype.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem7(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem7(inst2)

    def implCodeSystem7(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(
            force_bytes(inst.concept[0].code), force_bytes("disclosure-ca")
        )
        self.assertEqual(
            force_bytes(inst.concept[0].definition),
            force_bytes("Canadian health information disclosure policy."),
        )
        self.assertEqual(
            force_bytes(inst.concept[0].display), force_bytes("Disclosure-CA")
        )
        self.assertEqual(
            force_bytes(inst.concept[1].code), force_bytes("disclosure-us")
        )
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes("United States health information disclosure policy."),
        )
        self.assertEqual(
            force_bytes(inst.concept[1].display), force_bytes("Disclosure-US")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(
            force_bytes(inst.copyright), force_bytes("This is an example set.")
        )
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("This value set includes sample Contract Subtype codes."),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("fm"))
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[1].valueCode), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[2].valueInteger, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("contract-subtype"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.4.1198"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablecodesystem"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("ContractSubtypeCodes"))
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Financial Management")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Contract Subtype Codes"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://terminology.hl7.org/CodeSystem/contractsubtypecodes"),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/contract-subtype"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testCodeSystem8(self):
        inst = self.instantiate_from("codesystem-map-transform.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem8(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem8(inst2)

    def implCodeSystem8(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("create"))
        self.assertEqual(
            force_bytes(inst.concept[0].definition),
            force_bytes(
                "create(type : string) - type is passed through to the application on the standard API, and must be known by it."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[0].display), force_bytes("create"))
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("copy"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition), force_bytes("copy(source).")
        )
        self.assertEqual(force_bytes(inst.concept[1].display), force_bytes("copy"))
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("truncate"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes("truncate(source, length) - source must be stringy type."),
        )
        self.assertEqual(force_bytes(inst.concept[2].display), force_bytes("truncate"))
        self.assertEqual(force_bytes(inst.concept[3].code), force_bytes("escape"))
        self.assertEqual(
            force_bytes(inst.concept[3].definition),
            force_bytes(
                "escape(source, fmt1, fmt2) - change source from one kind of escaping to another (plain, java, xml, json). note that this is for when the string itself is escaped."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[3].display), force_bytes("escape"))
        self.assertEqual(force_bytes(inst.concept[4].code), force_bytes("cast"))
        self.assertEqual(
            force_bytes(inst.concept[4].definition),
            force_bytes(
                "cast(source, type?) - case source from one type to another. target type can be left as implicit if there is one and only one target type known."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[4].display), force_bytes("cast"))
        self.assertEqual(force_bytes(inst.concept[5].code), force_bytes("append"))
        self.assertEqual(
            force_bytes(inst.concept[5].definition),
            force_bytes("append(source...) - source is element or string."),
        )
        self.assertEqual(force_bytes(inst.concept[5].display), force_bytes("append"))
        self.assertEqual(force_bytes(inst.concept[6].code), force_bytes("translate"))
        self.assertEqual(
            force_bytes(inst.concept[6].definition),
            force_bytes("translate(source, uri_of_map) - use the translate operation."),
        )
        self.assertEqual(force_bytes(inst.concept[6].display), force_bytes("translate"))
        self.assertEqual(force_bytes(inst.concept[7].code), force_bytes("reference"))
        self.assertEqual(
            force_bytes(inst.concept[7].definition),
            force_bytes(
                "reference(source : object) - return a string that references the provided tree properly."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[7].display), force_bytes("reference"))
        self.assertEqual(force_bytes(inst.concept[8].code), force_bytes("dateOp"))
        self.assertEqual(
            force_bytes(inst.concept[8].definition),
            force_bytes("Perform a date operation. *Parameters to be documented*."),
        )
        self.assertEqual(force_bytes(inst.concept[8].display), force_bytes("dateOp"))
        self.assertEqual(force_bytes(inst.concept[9].code), force_bytes("uuid"))
        self.assertEqual(
            force_bytes(inst.concept[9].definition),
            force_bytes("Generate a random UUID (in lowercase). No Parameters."),
        )
        self.assertEqual(force_bytes(inst.concept[9].display), force_bytes("uuid"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description), force_bytes("How data is copied/created.")
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("fhir"))
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[1].valueCode), force_bytes("trial-use")
        )
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[2].valueInteger, 2)
        self.assertEqual(force_bytes(inst.id), force_bytes("map-transform"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.4.682"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("StructureMapTransform"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("StructureMapTransform"))
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/map-transform")
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/map-transform"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testCodeSystem9(self):
        inst = self.instantiate_from("codesystem-imagingstudy-status.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem9(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem9(inst2)

    def implCodeSystem9(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("registered"))
        self.assertEqual(
            force_bytes(inst.concept[0].definition),
            force_bytes(
                "The existence of the imaging study is registered, but there is nothing yet available."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[0].display), force_bytes("Registered")
        )
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("available"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes(
                "At least one instance has been associated with this imaging study."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[1].display), force_bytes("Available"))
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("cancelled"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes(
                'The imaging study is unavailable because the imaging study was not started or not completed (also sometimes called "aborted").'
            ),
        )
        self.assertEqual(force_bytes(inst.concept[2].display), force_bytes("Cancelled"))
        self.assertEqual(
            force_bytes(inst.concept[3].code), force_bytes("entered-in-error")
        )
        self.assertEqual(
            force_bytes(inst.concept[3].display), force_bytes("Entered in Error")
        )
        self.assertEqual(force_bytes(inst.concept[4].code), force_bytes("unknown"))
        self.assertEqual(force_bytes(inst.concept[4].display), force_bytes("Unknown"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].system), force_bytes("email")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[1].value),
            force_bytes("fhir@lists.hl7.org"),
        )
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("The status of the ImagingStudy."),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("ii"))
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[1].valueCode), force_bytes("trial-use")
        )
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[2].valueInteger, 3)
        self.assertEqual(force_bytes(inst.id), force_bytes("imagingstudy-status"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.4.991"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("ImagingStudyStatus"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("ImagingStudyStatus"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/imagingstudy-status"),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/imagingstudy-status"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testCodeSystem10(self):
        inst = self.instantiate_from("codesystem-benefit-type.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem10(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem10(inst2)

    def implCodeSystem10(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("benefit"))
        self.assertEqual(
            force_bytes(inst.concept[0].definition),
            force_bytes("Maximum benefit allowable."),
        )
        self.assertEqual(force_bytes(inst.concept[0].display), force_bytes("Benefit"))
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("deductible"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes("Cost to be incurred before benefits are applied"),
        )
        self.assertEqual(
            force_bytes(inst.concept[1].display), force_bytes("Deductible")
        )
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("visit"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition), force_bytes("Service visit")
        )
        self.assertEqual(force_bytes(inst.concept[2].display), force_bytes("Visit"))
        self.assertEqual(force_bytes(inst.concept[3].code), force_bytes("room"))
        self.assertEqual(
            force_bytes(inst.concept[3].definition), force_bytes("Type of room")
        )
        self.assertEqual(force_bytes(inst.concept[3].display), force_bytes("Room"))
        self.assertEqual(force_bytes(inst.concept[4].code), force_bytes("copay"))
        self.assertEqual(
            force_bytes(inst.concept[4].definition),
            force_bytes("Copayment per service"),
        )
        self.assertEqual(
            force_bytes(inst.concept[4].display), force_bytes("Copayment per service")
        )
        self.assertEqual(
            force_bytes(inst.concept[5].code), force_bytes("copay-percent")
        )
        self.assertEqual(
            force_bytes(inst.concept[5].definition),
            force_bytes("Copayment percentage per service"),
        )
        self.assertEqual(
            force_bytes(inst.concept[5].display),
            force_bytes("Copayment Percent per service"),
        )
        self.assertEqual(
            force_bytes(inst.concept[6].code), force_bytes("copay-maximum")
        )
        self.assertEqual(
            force_bytes(inst.concept[6].definition),
            force_bytes("Copayment maximum per service"),
        )
        self.assertEqual(
            force_bytes(inst.concept[6].display),
            force_bytes("Copayment maximum per service"),
        )
        self.assertEqual(force_bytes(inst.concept[7].code), force_bytes("vision-exam"))
        self.assertEqual(
            force_bytes(inst.concept[7].definition), force_bytes("Vision Exam")
        )
        self.assertEqual(
            force_bytes(inst.concept[7].display), force_bytes("Vision Exam")
        )
        self.assertEqual(
            force_bytes(inst.concept[8].code), force_bytes("vision-glasses")
        )
        self.assertEqual(
            force_bytes(inst.concept[8].definition), force_bytes("Frames and lenses")
        )
        self.assertEqual(
            force_bytes(inst.concept[8].display), force_bytes("Vision Glasses")
        )
        self.assertEqual(
            force_bytes(inst.concept[9].code), force_bytes("vision-contacts")
        )
        self.assertEqual(
            force_bytes(inst.concept[9].definition), force_bytes("Contact Lenses")
        )
        self.assertEqual(
            force_bytes(inst.concept[9].display),
            force_bytes("Vision Contacts Coverage"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(
            force_bytes(inst.copyright), force_bytes("This is an example set.")
        )
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("This value set includes a smattering of Benefit type codes."),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("fm"))
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[1].valueCode), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[2].valueInteger, 1)
        self.assertEqual(force_bytes(inst.id), force_bytes("benefit-type"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.4.1176"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablecodesystem"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("BenefitTypeCodes"))
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Financial Management")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Benefit Type Codes"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://terminology.hl7.org/CodeSystem/benefit-type"),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/benefit-type"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))
