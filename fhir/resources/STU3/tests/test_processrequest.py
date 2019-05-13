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
from .. import processrequest
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ProcessRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ProcessRequest", js["resourceType"])
        return processrequest.ProcessRequest(js)
    
    def testProcessRequest1(self):
        inst = self.instantiate_from("processrequest-example-reverse.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest1(inst2)
    
    def implProcessRequest1(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("cancel"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("87654"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/processrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("76543"))
        self.assertFalse(inst.nullify)
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Reversal ProcessRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcessRequest2(self):
        inst = self.instantiate_from("processrequest-example-poll-inclusive.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest2(inst2)
    
    def implProcessRequest2(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("poll"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("1112"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/processrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("112"))
        self.assertEqual(force_bytes(inst.include[0]), force_bytes("PaymentReconciliation"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcessRequest3(self):
        inst = self.instantiate_from("processrequest-example-poll-eob.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest3(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest3(inst2)
    
    def implProcessRequest3(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("poll"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("1115"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.phr.com/patient/12345/processrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("115"))
        self.assertEqual(force_bytes(inst.include[0]), force_bytes("ExplanationOfBenefit"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcessRequest4(self):
        inst = self.instantiate_from("processrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest4(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest4(inst2)
    
    def implProcessRequest4(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("poll"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("1110"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/processrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("110"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcessRequest5(self):
        inst = self.instantiate_from("processrequest-example-poll-exclusive.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest5(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest5(inst2)
    
    def implProcessRequest5(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("poll"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.exclude[0]), force_bytes("Communication"))
        self.assertEqual(force_bytes(inst.exclude[1]), force_bytes("PaymentReconciliation"))
        self.assertEqual(force_bytes(inst.id), force_bytes("1113"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/processrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("113"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcessRequest6(self):
        inst = self.instantiate_from("processrequest-example-reprocess.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest6(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest6(inst2)
    
    def implProcessRequest6(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("reprocess"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("44654"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/processrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("44543"))
        self.assertEqual(inst.item[0].sequenceLinkId, 1)
        self.assertEqual(force_bytes(inst.reference), force_bytes("ABC12345G"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ReProcess ProcessRequest resource.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcessRequest7(self):
        inst = self.instantiate_from("processrequest-example-poll-specific.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest7(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest7(inst2)
    
    def implProcessRequest7(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("poll"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("1111"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/processrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("111"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcessRequest8(self):
        inst = self.instantiate_from("processrequest-example-poll-payrec.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest8(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest8(inst2)
    
    def implProcessRequest8(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("poll"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("1114"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/processrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("114"))
        self.assertEqual(force_bytes(inst.include[0]), force_bytes("PaymentReconciliation"))
        self.assertEqual(inst.period.end.date, FHIRDate("2014-08-20").date)
        self.assertEqual(inst.period.end.as_json(), "2014-08-20")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-08-10").date)
        self.assertEqual(inst.period.start.as_json(), "2014-08-10")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcessRequest9(self):
        inst = self.instantiate_from("processrequest-example-status.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest9(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest9(inst2)
    
    def implProcessRequest9(self, inst):
        self.assertEqual(force_bytes(inst.action), force_bytes("status"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("87655"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/processrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("1776543"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Status ProcessRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

