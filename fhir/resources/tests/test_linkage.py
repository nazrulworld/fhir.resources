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
from .. import linkage
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class LinkageTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Linkage", js["resourceType"])
        return linkage.Linkage(js)
    
    def testLinkage1(self):
        inst = self.instantiate_from("linkage-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Linkage instance")
        self.implLinkage1(inst)
        
        js = inst.as_json()
        self.assertEqual("Linkage", js["resourceType"])
        inst2 = linkage.Linkage(js)
        self.implLinkage1(inst2)
    
    def implLinkage1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("source"))
        self.assertEqual(force_bytes(inst.item[1].type), force_bytes("alternate"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

