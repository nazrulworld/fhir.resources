# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DocumentManifest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
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
        self.assertEqual(
            force_bytes(inst.content[0].pAttachment.contentType),
            force_bytes("application/pdf"),
        )
        self.assertEqual(
            inst.content[0].pAttachment.creation.date,
            FHIRDate("2010-02-01T11:50:23-05:00").date,
        )
        self.assertEqual(
            inst.content[0].pAttachment.creation.as_json(), "2010-02-01T11:50:23-05:00"
        )
        self.assertEqual(
            force_bytes(inst.content[0].pAttachment.data), force_bytes("SGVsbG8=")
        )
        self.assertEqual(
            force_bytes(inst.content[0].pAttachment.title),
            force_bytes("accident notes 20100201.pdf"),
        )
        self.assertEqual(
            force_bytes(inst.content[1].pAttachment.contentType),
            force_bytes("application/pdf"),
        )
        self.assertEqual(
            inst.content[1].pAttachment.creation.date,
            FHIRDate("2010-02-01T10:57:34+01:00").date,
        )
        self.assertEqual(
            inst.content[1].pAttachment.creation.as_json(), "2010-02-01T10:57:34+01:00"
        )
        self.assertEqual(
            force_bytes(inst.content[1].pAttachment.hash),
            force_bytes("SGVsbG8gdGhlcmU="),
        )
        self.assertEqual(inst.content[1].pAttachment.size, 104274)
        self.assertEqual(
            force_bytes(inst.content[1].pAttachment.url),
            force_bytes("http://happyvalley.com/docs/AB12345"),
        )
        self.assertEqual(inst.created.date, FHIRDate("2014-09-21T11:50:23-05:00").date)
        self.assertEqual(inst.created.as_json(), "2014-09-21T11:50:23-05:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("654789"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://happyvalley.com/supportingdocumentation"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("52345"))
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
