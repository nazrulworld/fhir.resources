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
from .. import supplydelivery
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class SupplyDeliveryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SupplyDelivery", js["resourceType"])
        return supplydelivery.SupplyDelivery(js)
    
    def testSupplyDelivery1(self):
        inst = self.instantiate_from("supplydelivery-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SupplyDelivery instance")
        self.implSupplyDelivery1(inst)
        
        js = inst.as_json()
        self.assertEqual("SupplyDelivery", js["resourceType"])
        inst2 = supplydelivery.SupplyDelivery(js)
        self.implSupplyDelivery1(inst2)
    
    def implSupplyDelivery1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("simpledelivery"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("Order10284"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-12-31").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-12-31")
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.suppliedItem.itemCodeableConcept.coding[0].code), force_bytes("BlueTubes"))
        self.assertEqual(force_bytes(inst.suppliedItem.itemCodeableConcept.coding[0].display), force_bytes("Blood collect tubes blue cap"))
        self.assertEqual(inst.suppliedItem.quantity.value, 10)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("device"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/supply-item-type"))
        self.assertEqual(force_bytes(inst.type.text), force_bytes("Blood collect tubes blue cap"))
    
    def testSupplyDelivery2(self):
        inst = self.instantiate_from("supplydelivery-example-pumpdelivery.json")
        self.assertIsNotNone(inst, "Must have instantiated a SupplyDelivery instance")
        self.implSupplyDelivery2(inst)
        
        js = inst.as_json()
        self.assertEqual("SupplyDelivery", js["resourceType"])
        inst2 = supplydelivery.SupplyDelivery(js)
        self.implSupplyDelivery2(inst2)
    
    def implSupplyDelivery2(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("pumpdelivery"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("98398459409"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.status), force_bytes("in-progress"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

