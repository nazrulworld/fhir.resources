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
from .. import paymentnotice
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class PaymentNoticeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PaymentNotice", js["resourceType"])
        return paymentnotice.PaymentNotice(js)
    
    def testPaymentNotice1(self):
        inst = self.instantiate_from("paymentnotice-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PaymentNotice instance")
        self.implPaymentNotice1(inst)
        
        js = inst.as_json()
        self.assertEqual("PaymentNotice", js["resourceType"])
        inst2 = paymentnotice.PaymentNotice(js)
        self.implPaymentNotice1(inst2)
    
    def implPaymentNotice1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("77654"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://benefitsinc.com/paymentnotice"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("776543"))
        self.assertEqual(force_bytes(inst.paymentStatus.coding[0].code), force_bytes("paid"))
        self.assertEqual(force_bytes(inst.paymentStatus.coding[0].system), force_bytes("http://hl7.org/fhir/paymentstatus"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(inst.statusDate.date, FHIRDate("2014-08-15").date)
        self.assertEqual(inst.statusDate.as_json(), "2014-08-15")
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the PaymentNotice</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

