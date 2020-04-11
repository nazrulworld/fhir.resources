# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcedureRequest
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

from .. import procedurerequest
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ProcedureRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ProcedureRequest", js["resourceType"])
        return procedurerequest.ProcedureRequest(js)

    def testProcedureRequest1(self):
        inst = self.instantiate_from("procedurerequest-example-lipid.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest1(inst)

        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest1(inst2)

    def implProcedureRequest1(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("LIPID"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://acme.org/tests"),
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Lipid Panel"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("fasting"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("serum"))
        self.assertEqual(force_bytes(inst.id), force_bytes("lipid"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:oid:1.3.4.5.6.7")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("PLAC")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://hl7.org/fhir/identifier-type"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.text), force_bytes("Placer")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("2345234234234")
        )
        self.assertEqual(force_bytes(inst.intent), force_bytes("original-order"))
        self.assertEqual(
            force_bytes(inst.note[0].text), force_bytes("patient is afraid of needles")
        )
        self.assertEqual(
            inst.occurrenceDateTime.date, FHIRDate("2013-05-02T16:16:00-07:00").date
        )
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-02T16:16:00-07:00")
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("V173")
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].display),
            force_bytes("Fam hx-ischem heart dis"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/sid/icd-9"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProcedureRequest2(self):
        inst = self.instantiate_from("procedurerequest-example4.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest2(inst)

        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest2(inst2)

    def implProcedureRequest2(self, inst):
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("229115003")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Bench Press (regime/therapy) "),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("benchpress"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("plan"))
        self.assertEqual(
            force_bytes(inst.note[0].text),
            force_bytes(
                "Start with 30kg and increase in increments of 5kg when you feel ready"
            ),
        )
        self.assertEqual(inst.occurrenceTiming.repeat.count, 20)
        self.assertEqual(inst.occurrenceTiming.repeat.countMax, 30)
        self.assertEqual(inst.occurrenceTiming.repeat.frequency, 3)
        self.assertEqual(inst.occurrenceTiming.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.occurrenceTiming.repeat.periodUnit), force_bytes("wk")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProcedureRequest3(self):
        inst = self.instantiate_from("procedurerequest-example-edu.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest3(inst)

        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest3(inst2)

    def implProcedureRequest3(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-08-16").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-08-16")
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("311401005")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display),
            force_bytes("Patient education (procedure)"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Education"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("48023004"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Breast self-examination technique education (procedure)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.code.text),
            force_bytes("Health education - breast examination"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("education"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.reasonCode[0].text),
            force_bytes("early detection of breast mass"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProcedureRequest4(self):
        inst = self.instantiate_from("procedurerequest-example-pt.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest4(inst)

        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest4(inst2)

    def implProcedureRequest4(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-09-20").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-09-20")
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].code), force_bytes("36701003")
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].display),
            force_bytes("Both knees (body structure)"),
        )
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.bodySite[0].text), force_bytes("Both knees"))
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].code), force_bytes("386053000")
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].display),
            force_bytes("Evaluation procedure (procedure)"),
        )
        self.assertEqual(
            force_bytes(inst.category[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Evaluation"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("710830005")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Assessment of passive range of motion (procedure)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.code.text),
            force_bytes("Assessment of passive range of motion"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("physical-therapy"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-09-27").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-09-27")
        self.assertEqual(
            force_bytes(inst.reasonCode[0].text),
            force_bytes("assessment of mobility limitations due to osteoarthritis"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProcedureRequest5(self):
        inst = self.instantiate_from("procedurerequest-genetics-example-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest5(inst)

        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest5(inst2)

    def implProcedureRequest5(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("49874-1"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(
            force_bytes(inst.code.text), force_bytes("ABCB4 gene mutation analysis")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("og-example1"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("original-order"))
        self.assertEqual(
            inst.occurrenceDateTime.date, FHIRDate("2014-05-12T16:16:00-07:00").date
        )
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-05-12T16:16:00-07:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProcedureRequest6(self):
        inst = self.instantiate_from("procedurerequest-example-di.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest6(inst)

        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest6(inst2)

    def implProcedureRequest6(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("24627-2"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Chest CT"))
        self.assertEqual(force_bytes(inst.id), force_bytes("di"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("original-order"))
        self.assertEqual(
            inst.occurrenceDateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date
        )
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(
            force_bytes(inst.reasonCode[0].text),
            force_bytes("Check for metastatic disease"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProcedureRequest7(self):
        inst = self.instantiate_from("procedurerequest-example-subrequest.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest7(inst)

        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest7(inst2)

    def implProcedureRequest7(self, inst):
        self.assertEqual(
            force_bytes(inst.bodySite[0].coding[0].display), force_bytes("Right arm")
        )
        self.assertEqual(force_bytes(inst.bodySite[0].text), force_bytes("Right arm"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("35542-0"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Peanut IgG"))
        self.assertEqual(force_bytes(inst.id), force_bytes("subrequest"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("instance-order"))
        self.assertEqual(
            inst.occurrenceDateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date
        )
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(
            force_bytes(inst.performerType.coding[0].display),
            force_bytes("Qualified nurse"),
        )
        self.assertEqual(force_bytes(inst.performerType.text), force_bytes("Nurse"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(
            force_bytes(inst.reasonCode[0].text),
            force_bytes("Check for Peanut Allergy"),
        )
        self.assertEqual(force_bytes(inst.requisition.value), force_bytes("A13848392"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProcedureRequest8(self):
        inst = self.instantiate_from("procedurerequest-example2.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest8(inst)

        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest8(inst2)

    def implProcedureRequest8(self, inst):
        self.assertEqual(
            force_bytes(inst.asNeededCodeableConcept.text),
            force_bytes("as needed to clear mucus"),
        )
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-02-01T17:23:07Z").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-02-01T17:23:07Z")
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("34431008"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Physiotherapy of chest (regime/therapy) "),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("signature"))
        self.assertEqual(
            force_bytes(inst.contained[1].id), force_bytes("cystic-fibrosis")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("physiotherapy"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://goodhealth.org/placer-ids"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("PLAC")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].display),
            force_bytes("Placer Identifier"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://hl7.org/fhir/identifier-type"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.text), force_bytes("Placer")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("20170201-0001")
        )
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(inst.occurrenceTiming.repeat.duration, 15)
        self.assertEqual(inst.occurrenceTiming.repeat.durationMax, 25)
        self.assertEqual(
            force_bytes(inst.occurrenceTiming.repeat.durationUnit), force_bytes("min")
        )
        self.assertEqual(inst.occurrenceTiming.repeat.frequency, 1)
        self.assertEqual(inst.occurrenceTiming.repeat.frequencyMax, 4)
        self.assertEqual(inst.occurrenceTiming.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.occurrenceTiming.repeat.periodUnit), force_bytes("d")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProcedureRequest9(self):
        inst = self.instantiate_from("procedurerequest-example3.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest9(inst)

        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest9(inst2)

    def implProcedureRequest9(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-02-01T17:23:07Z").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-02-01T17:23:07Z")
        self.assertEqual(
            force_bytes(inst.code.coding[0].code), force_bytes("359962006")
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Turning patient in bed (procedure)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertTrue(inst.doNotPerform)
        self.assertEqual(force_bytes(inst.id), force_bytes("do-not-turn"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://goodhealth.org/placer-ids"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("20170201-0002")
        )
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("stat"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testProcedureRequest10(self):
        inst = self.instantiate_from("procedurerequest-example-ambulation.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest10(inst)

        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest10(inst2)

    def implProcedureRequest10(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-05").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-05")
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("62013009"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Ambulating patient (procedure)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Ambulation"))
        self.assertEqual(force_bytes(inst.id), force_bytes("ambulation"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("45678"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
