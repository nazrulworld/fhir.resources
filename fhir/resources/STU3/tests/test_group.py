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
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
        self.assertEqual(force_bytes(inst.type), force_bytes("person"))

