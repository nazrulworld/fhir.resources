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
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("ONC"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://www.healthit.gov"))
        self.assertEqual(force_bytes(inst.contact[1].name), force_bytes("HL7"))
        self.assertEqual(force_bytes(inst.contact[1].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[1].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(force_bytes(inst.copyright), force_bytes("Published by ONC under the standard FHIR license (CC0)"))
        self.assertEqual(inst.date.date, FHIRDate("2015-01-01").date)
        self.assertEqual(inst.date.as_json(), "2015-01-01")
        self.assertEqual(force_bytes(inst.definition.grouping[0].description), force_bytes("Base package (not broken up into multiple packages)"))
        self.assertEqual(force_bytes(inst.definition.grouping[0].name), force_bytes("test"))
        self.assertEqual(force_bytes(inst.definition.page.generation), force_bytes("html"))
        self.assertEqual(force_bytes(inst.definition.page.nameUrl), force_bytes("patient-example.html"))
        self.assertEqual(force_bytes(inst.definition.page.page[0].generation), force_bytes("html"))
        self.assertEqual(force_bytes(inst.definition.page.page[0].nameUrl), force_bytes("list.html"))
        self.assertEqual(force_bytes(inst.definition.page.page[0].title), force_bytes("Value Set Page"))
        self.assertEqual(force_bytes(inst.definition.page.title), force_bytes("Example Patient Page"))
        self.assertEqual(force_bytes(inst.definition.parameter[0].code), force_bytes("apply"))
        self.assertEqual(force_bytes(inst.definition.parameter[0].value), force_bytes("version"))
        self.assertEqual(force_bytes(inst.definition.resource[0].description), force_bytes("A test example to show how an implementation guide works"))
        self.assertEqual(force_bytes(inst.definition.resource[0].exampleCanonical), force_bytes("http://hl7.org/fhir/us/core/StructureDefinition/patient"))
        self.assertEqual(force_bytes(inst.definition.resource[0].name), force_bytes("Test Example"))
        self.assertEqual(force_bytes(inst.dependsOn[0].uri), force_bytes("http://hl7.org/fhir/ImplementationGuide/uscore"))
        self.assertFalse(inst.experimental)
        self.assertEqual(force_bytes(inst.fhirVersion[0]), force_bytes("4.0.0"))
        self.assertEqual(force_bytes(inst.global_fhir[0].profile), force_bytes("http://hl7.org/fhir/us/core/StructureDefinition/patient"))
        self.assertEqual(force_bytes(inst.global_fhir[0].type), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.license), force_bytes("CC0-1.0"))
        self.assertEqual(force_bytes(inst.manifest.image[0]), force_bytes("fhir.png"))
        self.assertEqual(force_bytes(inst.manifest.other[0]), force_bytes("fhir.css"))
        self.assertEqual(force_bytes(inst.manifest.page[0].anchor[0]), force_bytes("patient-test"))
        self.assertEqual(force_bytes(inst.manifest.page[0].anchor[1]), force_bytes("tx"))
        self.assertEqual(force_bytes(inst.manifest.page[0].anchor[2]), force_bytes("uml"))
        self.assertEqual(force_bytes(inst.manifest.page[0].name), force_bytes("patient-test.html"))
        self.assertEqual(force_bytes(inst.manifest.page[0].title), force_bytes("Test Patient Example"))
        self.assertEqual(force_bytes(inst.manifest.rendering), force_bytes("http://hl7.org/fhir/us/daf"))
        self.assertEqual(force_bytes(inst.manifest.resource[0].exampleCanonical), force_bytes("http://hl7.org/fhir/us/core/StructureDefinition/patient"))
        self.assertEqual(force_bytes(inst.manifest.resource[0].relativePath), force_bytes("patient-test.html#patient-test"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Data Access Framework (DAF)"))
        self.assertEqual(force_bytes(inst.packageId), force_bytes("hl7.fhir.us.daf"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("ONC / HL7 Joint project"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/us/daf"))
        self.assertEqual(force_bytes(inst.version), force_bytes("0"))

