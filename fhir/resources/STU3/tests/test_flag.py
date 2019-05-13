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
from .. import flag
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class FlagTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Flag", js["resourceType"])
        return flag.Flag(js)
    
    def testFlag1(self):
        inst = self.instantiate_from("flag-example-encounter.json")
        self.assertIsNotNone(inst, "Must have instantiated a Flag instance")
        self.implFlag1(inst)
        
        js = inst.as_json()
        self.assertEqual("Flag", js["resourceType"])
        inst2 = flag.Flag(js)
        self.implFlag1(inst2)
    
    def implFlag1(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("infection"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Infection Control Level"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://example.org/local"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("l3"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Follow Level 3 Protocol"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://example.org/local/if1"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-encounter"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Follow Infection Control Level 3 Protocol</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testFlag2(self):
        inst = self.instantiate_from("flag-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Flag instance")
        self.implFlag2(inst)
        
        js = inst.as_json()
        self.assertEqual("Flag", js["resourceType"])
        inst2 = flag.Flag(js)
        self.implFlag2(inst2)
    
    def implFlag2(self, inst):
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("admin"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Admin"))
        self.assertEqual(force_bytes(inst.category.coding[0].system), force_bytes("http://example.org/local"))
        self.assertEqual(force_bytes(inst.category.text), force_bytes("admin"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("bigdog"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Big dog"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://example.org/local"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Patient has a big dog at his home. Always always wear a suit of armor or take other active counter-measures"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(inst.period.end.date, FHIRDate("2016-12-01").date)
        self.assertEqual(inst.period.end.as_json(), "2016-12-01")
        self.assertEqual(inst.period.start.date, FHIRDate("2015-01-17").date)
        self.assertEqual(inst.period.start.as_json(), "2015-01-17")
        self.assertEqual(force_bytes(inst.status), force_bytes("inactive"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Large Dog warning for Peter Patient</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

