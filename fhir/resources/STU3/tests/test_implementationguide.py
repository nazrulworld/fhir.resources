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
from .. import implementationguide
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ImplementationGuideTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImplementationGuide", js["resourceType"])
        return implementationguide.ImplementationGuide(js)
    
    def testImplementationGuide1(self):
        inst = self.instantiate_from("implementationguide-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImplementationGuide instance")
        self.implImplementationGuide1(inst)
        
        js = inst.as_json()
        self.assertEqual("ImplementationGuide", js["resourceType"])
        inst2 = implementationguide.ImplementationGuide(js)
        self.implImplementationGuide1(inst2)
    
    def implImplementationGuide1(self, inst):
        self.assertEqual(force_bytes(inst.binary[0]), force_bytes("http://h7.org/fhir/fhir.css"))
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("ONC"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://www.healthit.gov"))
        self.assertEqual(force_bytes(inst.contact[1].name), force_bytes("HL7"))
        self.assertEqual(force_bytes(inst.contact[1].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[1].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(force_bytes(inst.copyright), force_bytes("Published by ONC under the standard FHIR license (CC0)"))
        self.assertEqual(inst.date.date, FHIRDate("2015-01-01").date)
        self.assertEqual(inst.date.as_json(), "2015-01-01")
        self.assertEqual(force_bytes(inst.dependency[0].type), force_bytes("reference"))
        self.assertEqual(force_bytes(inst.dependency[0].uri), force_bytes("http://hl7.org/fhir/ImplementationGuide/uscore"))
        self.assertFalse(inst.experimental)
        self.assertEqual(force_bytes(inst.fhirVersion), force_bytes("1.0.0"))
        self.assertEqual(force_bytes(inst.global_fhir[0].type), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Data Access Framework (DAF)"))
        self.assertEqual(force_bytes(inst.package[0].description), force_bytes("Base package (not broken up into multiple packages)"))
        self.assertEqual(force_bytes(inst.package[0].name), force_bytes("test"))
        self.assertEqual(force_bytes(inst.package[0].resource[0].acronym), force_bytes("daf-tst"))
        self.assertEqual(force_bytes(inst.package[0].resource[0].description), force_bytes("A test example to show how a package works"))
        self.assertTrue(inst.package[0].resource[0].example)
        self.assertEqual(force_bytes(inst.package[0].resource[0].name), force_bytes("Test Example"))
        self.assertEqual(force_bytes(inst.package[0].resource[0].sourceUri), force_bytes("test.html"))
        self.assertEqual(force_bytes(inst.page.kind), force_bytes("page"))
        self.assertEqual(force_bytes(inst.page.page[0].format), force_bytes("text/html"))
        self.assertEqual(force_bytes(inst.page.page[0].kind), force_bytes("list"))
        self.assertEqual(force_bytes(inst.page.page[0].package[0]), force_bytes("test"))
        self.assertEqual(force_bytes(inst.page.page[0].source), force_bytes("list.html"))
        self.assertEqual(force_bytes(inst.page.page[0].title), force_bytes("Value Set Page"))
        self.assertEqual(force_bytes(inst.page.page[0].type[0]), force_bytes("ValueSet"))
        self.assertEqual(force_bytes(inst.page.source), force_bytes("patient-example.html"))
        self.assertEqual(force_bytes(inst.page.title), force_bytes("Example Patient Page"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("ONC / HL7 Joint project"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/us/daf"))
        self.assertEqual(force_bytes(inst.version), force_bytes("0"))

