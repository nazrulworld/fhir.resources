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
from .. import operationoutcome
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class OperationOutcomeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("OperationOutcome", js["resourceType"])
        return operationoutcome.OperationOutcome(js)
    
    def testOperationOutcome1(self):
        inst = self.instantiate_from("operationoutcome-example-allok.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome1(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome1(inst2)
    
    def implOperationOutcome1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("allok"))
        self.assertEqual(force_bytes(inst.issue[0].code), force_bytes("informational"))
        self.assertEqual(force_bytes(inst.issue[0].details.text), force_bytes("All OK"))
        self.assertEqual(force_bytes(inst.issue[0].severity), force_bytes("information"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOperationOutcome2(self):
        inst = self.instantiate_from("operationoutcome-example-searchfail.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome2(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome2(inst2)
    
    def implOperationOutcome2(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("searchfail"))
        self.assertEqual(force_bytes(inst.issue[0].code), force_bytes("code-invalid"))
        self.assertEqual(force_bytes(inst.issue[0].details.text), force_bytes("The \"name\" parameter has the modifier \"exact\" which is not supported by this server"))
        self.assertEqual(force_bytes(inst.issue[0].location[0]), force_bytes("http.name:exact"))
        self.assertEqual(force_bytes(inst.issue[0].severity), force_bytes("fatal"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOperationOutcome3(self):
        inst = self.instantiate_from("operationoutcome-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome3(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome3(inst2)
    
    def implOperationOutcome3(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("101"))
        self.assertEqual(force_bytes(inst.issue[0].code), force_bytes("code-invalid"))
        self.assertEqual(force_bytes(inst.issue[0].details.text), force_bytes("The code \"W\" is not known and not legal in this context"))
        self.assertEqual(force_bytes(inst.issue[0].diagnostics), force_bytes("Acme.Interop.FHIRProcessors.Patient.processGender line 2453"))
        self.assertEqual(force_bytes(inst.issue[0].expression[0]), force_bytes("Patient.gender"))
        self.assertEqual(force_bytes(inst.issue[0].location[0]), force_bytes("/f:Patient/f:gender"))
        self.assertEqual(force_bytes(inst.issue[0].severity), force_bytes("error"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOperationOutcome4(self):
        inst = self.instantiate_from("operationoutcome-example-exception.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome4(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome4(inst2)
    
    def implOperationOutcome4(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("exception"))
        self.assertEqual(force_bytes(inst.issue[0].code), force_bytes("exception"))
        self.assertEqual(force_bytes(inst.issue[0].details.text), force_bytes("SQL Link Communication Error (dbx = 34234)"))
        self.assertEqual(force_bytes(inst.issue[0].severity), force_bytes("error"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOperationOutcome5(self):
        inst = self.instantiate_from("operationoutcome-example-break-the-glass.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome5(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome5(inst2)
    
    def implOperationOutcome5(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("break-the-glass"))
        self.assertEqual(force_bytes(inst.issue[0].code), force_bytes("suppressed"))
        self.assertEqual(force_bytes(inst.issue[0].details.coding[0].code), force_bytes("ETREAT"))
        self.assertEqual(force_bytes(inst.issue[0].details.coding[0].display), force_bytes("Emergency Treatment"))
        self.assertEqual(force_bytes(inst.issue[0].details.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.issue[0].details.text), force_bytes("Additional information may be available using the Break-The-Glass Protocol"))
        self.assertEqual(force_bytes(inst.issue[0].severity), force_bytes("information"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOperationOutcome6(self):
        inst = self.instantiate_from("operationoutcome-example-validationfail.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome6(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome6(inst2)
    
    def implOperationOutcome6(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("validationfail"))
        self.assertEqual(force_bytes(inst.issue[0].code), force_bytes("structure"))
        self.assertEqual(force_bytes(inst.issue[0].details.text), force_bytes("Error parsing resource XML (Unknown Content \"label\""))
        self.assertEqual(force_bytes(inst.issue[0].expression[0]), force_bytes("Patient.identifier"))
        self.assertEqual(force_bytes(inst.issue[0].location[0]), force_bytes("/f:Patient/f:identifier"))
        self.assertEqual(force_bytes(inst.issue[0].severity), force_bytes("error"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

