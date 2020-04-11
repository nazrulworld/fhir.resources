# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyDelivery
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import supplydelivery
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class SupplyDeliveryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
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
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("Order10284"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-12-31").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-12-31")
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(
            force_bytes(inst.suppliedItem.itemCodeableConcept.coding[0].code),
            force_bytes("BlueTubes"),
        )
        self.assertEqual(
            force_bytes(inst.suppliedItem.itemCodeableConcept.coding[0].display),
            force_bytes("Blood collect tubes blue cap"),
        )
        self.assertEqual(inst.suppliedItem.quantity.value, 10)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("device"))
        self.assertEqual(
            force_bytes(inst.type.coding[0].system),
            force_bytes("http://hl7.org/fhir/supply-item-type"),
        )
        self.assertEqual(
            force_bytes(inst.type.text), force_bytes("Blood collect tubes blue cap")
        )

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
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("98398459409"))
        self.assertEqual(force_bytes(inst.status), force_bytes("in-progress"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering here]</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
