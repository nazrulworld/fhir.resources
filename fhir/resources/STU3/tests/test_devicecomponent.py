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
from .. import devicecomponent
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class DeviceComponentTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceComponent", js["resourceType"])
        return devicecomponent.DeviceComponent(js)
    
    def testDeviceComponent1(self):
        inst = self.instantiate_from("devicecomponent-example-prodspec.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceComponent instance")
        self.implDeviceComponent1(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceComponent", js["resourceType"])
        inst2 = devicecomponent.DeviceComponent(js)
        self.implDeviceComponent1(inst2)
    
    def implDeviceComponent1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example-prodspec"))
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("789123"))
        self.assertEqual(force_bytes(inst.languageCode.coding[0].code), force_bytes("en-US"))
        self.assertEqual(force_bytes(inst.languageCode.coding[0].system), force_bytes("http://tools.ietf.org/html/bcp47"))
        self.assertEqual(inst.lastSystemChange.date, FHIRDate("2014-10-07T14:45:00Z").date)
        self.assertEqual(inst.lastSystemChange.as_json(), "2014-10-07T14:45:00Z")
        self.assertEqual(force_bytes(inst.operationalStatus[0].coding[0].code), force_bytes("off"))
        self.assertEqual(force_bytes(inst.operationalStatus[0].coding[0].display), force_bytes("Off"))
        self.assertEqual(force_bytes(inst.productionSpecification[0].productionSpec), force_bytes("xa-12324-b"))
        self.assertEqual(force_bytes(inst.productionSpecification[0].specType.coding[0].code), force_bytes("serial-number"))
        self.assertEqual(force_bytes(inst.productionSpecification[0].specType.coding[0].display), force_bytes("Serial number"))
        self.assertEqual(force_bytes(inst.productionSpecification[1].productionSpec), force_bytes("1.1"))
        self.assertEqual(force_bytes(inst.productionSpecification[1].specType.coding[0].code), force_bytes("hardware-revision"))
        self.assertEqual(force_bytes(inst.productionSpecification[1].specType.coding[0].display), force_bytes("Hardware Revision"))
        self.assertEqual(force_bytes(inst.productionSpecification[2].productionSpec), force_bytes("1.12"))
        self.assertEqual(force_bytes(inst.productionSpecification[2].specType.coding[0].code), force_bytes("software-revision"))
        self.assertEqual(force_bytes(inst.productionSpecification[2].specType.coding[0].display), force_bytes("Software Revision"))
        self.assertEqual(force_bytes(inst.productionSpecification[3].productionSpec), force_bytes("1.0.23"))
        self.assertEqual(force_bytes(inst.productionSpecification[3].specType.coding[0].code), force_bytes("firmware-revision"))
        self.assertEqual(force_bytes(inst.productionSpecification[3].specType.coding[0].display), force_bytes("Firmware Revision"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("2000"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("MDC_DEV_ANALY_SAT_O2_MDS"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("urn:iso:std:iso:11073:10101"))
    
    def testDeviceComponent2(self):
        inst = self.instantiate_from("devicecomponent-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceComponent instance")
        self.implDeviceComponent2(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceComponent", js["resourceType"])
        inst2 = devicecomponent.DeviceComponent(js)
        self.implDeviceComponent2(inst2)
    
    def implDeviceComponent2(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("0"))
        self.assertEqual(force_bytes(inst.languageCode.coding[0].code), force_bytes("en-US"))
        self.assertEqual(force_bytes(inst.languageCode.coding[0].system), force_bytes("http://tools.ietf.org/html/bcp47"))
        self.assertEqual(inst.lastSystemChange.date, FHIRDate("2014-10-07T14:45:00Z").date)
        self.assertEqual(inst.lastSystemChange.as_json(), "2014-10-07T14:45:00Z")
        self.assertEqual(force_bytes(inst.measurementPrinciple), force_bytes("optical"))
        self.assertEqual(force_bytes(inst.operationalStatus[0].coding[0].code), force_bytes("off"))
        self.assertEqual(force_bytes(inst.operationalStatus[0].coding[0].display), force_bytes("Off"))
        self.assertEqual(force_bytes(inst.operationalStatus[0].coding[0].system), force_bytes("urn:iso:std:iso:11073:10101"))
        self.assertEqual(force_bytes(inst.parameterGroup.coding[0].code), force_bytes("miscellaneous"))
        self.assertEqual(force_bytes(inst.parameterGroup.coding[0].display), force_bytes("Miscellaneous Parameter Group"))
        self.assertEqual(force_bytes(inst.parameterGroup.coding[0].system), force_bytes("urn:iso:std:iso:11073:10101"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("2000"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("MDC_DEV_ANALY_SAT_O2_MDS"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("urn:iso:std:iso:11073:10101"))

