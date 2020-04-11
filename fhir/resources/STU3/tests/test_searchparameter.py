# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SearchParameter
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""

import io
import json
import os
import sys
import unittest

import pytest

from .. import searchparameter
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class SearchParameterTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("SearchParameter", js["resourceType"])
            if "base" not in js:
                raise ValueError("Required `base` attribute doesnt found! ")
        return searchparameter.SearchParameter(js)

    def testSearchParameter1(self):
        try:
            inst = self.instantiate_from("valueset-extensions-ValueSet-workflow.json")
        except ValueError as exc:
            sys.stderr.write(str(exc) + "\n")
            return 1
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter1(inst)

        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter1(inst2)

    def implSearchParameter1(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("workflow"))
        self.assertEqual(
            force_bytes(inst.description), force_bytes("Optional Extensions Element")
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("valueset-extensions-ValueSet-workflow")
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("workflow"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.type), force_bytes("token"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/valueset-extensions-ValueSet-workflow"
            ),
        )
        self.assertEqual(
            force_bytes(inst.xpath),
            force_bytes(
                "f:ValueSet/f:extension[@url='http://hl7.org/fhir/StructureDefinition/valueset-workflowStatus'] | /f:#workflowStatus"
            ),
        )
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))

    def testSearchParameter2(self):
        try:
            inst = self.instantiate_from("codesystem-extensions-CodeSystem-author.json")
        except ValueError as exc:
            sys.stderr.write(str(exc) + "\n")
            return 1
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter2(inst)

        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter2(inst2)

    def implSearchParameter2(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("author"))
        self.assertEqual(
            force_bytes(inst.description), force_bytes("Optional Extensions Element")
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("codesystem-extensions-CodeSystem-author")
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("author"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.type), force_bytes("string"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/codesystem-extensions-CodeSystem-author"
            ),
        )
        self.assertEqual(
            force_bytes(inst.xpath),
            force_bytes(
                "f:CodeSystem/f:extension[@url='http://hl7.org/fhir/StructureDefinition/codesystem-author'] | /f:#author"
            ),
        )
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))

    def testSearchParameter3(self):
        inst = self.instantiate_from("searchparameter-example-extension.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter3(inst)

        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter3(inst2)

    def implSearchParameter3(self, inst):
        self.assertEqual(force_bytes(inst.base[0]), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.code), force_bytes("part-agree"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "Search by url for a participation agreement, which is stored in a DocumentReference"
            ),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.expression),
            force_bytes(
                "DocumentReference.extension('http://example.org/fhir/StructureDefinition/participation-agreement')"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example-extension"))
        self.assertEqual(
            force_bytes(inst.name),
            force_bytes("Example Search Parameter on an extension"),
        )
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes("Health Level Seven International (FHIR Infrastructure)"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.target[0]), force_bytes("DocumentReference"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("reference"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/SearchParameter/example-extension"),
        )
        self.assertEqual(
            force_bytes(inst.xpath),
            force_bytes(
                "f:DocumentReference/f:extension[@url='http://example.org/fhir/StructureDefinition/participation-agreement']"
            ),
        )
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))

    def testSearchParameter4(self):
        inst = self.instantiate_from("condition-extensions-Condition-part-of.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter4(inst)

        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter4(inst2)

    def implSearchParameter4(self, inst):
        self.assertEqual(force_bytes(inst.base[0]), force_bytes("Condition"))
        self.assertEqual(force_bytes(inst.code), force_bytes("part-of"))
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Matches on the partOf extension value"),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("condition-extensions-Condition-part-of")
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("part-of"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.type), force_bytes("reference"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/condition-extensions-Condition-part-of"
            ),
        )
        self.assertEqual(
            force_bytes(inst.xpath),
            force_bytes(
                "f:Condition/f:extension[@url='http://hl7.org/fhir/StructureDefinition/condition-partOf'] | f:Condition/f:extension[@url='http://hl7.org/fhir/StructureDefinition/condition-partOf']"
            ),
        )
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))

    def testSearchParameter5(self):
        inst = self.instantiate_from("condition-extensions-Condition-definition.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter5(inst)

        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter5(inst2)

    def implSearchParameter5(self, inst):
        self.assertEqual(force_bytes(inst.base[0]), force_bytes("Condition"))
        self.assertEqual(force_bytes(inst.code), force_bytes("definition"))
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Matches on the definition extension value"),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id),
            force_bytes("condition-extensions-Condition-definition"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("definition"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.type), force_bytes("reference"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/condition-extensions-Condition-definition"
            ),
        )
        self.assertEqual(
            force_bytes(inst.xpath),
            force_bytes(
                "f:Condition/f:extension[@url='http://hl7.org/fhir/StructureDefinition/condition-definition'] | f:Condition/f:extension[@url='http://hl7.org/fhir/StructureDefinition/condition-definition']"
            ),
        )
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))

    def testSearchParameter6(self):
        inst = self.instantiate_from("searchparameter-example-reference.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter6(inst)

        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter6(inst2)

    def implSearchParameter6(self, inst):
        self.assertEqual(force_bytes(inst.base[0]), force_bytes("Condition"))
        self.assertEqual(force_bytes(inst.chain[0]), force_bytes("name"))
        self.assertEqual(force_bytes(inst.chain[1]), force_bytes("identifier"))
        self.assertEqual(force_bytes(inst.code), force_bytes("subject"))
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("[string]"))
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("url")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value),
            force_bytes("http://hl7.org/fhir"),
        )
        self.assertEqual(inst.date.date, FHIRDate("2013-10-23").date)
        self.assertEqual(inst.date.as_json(), "2013-10-23")
        self.assertEqual(
            force_bytes(inst.description), force_bytes("Search by condition subject")
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.expression), force_bytes("Condition.subject"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-reference"))
        self.assertEqual(force_bytes(inst.modifier[0]), force_bytes("missing"))
        self.assertEqual(
            force_bytes(inst.name), force_bytes("Example Search Parameter")
        )
        self.assertEqual(
            force_bytes(inst.publisher),
            force_bytes("Health Level Seven International (FHIR Infrastructure)"),
        )
        self.assertEqual(
            force_bytes(inst.purpose),
            force_bytes("Need to search Condition by subject"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.target[0]), force_bytes("Organization"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("reference"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes("http://hl7.org/fhir/SearchParameter/example"),
        )
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))

    def testSearchParameter7(self):
        try:
            inst = self.instantiate_from(
                "organization-extensions-Organization-alias.json"
            )
        except ValueError as exc:
            sys.stderr.write(str(exc) + "\n")
            return 1
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter7(inst)

        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter7(inst2)

    def implSearchParameter7(self, inst):
        self.assertEqual(force_bytes(inst.code), force_bytes("alias"))
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Include Organizations that contain the provided alias"),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id),
            force_bytes("organization-extensions-Organization-alias"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("alias"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.type), force_bytes("string"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/organization-extensions-Organization-alias"
            ),
        )
        self.assertEqual(
            force_bytes(inst.xpath),
            force_bytes(
                "f:Organization/f:extension[@url='http://hl7.org/fhir/StructureDefinition/organization-alias'] | /f:#alias"
            ),
        )
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))

    def testSearchParameter8(self):
        inst = self.instantiate_from(
            "elementdefinition-11179-DataElement-objectClass.json"
        )
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter8(inst)

        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter8(inst2)

    def implSearchParameter8(self, inst):
        self.assertEqual(force_bytes(inst.base[0]), force_bytes("DataElement"))
        self.assertEqual(force_bytes(inst.code), force_bytes("objectClass"))
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Matches on the 11179-objectClass extension value"),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id),
            force_bytes("elementdefinition-11179-DataElement-objectClass"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("objectClass"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.type), force_bytes("token"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/elementdefinition-11179-DataElement-objectClass"
            ),
        )
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))

    def testSearchParameter9(self):
        inst = self.instantiate_from(
            "diagnosticreport-genetic-DiagnosticReport-assessed-condition.json"
        )
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter9(inst)

        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter9(inst2)

    def implSearchParameter9(self, inst):
        self.assertEqual(force_bytes(inst.base[0]), force_bytes("DiagnosticReport"))
        self.assertEqual(force_bytes(inst.code), force_bytes("assessed-condition"))
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("Condition assessed by genetic test"),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id),
            force_bytes("diagnosticreport-genetic-DiagnosticReport-assessed-condition"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("assessed-condition"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.type), force_bytes("reference"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/diagnosticreport-genetic-DiagnosticReport-assessed-condition"
            ),
        )
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))

    def testSearchParameter10(self):
        try:
            inst = self.instantiate_from("device-extensions-Device-din.json")
        except ValueError as exc:
            sys.stderr.write(str(exc) + "\n")
            return 1
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter10(inst)

        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter10(inst2)

    def implSearchParameter10(self, inst):
        self.assertEqual(force_bytes(inst.base[0]), force_bytes("Device"))
        self.assertEqual(force_bytes(inst.code), force_bytes("din"))
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes("The donation identification number (DIN)"),
        )
        self.assertTrue(inst.experimental)
        self.assertEqual(
            force_bytes(inst.id), force_bytes("device-extensions-Device-din")
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("din"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.type), force_bytes("token"))
        self.assertEqual(
            force_bytes(inst.url),
            force_bytes(
                "http://hl7.org/fhir/SearchParameter/device-extensions-Device-din"
            ),
        )
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))
