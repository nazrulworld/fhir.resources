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
from .. import catalogentry
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class CatalogEntryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CatalogEntry", js["resourceType"])
        return catalogentry.CatalogEntry(js)
    
    def testCatalogEntry1(self):
        inst = self.instantiate_from("catalogentry-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CatalogEntry instance")
        self.implCatalogEntry1(inst)
        
        js = inst.as_json()
        self.assertEqual("CatalogEntry", js["resourceType"])
        inst2 = catalogentry.CatalogEntry(js)
        self.implCatalogEntry1(inst2)
    
    def implCatalogEntry1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.com/identifier"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertTrue(inst.orderable)
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.text), force_bytes("Medication"))

