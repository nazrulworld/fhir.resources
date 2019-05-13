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
from .. import bodystructure
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class BodyStructureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("BodyStructure", js["resourceType"])
        return bodystructure.BodyStructure(js)
    
    def testBodyStructure1(self):
        inst = self.instantiate_from("bodystructure-example-fetus.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodyStructure instance")
        self.implBodyStructure1(inst)
        
        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure1(inst2)
    
    def implBodyStructure1(self, inst):
        self.assertEqual(force_bytes(inst.description), force_bytes("EDD 1/1/2017 confirmation by LMP"))
        self.assertEqual(force_bytes(inst.id), force_bytes("fetus"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://goodhealth.org/bodystructure/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.location.coding[0].code), force_bytes("83418008"))
        self.assertEqual(force_bytes(inst.location.coding[0].display), force_bytes("Entire fetus (body structure)"))
        self.assertEqual(force_bytes(inst.location.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.location.text), force_bytes("Fetus"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testBodyStructure2(self):
        inst = self.instantiate_from("bodystructure-example-skin-patch.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodyStructure instance")
        self.implBodyStructure2(inst)
        
        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure2(inst2)
    
    def implBodyStructure2(self, inst):
        self.assertFalse(inst.active)
        self.assertEqual(force_bytes(inst.description), force_bytes("inner surface (volar) of the left forearm"))
        self.assertEqual(force_bytes(inst.id), force_bytes("skin-patch"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://goodhealth.org/bodystructure/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.location.coding[0].code), force_bytes("14975008"))
        self.assertEqual(force_bytes(inst.location.coding[0].display), force_bytes("Forearm"))
        self.assertEqual(force_bytes(inst.location.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.location.text), force_bytes("Forearm"))
        self.assertEqual(force_bytes(inst.locationQualifier[0].coding[0].code), force_bytes("419161000"))
        self.assertEqual(force_bytes(inst.locationQualifier[0].coding[0].display), force_bytes("Unilateral left"))
        self.assertEqual(force_bytes(inst.locationQualifier[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.locationQualifier[0].text), force_bytes("Left"))
        self.assertEqual(force_bytes(inst.locationQualifier[1].coding[0].code), force_bytes("263929005"))
        self.assertEqual(force_bytes(inst.locationQualifier[1].coding[0].display), force_bytes("Volar"))
        self.assertEqual(force_bytes(inst.locationQualifier[1].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.locationQualifier[1].text), force_bytes("Volar"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.morphology.text), force_bytes("Skin patch"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testBodyStructure3(self):
        inst = self.instantiate_from("bodystructure-example-tumor.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodyStructure instance")
        self.implBodyStructure3(inst)
        
        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure3(inst2)
    
    def implBodyStructure3(self, inst):
        self.assertEqual(force_bytes(inst.description), force_bytes("7 cm maximum diameter"))
        self.assertEqual(force_bytes(inst.id), force_bytes("tumor"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://goodhealth.org/bodystructure/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.image[0].contentType), force_bytes("application/dicom"))
        self.assertEqual(force_bytes(inst.image[0].url), force_bytes("http://imaging.acme.com/wado/server?requestType=WADO&amp;wado_details"))
        self.assertEqual(force_bytes(inst.location.coding[0].code), force_bytes("78961009"))
        self.assertEqual(force_bytes(inst.location.coding[0].display), force_bytes("Splenic structure (body structure)"))
        self.assertEqual(force_bytes(inst.location.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.location.text), force_bytes("Spleen"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.morphology.coding[0].code), force_bytes("4147007"))
        self.assertEqual(force_bytes(inst.morphology.coding[0].display), force_bytes("Mass (morphologic abnormality)"))
        self.assertEqual(force_bytes(inst.morphology.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.morphology.text), force_bytes("Splenic mass"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

