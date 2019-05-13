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
from .. import chargeitemdefinition
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ChargeItemDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ChargeItemDefinition", js["resourceType"])
        return chargeitemdefinition.ChargeItemDefinition(js)
    
    def testChargeItemDefinition1(self):
        inst = self.instantiate_from("chargeitemdefinition-device-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ChargeItemDefinition instance")
        self.implChargeItemDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ChargeItemDefinition", js["resourceType"])
        inst2 = chargeitemdefinition.ChargeItemDefinition(js)
        self.implChargeItemDefinition1(inst2)
    
    def implChargeItemDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.applicability[0].description), force_bytes("Verify ChargeItem pertains to Device 12345"))
        self.assertEqual(force_bytes(inst.applicability[0].expression), force_bytes("%context.service.suppliedItem='Device/12345'"))
        self.assertEqual(force_bytes(inst.applicability[0].language), force_bytes("text/fhirpath"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Financial details for  custom made device"))
        self.assertEqual(force_bytes(inst.id), force_bytes("device"))
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[0].amount.currency), force_bytes("EUR"))
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.value, 67.44)
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[0].code.coding[0].code), force_bytes("VK"))
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[0].code.coding[0].display), force_bytes("Verkaufspreis (netto)"))
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[0].code.coding[0].system), force_bytes("http://fhir.de/CodeSystem/billing-attributes"))
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[0].type), force_bytes("base"))
        self.assertEqual(force_bytes(inst.propertyGroup[1].applicability[0].description), force_bytes("Gültigkeit Steuersatz"))
        self.assertEqual(force_bytes(inst.propertyGroup[1].applicability[0].expression), force_bytes("%context.occurenceDateTime > '2018-04-01'"))
        self.assertEqual(force_bytes(inst.propertyGroup[1].applicability[0].language), force_bytes("text/fhirpath"))
        self.assertEqual(force_bytes(inst.propertyGroup[1].priceComponent[0].code.coding[0].code), force_bytes("MWST"))
        self.assertEqual(force_bytes(inst.propertyGroup[1].priceComponent[0].code.coding[0].display), force_bytes("Mehrwersteuersatz"))
        self.assertEqual(force_bytes(inst.propertyGroup[1].priceComponent[0].code.coding[0].system), force_bytes("http://fhir.de/CodeSystem/billing-attributes"))
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].factor, 1.19)
        self.assertEqual(force_bytes(inst.propertyGroup[1].priceComponent[0].type), force_bytes("tax"))
        self.assertEqual(force_bytes(inst.propertyGroup[2].applicability[0].description), force_bytes("Gültigkeit Steuersatz"))
        self.assertEqual(force_bytes(inst.propertyGroup[2].applicability[0].expression), force_bytes("%context.occurenceDateTime <= '2018-04-01'"))
        self.assertEqual(force_bytes(inst.propertyGroup[2].applicability[0].language), force_bytes("text/fhirpath"))
        self.assertEqual(force_bytes(inst.propertyGroup[2].priceComponent[0].code.coding[0].code), force_bytes("MWST"))
        self.assertEqual(force_bytes(inst.propertyGroup[2].priceComponent[0].code.coding[0].display), force_bytes("Mehrwersteuersatz"))
        self.assertEqual(force_bytes(inst.propertyGroup[2].priceComponent[0].code.coding[0].system), force_bytes("http://fhir.de/CodeSystem/billing-attributes"))
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].factor, 1.07)
        self.assertEqual(force_bytes(inst.propertyGroup[2].priceComponent[0].type), force_bytes("tax"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://sap.org/ChargeItemDefinition/device-123"))
    
    def testChargeItemDefinition2(self):
        inst = self.instantiate_from("chargeitemdefinition-ebm-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ChargeItemDefinition instance")
        self.implChargeItemDefinition2(inst)
        
        js = inst.as_json()
        self.assertEqual("ChargeItemDefinition", js["resourceType"])
        inst2 = chargeitemdefinition.ChargeItemDefinition(js)
        self.implChargeItemDefinition2(inst2)
    
    def implChargeItemDefinition2(self, inst):
        self.assertEqual(force_bytes(inst.applicability[0].description), force_bytes("Excludes billing code 13250 for same Encounter"))
        self.assertEqual(force_bytes(inst.applicability[0].expression), force_bytes("[some CQL expression]"))
        self.assertEqual(force_bytes(inst.applicability[0].language), force_bytes("text/cql"))
        self.assertEqual(force_bytes(inst.applicability[1].description), force_bytes("Applies only once per Encounter"))
        self.assertEqual(force_bytes(inst.applicability[1].expression), force_bytes("[some CQL expression]"))
        self.assertEqual(force_bytes(inst.applicability[1].language), force_bytes("text/CQL"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("30110"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Allergologiediagnostik I"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://fhir.de/CodingSystem/kbv/ebm"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Allergologisch-diagnostischer Komplex zur Diagnostik und/oder zum Ausschluss einer (Kontakt-)Allergie vom Spättyp (Typ IV), einschl. Kosten"))
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2018-06-30").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2018-06-30")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2018-04-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2018-04-01")
        self.assertEqual(force_bytes(inst.id), force_bytes("ebm"))
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[0].amount.currency), force_bytes("EUR"))
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.value, 67.44)
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[0].code.coding[0].code), force_bytes("gesamt-euro"))
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[0].code.coding[0].display), force_bytes("Gesamt (Euro)"))
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[0].code.coding[0].system), force_bytes("http://fhir.de/CodeSystem/kbv/ebm-attribute"))
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[0].type), force_bytes("base"))
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[1].code.coding[0].code), force_bytes("gesamt-punkte"))
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[1].code.coding[0].display), force_bytes("Gesamt (Punkte)"))
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[1].code.coding[0].system), force_bytes("http://fhir.de/CodeSystem/kbv/ebm-attribute"))
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].factor, 633)
        self.assertEqual(force_bytes(inst.propertyGroup[0].priceComponent[1].type), force_bytes("informational"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://fhir.de/ChargeItemDefinition/kbv/ebm-30110"))
        self.assertEqual(force_bytes(inst.version), force_bytes("2-2018"))

