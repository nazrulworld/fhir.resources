# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/StructureMap
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

from .. import structuremap
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class StructureMapTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("StructureMap", js["resourceType"])
        return structuremap.StructureMap(js)

    def testStructureMap1(self):
        inst = self.instantiate_from("structuremap-supplyrequest-transform.json")
        self.assertIsNotNone(inst, "Must have instantiated a StructureMap instance")
        self.implStructureMap1(inst)

        js = inst.as_json()
        self.assertEqual("StructureMap", js["resourceType"])
        inst2 = structuremap.StructureMap(js)
        self.implStructureMap1(inst2)

    def implStructureMap1(self, inst):
        self.assertEqual(
            force_bytes(inst.group[0].input[0].mode), force_bytes("source")
        )
        self.assertEqual(
            force_bytes(inst.group[0].input[0].name), force_bytes("source")
        )
        self.assertEqual(
            force_bytes(inst.group[0].input[0].type), force_bytes("ActivityDefinition")
        )
        self.assertEqual(
            force_bytes(inst.group[0].input[1].mode), force_bytes("target")
        )
        self.assertEqual(
            force_bytes(inst.group[0].input[1].name), force_bytes("target")
        )
        self.assertEqual(
            force_bytes(inst.group[0].input[1].type), force_bytes("SupplyRequest")
        )
        self.assertEqual(force_bytes(inst.group[0].name), force_bytes("main"))
        self.assertEqual(force_bytes(inst.group[0].rule[0].name), force_bytes("status"))
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].source[0].context), force_bytes("source")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].source[0].element), force_bytes("id")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].source[0].variable), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].target[0].context), force_bytes("target")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].target[0].contextType),
            force_bytes("variable"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].target[0].element), force_bytes("status")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].target[0].parameter[0].valueString),
            force_bytes("'draft'"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].target[0].transform),
            force_bytes("evaluate"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[1].name), force_bytes("category")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[1].source[0].context), force_bytes("source")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[1].source[0].element), force_bytes("id")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[1].source[0].variable), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[1].target[0].context), force_bytes("target")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[1].target[0].contextType),
            force_bytes("variable"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[1].target[0].element),
            force_bytes("category"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[1].target[0].parameter[0].valueString),
            force_bytes("'non-stock'"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[1].target[0].transform),
            force_bytes("evaluate"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[2].name), force_bytes("priority")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[2].source[0].context), force_bytes("source")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[2].source[0].element), force_bytes("id")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[2].source[0].variable), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[2].target[0].context), force_bytes("target")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[2].target[0].contextType),
            force_bytes("variable"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[2].target[0].element),
            force_bytes("priority"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[2].target[0].parameter[0].valueString),
            force_bytes("'routine'"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[2].target[0].transform),
            force_bytes("evaluate"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[3].name), force_bytes("quantity")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[3].source[0].context), force_bytes("source")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[3].source[0].element),
            force_bytes("quantity"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[3].source[0].variable), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[3].target[0].context), force_bytes("target")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[3].target[0].contextType),
            force_bytes("variable"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[3].target[0].element),
            force_bytes("category"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[3].target[0].transform), force_bytes("copy")
        )
        self.assertEqual(force_bytes(inst.group[0].rule[4].name), force_bytes("item"))
        self.assertEqual(
            force_bytes(inst.group[0].rule[4].source[0].context), force_bytes("source")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[4].source[0].element), force_bytes("code")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[4].source[0].variable), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[4].target[0].context), force_bytes("target")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[4].target[0].contextType),
            force_bytes("variable"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[4].target[0].element),
            force_bytes("orderedItem.itemCodeableConcept"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[4].target[0].transform), force_bytes("copy")
        )
        self.assertEqual(force_bytes(inst.group[0].rule[5].name), force_bytes("when"))
        self.assertEqual(
            force_bytes(inst.group[0].rule[5].source[0].context), force_bytes("source")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[5].source[0].element), force_bytes("id")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[5].source[0].variable), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[5].target[0].context), force_bytes("target")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[5].target[0].contextType),
            force_bytes("variable"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[5].target[0].element),
            force_bytes("occurrenceDateTime"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[5].target[0].parameter[0].valueString),
            force_bytes("now()"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[5].target[0].transform),
            force_bytes("evaluate"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[6].name), force_bytes("authoredOn")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[6].source[0].context), force_bytes("source")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[6].source[0].element), force_bytes("id")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[6].source[0].variable), force_bytes("a")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[6].target[0].context), force_bytes("target")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[6].target[0].contextType),
            force_bytes("variable"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[6].target[0].element),
            force_bytes("authoredOn"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[6].target[0].parameter[0].valueString),
            force_bytes("now()"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[6].target[0].transform),
            force_bytes("evaluate"),
        )
        self.assertEqual(force_bytes(inst.group[0].typeMode), force_bytes("none"))
        self.assertEqual(force_bytes(inst.id), force_bytes("supplyrequest-transform"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Transform from an ActivityDefinition to a SupplyRequest"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.structure[0].mode), force_bytes("source"))
        self.assertEqual(
            force_bytes(inst.structure[0].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/activitydefinition"),
        )
        self.assertEqual(force_bytes(inst.structure[1].mode), force_bytes("target"))
        self.assertEqual(
            force_bytes(inst.structure[1].url),
            force_bytes("http://hl7.org/fhir/StructureDefinition/supplyrequest"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/StructureMap/supplyrequest-transform"),
        )

    def testStructureMap2(self):
        inst = self.instantiate_from("structuremap-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a StructureMap instance")
        self.implStructureMap2(inst)

        js = inst.as_json()
        self.assertEqual("StructureMap", js["resourceType"])
        inst2 = structuremap.StructureMap(js)
        self.implStructureMap2(inst2)

    def implStructureMap2(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2017-03-09").date)
        self.assertEqual(inst.date.as_json(), "2017-03-09")
        self.assertEqual(
            force_bytes(inst.description), force_bytes("Example Structure Map")
        )
        self.assertEqual(
            force_bytes(inst.group[0].documentation), force_bytes("test -> testValue")
        )
        self.assertEqual(
            force_bytes(inst.group[0].input[0].mode), force_bytes("source")
        )
        self.assertEqual(force_bytes(inst.group[0].input[0].name), force_bytes("test"))
        self.assertEqual(force_bytes(inst.group[0].name), force_bytes("Examples"))
        self.assertEqual(force_bytes(inst.group[0].rule[0].name), force_bytes("rule1"))
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].source[0].context), force_bytes("Source")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].source[0].element), force_bytes("test")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].source[0].type),
            force_bytes("SourceClassA"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].source[0].variable), force_bytes("t")
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].target[0].context),
            force_bytes("Destination"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].target[0].contextType),
            force_bytes("variable"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].target[0].element),
            force_bytes("testValue"),
        )
        self.assertEqual(
            force_bytes(inst.group[0].rule[0].target[0].transform), force_bytes("copy")
        )
        self.assertEqual(force_bytes(inst.group[0].typeMode), force_bytes("none"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes("urn:oid:37843577-95fb-4adb-84c0-8837188a7bf3"),
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("009")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].display), force_bytes("Oceania")
        )
        self.assertEqual(
            force_bytes(inst.jurisdiction[0].coding[0].system),
            force_bytes("http://unstats.un.org/unsd/methods/m49/m49.htm"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("ExampleMap"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7 FHIR Standard"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Example Map"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/StructureMap/example"),
        )
        self.assertEqual(force_bytes(inst.version), force_bytes("0.1"))
