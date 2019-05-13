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
from .. import adverseevent
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class AdverseEventTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AdverseEvent", js["resourceType"])
        return adverseevent.AdverseEvent(js)
    
    def testAdverseEvent1(self):
        inst = self.instantiate_from("adverseevent-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AdverseEvent instance")
        self.implAdverseEvent1(inst)
        
        js = inst.as_json()
        self.assertEqual("AdverseEvent", js["resourceType"])
        inst2 = adverseevent.AdverseEvent(js)
        self.implAdverseEvent1(inst2)
    
    def implAdverseEvent1(self, inst):
        self.assertEqual(force_bytes(inst.category), force_bytes("AE"))
        self.assertEqual(inst.date.date, FHIRDate("2017-01-29T12:34:56+00:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-29T12:34:56+00:00")
        self.assertEqual(force_bytes(inst.description), force_bytes("This was a mild rash on the left forearm"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier.system), force_bytes("http://acme.com/ids/patients/risks"))
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("49476534"))
        self.assertEqual(force_bytes(inst.seriousness.coding[0].code), force_bytes("Mild"))
        self.assertEqual(force_bytes(inst.seriousness.coding[0].display), force_bytes("Mild"))
        self.assertEqual(force_bytes(inst.seriousness.coding[0].system), force_bytes("http://hl7.org/fhir/adverse-event-seriousness"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("304386008"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("O/E - itchy rash"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://snomed.info/sct"))

