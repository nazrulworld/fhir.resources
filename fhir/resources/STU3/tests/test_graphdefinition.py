# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GraphDefinition
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

from .. import graphdefinition
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class GraphDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("GraphDefinition", js["resourceType"])
        return graphdefinition.GraphDefinition(js)

    def testGraphDefinition1(self):
        inst = self.instantiate_from("graphdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a GraphDefinition instance")
        self.implGraphDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("GraphDefinition", js["resourceType"])
        inst2 = graphdefinition.GraphDefinition(js)
        self.implGraphDefinition1(inst2)

    def implGraphDefinition1(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2015-08-04").date)
        self.assertEqual(inst.date.as_json(), "2015-08-04")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Specify to include list references when generating a document using the $document operation"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.link[0].description), force_bytes("Link to List")
        )
        self.assertEqual(
            force_bytes(inst.link[0].path), force_bytes("Composition.section.entry")
        )
        self.assertEqual(
            force_bytes(inst.link[0].target[0].compartment[0].code),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.link[0].target[0].compartment[0].rule),
            force_bytes("identical"),
        )
        self.assertEqual(
            force_bytes(inst.link[0].target[0].link[0].description),
            force_bytes("Include any list entries"),
        )
        self.assertEqual(
            force_bytes(inst.link[0].target[0].link[0].path),
            force_bytes("List.entry.item"),
        )
        self.assertEqual(
            force_bytes(inst.link[0].target[0].link[0].target[0].compartment[0].code),
            force_bytes("Patient"),
        )
        self.assertEqual(
            force_bytes(inst.link[0].target[0].link[0].target[0].compartment[0].rule),
            force_bytes("identical"),
        )
        self.assertEqual(
            force_bytes(inst.link[0].target[0].link[0].target[0].type),
            force_bytes("Resource"),
        )
        self.assertEqual(force_bytes(inst.link[0].target[0].type), force_bytes("List"))
        self.assertEqual(
            force_bytes(inst.name), force_bytes("Document Generation Template")
        )
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR Project"))
        self.assertEqual(force_bytes(inst.start), force_bytes("Composition"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://h7.org/fhir/GraphDefinition/example"),
        )
