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
from .. import supplyrequest
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class SupplyRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SupplyRequest", js["resourceType"])
        return supplyrequest.SupplyRequest(js)
    
    def testSupplyRequest1(self):
        inst = self.instantiate_from("supplyrequest-example-simpleorder.json")
        self.assertIsNotNone(inst, "Must have instantiated a SupplyRequest instance")
        self.implSupplyRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("SupplyRequest", js["resourceType"])
        inst2 = supplyrequest.SupplyRequest(js)
        self.implSupplyRequest1(inst2)
    
    def implSupplyRequest1(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-12-31").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-12-31")
        self.assertEqual(force_bytes(inst.category.coding[0].code), force_bytes("central"))
        self.assertEqual(force_bytes(inst.category.coding[0].display), force_bytes("Central Stock Resupply"))
        self.assertEqual(force_bytes(inst.id), force_bytes("simpleorder"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("Order10284"))
        self.assertEqual(force_bytes(inst.itemCodeableConcept.coding[0].code), force_bytes("BlueTubes"))
        self.assertEqual(force_bytes(inst.itemCodeableConcept.coding[0].display), force_bytes("Blood collect tubes blue cap"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-12-31").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-12-31")
        self.assertEqual(force_bytes(inst.priority), force_bytes("asap"))
        self.assertEqual(inst.quantity.value, 10)
        self.assertEqual(force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("stock_low"))
        self.assertEqual(force_bytes(inst.reasonCode[0].coding[0].display), force_bytes("Refill due to low stock"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

