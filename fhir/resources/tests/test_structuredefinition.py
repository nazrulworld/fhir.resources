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
from .. import structuredefinition
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class StructureDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("StructureDefinition", js["resourceType"])
        return structuredefinition.StructureDefinition(js)
    
    def testStructureDefinition1(self):
        inst = self.instantiate_from("structuredefinition-example-section-library.json")
        self.assertIsNotNone(inst, "Must have instantiated a StructureDefinition instance")
        self.implStructureDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("StructureDefinition", js["resourceType"])
        inst2 = structuredefinition.StructureDefinition(js)
        self.implStructureDefinition1(inst2)
    
    def implStructureDefinition1(self, inst):
        self.assertTrue(inst.abstract)
        self.assertEqual(force_bytes(inst.baseDefinition), force_bytes("http://hl7.org/fhir/StructureDefinition/Composition"))
        self.assertEqual(inst.date.date, FHIRDate("2018-11-05T17:57:00+11:00").date)
        self.assertEqual(inst.date.as_json(), "2018-11-05T17:57:00+11:00")
        self.assertEqual(force_bytes(inst.derivation), force_bytes("constraint"))
        self.assertEqual(force_bytes(inst.differential.element[0].id), force_bytes("Composition"))
        self.assertEqual(force_bytes(inst.differential.element[0].path), force_bytes("Composition"))
        self.assertEqual(force_bytes(inst.differential.element[1].id), force_bytes("Composition.section"))
        self.assertEqual(force_bytes(inst.differential.element[1].path), force_bytes("Composition.section"))
        self.assertEqual(force_bytes(inst.differential.element[1].slicing.description), force_bytes("Slice by .section.code when using this library of sections"))
        self.assertEqual(force_bytes(inst.differential.element[1].slicing.discriminator[0].path), force_bytes("code"))
        self.assertEqual(force_bytes(inst.differential.element[1].slicing.discriminator[0].type), force_bytes("pattern"))
        self.assertTrue(inst.differential.element[1].slicing.ordered)
        self.assertEqual(force_bytes(inst.differential.element[1].slicing.rules), force_bytes("closed"))
        self.assertEqual(force_bytes(inst.differential.element[2].id), force_bytes("Composition.section:procedure"))
        self.assertEqual(force_bytes(inst.differential.element[2].path), force_bytes("Composition.section"))
        self.assertEqual(force_bytes(inst.differential.element[2].sliceName), force_bytes("procedure"))
        self.assertEqual(force_bytes(inst.differential.element[3].fixedString), force_bytes("Procedures Performed"))
        self.assertEqual(force_bytes(inst.differential.element[3].id), force_bytes("Composition.section:procedure.title"))
        self.assertEqual(inst.differential.element[3].min, 1)
        self.assertEqual(force_bytes(inst.differential.element[3].path), force_bytes("Composition.section.title"))
        self.assertEqual(force_bytes(inst.differential.element[4].id), force_bytes("Composition.section:procedure.code"))
        self.assertEqual(inst.differential.element[4].min, 1)
        self.assertEqual(force_bytes(inst.differential.element[4].path), force_bytes("Composition.section.code"))
        self.assertEqual(force_bytes(inst.differential.element[4].patternCodeableConcept.coding[0].code), force_bytes("29554-3"))
        self.assertEqual(force_bytes(inst.differential.element[4].patternCodeableConcept.coding[0].display), force_bytes("Procedure Narrative"))
        self.assertEqual(force_bytes(inst.differential.element[4].patternCodeableConcept.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.differential.element[5].id), force_bytes("Composition.section:medications"))
        self.assertEqual(force_bytes(inst.differential.element[5].path), force_bytes("Composition.section"))
        self.assertEqual(force_bytes(inst.differential.element[5].sliceName), force_bytes("medications"))
        self.assertEqual(force_bytes(inst.differential.element[6].fixedString), force_bytes("Medications Administered"))
        self.assertEqual(force_bytes(inst.differential.element[6].id), force_bytes("Composition.section:medications.title"))
        self.assertEqual(inst.differential.element[6].min, 1)
        self.assertEqual(force_bytes(inst.differential.element[6].path), force_bytes("Composition.section.title"))
        self.assertEqual(force_bytes(inst.differential.element[7].id), force_bytes("Composition.section:medications.code"))
        self.assertEqual(inst.differential.element[7].min, 1)
        self.assertEqual(force_bytes(inst.differential.element[7].path), force_bytes("Composition.section.code"))
        self.assertEqual(force_bytes(inst.differential.element[7].patternCodeableConcept.coding[0].code), force_bytes("29549-3"))
        self.assertEqual(force_bytes(inst.differential.element[7].patternCodeableConcept.coding[0].display), force_bytes("Medication administered Narrative"))
        self.assertEqual(force_bytes(inst.differential.element[7].patternCodeableConcept.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.differential.element[8].id), force_bytes("Composition.section:plan"))
        self.assertEqual(force_bytes(inst.differential.element[8].path), force_bytes("Composition.section"))
        self.assertEqual(force_bytes(inst.differential.element[8].sliceName), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.differential.element[9].fixedString), force_bytes("Discharge Treatment Plan"))
        self.assertEqual(force_bytes(inst.differential.element[9].id), force_bytes("Composition.section:plan.title"))
        self.assertEqual(inst.differential.element[9].min, 1)
        self.assertEqual(force_bytes(inst.differential.element[9].path), force_bytes("Composition.section.title"))
        self.assertFalse(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("example-section-library"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("complex-type"))
        self.assertEqual(force_bytes(inst.name), force_bytes("DocumentSectionLibrary"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Document Section Library (For testing section templates)"))
        self.assertEqual(force_bytes(inst.type), force_bytes("Composition"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/StructureDefinition/example-section-library"))
    
    def testStructureDefinition2(self):
        inst = self.instantiate_from("structuredefinition-example-composition.json")
        self.assertIsNotNone(inst, "Must have instantiated a StructureDefinition instance")
        self.implStructureDefinition2(inst)
        
        js = inst.as_json()
        self.assertEqual("StructureDefinition", js["resourceType"])
        inst2 = structuredefinition.StructureDefinition(js)
        self.implStructureDefinition2(inst2)
    
    def implStructureDefinition2(self, inst):
        self.assertFalse(inst.abstract)
        self.assertEqual(force_bytes(inst.baseDefinition), force_bytes("http://hl7.org/fhir/StructureDefinition/Composition"))
        self.assertEqual(inst.date.date, FHIRDate("2018-11-05T17:47:00+11:00").date)
        self.assertEqual(inst.date.as_json(), "2018-11-05T17:47:00+11:00")
        self.assertEqual(force_bytes(inst.derivation), force_bytes("constraint"))
        self.assertEqual(force_bytes(inst.differential.element[0].id), force_bytes("Composition"))
        self.assertEqual(force_bytes(inst.differential.element[0].path), force_bytes("Composition"))
        self.assertEqual(force_bytes(inst.differential.element[1].id), force_bytes("Composition.section"))
        self.assertEqual(force_bytes(inst.differential.element[1].path), force_bytes("Composition.section"))
        self.assertEqual(force_bytes(inst.differential.element[1].slicing.description), force_bytes("Slice by .section.code"))
        self.assertEqual(force_bytes(inst.differential.element[1].slicing.discriminator[0].path), force_bytes("code"))
        self.assertEqual(force_bytes(inst.differential.element[1].slicing.discriminator[0].type), force_bytes("pattern"))
        self.assertTrue(inst.differential.element[1].slicing.ordered)
        self.assertEqual(force_bytes(inst.differential.element[1].slicing.rules), force_bytes("closed"))
        self.assertEqual(force_bytes(inst.differential.element[2].id), force_bytes("Composition.section:procedure"))
        self.assertEqual(inst.differential.element[2].min, 1)
        self.assertEqual(force_bytes(inst.differential.element[2].path), force_bytes("Composition.section"))
        self.assertEqual(force_bytes(inst.differential.element[2].sliceName), force_bytes("procedure"))
        self.assertEqual(force_bytes(inst.differential.element[2].type[0].code), force_bytes("BackboneElement"))
        self.assertEqual(force_bytes(inst.differential.element[2].type[0].profile[0]), force_bytes("http://hl7.org/fhir/StructureDefinition/document-section-library"))
        self.assertEqual(force_bytes(inst.differential.element[3].id), force_bytes("Composition.section:medications"))
        self.assertEqual(inst.differential.element[3].min, 1)
        self.assertEqual(force_bytes(inst.differential.element[3].path), force_bytes("Composition.section"))
        self.assertEqual(force_bytes(inst.differential.element[3].sliceName), force_bytes("medications"))
        self.assertEqual(force_bytes(inst.differential.element[3].type[0].code), force_bytes("BackboneElement"))
        self.assertEqual(force_bytes(inst.differential.element[3].type[0].profile[0]), force_bytes("http://hl7.org/fhir/StructureDefinition/document-section-library"))
        self.assertEqual(force_bytes(inst.differential.element[4].id), force_bytes("Composition.section:plan"))
        self.assertEqual(inst.differential.element[4].min, 0)
        self.assertEqual(force_bytes(inst.differential.element[4].path), force_bytes("Composition.section"))
        self.assertEqual(force_bytes(inst.differential.element[4].sliceName), force_bytes("plan"))
        self.assertEqual(force_bytes(inst.differential.element[4].type[0].code), force_bytes("BackboneElement"))
        self.assertEqual(force_bytes(inst.differential.element[4].type[0].profile[0]), force_bytes("http://hl7.org/fhir/StructureDefinition/document-section-library"))
        self.assertFalse(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("example-composition"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("complex-type"))
        self.assertEqual(force_bytes(inst.name), force_bytes("DocumentStructure"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Document Structure (For testing section templates)"))
        self.assertEqual(force_bytes(inst.type), force_bytes("Composition"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/StructureDefinition/example-composition"))

