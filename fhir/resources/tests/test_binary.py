# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Binary
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

from .. import binary
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class BinaryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Binary", js["resourceType"])
        return binary.Binary(js)

    def testBinary1(self):
        inst = self.instantiate_from("binary-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Binary instance")
        self.implBinary1(inst)

        js = inst.as_json()
        self.assertEqual("Binary", js["resourceType"])
        inst2 = binary.Binary(js)
        self.implBinary1(inst2)

    def implBinary1(self, inst):
        self.assertEqual(force_bytes(inst.contentType), force_bytes("application/pdf"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )

    def testBinary2(self):
        inst = self.instantiate_from("binary-f006.json")
        self.assertIsNotNone(inst, "Must have instantiated a Binary instance")
        self.implBinary2(inst)

        js = inst.as_json()
        self.assertEqual("Binary", js["resourceType"])
        inst2 = binary.Binary(js)
        self.implBinary2(inst2)

    def implBinary2(self, inst):
        self.assertEqual(force_bytes(inst.contentType), force_bytes("image/jpeg"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f006"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
