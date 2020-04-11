# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentManifest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import documentmanifest
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class DocumentManifestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
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
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://example.org/documents"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("23425234234-2347")
        )
        self.assertEqual(
            force_bytes(inst.masterIdentifier.system),
            force_bytes("http://example.org/documents"),
        )
        self.assertEqual(
            force_bytes(inst.masterIdentifier.value), force_bytes("23425234234-2346")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.related[0].identifier.system),
            force_bytes("http://example.org/documents"),
        )
        self.assertEqual(
            force_bytes(inst.related[0].identifier.value),
            force_bytes("23425234234-9999"),
        )
        self.assertEqual(
            force_bytes(inst.source),
            force_bytes("urn:oid:1.3.6.1.4.1.21367.2009.1.2.1"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes('<div xmlns="http://www.w3.org/1999/xhtml">Text</div>'),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.type.text), force_bytes("History and Physical")
        )

    def testDocumentManifest2(self):
        inst = self.instantiate_from("documentmanifest-fm-attachment.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentManifest instance")
        self.implDocumentManifest2(inst)

        js = inst.as_json()
        self.assertEqual("DocumentManifest", js["resourceType"])
        inst2 = documentmanifest.DocumentManifest(js)
        self.implDocumentManifest2(inst2)

    def implDocumentManifest2(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("org-1"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("a1"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("a2"))
        self.assertEqual(inst.created.date, FHIRDate("2014-09-21T11:50:23-05:00").date)
        self.assertEqual(inst.created.as_json(), "2014-09-21T11:50:23-05:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("654789"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happyvalley.com/supportingdocumentation"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("52345"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(
            force_bytes(inst.related[0].identifier.system),
            force_bytes("http://happyvalley.com/claim"),
        )
        self.assertEqual(
            force_bytes(inst.related[0].identifier.value), force_bytes("12345")
        )
        self.assertEqual(
            force_bytes(inst.related[1].identifier.system),
            force_bytes("http://www.BenefitsInc.com/fhir/remittance"),
        )
        self.assertEqual(
            force_bytes(inst.related[1].identifier.value), force_bytes("R3500")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("current"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A Financial Management Attachment example</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
