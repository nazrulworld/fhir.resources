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
from .. import medicinalproductmanufactured
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class MedicinalProductManufacturedTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductManufactured", js["resourceType"])
        return medicinalproductmanufactured.MedicinalProductManufactured(js)
    
    def testMedicinalProductManufactured1(self):
        inst = self.instantiate_from("medicinalproductmanufactured-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductManufactured instance")
        self.implMedicinalProductManufactured1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductManufactured", js["resourceType"])
        inst2 = medicinalproductmanufactured.MedicinalProductManufactured(js)
        self.implMedicinalProductManufactured1(inst2)
    
    def implMedicinalProductManufactured1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.manufacturedDoseForm.coding[0].code), force_bytes("Film-coatedtablet"))
        self.assertEqual(force_bytes(inst.manufacturedDoseForm.coding[0].system), force_bytes("http://ema.europa.eu/example/manufactureddoseform"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.physicalCharacteristics.color[0]), force_bytes("Pink"))
        self.assertEqual(force_bytes(inst.physicalCharacteristics.imprint[0]), force_bytes("894"))
        self.assertEqual(force_bytes(inst.physicalCharacteristics.shape), force_bytes("Oval"))
        self.assertEqual(force_bytes(inst.quantity.unit), force_bytes("1"))
        self.assertEqual(inst.quantity.value, 10)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.unitOfPresentation.coding[0].code), force_bytes("Tablet"))
        self.assertEqual(force_bytes(inst.unitOfPresentation.coding[0].system), force_bytes("http://ema.europa.eu/example/unitofpresentation"))

