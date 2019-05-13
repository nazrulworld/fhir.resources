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
from .. import invoice
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class InvoiceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Invoice", js["resourceType"])
        return invoice.Invoice(js)
    
    def testInvoice1(self):
        inst = self.instantiate_from("invoice-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Invoice instance")
        self.implInvoice1(inst)
        
        js = inst.as_json()
        self.assertEqual("Invoice", js["resourceType"])
        inst2 = invoice.Invoice(js)
        self.implInvoice1(inst2)
    
    def implInvoice1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2017-01-25T08:00:00+01:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-25T08:00:00+01:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://myHospital.org/Invoices"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("654321"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.participant[0].role.coding[0].code), force_bytes("17561000"))
        self.assertEqual(force_bytes(inst.participant[0].role.coding[0].display), force_bytes("Cardiologist"))
        self.assertEqual(force_bytes(inst.participant[0].role.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.status), force_bytes("issued"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Example of Invoice</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.totalGross.currency), force_bytes("EUR"))
        self.assertEqual(inst.totalGross.value, 48)
        self.assertEqual(force_bytes(inst.totalNet.currency), force_bytes("EUR"))
        self.assertEqual(inst.totalNet.value, 40)

