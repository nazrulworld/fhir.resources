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
from .. import devicerequest
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class DeviceRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceRequest", js["resourceType"])
        return devicerequest.DeviceRequest(js)
    
    def testDeviceRequest1(self):
        inst = self.instantiate_from("devicerequest-example-insulinpump.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceRequest instance")
        self.implDeviceRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceRequest", js["resourceType"])
        inst2 = devicerequest.DeviceRequest(js)
        self.implDeviceRequest1(inst2)
    
    def implDeviceRequest1(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2013-05-08T09:33:27+07:00").date)
        self.assertEqual(inst.authoredOn.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(force_bytes(inst.codeCodeableConcept.coding[0].code), force_bytes("43148-6"))
        self.assertEqual(force_bytes(inst.codeCodeableConcept.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.codeCodeableConcept.text), force_bytes("Insulin delivery device panel"))
        self.assertEqual(force_bytes(inst.groupIdentifier.value), force_bytes("ip_request1"))
        self.assertEqual(force_bytes(inst.id), force_bytes("insulinpump"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("ip_request1.1"))
        self.assertEqual(force_bytes(inst.intent.text), force_bytes("instance-order"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("this is the right device brand and model"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(force_bytes(inst.performerType.coding[0].display), force_bytes("Qualified nurse"))
        self.assertEqual(force_bytes(inst.performerType.text), force_bytes("Nurse"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(force_bytes(inst.reasonCode[0].text), force_bytes("gastroparesis"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testDeviceRequest2(self):
        inst = self.instantiate_from("devicerequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceRequest instance")
        self.implDeviceRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceRequest", js["resourceType"])
        inst2 = devicerequest.DeviceRequest(js)
        self.implDeviceRequest2(inst2)
    
    def implDeviceRequest2(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.intent.coding[0].code), force_bytes("original-order"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

