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
from .. import schedule
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ScheduleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Schedule", js["resourceType"])
        return schedule.Schedule(js)
    
    def testSchedule1(self):
        inst = self.instantiate_from("schedule-provider-location1-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Schedule instance")
        self.implSchedule1(inst)
        
        js = inst.as_json()
        self.assertEqual("Schedule", js["resourceType"])
        inst2 = schedule.Schedule(js)
        self.implSchedule1(inst2)
    
    def implSchedule1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.comment), force_bytes("The slots attached to this schedule are for genetic counselling in the USS Enterprise-D Sickbay."))
        self.assertEqual(force_bytes(inst.id), force_bytes("exampleloc1"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/scheduleid"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("46"))
        self.assertEqual(inst.planningHorizon.end.date, FHIRDate("2017-12-25T09:30:00Z").date)
        self.assertEqual(inst.planningHorizon.end.as_json(), "2017-12-25T09:30:00Z")
        self.assertEqual(inst.planningHorizon.start.date, FHIRDate("2017-12-25T09:15:00Z").date)
        self.assertEqual(inst.planningHorizon.start.as_json(), "2017-12-25T09:15:00Z")
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].code), force_bytes("17"))
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].display), force_bytes("General Practice"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].code), force_bytes("75"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].display), force_bytes("Genetic Counselling"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].code), force_bytes("394580004"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].display), force_bytes("Clinical genetics"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testSchedule2(self):
        inst = self.instantiate_from("schedule-provider-location2-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Schedule instance")
        self.implSchedule2(inst)
        
        js = inst.as_json()
        self.assertEqual("Schedule", js["resourceType"])
        inst2 = schedule.Schedule(js)
        self.implSchedule2(inst2)
    
    def implSchedule2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.comment), force_bytes("The slots attached to this schedule are for neurosurgery operations at Starfleet HQ only."))
        self.assertEqual(force_bytes(inst.id), force_bytes("exampleloc2"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/scheduleid"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("47"))
        self.assertEqual(inst.planningHorizon.end.date, FHIRDate("2017-12-25T09:30:00Z").date)
        self.assertEqual(inst.planningHorizon.end.as_json(), "2017-12-25T09:30:00Z")
        self.assertEqual(inst.planningHorizon.start.date, FHIRDate("2017-12-25T09:15:00Z").date)
        self.assertEqual(inst.planningHorizon.start.as_json(), "2017-12-25T09:15:00Z")
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].code), force_bytes("31"))
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].display), force_bytes("Specialist Surgical"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].code), force_bytes("221"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].display), force_bytes("Surgery - General"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].code), force_bytes("394610002"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].display), force_bytes("Surgery-Neurosurgery"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testSchedule3(self):
        inst = self.instantiate_from("schedule-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Schedule instance")
        self.implSchedule3(inst)
        
        js = inst.as_json()
        self.assertEqual("Schedule", js["resourceType"])
        inst2 = schedule.Schedule(js)
        self.implSchedule3(inst2)
    
    def implSchedule3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.comment), force_bytes("The slots attached to this schedule should be specialized to cover immunizations within the clinic"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/scheduleid"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("45"))
        self.assertEqual(inst.planningHorizon.end.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.planningHorizon.end.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(inst.planningHorizon.start.date, FHIRDate("2013-12-25T09:15:00Z").date)
        self.assertEqual(inst.planningHorizon.start.as_json(), "2013-12-25T09:15:00Z")
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].code), force_bytes("17"))
        self.assertEqual(force_bytes(inst.serviceCategory.coding[0].display), force_bytes("General Practice"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].code), force_bytes("57"))
        self.assertEqual(force_bytes(inst.serviceType[0].coding[0].display), force_bytes("Immunization"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].code), force_bytes("408480009"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].display), force_bytes("Clinical immunology"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

