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
from .. import detectedissue
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class DetectedIssueTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DetectedIssue", js["resourceType"])
        return detectedissue.DetectedIssue(js)
    
    def testDetectedIssue1(self):
        inst = self.instantiate_from("detectedissue-example-allergy.json")
        self.assertIsNotNone(inst, "Must have instantiated a DetectedIssue instance")
        self.implDetectedIssue1(inst)
        
        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue1(inst2)
    
    def implDetectedIssue1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("allergy"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testDetectedIssue2(self):
        inst = self.instantiate_from("detectedissue-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DetectedIssue instance")
        self.implDetectedIssue2(inst)
        
        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue2(inst2)
    
    def implDetectedIssue2(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("DRG"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Drug Interaction Alert"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(inst.date.date, FHIRDate("2014-01-05").date)
        self.assertEqual(inst.date.as_json(), "2014-01-05")
        self.assertEqual(force_bytes(inst.id), force_bytes("ddi"))
        self.assertEqual(force_bytes(inst.mitigation[0].action.coding[0].code), force_bytes("13"))
        self.assertEqual(force_bytes(inst.mitigation[0].action.coding[0].display), force_bytes("Stopped Concurrent Therapy"))
        self.assertEqual(force_bytes(inst.mitigation[0].action.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(force_bytes(inst.mitigation[0].action.text), force_bytes("Asked patient to discontinue regular use of Tylenol and to consult with clinician if they need to resume to allow appropriate INR monitoring"))
        self.assertEqual(inst.mitigation[0].date.date, FHIRDate("2014-01-05").date)
        self.assertEqual(inst.mitigation[0].date.as_json(), "2014-01-05")
        self.assertEqual(force_bytes(inst.severity), force_bytes("high"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testDetectedIssue3(self):
        inst = self.instantiate_from("detectedissue-example-lab.json")
        self.assertIsNotNone(inst, "Must have instantiated a DetectedIssue instance")
        self.implDetectedIssue3(inst)
        
        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue3(inst2)
    
    def implDetectedIssue3(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("lab"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testDetectedIssue4(self):
        inst = self.instantiate_from("detectedissue-example-dup.json")
        self.assertIsNotNone(inst, "Must have instantiated a DetectedIssue instance")
        self.implDetectedIssue4(inst)
        
        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue4(inst2)
    
    def implDetectedIssue4(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("DUPTHPY"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Duplicate Therapy Alert"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://hl7.org/fhir/v3/ActCode"))
        self.assertEqual(inst.date.date, FHIRDate("2013-05-08").date)
        self.assertEqual(inst.date.as_json(), "2013-05-08")
        self.assertEqual(force_bytes(inst.detail), force_bytes("Similar test was performed within the past 14 days"))
        self.assertEqual(force_bytes(inst.id), force_bytes("duplicate"))
        self.assertEqual(force_bytes(inst.identifier.system), force_bytes("http://example.org"))
        self.assertEqual(force_bytes(inst.identifier.use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.reference), force_bytes("http://www.tmhp.com/RadiologyClinicalDecisionSupport/2011/CHEST%20IMAGING%20GUIDELINES%202011.pdf"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

