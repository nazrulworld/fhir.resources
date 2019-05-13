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
from .. import documentmanifest
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class DocumentManifestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DocumentManifest", js["resourceType"])
        return documentmanifest.DocumentManifest(js)
    
    def testDocumentManifest1(self):
        inst = self.instantiate_from("documentmanifest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentManifest instance")
        self.implDocumentManifest1(inst)
        
        js = inst.as_json()
        self.assertEqual("DocumentManifest", js["resourceType"])
        inst2 = documentmanifest.DocumentManifest(js)
        self.implDocumentManifest1(inst2)
    
    def implDocumentManifest1(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("a1"))
        self.assertEqual(inst.created.date, FHIRDate("2004-12-25T23:50:50-05:00").date)
        self.assertEqual(inst.created.as_json(), "2004-12-25T23:50:50-05:00")
        self.assertEqual(force_bytes(inst.description), force_bytes("Physical"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/documents"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("23425234234-2347"))
        self.assertEqual(force_bytes(inst.masterIdentifier.system), force_bytes("http://example.org/documents"))
        self.assertEqual(force_bytes(inst.masterIdentifier.value), force_bytes("23425234234-2346"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.related[0].identifier.system), force_bytes("http://example.org/documents"))
        self.assertEqual(force_bytes(inst.related[0].identifier.value), force_bytes("23425234234-9999"))
        self.assertEqual(force_bytes(inst.source), force_bytes("urn:oid:1.3.6.1.4.1.21367.2009.1.2.1"))
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Text</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.text), force_bytes("History and Physical"))

