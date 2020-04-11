# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ValueSet
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
        inst = self.instantiate_from("valueset-encounter-status.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet1(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet1(inst2)

    def implValueSet1(self, inst):
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description), force_bytes("Current state of the encounter")
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
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("pa"))
        self.assertEqual(force_bytes(inst.id), force_bytes("encounter-status"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.241"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("EncounterStatus"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/encounter-status"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testValueSet2(self):
        inst = self.instantiate_from("valueset-report-status-codes.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet2(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet2(inst2)

    def implValueSet2(self, inst):
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("The current status of the test report."),
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
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"
            ),
        )
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("fhir"))
        self.assertEqual(force_bytes(inst.id), force_bytes("report-status-codes"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.712"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("TestReportStatus"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/report-status-codes"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testValueSet3(self):
        inst = self.instantiate_from("valueset-note-type.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet3(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet3(inst2)

    def implValueSet3(self, inst):
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("The presentation types of notes."),
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
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("fm"))
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
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("NoteType"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url), force_bytes("http://hl7.org/fhir/ValueSet/note-type")
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testValueSet4(self):
        inst = self.instantiate_from("valueset-sequence-quality-method.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet4(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet4(inst2)

    def implValueSet4(self, inst):
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("This value set includes sequence quality method"),
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
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("cg"))
        self.assertEqual(force_bytes(inst.id), force_bytes("sequence-quality-method"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.218"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("FDA-Method"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project team"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/sequence-quality-method"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testValueSet5(self):
        inst = self.instantiate_from("valueset-issue-severity.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet5(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet5(inst2)

    def implValueSet5(self, inst):
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("How the issue affects the success of the action."),
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
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("fhir"))
        self.assertEqual(force_bytes(inst.id), force_bytes("issue-severity"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.397"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("IssueSeverity"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/issue-severity"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testValueSet6(self):
        inst = self.instantiate_from("valueset-sequence-referenceSeq.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet6(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet6(inst2)

    def implValueSet6(self, inst):
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("This value set includes all Reference codes"),
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
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("cg"))
        self.assertEqual(force_bytes(inst.id), force_bytes("sequence-referenceSeq"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.216"),
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("ENSEMBL"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project team"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/sequence-referenceSeq"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testValueSet7(self):
        inst = self.instantiate_from("valueset-process-outcome.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet7(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet7(inst2)

    def implValueSet7(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://hl7.org/fhir/processoutcomecodes"),
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("This value set includes sample Process Outcome codes."),
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
        self.assertEqual(force_bytes(inst.id), force_bytes("process-outcome"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.677"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("Process Outcome Codes"))
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Financial Management")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/process-outcome"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testValueSet8(self):
        inst = self.instantiate_from("valueset-claim-exception.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet8(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet8(inst2)

    def implValueSet8(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://hl7.org/fhir/claim-exception"),
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
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("This value set includes sample Exception codes."),
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
        self.assertEqual(force_bytes(inst.id), force_bytes("claim-exception"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.572"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("Exception Codes"))
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("Financial Management")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/claim-exception"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))

    def testValueSet9(self):
        inst = self.instantiate_from("valueset-object-lifecycle-events.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet9(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet9(inst2)

    def implValueSet9(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://hl7.org/fhir/dicom-audit-lifecycle"),
        )
        self.assertEqual(
            force_bytes(inst.compose.include[1].system),
            force_bytes("http://hl7.org/fhir/iso-21089-lifecycle"),
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
        self.assertEqual(inst.date.date, FHIRDate("2017-02-19T18:00:00+01:00").date)
        self.assertEqual(inst.date.as_json(), "2017-02-19T18:00:00+01:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "This example FHIR value set is comprised of lifecycle event codes. The FHIR Actor value set is based on    DICOM Audit Message, ParticipantObjectDataLifeCycle;   ISO Standard, TS 21089-2017;  "
            ),
        )
        self.assertFalse(inst.experimental)
        self.assertTrue(inst.extensible)
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
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[1].valueString), force_bytes("Trial Use")
        )
        self.assertEqual(
            force_bytes(inst.extension[2].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm"
            ),
        )
        self.assertEqual(inst.extension[2].valueInteger, 3)
        self.assertEqual(force_bytes(inst.id), force_bytes("object-lifecycle-events"))
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("ObjectLifecycleEvents"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 (FHIR Project)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml"> This value set includes codes from multiple codesets. </div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/object-lifecycle-events"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("1.1.0"))

    def testValueSet10(self):
        inst = self.instantiate_from("valueset-entformula-additive.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet10(inst)

        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet10(inst2)

    def implValueSet10(self, inst):
        self.assertEqual(
            force_bytes(inst.compose.include[0].system),
            force_bytes("http://hl7.org/fhir/entformula-additive"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-04-19T07:44:43+10:00").date)
        self.assertEqual(inst.date.as_json(), "2017-04-19T07:44:43+10:00")
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
        self.assertEqual(force_bytes(inst.extension[2].valueCode), force_bytes("oo"))
        self.assertEqual(force_bytes(inst.id), force_bytes("entformula-additive"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:2.16.840.1.113883.4.642.3.379"),
        )
        self.assertTrue(inst.immutable)
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2017-04-19T07:44:43.294+10:00").date
        )
        self.assertEqual(
            inst.meta.lastUpdated.as_json(), "2017-04-19T07:44:43.294+10:00"
        )
        self.assertEqual(
            force_bytes(inst.meta.profile[0]),
            force_bytes("http://hl7.org/fhir/StructureDefinition/shareablevalueset"),
        )
        self.assertEqual(
            force_bytes(inst.name), force_bytes("Enteral Formula Additive Type Code")
        )
        self.assertEqual(
            force_bytes(inst.publisher), force_bytes("FHIR NutritionOrder team")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/ValueSet/entformula-additive"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))
