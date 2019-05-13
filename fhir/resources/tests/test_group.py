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
from .. import group
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class GroupTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Group", js["resourceType"])
        return group.Group(js)
    
    def testGroup1(self):
        inst = self.instantiate_from("group-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Group instance")
        self.implGroup1(inst)
        
        js = inst.as_json()
        self.assertEqual("Group", js["resourceType"])
        inst2 = group.Group(js)
        self.implGroup1(inst2)
    
    def implGroup1(self, inst):
        self.assertTrue(inst.actual)
        self.assertEqual(force_bytes(inst.characteristic[0].code.text), force_bytes("gender"))
        self.assertFalse(inst.characteristic[0].exclude)
        self.assertEqual(force_bytes(inst.characteristic[0].valueCodeableConcept.text), force_bytes("mixed"))
        self.assertEqual(force_bytes(inst.characteristic[1].code.text), force_bytes("owner"))
        self.assertFalse(inst.characteristic[1].exclude)
        self.assertEqual(force_bytes(inst.characteristic[1].valueCodeableConcept.text), force_bytes("John Smith"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Horse"))
        self.assertEqual(force_bytes(inst.id), force_bytes("101"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://someveterinarianclinic.org/fhir/NamingSystem/herds"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("John's herd"))
        self.assertEqual(inst.quantity, 25)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
        self.assertEqual(force_bytes(inst.type), force_bytes("animal"))
    
    def testGroup2(self):
        inst = self.instantiate_from("group-example-member.json")
        self.assertIsNotNone(inst, "Must have instantiated a Group instance")
        self.implGroup2(inst)
        
        js = inst.as_json()
        self.assertEqual("Group", js["resourceType"])
        inst2 = group.Group(js)
        self.implGroup2(inst2)
    
    def implGroup2(self, inst):
        self.assertTrue(inst.actual)
        self.assertEqual(force_bytes(inst.id), force_bytes("102"))
        self.assertEqual(inst.member[0].period.start.date, FHIRDate("2014-10-08").date)
        self.assertEqual(inst.member[0].period.start.as_json(), "2014-10-08")
        self.assertTrue(inst.member[1].inactive)
        self.assertEqual(inst.member[1].period.start.date, FHIRDate("2015-04-02").date)
        self.assertEqual(inst.member[1].period.start.as_json(), "2015-04-02")
        self.assertEqual(inst.member[2].period.start.date, FHIRDate("2015-08-06").date)
        self.assertEqual(inst.member[2].period.start.as_json(), "2015-08-06")
        self.assertEqual(inst.member[3].period.start.date, FHIRDate("2015-08-06").date)
        self.assertEqual(inst.member[3].period.start.as_json(), "2015-08-06")
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
        self.assertEqual(force_bytes(inst.type), force_bytes("person"))
    
    def testGroup3(self):
        inst = self.instantiate_from("group-example-herd1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Group instance")
        self.implGroup3(inst)
        
        js = inst.as_json()
        self.assertEqual("Group", js["resourceType"])
        inst2 = group.Group(js)
        self.implGroup3(inst2)
    
    def implGroup3(self, inst):
        self.assertTrue(inst.active)
        self.assertTrue(inst.actual)
        self.assertEqual(force_bytes(inst.characteristic[0].code.text), force_bytes("gender"))
        self.assertFalse(inst.characteristic[0].exclude)
        self.assertEqual(force_bytes(inst.characteristic[0].valueCodeableConcept.text), force_bytes("female"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("388393002"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Genus Sus (organism)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.coding[1].code), force_bytes("POR"))
        self.assertEqual(force_bytes(inst.code.coding[1].display), force_bytes("porcine"))
        self.assertEqual(force_bytes(inst.code.coding[1].system), force_bytes("https://www.aphis.usda.gov"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Porcine"))
        self.assertEqual(force_bytes(inst.extension[0].url), force_bytes("http://example.org/fhir/StructureDefinition/owner"))
        self.assertEqual(force_bytes(inst.id), force_bytes("herd1"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("https://vetmed.iastate.edu/vdl"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("20171120-1234"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Breeding herd"))
        self.assertEqual(inst.quantity, 2500)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("animal"))
    
    def testGroup4(self):
        inst = self.instantiate_from("group-example-patientlist.json")
        self.assertIsNotNone(inst, "Must have instantiated a Group instance")
        self.implGroup4(inst)
        
        js = inst.as_json()
        self.assertEqual("Group", js["resourceType"])
        inst2 = group.Group(js)
        self.implGroup4(inst2)
    
    def implGroup4(self, inst):
        self.assertTrue(inst.actual)
        self.assertEqual(force_bytes(inst.characteristic[0].code.coding[0].code), force_bytes("attributed-to"))
        self.assertEqual(force_bytes(inst.characteristic[0].code.coding[0].system), force_bytes("http://example.org"))
        self.assertEqual(force_bytes(inst.characteristic[0].code.text), force_bytes("Patients primarily attributed to"))
        self.assertFalse(inst.characteristic[0].exclude)
        self.assertEqual(force_bytes(inst.id), force_bytes("example-patientlist"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
        self.assertEqual(force_bytes(inst.type), force_bytes("person"))

