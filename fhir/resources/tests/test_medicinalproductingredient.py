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
from .. import medicinalproductingredient
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class MedicinalProductIngredientTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductIngredient", js["resourceType"])
        return medicinalproductingredient.MedicinalProductIngredient(js)
    
    def testMedicinalProductIngredient1(self):
        inst = self.instantiate_from("medicinalproductingredient-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductIngredient instance")
        self.implMedicinalProductIngredient1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductIngredient", js["resourceType"])
        inst2 = medicinalproductingredient.MedicinalProductIngredient(js)
        self.implMedicinalProductIngredient1(inst2)
    
    def implMedicinalProductIngredient1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.role.coding[0].code), force_bytes("ActiveBase"))
        self.assertEqual(force_bytes(inst.role.coding[0].system), force_bytes("http://ema.europa.eu/example/ingredientRole"))
        self.assertEqual(force_bytes(inst.specifiedSubstance[0].code.coding[0].code), force_bytes("equixabanCompanyequixaban1"))
        self.assertEqual(force_bytes(inst.specifiedSubstance[0].code.coding[0].system), force_bytes("http://ema.europa.eu/example/specifiedSubstance"))
        self.assertEqual(force_bytes(inst.specifiedSubstance[0].group.coding[0].code), force_bytes("2"))
        self.assertEqual(force_bytes(inst.specifiedSubstance[0].group.coding[0].system), force_bytes("http://ema.europa.eu/example/specifiedSubstanceGroup"))
        self.assertEqual(force_bytes(inst.substance.code.coding[0].code), force_bytes("EQUIXABAN"))
        self.assertEqual(force_bytes(inst.substance.code.coding[0].system), force_bytes("http://ema.europa.eu/example/substance"))
        self.assertEqual(force_bytes(inst.substance.strength[0].presentation.denominator.unit), force_bytes("{tablet}"))
        self.assertEqual(inst.substance.strength[0].presentation.denominator.value, 1)
        self.assertEqual(force_bytes(inst.substance.strength[0].presentation.numerator.unit), force_bytes("mg"))
        self.assertEqual(inst.substance.strength[0].presentation.numerator.value, 2.5)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

