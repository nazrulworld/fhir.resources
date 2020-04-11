# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
                "This structure describes an instance passed to the mapping engine that is used a source of data"
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
                "This structure describes an instance that the mapping engine may ask for that is used a source of data"
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
                "This structure describes an instance passed to the mapping engine that is used a target of data"
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
                "This structure describes an instance that the mapping engine may ask to create that is used a target of data"
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("How the referenced structure is used in this mapping"),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Informative")
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[1].valueInteger, 2)
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("fhir"))
        self.assertEqual(force_bytes(inst.id), force_bytes("map-model-mode"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.1.662"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("StructureMapModelMode"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/map-model-mode")
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/map-model-mode"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testCodeSystem2(self):
        inst = self.instantiate_from("codesystem-medication-package-form.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem2(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem2(inst2)

    def implCodeSystem2(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("ampoule"))
        self.assertEqual(
            force_bytes(inst.concept[0].definition),
            force_bytes("A sealed glass capsule containing a liquid"),
        )
        self.assertEqual(force_bytes(inst.concept[0].display), force_bytes("Ampoule"))
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("bottle"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes(
                "A container, typically made of glass or plastic and with a narrow neck, used for storing liquids."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[1].display), force_bytes("Bottle"))
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("box"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes(
                "A container with a flat base and sides, typically square or rectangular and having a lid."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[2].display), force_bytes("Box"))
        self.assertEqual(force_bytes(inst.concept[3].code), force_bytes("cartridge"))
        self.assertEqual(
            force_bytes(inst.concept[3].definition),
            force_bytes(
                "A device of various configuration and composition used with a syringe for the application of anesthetic or other materials to a patient."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[3].display), force_bytes("Cartridge"))
        self.assertEqual(force_bytes(inst.concept[4].code), force_bytes("container"))
        self.assertEqual(
            force_bytes(inst.concept[4].definition),
            force_bytes("A package intended to store pharmaceuticals."),
        )
        self.assertEqual(force_bytes(inst.concept[4].display), force_bytes("Container"))
        self.assertEqual(force_bytes(inst.concept[5].code), force_bytes("tube"))
        self.assertEqual(
            force_bytes(inst.concept[5].definition),
            force_bytes(
                "A long, hollow cylinder of metal, plastic, glass, etc., for holding medications, typically creams or ointments"
            ),
        )
        self.assertEqual(force_bytes(inst.concept[5].display), force_bytes("Tube"))
        self.assertEqual(force_bytes(inst.concept[6].code), force_bytes("unitdose"))
        self.assertEqual(
            force_bytes(inst.concept[6].definition),
            force_bytes(
                "A dose of medicine prepared in an individual package for convenience, safety or monitoring."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[6].display), force_bytes("Unit Dose Blister")
        )
        self.assertEqual(force_bytes(inst.concept[7].code), force_bytes("vial"))
        self.assertEqual(
            force_bytes(inst.concept[7].definition),
            force_bytes(
                "A small container, typically cylindrical and made of glass, used especially for holding liquid medications."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[7].display), force_bytes("Vial"))
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "A coded concept defining the kind of container a medication package is packaged in"
            ),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Informative")
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[1].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("phx"))
        self.assertEqual(force_bytes(inst.id), force_bytes("medication-package-form"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.1.362"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("MedicationContainer"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/medication-package-form"),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/medication-package-form"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testCodeSystem3(self):
        inst = self.instantiate_from("codesystem-special-values.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem3(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem3(inst2)

    def implCodeSystem3(self, inst):
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
            force_bytes("http://hl7.org/fhir/StructureDefinition/codesystem-comments"),
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
            force_bytes("http://hl7.org/fhir/StructureDefinition/codesystem-comments"),
        )
        self.assertEqual(
            force_bytes(inst.concept[5].extension[0].valueString),
            force_bytes("The existence of this subject to review"),
        )
        self.assertEqual(force_bytes(inst.content), force_bytes("complete"))
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
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
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Informative")
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[1].valueInteger, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("special-values"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.1.10"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("SpecialValues"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("extensions"))
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/special-values")
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/special-values"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testCodeSystem4(self):
        inst = self.instantiate_from("codesystem-communication-not-done-reason.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem4(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem4(inst2)

    def implCodeSystem4(self, inst):
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Codes for the reason why a communication was not done."),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Informative")
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[1].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("pc"))
        self.assertEqual(
            force_bytes(inst.id), force_bytes("communication-not-done-reason")
        )
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.1.165"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("CommunicationNotDoneReason")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/communication-not-done-reason"),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/communication-not-done-reason"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testCodeSystem5(self):
        inst = self.instantiate_from("codesystem-codesystem-hierarchy-meaning.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem5(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem5(inst2)

    def implCodeSystem5(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("grouped-by"))
        self.assertEqual(
            force_bytes(inst.concept[0].display), force_bytes("Grouped By")
        )
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("is-a"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes(
                "A hierarchy where the child concepts have an IS-A relationship with the parents - that is, all the properties of the parent are also true for its child concepts"
            ),
        )
        self.assertEqual(force_bytes(inst.concept[1].display), force_bytes("Is-A"))
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("part-of"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes(
                "Child elements list the individual parts of a composite whole (e.g. body site)"
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("The meaning of the hierarchy of concepts in a code system"),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Informative")
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[1].valueInteger, 5)
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("vocab"))
        self.assertEqual(
            force_bytes(inst.id), force_bytes("codesystem-hierarchy-meaning")
        )
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.1.768"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("CodeSystemHierarchyMeaning")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/codesystem-hierarchy-meaning"),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

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
                "The action was not successful due to some kind of catered for error (often equivalent to an HTTP 400 response)."
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Indicates whether the event succeeded or failed"),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Informative")
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[1].valueInteger, 3)
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("sec"))
        self.assertEqual(force_bytes(inst.id), force_bytes("audit-event-outcome"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.1.448"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("AuditEventOutcome"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/audit-event-outcome"),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/audit-event-outcome"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

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
            force_bytes("Canadian health information displosure policy."),
        )
        self.assertEqual(
            force_bytes(inst.concept[0].display), force_bytes("Disclosure-CA")
        )
        self.assertEqual(
            force_bytes(inst.concept[1].code), force_bytes("disclosure-us")
        )
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes("United States health information displosure policy."),
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
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Informative")
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[1].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("fm"))
        self.assertEqual(force_bytes(inst.id), force_bytes("contract-subtype"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.1.720"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablecodesystem"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("Contract Subtype Codes"))
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Financial Management")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/contractsubtypecodes"),
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/contract-subtype"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

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
                "create(type : string) - type is passed through to the application on the standard API, and must be known by it"
            ),
        )
        self.assertEqual(force_bytes(inst.concept[0].display), force_bytes("create"))
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("copy"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition), force_bytes("copy(source)")
        )
        self.assertEqual(force_bytes(inst.concept[1].display), force_bytes("copy"))
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("truncate"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes("truncate(source, length) - source must be stringy type"),
        )
        self.assertEqual(force_bytes(inst.concept[2].display), force_bytes("truncate"))
        self.assertEqual(force_bytes(inst.concept[3].code), force_bytes("escape"))
        self.assertEqual(
            force_bytes(inst.concept[3].definition),
            force_bytes(
                "escape(source, fmt1, fmt2) - change source from one kind of escaping to another (plain, java, xml, json). note that this is for when the string itself is escaped"
            ),
        )
        self.assertEqual(force_bytes(inst.concept[3].display), force_bytes("escape"))
        self.assertEqual(force_bytes(inst.concept[4].code), force_bytes("cast"))
        self.assertEqual(
            force_bytes(inst.concept[4].definition),
            force_bytes(
                "cast(source, type?) - case source from one type to another. target type can be left as implicit if there is one and only one target type known"
            ),
        )
        self.assertEqual(force_bytes(inst.concept[4].display), force_bytes("cast"))
        self.assertEqual(force_bytes(inst.concept[5].code), force_bytes("append"))
        self.assertEqual(
            force_bytes(inst.concept[5].definition),
            force_bytes("append(source...) - source is element or string"),
        )
        self.assertEqual(force_bytes(inst.concept[5].display), force_bytes("append"))
        self.assertEqual(force_bytes(inst.concept[6].code), force_bytes("translate"))
        self.assertEqual(
            force_bytes(inst.concept[6].definition),
            force_bytes("translate(source, uri_of_map) - use the translate operation"),
        )
        self.assertEqual(force_bytes(inst.concept[6].display), force_bytes("translate"))
        self.assertEqual(force_bytes(inst.concept[7].code), force_bytes("reference"))
        self.assertEqual(
            force_bytes(inst.concept[7].definition),
            force_bytes(
                "reference(source : object) - return a string that references the provided tree properly"
            ),
        )
        self.assertEqual(force_bytes(inst.concept[7].display), force_bytes("reference"))
        self.assertEqual(force_bytes(inst.concept[8].code), force_bytes("dateOp"))
        self.assertEqual(
            force_bytes(inst.concept[8].definition),
            force_bytes("Perform a date operation. *Parameters to be documented*"),
        )
        self.assertEqual(force_bytes(inst.concept[8].display), force_bytes("dateOp"))
        self.assertEqual(force_bytes(inst.concept[9].code), force_bytes("uuid"))
        self.assertEqual(
            force_bytes(inst.concept[9].definition),
            force_bytes("Generate a random UUID (in lowercase). No Parameters"),
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description), force_bytes("How data is copied/created")
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Informative")
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[1].valueInteger, 2)
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("fhir"))
        self.assertEqual(force_bytes(inst.id), force_bytes("map-transform"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.1.668"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("StructureMapTransform"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/map-transform")
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/map-transform"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testCodeSystem9(self):
        inst = self.instantiate_from("codesystem-benefit-type.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem9(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem9(inst2)

    def implCodeSystem9(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(force_bytes(inst.concept[0].code), force_bytes("benefit"))
        self.assertEqual(
            force_bytes(inst.concept[0].definition),
            force_bytes("Maximum benefit allowable."),
        )
        self.assertEqual(force_bytes(inst.concept[0].display), force_bytes("Benefit"))
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("deductable"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes("Cost to be incurred before benefits are applied"),
        )
        self.assertEqual(
            force_bytes(inst.concept[1].display), force_bytes("Deductable")
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
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Informative")
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[1].valueInteger, 1)
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("fm"))
        self.assertEqual(force_bytes(inst.id), force_bytes("benefit-type"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.1.599"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablecodesystem"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("Benefit Type Codes"))
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Financial Management")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/benefit-type")
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/benefit-type"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testCodeSystem10(self):
        inst = self.instantiate_from("codesystem-claim-type.json")
        self.assertIsNotNone(inst, "Must have instantiated a CodeSystem instance")
        self.implCodeSystem10(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem10(inst2)

    def implCodeSystem10(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(
            force_bytes(inst.concept[0].code), force_bytes("institutional")
        )
        self.assertEqual(
            force_bytes(inst.concept[0].definition),
            force_bytes("Hospital, clinic and typically inpatient claims."),
        )
        self.assertEqual(
            force_bytes(inst.concept[0].display), force_bytes("Institutional")
        )
        self.assertEqual(force_bytes(inst.concept[1].code), force_bytes("oral"))
        self.assertEqual(
            force_bytes(inst.concept[1].definition),
            force_bytes("Dental, Denture and Hygiene claims."),
        )
        self.assertEqual(force_bytes(inst.concept[1].display), force_bytes("Oral"))
        self.assertEqual(force_bytes(inst.concept[2].code), force_bytes("pharmacy"))
        self.assertEqual(
            force_bytes(inst.concept[2].definition),
            force_bytes("Pharmacy claims for goods and services."),
        )
        self.assertEqual(force_bytes(inst.concept[2].display), force_bytes("Pharmacy"))
        self.assertEqual(force_bytes(inst.concept[3].code), force_bytes("professional"))
        self.assertEqual(
            force_bytes(inst.concept[3].definition),
            force_bytes(
                "Typically outpatient claims from Physician, Psychological, Chiropractor, Physiotherapy, Speach Pathology, rehabilitative, consulting."
            ),
        )
        self.assertEqual(
            force_bytes(inst.concept[3].display), force_bytes("Professional")
        )
        self.assertEqual(force_bytes(inst.concept[4].code), force_bytes("vision"))
        self.assertEqual(
            force_bytes(inst.concept[4].definition),
            force_bytes(
                "Vision claims for professional services and products such as glasses and contact lenses."
            ),
        )
        self.assertEqual(force_bytes(inst.concept[4].display), force_bytes("Vision"))
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
            force_bytes("This value set includes sample Claim Type codes."),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Informative")
        )
        self.assertEqual(
            force_bytes(inst.extension[1].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[1].valueInteger, 2)
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("fm"))
        self.assertEqual(force_bytes(inst.id), force_bytes("claim-type"))
        self.assertEqual(
            force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.1.551"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablecodesystem"),
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("Example Claim Type Codes")
        )
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Financial Management")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/ex-claimtype")
        )
        self.assertEqual(
            force_bytes(inst.valueSet),
            force_bytes("http://hl7.org/fhir/ValueSet/claim-type"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))
