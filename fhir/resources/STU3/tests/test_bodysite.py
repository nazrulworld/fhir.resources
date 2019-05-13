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
from .. import bodysite
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class BodySiteTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("BodySite", js["resourceType"])
        return bodysite.BodySite(js)
    
    def testBodySite1(self):
        inst = self.instantiate_from("bodysite-example-skin-patch.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodySite instance")
        self.implBodySite1(inst)
        
        js = inst.as_json()
        self.assertEqual("BodySite", js["resourceType"])
        inst2 = bodysite.BodySite(js)
        self.implBodySite1(inst2)
    
    def implBodySite1(self, inst):
        self.assertFalse(inst.active)
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("39937001"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Skin structure (body structure)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Skin patch"))
        self.assertEqual(force_bytes(inst.description), force_bytes("inner surface (volar) of the left forearm"))
        self.assertEqual(force_bytes(inst.id), force_bytes("skin-patch"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://goodhealth.org/bodysite/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testBodySite2(self):
        inst = self.instantiate_from("bodysite-example-tumor.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodySite instance")
        self.implBodySite2(inst)
        
        js = inst.as_json()
        self.assertEqual("BodySite", js["resourceType"])
        inst2 = bodysite.BodySite(js)
        self.implBodySite2(inst2)
    
    def implBodySite2(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("4147007"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Mass (morphologic abnormality)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Splenic mass"))
        self.assertEqual(force_bytes(inst.description), force_bytes("7 cm maximum diameter"))
        self.assertEqual(force_bytes(inst.id), force_bytes("tumor"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://goodhealth.org/bodysite/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.image[0].contentType), force_bytes("application/dicom"))
        self.assertEqual(force_bytes(inst.image[0].url), force_bytes("http://imaging.acme.com/wado/server?requestType=WADO&amp;wado_details"))
        self.assertEqual(force_bytes(inst.qualifier[0].coding[0].code), force_bytes("78961009"))
        self.assertEqual(force_bytes(inst.qualifier[0].coding[0].display), force_bytes("Splenic structure (body structure)"))
        self.assertEqual(force_bytes(inst.qualifier[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.qualifier[0].text), force_bytes("Splenic mass"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testBodySite3(self):
        inst = self.instantiate_from("bodysite-example-fetus.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodySite instance")
        self.implBodySite3(inst)
        
        js = inst.as_json()
        self.assertEqual("BodySite", js["resourceType"])
        inst2 = bodysite.BodySite(js)
        self.implBodySite3(inst2)
    
    def implBodySite3(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("83418008"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Entire fetus (body structure)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Fetus"))
        self.assertEqual(force_bytes(inst.description), force_bytes("EDD 1/1/2017 confirmation by LMP"))
        self.assertEqual(force_bytes(inst.id), force_bytes("fetus"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://goodhealth.org/bodysite/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

