# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
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

from .. import valueset
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ValueSetTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ValueSet", js["resourceType"])
        return valueset.ValueSet(js)

    def testValueSet1(self):
        inst = self.instantiate_from("valueset-device-status-reason.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet1(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet1(inst2)

    def implValueSet1(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/device-status-reason"),
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("The availability status reason of the device."),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("oo"))
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
        self.assertEqual(force_bytes(inst.id), force_bytes("device-status-reason"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.1081"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("FHIRDeviceStatusReason"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("FHIRDeviceStatusReason"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/device-status-reason"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testValueSet2(self):
        inst = self.instantiate_from("valueset-definition-resource-types.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet2(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet2(inst2)

    def implValueSet2(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://hl7.org/fhir/definition-resource-types"),
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "A list of all the definition resource types defined in this version of the FHIR specification."
            ),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("vocab"))
        self.assertEqual(force_bytes(inst.id), force_bytes("definition-resource-types"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.1056"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("DefinitionResourceType"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("DefinitionResourceType"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/definition-resource-types"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testValueSet3(self):
        inst = self.instantiate_from("valueset-bodystructure-relative-location.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet3(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet3(inst2)

    def implValueSet3(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[0].code),
            force_bytes("419161000"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[0].display),
            force_bytes("Unilateral left"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[1].code),
            force_bytes("419465000"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[1].display),
            force_bytes("Unilateral right"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[2].code),
            force_bytes("51440002"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[2].display),
            force_bytes("Bilateral"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[3].code),
            force_bytes("261183002"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[3].display),
            force_bytes("Upper"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[4].code),
            force_bytes("261122009"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[4].display),
            force_bytes("Lower"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[5].code),
            force_bytes("255561001"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[5].display),
            force_bytes("Medial"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[6].code),
            force_bytes("49370004"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[6].display),
            force_bytes("Lateral"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[7].code),
            force_bytes("264217000"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[7].display),
            force_bytes("Superior"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[8].code),
            force_bytes("261089000"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[8].display),
            force_bytes("Inferior"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[9].code),
            force_bytes("255551008"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].concept[9].display),
            force_bytes("Posterior"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("SNOMED-CT concepts modifying the anatomic location"),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("oo"))
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
            force_bytes(inst.id), force_bytes("bodystructure-relative-location")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.140"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("BodystructureLocationQualifier")
        )
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Order and Observation Workgroup")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.title), force_bytes("Bodystructure Location Qualifier")
        )
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/bodystructure-relative-location"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testValueSet4(self):
        inst = self.instantiate_from("valueset-encounter-status.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet4(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet4(inst2)

    def implValueSet4(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://hl7.org/fhir/encounter-status"),
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Current state of the encounter."),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("pa"))
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
        self.assertEqual(force_bytes(inst.id), force_bytes("encounter-status"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.246"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("EncounterStatus"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("EncounterStatus"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/encounter-status"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testValueSet5(self):
        inst = self.instantiate_from("valueset-consent-scope.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet5(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet5(inst2)

    def implValueSet5(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/consentscope"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.copyright), force_bytes("This is an example set.")
        )
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("This value set includes the four Consent scope codes."),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("cbcc"))
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
        self.assertEqual(force_bytes(inst.id), force_bytes("consent-scope"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.761"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("ConsentScopeCodes"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("CBCC"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Consent Scope Codes"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/consent-scope"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testValueSet6(self):
        inst = self.instantiate_from("valueset-report-status-codes.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet6(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet6(inst2)

    def implValueSet6(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://hl7.org/fhir/report-status-codes"),
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("The current status of the test report."),
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
        self.assertEqual(inst.extension[2].valueInteger, 0)
        self.assertEqual(force_bytes(inst.id), force_bytes("report-status-codes"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.724"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("TestReportStatus"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("TestReportStatus"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/report-status-codes"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testValueSet7(self):
        inst = self.instantiate_from("valueset-note-type.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet7(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet7(inst2)

    def implValueSet7(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://hl7.org/fhir/note-type"),
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("The presentation types of notes."),
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
        self.assertEqual(force_bytes(inst.id), force_bytes("note-type"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.15"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("NoteType"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("NoteType"))
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/ValueSet/note-type")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testValueSet8(self):
        inst = self.instantiate_from("valueset-sequence-quality-method.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet8(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet8(inst2)

    def implValueSet8(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("https://precision.fda.gov/apps/"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[1].system),
            force_bytes("https://precision.fda.gov/jobs/"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("This value set includes sequence quality method"),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("cg"))
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
        self.assertEqual(force_bytes(inst.id), force_bytes("sequence-quality-method"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.223"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("FDA-Method"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project team"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("F d a- method"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/sequence-quality-method"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testValueSet9(self):
        inst = self.instantiate_from("valueset-issue-severity.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet9(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet9(inst2)

    def implValueSet9(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://hl7.org/fhir/issue-severity"),
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
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("How the issue affects the success of the action."),
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
        self.assertEqual(force_bytes(inst.id), force_bytes("issue-severity"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.408"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("IssueSeverity"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("IssueSeverity"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/issue-severity"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))

    def testValueSet10(self):
        inst = self.instantiate_from("valueset-sequence-referenceSeq.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet10(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet10(inst2)

    def implValueSet10(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://www.ensembl.org"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[1].system),
            force_bytes("http://www.ncbi.nlm.nih.gov/nuccore"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2019-11-01T09:29:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("This value set includes all Reference codes"),
        )
        self.assertFalse(inst.experimental)
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[0].valueCode), force_bytes("cg"))
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
        self.assertEqual(force_bytes(inst.id), force_bytes("sequence-referenceSeq"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.221"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2019-11-01T09:29:23.356+11:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("ENSEMBL"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project team"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("E n s e m b l"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/sequence-referenceSeq"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("4.0.1"))
