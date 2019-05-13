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
from .. import practitionerrole
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class PractitionerRoleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PractitionerRole", js["resourceType"])
        return practitionerrole.PractitionerRole(js)
    
    def testPractitionerRole1(self):
        inst = self.instantiate_from("practitionerrole-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PractitionerRole instance")
        self.implPractitionerRole1(inst)
        
        js = inst.as_json()
        self.assertEqual("PractitionerRole", js["resourceType"])
        inst2 = practitionerrole.PractitionerRole(js)
        self.implPractitionerRole1(inst2)
    
    def implPractitionerRole1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.availabilityExceptions), force_bytes("Adam is generally unavailable on public holidays and during the Christmas/New Year break"))
        self.assertEqual(inst.availableTime[0].availableEndTime.date, FHIRDate("16:30:00").date)
        self.assertEqual(inst.availableTime[0].availableEndTime.as_json(), "16:30:00")
        self.assertEqual(inst.availableTime[0].availableStartTime.date, FHIRDate("09:00:00").date)
        self.assertEqual(inst.availableTime[0].availableStartTime.as_json(), "09:00:00")
        self.assertEqual(force_bytes(inst.availableTime[0].daysOfWeek[0]), force_bytes("mon"))
        self.assertEqual(force_bytes(inst.availableTime[0].daysOfWeek[1]), force_bytes("tue"))
        self.assertEqual(force_bytes(inst.availableTime[0].daysOfWeek[2]), force_bytes("wed"))
        self.assertEqual(inst.availableTime[1].availableEndTime.date, FHIRDate("12:00:00").date)
        self.assertEqual(inst.availableTime[1].availableEndTime.as_json(), "12:00:00")
        self.assertEqual(inst.availableTime[1].availableStartTime.date, FHIRDate("09:00:00").date)
        self.assertEqual(inst.availableTime[1].availableStartTime.as_json(), "09:00:00")
        self.assertEqual(force_bytes(inst.availableTime[1].daysOfWeek[0]), force_bytes("thu"))
        self.assertEqual(force_bytes(inst.availableTime[1].daysOfWeek[1]), force_bytes("fri"))
        self.assertEqual(force_bytes(inst.code[0].coding[0].code), force_bytes("RP"))
        self.assertEqual(force_bytes(inst.code[0].coding[0].system), force_bytes("http://hl7.org/fhir/v2/0286"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.acme.org/practitioners"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("23"))
        self.assertEqual(force_bytes(inst.notAvailable[0].description), force_bytes("Adam will be on extended leave during May 2017"))
        self.assertEqual(inst.notAvailable[0].during.end.date, FHIRDate("2017-05-20").date)
        self.assertEqual(inst.notAvailable[0].during.end.as_json(), "2017-05-20")
        self.assertEqual(inst.notAvailable[0].during.start.date, FHIRDate("2017-05-01").date)
        self.assertEqual(inst.notAvailable[0].during.start.as_json(), "2017-05-01")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2012-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2012-01-01")
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].code), force_bytes("408443003"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].display), force_bytes("General medical practice"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("(03) 5555 6473"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[1].value), force_bytes("adam.southern@example.org"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

