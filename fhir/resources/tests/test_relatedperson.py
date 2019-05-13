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
from .. import relatedperson
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class RelatedPersonTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("RelatedPerson", js["resourceType"])
        return relatedperson.RelatedPerson(js)
    
    def testRelatedPerson1(self):
        inst = self.instantiate_from("relatedperson-example-newborn-mom.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson1(inst)
        
        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson1(inst2)
    
    def implRelatedPerson1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].line[0]), force_bytes("2222 Home Street"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("home"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1973-05-31").date)
        self.assertEqual(inst.birthDate.as_json(), "1973-05-31")
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("newborn-mom"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://hl7.org/fhir/sid/us-ssn"))
        self.assertEqual(force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("SS"))
        self.assertEqual(force_bytes(inst.identifier[0].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("444222222"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Everywoman"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Eve"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[0].code), force_bytes("NMTH"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[0].display), force_bytes("natural mother"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-RoleCode"))
        self.assertEqual(force_bytes(inst.relationship[0].text), force_bytes("Natural Mother"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("555-555-2003"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testRelatedPerson2(self):
        inst = self.instantiate_from("relatedperson-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson2(inst)
        
        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson2(inst2)
    
    def implRelatedPerson2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Paris"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("FRA"))
        self.assertEqual(force_bytes(inst.address[0].line[0]), force_bytes("43, Place du Marché Sainte Catherine"))
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("75004"))
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("benedicte"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:oid:1.2.250.1.61"))
        self.assertEqual(force_bytes(inst.identifier[0].type.text), force_bytes("INSEE"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("272117510400399"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("du Marché"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Bénédicte"))
        self.assertEqual(force_bytes(inst.photo[0].contentType), force_bytes("image/jpeg"))
        self.assertEqual(force_bytes(inst.photo[0].url), force_bytes("Binary/f016"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[0].code), force_bytes("N"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0131"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[1].code), force_bytes("WIFE"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[1].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-RoleCode"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("+33 (237) 998327"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testRelatedPerson3(self):
        inst = self.instantiate_from("relatedperson-example-f001-sarah.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson3(inst)
        
        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson3(inst2)
    
    def implRelatedPerson3(self, inst):
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f001"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:oid:2.16.840.1.113883.2.4.6.3"))
        self.assertEqual(force_bytes(inst.identifier[0].type.text), force_bytes("BSN"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Abels"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Sarah"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[0].code), force_bytes("SIGOTHR"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-RoleCode"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("mobile"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("0690383372"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("home"))
        self.assertEqual(force_bytes(inst.telecom[1].value), force_bytes("s.abels@kpn.nl"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testRelatedPerson4(self):
        inst = self.instantiate_from("relatedperson-example-peter.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson4(inst)
        
        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson4(inst2)
    
    def implRelatedPerson4(self, inst):
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("PleasantVille"))
        self.assertEqual(force_bytes(inst.address[0].line[0]), force_bytes("534 Erewhon St"))
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("3999"))
        self.assertEqual(force_bytes(inst.address[0].state), force_bytes("Vic"))
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("home"))
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("peter"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Chalmers"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Peter"))
        self.assertEqual(force_bytes(inst.name[0].given[1]), force_bytes("James"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(inst.period.start.date, FHIRDate("2012-03-11").date)
        self.assertEqual(inst.period.start.as_json(), "2012-03-11")
        self.assertEqual(force_bytes(inst.photo[0].contentType), force_bytes("image/jpeg"))
        self.assertEqual(force_bytes(inst.photo[0].url), force_bytes("Binary/f012"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[0].code), force_bytes("C"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0131"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("(03) 5555 6473"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testRelatedPerson5(self):
        inst = self.instantiate_from("relatedperson-example-f002-ariadne.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson5(inst)
        
        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson5(inst2)
    
    def implRelatedPerson5(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("1963").date)
        self.assertEqual(inst.birthDate.as_json(), "1963")
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f002"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name[0].text), force_bytes("Ariadne Bor-Jansma"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("usual"))
        self.assertEqual(inst.period.start.date, FHIRDate("1975").date)
        self.assertEqual(inst.period.start.as_json(), "1975")
        self.assertEqual(force_bytes(inst.photo[0].contentType), force_bytes("image/jpeg"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[0].code), force_bytes("SIGOTHR"))
        self.assertEqual(force_bytes(inst.relationship[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-RoleCode"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("home"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("+31201234567"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

