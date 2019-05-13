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
from .. import medicationknowledge
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class MedicationKnowledgeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicationKnowledge", js["resourceType"])
        return medicationknowledge.MedicationKnowledge(js)
    
    def testMedicationKnowledge1(self):
        inst = self.instantiate_from("medicationknowledge-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationKnowledge instance")
        self.implMedicationKnowledge1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationKnowledge", js["resourceType"])
        inst2 = medicationknowledge.MedicationKnowledge(js)
        self.implMedicationKnowledge1(inst2)
    
    def implMedicationKnowledge1(self, inst):
        self.assertEqual(force_bytes(inst.amount.unit), force_bytes("mg/ml"))
        self.assertEqual(inst.amount.value, 50)
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("0069-2587-10"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://hl7.org/fhir/sid/ndc"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("org4"))
        self.assertEqual(force_bytes(inst.doseForm.coding[0].code), force_bytes("385219001"))
        self.assertEqual(force_bytes(inst.doseForm.coding[0].display), force_bytes("Injection Solution (qualifier value)"))
        self.assertEqual(force_bytes(inst.doseForm.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.synonym[0]), force_bytes("Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

