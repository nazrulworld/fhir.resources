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
from .. import deviceusestatement
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class DeviceUseStatementTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceUseStatement", js["resourceType"])
        return deviceusestatement.DeviceUseStatement(js)
    
    def testDeviceUseStatement1(self):
        inst = self.instantiate_from("deviceusestatement-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceUseStatement instance")
        self.implDeviceUseStatement1(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceUseStatement", js["resourceType"])
        inst2 = deviceusestatement.DeviceUseStatement(js)
        self.implDeviceUseStatement1(inst2)
    
    def implDeviceUseStatement1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http:goodhealth.org/identifiers"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("51ebb7a9-4e3a-4360-9a05-0cc2d869086f"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

