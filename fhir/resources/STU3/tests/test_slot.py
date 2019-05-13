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
from .. import slot
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class SlotTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Slot", js["resourceType"])
        return slot.Slot(js)
    
    def testSlot1(self):
        inst = self.instantiate_from("slot-example-unavailable.json")
        self.assertIsNotNone(inst, "Must have instantiated a Slot instance")
        self.implSlot1(inst)
        
        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot1(inst2)
    
    def implSlot1(self, inst):
        self.assertEqual(force_bytes(inst.comment), force_bytes("Dr Careful is out of the office"))
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T09:45:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T09:45:00Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("3"))
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].code), force_bytes("17"))
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].display), force_bytes("General Practice"))
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(force_bytes(inst.status), force_bytes("busy-unavailable"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testSlot2(self):
        inst = self.instantiate_from("slot-example-tentative.json")
        self.assertIsNotNone(inst, "Must have instantiated a Slot instance")
        self.implSlot2(inst)
        
        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot2(inst2)
    
    def implSlot2(self, inst):
        self.assertEqual(force_bytes(inst.comment), force_bytes("Dr Careful is out of the office"))
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T10:00:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T10:00:00Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("2"))
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].code), force_bytes("17"))
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].display), force_bytes("General Practice"))
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:45:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:45:00Z")
        self.assertEqual(force_bytes(inst.status), force_bytes("busy-tentative"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testSlot3(self):
        inst = self.instantiate_from("slot-example-busy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Slot instance")
        self.implSlot3(inst)
        
        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot3(inst2)
    
    def implSlot3(self, inst):
        self.assertEqual(force_bytes(inst.comment), force_bytes("Assessments should be performed before requesting appointments in this slot."))
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T09:15:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T09:15:00Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("1"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/identifiers/slots"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123132"))
        self.assertTrue(inst.overbooked)
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].code), force_bytes("17"))
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].display), force_bytes("General Practice"))
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:00:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:00:00Z")
        self.assertEqual(force_bytes(inst.status), force_bytes("busy"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testSlot4(self):
        inst = self.instantiate_from("slot-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Slot instance")
        self.implSlot4(inst)
        
        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot4(inst2)
    
    def implSlot4(self, inst):
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].code), force_bytes("WALKIN"))
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].display), force_bytes("A previously unscheduled walk-in visit"))
        self.assertEqual(force_bytes(inst.appointmentType.coding[0].system), force_bytes("http://hl7.org/fhir/v2/0276"))
        self.assertEqual(force_bytes(inst.comment), force_bytes("Assessments should be performed before requesting appointments in this slot."))
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].code), force_bytes("17"))
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].display), force_bytes("General Practice"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].code), force_bytes("57"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].display), force_bytes("Immunization"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].code), force_bytes("408480009"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].display), force_bytes("Clinical immunology"))
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:15:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:15:00Z")
        self.assertEqual(force_bytes(inst.status), force_bytes("free"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

