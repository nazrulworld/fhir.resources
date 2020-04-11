# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Linkage
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

from .. import linkage
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class LinkageTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Linkage", js["resourceType"])
        return linkage.Linkage(js)

    def testLinkage1(self):
        inst = self.instantiate_from("linkage-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Linkage instance")
        self.implLinkage1(inst)

        js = inst.as_json()
        self.assertEqual("Linkage", js["resourceType"])
        inst2 = linkage.Linkage(js)
        self.implLinkage1(inst2)

    def implLinkage1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.item[0].type), force_bytes("source"))
        self.assertEqual(force_bytes(inst.item[1].type), force_bytes("alternate"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
