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
from .. import episodeofcare
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class EpisodeOfCareTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EpisodeOfCare", js["resourceType"])
        return episodeofcare.EpisodeOfCare(js)
    
    def testEpisodeOfCare1(self):
        inst = self.instantiate_from("episodeofcare-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EpisodeOfCare instance")
        self.implEpisodeOfCare1(inst)
        
        js = inst.as_json()
        self.assertEqual("EpisodeOfCare", js["resourceType"])
        inst2 = episodeofcare.EpisodeOfCare(js)
        self.implEpisodeOfCare1(inst2)
    
    def implEpisodeOfCare1(self, inst):
        self.assertEqual(inst.diagnosis[0].rank, 1)
        self.assertEqual(force_bytes(inst.diagnosis[0].role.coding[0].code), force_bytes("CC"))
        self.assertEqual(force_bytes(inst.diagnosis[0].role.coding[0].display), force_bytes("Chief complaint"))
        self.assertEqual(force_bytes(inst.diagnosis[0].role.coding[0].system), force_bytes("http://hl7.org/fhir/diagnosis-role"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/sampleepisodeofcare-identifier"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(inst.period.start.date, FHIRDate("2014-09-01").date)
        self.assertEqual(inst.period.start.as_json(), "2014-09-01")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(inst.statusHistory[0].period.end.date, FHIRDate("2014-09-14").date)
        self.assertEqual(inst.statusHistory[0].period.end.as_json(), "2014-09-14")
        self.assertEqual(inst.statusHistory[0].period.start.date, FHIRDate("2014-09-01").date)
        self.assertEqual(inst.statusHistory[0].period.start.as_json(), "2014-09-01")
        self.assertEqual(force_bytes(inst.statusHistory[0].status), force_bytes("planned"))
        self.assertEqual(inst.statusHistory[1].period.end.date, FHIRDate("2014-09-21").date)
        self.assertEqual(inst.statusHistory[1].period.end.as_json(), "2014-09-21")
        self.assertEqual(inst.statusHistory[1].period.start.date, FHIRDate("2014-09-15").date)
        self.assertEqual(inst.statusHistory[1].period.start.as_json(), "2014-09-15")
        self.assertEqual(force_bytes(inst.statusHistory[1].status), force_bytes("active"))
        self.assertEqual(inst.statusHistory[2].period.end.date, FHIRDate("2014-09-24").date)
        self.assertEqual(inst.statusHistory[2].period.end.as_json(), "2014-09-24")
        self.assertEqual(inst.statusHistory[2].period.start.date, FHIRDate("2014-09-22").date)
        self.assertEqual(inst.statusHistory[2].period.start.as_json(), "2014-09-22")
        self.assertEqual(force_bytes(inst.statusHistory[2].status), force_bytes("onhold"))
        self.assertEqual(inst.statusHistory[3].period.start.date, FHIRDate("2014-09-25").date)
        self.assertEqual(inst.statusHistory[3].period.start.as_json(), "2014-09-25")
        self.assertEqual(force_bytes(inst.statusHistory[3].status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].code), force_bytes("hacc"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].display), force_bytes("Home and Community Care"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].system), force_bytes("http://hl7.org/fhir/episodeofcare-type"))

