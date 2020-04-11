# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
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

from .. import researchsubject
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ResearchSubjectTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ResearchSubject", js["resourceType"])
        return researchsubject.ResearchSubject(js)

    def testResearchSubject1(self):
        inst = self.instantiate_from("researchsubject-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ResearchSubject instance")
        self.implResearchSubject1(inst)

        js = inst.as_json()
        self.assertEqual("ResearchSubject", js["resourceType"])
        inst2 = researchsubject.ResearchSubject(js)
        self.implResearchSubject1(inst2)

    def implResearchSubject1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.identifier.system),
            force_bytes("http://example.org/studysubjectids"),
        )
        self.assertEqual(
            force_bytes(inst.identifier.type.text), force_bytes("Subject id")
        )
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("123"))
        self.assertEqual(force_bytes(inst.status), force_bytes("candidate"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering here]</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
