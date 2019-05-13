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
from .. import processresponse
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ProcessResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ProcessResponse", js["resourceType"])
        return processresponse.ProcessResponse(js)
    
    def testProcessResponse1(self):
        inst = self.instantiate_from("processresponse-example-pended.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessResponse instance")
        self.implProcessResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessResponse", js["resourceType"])
        inst2 = processresponse.ProcessResponse(js)
        self.implProcessResponse1(inst2)
    
    def implProcessResponse1(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("comreq-1"))
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.disposition), force_bytes("Additional information required."))
        self.assertEqual(force_bytes(inst.id), force_bytes("SR2499"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.BenefitsInc.com/fhir/processresponse"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("881222"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].code), force_bytes("pended"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].system), force_bytes("http://hl7.org/fhir/processoutcomecodes"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A ProcessResponse indicating pended status with a request for additional information.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcessResponse2(self):
        inst = self.instantiate_from("processresponse-example-error.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessResponse instance")
        self.implProcessResponse2(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessResponse", js["resourceType"])
        inst2 = processresponse.ProcessResponse(js)
        self.implProcessResponse2(inst2)
    
    def implProcessResponse2(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-07-14").date)
        self.assertEqual(inst.created.as_json(), "2014-07-14")
        self.assertEqual(force_bytes(inst.disposition), force_bytes("Referred to claim not found on system."))
        self.assertEqual(force_bytes(inst.error[0].coding[0].code), force_bytes("a001"))
        self.assertEqual(force_bytes(inst.error[0].coding[0].system), force_bytes("http://hl7.org/fhir/adjudication-error"))
        self.assertEqual(force_bytes(inst.form.coding[0].code), force_bytes("PRRESP/2016/01"))
        self.assertEqual(force_bytes(inst.form.coding[0].system), force_bytes("http://ncforms.org/formid"))
        self.assertEqual(force_bytes(inst.id), force_bytes("SR2349"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.BenefitsInc.com/fhir/processresponse"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("ER987634"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].code), force_bytes("error"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].system), force_bytes("http://hl7.org/fhir/processoutcomecodes"))
        self.assertEqual(force_bytes(inst.processNote[0].text), force_bytes("Please check the submitted payor identification and local claim number."))
        self.assertEqual(force_bytes(inst.processNote[0].type.coding[0].code), force_bytes("print"))
        self.assertEqual(force_bytes(inst.processNote[0].type.coding[0].system), force_bytes("http://hl7.org/fhir/note-type"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ProcessResponse</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testProcessResponse3(self):
        inst = self.instantiate_from("processresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessResponse instance")
        self.implProcessResponse3(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessResponse", js["resourceType"])
        inst2 = processresponse.ProcessResponse(js)
        self.implProcessResponse3(inst2)
    
    def implProcessResponse3(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.disposition), force_bytes("Adjudication processing completed, ClaimResponse and EOB ready for retrieval."))
        self.assertEqual(force_bytes(inst.id), force_bytes("SR2500"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.BenefitsInc.com/fhir/processresponse"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("881234"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].code), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].system), force_bytes("http://hl7.org/fhir/processoutcomecodes"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ProcessResponse</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

