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
from .. import basic
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class BasicTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Basic", js["resourceType"])
        return basic.Basic(js)
    
    def testBasic1(self):
        inst = self.instantiate_from("basic-example2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Basic instance")
        self.implBasic1(inst)
        
        js = inst.as_json()
        self.assertEqual("Basic", js["resourceType"])
        inst2 = basic.Basic(js)
        self.implBasic1(inst2)
    
    def implBasic1(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("UMLCLASSMODEL"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://example.org/do-not-use/fhir-codes#resourceTypes"))
        self.assertEqual(force_bytes(inst.extension[0].extension[0].url), force_bytes("name"))
        self.assertEqual(force_bytes(inst.extension[0].extension[0].valueString), force_bytes("Class1"))
        self.assertEqual(force_bytes(inst.extension[0].extension[1].extension[0].url), force_bytes("name"))
        self.assertEqual(force_bytes(inst.extension[0].extension[1].extension[0].valueString), force_bytes("attribute1"))
        self.assertEqual(force_bytes(inst.extension[0].extension[1].extension[1].url), force_bytes("minOccurs"))
        self.assertEqual(inst.extension[0].extension[1].extension[1].valueInteger, 1)
        self.assertEqual(force_bytes(inst.extension[0].extension[1].extension[2].url), force_bytes("maxOccurs"))
        self.assertEqual(force_bytes(inst.extension[0].extension[1].extension[2].valueCode), force_bytes("*"))
        self.assertEqual(force_bytes(inst.extension[0].extension[1].url), force_bytes("attribute"))
        self.assertEqual(force_bytes(inst.extension[0].extension[2].extension[0].url), force_bytes("name"))
        self.assertEqual(force_bytes(inst.extension[0].extension[2].extension[0].valueString), force_bytes("attribute2"))
        self.assertEqual(force_bytes(inst.extension[0].extension[2].extension[1].url), force_bytes("minOccurs"))
        self.assertEqual(inst.extension[0].extension[2].extension[1].valueInteger, 0)
        self.assertEqual(force_bytes(inst.extension[0].extension[2].extension[2].url), force_bytes("maxOccurs"))
        self.assertEqual(inst.extension[0].extension[2].extension[2].valueInteger, 1)
        self.assertEqual(force_bytes(inst.extension[0].extension[2].url), force_bytes("attribute"))
        self.assertEqual(force_bytes(inst.extension[0].url), force_bytes("http://example.org/do-not-use/fhir-extensions/UMLclass"))
        self.assertEqual(force_bytes(inst.id), force_bytes("classModel"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testBasic2(self):
        inst = self.instantiate_from("basic-example-narrative.json")
        self.assertIsNotNone(inst, "Must have instantiated a Basic instance")
        self.implBasic2(inst)
        
        js = inst.as_json()
        self.assertEqual("Basic", js["resourceType"])
        inst2 = basic.Basic(js)
        self.implBasic2(inst2)
    
    def implBasic2(self, inst):
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Example Narrative Tester"))
        self.assertEqual(force_bytes(inst.id), force_bytes("basic-example-narrative"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
    
    def testBasic3(self):
        inst = self.instantiate_from("basic-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Basic instance")
        self.implBasic3(inst)
        
        js = inst.as_json()
        self.assertEqual("Basic", js["resourceType"])
        inst2 = basic.Basic(js)
        self.implBasic3(inst2)
    
    def implBasic3(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("referral"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://hl7.org/fhir/basic-resource-type"))
        self.assertEqual(inst.created.date, FHIRDate("2013-05-14").date)
        self.assertEqual(inst.created.as_json(), "2013-05-14")
        self.assertEqual(force_bytes(inst.extension[0].url), force_bytes("http://example.org/do-not-use/fhir-extensions/referral#requestingPractitioner"))
        self.assertEqual(force_bytes(inst.extension[1].url), force_bytes("http://example.org/do-not-use/fhir-extensions/referral#notes"))
        self.assertEqual(force_bytes(inst.extension[1].valueString), force_bytes("The patient had fever peaks over the last couple of days. He is worried about these peaks."))
        self.assertEqual(force_bytes(inst.extension[2].url), force_bytes("http://example.org/do-not-use/fhir-extensions/referral#fulfillingEncounter"))
        self.assertEqual(force_bytes(inst.id), force_bytes("referral"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://goodhealth.org/basic/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("19283746"))
        self.assertEqual(force_bytes(inst.modifierExtension[0].url), force_bytes("http://example.org/do-not-use/fhir-extensions/referral#referredForService"))
        self.assertEqual(force_bytes(inst.modifierExtension[0].valueCodeableConcept.coding[0].code), force_bytes("11429006"))
        self.assertEqual(force_bytes(inst.modifierExtension[0].valueCodeableConcept.coding[0].display), force_bytes("Consultation"))
        self.assertEqual(force_bytes(inst.modifierExtension[0].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.modifierExtension[1].url), force_bytes("http://example.org/do-not-use/fhir-extensions/referral#targetDate"))
        self.assertEqual(inst.modifierExtension[1].valuePeriod.end.date, FHIRDate("2013-04-15").date)
        self.assertEqual(inst.modifierExtension[1].valuePeriod.end.as_json(), "2013-04-15")
        self.assertEqual(inst.modifierExtension[1].valuePeriod.start.date, FHIRDate("2013-04-01").date)
        self.assertEqual(inst.modifierExtension[1].valuePeriod.start.as_json(), "2013-04-01")
        self.assertEqual(force_bytes(inst.modifierExtension[2].url), force_bytes("http://example.org/do-not-use/fhir-extensions/referral#status"))
        self.assertEqual(force_bytes(inst.modifierExtension[2].valueCode), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

