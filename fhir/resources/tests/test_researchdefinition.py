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
from .. import researchdefinition
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ResearchDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ResearchDefinition", js["resourceType"])
        return researchdefinition.ResearchDefinition(js)
    
    def testResearchDefinition1(self):
        inst = self.instantiate_from("researchdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ResearchDefinition instance")
        self.implResearchDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ResearchDefinition", js["resourceType"])
        inst2 = researchdefinition.ResearchDefinition(js)
        self.implResearchDefinition1(inst2)
    
    def implResearchDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

