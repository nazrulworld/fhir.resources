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
from .. import device
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class DeviceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Device", js["resourceType"])
        return device.Device(js)
    
    def testDevice1(self):
        inst = self.instantiate_from("device-example-udi4.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice1(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice1(inst2)
    
    def implDevice1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example-udi4"))
        self.assertEqual(force_bytes(inst.lotNumber), force_bytes("RZ12345678"))
        self.assertEqual(force_bytes(inst.manufacturer), force_bytes("GlobalMed, Inc"))
        self.assertEqual(force_bytes(inst.status), force_bytes("inactive"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.udi.carrierHRF), force_bytes("=)1TE123456A&)RZ12345678"))
        self.assertEqual(force_bytes(inst.udi.issuer), force_bytes("http://hl7.org/fhir/NamingSystem/iccbba-blood"))
        self.assertEqual(force_bytes(inst.udi.jurisdiction), force_bytes("http://hl7.org/fhir/NamingSystem/fda-udi"))
    
    def testDevice2(self):
        inst = self.instantiate_from("device-example-udi2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice2(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice2(inst2)
    
    def implDevice2(self, inst):
        self.assertEqual(inst.expirationDate.date, FHIRDate("2014-02-01").date)
        self.assertEqual(inst.expirationDate.as_json(), "2014-02-01")
        self.assertEqual(force_bytes(inst.extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/device-din"))
        self.assertEqual(force_bytes(inst.extension[0].valueIdentifier.system), force_bytes("http://hl7.org/fhir/NamingSystem/iccbba-din"))
        self.assertEqual(force_bytes(inst.extension[0].valueIdentifier.value), force_bytes("A99971312345600"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-udi2"))
        self.assertEqual(inst.manufactureDate.date, FHIRDate("2013-02-01").date)
        self.assertEqual(inst.manufactureDate.as_json(), "2013-02-01")
        self.assertEqual(force_bytes(inst.manufacturer), force_bytes("Acme Devices, Inc"))
        self.assertEqual(force_bytes(inst.status), force_bytes("inactive"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.udi.deviceIdentifier), force_bytes("A9999XYZ100T0474"))
        self.assertEqual(force_bytes(inst.udi.issuer), force_bytes("http://hl7.org/fhir/NamingSystem/iccbba-other"))
        self.assertEqual(force_bytes(inst.udi.jurisdiction), force_bytes("http://hl7.org/fhir/NamingSystem/fda-udi"))
        self.assertEqual(force_bytes(inst.udi.name), force_bytes("Bone,Putty Demineralized"))
    
    def testDevice3(self):
        inst = self.instantiate_from("device-example-pacemaker.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice3(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice3(inst2)
    
    def implDevice3(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.contact[0].value), force_bytes("ext 4352"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-pacemaker"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://acme.com/devices/pacemakers/octane/serial"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("1234-5678-90AB-CDEF"))
        self.assertEqual(force_bytes(inst.lotNumber), force_bytes("1234-5678"))
        self.assertEqual(force_bytes(inst.manufacturer), force_bytes("Acme Devices, Inc"))
        self.assertEqual(force_bytes(inst.model), force_bytes("PM/Octane 2014"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("octane2014"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Performance pace maker for high octane patients"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://acme.com/devices"))
    
    def testDevice4(self):
        inst = self.instantiate_from("device-example-udi3.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice4(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice4(inst2)
    
    def implDevice4(self, inst):
        self.assertEqual(inst.expirationDate.date, FHIRDate("2020-02-02").date)
        self.assertEqual(inst.expirationDate.as_json(), "2020-02-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("example-udi3"))
        self.assertEqual(force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("SNO"))
        self.assertEqual(force_bytes(inst.identifier[0].type.coding[0].system), force_bytes("http://hl7.org/fhir/identifier-type"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("XYZ456789012345678"))
        self.assertEqual(force_bytes(inst.lotNumber), force_bytes("LOT123456789012345"))
        self.assertEqual(inst.manufactureDate.date, FHIRDate("2013-02-02").date)
        self.assertEqual(inst.manufactureDate.as_json(), "2013-02-02")
        self.assertEqual(force_bytes(inst.manufacturer), force_bytes("GlobalMed, Inc"))
        self.assertEqual(force_bytes(inst.model), force_bytes("Ultra Implantable"))
        self.assertEqual(force_bytes(inst.status), force_bytes("inactive"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.udi.carrierHRF), force_bytes("+H123PARTNO1234567890120/$$420020216LOT123456789012345/SXYZ456789012345678/16D20130202C"))
        self.assertEqual(force_bytes(inst.udi.entryType), force_bytes("manual"))
        self.assertEqual(force_bytes(inst.udi.issuer), force_bytes("http://hl7.org/fhir/NamingSystem/hibcc"))
        self.assertEqual(force_bytes(inst.udi.jurisdiction), force_bytes("http://hl7.org/fhir/NamingSystem/fda-udi"))
        self.assertEqual(force_bytes(inst.udi.name), force_bytes("FHIR® Ulltra Implantable"))
    
    def testDevice5(self):
        inst = self.instantiate_from("device-example-software.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice5(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice5(inst2)
    
    def implDevice5(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].value), force_bytes("http://acme.com"))
        self.assertEqual(force_bytes(inst.id), force_bytes("software"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://acme.com/ehr/client-ids"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("goodhealth"))
        self.assertEqual(force_bytes(inst.manufacturer), force_bytes("Acme Devices, Inc"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.text), force_bytes("EHR"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://acme.com/goodhealth/ehr/"))
        self.assertEqual(force_bytes(inst.version), force_bytes("10.23-23423"))
    
    def testDevice6(self):
        inst = self.instantiate_from("device-example-f001-feedingtube.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice6(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice6(inst2)
    
    def implDevice6(self, inst):
        self.assertEqual(inst.expirationDate.date, FHIRDate("2020-08-08").date)
        self.assertEqual(inst.expirationDate.as_json(), "2020-08-08")
        self.assertEqual(force_bytes(inst.id), force_bytes("f001"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http:/goodhealthhospital/identifier/devices"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(inst.manufactureDate.date, FHIRDate("2015-08-08").date)
        self.assertEqual(inst.manufactureDate.as_json(), "2015-08-08")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("25062003"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Feeding tube, device"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://snomed.info/sct"))
    
    def testDevice7(self):
        inst = self.instantiate_from("device-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice7(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice7(inst2)
    
    def implDevice7(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.contact[0].value), force_bytes("ext 4352"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://goodcare.org/devices/id"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("345675"))
        self.assertEqual(force_bytes(inst.identifier[1].type.coding[0].code), force_bytes("SNO"))
        self.assertEqual(force_bytes(inst.identifier[1].type.coding[0].system), force_bytes("http://hl7.org/fhir/identifier-type"))
        self.assertEqual(force_bytes(inst.identifier[1].type.text), force_bytes("Serial Number"))
        self.assertEqual(force_bytes(inst.identifier[1].value), force_bytes("AMID-342135-8464"))
        self.assertEqual(force_bytes(inst.lotNumber), force_bytes("43453424"))
        self.assertEqual(force_bytes(inst.manufacturer), force_bytes("Acme Devices, Inc"))
        self.assertEqual(force_bytes(inst.model), force_bytes("AB 45-J"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("QA Checked"))
        self.assertEqual(inst.note[0].time.date, FHIRDate("2015-06-28T14:03:32+10:00").date)
        self.assertEqual(inst.note[0].time.as_json(), "2015-06-28T14:03:32+10:00")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("86184003"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Electrocardiographic monitor and recorder"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.type.text), force_bytes("ECG"))
    
    def testDevice8(self):
        inst = self.instantiate_from("device-example-udi1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice8(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice8(inst2)
    
    def implDevice8(self, inst):
        self.assertEqual(inst.expirationDate.date, FHIRDate("2014-11-20").date)
        self.assertEqual(inst.expirationDate.as_json(), "2014-11-20")
        self.assertEqual(force_bytes(inst.id), force_bytes("example-udi1"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://acme.com/devices/pacemakers/octane/serial"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("1234-5678-90AB-CDEF"))
        self.assertEqual(force_bytes(inst.identifier[1].type.coding[0].code), force_bytes("SNO"))
        self.assertEqual(force_bytes(inst.identifier[1].type.coding[0].system), force_bytes("http://hl7.org/fhir/identifier-type"))
        self.assertEqual(force_bytes(inst.identifier[1].value), force_bytes("10987654d321"))
        self.assertEqual(force_bytes(inst.lotNumber), force_bytes("7654321D"))
        self.assertEqual(force_bytes(inst.manufacturer), force_bytes("Acme Devices, Inc"))
        self.assertEqual(force_bytes(inst.model), force_bytes("PM/Octane 2014"))
        self.assertEqual(force_bytes(inst.safety[0].coding[0].code), force_bytes("mr-unsafe"))
        self.assertEqual(force_bytes(inst.safety[0].coding[0].display), force_bytes("MR Unsafe"))
        self.assertEqual(force_bytes(inst.safety[0].coding[0].system), force_bytes("urn:oid:2.16.840.1.113883.3.26.1.1"))
        self.assertEqual(force_bytes(inst.safety[0].text), force_bytes("MR Unsafe"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("468063009"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Coated femoral stem prosthesis, modular"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.type.text), force_bytes("Coated femoral stem prosthesis, modular"))
        self.assertEqual(force_bytes(inst.udi.carrierAIDC), force_bytes("XWQyMDExMDg1NzY3NDAwMjAxNzE3MTQxMTIwMTBOWUZVTDAx4oaUMjExOTI4MzfihpQ3MTNBMUIyQzNENEU1RjZH"))
        self.assertEqual(force_bytes(inst.udi.carrierHRF), force_bytes("{01}00844588003288{17}141120{10}7654321D{21}10987654d321"))
        self.assertEqual(force_bytes(inst.udi.deviceIdentifier), force_bytes("00844588003288"))
        self.assertEqual(force_bytes(inst.udi.entryType), force_bytes("barcode"))
        self.assertEqual(force_bytes(inst.udi.issuer), force_bytes("http://hl7.org/fhir/NamingSystem/gs1"))
        self.assertEqual(force_bytes(inst.udi.jurisdiction), force_bytes("http://hl7.org/fhir/NamingSystem/fda-udi"))
        self.assertEqual(force_bytes(inst.udi.name), force_bytes("FHIR® Hip System"))
    
    def testDevice9(self):
        inst = self.instantiate_from("device-example-ihe-pcd.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice9(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice9(inst2)
    
    def implDevice9(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("ihe-pcd"))
        self.assertEqual(force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("SNO"))
        self.assertEqual(force_bytes(inst.identifier[0].type.coding[0].system), force_bytes("http://hl7.org/fhir/identifier-type"))
        self.assertEqual(force_bytes(inst.identifier[0].type.text), force_bytes("Serial Number"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("AMID-123-456"))
        self.assertEqual(force_bytes(inst.lotNumber), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.manufacturer), force_bytes("Acme Devices, Inc"))
        self.assertEqual(force_bytes(inst.model), force_bytes("A.1.1"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.text), force_bytes("Vital Signs Monitor"))

