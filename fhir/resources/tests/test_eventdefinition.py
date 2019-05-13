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
from .. import eventdefinition
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class EventDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EventDefinition", js["resourceType"])
        return eventdefinition.EventDefinition(js)
    
    def testEventDefinition1(self):
        inst = self.instantiate_from("eventdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EventDefinition instance")
        self.implEventDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("EventDefinition", js["resourceType"])
        inst2 = eventdefinition.EventDefinition(js)
        self.implEventDefinition1(inst2)
    
    def implEventDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Monitor all admissions to Emergency"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.trigger[0].condition.description), force_bytes("Encounter Location = emergency (active/completed encounters, current or previous)"))
        self.assertEqual(force_bytes(inst.trigger[0].condition.expression), force_bytes("(this | %previous).location.where(location = 'Location/emergency' and status in {'active', 'completed'}).exists()"))
        self.assertEqual(force_bytes(inst.trigger[0].condition.language), force_bytes("text/fhirpath"))
        self.assertEqual(force_bytes(inst.trigger[0].data[0].type), force_bytes("Encounter"))
        self.assertEqual(force_bytes(inst.trigger[0].name), force_bytes("monitor-emergency-admissions"))
        self.assertEqual(force_bytes(inst.trigger[0].type), force_bytes("named-event"))

