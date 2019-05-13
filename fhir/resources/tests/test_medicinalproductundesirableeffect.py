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
from .. import medicinalproductundesirableeffect
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class MedicinalProductUndesirableEffectTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductUndesirableEffect", js["resourceType"])
        return medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(js)
    
    def testMedicinalProductUndesirableEffect1(self):
        inst = self.instantiate_from("medicinalproductundesirableeffect-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductUndesirableEffect instance")
        self.implMedicinalProductUndesirableEffect1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductUndesirableEffect", js["resourceType"])
        inst2 = medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(js)
        self.implMedicinalProductUndesirableEffect1(inst2)
    
    def implMedicinalProductUndesirableEffect1(self, inst):
        self.assertEqual(force_bytes(inst.classification.coding[0].code), force_bytes("Bloodandlymphaticsystemdisorders"))
        self.assertEqual(force_bytes(inst.classification.coding[0].system), force_bytes("http://ema.europa.eu/example/symptom-condition-effectclassification"))
        self.assertEqual(force_bytes(inst.frequencyOfOccurrence.coding[0].code), force_bytes("Common"))
        self.assertEqual(force_bytes(inst.frequencyOfOccurrence.coding[0].system), force_bytes("http://ema.europa.eu/example/frequencyofoccurrence"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.symptomConditionEffect.coding[0].code), force_bytes("Anaemia"))
        self.assertEqual(force_bytes(inst.symptomConditionEffect.coding[0].system), force_bytes("http://ema.europa.eu/example/undesirableeffectassymptom-condition-effect"))
        self.assertEqual(force_bytes(inst.symptomConditionEffect.text), force_bytes("Prevention of\\nVTE in adult\\npatients who have\\nundergone\\nelective hip or\\nknee replacement\\nsurgery (VTEp)"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

