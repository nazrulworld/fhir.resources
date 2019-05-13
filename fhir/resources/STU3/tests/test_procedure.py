#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-05-13.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import procedure
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ProcedureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Procedure", js["resourceType"])
        return procedure.Procedure(js)
    
    def testProcedure1(self):
        inst = self.instantiate_from("procedure-example-colonoscopy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure1(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure1(inst2)
    
    def implProcedure1(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("73761001"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Colonoscopy (procedure)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Colonoscopy"))
        self.assertEqual(force_bytes(inst.id), force_bytes("colonoscopy"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertFalse(inst.notDone)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Colonoscopy with complication</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcedure2(self):
        inst = self.instantiate_from("procedure-example-f003-abscess.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure2(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure2(inst2)
    
    def implProcedure2(self, inst):
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].code), force_bytes("83030008"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].display), force_bytes("Retropharyngeal area"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("172960003"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Incision of retropharyngeal abscess"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.followUp[0].text), force_bytes("described in care plan"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f003"))
        self.assertEqual(force_bytes(inst.outcome.text), force_bytes("removal of the retropharyngeal abscess"))
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-03-24T10:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.end.as_json(), "2013-03-24T10:30:10+01:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-03-24T09:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.start.as_json(), "2013-03-24T09:30:10+01:00")
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].code), force_bytes("01.000"))
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].display), force_bytes("Arts"))
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].system), force_bytes("urn:oid:2.16.840.1.113883.2.4.15.111"))
        self.assertEqual(force_bytes(inst.performer[0].role.text), force_bytes("Care role"))
        self.assertEqual(force_bytes(inst.reasonCode[0].text), force_bytes("abcess in retropharyngeal area"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcedure3(self):
        inst = self.instantiate_from("procedure-example-biopsy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure3(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure3(inst2)
    
    def implProcedure3(self, inst):
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].code), force_bytes("368225008"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].display), force_bytes("Entire Left Forearm"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.bodySite[0].text), force_bytes("Left forearm"))
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("103693007"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Diagnostic procedure (procedure)"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.category.text), force_bytes("Diagnostic procedure"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("90105005"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Biopsy of soft tissue of forearm (Procedure)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Biopsy of suspected melanoma L) arm"))
        self.assertEqual(force_bytes(inst.complication[0].coding[0].code), force_bytes("67750007"))
        self.assertEqual(force_bytes(inst.complication[0].coding[0].display), force_bytes("Ineffective airway clearance (finding)"))
        self.assertEqual(force_bytes(inst.complication[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.complication[0].text), force_bytes("Ineffective airway clearance"))
        self.assertEqual(force_bytes(inst.followUp[0].text), force_bytes("Review in clinic"))
        self.assertEqual(force_bytes(inst.id), force_bytes("biopsy"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Standard Biopsy"))
        self.assertEqual(inst.performedDateTime.date, FHIRDate("2014-02-03").date)
        self.assertEqual(inst.performedDateTime.as_json(), "2014-02-03")
        self.assertEqual(force_bytes(inst.reasonCode[0].text), force_bytes("Dark lesion l) forearm. getting darker last 3 months."))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Biopsy of suspected melanoma L) arm</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.usedCode[0].coding[0].code), force_bytes("79068005"))
        self.assertEqual(force_bytes(inst.usedCode[0].coding[0].display), force_bytes("Needle, device (physical object)"))
        self.assertEqual(force_bytes(inst.usedCode[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.usedCode[0].text), force_bytes("30-guage needle"))
    
    def testProcedure4(self):
        inst = self.instantiate_from("procedure-example-f201-tpf.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure4(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure4(inst2)
    
    def implProcedure4(self, inst):
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].code), force_bytes("272676008"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].display), force_bytes("Sphenoid bone"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("367336001"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Chemotherapy"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f201"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Eerste neo-adjuvante TPF-kuur bij groot proces in sphenoid met intracraniale uitbreiding."))
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-01-28T14:27:00+01:00").date)
        self.assertEqual(inst.performedPeriod.end.as_json(), "2013-01-28T14:27:00+01:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-01-28T13:31:00+01:00").date)
        self.assertEqual(inst.performedPeriod.start.as_json(), "2013-01-28T13:31:00+01:00")
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].code), force_bytes("310512001"))
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].display), force_bytes("Medical oncologist"))
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.reasonCode[0].text), force_bytes("DiagnosticReport/f201"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcedure5(self):
        inst = self.instantiate_from("procedure-example-f002-lung.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure5(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure5(inst2)
    
    def implProcedure5(self, inst):
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].code), force_bytes("39607008"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].display), force_bytes("Lung structure"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("359615001"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Partial lobectomy of lung"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.followUp[0].text), force_bytes("described in care plan"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f002"))
        self.assertEqual(force_bytes(inst.outcome.text), force_bytes("improved blood circulation"))
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-03-08T09:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.end.as_json(), "2013-03-08T09:30:10+01:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-03-08T09:00:10+01:00").date)
        self.assertEqual(inst.performedPeriod.start.as_json(), "2013-03-08T09:00:10+01:00")
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].code), force_bytes("01.000"))
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].display), force_bytes("Arts"))
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].system), force_bytes("urn:oid:2.16.840.1.113883.2.4.15.111"))
        self.assertEqual(force_bytes(inst.performer[0].role.text), force_bytes("Care role"))
        self.assertEqual(force_bytes(inst.reasonCode[0].text), force_bytes("Malignant tumor of lung"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcedure6(self):
        inst = self.instantiate_from("procedure-example-ambulation.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure6(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure6(inst2)
    
    def implProcedure6(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("62013009"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Ambulating patient (procedure)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Ambulation"))
        self.assertEqual(force_bytes(inst.id), force_bytes("ambulation"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertTrue(inst.notDone)
        self.assertEqual(force_bytes(inst.notDoneReason.coding[0].code), force_bytes("398254007"))
        self.assertEqual(force_bytes(inst.notDoneReason.coding[0].display), force_bytes("  Pre-eclampsia (disorder)"))
        self.assertEqual(force_bytes(inst.notDoneReason.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.notDoneReason.text), force_bytes("Pre-eclampsia"))
        self.assertEqual(force_bytes(inst.status), force_bytes("suspended"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Ambulation procedure was not done</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcedure7(self):
        inst = self.instantiate_from("procedure-example-education.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure7(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure7(inst2)
    
    def implProcedure7(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("311401005"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Patient education (procedure)"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.category.text), force_bytes("Education"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("48023004"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Breast self-examination technique education (procedure)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Health education - breast examination"))
        self.assertEqual(force_bytes(inst.id), force_bytes("education"))
        self.assertEqual(inst.performedDateTime.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.performedDateTime.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.reasonCode[0].text), force_bytes("early detection of breast mass"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Health education - breast examination for early detection of breast mass</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcedure8(self):
        inst = self.instantiate_from("procedure-example-colon-biopsy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure8(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure8(inst2)
    
    def implProcedure8(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("76164006"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Biopsy of colon (procedure)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Biopsy of colon"))
        self.assertEqual(force_bytes(inst.id), force_bytes("colon-biopsy"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertFalse(inst.notDone)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Biopsy of colon, which was part of colonoscopy</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcedure9(self):
        inst = self.instantiate_from("procedure-example-appendectomy-narrative.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure9(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure9(inst2)
    
    def implProcedure9(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("appendectomy-narrative"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Routine Appendectomy in April 2013 performed by Dr Cecil Surgeon</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
    
    def testProcedure10(self):
        inst = self.instantiate_from("procedure-example-f004-tracheotomy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure10(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure10(inst2)
    
    def implProcedure10(self, inst):
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].code), force_bytes("83030008"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].display), force_bytes("Retropharyngeal area"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("48387007"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Tracheotomy"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.followUp[0].text), force_bytes("described in care plan"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f004"))
        self.assertEqual(force_bytes(inst.outcome.text), force_bytes("removal of the retropharyngeal abscess"))
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-03-22T10:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.end.as_json(), "2013-03-22T10:30:10+01:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-03-22T09:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.start.as_json(), "2013-03-22T09:30:10+01:00")
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].code), force_bytes("01.000"))
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].display), force_bytes("Arts"))
        self.assertEqual(force_bytes(inst.performer[0].role.coding[0].system), force_bytes("urn:oid:2.16.840.1.113883.2.4.15.111"))
        self.assertEqual(force_bytes(inst.performer[0].role.text), force_bytes("Care role"))
        self.assertEqual(force_bytes(inst.reasonCode[0].text), force_bytes("ensure breathing during surgery"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

