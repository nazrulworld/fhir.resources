#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-01-11.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json
from fhir.resources import procedurerequest
from fhir.resources.fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ProcedureRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ProcedureRequest", js["resourceType"])
        return procedurerequest.ProcedureRequest(js)
    
    def testProcedureRequest1(self):
        inst = self.instantiate_from("procedurerequest-example-ft4.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest1(inst2)
    
    def implProcedureRequest1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "3024-7")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Free T4")
        self.assertEqual(inst.id, "ft4")
        self.assertEqual(inst.intent, "reflex-order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2015-08-27T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2015-08-27T09:33:27+07:00")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest2(self):
        inst = self.instantiate_from("procedurerequest-example-edu.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest2(inst2)
    
    def implProcedureRequest2(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-08-16").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-08-16")
        self.assertEqual(inst.category[0].coding[0].code, "311401005")
        self.assertEqual(inst.category[0].coding[0].display, "Patient education (procedure)")
        self.assertEqual(inst.category[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].text, "Education")
        self.assertEqual(inst.code.coding[0].code, "48023004")
        self.assertEqual(inst.code.coding[0].display, "Breast self-examination technique education (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Health education - breast examination")
        self.assertEqual(inst.id, "education")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-08-16")
        self.assertEqual(inst.reasonCode[0].text, "early detection of breast mass")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest3(self):
        inst = self.instantiate_from("procedurerequest-genetics-example-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest3(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest3(inst2)
    
    def implProcedureRequest3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "49874-1")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "ABCB4 gene mutation analysis")
        self.assertEqual(inst.id, "og-example1")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-05-12T16:16:00-07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-05-12T16:16:00-07:00")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest4(self):
        inst = self.instantiate_from("procedurerequest-example-lipid.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest4(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest4(inst2)
    
    def implProcedureRequest4(self, inst):
        self.assertEqual(inst.code.coding[0].code, "LIPID")
        self.assertEqual(inst.code.coding[0].system, "http://acme.org/tests")
        self.assertEqual(inst.code.text, "Lipid Panel")
        self.assertEqual(inst.contained[0].id, "fasting")
        self.assertEqual(inst.contained[1].id, "serum")
        self.assertEqual(inst.id, "lipid")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "PLAC")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://hl7.org/fhir/identifier-type")
        self.assertEqual(inst.identifier[0].type.text, "Placer")
        self.assertEqual(inst.identifier[0].value, "2345234234234")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.note[0].text, "patient is afraid of needles")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-02T16:16:00-07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-02T16:16:00-07:00")
        self.assertEqual(inst.reasonCode[0].coding[0].code, "V173")
        self.assertEqual(inst.reasonCode[0].coding[0].display, "Fam hx-ischem heart dis")
        self.assertEqual(inst.reasonCode[0].coding[0].system, "http://hl7.org/fhir/sid/icd-9")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest5(self):
        inst = self.instantiate_from("procedurerequest-example-pgx.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest5(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest5(inst2)
    
    def implProcedureRequest5(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-10-10T15:00:00-07:00").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-10-10T15:00:00-07:00")
        self.assertEqual(inst.code.coding[0].code, "47403-1")
        self.assertEqual(inst.code.coding[0].display, "CYP2D6 gene targeted mutation analysis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.id, "example-pgx")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest6(self):
        inst = self.instantiate_from("procedurerequest-example-di.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest6(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest6(inst2)
    
    def implProcedureRequest6(self, inst):
        self.assertEqual(inst.code.coding[0].code, "24627-2")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Chest CT")
        self.assertEqual(inst.id, "di")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(inst.reasonCode[0].text, "Check for metastatic disease")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest7(self):
        inst = self.instantiate_from("procedurerequest-example-pt.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest7(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest7(inst2)
    
    def implProcedureRequest7(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-09-20").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-09-20")
        self.assertEqual(inst.bodySite[0].coding[0].code, "36701003")
        self.assertEqual(inst.bodySite[0].coding[0].display, "Both knees (body structure)")
        self.assertEqual(inst.bodySite[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.bodySite[0].text, "Both knees")
        self.assertEqual(inst.category[0].coding[0].code, "386053000")
        self.assertEqual(inst.category[0].coding[0].display, "Evaluation procedure (procedure)")
        self.assertEqual(inst.category[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].text, "Evaluation")
        self.assertEqual(inst.code.coding[0].code, "710830005")
        self.assertEqual(inst.code.coding[0].display, "Assessment of passive range of motion (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Assessment of passive range of motion")
        self.assertEqual(inst.id, "physical-therapy")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-09-27").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-09-27")
        self.assertEqual(inst.reasonCode[0].text, "assessment of mobility limitations due to osteoarthritis")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest8(self):
        inst = self.instantiate_from("procedurerequest-example-colonoscopy.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest8(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest8(inst2)
    
    def implProcedureRequest8(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-05").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-05")
        self.assertEqual(inst.code.coding[0].code, "73761001")
        self.assertEqual(inst.code.coding[0].display, "Colonoscopy (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Colonoscopy")
        self.assertEqual(inst.id, "colonoscopy")
        self.assertEqual(inst.identifier[0].value, "45678")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.requisition.system, "http://bumc.org/requisitions")
        self.assertEqual(inst.requisition.value, "req12345")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest9(self):
        inst = self.instantiate_from("procedurerequest-example-implant.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest9(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest9(inst2)
    
    def implProcedureRequest9(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-03-30").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-03-30")
        self.assertEqual(inst.code.coding[0].code, "25267002")
        self.assertEqual(inst.code.coding[0].display, "Insertion of intracardiac pacemaker (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Implant Pacemaker")
        self.assertEqual(inst.id, "example-implant")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.reasonCode[0].text, "Bradycardia")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest10(self):
        inst = self.instantiate_from("procedurerequest-example4.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest10(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest10(inst2)
    
    def implProcedureRequest10(self, inst):
        self.assertEqual(inst.code.coding[0].code, "229115003")
        self.assertEqual(inst.code.coding[0].display, "Bench Press (regime/therapy) ")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "benchpress")
        self.assertEqual(inst.intent, "plan")
        self.assertEqual(inst.note[0].text, "Start with 30kg and increase in increments of 5kg when you feel ready")
        self.assertEqual(inst.occurrenceTiming.repeat.count, 20)
        self.assertEqual(inst.occurrenceTiming.repeat.countMax, 30)
        self.assertEqual(inst.occurrenceTiming.repeat.frequency, 3)
        self.assertEqual(inst.occurrenceTiming.repeat.period, 1)
        self.assertEqual(inst.occurrenceTiming.repeat.periodUnit, "wk")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

