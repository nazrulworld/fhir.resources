#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-13.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import searchparameter
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class SearchParameterTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SearchParameter", js["resourceType"])
        return searchparameter.SearchParameter(js)
    
    def testSearchParameter1(self):
        inst = self.instantiate_from("searchparameter-example-extension.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter1(inst)
        
        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter1(inst2)
    
    def implSearchParameter1(self, inst):
        self.assertEqual(force_bytes(inst.base[0]), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.code), force_bytes("part-agree"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Search by url for a participation agreement, which is stored in a DocumentReference"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.expression), force_bytes("DocumentReference.extension('http://example.org/fhir/StructureDefinition/participation-agreement')"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-extension"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Example Search Parameter on an extension"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Health Level Seven International (FHIR Infrastructure)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.target[0]), force_bytes("DocumentReference"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("reference"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/SearchParameter/example-extension"))
        self.assertEqual(force_bytes(inst.xpath), force_bytes("f:DocumentReference/f:extension[@url='http://example.org/fhir/StructureDefinition/participation-agreement']"))
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))
    
    def testSearchParameter2(self):
        inst = self.instantiate_from("searchparameter-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter2(inst)
        
        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter2(inst2)
    
    def implSearchParameter2(self, inst):
        self.assertEqual(force_bytes(inst.base[0]), force_bytes("Resource"))
        self.assertEqual(force_bytes(inst.code), force_bytes("_id"))
        self.assertEqual(force_bytes(inst.comparator[0]), force_bytes("eq"))
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("[string]"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(inst.date.date, FHIRDate("2013-10-23").date)
        self.assertEqual(inst.date.as_json(), "2013-10-23")
        self.assertEqual(force_bytes(inst.derivedFrom), force_bytes("http://hl7.org/fhir/SearchParameter/Resource-id"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Search by resource identifier - e.g. same as the read interaction, but can return included resources"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.expression), force_bytes("id"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].display), force_bytes("United States of America (the)"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.name), force_bytes("ID-SEARCH-PARAMETER"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Health Level Seven International (FHIR Infrastructure)"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Need to search by identifier for various infrastructural cases - mainly retrieving packages, and matching as part of a chain"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("token"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/SearchParameter/example"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code), force_bytes("positive"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/variant-state"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1"))
        self.assertEqual(force_bytes(inst.xpath), force_bytes("f:*/f:id"))
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))
    
    def testSearchParameter3(self):
        inst = self.instantiate_from("searchparameter-example-reference.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter3(inst)
        
        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter3(inst2)
    
    def implSearchParameter3(self, inst):
        self.assertEqual(force_bytes(inst.base[0]), force_bytes("Condition"))
        self.assertEqual(force_bytes(inst.chain[0]), force_bytes("name"))
        self.assertEqual(force_bytes(inst.chain[1]), force_bytes("identifier"))
        self.assertEqual(force_bytes(inst.code), force_bytes("subject"))
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("[string]"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(inst.date.date, FHIRDate("2013-10-23").date)
        self.assertEqual(inst.date.as_json(), "2013-10-23")
        self.assertEqual(force_bytes(inst.description), force_bytes("Search by condition subject"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.expression), force_bytes("Condition.subject"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-reference"))
        self.assertEqual(force_bytes(inst.modifier[0]), force_bytes("missing"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Example Search Parameter"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Health Level Seven International (FHIR Infrastructure)"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Need to search Condition by subject"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.target[0]), force_bytes("Organization"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("reference"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/SearchParameter/example-reference"))
        self.assertEqual(force_bytes(inst.xpathUsage), force_bytes("normal"))

