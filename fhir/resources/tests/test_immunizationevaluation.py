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
from .. import immunizationevaluation
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ImmunizationEvaluationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImmunizationEvaluation", js["resourceType"])
        return immunizationevaluation.ImmunizationEvaluation(js)
    
    def testImmunizationEvaluation1(self):
        inst = self.instantiate_from("immunizationevaluation-example-notvalid.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImmunizationEvaluation instance")
        self.implImmunizationEvaluation1(inst)
        
        js = inst.as_json()
        self.assertEqual("ImmunizationEvaluation", js["resourceType"])
        inst2 = immunizationevaluation.ImmunizationEvaluation(js)
        self.implImmunizationEvaluation1(inst2)
    
    def implImmunizationEvaluation1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.date.as_json(), "2013-01-10")
        self.assertEqual(inst.doseNumberPositiveInt, 2)
        self.assertEqual(force_bytes(inst.doseStatus.coding[0].code), force_bytes("notvalid"))
        self.assertEqual(force_bytes(inst.doseStatus.coding[0].display), force_bytes("Not Valid"))
        self.assertEqual(force_bytes(inst.doseStatus.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status"))
        self.assertEqual(force_bytes(inst.doseStatusReason[0].coding[0].code), force_bytes("outsidesched"))
        self.assertEqual(force_bytes(inst.doseStatusReason[0].coding[0].display), force_bytes("Administered outside recommended schedule"))
        self.assertEqual(force_bytes(inst.doseStatusReason[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status-reason"))
        self.assertEqual(force_bytes(inst.id), force_bytes("notValid"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.series), force_bytes("Vaccination Series 1"))
        self.assertEqual(inst.seriesDosesPositiveInt, 3)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.targetDisease.coding[0].code), force_bytes("1857005"))
        self.assertEqual(force_bytes(inst.targetDisease.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testImmunizationEvaluation2(self):
        inst = self.instantiate_from("immunizationevaluation-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImmunizationEvaluation instance")
        self.implImmunizationEvaluation2(inst)
        
        js = inst.as_json()
        self.assertEqual("ImmunizationEvaluation", js["resourceType"])
        inst2 = immunizationevaluation.ImmunizationEvaluation(js)
        self.implImmunizationEvaluation2(inst2)
    
    def implImmunizationEvaluation2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.date.as_json(), "2013-01-10")
        self.assertEqual(inst.doseNumberPositiveInt, 1)
        self.assertEqual(force_bytes(inst.doseStatus.coding[0].code), force_bytes("valid"))
        self.assertEqual(force_bytes(inst.doseStatus.coding[0].display), force_bytes("Valid"))
        self.assertEqual(force_bytes(inst.doseStatus.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.series), force_bytes("Vaccination Series 1"))
        self.assertEqual(inst.seriesDosesPositiveInt, 3)
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.targetDisease.coding[0].code), force_bytes("1857005"))
        self.assertEqual(force_bytes(inst.targetDisease.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

