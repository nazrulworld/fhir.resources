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
from .. import messageheader
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class MessageHeaderTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MessageHeader", js["resourceType"])
        return messageheader.MessageHeader(js)
    
    def testMessageHeader1(self):
        inst = self.instantiate_from("messageheader-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MessageHeader instance")
        self.implMessageHeader1(inst)
        
        js = inst.as_json()
        self.assertEqual("MessageHeader", js["resourceType"])
        inst2 = messageheader.MessageHeader(js)
        self.implMessageHeader1(inst2)
    
    def implMessageHeader1(self, inst):
        self.assertEqual(force_bytes(inst.destination[0].endpoint), force_bytes("llp:10.11.12.14:5432"))
        self.assertEqual(force_bytes(inst.destination[0].name), force_bytes("Acme Message Gateway"))
        self.assertEqual(force_bytes(inst.event.code), force_bytes("admin-notify"))
        self.assertEqual(force_bytes(inst.event.system), force_bytes("http://hl7.org/fhir/message-events"))
        self.assertEqual(force_bytes(inst.id), force_bytes("1cbdfb97-5859-48a4-8301-d54eab818d68"))
        self.assertEqual(force_bytes(inst.reason.coding[0].code), force_bytes("admit"))
        self.assertEqual(force_bytes(inst.reason.coding[0].system), force_bytes("http://hl7.org/fhir/message-reasons-encounter"))
        self.assertEqual(force_bytes(inst.response.code), force_bytes("ok"))
        self.assertEqual(force_bytes(inst.response.identifier), force_bytes("5015fe84-8e76-4526-89d8-44b322e8d4fb"))
        self.assertEqual(force_bytes(inst.source.contact.system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.source.contact.value), force_bytes("+1 (555) 123 4567"))
        self.assertEqual(force_bytes(inst.source.endpoint), force_bytes("llp:10.11.12.13:5432"))
        self.assertEqual(force_bytes(inst.source.name), force_bytes("Acme Central Patient Registry"))
        self.assertEqual(force_bytes(inst.source.software), force_bytes("FooBar Patient Manager"))
        self.assertEqual(force_bytes(inst.source.version), force_bytes("3.1.45.AABB"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(inst.timestamp.date, FHIRDate("2012-01-04T09:10:14Z").date)
        self.assertEqual(inst.timestamp.as_json(), "2012-01-04T09:10:14Z")

