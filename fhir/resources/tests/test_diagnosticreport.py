#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-13.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import diagnosticreport
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class DiagnosticReportTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DiagnosticReport", js["resourceType"])
        return diagnosticreport.DiagnosticReport(js)
    
    def testDiagnosticReport1(self):
        inst = self.instantiate_from("diagnosticreport-example-pgx.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport1(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport1(inst2)
    
    def implDiagnosticReport1(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("PGxReport"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Pharmacogenetics Report"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("https://system/PGxReport"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Pharmacogenetics Report"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2016-10-15T12:34:56+11:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2016-10-15T12:34:56+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("example-pgx"))
        self.assertEqual(inst.issued.date, FHIRDate("2016-10-20T14:00:05+11:00").date)
        self.assertEqual(inst.issued.as_json(), "2016-10-20T14:00:05+11:00")
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.presentedForm[0].contentType), force_bytes("application/pdf"))
        self.assertEqual(inst.presentedForm[0].creation.date, FHIRDate("2016-10-20T20:00:00+11:00").date)
        self.assertEqual(inst.presentedForm[0].creation.as_json(), "2016-10-20T20:00:00+11:00")
        self.assertEqual(force_bytes(inst.presentedForm[0].data), force_bytes("cGRmSW5CYXNlNjRCaW5hcnk="))
        self.assertEqual(force_bytes(inst.presentedForm[0].hash), force_bytes("571ef9c5655840f324e679072ed62b1b95eef8a0"))
        self.assertEqual(force_bytes(inst.presentedForm[0].language), force_bytes("en"))
        self.assertEqual(force_bytes(inst.presentedForm[0].title), force_bytes("Pharmacogenetics Report"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testDiagnosticReport2(self):
        inst = self.instantiate_from("diagnosticreport-example-dxa.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport2(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport2(inst2)
    
    def implDiagnosticReport2(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("38269-7"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("DXA BONE DENSITOMETRY"))
        self.assertEqual(force_bytes(inst.conclusionCode[0].coding[0].code), force_bytes("391040000"))
        self.assertEqual(force_bytes(inst.conclusionCode[0].coding[0].display), force_bytes("At risk of osteoporotic fracture"))
        self.assertEqual(force_bytes(inst.conclusionCode[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2008-06-17").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2008-06-17")
        self.assertEqual(force_bytes(inst.id), force_bytes("102"))
        self.assertEqual(inst.issued.date, FHIRDate("2008-06-18T09:23:00+10:00").date)
        self.assertEqual(inst.issued.as_json(), "2008-06-18T09:23:00+10:00")
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testDiagnosticReport3(self):
        inst = self.instantiate_from("diagnosticreport-example-papsmear.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport3(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport3(inst2)
    
    def implDiagnosticReport3(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("47527-7"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2013-02-11T10:33:33+11:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2013-02-11T10:33:33+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("pap"))
        self.assertEqual(inst.issued.date, FHIRDate("2013-02-13T11:45:33+11:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-02-13T11:45:33+11:00")
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
    
    def testDiagnosticReport4(self):
        inst = self.instantiate_from("diagnosticreport-example-gingival-mass.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport4(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport4(inst2)
    
    def implDiagnosticReport4(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("PAT"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Pathology (gross & histopath, not surgical)"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0074"))
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Pathology"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("4503"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Biopsy without Microscopic Description (1 Site/Lesion)-Standard"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("https://www.acmeonline.com"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Biopsy without Microscopic Description (1 Site/Lesion)-Standard"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2017-03-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2017-03-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("gingival-mass"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("https://www.acmeonline.com"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("P73456090"))
        self.assertEqual(inst.issued.date, FHIRDate("2017-03-15T08:13:08Z").date)
        self.assertEqual(inst.issued.as_json(), "2017-03-15T08:13:08Z")
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.presentedForm[0].contentType), force_bytes("application/pdf"))
        self.assertEqual(force_bytes(inst.presentedForm[0].language), force_bytes("en"))
        self.assertEqual(force_bytes(inst.presentedForm[0].title), force_bytes("LAB ID: P73456090 MAX JONES Biopsy without Microscopic Description (1 Site/Lesion)-Standard"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testDiagnosticReport5(self):
        inst = self.instantiate_from("diagnosticreport-example-ultrasound.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport5(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport5(inst2)
    
    def implDiagnosticReport5(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("394914008"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Radiology"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.category[0].coding[1].code), force_bytes("RAD"))
        self.assertEqual(force_bytes(inst.category[0].coding[1].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0074"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("45036003"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Ultrasonography of abdomen"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Abdominal Ultrasound"))
        self.assertEqual(force_bytes(inst.conclusion), force_bytes("Unremarkable study"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("ultrasound"))
        self.assertEqual(inst.issued.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(force_bytes(inst.media[0].comment), force_bytes("A comment about the image"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testDiagnosticReport6(self):
        inst = self.instantiate_from("diagnosticreport-example-f201-brainct.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport6(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport6(inst2)
    
    def implDiagnosticReport6(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("394914008"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Radiology"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.category[0].coding[1].code), force_bytes("RAD"))
        self.assertEqual(force_bytes(inst.category[0].coding[1].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0074"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("429858000"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Computed tomography (CT) of head and neck"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("CT of head-neck"))
        self.assertEqual(force_bytes(inst.conclusion), force_bytes("CT brains: large tumor sphenoid/clivus."))
        self.assertEqual(force_bytes(inst.conclusionCode[0].coding[0].code), force_bytes("188340000"))
        self.assertEqual(force_bytes(inst.conclusionCode[0].coding[0].display), force_bytes("Malignant tumor of craniopharyngeal duct"))
        self.assertEqual(force_bytes(inst.conclusionCode[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("f201"))
        self.assertEqual(inst.issued.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

