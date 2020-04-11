# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyRequest
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

from .. import supplyrequest
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class SupplyRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
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
        self.assertEqual(
            force_bytes(inst.category.coding[0].code), force_bytes("central")
        )
        self.assertEqual(
            force_bytes(inst.category.coding[0].display),
            force_bytes("Central Stock Resupply"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("simpleorder"))
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("Order10284"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-12-31").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-12-31")
        self.assertEqual(
            force_bytes(inst.orderedItem.itemCodeableConcept.coding[0].code),
            force_bytes("BlueTubes"),
        )
        self.assertEqual(
            force_bytes(inst.orderedItem.itemCodeableConcept.coding[0].display),
            force_bytes("Blood collect tubes blue cap"),
        )
        self.assertEqual(inst.orderedItem.quantity.value, 10)
        self.assertEqual(force_bytes(inst.priority), force_bytes("asap"))
        self.assertEqual(
            force_bytes(inst.reasonCodeableConcept.coding[0].code),
            force_bytes("stock_low"),
        )
        self.assertEqual(
            force_bytes(inst.reasonCodeableConcept.coding[0].display),
            force_bytes("Refill due to low stock"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
