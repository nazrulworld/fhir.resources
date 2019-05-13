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
from .. import chargeitem
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ChargeItemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ChargeItem", js["resourceType"])
        return chargeitem.ChargeItem(js)
    
    def testChargeItem1(self):
        inst = self.instantiate_from("chargeitem-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ChargeItem instance")
        self.implChargeItem1(inst)
        
        js = inst.as_json()
        self.assertEqual("ChargeItem", js["resourceType"])
        inst2 = chargeitem.ChargeItem(js)
        self.implChargeItem1(inst2)
    
    def implChargeItem1(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("01510"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Zusatzpauschale für Beobachtung nach diagnostischer Koronarangiografie"))
        self.assertEqual(force_bytes(inst.definitionUri[0]), force_bytes("http://www.kbv.de/tools/ebm/html/01520_2904360860826220813632.html"))
        self.assertEqual(inst.enteredDate.date, FHIRDate("2017-01-25T23:55:04+01:00").date)
        self.assertEqual(inst.enteredDate.as_json(), "2017-01-25T23:55:04+01:00")
        self.assertEqual(inst.factorOverride, 0.8)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://myHospital.org/ChargeItems"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("654321"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("The code is only applicable for periods longer than 4h"))
        self.assertEqual(inst.note[0].time.date, FHIRDate("2017-01-25T23:55:04+01:00").date)
        self.assertEqual(inst.note[0].time.as_json(), "2017-01-25T23:55:04+01:00")
        self.assertEqual(inst.occurrencePeriod.end.date, FHIRDate("2017-01-25T12:35:00+01:00").date)
        self.assertEqual(inst.occurrencePeriod.end.as_json(), "2017-01-25T12:35:00+01:00")
        self.assertEqual(inst.occurrencePeriod.start.date, FHIRDate("2017-01-25T08:00:00+01:00").date)
        self.assertEqual(inst.occurrencePeriod.start.as_json(), "2017-01-25T08:00:00+01:00")
        self.assertEqual(force_bytes(inst.overrideReason), force_bytes("Patient is Cardiologist's golf buddy, so he gets a 20% discount!"))
        self.assertEqual(force_bytes(inst.performer[0].function.coding[0].code), force_bytes("17561000"))
        self.assertEqual(force_bytes(inst.performer[0].function.coding[0].display), force_bytes("Cardiologist"))
        self.assertEqual(force_bytes(inst.performer[0].function.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.performer[1].function.coding[0].code), force_bytes("224542009"))
        self.assertEqual(force_bytes(inst.performer[1].function.coding[0].display), force_bytes("Coronary Care Nurse"))
        self.assertEqual(force_bytes(inst.performer[1].function.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.priceOverride.currency), force_bytes("EUR"))
        self.assertEqual(inst.priceOverride.value, 40)
        self.assertEqual(inst.quantity.value, 1)
        self.assertEqual(force_bytes(inst.reason[0].coding[0].code), force_bytes("123456"))
        self.assertEqual(force_bytes(inst.reason[0].coding[0].display), force_bytes("DIAG-1"))
        self.assertEqual(force_bytes(inst.reason[0].coding[0].system), force_bytes("http://hl7.org/fhir/sid/icd-10"))
        self.assertEqual(force_bytes(inst.status), force_bytes("billable"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Example of ChargeItem Usage in Context of the German EBM Billing code system</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

