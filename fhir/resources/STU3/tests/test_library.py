#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-05-13.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import library
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class LibraryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Library", js["resourceType"])
        return library.Library(js)
    
    def testLibrary1(self):
        inst = self.instantiate_from("library-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary1(inst)
        
        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary1(inst2)
    
    def implLibrary1(self, inst):
        self.assertEqual(force_bytes(inst.content[0].contentType), force_bytes("text/cql"))
        self.assertEqual(force_bytes(inst.content[0].url), force_bytes("library-example-content.cql"))
        self.assertEqual(force_bytes(inst.dataRequirement[0].codeFilter[0].path), force_bytes("code"))
        self.assertEqual(force_bytes(inst.dataRequirement[0].codeFilter[0].valueSetString), force_bytes("Other Female Reproductive Conditions"))
        self.assertEqual(force_bytes(inst.dataRequirement[0].type), force_bytes("Condition"))
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(force_bytes(inst.description), force_bytes("Common Logic for adherence to Chlamydia Screening guidelines"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("ChalmydiaScreening_Common"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].type), force_bytes("depends-on"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Chlamydia Screening Common Library"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("Chlamydia Screening"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("logic-library"))
        self.assertEqual(force_bytes(inst.version), force_bytes("2.0.0"))
    
    def testLibrary2(self):
        inst = self.instantiate_from("library-composition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary2(inst)
        
        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary2(inst2)
    
    def implLibrary2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2017-03-10").date)
        self.assertEqual(inst.date.as_json(), "2017-03-10")
        self.assertEqual(force_bytes(inst.description), force_bytes("Artifacts required for implementation of Zika Virus Management"))
        self.assertEqual(force_bytes(inst.id), force_bytes("composition-example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("Zika Artifacts"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].type), force_bytes("composed-of"))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].type), force_bytes("composed-of"))
        self.assertEqual(force_bytes(inst.relatedArtifact[2].type), force_bytes("composed-of"))
        self.assertEqual(force_bytes(inst.relatedArtifact[3].type), force_bytes("composed-of"))
        self.assertEqual(force_bytes(inst.relatedArtifact[4].type), force_bytes("composed-of"))
        self.assertEqual(force_bytes(inst.relatedArtifact[5].type), force_bytes("composed-of"))
        self.assertEqual(force_bytes(inst.relatedArtifact[6].type), force_bytes("derived-from"))
        self.assertEqual(force_bytes(inst.relatedArtifact[6].url), force_bytes("https://www.cdc.gov/mmwr/volumes/65/wr/mm6539e1.htm?s_cid=mm6539e1_w"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Zika Artifacts"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("Zika Virus Management"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("asset-collection"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))
    
    def testLibrary3(self):
        inst = self.instantiate_from("library-cms146-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary3(inst)
        
        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary3(inst2)
    
    def implLibrary3(self, inst):
        self.assertEqual(force_bytes(inst.content[0].contentType), force_bytes("text/cql"))
        self.assertEqual(force_bytes(inst.content[0].url), force_bytes("library-cms146-example-content.cql"))
        self.assertEqual(force_bytes(inst.dataRequirement[0].type), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.dataRequirement[1].codeFilter[0].path), force_bytes("category"))
        self.assertEqual(force_bytes(inst.dataRequirement[1].codeFilter[0].valueCode[0]), force_bytes("diagnosis"))
        self.assertEqual(force_bytes(inst.dataRequirement[1].codeFilter[1].path), force_bytes("clinicalStatus"))
        self.assertEqual(force_bytes(inst.dataRequirement[1].codeFilter[1].valueCode[0]), force_bytes("confirmed"))
        self.assertEqual(force_bytes(inst.dataRequirement[1].codeFilter[2].path), force_bytes("code"))
        self.assertEqual(force_bytes(inst.dataRequirement[1].codeFilter[2].valueSetString), force_bytes("2.16.840.1.113883.3.464.1003.102.12.1011"))
        self.assertEqual(force_bytes(inst.dataRequirement[1].type), force_bytes("Condition"))
        self.assertEqual(force_bytes(inst.dataRequirement[2].codeFilter[0].path), force_bytes("category"))
        self.assertEqual(force_bytes(inst.dataRequirement[2].codeFilter[0].valueCode[0]), force_bytes("diagnosis"))
        self.assertEqual(force_bytes(inst.dataRequirement[2].codeFilter[1].path), force_bytes("clinicalStatus"))
        self.assertEqual(force_bytes(inst.dataRequirement[2].codeFilter[1].valueCode[0]), force_bytes("confirmed"))
        self.assertEqual(force_bytes(inst.dataRequirement[2].codeFilter[2].path), force_bytes("code"))
        self.assertEqual(force_bytes(inst.dataRequirement[2].codeFilter[2].valueSetString), force_bytes("2.16.840.1.113883.3.464.1003.102.12.1012"))
        self.assertEqual(force_bytes(inst.dataRequirement[2].type), force_bytes("Condition"))
        self.assertEqual(force_bytes(inst.dataRequirement[3].codeFilter[0].path), force_bytes("status"))
        self.assertEqual(force_bytes(inst.dataRequirement[3].codeFilter[0].valueCode[0]), force_bytes("finished"))
        self.assertEqual(force_bytes(inst.dataRequirement[3].codeFilter[1].path), force_bytes("class"))
        self.assertEqual(force_bytes(inst.dataRequirement[3].codeFilter[1].valueCode[0]), force_bytes("ambulatory"))
        self.assertEqual(force_bytes(inst.dataRequirement[3].codeFilter[2].path), force_bytes("type"))
        self.assertEqual(force_bytes(inst.dataRequirement[3].codeFilter[2].valueSetString), force_bytes("2.16.840.1.113883.3.464.1003.101.12.1061"))
        self.assertEqual(force_bytes(inst.dataRequirement[3].type), force_bytes("Encounter"))
        self.assertEqual(force_bytes(inst.dataRequirement[4].codeFilter[0].path), force_bytes("diagnosis"))
        self.assertEqual(force_bytes(inst.dataRequirement[4].codeFilter[0].valueSetString), force_bytes("2.16.840.1.113883.3.464.1003.198.12.1012"))
        self.assertEqual(force_bytes(inst.dataRequirement[4].type), force_bytes("DiagnosticReport"))
        self.assertEqual(force_bytes(inst.dataRequirement[5].codeFilter[0].path), force_bytes("code"))
        self.assertEqual(force_bytes(inst.dataRequirement[5].codeFilter[0].valueSetString), force_bytes("2.16.840.1.113883.3.464.1003.196.12.1001"))
        self.assertEqual(force_bytes(inst.dataRequirement[5].type), force_bytes("Medication"))
        self.assertEqual(force_bytes(inst.dataRequirement[6].codeFilter[0].path), force_bytes("status"))
        self.assertEqual(force_bytes(inst.dataRequirement[6].codeFilter[0].valueCode[0]), force_bytes("active"))
        self.assertEqual(force_bytes(inst.dataRequirement[6].codeFilter[1].path), force_bytes("medication.code"))
        self.assertEqual(force_bytes(inst.dataRequirement[6].codeFilter[1].valueSetString), force_bytes("2.16.840.1.113883.3.464.1003.196.12.1001"))
        self.assertEqual(force_bytes(inst.dataRequirement[6].type), force_bytes("MedicationRequest"))
        self.assertEqual(force_bytes(inst.dataRequirement[7].codeFilter[0].path), force_bytes("status"))
        self.assertEqual(force_bytes(inst.dataRequirement[7].codeFilter[0].valueCode[0]), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.dataRequirement[7].codeFilter[1].path), force_bytes("medication.code"))
        self.assertEqual(force_bytes(inst.dataRequirement[7].codeFilter[1].valueSetString), force_bytes("2.16.840.1.113883.3.464.1003.196.12.1001"))
        self.assertEqual(force_bytes(inst.dataRequirement[7].type), force_bytes("MedicationStatement"))
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(force_bytes(inst.description), force_bytes("Logic for CMS 146: Appropriate Testing for Children with Pharyngitis"))
        self.assertEqual(force_bytes(inst.id), force_bytes("library-cms146-example"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("CMS146"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].type), force_bytes("depends-on"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Appropriate Testing for Children with Pharyngitis"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("logic-library"))
        self.assertEqual(force_bytes(inst.version), force_bytes("2.0.0"))
    
    def testLibrary4(self):
        inst = self.instantiate_from("library-predecessor-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary4(inst)
        
        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary4(inst2)
    
    def implLibrary4(self, inst):
        self.assertEqual(force_bytes(inst.content[0].contentType), force_bytes("text/cql"))
        self.assertEqual(force_bytes(inst.content[0].title), force_bytes("FHIR Helpers"))
        self.assertEqual(force_bytes(inst.content[0].url), force_bytes("library-fhir-helpers-content.cql"))
        self.assertEqual(inst.date.date, FHIRDate("2016-11-14").date)
        self.assertEqual(inst.date.as_json(), "2016-11-14")
        self.assertEqual(force_bytes(inst.description), force_bytes("FHIR Helpers"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("library-fhir-helpers-predecessor"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("FHIRHelpers"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].type), force_bytes("depends-on"))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].type), force_bytes("successor"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("FHIR Helpers"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("FHIR Helpers"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("logic-library"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1.6"))

