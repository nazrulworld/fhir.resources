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
from .. import endpoint
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class EndpointTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Endpoint", js["resourceType"])
        return endpoint.Endpoint(js)
    
    def testEndpoint1(self):
        inst = self.instantiate_from("endpoint-example-direct.json")
        self.assertIsNotNone(inst, "Must have instantiated a Endpoint instance")
        self.implEndpoint1(inst)
        
        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint1(inst2)
    
    def implEndpoint1(self, inst):
        self.assertEqual(force_bytes(inst.address), force_bytes("mailto:MARTIN.SMIETANKA@directnppes.com"))
        self.assertEqual(force_bytes(inst.connectionType.code), force_bytes("direct-project"))
        self.assertEqual(force_bytes(inst.id), force_bytes("direct-endpoint"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("MARTIN SMIETANKA"))
        self.assertEqual(force_bytes(inst.payloadType[0].coding[0].code), force_bytes("urn:hl7-org:sdwg:ccda-structuredBody:1.1"))
        self.assertEqual(force_bytes(inst.payloadType[0].coding[0].system), force_bytes("urn:oid:1.3.6.1.4.1.19376.1.2.3"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testEndpoint2(self):
        inst = self.instantiate_from("endpoint-example-iid.json")
        self.assertIsNotNone(inst, "Must have instantiated a Endpoint instance")
        self.implEndpoint2(inst)
        
        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint2(inst2)
    
    def implEndpoint2(self, inst):
        self.assertEqual(force_bytes(inst.address), force_bytes("https://pacs.hospital.org/IHEInvokeImageDisplay"))
        self.assertEqual(force_bytes(inst.connectionType.code), force_bytes("ihe-iid"))
        self.assertEqual(force_bytes(inst.connectionType.system), force_bytes("http://terminology.hl7.org/CodeSystem/endpoint-connection-type"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-iid"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("PACS Hospital Invoke Image Display endpoint"))
        self.assertEqual(force_bytes(inst.payloadType[0].text), force_bytes("DICOM IID"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testEndpoint3(self):
        inst = self.instantiate_from("endpoint-example-wadors.json")
        self.assertIsNotNone(inst, "Must have instantiated a Endpoint instance")
        self.implEndpoint3(inst)
        
        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint3(inst2)
    
    def implEndpoint3(self, inst):
        self.assertEqual(force_bytes(inst.address), force_bytes("https://pacs.hospital.org/wado-rs"))
        self.assertEqual(force_bytes(inst.connectionType.code), force_bytes("dicom-wado-rs"))
        self.assertEqual(force_bytes(inst.connectionType.system), force_bytes("http://terminology.hl7.org/CodeSystem/endpoint-connection-type"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-wadors"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("PACS Hospital DICOM WADO-RS endpoint"))
        self.assertEqual(force_bytes(inst.payloadMimeType[0]), force_bytes("application/dicom"))
        self.assertEqual(force_bytes(inst.payloadType[0].text), force_bytes("DICOM WADO-RS"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testEndpoint4(self):
        inst = self.instantiate_from("endpoint-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Endpoint instance")
        self.implEndpoint4(inst)
        
        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint4(inst2)
    
    def implEndpoint4(self, inst):
        self.assertEqual(force_bytes(inst.address), force_bytes("http://fhir3.healthintersections.com.au/open/CarePlan"))
        self.assertEqual(force_bytes(inst.connectionType.code), force_bytes("hl7-fhir-rest"))
        self.assertEqual(force_bytes(inst.connectionType.system), force_bytes("http://terminology.hl7.org/CodeSystem/endpoint-connection-type"))
        self.assertEqual(force_bytes(inst.contact[0].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.contact[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.contact[0].value), force_bytes("endpointmanager@example.org"))
        self.assertEqual(force_bytes(inst.header[0]), force_bytes("bearer-code BASGS534s4"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/enpoint-identifier"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("epcp12"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Health Intersections CarePlan Hub"))
        self.assertEqual(force_bytes(inst.payloadMimeType[0]), force_bytes("application/fhir+xml"))
        self.assertEqual(force_bytes(inst.payloadType[0].coding[0].code), force_bytes("CarePlan"))
        self.assertEqual(force_bytes(inst.payloadType[0].coding[0].system), force_bytes("http://hl7.org/fhir/resource-types"))
        self.assertEqual(inst.period.start.date, FHIRDate("2014-09-01").date)
        self.assertEqual(inst.period.start.as_json(), "2014-09-01")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

