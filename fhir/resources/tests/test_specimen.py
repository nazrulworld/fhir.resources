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
from .. import specimen
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class SpecimenTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Specimen", js["resourceType"])
        return specimen.Specimen(js)
    
    def testSpecimen1(self):
        inst = self.instantiate_from("specimen-example-serum.json")
        self.assertIsNotNone(inst, "Must have instantiated a Specimen instance")
        self.implSpecimen1(inst)
        
        js = inst.as_json()
        self.assertEqual("Specimen", js["resourceType"])
        inst2 = specimen.Specimen(js)
        self.implSpecimen1(inst2)
    
    def implSpecimen1(self, inst):
        self.assertEqual(force_bytes(inst.accessionIdentifier.system), force_bytes("http://acme.com/labs/accession-ids"))
        self.assertEqual(force_bytes(inst.accessionIdentifier.value), force_bytes("20150816-00124"))
        self.assertEqual(inst.collection.collectedDateTime.date, FHIRDate("2015-08-16T06:40:17Z").date)
        self.assertEqual(inst.collection.collectedDateTime.as_json(), "2015-08-16T06:40:17Z")
        self.assertEqual(force_bytes(inst.container[0].type.coding[0].code), force_bytes("SST"))
        self.assertEqual(force_bytes(inst.container[0].type.coding[0].display), force_bytes("Serum Separator Tube"))
        self.assertEqual(force_bytes(inst.container[0].type.coding[0].system), force_bytes("http://acme.com/labs"))
        self.assertEqual(force_bytes(inst.id), force_bytes("sst"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("119364003"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Serum sample"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://snomed.info/sct"))
    
    def testSpecimen2(self):
        inst = self.instantiate_from("specimen-example-pooled-serum.json")
        self.assertIsNotNone(inst, "Must have instantiated a Specimen instance")
        self.implSpecimen2(inst)
        
        js = inst.as_json()
        self.assertEqual("Specimen", js["resourceType"])
        inst2 = specimen.Specimen(js)
        self.implSpecimen2(inst2)
    
    def implSpecimen2(self, inst):
        self.assertEqual(force_bytes(inst.accessionIdentifier.system), force_bytes("https://vetmed.iastate.edu/vdl"))
        self.assertEqual(force_bytes(inst.accessionIdentifier.value), force_bytes("20171120-1234"))
        self.assertEqual(inst.collection.collectedDateTime.date, FHIRDate("2017-11-14").date)
        self.assertEqual(inst.collection.collectedDateTime.as_json(), "2017-11-14")
        self.assertEqual(force_bytes(inst.container[0].type.coding[0].code), force_bytes("RTT"))
        self.assertEqual(force_bytes(inst.container[0].type.coding[0].display), force_bytes("Red Top Tube"))
        self.assertEqual(force_bytes(inst.container[0].type.coding[0].system), force_bytes("https://vetmed.iastate.edu/vdl"))
        self.assertEqual(force_bytes(inst.container[0].type.text), force_bytes("Red Top Blood Collection Tube"))
        self.assertEqual(force_bytes(inst.id), force_bytes("pooled-serum"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Pooled serum sample from 30 individuals"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("Serum sample, pooled"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Serum sample, pooled"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("https://vetmed.iastate.edu/vdl"))
        self.assertEqual(force_bytes(inst.type.text), force_bytes("Pooled serum sample"))
    
    def testSpecimen3(self):
        inst = self.instantiate_from("specimen-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Specimen instance")
        self.implSpecimen3(inst)
        
        js = inst.as_json()
        self.assertEqual("Specimen", js["resourceType"])
        inst2 = specimen.Specimen(js)
        self.implSpecimen3(inst2)
    
    def implSpecimen3(self, inst):
        self.assertEqual(force_bytes(inst.accessionIdentifier.system), force_bytes("http://lab.acme.org/specimens/2011"))
        self.assertEqual(force_bytes(inst.accessionIdentifier.value), force_bytes("X352356"))
        self.assertEqual(force_bytes(inst.collection.bodySite.coding[0].code), force_bytes("49852007"))
        self.assertEqual(force_bytes(inst.collection.bodySite.coding[0].display), force_bytes("Structure of median cubital vein (body structure)"))
        self.assertEqual(force_bytes(inst.collection.bodySite.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.collection.bodySite.text), force_bytes("Right median cubital vein"))
        self.assertEqual(inst.collection.collectedDateTime.date, FHIRDate("2011-05-30T06:15:00Z").date)
        self.assertEqual(inst.collection.collectedDateTime.as_json(), "2011-05-30T06:15:00Z")
        self.assertEqual(force_bytes(inst.collection.method.coding[0].code), force_bytes("LNV"))
        self.assertEqual(force_bytes(inst.collection.method.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0488"))
        self.assertEqual(force_bytes(inst.collection.quantity.unit), force_bytes("mL"))
        self.assertEqual(inst.collection.quantity.value, 6)
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("hep"))
        self.assertEqual(force_bytes(inst.container[0].capacity.unit), force_bytes("mL"))
        self.assertEqual(inst.container[0].capacity.value, 10)
        self.assertEqual(force_bytes(inst.container[0].description), force_bytes("Green Gel tube"))
        self.assertEqual(force_bytes(inst.container[0].identifier[0].value), force_bytes("48736-15394-75465"))
        self.assertEqual(force_bytes(inst.container[0].specimenQuantity.unit), force_bytes("mL"))
        self.assertEqual(inst.container[0].specimenQuantity.value, 6)
        self.assertEqual(force_bytes(inst.container[0].type.text), force_bytes("Vacutainer"))
        self.assertEqual(force_bytes(inst.id), force_bytes("101"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://ehr.acme.org/identifiers/collections"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("23234352356"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Specimen is grossly lipemic"))
        self.assertEqual(inst.receivedTime.date, FHIRDate("2011-03-04T07:03:00Z").date)
        self.assertEqual(inst.receivedTime.as_json(), "2011-03-04T07:03:00Z")
        self.assertEqual(force_bytes(inst.status), force_bytes("available"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("122555007"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Venous blood specimen"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://snomed.info/sct"))
    
    def testSpecimen4(self):
        inst = self.instantiate_from("specimen-example-urine.json")
        self.assertIsNotNone(inst, "Must have instantiated a Specimen instance")
        self.implSpecimen4(inst)
        
        js = inst.as_json()
        self.assertEqual("Specimen", js["resourceType"])
        inst2 = specimen.Specimen(js)
        self.implSpecimen4(inst2)
    
    def implSpecimen4(self, inst):
        self.assertEqual(force_bytes(inst.accessionIdentifier.system), force_bytes("http://lab.acme.org/specimens/2015"))
        self.assertEqual(force_bytes(inst.accessionIdentifier.value), force_bytes("X352356"))
        self.assertEqual(inst.collection.collectedDateTime.date, FHIRDate("2015-08-18T07:03:00Z").date)
        self.assertEqual(inst.collection.collectedDateTime.as_json(), "2015-08-18T07:03:00Z")
        self.assertEqual(force_bytes(inst.container[0].capacity.unit), force_bytes("mls"))
        self.assertEqual(inst.container[0].capacity.value, 50)
        self.assertEqual(force_bytes(inst.container[0].specimenQuantity.unit), force_bytes("mls"))
        self.assertEqual(inst.container[0].specimenQuantity.value, 10)
        self.assertEqual(force_bytes(inst.container[0].type.text), force_bytes("Non-sterile specimen container"))
        self.assertEqual(force_bytes(inst.id), force_bytes("vma-urine"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.processing[0].description), force_bytes("Acidify to pH < 3.0 with 6 N HCl."))
        self.assertEqual(force_bytes(inst.processing[0].procedure.coding[0].code), force_bytes("ACID"))
        self.assertEqual(force_bytes(inst.processing[0].procedure.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0373"))
        self.assertEqual(inst.processing[0].timeDateTime.date, FHIRDate("2015-08-18T08:10:00Z").date)
        self.assertEqual(inst.processing[0].timeDateTime.as_json(), "2015-08-18T08:10:00Z")
        self.assertEqual(inst.receivedTime.date, FHIRDate("2015-08-18T07:03:00Z").date)
        self.assertEqual(inst.receivedTime.as_json(), "2015-08-18T07:03:00Z")
        self.assertEqual(force_bytes(inst.status), force_bytes("available"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("RANDU"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Urine, Random"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0487"))
    
    def testSpecimen5(self):
        inst = self.instantiate_from("specimen-example-isolate.json")
        self.assertIsNotNone(inst, "Must have instantiated a Specimen instance")
        self.implSpecimen5(inst)
        
        js = inst.as_json()
        self.assertEqual("Specimen", js["resourceType"])
        inst2 = specimen.Specimen(js)
        self.implSpecimen5(inst2)
    
    def implSpecimen5(self, inst):
        self.assertEqual(force_bytes(inst.accessionIdentifier.system), force_bytes("http://lab.acme.org/specimens/2011"))
        self.assertEqual(force_bytes(inst.accessionIdentifier.value), force_bytes("X352356-ISO1"))
        self.assertEqual(inst.collection.collectedDateTime.date, FHIRDate("2015-08-16T07:03:00Z").date)
        self.assertEqual(inst.collection.collectedDateTime.as_json(), "2015-08-16T07:03:00Z")
        self.assertEqual(force_bytes(inst.collection.method.coding[0].code), force_bytes("BAP"))
        self.assertEqual(force_bytes(inst.collection.method.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0488"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("stool"))
        self.assertEqual(force_bytes(inst.id), force_bytes("isolate"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Patient dropped off specimen"))
        self.assertEqual(inst.receivedTime.date, FHIRDate("2015-08-18T07:03:00Z").date)
        self.assertEqual(inst.receivedTime.as_json(), "2015-08-18T07:03:00Z")
        self.assertEqual(force_bytes(inst.status), force_bytes("available"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("429951000124103"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Bacterial isolate specimen"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://snomed.info/sct"))

