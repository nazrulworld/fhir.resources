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
from .. import substance
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class SubstanceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Substance", js["resourceType"])
        return substance.Substance(js)
    
    def testSubstance1(self):
        inst = self.instantiate_from("substance-example-f201-dust.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance1(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance1(inst2)
    
    def implSubstance1(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("406466009"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("House dust allergen"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f201"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testSubstance2(self):
        inst = self.instantiate_from("substance-example-f203-potassium.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance2(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance2(inst2)
    
    def implSubstance2(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("chemical"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Chemical"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/substance-category"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("88480006"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Potassium"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f203"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://acme.org/identifiers/substances"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("1234"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testSubstance3(self):
        inst = self.instantiate_from("substance-example-f202-staphylococcus.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance3(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance3(inst2)
    
    def implSubstance3(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("3092008"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Staphylococcus Aureus"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f202"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testSubstance4(self):
        inst = self.instantiate_from("substance-example-silver-nitrate-product.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance4(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance4(inst2)
    
    def implSubstance4(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("chemical"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Chemical"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/substance-category"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("333346007"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Silver nitrate 20% solution (product)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Solution for silver nitrate stain"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f204"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://acme.org/identifiers/substances"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("15970"))
        self.assertEqual(inst.instance[0].expiry.date, FHIRDate("2018-01-01").date)
        self.assertEqual(inst.instance[0].expiry.as_json(), "2018-01-01")
        self.assertEqual(force_bytes(inst.instance[0].identifier.system), force_bytes("http://acme.org/identifiers/substances/lot"))
        self.assertEqual(force_bytes(inst.instance[0].identifier.value), force_bytes("AB94687"))
        self.assertEqual(force_bytes(inst.instance[0].quantity.code), force_bytes("mL"))
        self.assertEqual(force_bytes(inst.instance[0].quantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.instance[0].quantity.unit), force_bytes("mL"))
        self.assertEqual(inst.instance[0].quantity.value, 100)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testSubstance5(self):
        inst = self.instantiate_from("substance-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance5(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance5(inst2)
    
    def implSubstance5(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("allergen"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Allergen"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/substance-category"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("apitoxin (Honey Bee Venom)"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://acme.org/identifiers/substances"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("1463"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testSubstance6(self):
        inst = self.instantiate_from("substance-example-amoxicillin-clavulanate.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance6(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance6(inst2)
    
    def implSubstance6(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("drug"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Drug or Medicament"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/substance-category"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("392259005"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Amoxicillin + clavulanate potassium 875mg/125mg tablet (product)"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("ingr1"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("ingr2"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Augmentin 875"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f205"))
        self.assertEqual(force_bytes(inst.ingredient[0].quantity.denominator.code), force_bytes("mg"))
        self.assertEqual(force_bytes(inst.ingredient[0].quantity.denominator.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.ingredient[0].quantity.denominator.unit), force_bytes("mg"))
        self.assertEqual(inst.ingredient[0].quantity.denominator.value, 1000)
        self.assertEqual(force_bytes(inst.ingredient[0].quantity.numerator.code), force_bytes("mg"))
        self.assertEqual(force_bytes(inst.ingredient[0].quantity.numerator.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.ingredient[0].quantity.numerator.unit), force_bytes("mg"))
        self.assertEqual(inst.ingredient[0].quantity.numerator.value, 875)
        self.assertEqual(force_bytes(inst.ingredient[1].quantity.denominator.code), force_bytes("mg"))
        self.assertEqual(force_bytes(inst.ingredient[1].quantity.denominator.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.ingredient[1].quantity.denominator.unit), force_bytes("mg"))
        self.assertEqual(inst.ingredient[1].quantity.denominator.value, 1000)
        self.assertEqual(force_bytes(inst.ingredient[1].quantity.numerator.code), force_bytes("mg"))
        self.assertEqual(force_bytes(inst.ingredient[1].quantity.numerator.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.ingredient[1].quantity.numerator.unit), force_bytes("mg"))
        self.assertEqual(inst.ingredient[1].quantity.numerator.value, 125)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

