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
from .. import messagedefinition
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class MessageDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MessageDefinition", js["resourceType"])
        return messagedefinition.MessageDefinition(js)
    
    def testMessageDefinition1(self):
        inst = self.instantiate_from("messagedefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MessageDefinition instance")
        self.implMessageDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("MessageDefinition", js["resourceType"])
        inst2 = messagedefinition.MessageDefinition(js)
        self.implMessageDefinition1(inst2)
    
    def implMessageDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.category), force_bytes("Notification"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org"))
        self.assertEqual(inst.date.date, FHIRDate("2016-11-09").date)
        self.assertEqual(inst.date.as_json(), "2016-11-09")
        self.assertEqual(force_bytes(inst.event.code), force_bytes("communication-request"))
        self.assertEqual(force_bytes(inst.event.system), force_bytes("http://hl7.org/fhir/message-events"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.name), force_bytes("EXAMPLE"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Health Level Seven, Int'l"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Defines a base example for other MessageDefintion instances."))
        self.assertFalse(inst.responseRequired)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Message definition base example</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Message definition base example"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/MessageDefinition/example"))

