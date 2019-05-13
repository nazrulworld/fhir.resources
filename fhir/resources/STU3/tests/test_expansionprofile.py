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
from .. import expansionprofile
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ExpansionProfileTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ExpansionProfile", js["resourceType"])
        return expansionprofile.ExpansionProfile(js)
    
    def testExpansionProfile1(self):
        inst = self.instantiate_from("expansionprofile-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ExpansionProfile instance")
        self.implExpansionProfile1(inst)
        
        js = inst.as_json()
        self.assertEqual("ExpansionProfile", js["resourceType"])
        inst2 = expansionprofile.ExpansionProfile(js)
        self.implExpansionProfile1(inst2)
    
    def implExpansionProfile1(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("FHIR project team"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(inst.date.date, FHIRDate("2016-12-23").date)
        self.assertEqual(inst.date.as_json(), "2016-12-23")
        self.assertEqual(force_bytes(inst.description), force_bytes("exanple ExpansionProfile for publication"))
        self.assertTrue(inst.excludeNested)
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier.system), force_bytes("http://example.org/profiles"))
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("example"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("001"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].display), force_bytes("World"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("http://unstats.un.org/unsd/methods/m49/m49.htm"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Example Expansion Profile"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 International"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">[ Provide Rendering ]</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/ExpansionProfile/example"))
        self.assertEqual(force_bytes(inst.version), force_bytes("0.1"))

