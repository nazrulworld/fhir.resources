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
from .. import person
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class PersonTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Person", js["resourceType"])
        return person.Person(js)
    
    def testPerson1(self):
        inst = self.instantiate_from("person-example-f002-ariadne.json")
        self.assertIsNotNone(inst, "Must have instantiated a Person instance")
        self.implPerson1(inst)
        
        js = inst.as_json()
        self.assertEqual("Person", js["resourceType"])
        inst2 = person.Person(js)
        self.implPerson1(inst2)
    
    def implPerson1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.birthDate.date, FHIRDate("1963").date)
        self.assertEqual(inst.birthDate.as_json(), "1963")
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f002"))
        self.assertEqual(force_bytes(inst.name[0].text), force_bytes("Ariadne Bor-Jansma"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.photo.contentType), force_bytes("image/jpeg"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("home"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("+31201234567"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testPerson2(self):
        inst = self.instantiate_from("person-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Person instance")
        self.implPerson2(inst)
        
        js = inst.as_json()
        self.assertEqual("Person", js["resourceType"])
        inst2 = person.Person(js)
        self.implPerson2(inst2)
    
    def implPerson2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("PleasantVille"))
        self.assertEqual(force_bytes(inst.address[0].line[0]), force_bytes("534 Erewhon St"))
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("3999"))
        self.assertEqual(force_bytes(inst.address[0].state), force_bytes("Vic"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("home"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1974-12-25").date)
        self.assertEqual(inst.birthDate.as_json(), "1974-12-25")
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(inst.identifier[0].period.start.date, FHIRDate("2001-05-06").date)
        self.assertEqual(inst.identifier[0].period.start.as_json(), "2001-05-06")
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:oid:1.2.36.146.595.217.0.1"))
        self.assertEqual(force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("MR"))
        self.assertEqual(force_bytes(inst.identifier[0].type.coding[0].system), force_bytes("http://hl7.org/fhir/v2/0203"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Chalmers"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Peter"))
        self.assertEqual(force_bytes(inst.name[0].given[1]), force_bytes("James"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.name[1].given[0]), force_bytes("Jim"))
        self.assertEqual(force_bytes(inst.name[1].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("home"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[1].value), force_bytes("(03) 5555 6473"))
        self.assertEqual(force_bytes(inst.telecom[2].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[2].use), force_bytes("home"))
        self.assertEqual(force_bytes(inst.telecom[2].value), force_bytes("Jim@example.org"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

