# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ServiceRequest
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

from .. import servicerequest
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ServiceRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ServiceRequest", js["resourceType"])
        return servicerequest.ServiceRequest(js)

    def testServiceRequest1(self):
        inst = self.instantiate_from("servicerequest-example2.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest1(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest1(inst2)

    def implServiceRequest1(self, inst):
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
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.text), force_bytes("Placer")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("20170201-0001")
        )
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
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

    def testServiceRequest2(self):
        inst = self.instantiate_from("servicerequest-example3.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest2(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest2(inst2)

    def implServiceRequest2(self, inst):
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
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.priority), force_bytes("stat"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testServiceRequest3(self):
        inst = self.instantiate_from("servicerequest-example-lipid.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest3(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest3(inst2)

    def implServiceRequest3(self, inst):
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
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.text), force_bytes("Placer")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("2345234234234")
        )
        self.assertEqual(force_bytes(inst.intent), force_bytes("original-order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
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

    def testServiceRequest4(self):
        inst = self.instantiate_from("servicerequest-example-colonoscopy-bx.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest4(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest4(inst2)

    def implServiceRequest4(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-05").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-05")
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("76164006"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Biopsy of colon (procedure)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Biopsy of colon"))
        self.assertEqual(force_bytes(inst.id), force_bytes("colon-biopsy"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.requisition.system),
            force_bytes("http://bumc.org/requisitions"),
        )
        self.assertEqual(force_bytes(inst.requisition.value), force_bytes("req12345"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testServiceRequest5(self):
        inst = self.instantiate_from("servicerequest-example4.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest5(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest5(inst2)

    def implServiceRequest5(self, inst):
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
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.occurrenceTiming.repeat.count, 20)
        self.assertEqual(inst.occurrenceTiming.repeat.countMax, 30)
        self.assertEqual(inst.occurrenceTiming.repeat.frequency, 3)
        self.assertEqual(inst.occurrenceTiming.repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.occurrenceTiming.repeat.periodUnit), force_bytes("wk")
        )
        self.assertEqual(
            force_bytes(inst.patientInstruction),
            force_bytes(
                "Start with 30kg 10-15 repetitions for three sets and increase in increments of 5kg when you feel ready"
            ),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testServiceRequest6(self):
        inst = self.instantiate_from("servicerequest-example-edu.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest6(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest6(inst2)

    def implServiceRequest6(self, inst):
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
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-08-16")
        self.assertEqual(
            force_bytes(inst.reasonCode[0].text),
            force_bytes("early detection of breast mass"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testServiceRequest7(self):
        inst = self.instantiate_from("servicerequest-example-ventilation.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest7(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest7(inst2)

    def implServiceRequest7(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2018-02-20").date)
        self.assertEqual(inst.authoredOn.as_json(), "2018-02-20")
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("40617009"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].display),
            force_bytes("Artificial respiration (procedure)"),
        )
        self.assertEqual(
            force_bytes(inst.code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.code.text), force_bytes("Mechanical Ventilation")
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("vent"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.orderDetail[0].coding[0].code), force_bytes("243144002")
        )
        self.assertEqual(
            force_bytes(inst.orderDetail[0].coding[0].display),
            force_bytes("Patient triggered inspiratory assistance (procedure)"),
        )
        self.assertEqual(
            force_bytes(inst.orderDetail[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(force_bytes(inst.orderDetail[0].text), force_bytes("IPPB"))
        self.assertEqual(
            force_bytes(inst.orderDetail[1].text),
            force_bytes(
                " Initial Settings : Sens: -1 cm H20 Pressure 15 cm H2O moderate flow:  Monitor VS every 15 minutes x 4 at the start of mechanical ventilation, then routine for unit OR every 5 hr"
            ),
        )
        self.assertEqual(
            force_bytes(inst.reasonCode[0].text),
            force_bytes("chronic obstructive lung disease (COLD)"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testServiceRequest8(self):
        inst = self.instantiate_from("servicerequest-example-ambulation.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest8(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest8(inst2)

    def implServiceRequest8(self, inst):
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
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testServiceRequest9(self):
        inst = self.instantiate_from("servicerequest-example-pt.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest9(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest9(inst2)

    def implServiceRequest9(self, inst):
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
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-09-27").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-09-27")
        self.assertEqual(
            force_bytes(inst.reasonCode[0].text),
            force_bytes("assessment of mobility limitations due to osteoarthritis"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testServiceRequest10(self):
        inst = self.instantiate_from("servicerequest-example-di.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest10(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest10(inst2)

    def implServiceRequest10(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("24627-2"))
        self.assertEqual(
            force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org")
        )
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Chest CT"))
        self.assertEqual(force_bytes(inst.id), force_bytes("di"))
        self.assertEqual(force_bytes(inst.intent), force_bytes("original-order"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
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
