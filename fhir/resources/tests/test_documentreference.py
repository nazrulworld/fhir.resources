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
from .. import documentreference
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class DocumentReferenceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DocumentReference", js["resourceType"])
        return documentreference.DocumentReference(js)
    
    def testDocumentReference1(self):
        inst = self.instantiate_from("documentreference-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentReference instance")
        self.implDocumentReference1(inst)
        
        js = inst.as_json()
        self.assertEqual("DocumentReference", js["resourceType"])
        inst2 = documentreference.DocumentReference(js)
        self.implDocumentReference1(inst2)
    
    def implDocumentReference1(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("History and Physical"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("History and Physical"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://ihe.net/xds/connectathon/classCodes"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("a2"))
        self.assertEqual(force_bytes(inst.content[0].attachment.contentType), force_bytes("application/hl7-v3+xml"))
        self.assertEqual(inst.content[0].attachment.creation.date, FHIRDate("2005-12-24T09:35:00+11:00").date)
        self.assertEqual(inst.content[0].attachment.creation.as_json(), "2005-12-24T09:35:00+11:00")
        self.assertEqual(force_bytes(inst.content[0].attachment.hash), force_bytes("2jmj7l5rSw0yVb/vlWAYkK/YBwk="))
        self.assertEqual(force_bytes(inst.content[0].attachment.language), force_bytes("en-US"))
        self.assertEqual(inst.content[0].attachment.size, 3654)
        self.assertEqual(force_bytes(inst.content[0].attachment.title), force_bytes("Physical"))
        self.assertEqual(force_bytes(inst.content[0].attachment.url), force_bytes("http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510"))
        self.assertEqual(force_bytes(inst.content[0].format.code), force_bytes("urn:ihe:pcc:handp:2008"))
        self.assertEqual(force_bytes(inst.content[0].format.display), force_bytes("History and Physical Specification"))
        self.assertEqual(force_bytes(inst.content[0].format.system), force_bytes("urn:oid:1.3.6.1.4.1.19376.1.2.3"))
        self.assertEqual(force_bytes(inst.context.event[0].coding[0].code), force_bytes("T-D8200"))
        self.assertEqual(force_bytes(inst.context.event[0].coding[0].display), force_bytes("Arm"))
        self.assertEqual(force_bytes(inst.context.event[0].coding[0].system), force_bytes("http://ihe.net/xds/connectathon/eventCodes"))
        self.assertEqual(force_bytes(inst.context.facilityType.coding[0].code), force_bytes("Outpatient"))
        self.assertEqual(force_bytes(inst.context.facilityType.coding[0].display), force_bytes("Outpatient"))
        self.assertEqual(force_bytes(inst.context.facilityType.coding[0].system), force_bytes("http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes"))
        self.assertEqual(inst.context.period.end.date, FHIRDate("2004-12-23T08:01:00+11:00").date)
        self.assertEqual(inst.context.period.end.as_json(), "2004-12-23T08:01:00+11:00")
        self.assertEqual(inst.context.period.start.date, FHIRDate("2004-12-23T08:00:00+11:00").date)
        self.assertEqual(inst.context.period.start.as_json(), "2004-12-23T08:00:00+11:00")
        self.assertEqual(force_bytes(inst.context.practiceSetting.coding[0].code), force_bytes("General Medicine"))
        self.assertEqual(force_bytes(inst.context.practiceSetting.coding[0].display), force_bytes("General Medicine"))
        self.assertEqual(force_bytes(inst.context.practiceSetting.coding[0].system), force_bytes("http://www.ihe.net/xds/connectathon/practiceSettingCodes"))
        self.assertEqual(inst.date.date, FHIRDate("2005-12-24T09:43:41+11:00").date)
        self.assertEqual(inst.date.as_json(), "2005-12-24T09:43:41+11:00")
        self.assertEqual(force_bytes(inst.description), force_bytes("Physical"))
        self.assertEqual(force_bytes(inst.docStatus), force_bytes("preliminary"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"))
        self.assertEqual(force_bytes(inst.masterIdentifier.system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.masterIdentifier.value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.relatesTo[0].code), force_bytes("appends"))
        self.assertEqual(force_bytes(inst.securityLabel[0].coding[0].code), force_bytes("V"))
        self.assertEqual(force_bytes(inst.securityLabel[0].coding[0].display), force_bytes("very restricted"))
        self.assertEqual(force_bytes(inst.securityLabel[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-Confidentiality"))
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("34108-1"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Outpatient Note"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org"))

