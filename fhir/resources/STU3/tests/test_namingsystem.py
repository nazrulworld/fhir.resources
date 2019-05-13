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
from .. import namingsystem
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class NamingSystemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("NamingSystem", js["resourceType"])
        return namingsystem.NamingSystem(js)
    
    def testNamingSystem1(self):
        inst = self.instantiate_from("namingsystem-example-replaced.json")
        self.assertIsNotNone(inst, "Must have instantiated a NamingSystem instance")
        self.implNamingSystem1(inst)
        
        js = inst.as_json()
        self.assertEqual("NamingSystem", js["resourceType"])
        inst2 = namingsystem.NamingSystem(js)
        self.implNamingSystem1(inst2)
    
    def implNamingSystem1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2005-01-25").date)
        self.assertEqual(inst.date.as_json(), "2005-01-25")
        self.assertEqual(force_bytes(inst.description), force_bytes("This was a wrong registration for the spanish editions of SNOMED CT. Do not use"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-replaced"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("codesystem"))
        self.assertEqual(force_bytes(inst.name), force_bytes("SNOMED CT Spanish"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Not HL7!"))
        self.assertEqual(force_bytes(inst.status), force_bytes("retired"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.uniqueId[0].type), force_bytes("oid"))
        self.assertEqual(force_bytes(inst.uniqueId[0].value), force_bytes("2.16.840.1.113883.6.96.1"))
    
    def testNamingSystem2(self):
        inst = self.instantiate_from("namingsystem-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a NamingSystem instance")
        self.implNamingSystem2(inst)
        
        js = inst.as_json()
        self.assertEqual("NamingSystem", js["resourceType"])
        inst2 = namingsystem.NamingSystem(js)
        self.implNamingSystem2(inst2)
    
    def implNamingSystem2(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("FHIR project team"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(inst.date.date, FHIRDate("2014-12-13").date)
        self.assertEqual(inst.date.as_json(), "2014-12-13")
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("codesystem"))
        self.assertEqual(force_bytes(inst.name), force_bytes("SNOMED CT"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 International on behalf of IHTSDO"))
        self.assertEqual(force_bytes(inst.responsible), force_bytes("IHTSDO & affiliates"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.uniqueId[0].type), force_bytes("oid"))
        self.assertEqual(force_bytes(inst.uniqueId[0].value), force_bytes("2.16.840.1.113883.6.96"))
        self.assertTrue(inst.uniqueId[1].preferred)
        self.assertEqual(force_bytes(inst.uniqueId[1].type), force_bytes("uri"))
        self.assertEqual(force_bytes(inst.uniqueId[1].value), force_bytes("http://snomed.info/sct"))
    
    def testNamingSystem3(self):
        inst = self.instantiate_from("namingsystem-example-id.json")
        self.assertIsNotNone(inst, "Must have instantiated a NamingSystem instance")
        self.implNamingSystem3(inst)
        
        js = inst.as_json()
        self.assertEqual("NamingSystem", js["resourceType"])
        inst2 = namingsystem.NamingSystem(js)
        self.implNamingSystem3(inst2)
    
    def implNamingSystem3(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("HL7 Australia FHIR Team"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7-australia.wikispaces.com/FHIR+Australia"))
        self.assertEqual(inst.date.date, FHIRDate("2015-08-31").date)
        self.assertEqual(inst.date.as_json(), "2015-08-31")
        self.assertEqual(force_bytes(inst.description), force_bytes("Australian HI Identifier as established by relevant regulations etc"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-id"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("AU"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("identifier"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Austalian Healthcare Identifier - Individual"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 Australia on behalf of NEHTA"))
        self.assertEqual(force_bytes(inst.responsible), force_bytes("HI Service Operator / NEHTA"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("NI"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("National unique individual identifier"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://hl7.org/fhir/v2/0203"))
        self.assertEqual(force_bytes(inst.type.text), force_bytes("IHI"))
        self.assertEqual(force_bytes(inst.uniqueId[0].comment), force_bytes("This value is used in Australian CDA documents"))
        self.assertEqual(force_bytes(inst.uniqueId[0].type), force_bytes("oid"))
        self.assertEqual(force_bytes(inst.uniqueId[0].value), force_bytes("1.2.36.1.2001.1003.0"))
        self.assertEqual(inst.uniqueId[1].period.start.date, FHIRDate("2015-08-21").date)
        self.assertEqual(inst.uniqueId[1].period.start.as_json(), "2015-08-21")
        self.assertTrue(inst.uniqueId[1].preferred)
        self.assertEqual(force_bytes(inst.uniqueId[1].type), force_bytes("uri"))
        self.assertEqual(force_bytes(inst.uniqueId[1].value), force_bytes("http://ns.electronichealth.net.au/id/hi/ihi/1.0"))
        self.assertEqual(force_bytes(inst.usage), force_bytes("Used in Australia for identifying patients"))

