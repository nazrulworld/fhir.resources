# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Binary
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
